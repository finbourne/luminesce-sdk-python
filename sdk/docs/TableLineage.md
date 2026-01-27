# TableLineage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_lineage** | [**List[Lineage]**](Lineage.md) |  | [optional] 
**row_lineage** | [**Lineage**](Lineage.md) |  | [optional] 
**failure_reason** | **str** |  | [optional] 
## Example

```python
from luminesce.models.table_lineage import TableLineage
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

column_lineage: Optional[List[Lineage]] = # Replace with your value
row_lineage: Optional[Lineage] = # Replace with your value
failure_reason: Optional[StrictStr] = "example_failure_reason"
table_lineage_instance = TableLineage(column_lineage=column_lineage, row_lineage=row_lineage, failure_reason=failure_reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

