import os
import unittest
import uuid

from fastiot.testlib import populate_test_env

from mvdp.edc_management_client.api import ApplicationObservabilityApi, AssetApi
from mvdp.edc_management_client.api_client import ApiClient
from mvdp.edc_management_client.configuration import Configuration
from mvdp.edc_management_client.models import AssetCreationRequestDto, AssetEntryDto, DataAddress, HealthStatus
from mvdp.env import mvdp_env, MVDP_EDC_PORT, MVDP_EDC_HOST, MVDP_EDC_PORT_2


class TestUploadingAssets(unittest.TestCase):

    def setUp(self):
        populate_test_env()
        os.environ[MVDP_EDC_PORT_2] = '8182'
        os.environ[MVDP_EDC_HOST] = 'localhost'

        config = Configuration()
        config.host = f"http://{mvdp_env.edc_host}:{mvdp_env.edc_port_2}/api/v1/management"
        config.verify_ssl = False
        config.debug = True
        config.api_key = {'X-Api-Key': 'ApiKeyDefaultValue'}

        self.api_client = ApiClient(config, header_name='X-Api-Key', header_value='ApiKeyDefaultValue')

    def test_health(self):
        health_api_instance = ApplicationObservabilityApi(self.api_client)
        raw_result = health_api_instance.check_health()
        result = HealthStatus(raw_result[0])
        self.assertEqual(result.is_system_healthy, None)

    def test_upload(self):
        asset_api_instance = AssetApi(self.api_client)

        asset = AssetEntryDto(asset=AssetCreationRequestDto(
            id=uuid.uuid4().hex,
            properties={
                "asset:prop:name": "test",
                "asset:prop:version": "1.0",
                "asset:prop:id": "DatasetTest",
                "asset:prop:contenttype": "text/plain"}),
            data_address=DataAddress(
                properties={"type": "LocalFile", "address": "/Files/test.txt"})
        )

        response = asset_api_instance.create_asset(body=asset)
        print(response)


if __name__ == '__main__':
    unittest.main()
