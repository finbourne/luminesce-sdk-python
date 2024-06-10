# InlinedPropertyDesign

Representation of a set of inlined properties for a given provider so that SQL can be generated to be able to inline properties into luminesce

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_name** | **str** | The provider name for which these properties are to be inlined | [optional] 
**inlined_property_items** | [**List[InlinedPropertyItem]**](InlinedPropertyItem.md) | Collection of Inlined properties | [optional] 

## Example

```python
from luminesce.models.inlined_property_design import InlinedPropertyDesign

# TODO update the JSON string below
json = "{}"
# create an instance of InlinedPropertyDesign from a JSON string
inlined_property_design_instance = InlinedPropertyDesign.from_json(json)
# print the JSON string representation of the object
print InlinedPropertyDesign.to_json()

# convert the object into a dict
inlined_property_design_dict = inlined_property_design_instance.to_dict()
# create an instance of InlinedPropertyDesign from a dict
inlined_property_design_form_dict = inlined_property_design.from_dict(inlined_property_design_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


