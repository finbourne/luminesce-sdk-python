# FieldDesign

Treatment of a single field within a QueryDesign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Field (column name, constant, complex expression, etc.) | 
**alias** | **str** | Alias if any (if none the Name is used) | [optional] 
**data_type** | [**DataType**](DataType.md) |  | [optional] 
**should_select** | **bool** | Should this be selected? False would imply it is only being filtered on.  Ignored when Aggregations are present | [optional] 
**filters** | [**List[FilterTermDesign]**](FilterTermDesign.md) | Filter clauses to apply to this field (And&#39;ed together) | [optional] 
**aggregations** | [**List[Aggregation]**](Aggregation.md) | Aggregations to apply (as opposed to simply selecting) | [optional] 
**is_expression** | **bool** | Is this field an expression | [optional] 

## Example

```python
from luminesce.models.field_design import FieldDesign

# TODO update the JSON string below
json = "{}"
# create an instance of FieldDesign from a JSON string
field_design_instance = FieldDesign.from_json(json)
# print the JSON string representation of the object
print FieldDesign.to_json()

# convert the object into a dict
field_design_dict = field_design_instance.to_dict()
# create an instance of FieldDesign from a dict
field_design_form_dict = field_design.from_dict(field_design_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


