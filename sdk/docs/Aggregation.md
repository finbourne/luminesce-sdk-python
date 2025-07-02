# Aggregation

How to aggregate over a field
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AggregateFunction**](AggregateFunction.md) |  | 
**alias** | **str** | Alias, if any, for the Aggregate expression when selected | [optional] 
## Example

```python
from luminesce.models.aggregation import Aggregation
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

type: AggregateFunction = # Replace with your value
alias: Optional[StrictStr] = "example_alias"
aggregation_instance = Aggregation(type=type, alias=alias)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

