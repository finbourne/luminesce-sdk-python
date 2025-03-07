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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictBool, StrictInt, StrictStr 

class OptionsCsv(BaseModel):
    """
    Additional options applicable to the given SourceType  # noqa: E501
    """
    column_names:  Optional[StrictStr] = Field(None,alias="columnNames", description="Column Names either overrides the header row or steps in when there is no header row (comma delimited list)") 
    column_names_wanted:  Optional[StrictStr] = Field(None,alias="columnNamesWanted", description="Column (by Name) that should be returned (comma delimited list)") 
    column_types:  Optional[StrictStr] = Field(None,alias="columnTypes", description="Column types (comma delimited list of: '{types}', some columns may be left blank while others are specified)") 
    infer_type_row_count: Optional[StrictInt] = Field(None, alias="inferTypeRowCount", description="If non-zero and 'types' is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified")
    no_header: Optional[StrictBool] = Field(None, alias="noHeader", description="Set this if there is no header row")
    delimiter:  Optional[StrictStr] = Field(None,alias="delimiter", description="The delimiter between values (\\t for tab)") 
    escape:  Optional[StrictStr] = Field(None,alias="escape", description="Character used to escape the 'Quote' character when within a value") 
    quote:  Optional[StrictStr] = Field(None,alias="quote", description="Character used around any field containing the 'delimiter' or a line break.") 
    values_to_make_null:  Optional[StrictStr] = Field(None,alias="valuesToMakeNull", description="Regex of values to map to 'null' in the returned data.") 
    skip_pre_header: Optional[StrictInt] = Field(None, alias="skipPreHeader", description="Number of rows to ignore before the header row")
    skip_post_header: Optional[StrictInt] = Field(None, alias="skipPostHeader", description="Number of rows to ignore after the header row")
    skip_invalid_rows: Optional[StrictBool] = Field(None, alias="skipInvalidRows", description="Skip invalid data rows (totally invalid ones),   This also allows for potentially wrong data if it can be handled somewhat e.g. embedded quotes misused (and still returns such rows).  In either case a warning will show in the progress feedback.")
    __properties = ["columnNames", "columnNamesWanted", "columnTypes", "inferTypeRowCount", "noHeader", "delimiter", "escape", "quote", "valuesToMakeNull", "skipPreHeader", "skipPostHeader", "skipInvalidRows"]

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
    def from_json(cls, json_str: str) -> OptionsCsv:
        """Create an instance of OptionsCsv from a JSON string"""
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

        # set to None if column_names_wanted (nullable) is None
        # and __fields_set__ contains the field
        if self.column_names_wanted is None and "column_names_wanted" in self.__fields_set__:
            _dict['columnNamesWanted'] = None

        # set to None if column_types (nullable) is None
        # and __fields_set__ contains the field
        if self.column_types is None and "column_types" in self.__fields_set__:
            _dict['columnTypes'] = None

        # set to None if delimiter (nullable) is None
        # and __fields_set__ contains the field
        if self.delimiter is None and "delimiter" in self.__fields_set__:
            _dict['delimiter'] = None

        # set to None if escape (nullable) is None
        # and __fields_set__ contains the field
        if self.escape is None and "escape" in self.__fields_set__:
            _dict['escape'] = None

        # set to None if quote (nullable) is None
        # and __fields_set__ contains the field
        if self.quote is None and "quote" in self.__fields_set__:
            _dict['quote'] = None

        # set to None if values_to_make_null (nullable) is None
        # and __fields_set__ contains the field
        if self.values_to_make_null is None and "values_to_make_null" in self.__fields_set__:
            _dict['valuesToMakeNull'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OptionsCsv:
        """Create an instance of OptionsCsv from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OptionsCsv.parse_obj(obj)

        _obj = OptionsCsv.parse_obj({
            "column_names": obj.get("columnNames"),
            "column_names_wanted": obj.get("columnNamesWanted"),
            "column_types": obj.get("columnTypes"),
            "infer_type_row_count": obj.get("inferTypeRowCount"),
            "no_header": obj.get("noHeader"),
            "delimiter": obj.get("delimiter"),
            "escape": obj.get("escape"),
            "quote": obj.get("quote"),
            "values_to_make_null": obj.get("valuesToMakeNull"),
            "skip_pre_header": obj.get("skipPreHeader"),
            "skip_post_header": obj.get("skipPostHeader"),
            "skip_invalid_rows": obj.get("skipInvalidRows")
        })
        return _obj
