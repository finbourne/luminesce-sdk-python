# ViewParameter

Parameters of view

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the provider | 
**data_type** | [**DataType**](DataType.md) |  | 
**value** | **str** | Value of the provider | 
**is_table_data_mandatory** | **bool** | Should this be selected? False would imply it is only being filtered on.  Ignored when Aggregations are present | [optional] 
**description** | **str** | Description of the parameter | [optional] 

## Example

```python
from luminesce.models.view_parameter import ViewParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ViewParameter from a JSON string
view_parameter_instance = ViewParameter.from_json(json)
# print the JSON string representation of the object
print ViewParameter.to_json()

# convert the object into a dict
view_parameter_dict = view_parameter_instance.to_dict()
# create an instance of ViewParameter from a dict
view_parameter_form_dict = view_parameter.from_dict(view_parameter_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


