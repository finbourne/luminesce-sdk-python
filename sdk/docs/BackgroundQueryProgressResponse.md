# BackgroundQueryProgressResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_data** | **bool** | Is there currently data for this Query? | [optional] 
**row_count** | **int** | Number of rows of data held. -1 if none as yet. | [optional] 
**status** | [**TaskStatus**](TaskStatus.md) |  | [optional] 
**state** | [**BackgroundQueryState**](BackgroundQueryState.md) |  | [optional] 
**progress** | **str** | The full progress log (up to this point at least) | [optional] 
**feedback** | [**List[FeedbackEventArgs]**](FeedbackEventArgs.md) | Individual Feedback Messages (to replace Progress).  A given message will be returned from only one call. | [optional] 
**query** | **str** | The LuminesceSql of the original request | [optional] 
**query_name** | **str** | The QueryName given in the original request | [optional] 
**columns_available** | [**List[Column]**](Column.md) | When HasData is true this is the schema of columns that will be returned if the data is requested | [optional] 
**lineage** | [**TableLineage**](TableLineage.md) |  | [optional] 
## Example

```python
from luminesce.models.background_query_progress_response import BackgroundQueryProgressResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

has_data: Optional[StrictBool] = # Replace with your value
has_data:Optional[StrictBool] = None
row_count: Optional[StrictInt] = # Replace with your value
row_count: Optional[StrictInt] = None
status: Optional[TaskStatus] = None
state: Optional[BackgroundQueryState] = None
progress: Optional[StrictStr] = "example_progress"
feedback: Optional[List[FeedbackEventArgs]] = # Replace with your value
query: Optional[StrictStr] = "example_query"
query_name: Optional[StrictStr] = "example_query_name"
columns_available: Optional[List[Column]] = # Replace with your value
lineage: Optional[TableLineage] = None
background_query_progress_response_instance = BackgroundQueryProgressResponse(has_data=has_data, row_count=row_count, status=status, state=state, progress=progress, feedback=feedback, query=query, query_name=query_name, columns_available=columns_available, lineage=lineage)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

