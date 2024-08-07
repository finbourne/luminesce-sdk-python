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





class BackgroundQueryState(str, Enum):
    """
    BackgroundQueryState
    """

    """
    allowed enum values
    """
    NEW = 'New'
    RUNNING = 'Running'
    ERRORED = 'Errored'
    CANCELLED = 'Cancelled'
    EXECUTED = 'Executed'
    EXECUTEDNOSERIALIZATIONREQUIRED = 'ExecutedNoSerializationRequired'
    SERIALIZED = 'Serialized'
    SERIALIZATIONFAILED = 'SerializationFailed'
    ATTEMPTINGTODESERIALIZE = 'AttemptingToDeserialize'
    LOADED = 'Loaded'
    CLEARED = 'Cleared'
    DISPOSED = 'Disposed'
    OWNERTERMINATED = 'OwnerTerminated'

    @classmethod
    def from_json(cls, json_str: str) -> BackgroundQueryState:
        """Create an instance of BackgroundQueryState from a JSON string"""
        return BackgroundQueryState(json.loads(json_str))
