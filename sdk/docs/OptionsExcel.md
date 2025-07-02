# OptionsExcel

Additional options applicable to the given SourceType
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_names** | **str** | Column Names either overrides the header row or steps in when there is no header row (comma delimited list) | [optional] 
**column_types** | **str** | Column types (comma delimited list of: &#39;{types}&#39;, some columns may be left blank while others are specified) | [optional] 
**infer_type_row_count** | **int** | If non-zero and &#39;types&#39; is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified | [optional] 
**no_header** | **bool** | Set this if there is no header row | [optional] 
**calculate** | **bool** | Whether to attempt a calculation of the imported cell range prior to import | [optional] 
**password** | **str** | If specified will be used as the password used for password protected workbooks | [optional] 
**worksheet** | **str** | The worksheet containing the cell range to import (name or index, will default to first) | [optional] 
**range_or_table** | **str** | The cell range to import as either a specified range or a table name | [optional] 
**ignore_invalid_cells** | **bool** | If specified cells which can not be successfully converted to the target type will be ignored | [optional] 
**ignore_blank_rows** | **bool** | If the entire rows has only blank cells it will be ignored will be ignored | [optional] 
## Example

```python
from luminesce.models.options_excel import OptionsExcel
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt, StrictStr

column_names: Optional[StrictStr] = "example_column_names"
column_types: Optional[StrictStr] = "example_column_types"
infer_type_row_count: Optional[StrictInt] = # Replace with your value
infer_type_row_count: Optional[StrictInt] = None
no_header: Optional[StrictBool] = # Replace with your value
no_header:Optional[StrictBool] = None
calculate: Optional[StrictBool] = # Replace with your value
calculate:Optional[StrictBool] = None
password: Optional[StrictStr] = "example_password"
worksheet: Optional[StrictStr] = "example_worksheet"
range_or_table: Optional[StrictStr] = "example_range_or_table"
ignore_invalid_cells: Optional[StrictBool] = # Replace with your value
ignore_invalid_cells:Optional[StrictBool] = None
ignore_blank_rows: Optional[StrictBool] = # Replace with your value
ignore_blank_rows:Optional[StrictBool] = None
options_excel_instance = OptionsExcel(column_names=column_names, column_types=column_types, infer_type_row_count=infer_type_row_count, no_header=no_header, calculate=calculate, password=password, worksheet=worksheet, range_or_table=range_or_table, ignore_invalid_cells=ignore_invalid_cells, ignore_blank_rows=ignore_blank_rows)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

