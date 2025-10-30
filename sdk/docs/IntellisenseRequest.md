# IntellisenseRequest

Representation of a request for IntellisenseItems
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lines** | **List[str]** | The lines of text the user currently has in the editor | 
**position** | [**CursorPosition**](CursorPosition.md) |  | 
## Example

```python
from luminesce.models.intellisense_request import IntellisenseRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

lines: List[StrictStr] = # Replace with your value
position: CursorPosition
intellisense_request_instance = IntellisenseRequest(lines=lines, position=position)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

