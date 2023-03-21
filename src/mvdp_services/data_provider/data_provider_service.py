"""
Application logic for data_provider service
"""

import asyncio
import logging
import random

from fastapi import FastAPI
from fastiot.core import FastIoTService, Subject, subscribe, loop
from fastiot.core.core_uuid import get_uuid
from fastiot.core.time import get_time_now
from fastiot.msg.thing import Thing

from mvdp_services.data_provider.env import env_data_provider
from mvdp_services.data_provider.uvicorn_server import UvicornAsyncServer


class DataProviderService(FastIoTService):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app = FastAPI()
        # self._register_routes()
        self.server = UvicornAsyncServer(self.app, port=env_data_provider.fastapi_port)

        self.message_received = asyncio.Event()
        self.last_msg = None

    """
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
    """

    async def _start(self):
        """ Methods to start once the module is initialized """
        await self.server.up()

    async def _stop(self):
        """ Methods to call on module shutdown """
        await self.server.down()

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
