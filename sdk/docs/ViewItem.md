# ViewItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the view | [optional] 
**domain** | **str** | The domain the view applies to | [optional] 
**file_path** | **str** | The full file path in the HcFs | [optional] 
**file_content** | **str** | The full file content in the HcFs. This will be needed for Upserting the view to a different domain / for use in fbn-config. | [optional] 
**last_updated_execution_id** | **str** | The last ExecutionId, needed to get the creating Sql out of the logs | [optional] 
**last_updated_at** | **datetime** | The last updated at time, needed to get the creating Sql out of the logs | [optional] 
**last_updated_by** | **str** | The last updated by this user | [optional] 
**created_by_user_id** | **str** | Originally created by this user | [optional] 
## Example

```python
from luminesce.models.view_item import ViewItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: Optional[StrictStr] = "example_name"
domain: Optional[StrictStr] = "example_domain"
file_path: Optional[StrictStr] = "example_file_path"
file_content: Optional[StrictStr] = "example_file_content"
last_updated_execution_id: Optional[StrictStr] = "example_last_updated_execution_id"
last_updated_at: Optional[datetime] = # Replace with your value
last_updated_by: Optional[StrictStr] = "example_last_updated_by"
created_by_user_id: Optional[StrictStr] = "example_created_by_user_id"
view_item_instance = ViewItem(name=name, domain=domain, file_path=file_path, file_content=file_content, last_updated_execution_id=last_updated_execution_id, last_updated_at=last_updated_at, last_updated_by=last_updated_by, created_by_user_id=created_by_user_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

