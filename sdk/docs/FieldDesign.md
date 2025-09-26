# FieldDesign

Treatment of a single field within a QueryDesign
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Field (column name, constant, complex expression, etc.) | 
**table_alias** | **str** | Alias of the Table the field belongs to | [optional] 
**alias** | **str** | Alias if any (if none the Name is used) | [optional] 
**data_type** | [**DataType**](DataType.md) |  | [optional] 
**should_select** | **bool** | Should this be selected? False would imply it is only being filtered on. Ignored when Aggregations are present | [optional] 
**filters** | [**List[FilterTermDesign]**](FilterTermDesign.md) | Filter clauses to apply to this field (And&#39;ed together) | [optional] 
**aggregations** | [**List[Aggregation]**](Aggregation.md) | Aggregations to apply (as opposed to simply selecting) | [optional] 
**is_expression** | **bool** | Is this field an expression | [optional] 
## Example

```python
from luminesce.models.field_design import FieldDesign
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, conlist, constr

name: StrictStr = "example_name"
table_alias: Optional[StrictStr] = "example_table_alias"
alias: Optional[StrictStr] = "example_alias"
data_type: Optional[DataType] = # Replace with your value
should_select: Optional[StrictBool] = # Replace with your value
should_select:Optional[StrictBool] = None
filters: Optional[conlist(FilterTermDesign)] = # Replace with your value
aggregations: Optional[conlist(Aggregation)] = # Replace with your value
is_expression: Optional[StrictBool] = # Replace with your value
is_expression:Optional[StrictBool] = None
field_design_instance = FieldDesign(name=name, table_alias=table_alias, alias=alias, data_type=data_type, should_select=should_select, filters=filters, aggregations=aggregations, is_expression=is_expression)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

