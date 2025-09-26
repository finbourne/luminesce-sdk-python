# AvailableField

Information about a field that can be designed on (regardless if it currently is) Kind of a \"mini-available catalog entry\"
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Field | 
**data_type** | [**DataType**](DataType.md) |  | [optional] 
**field_type** | [**FieldType**](FieldType.md) |  | 
**is_main** | **bool** | Is this a Main Field within the Provider | [optional] 
**is_primary_key** | **bool** | Is this a member of the PrimaryKey of the Provider | [optional] 
## Example

```python
from luminesce.models.available_field import AvailableField
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, constr

name: StrictStr = "example_name"
data_type: Optional[DataType] = # Replace with your value
field_type: FieldType = # Replace with your value
is_main: Optional[StrictBool] = # Replace with your value
is_main:Optional[StrictBool] = None
is_primary_key: Optional[StrictBool] = # Replace with your value
is_primary_key:Optional[StrictBool] = None
available_field_instance = AvailableField(name=name, data_type=data_type, field_type=field_type, is_main=is_main, is_primary_key=is_primary_key)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

