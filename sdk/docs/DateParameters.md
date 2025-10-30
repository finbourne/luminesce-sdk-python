# DateParameters

Collection of date parameters used in dashboards
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **datetime** | Parameter to determine the lower bound in a date range | [optional] 
**date_to** | **datetime** | Parameter to determine the upper bound in a date range | [optional] 
**effective_at** | **datetime** | EffectiveAt of the dashboard | [optional] 
**as_at** | **datetime** | AsAt of the dashboard | 
## Example

```python
from luminesce.models.date_parameters import DateParameters
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

date_from: Optional[datetime] = # Replace with your value
date_to: Optional[datetime] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
as_at: datetime = # Replace with your value
date_parameters_instance = DateParameters(date_from=date_from, date_to=date_to, effective_at=effective_at, as_at=as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

