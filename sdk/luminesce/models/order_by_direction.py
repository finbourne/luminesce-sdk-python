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





class OrderByDirection(str, Enum):
    """
    Direction of Order By terms in the Order By clause
    """

    """
    allowed enum values
    """
    ASC = 'asc'
    DESC = 'desc'

    @classmethod
    def from_json(cls, json_str: str) -> OrderByDirection:
        """Create an instance of OrderByDirection from a JSON string"""
        return OrderByDirection(json.loads(json_str))