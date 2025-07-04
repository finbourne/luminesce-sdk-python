# CursorPosition

Represents a cursor location
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row** | **int** | Row (0 based) of the user&#39;s cursor position | 
**column** | **int** | Column (0 based) of the user&#39;s cursor position | 
## Example

```python
from luminesce.models.cursor_position import CursorPosition
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictInt

row: StrictInt = # Replace with your value
row: StrictInt = 42
column: StrictInt = # Replace with your value
column: StrictInt = 42
cursor_position_instance = CursorPosition(row=row, column=column)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

