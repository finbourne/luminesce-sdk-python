# CustomMultiQueryListItem

A custom multi-query the calling user currently has results of available to them
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | ExecutionId of the multi-query, its queries having ExecutionIds of &#x60;{ExecutionId}_{Name}&#x60; | [optional] 
**query_name** | **str** | The QueryName given in the original request | [optional] 
**state** | [**BackgroundQueryState**](BackgroundQueryState.md) |  | [optional] 
**started_at** | **datetime** | When it was started (UTC) | [optional] 
**when** | **datetime** | When the state of it was last updated (UTC) | [optional] 
**expires_at** | **datetime** | When it (and the data of its queries) may be removed (UTC) | [optional] 
**queries** | [**List[CustomMultiQueryListItemQuery]**](CustomMultiQueryListItemQuery.md) | Its queries whose results may be fetched (those that are external results), in request order | [optional] 
## Example

```python
from luminesce.models.custom_multi_query_list_item import CustomMultiQueryListItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

execution_id: Optional[StrictStr] = "example_execution_id"
query_name: Optional[StrictStr] = "example_query_name"
state: Optional[BackgroundQueryState] = None
started_at: Optional[datetime] = # Replace with your value
when: Optional[datetime] = # Replace with your value
expires_at: Optional[datetime] = # Replace with your value
queries: Optional[List[CustomMultiQueryListItemQuery]] = # Replace with your value
custom_multi_query_list_item_instance = CustomMultiQueryListItem(execution_id=execution_id, query_name=query_name, state=state, started_at=started_at, when=when, expires_at=expires_at, queries=queries)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

