"""
Application logic for data_provider service
"""
import hashlib
import logging
import time
from typing import Type

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import Response, JSONResponse
from fastiot.core import FastIoTService, reply, ReplySubject
from fastiot.db.mongodb_helper_fn import get_mongodb_client_from_env
from fastiot.env import env_mongodb
from fastiot.msg.custom_db_data_type_conversion import from_mongo_data
from fastiot.util.object_helper import parse_object_list
from fastiot.util.read_yaml import read_config
from starlette.middleware.cors import CORSMiddleware

from mvdp.config_model import DataProviderConfiguration, AssetServingTypeEnum
from mvdp.edc_management_client import ApplicationObservabilityApi
from mvdp.edc_management_client.api import AssetApi
from mvdp.edc_management_client.models import AssetCreationRequestDto, AssetEntryDto, DataAddress
from mvdp.edc_management_client.rest import ApiException
from mvdp.env import mvdp_env, MVDP_EDC_HOST
from mvdp.msg import HealthCheckRequest, HealthCheckReply
from mvdp.tools.dataprovider_functions import *
from mvdp.uvicorn_server import UvicornAsyncServer
from mvdp_services.data_provider.api_response_msg import AssetList, AssetShortview
from mvdp_services.data_provider.edc_tools import init_edc
from mvdp_services.data_provider.env import env_data_provider


class DataProviderService(FastIoTService):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # init database
        mongo_db_client = get_mongodb_client_from_env()
        self.database = mongo_db_client.get_database(env_mongodb.name)
        # potentially load asset from the database (db queries: Asset_x -> [column1, column2, ...])
        # read configuration
        service_config = DataProviderConfiguration.from_service(self)
        if not service_config:
            self._logger.error('Please set the config as shown in the documentation! Aborting service!')
            time.sleep(10)
            raise RuntimeError
        self._parse_config(service_config)

        # init FastAPI and server
        self.app = FastAPI(root_path=env_data_provider.base_path)
        self._register_routes()
        self.server = UvicornAsyncServer(self.app, port=env_data_provider.port)

        # init edc
        if mvdp_env.edc_host:
            try:
                self.api_client = init_edc()
                self._edc_put_assets()
            except ApiException:
                self._logger.warn("Could not upload assets to EDC. Trying to continue.")
                # TODO: Retry uploading, maybe we just had a temporary issue with the EDC.
        else:
            self._logger.info("No host for EDC configured with environment variable %s. Not uploading assets.",
                              MVDP_EDC_HOST)

    async def _start(self):
        """ Methods to start once the module is initialized """
        await self.server.up()

    async def _stop(self):
        """ Methods to call on module shutdown """
        await self.server.down()

    def _register_routes(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['GET'],
            allow_headers=["*"],
        )
        self.app.get("/assets")(self._list_assets)
        self.app.get("/assets/{asset_name}")(self._serve_asset)
        # no mounting apps

    def _parse_config(self, config):
        self.assets = config.assets
        for asset in self.assets.values():
            asset.set_constraints(calculate_constraints(asset.constraints))

    def _list_assets(self) -> AssetList:
        """ List all assets configured in the dataspace participant """
        result = {}
        for name, asset_config in self.assets.items():
            columns = asset_config.constraints.get('columns') or ["all available columns"]
            asset_short = AssetShortview(**dict(asset_config))
            asset_short.constraints = {}
            asset_short.set_constraints({})
            asset_short.columns = columns
            result[name] = asset_short

        return AssetList(assets=result)

    @reply(ReplySubject(name="data_provider", msg_cls=HealthCheckRequest, reply_cls=HealthCheckReply))
    async def _health_check_response(self, _: HealthCheckRequest) -> HealthCheckReply:
        health_api_instance = ApplicationObservabilityApi(self.api_client)
        health = health_api_instance.check_health()

        return HealthCheckReply(edc_health=health[0].is_system_healthy)

    def _serve_asset(self, asset_name: str,
                     material_id: list = Query([]),
                     timestamp: list = Query([]),
                     columns: list = Query([]),
                     value: list = Query([]),
                     unit: list = Query([]),
                     machine: list = Query([])) -> Type[Response]:
        """ Receive a single, specified asset.

        Optionally set some limits to filter the provided data.
        """
        if asset_name not in self.assets:
            raise HTTPException(status_code=404, detail='Asset not configured!')

        if self.assets[asset_name].asset_serving_type == AssetServingTypeEnum.thing:
            return self._build_thing_asset(asset_name, material_id, timestamp, columns, value, unit, machine)
        elif self.assets[asset_name].asset_serving_type == AssetServingTypeEnum.json:
            return self._build_json_asset(asset_name)
        else:
            raise HTTPException(status_code=500, detail="Error in asset configuration.")

    def _build_thing_asset(self, asset_name, material_id: list = Query([]),
                     timestamp: list = Query([]),
                     columns: list = Query([]),
                     value: list = Query([]),
                     unit: list = Query([]),
                     machine: list = Query([])) -> Response:
        # TODO: enable one bounded range constraints + certain time ago
        # TODO: enable url interval queries
        # create custom_query
        custom_constraint_object = {
            'machine': machine,
            'measurement_id': material_id,
            'timestamp': timestamp,
            'name': columns,
            'value': value,
            'unit': unit
        }
        custom_constraints = calculate_constraints(custom_constraint_object)
        custom_query = build_query(custom_constraints)
        # create asset_query
        asset_query = build_query(self.assets[asset_name].calculated_constraints_)
        # create data_query (query intersection)
        if custom_query or asset_query:
            data_query = {"$and": [custom_query, asset_query]}
        else:
            data_query = {}
        collection = self.database.get_collection(self.assets[asset_name].asset_collection)
        result = collection.find(data_query)  # create list of things
        result = list(map(from_mongo_data, result))
        things= parse_object_list(result, Thing)  # TODO: Use things instead of dicts
        rows = things_to_rows(things)
        data_frame = pd.DataFrame.from_records(rows)
        # sort columns and log the table
        data_frame = data_frame[list(data_frame.columns.values)[:2] +
                                sorted(list(data_frame.columns.values)[2:])]
        self._logger.debug('\n' + str(data_frame))
        return Response(content=data_frame.to_json(orient="records", date_format="iso", force_ascii=False),
                        media_type='application/json')

    def _build_json_asset(self, asset_name: str) -> JSONResponse:
        collection = self.database.get_collection(self.assets[asset_name].asset_collection)
        result = collection.find({})
        return JSONResponse(content=[r.get('json_data') for r in result])


    def _edc_put_assets(self):
        asset_api_instance = AssetApi(self.api_client)

        for asset_name, asset_body in self.assets.items():
            asset_id = hashlib.md5(asset_name.encode('utf-8')).hexdigest()
            asset_entry = AssetEntryDto(
                asset=AssetCreationRequestDto(
                    id=asset_id,
                    properties={"asset:prop:name": "test", "asset:prop:version": "1.0",
                                "asset:prop:id": "DatasetTest", "asset:prop:contenttype": "text/plain"}),
                data_address=DataAddress(
                    properties={"type": "LocalFile", "address": "/Files/test.txt"})
            )
            # trying to update an existing asset, otherwise create a new asset
            try:
                response = asset_api_instance.update_asset(body=asset_entry, asset_id=asset_id)
            except ApiException:
                response = asset_api_instance.create_asset(body=asset_entry)
            self._logger.debug(response)


if __name__ == '__main__':
    # Change this to reduce verbosity or remove completely to use `FASTIOT_LOG_LEVEL` environment variable to configure
    # logging.
    logging.basicConfig(level=logging.DEBUG)
    DataProviderService.main()
