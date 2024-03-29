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



from pydantic import BaseModel, Field, StrictStr

class TerminateTransferDto(BaseModel):
    """
    TerminateTransferDto
    """
    reason: StrictStr = Field(...)
    __properties = ["reason"]

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
    def from_json(cls, json_str: str) -> TerminateTransferDto:
        """Create an instance of TerminateTransferDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TerminateTransferDto:
        """Create an instance of TerminateTransferDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TerminateTransferDto.parse_obj(obj)

        _obj = TerminateTransferDto.parse_obj({
            "reason": obj.get("reason")
        })
        return _obj

