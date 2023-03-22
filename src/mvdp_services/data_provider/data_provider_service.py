"""
Application logic for data_provider service
"""
import asyncio
import logging
import time
from typing import List

import pandas as pd

from fastapi import FastAPI, HTTPException
from fastiot.core import FastIoTService
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
        self.mongo_db_client = get_mongodb_client_from_env()
        database = self.mongo_db_client.get_database(env_mongodb.name)
        # potentially load asset from the database (db queries: Asset_x -> [column1, column2, ...])
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
        self.app.get("/assets/{asset_name}")(self._handle_get)
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

    async def _start(self):
        """ Methods to start once the module is initialized """
        await self.server.up()

    async def _stop(self):
        """ Methods to call on module shutdown """
        await self.server.down()

    def _handle_get(self, asset_name: str):
        if asset_name not in list(self.assets.keys()):
            raise HTTPException(status_code=500, detail='Asset not configured!')
        query = {"name": {"$in": self.assets[asset_name]}}
        result = self.mongodb_col.find(query)  # create list of things
        things = list(map(from_mongo_data, result))
        rows = self._things_to_rows(things)
        data_frame = pd.DataFrame.from_records(rows)
        self._logger.debug('\n' + str(data_frame))
        return data_frame.to_json()

    @ staticmethod
    def _things_to_rows(things: List):
        # empty list (exception state)
        if not things:
            return []
        # (timestamp, measurement_id) identifies row; make things order row by row
        things.sort(key=lambda th: (th['timestamp'], th['measurement_id']))
        rows = []
        # possibly columns from different tables (otherwise only check index instead of key)
        # init helper variables for the first list element
        key_now = (things[0]['timestamp'], things[0]['measurement_id'])
        row_now = {'Timestamp': things[0]['timestamp'],
                   'Material_ID': things[0]['measurement_id']}
        for ind, thing in enumerate(things):
            thing_key = (thing['timestamp'], thing['measurement_id'])
            if thing_key != key_now:  # this thing is from new row
                rows.append(row_now)  # push previous row
                row_now = {'Timestamp': thing['timestamp'],
                           'Material_ID': thing['measurement_id']}  # init current row
                key_now = thing_key  # set current key_now
            row_now[thing['name']] = str(thing['value']) + ' ' + str(thing['unit'])  # create new table cell
        rows.append(row_now)  # push the last row
        return rows


if __name__ == '__main__':
    # Change this to reduce verbosity or remove completely to use `FASTIOT_LOG_LEVEL` environment variable to configure
    # logging.
    logging.basicConfig(level=logging.DEBUG)
    DataProviderService.main()
