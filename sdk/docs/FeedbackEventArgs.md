# FeedbackEventArgs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**when** | **datetime** |  | [optional] 
**session_id** | **str** |  | [optional] 
**execution_id** | **str** |  | [optional] 
**level** | [**FeedbackLevel**](FeedbackLevel.md) |  | [optional] 
**sender** | **str** |  | [optional] 
**state_id** | **int** |  | [optional] 
**message_template** | **str** |  | [optional] 
**property_values** | **List[object]** |  | [optional] 
**message** | **str** |  | [optional] [readonly] 
## Example

```python
from luminesce.models.feedback_event_args import FeedbackEventArgs
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

when: Optional[datetime] = None
session_id: Optional[StrictStr] = "example_session_id"
execution_id: Optional[StrictStr] = "example_execution_id"
level: Optional[FeedbackLevel] = None
sender: Optional[StrictStr] = "example_sender"
state_id: Optional[StrictInt] = # Replace with your value
state_id: Optional[StrictInt] = None
message_template: Optional[StrictStr] = "example_message_template"
property_values: Optional[List[Any]] = # Replace with your value
message: Optional[StrictStr] = "example_message"
feedback_event_args_instance = FeedbackEventArgs(when=when, session_id=session_id, execution_id=execution_id, level=level, sender=sender, state_id=state_id, message_template=message_template, property_values=property_values, message=message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

