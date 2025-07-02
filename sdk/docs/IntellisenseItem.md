# IntellisenseItem

Representation of an item in an Intellisense popup
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** | The value to show the user in the popup | 
**value** | **str** | The value to substitute in | 
**meta** | **str** | The light-grey text shown to the right of the Caption in the popup | [optional] 
**score** | **int** | How important is this.  Bigger is more important. | [optional] 
**doc_html** | **str** | Popup further info (as in a whole documentation article!) | [optional] 
**type** | [**IntellisenseType**](IntellisenseType.md) |  | [optional] 
## Example

```python
from luminesce.models.intellisense_item import IntellisenseItem
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, constr

caption: StrictStr = "example_caption"
value: StrictStr = "example_value"
meta: Optional[StrictStr] = "example_meta"
score: Optional[StrictInt] = # Replace with your value
score: Optional[StrictInt] = None
doc_html: Optional[StrictStr] = "example_doc_html"
type: Optional[IntellisenseType] = None
intellisense_item_instance = IntellisenseItem(caption=caption, value=value, meta=meta, score=score, doc_html=doc_html, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

