# OrderByTermDesign

A single clause within an Order BY
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Name of the field to order by | 
**direction** | [**OrderByDirection**](OrderByDirection.md) |  | [optional] 
**table_alias** | **str** | Table Alias of the field to order by | [optional] 
## Example

```python
from luminesce.models.order_by_term_design import OrderByTermDesign
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_field: StrictStr = "example_var_field"
direction: Optional[OrderByDirection] = None
table_alias: Optional[StrictStr] = "example_table_alias"
order_by_term_design_instance = OrderByTermDesign(var_field=var_field, direction=direction, table_alias=table_alias)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

