# CaseStatementDesign

Representation of the selected field and a list of: filter, source, and target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_field** | **str** | Selected field in the SQL query. | [optional] 
**case_statement_items** | [**List[CaseStatementItem]**](CaseStatementItem.md) | A list containing the filter, source, and target. | [optional] 

## Example

```python
from luminesce.models.case_statement_design import CaseStatementDesign

# TODO update the JSON string below
json = "{}"
# create an instance of CaseStatementDesign from a JSON string
case_statement_design_instance = CaseStatementDesign.from_json(json)
# print the JSON string representation of the object
print CaseStatementDesign.to_json()

# convert the object into a dict
case_statement_design_dict = case_statement_design_instance.to_dict()
# create an instance of CaseStatementDesign from a dict
case_statement_design_form_dict = case_statement_design.from_dict(case_statement_design_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


