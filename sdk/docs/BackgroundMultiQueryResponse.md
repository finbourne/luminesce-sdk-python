# BackgroundMultiQueryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** |  | [optional] [readonly] 
**progress** | [**Link**](Link.md) |  | [optional] 
**cancel** | [**Link**](Link.md) |  | [optional] 
**fetch_json** | [**List[Link]**](Link.md) | Json (as a string) data request links for all of the child queries | [optional] [readonly] 
**fetch_json_proper** | [**List[Link]**](Link.md) | Json-proper data request links for all of the child queries | [optional] [readonly] 
**fetch_xml** | [**List[Link]**](Link.md) | Xml data request links for all of the child queries | [optional] [readonly] 
**fetch_parquet** | [**List[Link]**](Link.md) | Parquet data request links for all of the child queries | [optional] [readonly] 
**fetch_csv** | [**List[Link]**](Link.md) | CSV data request links for all of the child queries | [optional] [readonly] 
**fetch_pipe** | [**List[Link]**](Link.md) | Pipe delimited data request links for all of the child queries | [optional] [readonly] 
**fetch_excel** | [**List[Link]**](Link.md) | Excel workbook data request links for all of the child queries | [optional] [readonly] 
**fetch_sqlite** | [**List[Link]**](Link.md) | SqLite DB data request links for all of the child queries | [optional] [readonly] 
**histogram** | [**List[Link]**](Link.md) | Histogram links for all of the child queries | [optional] [readonly] 

## Example

```python
from luminesce.models.background_multi_query_response import BackgroundMultiQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundMultiQueryResponse from a JSON string
background_multi_query_response_instance = BackgroundMultiQueryResponse.from_json(json)
# print the JSON string representation of the object
print BackgroundMultiQueryResponse.to_json()

# convert the object into a dict
background_multi_query_response_dict = background_multi_query_response_instance.to_dict()
# create an instance of BackgroundMultiQueryResponse from a dict
background_multi_query_response_form_dict = background_multi_query_response.from_dict(background_multi_query_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


