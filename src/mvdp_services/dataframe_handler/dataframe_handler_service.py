"""
Application logic for dataframe_handler service
"""

import asyncio
import logging

import pandas as pd

from pandas import DataFrame
from fastapi import FastAPI, Form
from fastiot.core import FastIoTService
from starlette.middleware.cors import CORSMiddleware

from mvdp_services.dataframe_handler.env import env_dataframe_handler
from mvdp_services.dataframe_handler.uvicorn_server import UvicornAsyncServer


class DataframeHandlerService(FastIoTService):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app = FastAPI()
        self._register_routes()
        self.server = UvicornAsyncServer(self.app, port=env_dataframe_handler.fastapi_port)

        self.message_received = asyncio.Event()
        self.last_msg = None

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
                           content: str = Form(...)):
        dataframe = pd.read_json(content).sort_index()
        self._logger.debug(dataframe)
        return {"hello": "world"}


if __name__ == '__main__':
    # Change this to reduce verbosity or remove completely to use `FASTIOT_LOG_LEVEL` environment variable to configure
    # logging.
    logging.basicConfig(level=logging.DEBUG)
    DataframeHandlerService.main()
