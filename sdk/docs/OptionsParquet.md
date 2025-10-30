# OptionsParquet

Additional options applicable to the given SourceType
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_names_wanted** | **str** | Column (by Name) that should be returned (comma delimited list) | [optional] 
## Example

```python
from luminesce.models.options_parquet import OptionsParquet
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

column_names_wanted: Optional[StrictStr] = "example_column_names_wanted"
options_parquet_instance = OptionsParquet(column_names_wanted=column_names_wanted)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

