# IntellisenseRequest

Representation of a request for IntellisenseItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lines** | **List[str]** | The lines of text the user currently has in the editor | 
**position** | [**CursorPosition**](CursorPosition.md) |  | 

## Example

```python
from luminesce.models.intellisense_request import IntellisenseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IntellisenseRequest from a JSON string
intellisense_request_instance = IntellisenseRequest.from_json(json)
# print the JSON string representation of the object
print IntellisenseRequest.to_json()

# convert the object into a dict
intellisense_request_dict = intellisense_request_instance.to_dict()
# create an instance of IntellisenseRequest from a dict
intellisense_request_form_dict = intellisense_request.from_dict(intellisense_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


