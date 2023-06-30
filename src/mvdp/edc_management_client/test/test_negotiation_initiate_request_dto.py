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
from mvdp.edc_management_client.models.negotiation_initiate_request_dto import NegotiationInitiateRequestDto  # noqa: E501
from mvdp.edc_management_client.rest import ApiException

class TestNegotiationInitiateRequestDto(unittest.TestCase):
    """NegotiationInitiateRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NegotiationInitiateRequestDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NegotiationInitiateRequestDto`
        """
        model = mvdp.edc_management_client.models.negotiation_initiate_request_dto.NegotiationInitiateRequestDto()  # noqa: E501
        if include_optional :
            return NegotiationInitiateRequestDto(
                context = None, 
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
                connector_address = '', 
                connector_id = '', 
                consumer_id = '', 
                offer = mvdp.edc_management_client.models.contract_offer_description.ContractOfferDescription(
                    asset_id = '', 
                    offer_id = '', 
                    policy = mvdp.edc_management_client.models.policy.Policy(
                        @type = 'SET', 
                        assignee = '', 
                        assigner = '', 
                        extensible_properties = {
                            'key' : None
                            }, 
                        inherits_from = '', 
                        obligations = [
                            mvdp.edc_management_client.models.duty.Duty(
                                action = mvdp.edc_management_client.models.action.Action(
                                    constraint = mvdp.edc_management_client.models.constraint.Constraint(
                                        edctype = '', ), 
                                    included_in = '', 
                                    type = '', ), 
                                assignee = '', 
                                assigner = '', 
                                consequence = mvdp.edc_management_client.models.duty.Duty(
                                    assignee = '', 
                                    assigner = '', 
                                    constraints = [
                                        mvdp.edc_management_client.models.constraint.Constraint(
                                            edctype = '', )
                                        ], 
                                    parent_permission = mvdp.edc_management_client.models.permission.Permission(
                                        assignee = '', 
                                        assigner = '', 
                                        duties = [
                                            
                                            ], 
                                        target = '', ), 
                                    target = '', ), 
                                constraints = [
                                    
                                    ], 
                                parent_permission = mvdp.edc_management_client.models.permission.Permission(
                                    assignee = '', 
                                    assigner = '', 
                                    target = '', ), 
                                target = '', )
                            ], 
                        permissions = [
                            
                            ], 
                        prohibitions = [
                            mvdp.edc_management_client.models.prohibition.Prohibition(
                                assignee = '', 
                                assigner = '', 
                                target = '', )
                            ], 
                        target = '', ), 
                    validity = 56, ), 
                protocol = '', 
                provider_id = ''
            )
        else :
            return NegotiationInitiateRequestDto(
                connector_address = '',
                connector_id = '',
                offer = mvdp.edc_management_client.models.contract_offer_description.ContractOfferDescription(
                    asset_id = '', 
                    offer_id = '', 
                    policy = mvdp.edc_management_client.models.policy.Policy(
                        @type = 'SET', 
                        assignee = '', 
                        assigner = '', 
                        extensible_properties = {
                            'key' : None
                            }, 
                        inherits_from = '', 
                        obligations = [
                            mvdp.edc_management_client.models.duty.Duty(
                                action = mvdp.edc_management_client.models.action.Action(
                                    constraint = mvdp.edc_management_client.models.constraint.Constraint(
                                        edctype = '', ), 
                                    included_in = '', 
                                    type = '', ), 
                                assignee = '', 
                                assigner = '', 
                                consequence = mvdp.edc_management_client.models.duty.Duty(
                                    assignee = '', 
                                    assigner = '', 
                                    constraints = [
                                        mvdp.edc_management_client.models.constraint.Constraint(
                                            edctype = '', )
                                        ], 
                                    parent_permission = mvdp.edc_management_client.models.permission.Permission(
                                        assignee = '', 
                                        assigner = '', 
                                        duties = [
                                            
                                            ], 
                                        target = '', ), 
                                    target = '', ), 
                                constraints = [
                                    
                                    ], 
                                parent_permission = mvdp.edc_management_client.models.permission.Permission(
                                    assignee = '', 
                                    assigner = '', 
                                    target = '', ), 
                                target = '', )
                            ], 
                        permissions = [
                            
                            ], 
                        prohibitions = [
                            mvdp.edc_management_client.models.prohibition.Prohibition(
                                assignee = '', 
                                assigner = '', 
                                target = '', )
                            ], 
                        target = '', ), 
                    validity = 56, ),
                protocol = '',
        )
        """

    def testNegotiationInitiateRequestDto(self):
        """Test NegotiationInitiateRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()