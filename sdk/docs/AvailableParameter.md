# AvailableParameter

Information about a field that can be designed on (regardless if it currently is) Kind of a \"mini-available catalog entry\"
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_name** | **str** | Name of the Provider with a TableParameter | 
**parameter_name** | **str** | Name of the TableParameter on the Provider | 
**fields** | [**List[MappableField]**](MappableField.md) | Fields that can be mapped to | 
## Example

```python
from luminesce.models.available_parameter import AvailableParameter
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

provider_name: StrictStr = "example_provider_name"
parameter_name: StrictStr = "example_parameter_name"
fields: List[MappableField] = # Replace with your value
available_parameter_instance = AvailableParameter(provider_name=provider_name, parameter_name=parameter_name, fields=fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

