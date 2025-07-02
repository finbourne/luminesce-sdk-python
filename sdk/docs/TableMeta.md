# TableMeta

Representation of the table metadata
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_id** | **str** | A unique identifier for the table | 
## Example

```python
from luminesce.models.table_meta import TableMeta
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

table_id: StrictStr = "example_table_id"
table_meta_instance = TableMeta(table_id=table_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

