# InlinedPropertyDesign

Representation of a set of inlined properties for a given provider so that SQL can be generated to be able to inline properties into luminesce
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_name** | **str** | The provider name for which these properties are to be inlined | [optional] 
**provider_name_extension** | **str** | The provider extension name for extended providers | [optional] 
**inlined_property_items** | [**List[InlinedPropertyItem]**](InlinedPropertyItem.md) | Collection of Inlined properties | [optional] 
## Example

```python
from luminesce.models.inlined_property_design import InlinedPropertyDesign
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

provider_name: Optional[StrictStr] = "example_provider_name"
provider_name_extension: Optional[StrictStr] = "example_provider_name_extension"
inlined_property_items: Optional[List[InlinedPropertyItem]] = # Replace with your value
inlined_property_design_instance = InlinedPropertyDesign(provider_name=provider_name, provider_name_extension=provider_name_extension, inlined_property_items=inlined_property_items)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

