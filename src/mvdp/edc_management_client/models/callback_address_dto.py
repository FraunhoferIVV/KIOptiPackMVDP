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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist

class CallbackAddressDto(BaseModel):
    """
    CallbackAddressDto
    """
    context: Optional[Dict[str, Any]] = Field(None, alias="@context")
    type: Optional[StrictStr] = Field(None, alias="@type")
    auth_code_id: Optional[StrictStr] = Field(None, alias="authCodeId")
    auth_key: Optional[StrictStr] = Field(None, alias="authKey")
    events: conlist(StrictStr, unique_items=True) = Field(...)
    transactional: Optional[StrictBool] = None
    uri: StrictStr = Field(...)
    __properties = ["@context", "@type", "authCodeId", "authKey", "events", "transactional", "uri"]

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
    def from_json(cls, json_str: str) -> CallbackAddressDto:
        """Create an instance of CallbackAddressDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CallbackAddressDto:
        """Create an instance of CallbackAddressDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CallbackAddressDto.parse_obj(obj)

        _obj = CallbackAddressDto.parse_obj({
            "context": obj.get("@context"),
            "type": obj.get("@type"),
            "auth_code_id": obj.get("authCodeId"),
            "auth_key": obj.get("authKey"),
            "events": obj.get("events"),
            "transactional": obj.get("transactional"),
            "uri": obj.get("uri")
        })
        return _obj
