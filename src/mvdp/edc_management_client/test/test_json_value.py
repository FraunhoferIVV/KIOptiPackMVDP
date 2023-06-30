# coding: utf-8

"""
    EDC REST API

    EDC REST APIs - merged by OpenApiMerger  # noqa: E501

    The version of the OpenAPI document: 0.1.0-SNAPSHOT
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import mvdp.edc_management_client
from mvdp.edc_management_client.models.json_value import JsonValue  # noqa: E501
from mvdp.edc_management_client.rest import ApiException

class TestJsonValue(unittest.TestCase):
    """JsonValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JsonValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonValue`
        """
        model = mvdp.edc_management_client.models.json_value.JsonValue()  # noqa: E501
        if include_optional :
            return JsonValue(
                value_type = 'ARRAY'
            )
        else :
            return JsonValue(
        )
        """

    def testJsonValue(self):
        """Test JsonValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
