# FilterModel

Representation of the data used in a filter for the where clause
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_type** | [**FilterType**](FilterType.md) |  | 
**type** | [**Type**](Type.md) |  | [optional] 
**filter** | **str** | The filter value | [optional] 
**filter_to** | **float** | The upper bound filter value for the number filter type | [optional] 
**values** | **List[str]** | An array of possible values for the set filter type | [optional] 
**date_from** | **str** | A lower bound date for the date filter type | [optional] 
**date_to** | **str** | An upper bound date for the date filter type | [optional] 
## Example

```python
from luminesce.models.filter_model import FilterModel
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist

filter_type: FilterType = # Replace with your value
type: Optional[Type] = None
filter: Optional[StrictStr] = "example_filter"
filter_to: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
values: Optional[conlist(StrictStr)] = # Replace with your value
date_from: Optional[StrictStr] = "example_date_from"
date_to: Optional[StrictStr] = "example_date_to"
filter_model_instance = FilterModel(filter_type=filter_type, type=type, filter=filter, filter_to=filter_to, values=values, date_from=date_from, date_to=date_to)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

