# QueryDesign

Representation of a \"designable Query\" suitable for formatting to SQL or being built from compliant SQL.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_name** | **str** | Name of the table being designed | 
**alias** | **str** | Alias for the table in the generated SQL, if any | [optional] 
**fields** | [**List[FieldDesign]**](FieldDesign.md) | Fields to be selected, aggregated over and/or filtered on | 
**joined_tables** | [**List[JoinedTableDesign]**](JoinedTableDesign.md) | Joined in table to the main TableName / Alias | [optional] 
**order_by** | [**List[OrderByTermDesign]**](OrderByTermDesign.md) | Order By clauses to apply | [optional] 
**limit** | **int** | Row limit to apply, if any | [optional] 
**offset** | **int** | Row offset to apply, if any | [optional] 
**warnings** | **List[str]** | Any warnings to show the user when converting from SQL to this representation | [optional] 
**available_fields** | [**List[AvailableField]**](AvailableField.md) | Fields that are known to be available for design when parsing SQL | [optional] 
## Example

```python
from luminesce.models.query_design import QueryDesign
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

table_name: StrictStr = "example_table_name"
alias: Optional[StrictStr] = "example_alias"
fields: List[FieldDesign] = # Replace with your value
joined_tables: Optional[List[JoinedTableDesign]] = # Replace with your value
order_by: Optional[List[OrderByTermDesign]] = # Replace with your value
limit: Optional[StrictInt] = # Replace with your value
limit: Optional[StrictInt] = None
offset: Optional[StrictInt] = # Replace with your value
offset: Optional[StrictInt] = None
warnings: Optional[List[StrictStr]] = # Replace with your value
available_fields: Optional[List[AvailableField]] = # Replace with your value
query_design_instance = QueryDesign(table_name=table_name, alias=alias, fields=fields, joined_tables=joined_tables, order_by=order_by, limit=limit, offset=offset, warnings=warnings, available_fields=available_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

