# BackgroundQueryResponse

Response for Background Query Start requests

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | ExecutionId of the started-query | [optional] 
**progress** | [**Link**](Link.md) |  | [optional] 
**cancel** | [**Link**](Link.md) |  | [optional] 
**fetch_json** | [**Link**](Link.md) |  | [optional] 
**fetch_json_proper** | [**Link**](Link.md) |  | [optional] 
**fetch_xml** | [**Link**](Link.md) |  | [optional] 
**fetch_parquet** | [**Link**](Link.md) |  | [optional] 
**fetch_csv** | [**Link**](Link.md) |  | [optional] 
**fetch_pipe** | [**Link**](Link.md) |  | [optional] 
**fetch_excel** | [**Link**](Link.md) |  | [optional] 
**fetch_sqlite** | [**Link**](Link.md) |  | [optional] 
**histogram** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from finbourne_luminesce.models.background_query_response import BackgroundQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundQueryResponse from a JSON string
background_query_response_instance = BackgroundQueryResponse.from_json(json)
# print the JSON string representation of the object
print BackgroundQueryResponse.to_json()

# convert the object into a dict
background_query_response_dict = background_query_response_instance.to_dict()
# create an instance of BackgroundQueryResponse from a dict
background_query_response_form_dict = background_query_response.from_dict(background_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


