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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

query: Optional[StrictStr] = "example_query"
error: Optional[StrictStr] = "example_error"
columns: Optional[conlist(ColumnInfo)] = # Replace with your value
data: Optional[Any] = # Replace with your value
file_reader_builder_response_instance = FileReaderBuilderResponse(query=query, error=error, columns=columns, data=data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

