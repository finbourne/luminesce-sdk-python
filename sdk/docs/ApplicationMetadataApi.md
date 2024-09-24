# luminesce.ApplicationMetadataApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_services_as_access_controlled_resources**](ApplicationMetadataApi.md#get_services_as_access_controlled_resources) | **GET** /api/metadata/access/resources | GetServicesAsAccessControlledResources: Get resources available for access control


# **get_services_as_access_controlled_resources**
> ResourceListOfAccessControlledResource get_services_as_access_controlled_resources()

GetServicesAsAccessControlledResources: Get resources available for access control

 Get the comprehensive set of resources that are available for access control.  The following LuminesceSql is executed to return this information,  which is then packaged up as AccessControlledResource:  ```sql select     Name,     min(coalesce(Description, Name) || ' (' || Type || ')') as Description from     Sys.Registration where     Type in ('DirectProvider', 'DataProvider')     and     ShowAll = true group by 1 order by 1     ```  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    ApplicationMetadataApi
)

async def main():

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

    # Use the luminesce ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(ApplicationMetadataApi)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_services_as_access_controlled_resources(opts=opts)

            # GetServicesAsAccessControlledResources: Get resources available for access control
            api_response = await api_instance.get_services_as_access_controlled_resources()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ApplicationMetadataApi->get_services_as_access_controlled_resources: %s\n" % e)

asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfAccessControlledResource**](ResourceListOfAccessControlledResource.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

