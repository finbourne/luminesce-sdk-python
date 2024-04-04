# ErrorHighlightItem

Representation of a sql error

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | [**CursorPosition**](CursorPosition.md) |  | 
**stop** | [**CursorPosition**](CursorPosition.md) |  | 
**no_viable_alternative_start** | [**CursorPosition**](CursorPosition.md) |  | [optional] 
**length** | **int** | The length of the error token counting line breaks if any | 
**message** | **str** | The error message | 

## Example

```python
from luminesce.models.error_highlight_item import ErrorHighlightItem

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorHighlightItem from a JSON string
error_highlight_item_instance = ErrorHighlightItem.from_json(json)
# print the JSON string representation of the object
print ErrorHighlightItem.to_json()

# convert the object into a dict
error_highlight_item_dict = error_highlight_item_instance.to_dict()
# create an instance of ErrorHighlightItem from a dict
error_highlight_item_form_dict = error_highlight_item.from_dict(error_highlight_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


