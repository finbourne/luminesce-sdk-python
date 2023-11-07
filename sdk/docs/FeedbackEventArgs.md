# FeedbackEventArgs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**when** | **datetime** |  | [optional] 
**session_id** | **str** |  | [optional] 
**execution_id** | **str** |  | [optional] 
**level** | [**FeedbackLevel**](FeedbackLevel.md) |  | [optional] 
**sender** | **str** |  | [optional] 
**state_id** | **int** |  | [optional] 
**message_template** | **str** |  | [optional] 
**property_values** | **List[object]** |  | [optional] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from luminesce.models.feedback_event_args import FeedbackEventArgs

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackEventArgs from a JSON string
feedback_event_args_instance = FeedbackEventArgs.from_json(json)
# print the JSON string representation of the object
print FeedbackEventArgs.to_json()

# convert the object into a dict
feedback_event_args_dict = feedback_event_args_instance.to_dict()
# create an instance of FeedbackEventArgs from a dict
feedback_event_args_form_dict = feedback_event_args.from_dict(feedback_event_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


