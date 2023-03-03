import datetime
import unittest
import uuid

from fastiot.testlib import populate_test_env

import edc_management_client as edc
from mvdp.env import mvdp_env


class TestUploadingAssets(unittest.TestCase):

    def setUp(self):
        populate_test_env()

        config = edc.Configuration()
        config.host = f"http://{mvdp_env.edc_host}:{mvdp_env.edc_port}/api"
        config.verify_ssl = False
        config.debug = True

        self.api_client = edc.ApiClient(config)

    def test_health(self):
        health_api_instance = edc.ApplicationObservabilityApi(self.api_client)
        raw_result = health_api_instance.check_health()
        result = edc.HealthStatus(raw_result[0])
        self.assertEqual(result.is_system_healthy, None)

    @unittest.skip("Currently returns error 404")
    def test_upload(self):
        asset_api_instance = edc.AssetApi(self.api_client)

        asset = edc.Asset(created_at=datetime.datetime.now(),
                          id=uuid.uuid4().hex)

        response = asset_api_instance.create_asset(body=asset)
        print(response)


if __name__ == '__main__':
    unittest.main()
