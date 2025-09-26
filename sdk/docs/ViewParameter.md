# ViewParameter

Parameters of view
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the provider | 
**data_type** | [**DataType**](DataType.md) |  | 
**value** | **str** | Value of the provider | 
**is_table_data_mandatory** | **bool** | Should this be selected? False would imply it is only being filtered on. Ignored when Aggregations are present | [optional] 
**description** | **str** | Description of the parameter | [optional] 
## Example

```python
from luminesce.models.view_parameter import ViewParameter
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, constr

name: StrictStr = "example_name"
data_type: DataType = # Replace with your value
value: StrictStr = "example_value"
is_table_data_mandatory: Optional[StrictBool] = # Replace with your value
is_table_data_mandatory:Optional[StrictBool] = None
description: Optional[StrictStr] = "example_description"
view_parameter_instance = ViewParameter(name=name, data_type=data_type, value=value, is_table_data_mandatory=is_table_data_mandatory, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

