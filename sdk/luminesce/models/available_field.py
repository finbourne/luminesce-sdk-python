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
from pydantic.v1 import BaseModel, Field, StrictBool, constr
from luminesce.models.data_type import DataType
from luminesce.models.field_type import FieldType

class AvailableField(BaseModel):
    """
    Information about a field that can be designed on (regardless if it currently is)  Kind of a \"mini-available catalog entry\"  # noqa: E501
    """
    name: constr(strict=True, max_length=256, min_length=0) = Field(..., description="Name of the Field")
    data_type: Optional[DataType] = Field(None, alias="dataType")
    field_type: FieldType = Field(..., alias="fieldType")
    is_main: Optional[StrictBool] = Field(None, alias="isMain", description="Is this a Main Field within the Provider")
    is_primary_key: Optional[StrictBool] = Field(None, alias="isPrimaryKey", description="Is this a member of the PrimaryKey of the Provider")
    __properties = ["name", "dataType", "fieldType", "isMain", "isPrimaryKey"]

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
    def from_json(cls, json_str: str) -> AvailableField:
        """Create an instance of AvailableField from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if is_main (nullable) is None
        # and __fields_set__ contains the field
        if self.is_main is None and "is_main" in self.__fields_set__:
            _dict['isMain'] = None

        # set to None if is_primary_key (nullable) is None
        # and __fields_set__ contains the field
        if self.is_primary_key is None and "is_primary_key" in self.__fields_set__:
            _dict['isPrimaryKey'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AvailableField:
        """Create an instance of AvailableField from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AvailableField.parse_obj(obj)

        _obj = AvailableField.parse_obj({
            "name": obj.get("name"),
            "data_type": obj.get("dataType"),
            "field_type": obj.get("fieldType"),
            "is_main": obj.get("isMain"),
            "is_primary_key": obj.get("isPrimaryKey")
        })
        return _obj
