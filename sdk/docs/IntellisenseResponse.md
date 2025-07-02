# IntellisenseResponse

Available intellisense response information
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_complete_list** | [**List[IntellisenseItem]**](IntellisenseItem.md) | The available items at this point | 
**try_again_soon_for_more** | **bool** | Should the caller try again soon? (true means a cache is being built and this is a preliminary response!) | 
**sql_with_marker** | **str** | The SQL this is for with characters indicating the location the pop-up is for | 
**start_replacement_position** | [**CursorPosition**](CursorPosition.md) |  | 
**end_replacement_position** | [**CursorPosition**](CursorPosition.md) |  | 
## Example

```python
from luminesce.models.intellisense_response import IntellisenseResponse
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictBool, conlist, constr

auto_complete_list: conlist(IntellisenseItem) = # Replace with your value
try_again_soon_for_more: StrictBool = # Replace with your value
try_again_soon_for_more:StrictBool = True
sql_with_marker: StrictStr = "example_sql_with_marker"
start_replacement_position: CursorPosition = # Replace with your value
end_replacement_position: CursorPosition = # Replace with your value
intellisense_response_instance = IntellisenseResponse(auto_complete_list=auto_complete_list, try_again_soon_for_more=try_again_soon_for_more, sql_with_marker=sql_with_marker, start_replacement_position=start_replacement_position, end_replacement_position=end_replacement_position)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

