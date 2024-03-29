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
from mvdp.edc_management_client.models.contract_offer_description import ContractOfferDescription  # noqa: E501
from mvdp.edc_management_client.rest import ApiException

class TestContractOfferDescription(unittest.TestCase):
    """ContractOfferDescription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContractOfferDescription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContractOfferDescription`
        """
        model = mvdp.edc_management_client.models.contract_offer_description.ContractOfferDescription()  # noqa: E501
        if include_optional :
            return ContractOfferDescription(
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
                validity = 56
            )
        else :
            return ContractOfferDescription(
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
        )
        """

    def testContractOfferDescription(self):
        """Test ContractOfferDescription"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
