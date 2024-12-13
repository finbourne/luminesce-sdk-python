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


from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr
from luminesce.models.available_parameter import AvailableParameter
from luminesce.models.expression_with_alias import ExpressionWithAlias

class WriterDesign(BaseModel):
    """
    Representation of a \"designable Query for a writer\" suitable for formatting to SQL or being built from compliant SQL.  # noqa: E501
    """
    sql: constr(strict=True, min_length=1) = Field(..., description="Original SQL that started this off")
    available_to_map_from: Optional[conlist(ExpressionWithAlias)] = Field(None, alias="availableToMapFrom", description="The data able to be mapped from as derived from the Sql")
    parameter: Optional[AvailableParameter] = None
    available_parameters: Optional[conlist(AvailableParameter)] = Field(None, alias="availableParameters", description="All the parameter the user may wish to design")
    __properties = ["sql", "availableToMapFrom", "parameter", "availableParameters"]

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
    def from_json(cls, json_str: str) -> WriterDesign:
        """Create an instance of WriterDesign from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in available_to_map_from (list)
        _items = []
        if self.available_to_map_from:
            for _item in self.available_to_map_from:
                if _item:
                    _items.append(_item.to_dict())
            _dict['availableToMapFrom'] = _items
        # override the default output from pydantic by calling `to_dict()` of parameter
        if self.parameter:
            _dict['parameter'] = self.parameter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in available_parameters (list)
        _items = []
        if self.available_parameters:
            for _item in self.available_parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['availableParameters'] = _items
        # set to None if available_to_map_from (nullable) is None
        # and __fields_set__ contains the field
        if self.available_to_map_from is None and "available_to_map_from" in self.__fields_set__:
            _dict['availableToMapFrom'] = None

        # set to None if available_parameters (nullable) is None
        # and __fields_set__ contains the field
        if self.available_parameters is None and "available_parameters" in self.__fields_set__:
            _dict['availableParameters'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WriterDesign:
        """Create an instance of WriterDesign from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WriterDesign.parse_obj(obj)

        _obj = WriterDesign.parse_obj({
            "sql": obj.get("sql"),
            "available_to_map_from": [ExpressionWithAlias.from_dict(_item) for _item in obj.get("availableToMapFrom")] if obj.get("availableToMapFrom") is not None else None,
            "parameter": AvailableParameter.from_dict(obj.get("parameter")) if obj.get("parameter") is not None else None,
            "available_parameters": [AvailableParameter.from_dict(_item) for _item in obj.get("availableParameters")] if obj.get("availableParameters") is not None else None
        })
        return _obj
