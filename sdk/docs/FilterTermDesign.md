# FilterTermDesign

A single filter clause
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | [**QueryDesignerBinaryOperator**](QueryDesignerBinaryOperator.md) |  | 
**value** | **str** | The value to compare against (always as a string, but will be formatted to the correct type) | 
## Example

```python
from luminesce.models.filter_term_design import FilterTermDesign
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

operator: QueryDesignerBinaryOperator
value: StrictStr = "example_value"
filter_term_design_instance = FilterTermDesign(operator=operator, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

