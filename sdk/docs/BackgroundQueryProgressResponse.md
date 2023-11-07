# BackgroundQueryProgressResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_data** | **bool** | Is there currently data for this Query? | [optional] 
**row_count** | **int** | Number of rows of data held. -1 if none as yet. | [optional] 
**status** | [**TaskStatus**](TaskStatus.md) |  | [optional] 
**state** | [**BackgroundQueryState**](BackgroundQueryState.md) |  | [optional] 
**progress** | **str** | The full progress log (up to this point at least) | [optional] 
**feedback** | [**List[FeedbackEventArgs]**](FeedbackEventArgs.md) | Individual Feedback Messages (to replace Progress).  A given message will be returned from only one call. | [optional] 
**query** | **str** | The LuminesceSql of the original request | [optional] 
**query_name** | **str** | The QueryName given in the original request | [optional] 
**columns_available** | [**List[Column]**](Column.md) | When HasData is true this is the schema of columns that will be returned if the data is requested | [optional] 

## Example

```python
from finbourne_luminesce.models.background_query_progress_response import BackgroundQueryProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundQueryProgressResponse from a JSON string
background_query_progress_response_instance = BackgroundQueryProgressResponse.from_json(json)
# print the JSON string representation of the object
print BackgroundQueryProgressResponse.to_json()

# convert the object into a dict
background_query_progress_response_dict = background_query_progress_response_instance.to_dict()
# create an instance of BackgroundQueryProgressResponse from a dict
background_query_progress_response_form_dict = background_query_progress_response.from_dict(background_query_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


