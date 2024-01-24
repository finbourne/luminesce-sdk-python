# luminesce.BinaryDownloadingApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_binary**](BinaryDownloadingApi.md#download_binary) | **GET** /api/Download/download | [EXPERIMENTAL] DownloadBinary: Downloads the latest version (or specific if needs be) of the specified Luminesce Binary, given the required entitlements.


# **download_binary**
> bytearray download_binary(type=type, version=version)

[EXPERIMENTAL] DownloadBinary: Downloads the latest version (or specific if needs be) of the specified Luminesce Binary, given the required entitlements.

 Downloads the latest version (or specific if needs be) of the specified Luminesce Binary, given the required entitlements.  *NOTE:* This endpoint is an alternative to time-consuming manual distribution via Drive or Email. > it relies on as underlying datastore that is not quite as \"Highly Available\" to the degree  > that FINBOURNE services generally are.   > Thus it is not subject to the same SLAs as other API endpoints are. > *If you perceive an outage, please try again later.*  Once a file has been downloaded the following steps can be used to install it:  1. Open a terminal and cd to the directory you downloaded it to 2. Install / extract files from that package via: ``` dotnet tool install NameOfFileWithoutExtension -g --add-source \".\" ``` 3. Execute them (see documentation for specific binary)...  The installed binaries can then be found in - Windows - `%USERPROFILE%\\.dotnet\\tools\\.store\\` - Linux/macOS - `$HOME/.dotnet/tools/.store/`  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - binary file is not available for some reason (e.g. permissions or invalid version) - 401 Unauthorized 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import luminesce
from luminesce.rest import ApiException
from luminesce.models.luminesce_binary_type import LuminesceBinaryType
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
    api_instance = api_client_factory.build(luminesce.BinaryDownloadingApi)
    type = luminesce.LuminesceBinaryType() # LuminesceBinaryType | Type of binary to download (each requires separate licenses and entitlements) (optional)
    version = 'version_example' # str | An explicit version of the binary.  Leave blank to get the latest version (recommended) (optional)

    try:
        # [EXPERIMENTAL] DownloadBinary: Downloads the latest version (or specific if needs be) of the specified Luminesce Binary, given the required entitlements.
        api_response = await api_instance.download_binary(type=type, version=version)
        print("The response of BinaryDownloadingApi->download_binary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BinaryDownloadingApi->download_binary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**LuminesceBinaryType**](.md)| Type of binary to download (each requires separate licenses and entitlements) | [optional] 
 **version** | **str**| An explicit version of the binary.  Leave blank to get the latest version (recommended) | [optional] 

### Return type

**bytearray**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The .nupkg file of the requested binary |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

