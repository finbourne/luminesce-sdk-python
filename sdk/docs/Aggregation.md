# Aggregation

How to aggregate over a field
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AggregateFunction**](AggregateFunction.md) |  | 
**alias** | **str** | Alias, if any, for the Aggregate expression when selected | [optional] 
## Example

```python
from luminesce.models.aggregation import Aggregation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: AggregateFunction
alias: Optional[StrictStr] = "example_alias"
aggregation_instance = Aggregation(type=type, alias=alias)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

