# luminesce.HealthCheckingEndpointApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fake_node_reclaim**](HealthCheckingEndpointApi.md#fake_node_reclaim) | **GET** /fakeNodeReclaim | [INTERNAL] FakeNodeReclaim: An internal Method used to mark the next SIGTERM as though an Aws Node reclaim were about to take place.


# **fake_node_reclaim**
> object fake_node_reclaim(seconds_until_reclaim=seconds_until_reclaim)

[INTERNAL] FakeNodeReclaim: An internal Method used to mark the next SIGTERM as though an Aws Node reclaim were about to take place.

Internal testing controller to simulate having received an AWS node reclaim warning, or similar.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from pprint import pprint

import os
from luminesce import (
    ApiClientFactory,
    HealthCheckingEndpointApi,
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
    api_instance = api_client_factory.build(luminesce.HealthCheckingEndpointApi)
    seconds_until_reclaim = 119 # int | the number of seconds from which to assume node termination (optional) (default to 119)

    try:
        # [INTERNAL] FakeNodeReclaim: An internal Method used to mark the next SIGTERM as though an Aws Node reclaim were about to take place.
        api_response = await api_instance.fake_node_reclaim(seconds_until_reclaim=seconds_until_reclaim)
        print("The response of HealthCheckingEndpointApi->fake_node_reclaim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthCheckingEndpointApi->fake_node_reclaim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seconds_until_reclaim** | **int**| the number of seconds from which to assume node termination | [optional] [default to 119]

### Return type

**object**

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

