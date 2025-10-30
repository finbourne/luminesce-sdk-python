# TableView

Representation of the table structure
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_names** | **Dict[str, Optional[str]]** | Mapping of column ids to aliases | 
**column_state** | [**List[ColumnStateType]**](ColumnStateType.md) | Array of all columns in the dashboard | 
**filters** | [**Dict[str, FilterModel]**](FilterModel.md) | Filters applied to columns in the dashboard | [optional] 
**meta** | [**TableMeta**](TableMeta.md) |  | 
## Example

```python
from luminesce.models.table_view import TableView
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

header_names: Dict[str, Optional[StrictStr]] = # Replace with your value
column_state: List[ColumnStateType] = # Replace with your value
filters: Optional[Dict[str, FilterModel]] = # Replace with your value
meta: TableMeta
table_view_instance = TableView(header_names=header_names, column_state=column_state, filters=filters, meta=meta)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

