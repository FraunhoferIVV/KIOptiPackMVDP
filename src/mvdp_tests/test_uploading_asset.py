import time
import unittest
import uuid

from fastiot.core.time import get_time_now
from fastiot.testlib import populate_test_env

from mvdp.edc_management_client import ApplicationObservabilityApi, AssetApi
from mvdp.edc_management_client.api_client import ApiClient
from mvdp.edc_management_client.configuration import Configuration
from mvdp.edc_management_client.models import DataAddress, AssetEntryNewDto, Asset
from mvdp.env import mvdp_env


class TestUploadingAssets(unittest.TestCase):

    def setUp(self):
        populate_test_env()

        config = Configuration()
        config.host = f"http://{mvdp_env.edc_host}:{mvdp_env.edc_port_2}/management"
        config.verify_ssl = False
        config.debug = True
        config.api_key = {'X-Api-Key': 'ApiKeyDefaultValue'}

        self.api_client = ApiClient(config, header_name='X-Api-Key', header_value='ApiKeyDefaultValue')

    def test_health(self):
        health_api_instance = ApplicationObservabilityApi(self.api_client)
        result = health_api_instance.check_health()
        self.assertEqual(result.is_system_healthy, True)

    @unittest.skip("Not yet adjusted to latest EDC API")
    def test_upload(self):
        asset_api_instance = AssetApi(self.api_client)

        asset = AssetEntryNewDto(asset=Asset(
            created_at=int(time.mktime(get_time_now().timetuple())),
            id=uuid.uuid4().hex,
            properties={
                "asset:prop:name": "test",
                "asset:prop:version": "1.0",
                "asset:prop:id": "DatasetTest",
                "asset:prop:contenttype": "text/plain"}),
            data_address=DataAddress(
                properties={"type": "LocalFile", "address": "/Files/test.txt"})
        )

        response = asset_api_instance.create_asset(asset)
        print(response)


if __name__ == '__main__':
    unittest.main()
