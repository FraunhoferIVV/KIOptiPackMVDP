import asyncio
import os
import unittest

import pandas as pd
from fastiot.core.broker_connection import NatsBrokerConnection
from fastiot.testlib import populate_test_env
from fastiot.util.ports import get_local_random_port
from fastiot.db.mongodb_helper_fn import get_mongodb_client_from_env
from fastiot.env import env_mongodb
from unittest.mock import patch
from pandas import DataFrame

from mvdp.data_space_uploader.DataSpaceUploader import DataSpaceUploader
from mvdp_services.dataframe_handler.dataframe_handler_service import DataframeHandlerService
from mvdp_services.dataframe_handler.env import MVDP_DATAFRAME_HANDLER_PORT


class TestDataSpaceUploader(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        populate_test_env()
        self.broker_connection = await NatsBrokerConnection.connect()

        # os.environ[MVDP_DATAFRAME_HANDLER_PORT] = str(get_local_random_port())
        os.environ[MVDP_DATAFRAME_HANDLER_PORT] = '5480'

        db_client = get_mongodb_client_from_env()
        database = db_client.get_database(env_mongodb.name)
        self._db_col = database.get_collection('thing')
        self._db_col.delete_many({})

    async def asyncTearDown(self):
        self.broker_connection.close()

    async def test_upload_only_parameters(self):
        # async with DataframeHandlerService(broker_connection=self.broker_connection) as _:
        self._db_col.delete_many({})
        uploader = DataSpaceUploader(server='localhost',
                                     port=int(os.environ[MVDP_DATAFRAME_HANDLER_PORT]))
        df = DataFrame({
            'ExperimentName': ['exp1', '-', 'exp2'],
            'Parameter': ['param1', 'param2', 'param2'],
            'Value': [False, 42, 42.5]
        })
        uploader.upload('experiment323', df)
        await asyncio.sleep(0.02)
        results = list(self._db_col.find({}))
        self.assertEqual(3, len(results))


if __name__ == '__main__':
    unittest.main()
