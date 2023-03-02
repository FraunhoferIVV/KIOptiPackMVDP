"""
Application logic for frontend service
"""

import asyncio
import logging
import os
import random

from fastapi import FastAPI
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

    def _handle_post(self, message: UploadData):
        """
        Simple handling of Post Request

        the = Body(...) is needed as we don’t use pydantic classes,
        s. https://fastapi.tiangolo.com/tutorial/body-multiple-params/#embed-a-single-body-parameter for more details
        """

        return message

    @loop
    async def _produce(self):
        """ Creating some dummy data and publish it """
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
        logging.info("Published %d on sensor %s", value, subject.name)
        return asyncio.sleep(2)

    @subscribe(subject=Thing.get_subject('*'))
    async def _consume(self, topic: str, msg: Thing):
        """ Subscribing to `Thing.*` messages """
        self.last_msg = msg
        logging.info("%s: %s", topic, str(msg))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    FrontendService.main()
