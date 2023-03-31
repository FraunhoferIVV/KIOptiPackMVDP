"""
Application logic for dataframe_handler service
"""

import asyncio
import logging

import pandas as pd
from fastapi import FastAPI, Form
from fastiot.core import FastIoTService
from fastiot.core.time import get_time_now
from fastiot.msg.thing import Thing
from starlette.middleware.cors import CORSMiddleware

from mvdp.uvicorn_server import UvicornAsyncServer
from mvdp_services.dataframe_handler.TableThing import TableThing
from mvdp_services.dataframe_handler.env import env_dataframe_handler


class DataframeHandlerService(FastIoTService):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app = FastAPI()
        self._register_routes()
        self.server = UvicornAsyncServer(self.app, port=env_dataframe_handler.fastapi_port)

        self.message_received = asyncio.Event()
        self.last_msg = None

        # define machine for this frontend service
        self.machine = "TEST_MACHINE"

    def _register_routes(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["POST"],
            allow_headers=["*"]
        )
        self.app.post("/machine_upload")(self._handle_post)

    async def _start(self):
        """ Methods to start once the module is initialized """
        await self.server.up()

    async def _stop(self):
        """ Methods to call on module shutdown """
        await self.server.down()

    async def _handle_post(self, material_id: str = Form(...),
                           df_type: str = Form(...),
                           content: str = Form(...)):
        dataframe = pd.read_json(content).sort_index()
        self._logger.debug(dataframe)
        await self._send_table_things(material_id, df_type, dataframe)
        return "successfully uploaded"

    async def _send_table_things(self, material_id, df_type, dataframe):
        timestamp_in_table = 'Timestamp' in dataframe
        attributes = [column for column in dataframe
                      if column != 'Timestamp']
        # create table things from table
        for index, row in dataframe.iterrows():
            row = row.to_dict()   # This will make sure, we have python primitives like int and not np.int64
            row_timestamp = get_time_now()
            for attr in attributes:
                if timestamp_in_table:
                    timestamp = row['Timestamp'].to_pydatetime()
                else:
                    timestamp = row_timestamp
                # create table thing
                table_thing = TableThing(machine=self.machine,
                                         name=attr,
                                         measurement_id=material_id,
                                         value=row[attr],
                                         timestamp=timestamp,
                                         df_type=df_type,
                                         df_index=index
                                         )
                # no unit support yet

                await self.broker_connection.publish(subject=Thing.get_subject("DataFrameImporter"),
                                                     msg=table_thing)



if __name__ == '__main__':
    # Change this to reduce verbosity or remove completely to use `FASTIOT_LOG_LEVEL` environment variable to configure
    # logging.
    logging.basicConfig(level=logging.DEBUG)
    DataframeHandlerService.main()
