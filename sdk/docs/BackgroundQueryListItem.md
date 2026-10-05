# BackgroundQueryListItem

A background query the calling user currently has available to them
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | ExecutionId of the query | [optional] 
**query** | **str** | The LuminesceSql of the original request | [optional] 
**query_name** | **str** | The QueryName given in the original request | [optional] 
**state** | [**BackgroundQueryState**](BackgroundQueryState.md) |  | [optional] 
**when** | **datetime** | When the state of this query (and so its data) was last updated (UTC) | [optional] 
**expires_at** | **datetime** | When the query (and its data) may be removed (UTC) | [optional] 
## Example

```python
from luminesce.models.background_query_list_item import BackgroundQueryListItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

execution_id: Optional[StrictStr] = "example_execution_id"
query: Optional[StrictStr] = "example_query"
query_name: Optional[StrictStr] = "example_query_name"
state: Optional[BackgroundQueryState] = None
when: Optional[datetime] = # Replace with your value
expires_at: Optional[datetime] = # Replace with your value
background_query_list_item_instance = BackgroundQueryListItem(execution_id=execution_id, query=query, query_name=query_name, state=state, when=when, expires_at=expires_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

