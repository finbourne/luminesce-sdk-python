# AccessControlledResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**actions** | [**List[AccessControlledAction]**](AccessControlledAction.md) |  | [optional] 
**identifier_parts** | [**List[AccessControlledResourceIdentifierPartSchemaAttribute]**](AccessControlledResourceIdentifierPartSchemaAttribute.md) |  | [optional] 
## Example

```python
from luminesce.models.access_controlled_resource import AccessControlledResource
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

application: Optional[StrictStr] = "example_application"
name: Optional[StrictStr] = "example_name"
description: Optional[StrictStr] = "example_description"
actions: Optional[conlist(AccessControlledAction)] = None
identifier_parts: Optional[conlist(AccessControlledResourceIdentifierPartSchemaAttribute)] = # Replace with your value
access_controlled_resource_instance = AccessControlledResource(application=application, name=name, description=description, actions=actions, identifier_parts=identifier_parts)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

