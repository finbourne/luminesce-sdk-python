# BackgroundMultiQueryProgressResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**progress** | **str** | The full progress log (up to this point at least) | [optional] 
**feedback** | [**List[FeedbackEventArgs]**](FeedbackEventArgs.md) | Individual Feedback Messages (to replace Progress).  A given message will be returned from only one call. | [optional] 
**status** | [**TaskStatus**](TaskStatus.md) |  | [optional] 
**queries** | [**List[BackgroundQueryProgressResponse]**](BackgroundQueryProgressResponse.md) |  | [optional] 
## Example

```python
from luminesce.models.background_multi_query_progress_response import BackgroundMultiQueryProgressResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

progress: Optional[StrictStr] = "example_progress"
feedback: Optional[conlist(FeedbackEventArgs)] = # Replace with your value
status: Optional[TaskStatus] = None
queries: Optional[conlist(BackgroundQueryProgressResponse)] = None
background_multi_query_progress_response_instance = BackgroundMultiQueryProgressResponse(progress=progress, feedback=feedback, status=status, queries=queries)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

