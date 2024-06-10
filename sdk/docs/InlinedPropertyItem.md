# InlinedPropertyItem

Information about a inlined property so that decorated properties can be inlined into luminesce

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of the property | 
**name** | **str** | Name of the property | [optional] 
**is_main** | **bool** | Is Main indicator for the property | [optional] 
**description** | **str** | Description of the property | [optional] 

## Example

```python
from luminesce.models.inlined_property_item import InlinedPropertyItem

# TODO update the JSON string below
json = "{}"
# create an instance of InlinedPropertyItem from a JSON string
inlined_property_item_instance = InlinedPropertyItem.from_json(json)
# print the JSON string representation of the object
print InlinedPropertyItem.to_json()

# convert the object into a dict
inlined_property_item_dict = inlined_property_item_instance.to_dict()
# create an instance of InlinedPropertyItem from a dict
inlined_property_item_form_dict = inlined_property_item.from_dict(inlined_property_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


