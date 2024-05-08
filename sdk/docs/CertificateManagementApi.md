# luminesce.CertificateManagementApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_certificate**](CertificateManagementApi.md#download_certificate) | **GET** /api/Certificate/certificate | [EXPERIMENTAL] DownloadCertificate: Downloads your latest Domain or User certificate&#39;s public or private key - if any
[**list_certificates**](CertificateManagementApi.md#list_certificates) | **GET** /api/Certificate/certificates | [EXPERIMENTAL] ListCertificates: Lists all the certificates previously minted to which you have access
[**manage_certificate**](CertificateManagementApi.md#manage_certificate) | **PUT** /api/Certificate/manage | [EXPERIMENTAL] ManageCertificate: Manages a new certificate (Create / Renew / Revoke)


# **download_certificate**
> bytearray download_certificate(type=type, file_type=file_type, may_auto_create=may_auto_create)

[EXPERIMENTAL] DownloadCertificate: Downloads your latest Domain or User certificate's public or private key - if any

 Downloads your latest Domain or User certificate's public or private key - if any.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - certificate is not available for some reason - 401 Unauthorized - 403 Forbidden 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from luminesce.models.certificate_file_type import CertificateFileType
from luminesce.models.certificate_type import CertificateType
from pprint import pprint

import os
from luminesce import (
    ApiClientFactory,
    CertificateManagementApi,
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
    api_instance = api_client_factory.build(luminesce.CertificateManagementApi)
    type = luminesce.CertificateType() # CertificateType | User or Domain level cert (Domain level requires additional entitlements) (optional)
    file_type = luminesce.CertificateFileType() # CertificateFileType | Should the public key or private key be downloaded? (both must be in place to run providers) (optional)
    may_auto_create = False # bool | If no matching cert is available, should an attempt be made to Create/Renew it with default options? (optional) (default to False)

    try:
        # [EXPERIMENTAL] DownloadCertificate: Downloads your latest Domain or User certificate's public or private key - if any
        api_response = await api_instance.download_certificate(type=type, file_type=file_type, may_auto_create=may_auto_create)
        print("The response of CertificateManagementApi->download_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateManagementApi->download_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**CertificateType**](.md)| User or Domain level cert (Domain level requires additional entitlements) | [optional] 
 **file_type** | [**CertificateFileType**](.md)| Should the public key or private key be downloaded? (both must be in place to run providers) | [optional] 
 **may_auto_create** | **bool**| If no matching cert is available, should an attempt be made to Create/Renew it with default options? | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_certificates**
> List[CertificateState] list_certificates()

[EXPERIMENTAL] ListCertificates: Lists all the certificates previously minted to which you have access

 Lists all the certificates previously minted to which you have access.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from luminesce.models.certificate_state import CertificateState
from pprint import pprint

import os
from luminesce import (
    ApiClientFactory,
    CertificateManagementApi,
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
    api_instance = api_client_factory.build(luminesce.CertificateManagementApi)

    try:
        # [EXPERIMENTAL] ListCertificates: Lists all the certificates previously minted to which you have access
        api_response = await api_instance.list_certificates()
        print("The response of CertificateManagementApi->list_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateManagementApi->list_certificates: %s\n" % e)
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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_certificate**
> CertificateState manage_certificate(action=action, type=type, version=version, validity_start=validity_start, validity_end=validity_end, dry_run=dry_run)

[EXPERIMENTAL] ManageCertificate: Manages a new certificate (Create / Renew / Revoke)

 Manages a certificate.  This could be creating a new one, renewing an old one or revoking one explicitly.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something about the request cannot be processed - 401 Unauthorized - 403 Forbidden 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from luminesce.models.certificate_action import CertificateAction
from luminesce.models.certificate_state import CertificateState
from luminesce.models.certificate_type import CertificateType
from pprint import pprint

import os
from luminesce import (
    ApiClientFactory,
    CertificateManagementApi,
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
    api_instance = api_client_factory.build(luminesce.CertificateManagementApi)
    action = luminesce.CertificateAction() # CertificateAction | The Action to perform, e.g. Create / Renew / Revoke (optional)
    type = luminesce.CertificateType() # CertificateType | User or Domain level cert (Domain level requires additional entitlements) (optional)
    version = 1 # int | Version number of the cert, the request will fail to validate if incorrect (optional) (default to 1)
    validity_start = '2013-10-20T19:20:30+01:00' # datetime | When should the cert first be valid (defaults to the current time in UTC) (optional)
    validity_end = '2013-10-20T19:20:30+01:00' # datetime | When should the cert no longer be valid (defaults to 13 months from now) (optional)
    dry_run = True # bool | True will just validate the request, but perform no changes to any system (optional) (default to True)

    try:
        # [EXPERIMENTAL] ManageCertificate: Manages a new certificate (Create / Renew / Revoke)
        api_response = await api_instance.manage_certificate(action=action, type=type, version=version, validity_start=validity_start, validity_end=validity_end, dry_run=dry_run)
        print("The response of CertificateManagementApi->manage_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateManagementApi->manage_certificate: %s\n" % e)
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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

