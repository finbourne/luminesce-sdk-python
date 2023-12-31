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





class CertificateType(str, Enum):
    """
    The sort of certificate being Created / Revoked / Renewed
    """

    """
    allowed enum values
    """
    DOMAIN = 'Domain'
    USER = 'User'

    @classmethod
    def from_json(cls, json_str: str) -> CertificateType:
        """Create an instance of CertificateType from a JSON string"""
        return CertificateType(json.loads(json_str))
