# coding: utf-8

"""
    EDC REST API

    EDC REST APIs - merged by OpenApiMerger  # noqa: E501

    The version of the OpenAPI document: 0.1.0-SNAPSHOT
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import mvdp.edc_management_client
from mvdp.edc_management_client.api.application_observability_api import ApplicationObservabilityApi  # noqa: E501
from mvdp.edc_management_client.rest import ApiException


class TestApplicationObservabilityApi(unittest.TestCase):
    """ApplicationObservabilityApi unit test stubs"""

    def setUp(self):
        self.api = mvdp.edc_management_client.api.application_observability_api.ApplicationObservabilityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_health(self):
        """Test case for check_health

        """
        pass

    def test_get_liveness(self):
        """Test case for get_liveness

        """
        pass

    def test_get_readiness(self):
        """Test case for get_readiness

        """
        pass

    def test_get_startup(self):
        """Test case for get_startup

        """
        pass


if __name__ == '__main__':
    unittest.main()