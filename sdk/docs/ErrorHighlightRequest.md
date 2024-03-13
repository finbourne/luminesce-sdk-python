# ErrorHighlightRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lines** | **List[str]** | The lines of text the user currently has in the editor | 

## Example

```python
from luminesce.models.error_highlight_request import ErrorHighlightRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorHighlightRequest from a JSON string
error_highlight_request_instance = ErrorHighlightRequest.from_json(json)
# print the JSON string representation of the object
print ErrorHighlightRequest.to_json()

# convert the object into a dict
error_highlight_request_dict = error_highlight_request_instance.to_dict()
# create an instance of ErrorHighlightRequest from a dict
error_highlight_request_form_dict = error_highlight_request.from_dict(error_highlight_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


