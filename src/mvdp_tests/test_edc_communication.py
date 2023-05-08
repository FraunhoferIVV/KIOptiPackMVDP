import os
import unittest

from fastiot.cli.env import env_cli
from fastiot.core.broker_connection import NatsBrokerConnection
from fastiot.testlib import populate_test_env, BackgroundProcess
from fastiot.util.ports import get_local_random_port

from mvdp_services.data_provider.data_provider_service import DataProviderService

from mvdp_services.data_provider.env import MVDP_DATA_PROVIDER_PORT


class TestEDCConnection(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        populate_test_env()
        self.broker_connection = await NatsBrokerConnection.connect()

        if env_cli.is_ci_runner:
            os.environ[MVDP_DATA_PROVIDER_PORT] = str(get_local_random_port())
        else:
            os.environ[MVDP_DATA_PROVIDER_PORT] = '5479'

    async def asyncTearDown(self):
        await self.broker_connection.close()

    async def test_edc_upload(self):
        data_provider_service = DataProviderService()

