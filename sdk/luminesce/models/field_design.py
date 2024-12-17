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
from pydantic.v1 import BaseModel, Field, StrictBool, conlist, constr, Field
from luminesce.models.aggregation import Aggregation
from luminesce.models.data_type import DataType
from luminesce.models.filter_term_design import FilterTermDesign

class FieldDesign(BaseModel):
    """
    Treatment of a single field within a QueryDesign  # noqa: E501
    """
    name: constr(strict=True) = Field(...,alias="name", description="Name of the Field") 
    alias: constr(strict=True) = Field(None,alias="alias", description="Alias if any (if none the Name is used)") 
    data_type: Optional[DataType] = Field(None, alias="dataType")
    should_select: Optional[StrictBool] = Field(None, alias="shouldSelect", description="Should this be selected? False would imply it is only being filtered on.  Ignored when Aggregations are present")
    filters: Optional[conlist(FilterTermDesign)] = Field(None, description="Filter clauses to apply to this field (And'ed together)")
    aggregations: Optional[conlist(Aggregation)] = Field(None, description="Aggregations to apply (as opposed to simply selecting)")
    __properties = ["name", "alias", "dataType", "shouldSelect", "filters", "aggregations"]

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
    def from_json(cls, json_str: str) -> FieldDesign:
        """Create an instance of FieldDesign from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item in self.filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['filters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in aggregations (list)
        _items = []
        if self.aggregations:
            for _item in self.aggregations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['aggregations'] = _items
        # set to None if alias (nullable) is None
        # and __fields_set__ contains the field
        if self.alias is None and "alias" in self.__fields_set__:
            _dict['alias'] = None

        # set to None if filters (nullable) is None
        # and __fields_set__ contains the field
        if self.filters is None and "filters" in self.__fields_set__:
            _dict['filters'] = None

        # set to None if aggregations (nullable) is None
        # and __fields_set__ contains the field
        if self.aggregations is None and "aggregations" in self.__fields_set__:
            _dict['aggregations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FieldDesign:
        """Create an instance of FieldDesign from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FieldDesign.parse_obj(obj)

        _obj = FieldDesign.parse_obj({
            "name": obj.get("name"),
            "alias": obj.get("alias"),
            "data_type": obj.get("dataType"),
            "should_select": obj.get("shouldSelect"),
            "filters": [FilterTermDesign.from_dict(_item) for _item in obj.get("filters")] if obj.get("filters") is not None else None,
            "aggregations": [Aggregation.from_dict(_item) for _item in obj.get("aggregations")] if obj.get("aggregations") is not None else None
        })
        return _obj
