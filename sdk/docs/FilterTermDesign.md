# FilterTermDesign

A single filter clause
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | [**QueryDesignerBinaryOperator**](QueryDesignerBinaryOperator.md) |  | 
**value** | **str** | The value to compare against (always as a string, but will be formatted to the correct type) | 
## Example

```python
from luminesce.models.filter_term_design import FilterTermDesign
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

operator: QueryDesignerBinaryOperator = # Replace with your value
value: StrictStr = "example_value"
filter_term_design_instance = FilterTermDesign(operator=operator, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

