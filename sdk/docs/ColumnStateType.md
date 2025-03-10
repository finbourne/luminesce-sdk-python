# ColumnStateType

Representation of a column within the grid

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**col_id** | **str** | Unique identifier for the column | 
**hide** | **bool** | Flag to determine whether the column is visible in the grid | 
**sort** | **str** | The sort order (asc or desc) | [optional] 
**sort_index** | **int** | The index of the sort to determine the order in which the sorts are applied | [optional] 

## Example

```python
from luminesce.models.column_state_type import ColumnStateType

# TODO update the JSON string below
json = "{}"
# create an instance of ColumnStateType from a JSON string
column_state_type_instance = ColumnStateType.from_json(json)
# print the JSON string representation of the object
print ColumnStateType.to_json()

# convert the object into a dict
column_state_type_dict = column_state_type_instance.to_dict()
# create an instance of ColumnStateType from a dict
column_state_type_form_dict = column_state_type.from_dict(column_state_type_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


