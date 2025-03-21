# luminesce.BinaryDownloadingApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_binary**](BinaryDownloadingApi.md#download_binary) | **GET** /api/Download/download | DownloadBinary: Download a Luminesce Binary you may run on-site
[**get_binary_versions**](BinaryDownloadingApi.md#get_binary_versions) | **GET** /api/Download/versions | GetBinaryVersions: List available versions of binaries


# **download_binary**
> bytearray download_binary(type=type, version=version)

DownloadBinary: Download a Luminesce Binary you may run on-site

 Downloads the latest version (or specific if needs be) of the specified Luminesce Binary, given the required entitlements.  > This endpoint is an alternative to time-consuming manual distribution via Drive or Email. > it relies on an underlying datastore that is not quite as \"Highly Available\" to the degree  > that FINBOURNE services generally are.   > Thus it is not subject to the same SLAs as other API endpoints are. > *If you perceive an outage, please try again later.*  Once a file has been downloaded the following steps can be used to install it (for the dotnet tools at least):  (1) Open a terminal and cd to the directory you downloaded it to  (2) Install / extract files from that package via:  ``` dotnet tool install NameOfFileWithoutVersionNumberOrExtension -g --add-source \".\" ``` e.g. ``` dotnet tool install Finbourne.Luminesce.DbProviders.Oracle_Snowflake -g --add-source \".\" ``` More information on the installations can be found [here](https://support.lusid.com/docs/how-do-i-use-the-luminesce-cli).  (3) Execute them (see documentation for specific binary, e.g. [Sql.Db.Mine](https://support.lusid.com/docs/readwrite-to-sql-databases-sqldbmine) or [CLI](https://support.lusid.com/docs/how-do-i-use-the-luminesce-cli)).  The installed binaries can then be found in - Windows - `%USERPROFILE%\\.dotnet\\tools\\.store\\` - Linux/macOS - `$HOME/.dotnet/tools/.store/`  Note that the binaries all require the dotnet runtime to be installed. - `dotnet8` is required for all versions `1.18.X+` - `dotnet6` is required for all versions `1.17.X-` *Please upgrade if still running these*  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - binary file is not available for some reason (e.g. permissions or invalid version) - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    BinaryDownloadingApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "luminesceUrl":"https://<your-domain>.lusid.com/honeycomb",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the luminesce SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(BinaryDownloadingApi)
    type = luminesce.LuminesceBinaryType() # LuminesceBinaryType | Type of binary to download (each requires separate licenses and entitlements) (optional)
    version = 'version_example' # str | An explicit version of the binary.  Leave blank to get the latest version (recommended) (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.download_binary(type=type, version=version, opts=opts)

        # DownloadBinary: Download a Luminesce Binary you may run on-site
        api_response = api_instance.download_binary(type=type, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling BinaryDownloadingApi->download_binary: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**LuminesceBinaryType**](.md)| Type of binary to download (each requires separate licenses and entitlements) | [optional] 
 **version** | **str**| An explicit version of the binary.  Leave blank to get the latest version (recommended) | [optional] 

### Return type

**bytearray**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The .nupkg or .msi file of the requested binary |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_binary_versions**
> List[str] get_binary_versions(type=type)

GetBinaryVersions: List available versions of binaries

 Gets all available versions of a given binary type (from newest to oldest) This does not mean you are entitled to download them.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    BinaryDownloadingApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "luminesceUrl":"https://<your-domain>.lusid.com/honeycomb",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the luminesce SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(BinaryDownloadingApi)
    type = luminesce.LuminesceBinaryType() # LuminesceBinaryType | Type of binary to fetch available versions of (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_binary_versions(type=type, opts=opts)

        # GetBinaryVersions: List available versions of binaries
        api_response = api_instance.get_binary_versions(type=type)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling BinaryDownloadingApi->get_binary_versions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**LuminesceBinaryType**](.md)| Type of binary to fetch available versions of | [optional] 

### Return type

**List[str]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

