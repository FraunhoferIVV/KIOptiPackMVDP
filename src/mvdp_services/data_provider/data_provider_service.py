"""
Application logic for data_provider service
"""
import asyncio
import logging
import time
from typing import List

import pandas as pd

from fastapi import FastAPI
from fastiot.core import FastIoTService
from fastiot.msg.thing import Thing
from fastiot.db.mongodb_helper_fn import get_mongodb_client_from_env
from fastiot.env import env_mongodb
from fastiot.msg.custom_db_data_type_conversion import from_mongo_data
from fastiot.util.read_yaml import read_config
from starlette.middleware.cors import CORSMiddleware


from mvdp_services.data_provider.env import env_data_provider
from mvdp_services.data_provider.uvicorn_server import UvicornAsyncServer


class DataProviderService(FastIoTService):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # TODO: connect pipe input with a database, output with EDC
        self.mongo_db_client = get_mongodb_client_from_env()
        database = self.mongo_db_client.get_database(env_mongodb.name)
        """
        self._mongodb_handler = MongoDBHandler()
        database = self._mongodb_handler.get_database(env_mongodb.name)
        """
        #  potentially asset from the database (db queries: Asset_x -> [column1, column2, ...])
        service_config = read_config(self)
        if not service_config:
            self._logger.error('Please set the config as shown in the documentation! Aborting service!')
            time.sleep(10)
            raise RuntimeError
        self.mongodb_col = database.get_collection(service_config['collection'])
        self._parse_config(service_config)
        # self._create_index(self.mongo_indices)

        self.app = FastAPI()
        self._register_routes()
        self.server = UvicornAsyncServer(self.app, port=env_data_provider.fastapi_port)

        self.message_received = asyncio.Event()
        self.last_msg = None

    def _register_routes(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
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
        self.mongo_indices = config.get('search_index', [])
        self.assets = {}
        for attr, content in config.items():
            if attr.startswith('Asset_'):
                self.assets[attr] = content.split(", ")

    """
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
    """

    async def _start(self):
        """ Methods to start once the module is initialized """
        await self.server.up()

    async def _stop(self):
        """ Methods to call on module shutdown """
        await self.server.down()

    def _handle_get(self, asset_id: str):
        asset_name = 'Asset_' + asset_id
        query = {"name": {"$in": self.assets[asset_name]}}
        result = self.mongodb_col.find(query)
        # create list of things
        things = list(map(from_mongo_data, result))
        rows = self._things_to_rows(things, asset_name)
        data_frame = pd.DataFrame.from_records(rows)
        self._logger.debug('\n' + str(data_frame))
        return data_frame.to_json()

    def _things_to_rows(self, things: List, asset_name):
        # (timestamp, measurement_id) identifies row
        # sort by (timestamp, measurement_id, name) ascending => row by row, columns sorted
        things.sort(key=lambda thing: (thing['timestamp'], thing['measurement_id'], thing['name']))
        columns = sorted(self.assets[asset_name])
        rows = []
        # possibly columns from different tables
        key_now = (things[0]['timestamp'], things[0]['measurement_id'])
        row_now = {'Timestamp': things[0]['timestamp'],
                   'Material_ID': things[0]['measurement_id']}
        for ind, thing in enumerate(things):
            thing_key = (thing['timestamp'], thing['measurement_id'])
            if thing_key != key_now:  # this thing is from new row
                rows.append(row_now)  # push previous row
                row_now = {'Timestamp': thing['timestamp'],
                           'Material_ID': thing['measurement_id']}
                key_now = thing_key
            row_now[thing['name']] = str(thing['value']) + ' ' + str(thing['unit'])  # create new table cell
        rows.append(row_now)  # push the last row
        return rows




if __name__ == '__main__':
    # Change this to reduce verbosity or remove completely to use `FASTIOT_LOG_LEVEL` environment variable to configure
    # logging.
    logging.basicConfig(level=logging.DEBUG)
    DataProviderService.main()
