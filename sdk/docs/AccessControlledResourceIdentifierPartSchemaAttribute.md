# AccessControlledResourceIdentifierPartSchemaAttribute

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**values_path** | **str** |  | [optional] 
**type_id** | **object** |  | [optional] [readonly] 
## Example

```python
from luminesce.models.access_controlled_resource_identifier_part_schema_attribute import AccessControlledResourceIdentifierPartSchemaAttribute
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

index: Optional[StrictInt] = None
index: Optional[StrictInt] = None
name: Optional[StrictStr] = "example_name"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
required: Optional[StrictBool] = None
required:Optional[StrictBool] = None
values_path: Optional[StrictStr] = "example_values_path"
type_id: Optional[Any] = # Replace with your value
access_controlled_resource_identifier_part_schema_attribute_instance = AccessControlledResourceIdentifierPartSchemaAttribute(index=index, name=name, display_name=display_name, description=description, required=required, values_path=values_path, type_id=type_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

