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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from mvdp.edc_management_client.models.callback_address import CallbackAddress

class ContractNegotiationDto(BaseModel):
    """
    ContractNegotiationDto
    """
    context: Optional[Dict[str, Any]] = Field(None, alias="@context")
    id: Optional[StrictStr] = Field(None, alias="@id")
    type: Optional[StrictStr] = Field(None, alias="@type")
    callback_addresses: Optional[conlist(CallbackAddress)] = Field(None, alias="callbackAddresses")
    contract_agreement_id: Optional[StrictStr] = Field(None, alias="contractAgreementId")
    counter_party_address: Optional[StrictStr] = Field(None, alias="counterPartyAddress")
    created_at: Optional[StrictInt] = Field(None, alias="createdAt")
    error_detail: Optional[StrictStr] = Field(None, alias="errorDetail")
    protocol: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    updated_at: Optional[StrictInt] = Field(None, alias="updatedAt")
    __properties = ["@context", "@id", "@type", "callbackAddresses", "contractAgreementId", "counterPartyAddress", "createdAt", "errorDetail", "protocol", "state", "type", "updatedAt"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CONSUMER', 'PROVIDER'):
            raise ValueError("must be one of enum values ('CONSUMER', 'PROVIDER')")
        return value

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
    def from_json(cls, json_str: str) -> ContractNegotiationDto:
        """Create an instance of ContractNegotiationDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in callback_addresses (list)
        _items = []
        if self.callback_addresses:
            for _item in self.callback_addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['callbackAddresses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContractNegotiationDto:
        """Create an instance of ContractNegotiationDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContractNegotiationDto.parse_obj(obj)

        _obj = ContractNegotiationDto.parse_obj({
            "context": obj.get("@context"),
            "id": obj.get("@id"),
            "type": obj.get("@type"),
            "callback_addresses": [CallbackAddress.from_dict(_item) for _item in obj.get("callbackAddresses")] if obj.get("callbackAddresses") is not None else None,
            "contract_agreement_id": obj.get("contractAgreementId"),
            "counter_party_address": obj.get("counterPartyAddress"),
            "created_at": obj.get("createdAt"),
            "error_detail": obj.get("errorDetail"),
            "protocol": obj.get("protocol"),
            "state": obj.get("state"),
            "type": obj.get("type"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj

