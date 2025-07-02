# ErrorHighlightRequest

Request for Error highlighting
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lines** | **List[str]** | The lines of text the user currently has in the editor | 
**ensure_some_text_is_selected** | **bool** | If an editor requires some selection of non-whitespace this can be set to true to force  at least one visible character to be selected. | [optional] 
## Example

```python
from luminesce.models.error_highlight_request import ErrorHighlightRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist

lines: conlist(StrictStr) = # Replace with your value
ensure_some_text_is_selected: Optional[StrictBool] = # Replace with your value
ensure_some_text_is_selected:Optional[StrictBool] = None
error_highlight_request_instance = ErrorHighlightRequest(lines=lines, ensure_some_text_is_selected=ensure_some_text_is_selected)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

