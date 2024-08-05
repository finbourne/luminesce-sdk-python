# AvailableParameter

Information about a field that can be designed on (regardless if it currently is)  Kind of a \"mini-available catalog entry\"

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_name** | **str** | Name of the Provider with a TableParameter | 
**parameter_name** | **str** | Name of the TableParameter on the Provider | 
**fields** | [**List[MappableField]**](MappableField.md) | Fields that can be mapped to | 

## Example

```python
from luminesce.models.available_parameter import AvailableParameter

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableParameter from a JSON string
available_parameter_instance = AvailableParameter.from_json(json)
# print the JSON string representation of the object
print AvailableParameter.to_json()

# convert the object into a dict
available_parameter_dict = available_parameter_instance.to_dict()
# create an instance of AvailableParameter from a dict
available_parameter_form_dict = available_parameter.from_dict(available_parameter_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


