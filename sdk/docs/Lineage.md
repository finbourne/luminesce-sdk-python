# Lineage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**subtype** | **str** |  | [optional] 
**alias** | **str** |  | [optional] 
**column_title_tooltip** | **str** |  | [optional] 
**column_title_icon** | [**LineageColumnIcon**](LineageColumnIcon.md) |  | [optional] 
**explain_title** | **str** |  | [optional] 
**explain_tooltip** | **str** |  | [optional] 
**full_formula** | **str** |  | [optional] 
**documentation_as_html** | **str** |  | [optional] 
**documentation_as_mark_down** | **str** |  | [optional] 
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
column_title_tooltip: Optional[StrictStr] = "example_column_title_tooltip"
column_title_icon: Optional[LineageColumnIcon] = # Replace with your value
explain_title: Optional[StrictStr] = "example_explain_title"
explain_tooltip: Optional[StrictStr] = "example_explain_tooltip"
full_formula: Optional[StrictStr] = "example_full_formula"
documentation_as_html: Optional[StrictStr] = "example_documentation_as_html"
documentation_as_mark_down: Optional[StrictStr] = "example_documentation_as_mark_down"
children: Optional[List[Lineage]] = None
lineage_instance = Lineage(type=type, subtype=subtype, alias=alias, column_title_tooltip=column_title_tooltip, column_title_icon=column_title_icon, explain_title=explain_title, explain_tooltip=explain_tooltip, full_formula=full_formula, documentation_as_html=documentation_as_html, documentation_as_mark_down=documentation_as_mark_down, children=children)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

