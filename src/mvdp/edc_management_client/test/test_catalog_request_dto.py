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
from mvdp.edc_management_client.models.catalog_request_dto import CatalogRequestDto  # noqa: E501
from mvdp.edc_management_client.rest import ApiException

class TestCatalogRequestDto(unittest.TestCase):
    """CatalogRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CatalogRequestDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CatalogRequestDto`
        """
        model = mvdp.edc_management_client.models.catalog_request_dto.CatalogRequestDto()  # noqa: E501
        if include_optional :
            return CatalogRequestDto(
                context = None, 
                type = '', 
                protocol = '', 
                provider_url = '', 
                query_spec = mvdp.edc_management_client.models.query_spec_dto.QuerySpecDto(
                    @context = mvdp.edc_management_client.models.@context.@context(), 
                    @type = '', 
                    filter_expression = [
                        mvdp.edc_management_client.models.criterion_dto.CriterionDto(
                            @context = mvdp.edc_management_client.models.@context.@context(), 
                            @type = '', 
                            operand_left = mvdp.edc_management_client.models.operand_left.operandLeft(), 
                            operand_right = mvdp.edc_management_client.models.operand_right.operandRight(), 
                            operator = '', )
                        ], 
                    limit = 56, 
                    offset = 56, 
                    sort_field = '', 
                    sort_order = 'ASC', )
            )
        else :
            return CatalogRequestDto(
                provider_url = '',
        )
        """

    def testCatalogRequestDto(self):
        """Test CatalogRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
