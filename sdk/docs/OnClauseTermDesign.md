# OnClauseTermDesign

A single on clause term (a pair of columns to join or a column to filter on)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_table_field** | **str** | Name of field in the left table to join to (complex expressions are not supported at this time) | [optional] 
**right_table_field** | **str** | Name of field in the left table to join to (complex expressions are not supported at this time) | [optional] 
**operator** | [**QueryDesignerBinaryOperator**](QueryDesignerBinaryOperator.md) |  | 
**filter_value** | **str** | The value to compare against (always as a string, but will be formatted to the correct type) | [optional] 
**filter_value_data_type** | [**DataType**](DataType.md) |  | [optional] 
## Example

```python
from luminesce.models.on_clause_term_design import OnClauseTermDesign
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

left_table_field: Optional[StrictStr] = "example_left_table_field"
right_table_field: Optional[StrictStr] = "example_right_table_field"
operator: QueryDesignerBinaryOperator = # Replace with your value
filter_value: Optional[StrictStr] = "example_filter_value"
filter_value_data_type: Optional[DataType] = # Replace with your value
on_clause_term_design_instance = OnClauseTermDesign(left_table_field=left_table_field, right_table_field=right_table_field, operator=operator, filter_value=filter_value, filter_value_data_type=filter_value_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

