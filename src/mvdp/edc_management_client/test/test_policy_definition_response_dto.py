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
from mvdp.edc_management_client.models.policy_definition_response_dto import PolicyDefinitionResponseDto  # noqa: E501
from mvdp.edc_management_client.rest import ApiException

class TestPolicyDefinitionResponseDto(unittest.TestCase):
    """PolicyDefinitionResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PolicyDefinitionResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PolicyDefinitionResponseDto`
        """
        model = mvdp.edc_management_client.models.policy_definition_response_dto.PolicyDefinitionResponseDto()  # noqa: E501
        if include_optional :
            return PolicyDefinitionResponseDto(
                context = None, 
                id = '', 
                type = '', 
                created_at = 56, 
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
                    target = '', )
            )
        else :
            return PolicyDefinitionResponseDto(
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
        )
        """

    def testPolicyDefinitionResponseDto(self):
        """Test PolicyDefinitionResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()