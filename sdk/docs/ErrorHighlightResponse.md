# ErrorHighlightResponse

Response for error highlighting
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ErrorHighlightItem]**](ErrorHighlightItem.md) | The errors within the Sql | 
**sql_with_marker** | **str** | The SQL this is for, with characters indicating the error locations | 
## Example

```python
from luminesce.models.error_highlight_response import ErrorHighlightResponse
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist, constr

errors: conlist(ErrorHighlightItem) = # Replace with your value
sql_with_marker: StrictStr = "example_sql_with_marker"
error_highlight_response_instance = ErrorHighlightResponse(errors=errors, sql_with_marker=sql_with_marker)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

