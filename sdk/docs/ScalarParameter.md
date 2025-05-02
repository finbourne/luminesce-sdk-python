# ScalarParameter

Describes a scalar parameter as defined in the SQL

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the scalar parameter | 
**type** | [**DataType**](DataType.md) |  | 
**value** | **object** | the default value of the parameter | [optional] 
**value_options** | **List[object]** | Values of the parameter listed as being available for choosing from. | [optional] 
**value_must_be_from_options** | **bool** | Must Value be one of ValueOptions (if any)? | [optional] 

## Example

```python
from luminesce.models.scalar_parameter import ScalarParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ScalarParameter from a JSON string
scalar_parameter_instance = ScalarParameter.from_json(json)
# print the JSON string representation of the object
print ScalarParameter.to_json()

# convert the object into a dict
scalar_parameter_dict = scalar_parameter_instance.to_dict()
# create an instance of ScalarParameter from a dict
scalar_parameter_form_dict = scalar_parameter.from_dict(scalar_parameter_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


