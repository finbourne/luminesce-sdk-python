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
from luminesce.models.background_query_response import BackgroundQueryResponse
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

execution_id: Optional[StrictStr] = "example_execution_id"
progress: Optional[Link] = None
cancel: Optional[Link] = None
fetch_json: Optional[Link] = # Replace with your value
fetch_json_proper: Optional[Link] = # Replace with your value
fetch_xml: Optional[Link] = # Replace with your value
fetch_parquet: Optional[Link] = # Replace with your value
fetch_csv: Optional[Link] = # Replace with your value
fetch_pipe: Optional[Link] = # Replace with your value
fetch_excel: Optional[Link] = # Replace with your value
fetch_sqlite: Optional[Link] = # Replace with your value
histogram: Optional[Link] = None
background_query_response_instance = BackgroundQueryResponse(execution_id=execution_id, progress=progress, cancel=cancel, fetch_json=fetch_json, fetch_json_proper=fetch_json_proper, fetch_xml=fetch_xml, fetch_parquet=fetch_parquet, fetch_csv=fetch_csv, fetch_pipe=fetch_pipe, fetch_excel=fetch_excel, fetch_sqlite=fetch_sqlite, histogram=histogram)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

