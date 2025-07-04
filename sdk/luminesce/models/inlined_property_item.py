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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictBool, StrictStr, constr 

class InlinedPropertyItem(BaseModel):
    """
    Information about a inlined property so that decorated properties can be inlined into luminesce  # noqa: E501
    """
    key:  StrictStr = Field(...,alias="key", description="Key of the property") 
    name:  Optional[StrictStr] = Field(None,alias="name", description="Name of the property") 
    is_main: Optional[StrictBool] = Field(None, alias="isMain", description="Is Main indicator for the property")
    description:  Optional[StrictStr] = Field(None,alias="description", description="Description of the property") 
    data_type:  Optional[StrictStr] = Field(None,alias="dataType", description="Data type of the property") 
    __properties = ["key", "name", "isMain", "description", "dataType"]

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
    def from_json(cls, json_str: str) -> InlinedPropertyItem:
        """Create an instance of InlinedPropertyItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if data_type (nullable) is None
        # and __fields_set__ contains the field
        if self.data_type is None and "data_type" in self.__fields_set__:
            _dict['dataType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InlinedPropertyItem:
        """Create an instance of InlinedPropertyItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InlinedPropertyItem.parse_obj(obj)

        _obj = InlinedPropertyItem.parse_obj({
            "key": obj.get("key"),
            "name": obj.get("name"),
            "is_main": obj.get("isMain"),
            "description": obj.get("description"),
            "data_type": obj.get("dataType")
        })
        return _obj
