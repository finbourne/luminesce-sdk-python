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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

query: Optional[StrictStr] = "example_query"
error: Optional[StrictStr] = "example_error"
columns: Optional[List[ColumnInfo]] = # Replace with your value
data: Optional[Any] = # Replace with your value
file_reader_builder_response_instance = FileReaderBuilderResponse(query=query, error=error, columns=columns, data=data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

