# InlinedPropertyItem

Information about a inlined property so that decorated properties can be inlined into luminesce
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of the property | 
**name** | **str** | Name of the property | [optional] 
**is_main** | **bool** | Is Main indicator for the property | [optional] 
**description** | **str** | Description of the property | [optional] 
**data_type** | **str** | Data type of the property | [optional] 
## Example

```python
from luminesce.models.inlined_property_item import InlinedPropertyItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: StrictStr = "example_key"
name: Optional[StrictStr] = "example_name"
is_main: Optional[StrictBool] = # Replace with your value
is_main:Optional[StrictBool] = None
description: Optional[StrictStr] = "example_description"
data_type: Optional[StrictStr] = "example_data_type"
inlined_property_item_instance = InlinedPropertyItem(key=key, name=name, is_main=is_main, description=description, data_type=data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

