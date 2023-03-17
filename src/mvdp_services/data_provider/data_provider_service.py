"""
This file has just been created automatically.
This is the file where you can write you own service.
Currently, the is code provides a basic producer and an basic consumer.
In order for your code to work, you must delete the code that you are not using and add your own application logic.
"""

import asyncio
import logging
import random

from fastiot.core import FastIoTService, Subject, subscribe, loop
from fastiot.core.core_uuid import get_uuid
from fastiot.core.time import get_time_now
from fastiot.msg.thing import Thing


class DataProviderService(FastIoTService):

    @loop
    async def produce(self):
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
        self._logger.info("Published %d on sensor %s", value, subject.name)
        return asyncio.sleep(2)

    @subscribe(subject=Thing.get_subject('*'))
    async def consume(self, topic: str, msg: Thing):
        """ Subscribing to `Thing.*` messages """
        self._logger.info("%s: %s", topic, str(msg))


if __name__ == '__main__':
    # Change this to reduce verbosity or remove completely to use `FASTIOT_LOG_LEVEL` environment variable to configure
    # logging.
    logging.basicConfig(level=logging.DEBUG)
    DataProviderService.main()
