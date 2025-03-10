# FilterModel

Representation of the data used in a filter for the where clause

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_type** | [**FilterType**](FilterType.md) |  | 
**type** | [**Type**](Type.md) |  | [optional] 
**filter** | **str** | The filter value | [optional] 
**filter_to** | **float** | The upper bound filter value for the number filter type | [optional] 
**values** | **List[str]** | An array of possible values for the set filter type | [optional] 
**date_from** | **str** | A lower bound date for the date filter type | [optional] 
**date_to** | **str** | An upper bound date for the date filter type | [optional] 

## Example

```python
from luminesce.models.filter_model import FilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of FilterModel from a JSON string
filter_model_instance = FilterModel.from_json(json)
# print the JSON string representation of the object
print FilterModel.to_json()

# convert the object into a dict
filter_model_dict = filter_model_instance.to_dict()
# create an instance of FilterModel from a dict
filter_model_form_dict = filter_model.from_dict(filter_model_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


