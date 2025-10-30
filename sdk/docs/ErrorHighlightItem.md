# ErrorHighlightItem

Representation of a sql error
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | [**CursorPosition**](CursorPosition.md) |  | 
**stop** | [**CursorPosition**](CursorPosition.md) |  | 
**no_viable_alternative_start** | [**CursorPosition**](CursorPosition.md) |  | [optional] 
**length** | **int** | The length of the error token counting line breaks if any | 
**message** | **str** | The error message | 
## Example

```python
from luminesce.models.error_highlight_item import ErrorHighlightItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start: CursorPosition
stop: CursorPosition
no_viable_alternative_start: Optional[CursorPosition] = # Replace with your value
length: StrictInt = # Replace with your value
length: StrictInt = 42
message: StrictStr = "example_message"
error_highlight_item_instance = ErrorHighlightItem(start=start, stop=stop, no_viable_alternative_start=no_viable_alternative_start, length=length, message=message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

