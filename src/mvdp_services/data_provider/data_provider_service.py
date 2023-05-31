"""
Application logic for data_provider service
"""
import logging

from fastapi import FastAPI
from fastiot.core import FastIoTService, reply, ReplySubject
from fastiot.db.mongodb_helper_fn import get_mongodb_client_from_env
from fastiot.db.redis_helper import get_redis_client
from fastiot.env import env_mongodb
from starlette.middleware.cors import CORSMiddleware

from mvdp.config_model import DataProviderConfiguration
from mvdp.edc_management_client import ApplicationObservabilityApi
from mvdp.edc_management_client.rest import ApiException
from mvdp.env import mvdp_env, MVDP_EDC_HOST
from mvdp.msg import HealthCheckRequest, HealthCheckReply
from mvdp.tools.dataprovider_functions import *
from mvdp.uvicorn_server import UvicornAsyncServer
from mvdp_services.data_provider.edc_tools import init_edc, edc_put_assets
from mvdp_services.data_provider.env import env_data_provider
from mvdp_services.data_provider.routers.edc import EDCCommunication
from mvdp_services.data_provider.routers.local_assets import LocalAssets
from mvdp_services.data_provider.routers.remote_assets import RemoteAssets


class DataProviderService(FastIoTService):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # init database
        mongo_db_client = get_mongodb_client_from_env()
        self.database = mongo_db_client.get_database(env_mongodb.name)
        # potentially load asset from the database (db queries: Asset_x -> [column1, column2, ...])
        # read configuration
        service_config = DataProviderConfiguration.from_service(self)
        self._parse_config(service_config)

        # init FastAPI and server
        self.app = FastAPI(root_path=env_data_provider.base_path)
        self._register_routes()
        self.server = UvicornAsyncServer(self.app, port=env_data_provider.port)

        # init edc
        if mvdp_env.edc_host:
            self._init_edc()
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

        local_assets = LocalAssets(service=self)
        self.app.include_router(local_assets.router_, prefix='/local_assets')

        remote_assets = RemoteAssets(service=self)
        self.app.include_router(remote_assets.router_, prefix='/remote_assets')

        edc = EDCCommunication(service=self)
        self.app.include_router(edc.router_, prefix='/edc')


    def _init_edc(self):
        try:
            self.api_client = init_edc()
            edc_put_assets(api_client=self.api_client, assets=self.assets)
        except ApiException:
            self._logger.warn("Could not upload assets to EDC. Trying to continue.")
            # TODO: Retry uploading, maybe we just had a temporary issue with the EDC.


    def _parse_config(self, config):
        self.assets = config.assets
        for asset in self.assets.values():
            asset.set_constraints(calculate_constraints(asset.constraints))


    @reply(ReplySubject(name="data_provider", msg_cls=HealthCheckRequest, reply_cls=HealthCheckReply))
    async def _health_check_response(self, _: HealthCheckRequest) -> HealthCheckReply:
        health_api_instance = ApplicationObservabilityApi(self.api_client)
        health = health_api_instance.check_health()

        return HealthCheckReply(edc_health=health[0].is_system_healthy)






if __name__ == '__main__':
    # Change this to reduce verbosity or remove completely to use `FASTIOT_LOG_LEVEL` environment variable to configure
    # logging.
    logging.basicConfig(level=logging.DEBUG)
    DataProviderService.main()
