# ExpressionWithAlias

Contract for an expression of data we \"have\" that we may \"want to map to a table-parameter's column\"

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | Expression (column name, constant, complex expression, etc.) | 
**alias** | **str** | Column Alias for the expression | [optional] 

## Example

```python
from luminesce.models.expression_with_alias import ExpressionWithAlias

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressionWithAlias from a JSON string
expression_with_alias_instance = ExpressionWithAlias.from_json(json)
# print the JSON string representation of the object
print ExpressionWithAlias.to_json()

# convert the object into a dict
expression_with_alias_dict = expression_with_alias_instance.to_dict()
# create an instance of ExpressionWithAlias from a dict
expression_with_alias_form_dict = expression_with_alias.from_dict(expression_with_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


