"""
Application logic for data_provider service
"""
import os
import asyncio
import logging
import random
import pymongo
import logging
import time

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastiot.core import FastIoTService, Subject, subscribe, loop
from fastiot.core.core_uuid import get_uuid
from fastiot.core.time import get_time_now
from fastiot.msg.thing import Thing
# from fastiot_core_services.object_storage.mongodb_handler import MongoDBHandler
from starlette.middleware.cors import CORSMiddleware
from fastiot.env import env_mongodb
from fastiot.util.read_yaml import read_config

from mvdp_services.data_provider.env import env_data_provider
from mvdp_services.data_provider.uvicorn_server import UvicornAsyncServer


class DataProviderService(FastIoTService):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # TODO: connect pipe input with a database, output with EDC
        """
        self._mongodb_handler = MongoDBHandler()
        database = self._mongodb_handler.get_database(env_mongodb.name)
        """

        # maybe load asset from the database (db queries: Asset_x -> [column1, column2, ...])
        service_config = read_config(self)
        if not service_config:
            self._logger.error('Please set the assets config as shown in the documentation! Aborting service!')
            time.sleep(10)
            raise RuntimeError
        self.assets, mongo_indices = self._parse_config(service_config)
        # self._create_index(mongo_indices)

        self.app = FastAPI()
        self._register_routes()
        self.server = UvicornAsyncServer(self.app, port=env_data_provider.fastapi_port)

        self.message_received = asyncio.Event()
        self.last_msg = None

    def _register_routes(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origin_regex='.*/assets/Asset_.*',
            allow_credentials=True,
            allow_methods=['GET'],
            allow_headers=["*"],
        )
        self.app.get("/assets/Asset_{asset_id}")(self._handle_get)

        # no mounting apps at first
        """
        try:
            self.app.mount("/",
                           StaticFiles(directory=os.path.join(os.path.dirname(__file__), "vue", "dist"),
                                       html=True),
                           name="static")
        except RuntimeError:
            pass
        """


    def _parse_config(self, config):
        mongo_indices = config.get('search_index', [])
        assets = {}
        for attr, content in config.items():
            if attr.startswith('Asset_'):
                assets[attr] = content.split(" ")
        return assets, mongo_indices

    def _create_index(self, mongo_indices):
        for index in mongo_indices:
            if "," in index:  # Build compound index
                indices = index.split(",")
                indices = [i.strip() for i in indices]
                compound_index = list(zip(indices,
                                          map(lambda index_name:
                                              pymongo.ASCENDING if index_name != '_timestamp' else pymongo.DESCENDING,
                                              indices)))
                # the later the _timestamp in mongo_data - the more time relevant query results
                self._logger.debug(compound_index)
                self._mongodb_handler.create_index(collection=self._mongo_object_db_col,
                                                   index_name="compound_index",
                                                   index=compound_index)
            else:
                self._mongodb_handler.create_index(collection=self._mongo_object_db_col,
                                                   index=[(index, pymongo.ASCENDING)],
                                                   index_name=f"{index}_ascending")



    async def _start(self):
        """ Methods to start once the module is initialized """
        await self.server.up()

    async def _stop(self):
        """ Methods to call on module shutdown """
        await self.server.down()

    async def _handle_get(self, asset_id: str):
       return asset_id

    """
    @loop
    async def produce(self):
        # Creating some dummy data and publish it 
        sensor_name = f'my_sensor_{random.randint(1, 5)}'
        value = random.randint(20, 30)
        subject = Thing.get_subject(sensor_name)
        await self.broker_connection.publish(
            subject=subject,
            msg=Thing(
                name=sensor_name,
                machine='FastIoT_Example_Machine',
                measurement_id=get_uuid(),
                value=value,
                timestamp=get_time_now()
            )
        )
        self._logger.info("Published %d on sensor %s", value, subject.name)
        return asyncio.sleep(2)

    @subscribe(subject=Thing.get_subject('*'))
    async def consume(self, topic: str, msg: Thing):
        # Subscribing to `Thing.*` messages 
        self._logger.info("%s: %s", topic, str(msg))
    """


if __name__ == '__main__':
    # Change this to reduce verbosity or remove completely to use `FASTIOT_LOG_LEVEL` environment variable to configure
    # logging.
    logging.basicConfig(level=logging.DEBUG)
    DataProviderService.main()
