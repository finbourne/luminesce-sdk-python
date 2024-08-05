# Aggregation

How to aggregate over a field

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AggregateFunction**](AggregateFunction.md) |  | 
**alias** | **str** | Alias, if any, for the Aggregate expression when selected | [optional] 

## Example

```python
from luminesce.models.aggregation import Aggregation

# TODO update the JSON string below
json = "{}"
# create an instance of Aggregation from a JSON string
aggregation_instance = Aggregation.from_json(json)
# print the JSON string representation of the object
print Aggregation.to_json()

# convert the object into a dict
aggregation_dict = aggregation_instance.to_dict()
# create an instance of Aggregation from a dict
aggregation_form_dict = aggregation.from_dict(aggregation_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


