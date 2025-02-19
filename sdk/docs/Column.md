# Column


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_primary_key** | **bool** |  | [optional] 
**is_main** | **bool** |  | [optional] 
**is_required_by_provider** | **bool** |  | [optional] 
**mandatory_for_actions** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**DataType**](DataType.md) |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**condition_usage** | [**ConditionAttributes**](ConditionAttributes.md) |  | [optional] 
**sample_values** | **str** |  | [optional] 
**allowed_values** | **str** |  | [optional] 

## Example

```python
from luminesce.models.column import Column

# TODO update the JSON string below
json = "{}"
# create an instance of Column from a JSON string
column_instance = Column.from_json(json)
# print the JSON string representation of the object
print Column.to_json()

# convert the object into a dict
column_dict = column_instance.to_dict()
# create an instance of Column from a dict
column_form_dict = column.from_dict(column_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


