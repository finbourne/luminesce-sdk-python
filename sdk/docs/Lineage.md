# Lineage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**subtype** | **str** |  | [optional] 
**alias** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**documentation_as_html** | **str** |  | [optional] 
**documentation_as_mark_down** | **str** |  | [optional] 
**full_text** | **str** |  | [optional] 
**children** | [**List[Lineage]**](Lineage.md) |  | [optional] 
## Example

```python
from luminesce.models.lineage import Lineage
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
subtype: Optional[StrictStr] = "example_subtype"
alias: Optional[StrictStr] = "example_alias"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
documentation_as_html: Optional[StrictStr] = "example_documentation_as_html"
documentation_as_mark_down: Optional[StrictStr] = "example_documentation_as_mark_down"
full_text: Optional[StrictStr] = "example_full_text"
children: Optional[List[Lineage]] = None
lineage_instance = Lineage(type=type, subtype=subtype, alias=alias, display_name=display_name, description=description, documentation_as_html=documentation_as_html, documentation_as_mark_down=documentation_as_mark_down, full_text=full_text, children=children)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

