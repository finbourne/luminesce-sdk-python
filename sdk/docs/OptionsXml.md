# OptionsXml

Additional options applicable to the given SourceType
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_types** | **str** | Column types (comma delimited list of: &#39;{types}&#39;, some columns may be left blank while others are specified) | [optional] 
**infer_type_row_count** | **int** | If non-zero and &#39;types&#39; is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified | [optional] 
**values_to_make_null** | **str** | Regex of values to map to &#39;null&#39; in the returned data. | [optional] 
**column_names** | **str** | Column Names either overrides the header row or steps in when there is no header row (comma delimited list) | [optional] 
**node_path** | **str** | XPath query that selects the nodes to map to rows | [optional] 
**namespaces** | **str** | Selected prefix(es) and namespace(s):prefix1&#x3D;namespace1-uri1,prefix2&#x3D;namespace2-uri2,...prefixN&#x3D;namespaceN-uriN | [optional] 
## Example

```python
from luminesce.models.options_xml import OptionsXml
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

column_types: Optional[StrictStr] = "example_column_types"
infer_type_row_count: Optional[StrictInt] = # Replace with your value
infer_type_row_count: Optional[StrictInt] = None
values_to_make_null: Optional[StrictStr] = "example_values_to_make_null"
column_names: Optional[StrictStr] = "example_column_names"
node_path: Optional[StrictStr] = "example_node_path"
namespaces: Optional[StrictStr] = "example_namespaces"
options_xml_instance = OptionsXml(column_types=column_types, infer_type_row_count=infer_type_row_count, values_to_make_null=values_to_make_null, column_names=column_names, node_path=node_path, namespaces=namespaces)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

