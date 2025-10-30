# ColumnStateType

Representation of a column within the grid
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**col_id** | **str** | Unique identifier for the column | 
**hide** | **bool** | Flag to determine whether the column is visible in the grid | 
**sort** | **str** | The sort order (asc or desc) | [optional] 
**sort_index** | **int** | The index of the sort to determine the order in which the sorts are applied | [optional] 
## Example

```python
from luminesce.models.column_state_type import ColumnStateType
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

col_id: StrictStr = "example_col_id"
hide: StrictBool = # Replace with your value
hide:StrictBool = True
sort: Optional[StrictStr] = "example_sort"
sort_index: Optional[StrictInt] = # Replace with your value
sort_index: Optional[StrictInt] = None
column_state_type_instance = ColumnStateType(col_id=col_id, hide=hide, sort=sort, sort_index=sort_index)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

