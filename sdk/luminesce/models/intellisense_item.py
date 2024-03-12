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
from pydantic import BaseModel, Field, StrictInt, StrictStr, constr
from luminesce.models.intellisense_type import IntellisenseType

class IntellisenseItem(BaseModel):
    """
    Representation of an item in an Intellisense popup  # noqa: E501
    """
    caption: constr(strict=True, min_length=1) = Field(..., description="The value to show the user in the popup")
    value: constr(strict=True, min_length=1) = Field(..., description="The value to substitute in")
    meta: Optional[StrictStr] = Field(None, description="The light-grey text shown to the right of the Caption in the popup")
    score: Optional[StrictInt] = Field(None, description="How important is this.  Bigger is more important.")
    doc_html: Optional[StrictStr] = Field(None, alias="docHTML", description="Popup further info (as in a whole documentation article!)")
    type: Optional[IntellisenseType] = None
    __properties = ["caption", "value", "meta", "score", "docHTML", "type"]

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
    def from_json(cls, json_str: str) -> IntellisenseItem:
        """Create an instance of IntellisenseItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if meta (nullable) is None
        # and __fields_set__ contains the field
        if self.meta is None and "meta" in self.__fields_set__:
            _dict['meta'] = None

        # set to None if doc_html (nullable) is None
        # and __fields_set__ contains the field
        if self.doc_html is None and "doc_html" in self.__fields_set__:
            _dict['docHTML'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IntellisenseItem:
        """Create an instance of IntellisenseItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IntellisenseItem.parse_obj(obj)

        _obj = IntellisenseItem.parse_obj({
            "caption": obj.get("caption"),
            "value": obj.get("value"),
            "meta": obj.get("meta"),
            "score": obj.get("score"),
            "doc_html": obj.get("docHTML"),
            "type": obj.get("type")
        })
        return _obj
