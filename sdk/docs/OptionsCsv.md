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
**skip_pre_header** | **bool** | Number of rows to ignore before the header row | [optional] 
**skip_post_header** | **bool** | Number of rows to ignore after the header row | [optional] 
**skip_invalid_rows** | **bool** | Skip invalid data rows (totally invalid ones),   This also allows for potentially wrong data if it can be handled somewhat e.g. embedded quotes misused (and still returns such rows).  In either case a warning will show in the progress feedback. | [optional] 

## Example

```python
from finbourne_luminesce.models.options_csv import OptionsCsv

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsCsv from a JSON string
options_csv_instance = OptionsCsv.from_json(json)
# print the JSON string representation of the object
print OptionsCsv.to_json()

# convert the object into a dict
options_csv_dict = options_csv_instance.to_dict()
# create an instance of OptionsCsv from a dict
options_csv_form_dict = options_csv.from_dict(options_csv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


