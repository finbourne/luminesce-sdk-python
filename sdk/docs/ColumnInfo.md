# ColumnInfo

Information on how to construct a file-read sql query

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select** | **bool** | Should the column be used/selected? | [optional] 
**type** | [**DataType**](DataType.md) |  | [optional] 
**name** | **str** | The name of the column | [optional] 
**x_path** | **str** | Xpath for the column (only applicable to XML defined columns) | [optional] 

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
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


