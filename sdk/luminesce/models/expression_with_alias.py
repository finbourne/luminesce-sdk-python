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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, constr 
from luminesce.models.mapping_flags import MappingFlags

class ExpressionWithAlias(BaseModel):
    """
    Contract for an expression of data we \"have\" that we may \"want to map to a table-parameter's column\"  # noqa: E501
    """
    expression:  StrictStr = Field(...,alias="expression", description="Expression (column name, constant, complex expression, etc.)") 
    alias:  Optional[StrictStr] = Field(None,alias="alias", description="Column Alias for the expression") 
    flags: Optional[MappingFlags] = None
    __properties = ["expression", "alias", "flags"]

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
    def from_json(cls, json_str: str) -> ExpressionWithAlias:
        """Create an instance of ExpressionWithAlias from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if alias (nullable) is None
        # and __fields_set__ contains the field
        if self.alias is None and "alias" in self.__fields_set__:
            _dict['alias'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExpressionWithAlias:
        """Create an instance of ExpressionWithAlias from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExpressionWithAlias.parse_obj(obj)

        _obj = ExpressionWithAlias.parse_obj({
            "expression": obj.get("expression"),
            "alias": obj.get("alias"),
            "flags": obj.get("flags")
        })
        return _obj
