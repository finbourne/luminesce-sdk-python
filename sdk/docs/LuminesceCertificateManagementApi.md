# luminesce.LuminesceCertificateManagementApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_certificates**](LuminesceCertificateManagementApi.md#get_certificates) | **GET** /api/Certificate/certificates | [EXPERIMENTAL] GetCertificates: Shows Table and Field level information on Providers that are currently running that you have access to (in Json format)
[**manage_certificate**](LuminesceCertificateManagementApi.md#manage_certificate) | **PUT** /api/Certificate/manage | [EXPERIMENTAL] ManageCertificate: Manages a new certificate (Create / Renew / Revoke)


# **get_certificates**
> List[CertificateState] get_certificates()

[EXPERIMENTAL] GetCertificates: Shows Table and Field level information on Providers that are currently running that you have access to (in Json format)

 Lists all the certificates previously minted to which you have access.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import luminesce
from luminesce.rest import ApiException
from luminesce.models.certificate_state import CertificateState
from pprint import pprint

from luminesce import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the luminesce ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/honeycomb"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(luminesce.LuminesceCertificateManagementApi)

    try:
        # [EXPERIMENTAL] GetCertificates: Shows Table and Field level information on Providers that are currently running that you have access to (in Json format)
        api_response = await api_instance.get_certificates()
        print("The response of LuminesceCertificateManagementApi->get_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LuminesceCertificateManagementApi->get_certificates: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[CertificateState]**](CertificateState.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_certificate**
> CertificateState manage_certificate(action=action, type=type, version=version, validity_start=validity_start, validity_end=validity_end, dry_run=dry_run, skip_systems=skip_systems)

[EXPERIMENTAL] ManageCertificate: Manages a new certificate (Create / Renew / Revoke)

 Manages a certificate.  This could be creating a new one, renewing an old one or revoking one explicitly.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something about the request cannot be processed - 401 Unauthorized 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import luminesce
from luminesce.rest import ApiException
from luminesce.models.certificate_action import CertificateAction
from luminesce.models.certificate_state import CertificateState
from luminesce.models.certificate_status import CertificateStatus
from luminesce.models.certificate_type import CertificateType
from pprint import pprint

from luminesce import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the luminesce ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/honeycomb"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(luminesce.LuminesceCertificateManagementApi)
    action = luminesce.CertificateAction() # CertificateAction | The Action to perform, e.g. Create / Renew / Revoke (optional)
    type = luminesce.CertificateType() # CertificateType | User or Domain level cert (Domain level requires additional entitlements) (optional)
    version = 1 # int | Version number of the cert, the request will fail to validate if incorrect (optional) (default to 1)
    validity_start = '2013-10-20T19:20:30+01:00' # datetime | When should the cert first be valid (defaults to the current time in UTC) (optional)
    validity_end = '2013-10-20T19:20:30+01:00' # datetime | When should the cert no longer be valid (defaults to 13 months from now) (optional)
    dry_run = True # bool | True will just validate the request, but perform no changes to any system (optional) (default to True)
    skip_systems = luminesce.CertificateStatus() # CertificateStatus | Any systems that should be skipped  (if any are the certificate will not function, but can be useful for certain forms of validation) (optional)

    try:
        # [EXPERIMENTAL] ManageCertificate: Manages a new certificate (Create / Renew / Revoke)
        api_response = await api_instance.manage_certificate(action=action, type=type, version=version, validity_start=validity_start, validity_end=validity_end, dry_run=dry_run, skip_systems=skip_systems)
        print("The response of LuminesceCertificateManagementApi->manage_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LuminesceCertificateManagementApi->manage_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | [**CertificateAction**](.md)| The Action to perform, e.g. Create / Renew / Revoke | [optional] 
 **type** | [**CertificateType**](.md)| User or Domain level cert (Domain level requires additional entitlements) | [optional] 
 **version** | **int**| Version number of the cert, the request will fail to validate if incorrect | [optional] [default to 1]
 **validity_start** | **datetime**| When should the cert first be valid (defaults to the current time in UTC) | [optional] 
 **validity_end** | **datetime**| When should the cert no longer be valid (defaults to 13 months from now) | [optional] 
 **dry_run** | **bool**| True will just validate the request, but perform no changes to any system | [optional] [default to True]
 **skip_systems** | [**CertificateStatus**](.md)| Any systems that should be skipped  (if any are the certificate will not function, but can be useful for certain forms of validation) | [optional] 

### Return type

[**CertificateState**](CertificateState.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

