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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, conlist 
from luminesce.models.column_info import ColumnInfo

class FileReaderBuilderResponse(BaseModel):
    """
    Information on how to construct a file-read sql query  # noqa: E501
    """
    query:  Optional[StrictStr] = Field(None,alias="query", description="The generated SQL") 
    error:  Optional[StrictStr] = Field(None,alias="error", description="The error from running generated SQL Query, if any") 
    columns: Optional[conlist(ColumnInfo)] = Field(None, description="Column information for the results")
    data: Optional[Any] = Field(None, description="The resulting data from running the Query")
    __properties = ["query", "error", "columns", "data"]

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
    def from_json(cls, json_str: str) -> FileReaderBuilderResponse:
        """Create an instance of FileReaderBuilderResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in columns (list)
        _items = []
        if self.columns:
            for _item in self.columns:
                if _item:
                    _items.append(_item.to_dict())
            _dict['columns'] = _items
        # set to None if query (nullable) is None
        # and __fields_set__ contains the field
        if self.query is None and "query" in self.__fields_set__:
            _dict['query'] = None

        # set to None if error (nullable) is None
        # and __fields_set__ contains the field
        if self.error is None and "error" in self.__fields_set__:
            _dict['error'] = None

        # set to None if columns (nullable) is None
        # and __fields_set__ contains the field
        if self.columns is None and "columns" in self.__fields_set__:
            _dict['columns'] = None

        # set to None if data (nullable) is None
        # and __fields_set__ contains the field
        if self.data is None and "data" in self.__fields_set__:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FileReaderBuilderResponse:
        """Create an instance of FileReaderBuilderResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FileReaderBuilderResponse.parse_obj(obj)

        _obj = FileReaderBuilderResponse.parse_obj({
            "query": obj.get("query"),
            "error": obj.get("error"),
            "columns": [ColumnInfo.from_dict(_item) for _item in obj.get("columns")] if obj.get("columns") is not None else None,
            "data": obj.get("data")
        })
        return _obj
