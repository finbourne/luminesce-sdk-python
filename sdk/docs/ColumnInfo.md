# ColumnInfo

Information on how to construct a file-read sql query

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select** | **bool** | Should the column be used/selected? | [optional] 
**type** | [**DataType**](DataType.md) |  | [optional] 
**name** | **str** | The name of the column | [optional] 

## Example

```python
from luminesce.models.column_info import ColumnInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ColumnInfo from a JSON string
column_info_instance = ColumnInfo.from_json(json)
# print the JSON string representation of the object
print ColumnInfo.to_json()

# convert the object into a dict
column_info_dict = column_info_instance.to_dict()
# create an instance of ColumnInfo from a dict
column_info_form_dict = column_info.from_dict(column_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


