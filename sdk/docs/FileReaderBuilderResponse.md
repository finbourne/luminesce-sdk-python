# FileReaderBuilderResponse

Information on how to construct a file-read sql query

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The generated SQL | [optional] 
**error** | **str** | The error from running generated SQL Query, if any | [optional] 
**columns** | [**List[ColumnInfo]**](ColumnInfo.md) | Column information for the results | [optional] 
**data** | **object** | The resulting data from running the Query | [optional] 

## Example

```python
from luminesce.models.file_reader_builder_response import FileReaderBuilderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileReaderBuilderResponse from a JSON string
file_reader_builder_response_instance = FileReaderBuilderResponse.from_json(json)
# print the JSON string representation of the object
print FileReaderBuilderResponse.to_json()

# convert the object into a dict
file_reader_builder_response_dict = file_reader_builder_response_instance.to_dict()
# create an instance of FileReaderBuilderResponse from a dict
file_reader_builder_response_form_dict = file_reader_builder_response.from_dict(file_reader_builder_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


