# CursorPosition

Represents a cursor location

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row** | **int** | Row (0 based) of the user&#39;s cursor position | 
**column** | **int** | Column (0 based) of the user&#39;s cursor position | 

## Example

```python
from luminesce.models.cursor_position import CursorPosition

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPosition from a JSON string
cursor_position_instance = CursorPosition.from_json(json)
# print the JSON string representation of the object
print CursorPosition.to_json()

# convert the object into a dict
cursor_position_dict = cursor_position_instance.to_dict()
# create an instance of CursorPosition from a dict
cursor_position_form_dict = cursor_position.from_dict(cursor_position_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


