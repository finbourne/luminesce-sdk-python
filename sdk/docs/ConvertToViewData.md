# ConvertToViewData

Representation of view data where will template the data into a 'create view' sql
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | view query | 
**name** | **str** | Name of view | 
**description** | **str** | Description of view | [optional] 
**documentation_link** | **str** | Documentation link | [optional] 
**view_parameters** | [**List[ViewParameter]**](ViewParameter.md) | View parameters | [optional] 
**other_parameters** | **Dict[str, str]** | Other parameters not explicitly handled by the ConvertToView generation. These will be populated by the \&quot;From SQL\&quot; and should simply be returned by the web GUI should the user edit / update / regenerate | [optional] 
**starting_variable_name** | **str** | Which variable the this start with, null if not started from a full Create View Sql Statement. | [optional] 
## Example

```python
from luminesce.models.convert_to_view_data import ConvertToViewData
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

query: StrictStr = "example_query"
name: StrictStr = "example_name"
description: Optional[StrictStr] = "example_description"
documentation_link: Optional[StrictStr] = "example_documentation_link"
view_parameters: Optional[conlist(ViewParameter)] = # Replace with your value
other_parameters: Optional[Dict[str, StrictStr]] = # Replace with your value
starting_variable_name: Optional[StrictStr] = "example_starting_variable_name"
convert_to_view_data_instance = ConvertToViewData(query=query, name=name, description=description, documentation_link=documentation_link, view_parameters=view_parameters, other_parameters=other_parameters, starting_variable_name=starting_variable_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

