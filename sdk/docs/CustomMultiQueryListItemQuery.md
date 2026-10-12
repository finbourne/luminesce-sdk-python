# CustomMultiQueryListItemQuery

One of the queries of a Finbourne.Honeycomb.WebApi.BackgroundQueries.MultiQuery.CustomMultiQueryListItem
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name given to the query in the original request | [optional] 
**state** | [**BackgroundQueryState**](BackgroundQueryState.md) |  | [optional] 
**has_result** | **bool** | Whether its results may be fetched | [optional] 
## Example

```python
from luminesce.models.custom_multi_query_list_item_query import CustomMultiQueryListItemQuery
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: Optional[StrictStr] = "example_name"
state: Optional[BackgroundQueryState] = None
has_result: Optional[StrictBool] = # Replace with your value
has_result:Optional[StrictBool] = None
custom_multi_query_list_item_query_instance = CustomMultiQueryListItemQuery(name=name, state=state, has_result=has_result)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

