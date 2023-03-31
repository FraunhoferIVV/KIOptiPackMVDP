"""
Application logic for frontend service
"""

import asyncio
import logging
import os
import io
import pandas as pd
import json

from typing import Optional

from fastapi import FastAPI, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastiot.core import FastIoTService, subscribe, loop
from fastiot.core.core_uuid import get_uuid
from fastiot.core.time import get_time_now
from fastiot.msg.thing import Thing
from starlette.middleware.cors import CORSMiddleware

from mvdp.uvicorn_server import UvicornAsyncServer
from mvdp_services.frontend.env import env_frontend


class FrontendService(FastIoTService):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app = FastAPI()
        self._register_routes()
        self.server = UvicornAsyncServer(self.app, port=env_frontend.fastapi_port)

        self.message_received = asyncio.Event()
        self.last_msg = None

        # define machine for this frontend service
        self.machine = "TEST_MACHINE"

    def _register_routes(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        self.app.get("/api/get_some_data")(self._handle_get)
        self.app.post("/api/post_some_data")(self._handle_post)
        try:
            self.app.mount("/",
                           StaticFiles(directory=os.path.join(os.path.dirname(__file__), "vue", "dist"),
                                       html=True),
                           name="static")
        except RuntimeError:
            pass

    async def _start(self):
        """ Methods to start once the module is initialized """
        await self.server.up()

    async def _stop(self):
        """ Methods to call on module shutdown """
        await self.server.down()

    """
    Below are some sample functions for interaction with FastAPI and its REST Interface (_handle_get and _handle_post) 
    and for FastIoT and the nats message broker (_produce, _consume)
    """

    def _handle_get(self):
        """ Simple method to reply to a get request """
        return json.dumps(['id1', 'id2', 'id3'])

    async def _handle_post(self, data_file: bytes = File(),
                           file_type: str = Form(...),
                           data_delimiter: str = Form(...),
                           decimal_delimiter: str = Form(...),
                           material_id: Optional[str] = Form(None)):
        """
        Simple handling of Post Request

        the = Body(...) is needed as we don’t use pydantic classes,
        s. https://fastapi.tiangolo.com/tutorial/body-multiple-params/#embed-a-single-body-parameter for more details
        """

        data_frame = self._parse_file(data_delimiter, data_file, decimal_delimiter, file_type)
        timestamp_in_table = 'Timestamp' in data_frame
        self._data_frame_validation(data_frame, material_id, timestamp_in_table)
        await self._data_frame_send_things(data_frame, material_id, timestamp_in_table)
        return "File successfully uploaded"

    async def _data_frame_send_things(self, data_frame, material_id, timestamp_in_table):
        attributes = [column for column in data_frame
                      if (column != 'Material_ID' and column != 'Timestamp')]
        # create things from table
        for index, row in data_frame.iterrows():
            row = row.to_dict()  # This will make sure, we have python primitives like int and not np.int64
            row_timestamp = get_time_now()  # the same timestamp for each thing from row
            for attr in attributes:
                measurement_id = material_id or row['Material_ID']

                if timestamp_in_table:
                    timestamp = row['Timestamp'].to_pydatetime()
                else:
                    timestamp = row_timestamp

                # create thing
                thing = Thing(machine=self.machine,
                              name=attr,
                              measurement_id=measurement_id,
                              value=row[attr],
                              timestamp=timestamp)
                # get unit after parsing the value in thing

                await self.broker_connection.publish(subject=Thing.get_subject("DataImporter"),
                                                     msg=thing)

    def _data_frame_validation(self, data_frame, material_id, timestamp_in_table):
        if len(data_frame.columns) <= 1:
            raise HTTPException(status_code=500, detail='Potentially wrong configuration!')
        material_id_exists = material_id or "Material_ID" in data_frame
        if not material_id_exists or ("Material_ID" not in data_frame and "Timestamp" not in data_frame):
            raise HTTPException(status_code=500, detail="No Material_ID or no Timestamp!")
        if timestamp_in_table:
            try:
                data_frame.Timestamp = pd.to_datetime(data_frame.Timestamp)
            except (pd.ParseError, ValueError):
                raise HTTPException(status_code=500, detail="Could not parse datetimes")
        return timestamp_in_table

    def _parse_file(self, data_delimiter, data_file, decimal_delimiter, file_type):
        decimal_delimiter = ',' if decimal_delimiter == 'comma' else '.'
        data_delimiters = {'comma': ',', 'semicolon': ';'}
        try:
            if file_type == '.csv':
                data_frame = pd.read_csv(io.StringIO(data_file.decode('utf-8')),
                                         delimiter=data_delimiters.get(data_delimiter, ","),
                                         decimal=decimal_delimiter)
            elif file_type == '.xlsx':
                data_frame = pd.read_excel(data_file)
            else:
                raise Exception('Unknown extension')
        except:
            raise HTTPException(status_code=500, detail='Could not parse the file!')
        return data_frame


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    FrontendService.main()
