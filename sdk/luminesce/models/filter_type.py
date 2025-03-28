# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class FilterType(str, Enum):
    """
    Filter categories
    """

    """
    allowed enum values
    """
    TEXT = 'text'
    NUMBER = 'number'
    BOOLEAN = 'boolean'
    DATE = 'date'
    SET = 'set'

    @classmethod
    def from_json(cls, json_str: str) -> FilterType:
        """Create an instance of FilterType from a JSON string"""
        return FilterType(json.loads(json_str))
