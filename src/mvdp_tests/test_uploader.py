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

from mvdp.data_space_uploader.DataSpaceUploader import DataSpaceUploader
from mvdp_services.dataframe_handler.dataframe_handler_service import DataframeHandlerService
from mvdp_services.dataframe_handler.env import env_dataframe_handler, MVDP_DATAFRAME_HANDLER_PORT

# ToDo: find a way set up dataframe_hanlder port to that port (change dataframe handler)
# ToDo: write unit and integration tests for uploader and dataframe_handler

MVDP_DATAFRAME_HANDLER_PORT = str(get_local_random_port())


@patch.dict('os.environ', {'MVDP_DATAFRAME_HANDLER_PORT': MVDP_DATAFRAME_HANDLER_PORT})
class TestDataSpaceUploader(unittest.IsolatedAsyncioTestCase):

    @patch.dict('os.environ', {'MVDP_DATAFRAME_HANDLER_PORT': MVDP_DATAFRAME_HANDLER_PORT})
    async def asyncSetUp(self):
        populate_test_env()
        self.broker_connection = await NatsBrokerConnection.connect()
        service = DataframeHandlerService(broker_connection=self.broker_connection)
        self.service_task = asyncio.create_task(service.run())
        await asyncio.sleep(0.005)
        self._db_client = get_mongodb_client_from_env()
        self._database = self._db_client.get_database(env_mongodb.name)
        self._db_col = self._database.get_collection('thing')
        self._db_col.delete_many({})

    @patch.dict('os.environ', {'MVDP_DATAFRAME_HANDLER_PORT': MVDP_DATAFRAME_HANDLER_PORT})
    async def asyncTearDown(self):
        self.service_task.cancel()
        self.broker_connection.close()

    async def test_upload_only_parameters(self):
        self._db_col.delete_many({})
        uploader = DataSpaceUploader(server='localhost')
        df = pd.DataFrame({
            'ExperimentName': ['exp1', '-', 'exp2'],
            'Parameter': ['param1', 'param2', 'param2'],
            'Value': [False, 42, 42.5]
        })
        uploader.upload('experiment323', df)
        await asyncio.sleep(0.02)
        results = set(self._db_col.find({}))
        self.assertEqual(3, len(results))


if __name__ == '__main__':
    unittest.main()
