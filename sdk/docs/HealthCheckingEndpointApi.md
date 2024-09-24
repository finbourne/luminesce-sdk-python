# luminesce.HealthCheckingEndpointApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fake_node_reclaim**](HealthCheckingEndpointApi.md#fake_node_reclaim) | **GET** /fakeNodeReclaim | [INTERNAL] FakeNodeReclaim: Helps testing of AWS node reclaim behaviour


# **fake_node_reclaim**
> object fake_node_reclaim(seconds_until_reclaim=seconds_until_reclaim)

[INTERNAL] FakeNodeReclaim: Helps testing of AWS node reclaim behaviour

 An internal Method used to mark the next SIGTERM as though an Aws Node reclaim were about to take place. Simulates having received an AWS node reclaim warning, or similar.

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    HealthCheckingEndpointApi
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
        api_instance = api_client_factory.build(HealthCheckingEndpointApi)
        seconds_until_reclaim = 119 # int | the number of seconds from which to assume node termination (optional) (default to 119)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.fake_node_reclaim(seconds_until_reclaim=seconds_until_reclaim, opts=opts)

            # [INTERNAL] FakeNodeReclaim: Helps testing of AWS node reclaim behaviour
            api_response = await api_instance.fake_node_reclaim(seconds_until_reclaim=seconds_until_reclaim)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling HealthCheckingEndpointApi->fake_node_reclaim: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seconds_until_reclaim** | **int**| the number of seconds from which to assume node termination | [optional] [default to 119]

### Return type

**object**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

