# CaseStatementItem

Information about a case statement. A typical case statement would look like: CASE WHEN Field {Filter} Source THEN Target For example: CASE WHEN 'currency' = 'USD' THEN 'US' Here the Field is 'currency', the Source is 'USD', the Filter is '=', and the Target is 'US'
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | The operator in the case statement SQL expression | 
**source** | **str** | The expression that is on the LHS of the operator A typical case statement would look like: CASE Field {Filter} Source THEN Target | 
**target** | **str** | The expression that is on the RHS of the operator A typical case statement would look like: CASE Field {Filter} Source THEN Target | 
**is_target_non_literal** | **bool** | The Target can be a literal value or a non literal (field) and hence will be interpreted differently. This can be determined from the UI and passed down as a true / false | [optional] 
## Example

```python
from luminesce.models.case_statement_item import CaseStatementItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

filter: StrictStr = "example_filter"
source: StrictStr = "example_source"
target: StrictStr = "example_target"
is_target_non_literal: Optional[StrictBool] = # Replace with your value
is_target_non_literal:Optional[StrictBool] = None
case_statement_item_instance = CaseStatementItem(filter=filter, source=source, target=target, is_target_non_literal=is_target_non_literal)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

