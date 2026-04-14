# luminesce.ViewManagementApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_view**](ViewManagementApi.md#delete_view) | **DELETE** /api/View/update | [EXPERIMENTAL] DeleteView: Deletes a view by name
[**get_view_creation_sql**](ViewManagementApi.md#get_view_creation_sql) | **PUT** /api/View/sql | [EXPERIMENTAL] GetViewCreationSql: Gets the original source Sql for a view (if available)
[**list_views**](ViewManagementApi.md#list_views) | **GET** /api/View/list | [EXPERIMENTAL] ListViews: List views which are visible to the current user
[**upsert_view**](ViewManagementApi.md#upsert_view) | **PUT** /api/View/update | [EXPERIMENTAL] UpsertView: Creates or updates a view from a full ViewDefinition.


# **delete_view**
> str delete_view(view_name=view_name)

[EXPERIMENTAL] DeleteView: Deletes a view by name

 Deletes a view.  This is primarily intended for use by an automated tool to synchronise views between domains.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

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
    view_name = 'view_name_example' # str | View to delete (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_view(view_name=view_name, opts=opts)

        # [EXPERIMENTAL] DeleteView: Deletes a view by name
        api_response = api_instance.delete_view(view_name=view_name)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ViewManagementApi->delete_view: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_name** | **str**| View to delete | [optional] 

### Return type

**str**

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
> List[ViewItem] list_views(show_all=show_all, reg_ex_filter=reg_ex_filter, name_like_filter=name_like_filter)

[EXPERIMENTAL] ListViews: List views which are visible to the current user

 Lists all the views which you have access to see. These come from directly from persisted files in the file system. Some limited filtering is available.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

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
    reg_ex_filter = 'reg_ex_filter_example' # str | Regular Expression filter to reduce the number of views returned, it is applied to the view *content* (this filter is applied withing the Filesystem itself.) (optional)
    name_like_filter = 'name_like_filter_example' # str | SQL Like-style filter on the view name, to reduce the number of views returned (this filter is applied to the Filesystem-returned view list.) (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_views(show_all=show_all, reg_ex_filter=reg_ex_filter, name_like_filter=name_like_filter, opts=opts)

        # [EXPERIMENTAL] ListViews: List views which are visible to the current user
        api_response = api_instance.list_views(show_all=show_all, reg_ex_filter=reg_ex_filter, name_like_filter=name_like_filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ViewManagementApi->list_views: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_all** | **bool**| Show additional views if permissions allow | [optional] [default to False]
 **reg_ex_filter** | **str**| Regular Expression filter to reduce the number of views returned, it is applied to the view *content* (this filter is applied withing the Filesystem itself.) | [optional] 
 **name_like_filter** | **str**| SQL Like-style filter on the view name, to reduce the number of views returned (this filter is applied to the Filesystem-returned view list.) | [optional] 

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

# **upsert_view**
> str upsert_view(allow_warnings=allow_warnings, may_update_existing=may_update_existing, view_item=view_item)

[EXPERIMENTAL] UpsertView: Creates or updates a view from a full ViewDefinition.

 Creates or updates a view from a full ViewDefinition.  Adds or creates a view from a view definition - without running the SQL of the view.  This is primarily intended for use by an automated tool to copy views between domains.  What this is *absolutely not* intended to do is to update views to tampered with definitions that were not originally created by `Sys.Admin.SetupView`, not even the smallest of changes are permitted as they may not work and will lead to additional support loads.  The flow for using fbn-config and these endpoints should generally be: - version control the `Sys.Admin.SetupView` query or the fbn-config resource that runs that query. - that can be automatically deployed to a development environment / domain. - an automated process then uses the `list` endpoint to get the full view definition (see above) from the dev-domain - then that definition can be given to a sit/uat/prod domain via this endpoint   - fbn-config could be responsible for this via a new resource type or simply a new, or any other script with PATs for both domains could be responsible for that)  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

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
    allow_warnings = False # bool | May views with *warnings* be upserted?  Regardless of this views with *errors* may not be. Warnings includes things like: - not using macros properly so that filters or aggregations cannot be passed down - using things like `select *` that can lead to results changing over time Errors includes things like: - uses a provider or view that simply doesn't exists (so perhaps a view this depends on needs creating first?) - The SQL or Metadata of the view was manually edited, not setup correctly by `Sys.Admin.SetupView` (optional) (default to False)
    may_update_existing = False # bool | May an existing view be overwritten?  Defaults to false to prevent accidental overwrites. Set to true when intentionally deploying an updated view definition to a domain. (optional) (default to False)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # view_item = ViewItem.from_json("")
    # view_item = ViewItem.from_dict({})
    view_item = ViewItem()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_view(allow_warnings=allow_warnings, may_update_existing=may_update_existing, view_item=view_item, opts=opts)

        # [EXPERIMENTAL] UpsertView: Creates or updates a view from a full ViewDefinition.
        api_response = api_instance.upsert_view(allow_warnings=allow_warnings, may_update_existing=may_update_existing, view_item=view_item)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ViewManagementApi->upsert_view: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_warnings** | **bool**| May views with *warnings* be upserted?  Regardless of this views with *errors* may not be. Warnings includes things like: - not using macros properly so that filters or aggregations cannot be passed down - using things like &#x60;select *&#x60; that can lead to results changing over time Errors includes things like: - uses a provider or view that simply doesn&#39;t exists (so perhaps a view this depends on needs creating first?) - The SQL or Metadata of the view was manually edited, not setup correctly by &#x60;Sys.Admin.SetupView&#x60; | [optional] [default to False]
 **may_update_existing** | **bool**| May an existing view be overwritten?  Defaults to false to prevent accidental overwrites. Set to true when intentionally deploying an updated view definition to a domain. | [optional] [default to False]
 **view_item** | [**ViewItem**](ViewItem.md)| View to create / change the definition of. | [optional] 

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

