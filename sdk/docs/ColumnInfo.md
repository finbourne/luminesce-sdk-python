# ColumnInfo

Information on how to construct a file-read sql query
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select** | **bool** | Should the column be used/selected? | [optional] 
**type** | [**DataType**](DataType.md) |  | [optional] 
**name** | **str** | The name of the column | [optional] 
**x_path** | **str** | Xpath for the column (only applicable to XML defined columns) | [optional] 
## Example

```python
from luminesce.models.column_info import ColumnInfo
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

select: Optional[StrictBool] = # Replace with your value
select:Optional[StrictBool] = None
type: Optional[DataType] = None
name: Optional[StrictStr] = "example_name"
x_path: Optional[StrictStr] = "example_x_path"
column_info_instance = ColumnInfo(select=select, type=type, name=name, x_path=x_path)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

