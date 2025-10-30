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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

execution_id: Optional[StrictStr] = "example_execution_id"
progress: Optional[Link] = None
cancel: Optional[Link] = None
fetch_json: Optional[List[Link]] = # Replace with your value
fetch_json_proper: Optional[List[Link]] = # Replace with your value
fetch_xml: Optional[List[Link]] = # Replace with your value
fetch_parquet: Optional[List[Link]] = # Replace with your value
fetch_csv: Optional[List[Link]] = # Replace with your value
fetch_pipe: Optional[List[Link]] = # Replace with your value
fetch_excel: Optional[List[Link]] = # Replace with your value
fetch_sqlite: Optional[List[Link]] = # Replace with your value
histogram: Optional[List[Link]] = # Replace with your value
background_multi_query_response_instance = BackgroundMultiQueryResponse(execution_id=execution_id, progress=progress, cancel=cancel, fetch_json=fetch_json, fetch_json_proper=fetch_json_proper, fetch_xml=fetch_xml, fetch_parquet=fetch_parquet, fetch_csv=fetch_csv, fetch_pipe=fetch_pipe, fetch_excel=fetch_excel, fetch_sqlite=fetch_sqlite, histogram=histogram)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

