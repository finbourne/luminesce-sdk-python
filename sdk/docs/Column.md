# Column

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_primary_key** | **bool** |  | [optional] 
**is_main** | **bool** |  | [optional] 
**is_required_by_provider** | **bool** |  | [optional] 
**mandatory_for_actions** | **str** |  | [optional] 
**lineage** | [**Lineage**](Lineage.md) |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**DataType**](DataType.md) |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**condition_usage** | [**ConditionAttributes**](ConditionAttributes.md) |  | [optional] 
**sample_values** | **str** |  | [optional] 
**allowed_values** | **str** |  | [optional] 
## Example

```python
from luminesce.models.column import Column
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

is_primary_key: Optional[StrictBool] = # Replace with your value
is_primary_key:Optional[StrictBool] = None
is_main: Optional[StrictBool] = # Replace with your value
is_main:Optional[StrictBool] = None
is_required_by_provider: Optional[StrictBool] = # Replace with your value
is_required_by_provider:Optional[StrictBool] = None
mandatory_for_actions: Optional[StrictStr] = "example_mandatory_for_actions"
lineage: Optional[Lineage] = None
name: Optional[StrictStr] = "example_name"
type: Optional[DataType] = None
description: Optional[StrictStr] = "example_description"
display_name: Optional[StrictStr] = "example_display_name"
condition_usage: Optional[ConditionAttributes] = # Replace with your value
sample_values: Optional[StrictStr] = "example_sample_values"
allowed_values: Optional[StrictStr] = "example_allowed_values"
column_instance = Column(is_primary_key=is_primary_key, is_main=is_main, is_required_by_provider=is_required_by_provider, mandatory_for_actions=mandatory_for_actions, lineage=lineage, name=name, type=type, description=description, display_name=display_name, condition_usage=condition_usage, sample_values=sample_values, allowed_values=allowed_values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

