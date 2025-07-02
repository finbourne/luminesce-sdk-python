# ExpressionWithAlias

Contract for an expression of data we \"have\" that we may \"want to map to a table-parameter's column\"
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | Expression (column name, constant, complex expression, etc.) | 
**alias** | **str** | Column Alias for the expression | [optional] 
**flags** | [**MappingFlags**](MappingFlags.md) |  | [optional] 
## Example

```python
from luminesce.models.expression_with_alias import ExpressionWithAlias
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

expression: StrictStr = "example_expression"
alias: Optional[StrictStr] = "example_alias"
flags: Optional[MappingFlags] = None
expression_with_alias_instance = ExpressionWithAlias(expression=expression, alias=alias, flags=flags)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

