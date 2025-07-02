# AccessControlledAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**action** | [**ActionId**](ActionId.md) |  | [optional] 
**limited_set** | [**List[IdSelectorDefinition]**](IdSelectorDefinition.md) |  | [optional] 
## Example

```python
from luminesce.models.access_controlled_action import AccessControlledAction
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

description: Optional[StrictStr] = "example_description"
action: Optional[ActionId] = None
limited_set: Optional[conlist(IdSelectorDefinition)] = # Replace with your value
access_controlled_action_instance = AccessControlledAction(description=description, action=action, limited_set=limited_set)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

