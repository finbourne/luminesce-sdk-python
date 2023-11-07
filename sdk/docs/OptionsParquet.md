# OptionsParquet

Additional options applicable to the given SourceType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_names_wanted** | **str** | Column (by Name) that should be returned (comma delimited list) | [optional] 

## Example

```python
from finbourne_luminesce.models.options_parquet import OptionsParquet

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsParquet from a JSON string
options_parquet_instance = OptionsParquet.from_json(json)
# print the JSON string representation of the object
print OptionsParquet.to_json()

# convert the object into a dict
options_parquet_dict = options_parquet_instance.to_dict()
# create an instance of OptionsParquet from a dict
options_parquet_form_dict = options_parquet.from_dict(options_parquet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


