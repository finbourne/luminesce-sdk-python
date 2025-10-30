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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

description: Optional[StrictStr] = "example_description"
action: Optional[ActionId] = None
limited_set: Optional[List[IdSelectorDefinition]] = # Replace with your value
access_controlled_action_instance = AccessControlledAction(description=description, action=action, limited_set=limited_set)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

