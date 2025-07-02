# CertificateState

Information held about the minting / revoking of a certificate.  It does *not* contain the certificate itself
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The \&quot;key\&quot; to which this belongs in the dictionary,  basically the CN without any version information | [optional] 
**version** | **int** | The version of this certificate | [optional] 
**common_name** | **str** | The common Name of the Certificate | [optional] 
**type** | [**CertificateType**](CertificateType.md) |  | [optional] 
**creation_status** | [**CertificateStatus**](CertificateStatus.md) |  | [optional] 
**revocation_status** | [**CertificateStatus**](CertificateStatus.md) |  | [optional] 
**validity_start** | **datetime** | The earliest point at which a certificate can be used | [optional] 
**validity_end** | **datetime** | The latest point at which a certificate can be used | [optional] 
**revoked_at** | **datetime** | The point at which this was revoked, if any | [optional] 
**revoked_by** | **str** | The user which revoked this, if any | [optional] 
**created_at** | **datetime** | The point at which this was created | [optional] 
**permissions_set_at** | **datetime** | The point at which permissions were adjusted by the system | [optional] 
**created_by** | **str** | The user which created this | [optional] 
**serial_number** | **str** | The Vault-issued serial number of the certificate, if any - used for revocation | [optional] 
**links** | [**List[Link]**](Link.md) | The location within Configuration Store that this is saved to | [optional] 
## Example

```python
from luminesce.models.certificate_state import CertificateState
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist
from datetime import datetime
key: Optional[StrictStr] = "example_key"
version: Optional[StrictInt] = # Replace with your value
version: Optional[StrictInt] = None
common_name: Optional[StrictStr] = "example_common_name"
type: Optional[CertificateType] = None
creation_status: Optional[CertificateStatus] = # Replace with your value
revocation_status: Optional[CertificateStatus] = # Replace with your value
validity_start: Optional[datetime] = # Replace with your value
validity_end: Optional[datetime] = # Replace with your value
revoked_at: Optional[datetime] = # Replace with your value
revoked_by: Optional[StrictStr] = "example_revoked_by"
created_at: Optional[datetime] = # Replace with your value
permissions_set_at: Optional[datetime] = # Replace with your value
created_by: Optional[StrictStr] = "example_created_by"
serial_number: Optional[StrictStr] = "example_serial_number"
links: Optional[conlist(Link)] = # Replace with your value
certificate_state_instance = CertificateState(key=key, version=version, common_name=common_name, type=type, creation_status=creation_status, revocation_status=revocation_status, validity_start=validity_start, validity_end=validity_end, revoked_at=revoked_at, revoked_by=revoked_by, created_at=created_at, permissions_set_at=permissions_set_at, created_by=created_by, serial_number=serial_number, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

