# OrderByTermDesign

A single clause within an Order BY
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Name of the field to order by | 
**direction** | [**OrderByDirection**](OrderByDirection.md) |  | [optional] 
## Example

```python
from luminesce.models.order_by_term_design import OrderByTermDesign
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

field: StrictStr = "example_field"
direction: Optional[OrderByDirection] = None
order_by_term_design_instance = OrderByTermDesign(field=field, direction=direction)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

