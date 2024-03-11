# IntellisenseResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_complete_list** | [**List[IntellisenseItem]**](IntellisenseItem.md) | The available items at this point | 
**try_again_soon_for_more** | **bool** | Should the caller try again soon? (true means a cache is being built and this is a preliminary response!) | 
**sql_with_marker** | **str** | The overall SQL this is for with a character marker for where the Intellisense is for | 

## Example

```python
from luminesce.models.intellisense_response import IntellisenseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntellisenseResponse from a JSON string
intellisense_response_instance = IntellisenseResponse.from_json(json)
# print the JSON string representation of the object
print IntellisenseResponse.to_json()

# convert the object into a dict
intellisense_response_dict = intellisense_response_instance.to_dict()
# create an instance of IntellisenseResponse from a dict
intellisense_response_form_dict = intellisense_response.from_dict(intellisense_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


