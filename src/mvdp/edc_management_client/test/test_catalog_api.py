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
from mvdp.edc_management_client.api.catalog_api import CatalogApi  # noqa: E501
from mvdp.edc_management_client.rest import ApiException


class TestCatalogApi(unittest.TestCase):
    """CatalogApi unit test stubs"""

    def setUp(self):
        self.api = mvdp.edc_management_client.api.catalog_api.CatalogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_request_catalog(self):
        """Test case for request_catalog

        """
        pass


if __name__ == '__main__':
    unittest.main()
