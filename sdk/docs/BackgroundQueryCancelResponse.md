# BackgroundQueryCancelResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**had_data** | **bool** |  | [optional] 
**previous_status** | [**TaskStatus**](TaskStatus.md) |  | [optional] 
**previous_state** | [**BackgroundQueryState**](BackgroundQueryState.md) |  | [optional] 
**progress** | **str** |  | [optional] 
## Example

```python
from luminesce.models.background_query_cancel_response import BackgroundQueryCancelResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

had_data: Optional[StrictBool] = # Replace with your value
had_data:Optional[StrictBool] = None
previous_status: Optional[TaskStatus] = # Replace with your value
previous_state: Optional[BackgroundQueryState] = # Replace with your value
progress: Optional[StrictStr] = "example_progress"
background_query_cancel_response_instance = BackgroundQueryCancelResponse(had_data=had_data, previous_status=previous_status, previous_state=previous_state, progress=progress)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

