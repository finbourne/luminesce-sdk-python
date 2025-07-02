# ResourceId

Unique identifier for a resource
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope used to identify a resource | 
**code** | **str** | The code used to identify a resource | [optional] 
## Example

```python
from luminesce.models.resource_id import ResourceId
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

scope: StrictStr = "example_scope"
code: Optional[StrictStr] = "example_code"
resource_id_instance = ResourceId(scope=scope, code=code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

