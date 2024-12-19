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
from pydantic.v1 import BaseModel, Field, StrictStr

class OptionsParquet(BaseModel):
    """
    Additional options applicable to the given SourceType  # noqa: E501
    """
    column_names_wanted: Optional[StrictStr] = Field(None, alias="columnNamesWanted", description="Column (by Name) that should be returned (comma delimited list)")
    __properties = ["columnNamesWanted"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> OptionsParquet:
        """Create an instance of OptionsParquet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if column_names_wanted (nullable) is None
        # and __fields_set__ contains the field
        if self.column_names_wanted is None and "column_names_wanted" in self.__fields_set__:
            _dict['columnNamesWanted'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OptionsParquet:
        """Create an instance of OptionsParquet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OptionsParquet.parse_obj(obj)

        _obj = OptionsParquet.parse_obj({
            "column_names_wanted": obj.get("columnNamesWanted")
        })
        return _obj
