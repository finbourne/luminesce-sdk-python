# OrderByTermDesign

A single clause within an Order BY

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Name of the field to order by | 
**direction** | [**OrderByDirection**](OrderByDirection.md) |  | [optional] 

## Example

```python
from finbourne_luminesce.models.order_by_term_design import OrderByTermDesign

# TODO update the JSON string below
json = "{}"
# create an instance of OrderByTermDesign from a JSON string
order_by_term_design_instance = OrderByTermDesign.from_json(json)
# print the JSON string representation of the object
print OrderByTermDesign.to_json()

# convert the object into a dict
order_by_term_design_dict = order_by_term_design_instance.to_dict()
# create an instance of OrderByTermDesign from a dict
order_by_term_design_form_dict = order_by_term_design.from_dict(order_by_term_design_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


