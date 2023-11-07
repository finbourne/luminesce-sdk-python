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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class OptionsExcel(BaseModel):
    """
    Additional options applicable to the given SourceType  # noqa: E501
    """
    column_names: Optional[StrictStr] = Field(None, alias="columnNames", description="Column Names either overrides the header row or steps in when there is no header row (comma delimited list)")
    column_types: Optional[StrictStr] = Field(None, alias="columnTypes", description="Column types (comma delimited list of: '{types}', some columns may be left blank while others are specified)")
    infer_type_row_count: Optional[StrictInt] = Field(None, alias="inferTypeRowCount", description="If non-zero and 'types' is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified")
    no_header: Optional[StrictBool] = Field(None, alias="noHeader", description="Set this if there is no header row")
    calculate: Optional[StrictBool] = Field(None, description="Whether to attempt a calculation of the imported cell range prior to import")
    password: Optional[StrictStr] = Field(None, description="If specified will be used as the password used for password protected workbooks")
    worksheet: Optional[StrictStr] = Field(None, description="The worksheet containing the cell range to import (name or index, will default to first)")
    range_or_table: Optional[StrictStr] = Field(None, alias="rangeOrTable", description="The cell range to import as either a specified range or a table name")
    ignore_invalid_cells: Optional[StrictBool] = Field(None, alias="ignoreInvalidCells", description="If specified cells which can not be successfully converted to the target type will be ignored")
    ignore_blank_rows: Optional[StrictBool] = Field(None, alias="ignoreBlankRows", description="If the entire rows has only blank cells it will be ignored will be ignored")
    __properties = ["columnNames", "columnTypes", "inferTypeRowCount", "noHeader", "calculate", "password", "worksheet", "rangeOrTable", "ignoreInvalidCells", "ignoreBlankRows"]

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
    def from_json(cls, json_str: str) -> OptionsExcel:
        """Create an instance of OptionsExcel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if column_names (nullable) is None
        # and __fields_set__ contains the field
        if self.column_names is None and "column_names" in self.__fields_set__:
            _dict['columnNames'] = None

        # set to None if column_types (nullable) is None
        # and __fields_set__ contains the field
        if self.column_types is None and "column_types" in self.__fields_set__:
            _dict['columnTypes'] = None

        # set to None if password (nullable) is None
        # and __fields_set__ contains the field
        if self.password is None and "password" in self.__fields_set__:
            _dict['password'] = None

        # set to None if worksheet (nullable) is None
        # and __fields_set__ contains the field
        if self.worksheet is None and "worksheet" in self.__fields_set__:
            _dict['worksheet'] = None

        # set to None if range_or_table (nullable) is None
        # and __fields_set__ contains the field
        if self.range_or_table is None and "range_or_table" in self.__fields_set__:
            _dict['rangeOrTable'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OptionsExcel:
        """Create an instance of OptionsExcel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OptionsExcel.parse_obj(obj)

        _obj = OptionsExcel.parse_obj({
            "column_names": obj.get("columnNames"),
            "column_types": obj.get("columnTypes"),
            "infer_type_row_count": obj.get("inferTypeRowCount"),
            "no_header": obj.get("noHeader"),
            "calculate": obj.get("calculate"),
            "password": obj.get("password"),
            "worksheet": obj.get("worksheet"),
            "range_or_table": obj.get("rangeOrTable"),
            "ignore_invalid_cells": obj.get("ignoreInvalidCells"),
            "ignore_blank_rows": obj.get("ignoreBlankRows")
        })
        return _obj