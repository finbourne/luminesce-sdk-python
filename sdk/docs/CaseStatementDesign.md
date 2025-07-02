# CaseStatementDesign

Representation of the selected field and a list of: filter, source, and target.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_field** | **str** | Selected field in the SQL query. | [optional] 
**case_statement_items** | [**List[CaseStatementItem]**](CaseStatementItem.md) | A list containing the filter, source, and target. | [optional] 
## Example

```python
from luminesce.models.case_statement_design import CaseStatementDesign
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

selected_field: Optional[StrictStr] = "example_selected_field"
case_statement_items: Optional[conlist(CaseStatementItem)] = # Replace with your value
case_statement_design_instance = CaseStatementDesign(selected_field=selected_field, case_statement_items=case_statement_items)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

