# ScalarParameter

Describes a scalar parameter as defined in the SQL
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the scalar parameter | 
**type** | [**DataType**](DataType.md) |  | 
**value** | **object** | the default value of the parameter | [optional] 
**value_options** | **List[object]** | Values of the parameter listed as being available for choosing from. | [optional] 
**value_must_be_from_options** | **bool** | Must Value be one of ValueOptions (if any)? | [optional] 
## Example

```python
from luminesce.models.scalar_parameter import ScalarParameter
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
type: DataType
value: Optional[Any] = # Replace with your value
value_options: Optional[List[Any]] = # Replace with your value
value_must_be_from_options: Optional[StrictBool] = # Replace with your value
value_must_be_from_options:Optional[StrictBool] = None
scalar_parameter_instance = ScalarParameter(name=name, type=type, value=value, value_options=value_options, value_must_be_from_options=value_must_be_from_options)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

