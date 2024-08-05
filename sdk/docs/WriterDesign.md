# WriterDesign

Representation of a \"designable Query for a writer\" suitable for formatting to SQL or being built from compliant SQL.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sql** | **str** | Original SQL that started this off | 
**available_to_map_from** | [**List[ExpressionWithAlias]**](ExpressionWithAlias.md) | The data able to be mapped from as derived from the Sql | [optional] 
**parameter** | [**AvailableParameter**](AvailableParameter.md) |  | [optional] 
**available_parameters** | [**List[AvailableParameter]**](AvailableParameter.md) | All the parameter the user may wish to design | [optional] 

## Example

```python
from luminesce.models.writer_design import WriterDesign

# TODO update the JSON string below
json = "{}"
# create an instance of WriterDesign from a JSON string
writer_design_instance = WriterDesign.from_json(json)
# print the JSON string representation of the object
print WriterDesign.to_json()

# convert the object into a dict
writer_design_dict = writer_design_instance.to_dict()
# create an instance of WriterDesign from a dict
writer_design_form_dict = writer_design.from_dict(writer_design_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


