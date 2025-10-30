# LusidGridData

Representation of the data we will get from the dashboard
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lusid_grid_design** | [**TableView**](TableView.md) |  | 
**resource_id** | [**ResourceId**](ResourceId.md) |  | 
**dashboard_type** | [**DashboardType**](DashboardType.md) |  | [optional] 
**use_settle_date** | **bool** | Whether to use the Settlement date or the Transaction date | [optional] 
**dates** | [**DateParameters**](DateParameters.md) |  | [optional] 
## Example

```python
from luminesce.models.lusid_grid_data import LusidGridData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

lusid_grid_design: TableView = # Replace with your value
resource_id: ResourceId = # Replace with your value
dashboard_type: Optional[DashboardType] = # Replace with your value
use_settle_date: Optional[StrictBool] = # Replace with your value
use_settle_date:Optional[StrictBool] = None
dates: Optional[DateParameters] = None
lusid_grid_data_instance = LusidGridData(lusid_grid_design=lusid_grid_design, resource_id=resource_id, dashboard_type=dashboard_type, use_settle_date=use_settle_date, dates=dates)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

