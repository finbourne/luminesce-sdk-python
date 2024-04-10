# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr
from luminesce.models.source_type import SourceType

class Source(BaseModel):
    """
    Information leading to choosing the provider  # noqa: E501
    """
    location: Optional[constr(strict=True, max_length=256, min_length=0)] = Field(None, description="The source location.  Start of a provider name, `Drive`, `LocalFs`, `AwsS3` etc.")
    type: Optional[SourceType] = None
    __properties = ["location", "type"]

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
    def from_json(cls, json_str: str) -> Source:
        """Create an instance of Source from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if location (nullable) is None
        # and __fields_set__ contains the field
        if self.location is None and "location" in self.__fields_set__:
            _dict['location'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Source:
        """Create an instance of Source from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Source.parse_obj(obj)

        _obj = Source.parse_obj({
            "location": obj.get("location"),
            "type": obj.get("type")
        })
        return _obj
