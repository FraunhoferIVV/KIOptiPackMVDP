"""
Application logic for frontend service
"""

import asyncio
import logging
import os
import random
from typing import Optional

import pandas as pd

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastiot.core import FastIoTService, subscribe, loop
from fastiot.core.core_uuid import get_uuid
from fastiot.core.time import get_time_now
from fastiot.msg.thing import Thing
from starlette.middleware.cors import CORSMiddleware

from mvdp_services.frontend.UploadData import UploadData
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

    async def _handle_post(self, data_file: bytes = UploadFile(...),
                           file_type: str = Form(...),
                           data_delimiter: str = Form(...),
                           decimal_delimiter: str = Form(...),
                           material_ID: str = Form(...)):
        """
        Simple handling of Post Request

        the = Body(...) is needed as we don’t use pydantic classes,
        s. https://fastapi.tiangolo.com/tutorial/body-multiple-params/#embed-a-single-body-parameter for more details
        """

        self.upload_data = UploadData(data_file, file_type, data_delimiter, decimal_delimiter, material_ID)

        data_frame = pd.read_excel(data_file.file)

        data_frame = self.parse_upload_data()

        if data_frame == None:
            return "Fehler bei der Datenextraktion"

        return "Datei erfolgreich hochgeladen"

    async def parse(self):
        try:
            if self.upload_data.file_type == '.csv':
                data_frame = await pd.read_csv(self.upload_data.data_file.file,
                                               sep=self.upload_data.get_sep(),
                                               delimiter=self.upload_data.get_delimiter())
            if self.upload_data.file_type == '.xlsx':
                data_frame = await pd.read_excel(self.upload_data.data_file.file)
            return data_frame
        except:
            return None


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    FrontendService.main()
