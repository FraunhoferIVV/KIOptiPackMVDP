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
from mvdp.edc_management_client.models.transfer_process_fail_state_dto import TransferProcessFailStateDto  # noqa: E501
from mvdp.edc_management_client.rest import ApiException

class TestTransferProcessFailStateDto(unittest.TestCase):
    """TransferProcessFailStateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TransferProcessFailStateDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransferProcessFailStateDto`
        """
        model = mvdp.edc_management_client.models.transfer_process_fail_state_dto.TransferProcessFailStateDto()  # noqa: E501
        if include_optional :
            return TransferProcessFailStateDto(
                error_message = ''
            )
        else :
            return TransferProcessFailStateDto(
                error_message = '',
        )
        """

    def testTransferProcessFailStateDto(self):
        """Test TransferProcessFailStateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
