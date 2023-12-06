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
**created_by** | **str** | The user which created this | [optional] 
**serial_number** | **str** | The Vault-issued serial number of the certificate, if any - used for revocation | [optional] 
**links** | [**List[Link]**](Link.md) | The location within Configuration Store that this is saved to | [optional] 

## Example

```python
from luminesce.models.certificate_state import CertificateState

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateState from a JSON string
certificate_state_instance = CertificateState.from_json(json)
# print the JSON string representation of the object
print CertificateState.to_json()

# convert the object into a dict
certificate_state_dict = certificate_state_instance.to_dict()
# create an instance of CertificateState from a dict
certificate_state_form_dict = certificate_state.from_dict(certificate_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


