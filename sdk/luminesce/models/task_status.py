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





class TaskStatus(str, Enum):
    """
    TaskStatus
    """

    """
    allowed enum values
    """
    CREATED = 'Created'
    WAITINGFORACTIVATION = 'WaitingForActivation'
    WAITINGTORUN = 'WaitingToRun'
    RUNNING = 'Running'
    WAITINGFORCHILDRENTOCOMPLETE = 'WaitingForChildrenToComplete'
    RANTOCOMPLETION = 'RanToCompletion'
    CANCELED = 'Canceled'
    FAULTED = 'Faulted'

    @classmethod
    def from_json(cls, json_str: str) -> TaskStatus:
        """Create an instance of TaskStatus from a JSON string"""
        return TaskStatus(json.loads(json_str))