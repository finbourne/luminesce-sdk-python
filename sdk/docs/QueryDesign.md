# QueryDesign

Representation of a \"designable Query\" suitable for formatting to SQL or being built from compliant SQL.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_name** | **str** | Name of the table being designed | 
**alias** | **str** | Alias for the table in the generated SQL, if any | [optional] 
**fields** | [**List[FieldDesign]**](FieldDesign.md) | Fields to be selected, aggregated over and/or filtered on | 
**order_by** | [**List[OrderByTermDesign]**](OrderByTermDesign.md) | Order By clauses to apply | [optional] 
**limit** | **int** | Row limit to apply, if any | [optional] 
**warnings** | **List[str]** | Any warnings to show the user when converting from SQL to this representation | [optional] 
**available_fields** | [**List[AvailableField]**](AvailableField.md) | Fields that are known to be available for design when parsing SQL | [optional] 
## Example

```python
from luminesce.models.query_design import QueryDesign
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist, constr

table_name: StrictStr = "example_table_name"
alias: Optional[StrictStr] = "example_alias"
fields: conlist(FieldDesign) = # Replace with your value
order_by: Optional[conlist(OrderByTermDesign)] = # Replace with your value
limit: Optional[StrictInt] = # Replace with your value
limit: Optional[StrictInt] = None
warnings: Optional[conlist(StrictStr)] = # Replace with your value
available_fields: Optional[conlist(AvailableField)] = # Replace with your value
query_design_instance = QueryDesign(table_name=table_name, alias=alias, fields=fields, order_by=order_by, limit=limit, warnings=warnings, available_fields=available_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

