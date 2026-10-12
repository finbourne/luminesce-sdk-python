# luminesce.MultiQueryExecutionApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_multi_query**](MultiQueryExecutionApi.md#cancel_multi_query) | **DELETE** /api/MultiQueryBackground/{executionId} | CancelMultiQuery: Cancel / Clear a previously started query-set
[**download_multi_query_results**](MultiQueryExecutionApi.md#download_multi_query_results) | **GET** /api/MultiQueryBackground/{executionId}/download | [EXPERIMENTAL] DownloadMultiQueryResults: Downloads the results of a custom query-set as one file
[**get_progress_of_multi_query**](MultiQueryExecutionApi.md#get_progress_of_multi_query) | **GET** /api/MultiQueryBackground/{executionId} | GetProgressOfMultiQuery: View progress of the entire query-set load
[**list_custom_queries**](MultiQueryExecutionApi.md#list_custom_queries) | **GET** /api/MultiQueryBackground | [EXPERIMENTAL] ListCustomQueries: List the custom query-sets available to the calling user
[**save_multi_query_results_to_drive**](MultiQueryExecutionApi.md#save_multi_query_results_to_drive) | **GET** /api/MultiQueryBackground/{executionId}/drive | [EXPERIMENTAL] SaveMultiQueryResultsToDrive: Saves the results of a custom query-set directly to Drive, as one file
[**start_custom_queries**](MultiQueryExecutionApi.md#start_custom_queries) | **PUT** /api/MultiQueryBackground/custom | [EXPERIMENTAL] StartCustomQueries: Run a caller-supplied set of Sql queries in the background
[**start_queries**](MultiQueryExecutionApi.md#start_queries) | **PUT** /api/MultiQueryBackground | StartQueries: Run a given set of Sql queries in the background


# **cancel_multi_query**
> BackgroundQueryCancelResponse cancel_multi_query(execution_id)

CancelMultiQuery: Cancel / Clear a previously started query-set

Cancel the query-set (if still running) / clear the data (if already returned) The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't exist and is not running. 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    MultiQueryExecutionApi
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
    api_instance = api_client_factory.build(MultiQueryExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.cancel_multi_query(execution_id, opts=opts)

        # CancelMultiQuery: Cancel / Clear a previously started query-set
        api_response = api_instance.cancel_multi_query(execution_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling MultiQueryExecutionApi->cancel_multi_query: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 

### Return type

[**BackgroundQueryCancelResponse**](BackgroundQueryCancelResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **download_multi_query_results**
> bytearray download_multi_query_results(execution_id, format=format, file_name=file_name, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds)

[EXPERIMENTAL] DownloadMultiQueryResults: Downloads the results of a custom query-set as one file

Exports the results of all the queries of a custom query-set (other than those which are not external results) as one file. Queries that failed, or were skipped as a query they depend on failed, are left out - though if none succeeded there is nothing to export.  The following error codes are to be anticipated most with standard Problem Detail reports: - 400 BadRequest : no query succeeded, or a placeholder or Drive parameter was incorrect in some way - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query-set doesn't exist, isn't a custom one, or the calling user did not run it. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    MultiQueryExecutionApi
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
    api_instance = api_client_factory.build(MultiQueryExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query-set
    format = luminesce.ExportType() # ExportType | Format to download in.  Several results are one worksheet each for Excel, one table each for Sqlite, and otherwise one file each within a zip. (optional)
    file_name = 'file_name_example' # str | Name of the file (without extension).  Defaults to `{executionId}`. May contain the placeholders `{executionId}`, `{date:format}` (when the queries started, UTC, e.g. `{date:yyyyMMdd}`) and `{param:name}` (the value of a scalar parameter). (optional)
    date_time_format = 'date_time_format_example' # str | Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently `yyyy-MM-dd HH:mm:ss.fff` (optional)
    load_wait_milliseconds = 0 # int | Optional maximum additional wait period for post execution platform processing. (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.download_multi_query_results(execution_id, format=format, file_name=file_name, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds, opts=opts)

        # [EXPERIMENTAL] DownloadMultiQueryResults: Downloads the results of a custom query-set as one file
        api_response = api_instance.download_multi_query_results(execution_id, format=format, file_name=file_name, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling MultiQueryExecutionApi->download_multi_query_results: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query-set | 
 **format** | [**ExportType**](.md)| Format to download in.  Several results are one worksheet each for Excel, one table each for Sqlite, and otherwise one file each within a zip. | [optional] 
 **file_name** | **str**| Name of the file (without extension).  Defaults to &#x60;{executionId}&#x60;. May contain the placeholders &#x60;{executionId}&#x60;, &#x60;{date:format}&#x60; (when the queries started, UTC, e.g. &#x60;{date:yyyyMMdd}&#x60;) and &#x60;{param:name}&#x60; (the value of a scalar parameter). | [optional] 
 **date_time_format** | **str**| Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently &#x60;yyyy-MM-dd HH:mm:ss.fff&#x60; | [optional] 
 **load_wait_milliseconds** | **int**| Optional maximum additional wait period for post execution platform processing. | [optional] [default to 0]

### Return type

**bytearray**

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

# **get_progress_of_multi_query**
> BackgroundMultiQueryProgressResponse get_progress_of_multi_query(execution_id)

GetProgressOfMultiQuery: View progress of the entire query-set load

View progress information (up until this point) for the entire query-set The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't exist and is not running. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    MultiQueryExecutionApi
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
    api_instance = api_client_factory.build(MultiQueryExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_progress_of_multi_query(execution_id, opts=opts)

        # GetProgressOfMultiQuery: View progress of the entire query-set load
        api_response = api_instance.get_progress_of_multi_query(execution_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling MultiQueryExecutionApi->get_progress_of_multi_query: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 

### Return type

[**BackgroundMultiQueryProgressResponse**](BackgroundMultiQueryProgressResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_custom_queries**
> List[CustomMultiQueryListItem] list_custom_queries(sql_like=sql_like)

[EXPERIMENTAL] ListCustomQueries: List the custom query-sets available to the calling user

Lists the custom query-sets (started by the calling user via `custom`) that have finished with at least one result which may be fetched,  and which have not yet passed their `keepForSeconds` time, most recent first.  Each lists its queries that are external results, and which of those have results. Those that errored are included, as some of their queries may still have succeeded.  The following error codes are to be anticipated most with standard Problem Detail reports: - 401 Unauthorized

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    MultiQueryExecutionApi
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
    api_instance = api_client_factory.build(MultiQueryExecutionApi)
    sql_like = 'sql_like_example' # str | An optional SQL-LIKE style filter on the LuminesceSql of the queries (manually include wildcards if desired), a query-set matching should any of its queries. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_custom_queries(sql_like=sql_like, opts=opts)

        # [EXPERIMENTAL] ListCustomQueries: List the custom query-sets available to the calling user
        api_response = api_instance.list_custom_queries(sql_like=sql_like)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling MultiQueryExecutionApi->list_custom_queries: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sql_like** | **str**| An optional SQL-LIKE style filter on the LuminesceSql of the queries (manually include wildcards if desired), a query-set matching should any of its queries. | [optional] 

### Return type

[**List[CustomMultiQueryListItem]**](CustomMultiQueryListItem.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **save_multi_query_results_to_drive**
> str save_multi_query_results_to_drive(execution_id, drive_location_and_file_name, may_overwrite=may_overwrite, format=format, drive_template_location=drive_template_location, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds)

[EXPERIMENTAL] SaveMultiQueryResultsToDrive: Saves the results of a custom query-set directly to Drive, as one file

Exports the results of all the queries of a custom query-set (other than those which are not external results) as one file. Queries that failed, or were skipped as a query they depend on failed, are left out - though if none succeeded there is nothing to export.  The following error codes are to be anticipated most with standard Problem Detail reports: - 400 BadRequest : no query succeeded, or a placeholder or Drive parameter was incorrect in some way - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query-set doesn't exist, isn't a custom one, or the calling user did not run it. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    MultiQueryExecutionApi
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
    api_instance = api_client_factory.build(MultiQueryExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query-set
    drive_location_and_file_name = 'drive_location_and_file_name_example' # str | Location and file name within drive where this should be saved to. Missing paths will be created, and extension (if given) will be ignored and inferred from the chosen format (zip where several results are zipped). May contain the placeholders `{executionId}`, `{date:format}` (when the queries started, UTC, e.g. `{date:yyyyMMdd}`) and `{param:name}` (the value of a scalar parameter).
    may_overwrite = False # bool | If there is an existing file at the requested location with the same name should this be overridden, or an error returned? (optional) (default to False)
    format = luminesce.ExportType() # ExportType | Format to save in.  Several results are one worksheet each for Excel, one table each for Sqlite, and otherwise one file each within a zip. (optional)
    drive_template_location = 'drive_template_location_example' # str | Drive path and full file name including extension to be used for the export. Only some export types support templates, such as Excel and Pdf, and this will need to match the format type, if given. (optional)
    date_time_format = 'date_time_format_example' # str | Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently `yyyy-MM-dd HH:mm:ss.fff` (optional)
    load_wait_milliseconds = 0 # int | Optional maximum additional wait period for post execution platform processing. (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.save_multi_query_results_to_drive(execution_id, drive_location_and_file_name, may_overwrite=may_overwrite, format=format, drive_template_location=drive_template_location, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds, opts=opts)

        # [EXPERIMENTAL] SaveMultiQueryResultsToDrive: Saves the results of a custom query-set directly to Drive, as one file
        api_response = api_instance.save_multi_query_results_to_drive(execution_id, drive_location_and_file_name, may_overwrite=may_overwrite, format=format, drive_template_location=drive_template_location, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling MultiQueryExecutionApi->save_multi_query_results_to_drive: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query-set | 
 **drive_location_and_file_name** | **str**| Location and file name within drive where this should be saved to. Missing paths will be created, and extension (if given) will be ignored and inferred from the chosen format (zip where several results are zipped). May contain the placeholders &#x60;{executionId}&#x60;, &#x60;{date:format}&#x60; (when the queries started, UTC, e.g. &#x60;{date:yyyyMMdd}&#x60;) and &#x60;{param:name}&#x60; (the value of a scalar parameter). | 
 **may_overwrite** | **bool**| If there is an existing file at the requested location with the same name should this be overridden, or an error returned? | [optional] [default to False]
 **format** | [**ExportType**](.md)| Format to save in.  Several results are one worksheet each for Excel, one table each for Sqlite, and otherwise one file each within a zip. | [optional] 
 **drive_template_location** | **str**| Drive path and full file name including extension to be used for the export. Only some export types support templates, such as Excel and Pdf, and this will need to match the format type, if given. | [optional] 
 **date_time_format** | **str**| Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently &#x60;yyyy-MM-dd HH:mm:ss.fff&#x60; | [optional] 
 **load_wait_milliseconds** | **int**| Optional maximum additional wait period for post execution platform processing. | [optional] [default to 0]

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

# **start_custom_queries**
> BackgroundMultiQueryResponse start_custom_queries(custom_multi_query_request)

[EXPERIMENTAL] StartCustomQueries: Run a caller-supplied set of Sql queries in the background

 Starts a caller-supplied set of named queries in the background, getting back an immediate response with how to - fetch the data of each (external) query in various formats, view progress information and cancel / clear them, as for any multi-query - download, or save to Drive, the results of all the (external) queries that succeeded as one file  The queries are started in the order given, at most `maxInParallel` at a time (1 by default, null for as many as possible). A query may use the results of an earlier one as a table variable of its name, e.g. `select * from @Holdings`, and is then only started once that has succeeded (and is skipped if it does not).  The scalar parameters are given to every query.  The multi-query as a whole is reported as failed if any of its queries fails or is skipped.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - the request was invalid, a Saved Query could not be loaded, or there was something wrong with the syntax of a query - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    MultiQueryExecutionApi
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
    api_instance = api_client_factory.build(MultiQueryExecutionApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # custom_multi_query_request = CustomMultiQueryRequest.from_json("")
    # custom_multi_query_request = CustomMultiQueryRequest.from_dict({})
    custom_multi_query_request = CustomMultiQueryRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.start_custom_queries(custom_multi_query_request, opts=opts)

        # [EXPERIMENTAL] StartCustomQueries: Run a caller-supplied set of Sql queries in the background
        api_response = api_instance.start_custom_queries(custom_multi_query_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling MultiQueryExecutionApi->start_custom_queries: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_multi_query_request** | [**CustomMultiQueryRequest**](CustomMultiQueryRequest.md)| The queries to run (as LuminesceSql or Saved Query references), the scalar parameters for them all, etc. | 

### Return type

[**BackgroundMultiQueryResponse**](BackgroundMultiQueryResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **start_queries**
> BackgroundMultiQueryResponse start_queries(type, body, as_at=as_at, effective_at=effective_at, limit1=limit1, limit2=limit2, input1=input1, input2=input2, input3=input3, timeout_seconds=timeout_seconds, keep_for_seconds=keep_for_seconds)

StartQueries: Run a given set of Sql queries in the background

 Allow for starting a potentially long running query and getting back an immediate response with how to  - fetch the data in various formats (if available, or if not simply being informed it is not yet ready), on a per result basis - view progress information (up until this point), for all results in one go - cancel the queries (if still running) / clear the data (if already returned)  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - there was something wrong with your query syntax (the issue was detected at parse-time) - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    MultiQueryExecutionApi
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
    api_instance = api_client_factory.build(MultiQueryExecutionApi)
    type = luminesce.MultiQueryDefinitionType() # MultiQueryDefinitionType | An enum value defining the set of statements being executed
    body = Apple # str | A \"search\" value (e.g. 'Apple' on an instrument search, a `Finbourne.Filtering` expression of Insights, etc.) In the cases where \"Nothing\" is valid for a `Finbourne.Filtering` expression, pass `True`.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt time used by any bitemporal provider in the queries. (optional)
    effective_at = '2013-10-20T19:20:30+01:00' # datetime | The EffectiveAt time used by any bitemporal provider in the queries. (optional)
    limit1 = 56 # int | A limit that is applied to first-level queries (e.g. Instruments themselves) (optional)
    limit2 = 56 # int | A limit that is applied to second-level queries (e.g. Holdings based on the set of Instruments found) (optional)
    input1 = 'input1_example' # str | A value available to queries, these vary by 'type' and are only used by some types at all. e.g. a start-date of some sort (optional)
    input2 = 'input2_example' # str | A second value available to queries, these vary by 'type' and are only used by some types at all. (optional)
    input3 = 'input3_example' # str | A third value available to queries, these vary by 'type' and are only used by some types at all. (optional)
    timeout_seconds = 0 # int | Maximum time the query may run for, in seconds: <0 → ∞, 0 → 1200s (20m) (optional) (default to 0)
    keep_for_seconds = 0 # int | Maximum time the result may be kept for, in seconds: <0 → 1200 (20m), 0 → 28800 (8h), max = 2,678,400 (31d) (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.start_queries(type, body, as_at=as_at, effective_at=effective_at, limit1=limit1, limit2=limit2, input1=input1, input2=input2, input3=input3, timeout_seconds=timeout_seconds, keep_for_seconds=keep_for_seconds, opts=opts)

        # StartQueries: Run a given set of Sql queries in the background
        api_response = api_instance.start_queries(type, body, as_at=as_at, effective_at=effective_at, limit1=limit1, limit2=limit2, input1=input1, input2=input2, input3=input3, timeout_seconds=timeout_seconds, keep_for_seconds=keep_for_seconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling MultiQueryExecutionApi->start_queries: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**MultiQueryDefinitionType**](.md)| An enum value defining the set of statements being executed | 
 **body** | **str**| A \&quot;search\&quot; value (e.g. &#39;Apple&#39; on an instrument search, a &#x60;Finbourne.Filtering&#x60; expression of Insights, etc.) In the cases where \&quot;Nothing\&quot; is valid for a &#x60;Finbourne.Filtering&#x60; expression, pass &#x60;True&#x60;. | 
 **as_at** | **datetime**| The AsAt time used by any bitemporal provider in the queries. | [optional] 
 **effective_at** | **datetime**| The EffectiveAt time used by any bitemporal provider in the queries. | [optional] 
 **limit1** | **int**| A limit that is applied to first-level queries (e.g. Instruments themselves) | [optional] 
 **limit2** | **int**| A limit that is applied to second-level queries (e.g. Holdings based on the set of Instruments found) | [optional] 
 **input1** | **str**| A value available to queries, these vary by &#39;type&#39; and are only used by some types at all. e.g. a start-date of some sort | [optional] 
 **input2** | **str**| A second value available to queries, these vary by &#39;type&#39; and are only used by some types at all. | [optional] 
 **input3** | **str**| A third value available to queries, these vary by &#39;type&#39; and are only used by some types at all. | [optional] 
 **timeout_seconds** | **int**| Maximum time the query may run for, in seconds: &lt;0 → ∞, 0 → 1200s (20m) | [optional] [default to 0]
 **keep_for_seconds** | **int**| Maximum time the result may be kept for, in seconds: &lt;0 → 1200 (20m), 0 → 28800 (8h), max &#x3D; 2,678,400 (31d) | [optional] [default to 0]

### Return type

[**BackgroundMultiQueryResponse**](BackgroundMultiQueryResponse.md)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

