# CaseStatementItem

Information about a case statement.  A typical case statement would look like:  CASE WHEN Field {Filter} Source THEN Target  For example: CASE WHEN 'currency' = 'USD' THEN 'US'  Here the Field is 'currency', the Source is 'USD', the Filter is '=', and the Target is 'US'

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | The operator in the case statement SQL expression | 
**source** | **str** | The expression that is on the LHS of the operator  A typical case statement would look like:  CASE Field {Filter} Source THEN Target | 
**target** | **str** | The expression that is on the RHS of the operator  A typical case statement would look like:  CASE Field {Filter} Source THEN Target | 
**is_target_non_literal** | **bool** | The Target can be a literal value or a non literal (field) and  hence will be interpreted differently.  This can be determined from the UI and passed down as a true / false | [optional] 

## Example

```python
from luminesce.models.case_statement_item import CaseStatementItem

# TODO update the JSON string below
json = "{}"
# create an instance of CaseStatementItem from a JSON string
case_statement_item_instance = CaseStatementItem.from_json(json)
# print the JSON string representation of the object
print CaseStatementItem.to_json()

# convert the object into a dict
case_statement_item_dict = case_statement_item_instance.to_dict()
# create an instance of CaseStatementItem from a dict
case_statement_item_form_dict = case_statement_item.from_dict(case_statement_item_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


