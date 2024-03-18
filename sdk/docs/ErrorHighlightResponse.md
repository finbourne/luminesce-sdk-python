# ErrorHighlightResponse

Response for error highlighting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ErrorHighlightItem]**](ErrorHighlightItem.md) | The errors within the Sql | 
**sql_with_marker** | **str** | The SQL this is for, with characters indicating the error locations | 

## Example

```python
from luminesce.models.error_highlight_response import ErrorHighlightResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorHighlightResponse from a JSON string
error_highlight_response_instance = ErrorHighlightResponse.from_json(json)
# print the JSON string representation of the object
print ErrorHighlightResponse.to_json()

# convert the object into a dict
error_highlight_response_dict = error_highlight_response_instance.to_dict()
# create an instance of ErrorHighlightResponse from a dict
error_highlight_response_form_dict = error_highlight_response.from_dict(error_highlight_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


