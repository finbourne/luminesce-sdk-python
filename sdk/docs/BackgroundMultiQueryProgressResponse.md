# BackgroundMultiQueryProgressResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**progress** | **str** | The full progress log (up to this point at least) | [optional] 
**feedback** | [**List[FeedbackEventArgs]**](FeedbackEventArgs.md) | Individual Feedback Messages (to replace Progress).  A given message will be returned from only one call. | [optional] 
**status** | [**TaskStatus**](TaskStatus.md) |  | [optional] 
**queries** | [**List[BackgroundQueryProgressResponse]**](BackgroundQueryProgressResponse.md) |  | [optional] 

## Example

```python
from luminesce.models.background_multi_query_progress_response import BackgroundMultiQueryProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundMultiQueryProgressResponse from a JSON string
background_multi_query_progress_response_instance = BackgroundMultiQueryProgressResponse.from_json(json)
# print the JSON string representation of the object
print BackgroundMultiQueryProgressResponse.to_json()

# convert the object into a dict
background_multi_query_progress_response_dict = background_multi_query_progress_response_instance.to_dict()
# create an instance of BackgroundMultiQueryProgressResponse from a dict
background_multi_query_progress_response_form_dict = background_multi_query_progress_response.from_dict(background_multi_query_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


