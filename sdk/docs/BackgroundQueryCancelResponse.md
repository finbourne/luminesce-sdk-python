# BackgroundQueryCancelResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**had_data** | **bool** |  | [optional] 
**previous_status** | [**TaskStatus**](TaskStatus.md) |  | [optional] 
**previous_state** | [**BackgroundQueryState**](BackgroundQueryState.md) |  | [optional] 
**progress** | **str** |  | [optional] 

## Example

```python
from luminesce.models.background_query_cancel_response import BackgroundQueryCancelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundQueryCancelResponse from a JSON string
background_query_cancel_response_instance = BackgroundQueryCancelResponse.from_json(json)
# print the JSON string representation of the object
print BackgroundQueryCancelResponse.to_json()

# convert the object into a dict
background_query_cancel_response_dict = background_query_cancel_response_instance.to_dict()
# create an instance of BackgroundQueryCancelResponse from a dict
background_query_cancel_response_form_dict = background_query_cancel_response.from_dict(background_query_cancel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


