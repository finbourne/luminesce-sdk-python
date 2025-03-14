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
from luminesce.models.link import Link

class BackgroundMultiQueryResponse(BaseModel):
    """
    BackgroundMultiQueryResponse
    """
    execution_id:  Optional[StrictStr] = Field(None,alias="executionId") 
    progress: Optional[Link] = None
    cancel: Optional[Link] = None
    fetch_json: Optional[conlist(Link)] = Field(None, alias="fetchJson", description="Json (as a string) data request links for all of the child queries")
    fetch_json_proper: Optional[conlist(Link)] = Field(None, alias="fetchJsonProper", description="Json-proper data request links for all of the child queries")
    fetch_xml: Optional[conlist(Link)] = Field(None, alias="fetchXml", description="Xml data request links for all of the child queries")
    fetch_parquet: Optional[conlist(Link)] = Field(None, alias="fetchParquet", description="Parquet data request links for all of the child queries")
    fetch_csv: Optional[conlist(Link)] = Field(None, alias="fetchCsv", description="CSV data request links for all of the child queries")
    fetch_pipe: Optional[conlist(Link)] = Field(None, alias="fetchPipe", description="Pipe delimited data request links for all of the child queries")
    fetch_excel: Optional[conlist(Link)] = Field(None, alias="fetchExcel", description="Excel workbook data request links for all of the child queries")
    fetch_sqlite: Optional[conlist(Link)] = Field(None, alias="fetchSqlite", description="SqLite DB data request links for all of the child queries")
    histogram: Optional[conlist(Link)] = Field(None, description="Histogram links for all of the child queries")
    __properties = ["executionId", "progress", "cancel", "fetchJson", "fetchJsonProper", "fetchXml", "fetchParquet", "fetchCsv", "fetchPipe", "fetchExcel", "fetchSqlite", "histogram"]

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
    def from_json(cls, json_str: str) -> BackgroundMultiQueryResponse:
        """Create an instance of BackgroundMultiQueryResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "execution_id",
                            "fetch_json",
                            "fetch_json_proper",
                            "fetch_xml",
                            "fetch_parquet",
                            "fetch_csv",
                            "fetch_pipe",
                            "fetch_excel",
                            "fetch_sqlite",
                            "histogram",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of progress
        if self.progress:
            _dict['progress'] = self.progress.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cancel
        if self.cancel:
            _dict['cancel'] = self.cancel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fetch_json (list)
        _items = []
        if self.fetch_json:
            for _item in self.fetch_json:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fetchJson'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fetch_json_proper (list)
        _items = []
        if self.fetch_json_proper:
            for _item in self.fetch_json_proper:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fetchJsonProper'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fetch_xml (list)
        _items = []
        if self.fetch_xml:
            for _item in self.fetch_xml:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fetchXml'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fetch_parquet (list)
        _items = []
        if self.fetch_parquet:
            for _item in self.fetch_parquet:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fetchParquet'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fetch_csv (list)
        _items = []
        if self.fetch_csv:
            for _item in self.fetch_csv:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fetchCsv'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fetch_pipe (list)
        _items = []
        if self.fetch_pipe:
            for _item in self.fetch_pipe:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fetchPipe'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fetch_excel (list)
        _items = []
        if self.fetch_excel:
            for _item in self.fetch_excel:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fetchExcel'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fetch_sqlite (list)
        _items = []
        if self.fetch_sqlite:
            for _item in self.fetch_sqlite:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fetchSqlite'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in histogram (list)
        _items = []
        if self.histogram:
            for _item in self.histogram:
                if _item:
                    _items.append(_item.to_dict())
            _dict['histogram'] = _items
        # set to None if fetch_json (nullable) is None
        # and __fields_set__ contains the field
        if self.fetch_json is None and "fetch_json" in self.__fields_set__:
            _dict['fetchJson'] = None

        # set to None if fetch_json_proper (nullable) is None
        # and __fields_set__ contains the field
        if self.fetch_json_proper is None and "fetch_json_proper" in self.__fields_set__:
            _dict['fetchJsonProper'] = None

        # set to None if fetch_xml (nullable) is None
        # and __fields_set__ contains the field
        if self.fetch_xml is None and "fetch_xml" in self.__fields_set__:
            _dict['fetchXml'] = None

        # set to None if fetch_parquet (nullable) is None
        # and __fields_set__ contains the field
        if self.fetch_parquet is None and "fetch_parquet" in self.__fields_set__:
            _dict['fetchParquet'] = None

        # set to None if fetch_csv (nullable) is None
        # and __fields_set__ contains the field
        if self.fetch_csv is None and "fetch_csv" in self.__fields_set__:
            _dict['fetchCsv'] = None

        # set to None if fetch_pipe (nullable) is None
        # and __fields_set__ contains the field
        if self.fetch_pipe is None and "fetch_pipe" in self.__fields_set__:
            _dict['fetchPipe'] = None

        # set to None if fetch_excel (nullable) is None
        # and __fields_set__ contains the field
        if self.fetch_excel is None and "fetch_excel" in self.__fields_set__:
            _dict['fetchExcel'] = None

        # set to None if fetch_sqlite (nullable) is None
        # and __fields_set__ contains the field
        if self.fetch_sqlite is None and "fetch_sqlite" in self.__fields_set__:
            _dict['fetchSqlite'] = None

        # set to None if histogram (nullable) is None
        # and __fields_set__ contains the field
        if self.histogram is None and "histogram" in self.__fields_set__:
            _dict['histogram'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BackgroundMultiQueryResponse:
        """Create an instance of BackgroundMultiQueryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BackgroundMultiQueryResponse.parse_obj(obj)

        _obj = BackgroundMultiQueryResponse.parse_obj({
            "execution_id": obj.get("executionId"),
            "progress": Link.from_dict(obj.get("progress")) if obj.get("progress") is not None else None,
            "cancel": Link.from_dict(obj.get("cancel")) if obj.get("cancel") is not None else None,
            "fetch_json": [Link.from_dict(_item) for _item in obj.get("fetchJson")] if obj.get("fetchJson") is not None else None,
            "fetch_json_proper": [Link.from_dict(_item) for _item in obj.get("fetchJsonProper")] if obj.get("fetchJsonProper") is not None else None,
            "fetch_xml": [Link.from_dict(_item) for _item in obj.get("fetchXml")] if obj.get("fetchXml") is not None else None,
            "fetch_parquet": [Link.from_dict(_item) for _item in obj.get("fetchParquet")] if obj.get("fetchParquet") is not None else None,
            "fetch_csv": [Link.from_dict(_item) for _item in obj.get("fetchCsv")] if obj.get("fetchCsv") is not None else None,
            "fetch_pipe": [Link.from_dict(_item) for _item in obj.get("fetchPipe")] if obj.get("fetchPipe") is not None else None,
            "fetch_excel": [Link.from_dict(_item) for _item in obj.get("fetchExcel")] if obj.get("fetchExcel") is not None else None,
            "fetch_sqlite": [Link.from_dict(_item) for _item in obj.get("fetchSqlite")] if obj.get("fetchSqlite") is not None else None,
            "histogram": [Link.from_dict(_item) for _item in obj.get("histogram")] if obj.get("histogram") is not None else None
        })
        return _obj
