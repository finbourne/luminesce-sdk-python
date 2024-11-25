# luminesce.HistoricallyExecutedQueriesApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_history**](HistoricallyExecutedQueriesApi.md#cancel_history) | **DELETE** /api/History/{executionId} | CancelHistory: Cancel / Clear data from a history search
[**fetch_history_result_histogram**](HistoricallyExecutedQueriesApi.md#fetch_history_result_histogram) | **GET** /api/History/{executionId}/histogram | FetchHistoryResultHistogram: Make a histogram of results of a history search
[**fetch_history_result_json**](HistoricallyExecutedQueriesApi.md#fetch_history_result_json) | **GET** /api/History/{executionId}/json | FetchHistoryResultJson: Fetch JSON results from a query history search
[**get_history**](HistoricallyExecutedQueriesApi.md#get_history) | **GET** /api/History | GetHistory: Start a background history search
[**get_progress_of_history**](HistoricallyExecutedQueriesApi.md#get_progress_of_history) | **GET** /api/History/{executionId} | GetProgressOfHistory: View progress of a history search


# **cancel_history**
> BackgroundQueryCancelResponse cancel_history(execution_id)

CancelHistory: Cancel / Clear data from a history search

Cancel the query (if still running) / clear the data (if already returned) The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't exist and is not running. 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    HistoricallyExecutedQueriesApi
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
    api_instance = api_client_factory.build(HistoricallyExecutedQueriesApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.cancel_history(execution_id, opts=opts)

        # CancelHistory: Cancel / Clear data from a history search
        api_response = api_instance.cancel_history(execution_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling HistoricallyExecutedQueriesApi->cancel_history: %s\n" % e)

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
**200** | Success |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **fetch_history_result_histogram**
> str fetch_history_result_histogram(execution_id, bucket_size=bucket_size, filter=filter, json_proper=json_proper)

FetchHistoryResultHistogram: Make a histogram of results of a history search

Fetch the histogram in Json format (if available, or if not simply being informed it is not yet ready) The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't (yet) exist. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    HistoricallyExecutedQueriesApi
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
    api_instance = api_client_factory.build(HistoricallyExecutedQueriesApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query
    bucket_size = 'bucket_size_example' # str | Optional histogram bucket width.  If not provided a set number of buckets between start/end range will be generated. (optional)
    filter = 'filter_example' # str | An ODATA filter per Finbourne.Filtering syntax. (optional)
    json_proper = False # bool | Should this be text/json (not json-encoded-as-a-string) (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.fetch_history_result_histogram(execution_id, bucket_size=bucket_size, filter=filter, json_proper=json_proper, opts=opts)

        # FetchHistoryResultHistogram: Make a histogram of results of a history search
        api_response = api_instance.fetch_history_result_histogram(execution_id, bucket_size=bucket_size, filter=filter, json_proper=json_proper)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling HistoricallyExecutedQueriesApi->fetch_history_result_histogram: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 
 **bucket_size** | **str**| Optional histogram bucket width.  If not provided a set number of buckets between start/end range will be generated. | [optional] 
 **filter** | **str**| An ODATA filter per Finbourne.Filtering syntax. | [optional] 
 **json_proper** | **bool**| Should this be text/json (not json-encoded-as-a-string) | [optional] [default to False]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **fetch_history_result_json**
> str fetch_history_result_json(execution_id, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, json_proper=json_proper)

FetchHistoryResultJson: Fetch JSON results from a query history search

Fetch the data in Json format (if available, or if not simply being informed it is not yet ready) The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't (yet) exist. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    HistoricallyExecutedQueriesApi
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
    api_instance = api_client_factory.build(HistoricallyExecutedQueriesApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query
    sort_by = 'sort_by_example' # str | Order the results by these fields.              Use the `-` sign to denote descending order, e.g. `-MyFieldName`.  Numeric indexes may be used also, e.g. `2,-3`.              Multiple fields can be denoted by a comma e.g. `-MyFieldName,AnotherFieldName,-AFurtherFieldName`.              Default is null, the sort order specified in the query itself. (optional)
    filter = 'filter_example' # str | An ODATA filter per Finbourne.Filtering syntax. (optional)
    select = 'select_example' # str | Default is null (meaning return all columns in the original query itself).  The values are in terms of the result column name from the original data set and are comma delimited.  The power of this comes in that you may aggregate the data if you wish  (that is the main reason for allowing this, in fact).  e.g.:  - `MyField`  - `Max(x) FILTER (WHERE y > 12) as ABC` (max of a field, if another field lets it qualify, with a nice column name)  - `count(*)` (count the rows for the given group, that would produce a rather ugly column name, but  it works)  - `count(distinct x) as numOfXs`  If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].   e.g.  - `some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name`    where you would likely want to pass `1` as the `groupBy` also. (optional)
    group_by = 'group_by_example' # str | Groups by the specified fields.              A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).              e.g. `2,3`, `myColumn`.              Default is null (meaning no grouping will be performed on the selected columns).              This applies only over the result set being requested here, meaning indexes into the \"select\" parameter fields.              Only specify this if you are selecting aggregations in the \"select\" parameter. (optional)
    limit = 0 # int | When paginating, only return this number of records, page should also be specified. (optional) (default to 0)
    page = 0 # int | 0-N based on chunk sized determined by the limit, ignored if limit < 1. (optional) (default to 0)
    json_proper = False # bool | Should this be text/json (not json-encoded-as-a-string) (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.fetch_history_result_json(execution_id, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, json_proper=json_proper, opts=opts)

        # FetchHistoryResultJson: Fetch JSON results from a query history search
        api_response = api_instance.fetch_history_result_json(execution_id, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, json_proper=json_proper)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling HistoricallyExecutedQueriesApi->fetch_history_result_json: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 
 **sort_by** | **str**| Order the results by these fields.              Use the &#x60;-&#x60; sign to denote descending order, e.g. &#x60;-MyFieldName&#x60;.  Numeric indexes may be used also, e.g. &#x60;2,-3&#x60;.              Multiple fields can be denoted by a comma e.g. &#x60;-MyFieldName,AnotherFieldName,-AFurtherFieldName&#x60;.              Default is null, the sort order specified in the query itself. | [optional] 
 **filter** | **str**| An ODATA filter per Finbourne.Filtering syntax. | [optional] 
 **select** | **str**| Default is null (meaning return all columns in the original query itself).  The values are in terms of the result column name from the original data set and are comma delimited.  The power of this comes in that you may aggregate the data if you wish  (that is the main reason for allowing this, in fact).  e.g.:  - &#x60;MyField&#x60;  - &#x60;Max(x) FILTER (WHERE y &gt; 12) as ABC&#x60; (max of a field, if another field lets it qualify, with a nice column name)  - &#x60;count(*)&#x60; (count the rows for the given group, that would produce a rather ugly column name, but  it works)  - &#x60;count(distinct x) as numOfXs&#x60;  If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].   e.g.  - &#x60;some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name&#x60;    where you would likely want to pass &#x60;1&#x60; as the &#x60;groupBy&#x60; also. | [optional] 
 **group_by** | **str**| Groups by the specified fields.              A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).              e.g. &#x60;2,3&#x60;, &#x60;myColumn&#x60;.              Default is null (meaning no grouping will be performed on the selected columns).              This applies only over the result set being requested here, meaning indexes into the \&quot;select\&quot; parameter fields.              Only specify this if you are selecting aggregations in the \&quot;select\&quot; parameter. | [optional] 
 **limit** | **int**| When paginating, only return this number of records, page should also be specified. | [optional] [default to 0]
 **page** | **int**| 0-N based on chunk sized determined by the limit, ignored if limit &lt; 1. | [optional] [default to 0]
 **json_proper** | **bool**| Should this be text/json (not json-encoded-as-a-string) | [optional] [default to False]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_history**
> BackgroundQueryResponse get_history(start_at=start_at, end_at=end_at, free_text_search=free_text_search, show_all=show_all, may_use_native_store=may_use_native_store)

GetHistory: Start a background history search

 Starts to load the historical query logs for a certain time range, search criteria, etc.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    HistoricallyExecutedQueriesApi
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
    api_instance = api_client_factory.build(HistoricallyExecutedQueriesApi)
    start_at = '2013-10-20T19:20:30+01:00' # datetime | Date time to start the search from.  Will default to Now - 1 Day (optional)
    end_at = '2013-10-20T19:20:30+01:00' # datetime | Date time to end the search at.  Defaults to now. (optional)
    free_text_search = 'free_text_search_example' # str | Some test that must be in at least one field returned. (optional)
    show_all = False # bool | For users with extra permissions, they may optionally see other users' queries. (optional) (default to False)
    may_use_native_store = True # bool | Should a native data store (e.g. Athena or Fabric) be used over Elastic Search if available? (optional) (default to True)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_history(start_at=start_at, end_at=end_at, free_text_search=free_text_search, show_all=show_all, may_use_native_store=may_use_native_store, opts=opts)

        # GetHistory: Start a background history search
        api_response = api_instance.get_history(start_at=start_at, end_at=end_at, free_text_search=free_text_search, show_all=show_all, may_use_native_store=may_use_native_store)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling HistoricallyExecutedQueriesApi->get_history: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_at** | **datetime**| Date time to start the search from.  Will default to Now - 1 Day | [optional] 
 **end_at** | **datetime**| Date time to end the search at.  Defaults to now. | [optional] 
 **free_text_search** | **str**| Some test that must be in at least one field returned. | [optional] 
 **show_all** | **bool**| For users with extra permissions, they may optionally see other users&#39; queries. | [optional] [default to False]
 **may_use_native_store** | **bool**| Should a native data store (e.g. Athena or Fabric) be used over Elastic Search if available? | [optional] [default to True]

### Return type

[**BackgroundQueryResponse**](BackgroundQueryResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_progress_of_history**
> BackgroundQueryProgressResponse get_progress_of_history(execution_id)

GetProgressOfHistory: View progress of a history search

View progress information (up until this point) of previously started History query The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't exist and is not running. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    HistoricallyExecutedQueriesApi
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
    api_instance = api_client_factory.build(HistoricallyExecutedQueriesApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_progress_of_history(execution_id, opts=opts)

        # GetProgressOfHistory: View progress of a history search
        api_response = api_instance.get_progress_of_history(execution_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling HistoricallyExecutedQueriesApi->get_progress_of_history: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 

### Return type

[**BackgroundQueryProgressResponse**](BackgroundQueryProgressResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

