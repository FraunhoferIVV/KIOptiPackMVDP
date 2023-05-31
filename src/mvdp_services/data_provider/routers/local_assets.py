from typing import Type

from fastapi import APIRouter
from fastapi import HTTPException, Query
from fastapi.responses import Response, JSONResponse
from fastiot.core import FastIoTService
from fastiot.msg.custom_db_data_type_conversion import from_mongo_data
from fastiot.util.object_helper import parse_object_list

from mvdp.config_model import AssetServingTypeEnum
from mvdp.tools.dataprovider_functions import *
from mvdp_services.data_provider.api_response_msg import AssetList, AssetShortview


class LocalAssets:

    def __init__(self, service: Type[FastIoTService]):
        self.router_ = APIRouter()
        self.service = service

        self.router_.get("/")(self._list_local_assets)
        self.router_.get("/{asset_name}")(self._serve_local_asset)

    def _list_local_assets(self) -> AssetList:
        """ List all assets configured in the dataspace participant """
        result = {}
        for name, asset_config in self.service.assets.items():
            columns = asset_config.constraints.get('columns') or ["all available columns"]
            asset_short = AssetShortview(**dict(asset_config))
            asset_short.constraints = {}
            asset_short.set_constraints({})
            asset_short.columns = columns
            result[name] = asset_short

        return AssetList(assets=result)

    def _serve_local_asset(self, asset_name: str,
                           material_id: list = Query([]),
                           timestamp: list = Query([]),
                           columns: list = Query([]),
                           value: list = Query([]),
                           unit: list = Query([]),
                           machine: list = Query([])) -> Type[Response]:
        """ Receive a single, specified asset.

        Optionally set some limits to filter the provided data.
        """
        if asset_name not in self.service.assets:
            raise HTTPException(status_code=404, detail='Asset not configured!')

        if self.service.assets[asset_name].asset_serving_type == AssetServingTypeEnum.thing:
            return self.service._build_thing_asset(asset_name, material_id, timestamp, columns, value, unit, machine)
        elif self.service.assets[asset_name].asset_serving_type == AssetServingTypeEnum.json:
            return self.service._build_json_asset(asset_name)

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
        asset_query = build_query(self.service.assets[asset_name].calculated_constraints_)
        # create data_query (query intersection)
        if custom_query or asset_query:
            data_query = {"$and": [custom_query, asset_query]}
        else:
            data_query = {}
        collection = self.service.database.get_collection(self.service.assets[asset_name].asset_collection)
        result = collection.find(data_query)  # create list of things
        result = list(map(from_mongo_data, result))

        things = parse_object_list(result, Thing)
        rows = things_to_rows(things)
        data_frame = pd.DataFrame.from_records(rows)
        # sort columns and log the table
        data_frame = data_frame[list(data_frame.columns.values)[:2] + sorted(list(data_frame.columns.values)[2:])]

        return Response(content=data_frame.to_json(orient="records", date_format="iso", force_ascii=False),
                        media_type='application/json')

    def _build_json_asset(self, asset_name: str) -> JSONResponse:
        collection = self.service.database.get_collection(self.service.assets[asset_name].asset_collection)
        result = collection.find({})
        return JSONResponse(content=[r.get('json_data') for r in result])
