# Source

Information leading to choosing the provider
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | The source location.  Start of a provider name, &#x60;Drive&#x60;, &#x60;LocalFs&#x60;, &#x60;AwsS3&#x60; etc. | [optional] 
**type** | [**SourceType**](SourceType.md) |  | [optional] 
## Example

```python
from luminesce.models.source import Source
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

location: Optional[StrictStr] = "example_location"
type: Optional[SourceType] = None
source_instance = Source(location=location, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

