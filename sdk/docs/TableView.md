# TableView

Representation of the table structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_names** | **Dict[str, str]** | Mapping of column ids to aliases | 
**column_state** | [**List[ColumnStateType]**](ColumnStateType.md) | Array of all columns in the dashboard | 
**filters** | [**Dict[str, FilterModel]**](FilterModel.md) | Filters applied to columns in the dashboard | [optional] 
**meta** | [**TableMeta**](TableMeta.md) |  | 

## Example

```python
from luminesce.models.table_view import TableView

# TODO update the JSON string below
json = "{}"
# create an instance of TableView from a JSON string
table_view_instance = TableView.from_json(json)
# print the JSON string representation of the object
print TableView.to_json()

# convert the object into a dict
table_view_dict = table_view_instance.to_dict()
# create an instance of TableView from a dict
table_view_form_dict = table_view.from_dict(table_view_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


