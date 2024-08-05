# QueryDesign

Representation of a \"designable Query\" suitable for formatting to SQL or being built from compliant SQL.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_name** | **str** | Name of the table being designed | 
**alias** | **str** | Alias for the table in the generated SQL, if any | [optional] 
**fields** | [**List[FieldDesign]**](FieldDesign.md) | Fields to be selected, aggregated over and/or filtered on | 
**order_by** | [**List[OrderByTermDesign]**](OrderByTermDesign.md) | Order By clauses to apply | [optional] 
**limit** | **int** | Row limit to apply, if any | [optional] 
**warnings** | **List[str]** | Any warnings to show the user when converting from SQL to this representation | [optional] 
**available_fields** | [**List[AvailableField]**](AvailableField.md) | Fields that are known to be available for design when parsing SQL | [optional] 

## Example

```python
from luminesce.models.query_design import QueryDesign

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDesign from a JSON string
query_design_instance = QueryDesign.from_json(json)
# print the JSON string representation of the object
print QueryDesign.to_json()

# convert the object into a dict
query_design_dict = query_design_instance.to_dict()
# create an instance of QueryDesign from a dict
query_design_form_dict = query_design.from_dict(query_design_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


