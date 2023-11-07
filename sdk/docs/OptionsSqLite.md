# OptionsSqLite

Additional options applicable to the given SourceType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table** | **str** | Table name to read.  If missing then an error will be raised if there is any number of tables other than one. | [optional] 

## Example

```python
from luminesce.models.options_sq_lite import OptionsSqLite

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsSqLite from a JSON string
options_sq_lite_instance = OptionsSqLite.from_json(json)
# print the JSON string representation of the object
print OptionsSqLite.to_json()

# convert the object into a dict
options_sq_lite_dict = options_sq_lite_instance.to_dict()
# create an instance of OptionsSqLite from a dict
options_sq_lite_form_dict = options_sq_lite.from_dict(options_sq_lite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


