# luminesce.ViewManagementApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_view_creation_sql**](ViewManagementApi.md#get_view_creation_sql) | **PUT** /api/View/sql | [EXPERIMENTAL] GetViewCreationSql: Gets the original source Sql for a view (if available)
[**list_views**](ViewManagementApi.md#list_views) | **GET** /api/View/list | [EXPERIMENTAL] ListViews: List views which are visible to the current users


# **get_view_creation_sql**
> str get_view_creation_sql(view_item=view_item)

[EXPERIMENTAL] GetViewCreationSql: Gets the original source Sql for a view (if available)

 Gets the original source Sql for a view (if available, 404 if not found in the logs)  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    ViewManagementApi
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
    api_instance = api_client_factory.build(ViewManagementApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # view_item = ViewItem.from_json("")
    # view_item = ViewItem.from_dict({})
    view_item = ViewItem()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_view_creation_sql(view_item=view_item, opts=opts)

        # [EXPERIMENTAL] GetViewCreationSql: Gets the original source Sql for a view (if available)
        api_response = api_instance.get_view_creation_sql(view_item=view_item)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ViewManagementApi->get_view_creation_sql: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_item** | [**ViewItem**](ViewItem.md)| View to fetch the create SQL for. Only the LastUpdatedAt and LastUpdatedExecutionId properties are required. | [optional] 

### Return type

**str**

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_views**
> List[ViewItem] list_views(show_all=show_all, reg_ex_filter=reg_ex_filter)

[EXPERIMENTAL] ListViews: List views which are visible to the current users

 Lists all the views which you have access, some limited filtering is available. These come from directly from persisted files in the file system.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    ViewManagementApi
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
    api_instance = api_client_factory.build(ViewManagementApi)
    show_all = False # bool | Show additional views if permissions allow (optional) (default to False)
    reg_ex_filter = 'reg_ex_filter_example' # str | Regular Expression filter to apply to the view content (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_views(show_all=show_all, reg_ex_filter=reg_ex_filter, opts=opts)

        # [EXPERIMENTAL] ListViews: List views which are visible to the current users
        api_response = api_instance.list_views(show_all=show_all, reg_ex_filter=reg_ex_filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ViewManagementApi->list_views: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_all** | **bool**| Show additional views if permissions allow | [optional] [default to False]
 **reg_ex_filter** | **str**| Regular Expression filter to apply to the view content | [optional] 

### Return type

[**List[ViewItem]**](ViewItem.md)

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

