import asyncio
import os
import unittest

import pandas as pd
from fastiot.core.broker_connection import NatsBrokerConnection
from fastiot.testlib import populate_test_env

from mvdp.data_space_uploader.DataSpaceUploader import DataSpaceUploader
from mvdp_services.dataframe_handler.dataframe_handler_service import DataframeHandlerService
from mvdp_services.dataframe_handler.env import env_dataframe_handler, MVDP_DATAFRAME_HANDLER_PORT


class MyTestCase(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        populate_test_env()
        os.environ[MVDP_DATAFRAME_HANDLER_PORT] = '44543'  # Todo: Find free port or read in .env…
        self.broker_connection = await NatsBrokerConnection.connect()
        service = DataframeHandlerService(broker_connection=self.broker_connection)
        self.service_task = asyncio.create_task(service.run())
        await asyncio.sleep(0.005)

    async def asyncTearDown(self):
        self.service_task.cancel()

    @unittest.skip("Work in progress")
    async def test_simple_upload(self):
        uploader = DataSpaceUploader(server='localhost')
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
        uploader.upload('A', df)


if __name__ == '__main__':
    unittest.main()
