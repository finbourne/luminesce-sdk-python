# DateParameters

Collection of date parameters used in dashboards

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **datetime** | Parameter to determine the lower bound in a date range | [optional] 
**date_to** | **datetime** | Parameter to determine the upper bound in a date range | [optional] 
**effective_at** | **datetime** | EffectiveAt of the dashboard | [optional] 
**as_at** | **datetime** | AsAt of the dashboard | 

## Example

```python
from luminesce.models.date_parameters import DateParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DateParameters from a JSON string
date_parameters_instance = DateParameters.from_json(json)
# print the JSON string representation of the object
print DateParameters.to_json()

# convert the object into a dict
date_parameters_dict = date_parameters_instance.to_dict()
# create an instance of DateParameters from a dict
date_parameters_form_dict = date_parameters.from_dict(date_parameters_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


