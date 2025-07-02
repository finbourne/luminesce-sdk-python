# TableView

Representation of the table structure
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_names** | **Dict[str, str]** | Mapping of column ids to aliases | 
**column_state** | [**List[ColumnStateType]**](ColumnStateType.md) | Array of all columns in the dashboard | 
**filters** | [**Dict[str, FilterModel]**](FilterModel.md) | Filters applied to columns in the dashboard | [optional] 
**meta** | [**TableMeta**](TableMeta.md) |  | 
## Example

```python
from luminesce.models.table_view import TableView
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

header_names: Dict[str, StrictStr] = # Replace with your value
column_state: conlist(ColumnStateType) = # Replace with your value
filters: Optional[Dict[str, FilterModel]] = # Replace with your value
meta: TableMeta = # Replace with your value
table_view_instance = TableView(header_names=header_names, column_state=column_state, filters=filters, meta=meta)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

