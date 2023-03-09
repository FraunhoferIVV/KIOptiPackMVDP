"""
Application logic for frontend service
"""

import asyncio
import logging
import os
import io
from datetime import datetime
from tempfile import NamedTemporaryFile

import pandas as pd

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastiot.core import FastIoTService, subscribe, loop
from fastiot.core.core_uuid import get_uuid
from fastiot.core.time import get_time_now
from fastiot.msg.thing import Thing
from starlette.middleware.cors import CORSMiddleware

from mvdp_services.frontend.env import env_frontend
from mvdp_services.frontend.uvicorn_server import UvicornAsyncServer

import pymongo
import fastiot.db.mongodb_helper_fn as mongodb_helper
import pprint


class FrontendService(FastIoTService):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app = FastAPI()
        self._register_routes()
        self.server = UvicornAsyncServer(self.app, port=env_frontend.fastapi_port)

        self.message_received = asyncio.Event()
        self.last_msg = None

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
        return {"hello_world": "Good morning!",
                "last_message": self.last_msg}

    async def _handle_post(self, data_file: bytes = File(),
                     file_type: str = Form(...),
                     data_delimiter: str = Form(...),
                     decimal_delimiter: str = Form(...),
                     material_ID: str = Form(...)):
        """
        Simple handling of Post Request

        the = Body(...) is needed as we don’t use pydantic classes,
        s. https://fastapi.tiangolo.com/tutorial/body-multiple-params/#embed-a-single-body-parameter for more details
        """

        decimal_delimiter = ',' if decimal_delimiter == 'comma' else '.'
        data_delimiters = {'comma': ',', 'semicolon': ';'}

        try:
            if file_type == '.csv':
                data_frame = pd.read_csv(io.StringIO(data_file.decode('utf-8')),
                                         delimiter=data_delimiters.get(data_delimiter, ","),
                                         decimal=decimal_delimiter)

            if file_type == '.xlsx':
                data_frame = pd.read_excel(data_file)

            # create translate function: attributes in thing -> attributes in data_frame
            translate = {'machine': 'machine',
                         'name': 'name',
                         'measurement_id': 'material_ID',
                         'timestamp': 'timestamp',
                         'value': 'value',
                         'unit': 'unit'}

            # Is material_ID set?
            if material_ID == 'no' and 'material_ID' in data_frame:
                # material_ID not set <=> there is a column named material_ID
                translate['measurement_id'] = 'material_ID'

            # now assume material_ID set!
            for index, thing_like in data_frame.iterrows():
                thing = Thing(machine=thing_like[translate['machine']],
                              name=thing_like[translate['name']],
                              measurement_id=thing_like[translate['measurement_id']],
                              timestamp=datetime.strptime(thing_like[translate['timestamp']],
                                                          '%m/%d/%y %H:%M:%S'),
                              value=thing_like[translate['value']])

                await self.broker_connection.publish(subject=Thing.get_subject("DataImporter"),
                                                     msg=thing)



        except:
            return "Fehler bei der Datenextraktion"


        """
        await self.broker_connection.publish(subject=Thing.get_subject("excel_importer"),
                                             msg=Thing(machine="ExcelImporter",
                                                       name="Test", value=0,
                                                       timestamp=datetime.utcnow()))
        """
        return "Datei erfolgreich hochgeladen"


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    FrontendService.main()
