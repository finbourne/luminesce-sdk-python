# finbourne_luminesce.ApplicationMetadataApi

All URIs are relative to *https://fbn-ci.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_services_as_access_controlled_resources**](ApplicationMetadataApi.md#get_services_as_access_controlled_resources) | **GET** /api/metadata/access/resources | GetServicesAsAccessControlledResources: Get resources available for access control


# **get_services_as_access_controlled_resources**
> ResourceListOfAccessControlledResource get_services_as_access_controlled_resources()

GetServicesAsAccessControlledResources: Get resources available for access control

 Get the comprehensive set of resources that are available for access control.  The following LuminesceSql is executed to return this information,  which is then packaged up as AccessControlledResource:  ```sql select     Name,     min(coalesce(Description, Name) || ' (' || Type || ')') as Description from     Sys.Registration where     Type in ('DirectProvider', 'DataProvider')     and     ShowAll = true group by 1 order by 1     ```  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized 

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_luminesce
from finbourne_luminesce.rest import ApiException
from finbourne_luminesce.models.resource_list_of_access_controlled_resource import ResourceListOfAccessControlledResource
from pprint import pprint

from finbourne_luminesce import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_luminesce ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-ci.lusid.com/honeycomb"
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
    api_instance = api_client_factory.build(finbourne_luminesce.ApplicationMetadataApi)

    try:
        # GetServicesAsAccessControlledResources: Get resources available for access control
        api_response = await api_instance.get_services_as_access_controlled_resources()
        print("The response of ApplicationMetadataApi->get_services_as_access_controlled_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationMetadataApi->get_services_as_access_controlled_resources: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfAccessControlledResource**](ResourceListOfAccessControlledResource.md)

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

