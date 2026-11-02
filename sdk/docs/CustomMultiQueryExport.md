# CustomMultiQueryExport

Where (and how) to save the results of a custom multi-query to Drive, as one file, once its queries are done: the same as calling `api/MultiQueryBackground/{executionId}/drive` then, which may still be called as often as wanted.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drive_location_and_file_name** | **str** | Location and file name within Drive to save to. Missing paths will be created, and extension (if given) will be ignored and inferred from the format (zip where several results are zipped). May contain the placeholders &#x60;{executionId}&#x60;, &#x60;{date:format}&#x60; (when the queries started, UTC, e.g. &#x60;{date:yyyyMMdd}&#x60;) and &#x60;{param:name}&#x60; (the value of a scalar parameter). | [optional] 
**format** | [**ExportType**](ExportType.md) |  | [optional] 
**may_overwrite** | **bool** | If there is an existing file at the location with the same name should it be overwritten (rather than the export failing)?  False by default. | [optional] 
**drive_template_location** | **str** | Drive path and full file name including extension of a template to export with.  Only Excel and Pdf exports support templates. | [optional] 
**date_time_format** | **str** | Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently &#x60;yyyy-MM-dd HH:mm:ss.fff&#x60; | [optional] 
**when_some_fail** | **bool** | Should the results of the queries that succeeded still be saved when others did not?  False by default, meaning nothing is saved then. Either way the multi-query as a whole is reported as failed. | [optional] 
## Example

```python
from luminesce.models.custom_multi_query_export import CustomMultiQueryExport
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

drive_location_and_file_name: Optional[StrictStr] = "example_drive_location_and_file_name"
format: Optional[ExportType] = None
may_overwrite: Optional[StrictBool] = # Replace with your value
may_overwrite:Optional[StrictBool] = None
drive_template_location: Optional[StrictStr] = "example_drive_template_location"
date_time_format: Optional[StrictStr] = "example_date_time_format"
when_some_fail: Optional[StrictBool] = # Replace with your value
when_some_fail:Optional[StrictBool] = None
custom_multi_query_export_instance = CustomMultiQueryExport(drive_location_and_file_name=drive_location_and_file_name, format=format, may_overwrite=may_overwrite, drive_template_location=drive_template_location, date_time_format=date_time_format, when_some_fail=when_some_fail)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

