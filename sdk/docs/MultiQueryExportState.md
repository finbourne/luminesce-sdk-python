# MultiQueryExportState

What became of the export of a custom multi-query once its queries were done (persisted in its shared state, so known to every pod).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drive_location_and_file_name** | **str** | Where it was to be saved, its placeholders filled in | [optional] 
**saved_to** | **str** | The Drive path (and file name, with its extension) it was saved to, once it has been | [optional] 
**error** | **str** | Why it was not saved, if it was not | [optional] 
## Example

```python
from luminesce.models.multi_query_export_state import MultiQueryExportState
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

drive_location_and_file_name: Optional[StrictStr] = "example_drive_location_and_file_name"
saved_to: Optional[StrictStr] = "example_saved_to"
error: Optional[StrictStr] = "example_error"
multi_query_export_state_instance = MultiQueryExportState(drive_location_and_file_name=drive_location_and_file_name, saved_to=saved_to, error=error)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

