# OptionsCsv

Additional options applicable to the given SourceType
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_names** | **str** | Column Names either overrides the header row or steps in when there is no header row (comma delimited list) | [optional] 
**column_names_wanted** | **str** | Column (by Name) that should be returned (comma delimited list) | [optional] 
**column_types** | **str** | Column types (comma delimited list of: &#39;{types}&#39;, some columns may be left blank while others are specified) | [optional] 
**infer_type_row_count** | **int** | If non-zero and &#39;types&#39; is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified | [optional] 
**no_header** | **bool** | Set this if there is no header row | [optional] 
**delimiter** | **str** | The delimiter between values (\\t for tab) | [optional] 
**escape** | **str** | Character used to escape the &#39;Quote&#39; character when within a value | [optional] 
**quote** | **str** | Character used around any field containing the &#39;delimiter&#39; or a line break. | [optional] 
**values_to_make_null** | **str** | Regex of values to map to &#39;null&#39; in the returned data. | [optional] 
**skip_pre_header** | **int** | Number of rows to ignore before the header row | [optional] 
**skip_post_header** | **int** | Number of rows to ignore after the header row | [optional] 
**skip_invalid_rows** | **bool** | Skip invalid data rows (totally invalid ones),  This also allows for potentially wrong data if it can be handled somewhat e.g. embedded quotes misused (and still returns such rows). In either case a warning will show in the progress feedback. | [optional] 
## Example

```python
from luminesce.models.options_csv import OptionsCsv
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

column_names: Optional[StrictStr] = "example_column_names"
column_names_wanted: Optional[StrictStr] = "example_column_names_wanted"
column_types: Optional[StrictStr] = "example_column_types"
infer_type_row_count: Optional[StrictInt] = # Replace with your value
infer_type_row_count: Optional[StrictInt] = None
no_header: Optional[StrictBool] = # Replace with your value
no_header:Optional[StrictBool] = None
delimiter: Optional[StrictStr] = "example_delimiter"
escape: Optional[StrictStr] = "example_escape"
quote: Optional[StrictStr] = "example_quote"
values_to_make_null: Optional[StrictStr] = "example_values_to_make_null"
skip_pre_header: Optional[StrictInt] = # Replace with your value
skip_pre_header: Optional[StrictInt] = None
skip_post_header: Optional[StrictInt] = # Replace with your value
skip_post_header: Optional[StrictInt] = None
skip_invalid_rows: Optional[StrictBool] = # Replace with your value
skip_invalid_rows:Optional[StrictBool] = None
options_csv_instance = OptionsCsv(column_names=column_names, column_names_wanted=column_names_wanted, column_types=column_types, infer_type_row_count=infer_type_row_count, no_header=no_header, delimiter=delimiter, escape=escape, quote=quote, values_to_make_null=values_to_make_null, skip_pre_header=skip_pre_header, skip_post_header=skip_post_header, skip_invalid_rows=skip_invalid_rows)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

