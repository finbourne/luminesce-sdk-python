# JoinedTableDesign

Treatment of a joined-to-table a QueryDesign
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**joined_table_name** | **str** | Name of the table on the right side of the join | 
**joined_table_alias** | **str** | Alias for the table on the right side of the join | 
**left_table_alias** | **str** | Alias for the table on the left side of the join | 
**join_type** | [**DesignJoinType**](DesignJoinType.md) |  | 
**on_clause_terms** | [**List[OnClauseTermDesign]**](OnClauseTermDesign.md) | Filter clauses to apply to this join in the on clause | 
**right_table_available_fields** | [**List[AvailableField]**](AvailableField.md) | Fields that are known to be available for design when parsing SQL, of the right hand table | [optional] 
## Example

```python
from luminesce.models.joined_table_design import JoinedTableDesign
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

joined_table_name: StrictStr = "example_joined_table_name"
joined_table_alias: StrictStr = "example_joined_table_alias"
left_table_alias: StrictStr = "example_left_table_alias"
join_type: DesignJoinType = # Replace with your value
on_clause_terms: List[OnClauseTermDesign] = # Replace with your value
right_table_available_fields: Optional[List[AvailableField]] = # Replace with your value
joined_table_design_instance = JoinedTableDesign(joined_table_name=joined_table_name, joined_table_alias=joined_table_alias, left_table_alias=left_table_alias, join_type=join_type, on_clause_terms=on_clause_terms, right_table_available_fields=right_table_available_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

