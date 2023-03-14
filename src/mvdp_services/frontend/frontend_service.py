"""
Application logic for frontend service
"""

import asyncio
import logging
import os
import io
from datetime import datetime

import pandas as pd
import json

from fastapi import FastAPI, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastiot.core import FastIoTService, subscribe, loop
from fastiot.core.core_uuid import get_uuid
from fastiot.core.time import get_time_now
from fastiot.msg.thing import Thing
from starlette.middleware.cors import CORSMiddleware

from mvdp_services.frontend.env import env_frontend
from mvdp_services.frontend.uvicorn_server import UvicornAsyncServer


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
        """
        return {"hello_world": "Good morning!",
                "last_message": self.last_msg}
        """
        return json.dumps(['id1', 'id2', 'id3'])

    async def _handle_post(self, data_file: bytes = File(),
                           file_type: str = Form(...),
                           data_delimiter: str = Form(...),
                           decimal_delimiter: str = Form(...),
                           material_id: str = Form(...)):
        """
        Simple handling of Post Request

        the = Body(...) is needed as we don’t use pydantic classes,
        s. https://fastapi.tiangolo.com/tutorial/body-multiple-params/#embed-a-single-body-parameter for more details
        """

        decimal_delimiter = ',' if decimal_delimiter == 'comma' else '.'
        data_delimiters = {'comma': ',', 'semicolon': ';'}

        material_id = None if material_id == 'no' else material_id

        try:
            if file_type == '.csv':
                data_frame = pd.read_csv(io.StringIO(data_file.decode('utf-8')),
                                         delimiter=data_delimiters.get(data_delimiter, ","),
                                         decimal=decimal_delimiter)
            elif file_type == '.xlsx':
                data_frame = pd.read_excel(data_file)

        except:
            raise HTTPException(status_code=500, detail='Could not parse the file!')

        if len(data_frame.columns) <= 1:
            raise HTTPException(status_code=500, detail='Potentially wrong configuration!')

        # information to use

        timestamp_in_table = 'Timestamp' in data_frame
        if not material_id and "Material_ID" not in data_frame:
            raise HTTPException(status_code=500, detail="No Material_ID!")

        if timestamp_in_table:
            try:
                data_frame.Timestamp = pd.to_datetime(data_frame.Timestamp)
            except (pd.ParseError, ValueError):
                self._logger.warning("Could not parse datetimes. Leaving as string.")

        attributes = [column for column in data_frame
                      if (column != 'Material_ID' and column != 'Timestamp')]

        # create things from table
        for index, row in data_frame.iterrows():
            row = row.to_dict()  # This will make sure, we have python primitives like int and not np.int64
            for attr in attributes:
                measurement_id = material_id or row['Material_ID']

                if timestamp_in_table:
                    timestamp = row['Timestamp'].to_pydatetime()
                else:
                    timestamp = get_time_now()

                # create thing
                thing = Thing(machine=self.machine,
                              name=attr,
                              measurement_id=measurement_id,
                              value=row[attr],
                              timestamp=timestamp)
                              # get unit after parsing the value in thing

                await self.broker_connection.publish(subject=Thing.get_subject("DataImporter"),
                                                     msg=thing)

        return "File successfully uploaded"


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    FrontendService.main()
