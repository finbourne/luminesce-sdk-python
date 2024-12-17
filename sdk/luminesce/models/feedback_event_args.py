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

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist, Field
from luminesce.models.feedback_level import FeedbackLevel

class FeedbackEventArgs(BaseModel):
    """
    FeedbackEventArgs
    """
    when: Optional[datetime] = None
    session_id: constr(strict=True) = Field(None,alias="sessionId") 
    execution_id: constr(strict=True) = Field(None,alias="executionId") 
    level: Optional[FeedbackLevel] = None
    sender: constr(strict=True) = Field(None,alias="sender") 
    state_id: Optional[StrictInt] = Field(None, alias="stateId")
    message_template: constr(strict=True) = Field(None,alias="messageTemplate") 
    property_values: Optional[conlist(Any)] = Field(None, alias="propertyValues")
    message: constr(strict=True) = Field(None,alias="message") 
    __properties = ["when", "sessionId", "executionId", "level", "sender", "stateId", "messageTemplate", "propertyValues", "message"]

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
    def from_json(cls, json_str: str) -> FeedbackEventArgs:
        """Create an instance of FeedbackEventArgs from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "message",
                          },
                          exclude_none=True)
        # set to None if sender (nullable) is None
        # and __fields_set__ contains the field
        if self.sender is None and "sender" in self.__fields_set__:
            _dict['sender'] = None

        # set to None if state_id (nullable) is None
        # and __fields_set__ contains the field
        if self.state_id is None and "state_id" in self.__fields_set__:
            _dict['stateId'] = None

        # set to None if message_template (nullable) is None
        # and __fields_set__ contains the field
        if self.message_template is None and "message_template" in self.__fields_set__:
            _dict['messageTemplate'] = None

        # set to None if property_values (nullable) is None
        # and __fields_set__ contains the field
        if self.property_values is None and "property_values" in self.__fields_set__:
            _dict['propertyValues'] = None

        # set to None if message (nullable) is None
        # and __fields_set__ contains the field
        if self.message is None and "message" in self.__fields_set__:
            _dict['message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FeedbackEventArgs:
        """Create an instance of FeedbackEventArgs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FeedbackEventArgs.parse_obj(obj)

        _obj = FeedbackEventArgs.parse_obj({
            "when": obj.get("when"),
            "session_id": obj.get("sessionId"),
            "execution_id": obj.get("executionId"),
            "level": obj.get("level"),
            "sender": obj.get("sender"),
            "state_id": obj.get("stateId"),
            "message_template": obj.get("messageTemplate"),
            "property_values": obj.get("propertyValues"),
            "message": obj.get("message")
        })
        return _obj
