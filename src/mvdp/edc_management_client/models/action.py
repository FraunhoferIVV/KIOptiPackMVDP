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
from mvdp.edc_management_client.models.constraint import Constraint

class Action(BaseModel):
    """
    Action
    """
    constraint: Optional[Constraint] = None
    included_in: Optional[StrictStr] = Field(None, alias="includedIn")
    type: Optional[StrictStr] = None
    __properties = ["constraint", "includedIn", "type"]

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
    def from_json(cls, json_str: str) -> Action:
        """Create an instance of Action from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of constraint
        if self.constraint:
            _dict['constraint'] = self.constraint.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Action:
        """Create an instance of Action from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Action.parse_obj(obj)

        _obj = Action.parse_obj({
            "constraint": Constraint.from_dict(obj.get("constraint")) if obj.get("constraint") is not None else None,
            "included_in": obj.get("includedIn"),
            "type": obj.get("type")
        })
        return _obj

