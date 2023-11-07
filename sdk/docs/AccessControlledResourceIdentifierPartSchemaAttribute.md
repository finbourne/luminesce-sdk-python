# AccessControlledResourceIdentifierPartSchemaAttribute


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**values_path** | **str** |  | [optional] 
**type_id** | **object** |  | [optional] [readonly] 

## Example

```python
from finbourne_luminesce.models.access_controlled_resource_identifier_part_schema_attribute import AccessControlledResourceIdentifierPartSchemaAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of AccessControlledResourceIdentifierPartSchemaAttribute from a JSON string
access_controlled_resource_identifier_part_schema_attribute_instance = AccessControlledResourceIdentifierPartSchemaAttribute.from_json(json)
# print the JSON string representation of the object
print AccessControlledResourceIdentifierPartSchemaAttribute.to_json()

# convert the object into a dict
access_controlled_resource_identifier_part_schema_attribute_dict = access_controlled_resource_identifier_part_schema_attribute_instance.to_dict()
# create an instance of AccessControlledResourceIdentifierPartSchemaAttribute from a dict
access_controlled_resource_identifier_part_schema_attribute_form_dict = access_controlled_resource_identifier_part_schema_attribute.from_dict(access_controlled_resource_identifier_part_schema_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


