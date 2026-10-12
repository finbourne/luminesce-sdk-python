# CustomMultiQueryRequest

A caller-supplied set of queries to run in the background, as one multi-query.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | An explicit ExecutionId to use.  This must be blank OR assigned to a valid GUID-as-a-string. | [optional] 
**scalar_parameters** | **Dict[str, Optional[str]]** | Scalar parameter values, handed to every query that runs (e.g. filling in &#x60;:someParameter:defaultValue&#x60; style references). At most 100, each named as an identifier of at most 256 characters, with a value of at most 4096. | [optional] 
**queries** | [**List[CustomMultiQueryItem]**](CustomMultiQueryItem.md) | The queries to run.  Those ready are started in the order given here (one still waiting on those it refers to does not hold up a later one), and each may only refer to queries earlier in the list. | 
**max_in_parallel** | **int** | Maximum number of the queries that may run concurrently.  Defaults to 1, meaning they run one after another. Explicitly null means as many as their dependencies allow. | [optional] 
**timeout_seconds** | **int** | Maximum time each query may run for, in seconds, timed from when it starts: &lt;0 → ∞, 0 → 1200s (20m). There is no limit on the set as a whole. | [optional] 
**keep_for_seconds** | **int** | Maximum time the results may be kept for, in seconds: &lt;0 → 1200 (20m), 0 → 28800 (8h), max &#x3D; 2,678,400 (31d) | [optional] 
**query_name** | **str** | A name for this set of queries.  This goes into logs and is returned when listing the sets of queries. | [optional] 
## Example

```python
from luminesce.models.custom_multi_query_request import CustomMultiQueryRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

execution_id: Optional[StrictStr] = "example_execution_id"
scalar_parameters: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
queries: List[CustomMultiQueryItem] = # Replace with your value
max_in_parallel: Optional[StrictInt] = # Replace with your value
max_in_parallel: Optional[StrictInt] = None
timeout_seconds: Optional[StrictInt] = # Replace with your value
timeout_seconds: Optional[StrictInt] = None
keep_for_seconds: Optional[StrictInt] = # Replace with your value
keep_for_seconds: Optional[StrictInt] = None
query_name: Optional[StrictStr] = "example_query_name"
custom_multi_query_request_instance = CustomMultiQueryRequest(execution_id=execution_id, scalar_parameters=scalar_parameters, queries=queries, max_in_parallel=max_in_parallel, timeout_seconds=timeout_seconds, keep_for_seconds=keep_for_seconds, query_name=query_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

