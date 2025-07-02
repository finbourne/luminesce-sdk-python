# OptionsSqLite

Additional options applicable to the given SourceType
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table** | **str** | Table name to read.  If missing then an error will be raised if there is any number of tables other than one. | [optional] 
## Example

```python
from luminesce.models.options_sq_lite import OptionsSqLite
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

table: Optional[StrictStr] = "example_table"
options_sq_lite_instance = OptionsSqLite(table=table)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

