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
from mvdp.edc_management_client.api.data_plane_control_api_api import DataPlaneControlAPIApi  # noqa: E501
from mvdp.edc_management_client.rest import ApiException


class TestDataPlaneControlAPIApi(unittest.TestCase):
    """DataPlaneControlAPIApi unit test stubs"""

    def setUp(self):
        self.api = mvdp.edc_management_client.api.data_plane_control_api_api.DataPlaneControlAPIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_transfer_state(self):
        """Test case for get_transfer_state

        """
        pass

    def test_initiate_transfer(self):
        """Test case for initiate_transfer

        """
        pass


if __name__ == '__main__':
    unittest.main()
