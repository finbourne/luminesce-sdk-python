# CustomMultiQueryItem

One query within a Finbourne.Honeycomb.WebApi.BackgroundQueries.MultiQuery.CustomMultiQueryRequest, given as either raw LuminesceSql or a saved query reference.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name of the query, of at most 31 characters. Later queries refer to this one&#39;s results as &#x60;@Name&#x60;, and it names the result in any export. | 
**sql** | **str** | The LuminesceSql to run.  Exactly one of this and &#x60;SavedQuery&#x60; must be given. | [optional] 
**saved_query** | **str** | A key within the Saved Queries (of the Workspaces API) to load the SQL from.  Exactly one of this and &#x60;Sql&#x60; must be given. e.g. &#x60;personal/YourUserId/items/queries/SomeQuery&#x60; or &#x60;shared/SomeWorkspace/items/queries/SomeQuery&#x60;. | [optional] 
**is_external_result** | **bool** | Should the results of this query be fetchable / exported?  If false it is only an intermediate step for later queries. | [optional] 
## Example

```python
from luminesce.models.custom_multi_query_item import CustomMultiQueryItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
sql: Optional[StrictStr] = "example_sql"
saved_query: Optional[StrictStr] = "example_saved_query"
is_external_result: Optional[StrictBool] = # Replace with your value
is_external_result:Optional[StrictBool] = None
custom_multi_query_item_instance = CustomMultiQueryItem(name=name, sql=sql, saved_query=saved_query, is_external_result=is_external_result)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

