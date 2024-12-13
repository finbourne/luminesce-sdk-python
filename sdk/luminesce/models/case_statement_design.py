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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from luminesce.models.case_statement_item import CaseStatementItem

class CaseStatementDesign(BaseModel):
    """
    Representation of the selected field and a list of: filter, source, and target.  # noqa: E501
    """
    selected_field: Optional[StrictStr] = Field(None, alias="selectedField", description="Selected field in the SQL query.")
    case_statement_items: Optional[conlist(CaseStatementItem)] = Field(None, alias="caseStatementItems", description="A list containing the filter, source, and target.")
    __properties = ["selectedField", "caseStatementItems"]

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
    def from_json(cls, json_str: str) -> CaseStatementDesign:
        """Create an instance of CaseStatementDesign from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in case_statement_items (list)
        _items = []
        if self.case_statement_items:
            for _item in self.case_statement_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['caseStatementItems'] = _items
        # set to None if selected_field (nullable) is None
        # and __fields_set__ contains the field
        if self.selected_field is None and "selected_field" in self.__fields_set__:
            _dict['selectedField'] = None

        # set to None if case_statement_items (nullable) is None
        # and __fields_set__ contains the field
        if self.case_statement_items is None and "case_statement_items" in self.__fields_set__:
            _dict['caseStatementItems'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CaseStatementDesign:
        """Create an instance of CaseStatementDesign from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CaseStatementDesign.parse_obj(obj)

        _obj = CaseStatementDesign.parse_obj({
            "selected_field": obj.get("selectedField"),
            "case_statement_items": [CaseStatementItem.from_dict(_item) for _item in obj.get("caseStatementItems")] if obj.get("caseStatementItems") is not None else None
        })
        return _obj
