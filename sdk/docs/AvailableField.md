# AvailableField

Information about a field that can be designed on (regardless if it currently is)  Kind of a \"mini-available catalog entry\"

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Field | 
**data_type** | [**DataType**](DataType.md) |  | [optional] 
**field_type** | [**FieldType**](FieldType.md) |  | 
**is_main** | **bool** | Is this a Main Field within the Provider | [optional] 
**is_primary_key** | **bool** | Is this a member of the PrimaryKey of the Provider | [optional] 

## Example

```python
from luminesce.models.available_field import AvailableField

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableField from a JSON string
available_field_instance = AvailableField.from_json(json)
# print the JSON string representation of the object
print AvailableField.to_json()

# convert the object into a dict
available_field_dict = available_field_instance.to_dict()
# create an instance of AvailableField from a dict
available_field_form_dict = available_field.from_dict(available_field_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


