# TableMeta

Representation of the table metadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_id** | **str** | A unique identifier for the table | 

## Example

```python
from luminesce.models.table_meta import TableMeta

# TODO update the JSON string below
json = "{}"
# create an instance of TableMeta from a JSON string
table_meta_instance = TableMeta.from_json(json)
# print the JSON string representation of the object
print TableMeta.to_json()

# convert the object into a dict
table_meta_dict = table_meta_instance.to_dict()
# create an instance of TableMeta from a dict
table_meta_form_dict = table_meta.from_dict(table_meta_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


