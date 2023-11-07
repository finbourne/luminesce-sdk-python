# ConvertToViewData

Representation of view data where will template the data into a 'create view' sql

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | view query | 
**name** | **str** | Name of view | 
**description** | **str** | Description of view | [optional] 
**documentation_link** | **str** | Documentation link | [optional] 
**view_parameters** | [**List[ViewParameter]**](ViewParameter.md) | View parameters | [optional] 

## Example

```python
from luminesce.models.convert_to_view_data import ConvertToViewData

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertToViewData from a JSON string
convert_to_view_data_instance = ConvertToViewData.from_json(json)
# print the JSON string representation of the object
print ConvertToViewData.to_json()

# convert the object into a dict
convert_to_view_data_dict = convert_to_view_data_instance.to_dict()
# create an instance of ConvertToViewData from a dict
convert_to_view_data_form_dict = convert_to_view_data.from_dict(convert_to_view_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


