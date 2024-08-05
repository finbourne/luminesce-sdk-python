# IntellisenseItem

Representation of an item in an Intellisense popup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** | The value to show the user in the popup | 
**value** | **str** | The value to substitute in | 
**meta** | **str** | The light-grey text shown to the right of the Caption in the popup | [optional] 
**score** | **int** | How important is this.  Bigger is more important. | [optional] 
**doc_html** | **str** | Popup further info (as in a whole documentation article!) | [optional] 
**type** | [**IntellisenseType**](IntellisenseType.md) |  | [optional] 

## Example

```python
from luminesce.models.intellisense_item import IntellisenseItem

# TODO update the JSON string below
json = "{}"
# create an instance of IntellisenseItem from a JSON string
intellisense_item_instance = IntellisenseItem.from_json(json)
# print the JSON string representation of the object
print IntellisenseItem.to_json()

# convert the object into a dict
intellisense_item_dict = intellisense_item_instance.to_dict()
# create an instance of IntellisenseItem from a dict
intellisense_item_form_dict = intellisense_item.from_dict(intellisense_item_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


