# coding: utf-8

"""
    EDC REST API

    EDC REST APIs - merged by OpenApiMerger  # noqa: E501

    The version of the OpenAPI document: 0.1.0-SNAPSHOT
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from mvdp.edc_management_client.models.policy import Policy

class ContractOffer(BaseModel):
    """
    ContractOffer
    """
    asset_id: Optional[StrictStr] = Field(None, alias="assetId")
    id: Optional[StrictStr] = None
    policy: Optional[Policy] = None
    provider_id: Optional[StrictStr] = Field(None, alias="providerId")
    __properties = ["assetId", "id", "policy", "providerId"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ContractOffer:
        """Create an instance of ContractOffer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of policy
        if self.policy:
            _dict['policy'] = self.policy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContractOffer:
        """Create an instance of ContractOffer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContractOffer.parse_obj(obj)

        _obj = ContractOffer.parse_obj({
            "asset_id": obj.get("assetId"),
            "id": obj.get("id"),
            "policy": Policy.from_dict(obj.get("policy")) if obj.get("policy") is not None else None,
            "provider_id": obj.get("providerId")
        })
        return _obj

