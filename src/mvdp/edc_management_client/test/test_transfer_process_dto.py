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
from mvdp.edc_management_client.models.transfer_process_dto import TransferProcessDto  # noqa: E501
from mvdp.edc_management_client.rest import ApiException

class TestTransferProcessDto(unittest.TestCase):
    """TransferProcessDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TransferProcessDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransferProcessDto`
        """
        model = mvdp.edc_management_client.models.transfer_process_dto.TransferProcessDto()  # noqa: E501
        if include_optional :
            return TransferProcessDto(
                context = None, 
                id = '', 
                type = '', 
                callback_addresses = [
                    mvdp.edc_management_client.models.callback_address_dto.CallbackAddressDto(
                        @context = mvdp.edc_management_client.models.@context.@context(), 
                        @type = '', 
                        auth_code_id = '', 
                        auth_key = '', 
                        events = [
                            ''
                            ], 
                        transactional = True, 
                        uri = '', )
                    ], 
                created_at = 56, 
                data_destination = mvdp.edc_management_client.models.data_address_dto.DataAddressDto(
                    @context = mvdp.edc_management_client.models.@context.@context(), 
                    @type = '', 
                    properties = {
                        'key' : ''
                        }, ), 
                data_request = mvdp.edc_management_client.models.data_request_dto.DataRequestDto(
                    asset_id = '', 
                    connector_id = '', 
                    contract_id = '', 
                    id = '', ), 
                error_detail = '', 
                properties = {
                    'key' : ''
                    }, 
                state = '', 
                state_timestamp = 56, 
                type = '', 
                updated_at = 56
            )
        else :
            return TransferProcessDto(
        )
        """

    def testTransferProcessDto(self):
        """Test TransferProcessDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()