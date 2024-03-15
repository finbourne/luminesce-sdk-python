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


from typing import Any, Dict, List
from pydantic import BaseModel, Field, conlist, constr
from luminesce.models.error_highlight_item import ErrorHighlightItem

class ErrorHighlightResponse(BaseModel):
    """
    ErrorHighlightResponse
    """
    errors: conlist(ErrorHighlightItem) = Field(..., description="The errors within the Sql")
    sql_with_marker: constr(strict=True, min_length=1) = Field(..., alias="sqlWithMarker", description="The SQL this is for, with characters indicating the error locations")
    __properties = ["errors", "sqlWithMarker"]

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
    def from_json(cls, json_str: str) -> ErrorHighlightResponse:
        """Create an instance of ErrorHighlightResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ErrorHighlightResponse:
        """Create an instance of ErrorHighlightResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ErrorHighlightResponse.parse_obj(obj)

        _obj = ErrorHighlightResponse.parse_obj({
            "errors": [ErrorHighlightItem.from_dict(_item) for _item in obj.get("errors")] if obj.get("errors") is not None else None,
            "sql_with_marker": obj.get("sqlWithMarker")
        })
        return _obj