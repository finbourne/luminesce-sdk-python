# WriterDesign

Representation of a \"designable Query for a writer\" suitable for formatting to SQL or being built from compliant SQL.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sql** | **str** | Original SQL that started this off | 
**available_to_map_from** | [**List[ExpressionWithAlias]**](ExpressionWithAlias.md) | The data able to be mapped from as derived from the Sql | [optional] 
**parameter** | [**AvailableParameter**](AvailableParameter.md) |  | [optional] 
**available_parameters** | [**List[AvailableParameter]**](AvailableParameter.md) | All the parameter the user may wish to design | [optional] 
## Example

```python
from luminesce.models.writer_design import WriterDesign
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

sql: StrictStr = "example_sql"
available_to_map_from: Optional[conlist(ExpressionWithAlias)] = # Replace with your value
parameter: Optional[AvailableParameter] = None
available_parameters: Optional[conlist(AvailableParameter)] = # Replace with your value
writer_design_instance = WriterDesign(sql=sql, available_to_map_from=available_to_map_from, parameter=parameter, available_parameters=available_parameters)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

