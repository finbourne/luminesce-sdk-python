# FilterTermDesign

A single filter clause

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | [**QueryDesignerBinaryOperator**](QueryDesignerBinaryOperator.md) |  | 
**value** | **str** | The value to compare against (always as a string, but will be formatted to the correct type) | 

## Example

```python
from finbourne_luminesce.models.filter_term_design import FilterTermDesign

# TODO update the JSON string below
json = "{}"
# create an instance of FilterTermDesign from a JSON string
filter_term_design_instance = FilterTermDesign.from_json(json)
# print the JSON string representation of the object
print FilterTermDesign.to_json()

# convert the object into a dict
filter_term_design_dict = filter_term_design_instance.to_dict()
# create an instance of FilterTermDesign from a dict
filter_term_design_form_dict = filter_term_design.from_dict(filter_term_design_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


