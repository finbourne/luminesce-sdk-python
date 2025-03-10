# LusidGridData

Representation of the data we will get from the dashboard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lusid_grid_design** | [**TableView**](TableView.md) |  | 
**resource_id** | [**ResourceId**](ResourceId.md) |  | 
**dashboard_type** | [**DashboardType**](DashboardType.md) |  | [optional] 
**use_settle_date** | **bool** | Whether to use the Settlement date or the Transaction date | [optional] 
**dates** | [**DateParameters**](DateParameters.md) |  | [optional] 

## Example

```python
from luminesce.models.lusid_grid_data import LusidGridData

# TODO update the JSON string below
json = "{}"
# create an instance of LusidGridData from a JSON string
lusid_grid_data_instance = LusidGridData.from_json(json)
# print the JSON string representation of the object
print LusidGridData.to_json()

# convert the object into a dict
lusid_grid_data_dict = lusid_grid_data_instance.to_dict()
# create an instance of LusidGridData from a dict
lusid_grid_data_form_dict = lusid_grid_data.from_dict(lusid_grid_data_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


