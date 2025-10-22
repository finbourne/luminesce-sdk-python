# luminesce.SqlBackgroundExecutionApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_query**](SqlBackgroundExecutionApi.md#cancel_query) | **DELETE** /api/SqlBackground/{executionId} | CancelQuery: Cancel / Clear data from a previously run query
[**fetch_query_result_csv**](SqlBackgroundExecutionApi.md#fetch_query_result_csv) | **GET** /api/SqlBackground/{executionId}/csv | FetchQueryResultCsv: Fetch the result of a query as CSV
[**fetch_query_result_excel**](SqlBackgroundExecutionApi.md#fetch_query_result_excel) | **GET** /api/SqlBackground/{executionId}/excel | FetchQueryResultExcel: Fetch the result of a query as an Excel file
[**fetch_query_result_histogram**](SqlBackgroundExecutionApi.md#fetch_query_result_histogram) | **GET** /api/SqlBackground/{executionId}/histogram | FetchQueryResultHistogram: Construct a histogram of the result of a query
[**fetch_query_result_json**](SqlBackgroundExecutionApi.md#fetch_query_result_json) | **GET** /api/SqlBackground/{executionId}/json | FetchQueryResultJson: Fetch the result of a query as a JSON string
[**fetch_query_result_json_proper**](SqlBackgroundExecutionApi.md#fetch_query_result_json_proper) | **GET** /api/SqlBackground/{executionId}/jsonProper | FetchQueryResultJsonProper: Fetch the result of a query as JSON
[**fetch_query_result_parquet**](SqlBackgroundExecutionApi.md#fetch_query_result_parquet) | **GET** /api/SqlBackground/{executionId}/parquet | FetchQueryResultParquet: Fetch the result of a query as Parquet
[**fetch_query_result_pipe**](SqlBackgroundExecutionApi.md#fetch_query_result_pipe) | **GET** /api/SqlBackground/{executionId}/pipe | FetchQueryResultPipe: Fetch the result of a query as pipe-delimited
[**fetch_query_result_sqlite**](SqlBackgroundExecutionApi.md#fetch_query_result_sqlite) | **GET** /api/SqlBackground/{executionId}/sqlite | FetchQueryResultSqlite: Fetch the result of a query as SqLite
[**fetch_query_result_xml**](SqlBackgroundExecutionApi.md#fetch_query_result_xml) | **GET** /api/SqlBackground/{executionId}/xml | FetchQueryResultXml: Fetch the result of a query as XML
[**get_historical_feedback**](SqlBackgroundExecutionApi.md#get_historical_feedback) | **GET** /api/SqlBackground/{executionId}/historicalFeedback | GetHistoricalFeedback: View query progress up to this point
[**get_progress_of**](SqlBackgroundExecutionApi.md#get_progress_of) | **GET** /api/SqlBackground/{executionId} | GetProgressOf: View query progress up to this point.
[**start_query**](SqlBackgroundExecutionApi.md#start_query) | **PUT** /api/SqlBackground | StartQuery: Start to Execute Sql in the background


# **cancel_query**
> BackgroundQueryCancelResponse cancel_query(execution_id)

CancelQuery: Cancel / Clear data from a previously run query

Cancel the query (if still running) / clear the data (if already returned) The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't exist and is not running or the calling user did not run the query. 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlBackgroundExecutionApi
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
    api_instance = api_client_factory.build(SqlBackgroundExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.cancel_query(execution_id, opts=opts)

        # CancelQuery: Cancel / Clear data from a previously run query
        api_response = api_instance.cancel_query(execution_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlBackgroundExecutionApi->cancel_query: %s\n" % e)

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

# **fetch_query_result_csv**
> str fetch_query_result_csv(execution_id, download=download, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, delimiter=delimiter, escape=escape, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds)

FetchQueryResultCsv: Fetch the result of a query as CSV

Fetch the data in the format of the method's name (if available, or if not simply being informed it is not yet ready).  The following error codes are to be anticipated most with standard Problem Detail reports: - 400 BadRequest : Something failed with the execution of your query - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't (yet) exist or the calling user did not run the query. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlBackgroundExecutionApi
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
    api_instance = api_client_factory.build(SqlBackgroundExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query
    download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
    sort_by = 'sort_by_example' # str | Order the results by these fields.             Use the `-` sign to denote descending order, e.g. `-MyFieldName`.  Numeric indexes may be used also, e.g. `2,-3`.             Multiple fields can be denoted by a comma e.g. `-MyFieldName,AnotherFieldName,-AFurtherFieldName`.             Default is null, the sort order specified in the query itself. (optional)
    filter = 'filter_example' # str | An ODATA filter per Finbourne.Filtering syntax. (optional)
    select = 'select_example' # str | Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - `MyField` - `Max(x) FILTER (WHERE y > 12) as ABC` (max of a field, if another field lets it qualify, with a nice column name) - `count(*)` (count the rows for the given group, that would produce a rather ugly column name, but  it works) - `count(distinct x) as numOfXs` If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - `some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name`   where you would likely want to pass `1` as the `groupBy` also. (optional)
    group_by = 'group_by_example' # str | Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. `2,3`, `myColumn`.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \"select\" parameter fields.             Only specify this if you are selecting aggregations in the \"select\" parameter. (optional)
    limit = 0 # int | When paginating, only return this number of records, page should also be specified. (optional) (default to 0)
    page = 0 # int | 0-N based on chunk sized determined by the limit, ignored if limit < 1. (optional) (default to 0)
    delimiter = 'delimiter_example' # str | Delimiter string to override the default (optional)
    escape = 'escape_example' # str | Escape character to override the default (optional)
    date_time_format = 'date_time_format_example' # str | Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently `yyyy-MM-dd HH:mm:ss.fff` (optional)
    load_wait_milliseconds = 0 # int | Optional maximum additional wait period for post execution platform processing. (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.fetch_query_result_csv(execution_id, download=download, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, delimiter=delimiter, escape=escape, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds, opts=opts)

        # FetchQueryResultCsv: Fetch the result of a query as CSV
        api_response = api_instance.fetch_query_result_csv(execution_id, download=download, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, delimiter=delimiter, escape=escape, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlBackgroundExecutionApi->fetch_query_result_csv: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **sort_by** | **str**| Order the results by these fields.             Use the &#x60;-&#x60; sign to denote descending order, e.g. &#x60;-MyFieldName&#x60;.  Numeric indexes may be used also, e.g. &#x60;2,-3&#x60;.             Multiple fields can be denoted by a comma e.g. &#x60;-MyFieldName,AnotherFieldName,-AFurtherFieldName&#x60;.             Default is null, the sort order specified in the query itself. | [optional] 
 **filter** | **str**| An ODATA filter per Finbourne.Filtering syntax. | [optional] 
 **select** | **str**| Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - &#x60;MyField&#x60; - &#x60;Max(x) FILTER (WHERE y &gt; 12) as ABC&#x60; (max of a field, if another field lets it qualify, with a nice column name) - &#x60;count(*)&#x60; (count the rows for the given group, that would produce a rather ugly column name, but  it works) - &#x60;count(distinct x) as numOfXs&#x60; If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - &#x60;some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name&#x60;   where you would likely want to pass &#x60;1&#x60; as the &#x60;groupBy&#x60; also. | [optional] 
 **group_by** | **str**| Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. &#x60;2,3&#x60;, &#x60;myColumn&#x60;.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \&quot;select\&quot; parameter fields.             Only specify this if you are selecting aggregations in the \&quot;select\&quot; parameter. | [optional] 
 **limit** | **int**| When paginating, only return this number of records, page should also be specified. | [optional] [default to 0]
 **page** | **int**| 0-N based on chunk sized determined by the limit, ignored if limit &lt; 1. | [optional] [default to 0]
 **delimiter** | **str**| Delimiter string to override the default | [optional] 
 **escape** | **str**| Escape character to override the default | [optional] 
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

# **fetch_query_result_excel**
> bytearray fetch_query_result_excel(execution_id, sort_by=sort_by, filter=filter, select=select, group_by=group_by, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds)

FetchQueryResultExcel: Fetch the result of a query as an Excel file

Fetch the data in the format of the method's name (if available, or if not simply being informed it is not yet ready).  The following error codes are to be anticipated most with standard Problem Detail reports: - 400 BadRequest : Something failed with the execution of your query - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't (yet) exist or the calling user did not run the query. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlBackgroundExecutionApi
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
    api_instance = api_client_factory.build(SqlBackgroundExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query
    sort_by = 'sort_by_example' # str | Order the results by these fields.             Use the `-` sign to denote descending order, e.g. `-MyFieldName`.  Numeric indexes may be used also, e.g. `2,-3`.             Multiple fields can be denoted by a comma e.g. `-MyFieldName,AnotherFieldName,-AFurtherFieldName`.             Default is null, the sort order specified in the query itself. (optional)
    filter = 'filter_example' # str | An ODATA filter per Finbourne.Filtering syntax. (optional)
    select = 'select_example' # str | Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - `MyField` - `Max(x) FILTER (WHERE y > 12) as ABC` (max of a field, if another field lets it qualify, with a nice column name) - `count(*)` (count the rows for the given group, that would produce a rather ugly column name, but  it works) - `count(distinct x) as numOfXs` If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - `some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name`   where you would likely want to pass `1` as the `groupBy` also. (optional)
    group_by = 'group_by_example' # str | Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. `2,3`, `myColumn`.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \"select\" parameter fields.             Only specify this if you are selecting aggregations in the \"select\" parameter. (optional)
    date_time_format = 'date_time_format_example' # str | Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently `yyyy-MM-dd HH:mm:ss.fff` (optional)
    load_wait_milliseconds = 0 # int | Optional maximum additional wait period for post execution platform processing. (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.fetch_query_result_excel(execution_id, sort_by=sort_by, filter=filter, select=select, group_by=group_by, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds, opts=opts)

        # FetchQueryResultExcel: Fetch the result of a query as an Excel file
        api_response = api_instance.fetch_query_result_excel(execution_id, sort_by=sort_by, filter=filter, select=select, group_by=group_by, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlBackgroundExecutionApi->fetch_query_result_excel: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 
 **sort_by** | **str**| Order the results by these fields.             Use the &#x60;-&#x60; sign to denote descending order, e.g. &#x60;-MyFieldName&#x60;.  Numeric indexes may be used also, e.g. &#x60;2,-3&#x60;.             Multiple fields can be denoted by a comma e.g. &#x60;-MyFieldName,AnotherFieldName,-AFurtherFieldName&#x60;.             Default is null, the sort order specified in the query itself. | [optional] 
 **filter** | **str**| An ODATA filter per Finbourne.Filtering syntax. | [optional] 
 **select** | **str**| Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - &#x60;MyField&#x60; - &#x60;Max(x) FILTER (WHERE y &gt; 12) as ABC&#x60; (max of a field, if another field lets it qualify, with a nice column name) - &#x60;count(*)&#x60; (count the rows for the given group, that would produce a rather ugly column name, but  it works) - &#x60;count(distinct x) as numOfXs&#x60; If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - &#x60;some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name&#x60;   where you would likely want to pass &#x60;1&#x60; as the &#x60;groupBy&#x60; also. | [optional] 
 **group_by** | **str**| Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. &#x60;2,3&#x60;, &#x60;myColumn&#x60;.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \&quot;select\&quot; parameter fields.             Only specify this if you are selecting aggregations in the \&quot;select\&quot; parameter. | [optional] 
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

# **fetch_query_result_histogram**
> str fetch_query_result_histogram(execution_id, timestamp_field_name, start_at=start_at, end_at=end_at, bucket_size=bucket_size, filter=filter, json_proper=json_proper)

FetchQueryResultHistogram: Construct a histogram of the result of a query

Fetch the histogram in Json format (if available, or if not simply being informed it is not yet ready) The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't (yet) exist or the calling user did not run the query. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlBackgroundExecutionApi
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
    api_instance = api_client_factory.build(SqlBackgroundExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query
    timestamp_field_name = 'timestamp_field_name_example' # str | Name of the timestamp field used in building the histogram
    start_at = '2013-10-20T19:20:30+01:00' # datetime | Start point (of the timestampFieldName field) for the histogram (optional)
    end_at = '2013-10-20T19:20:30+01:00' # datetime | End point (of the timestampFieldName field) for the histogram (optional)
    bucket_size = 'bucket_size_example' # str | Optional histogram bucket width.  If not provided a set number of buckets between start/end range will be generated. (optional)
    filter = 'filter_example' # str | An ODATA filter per Finbourne.Filtering syntax. (optional)
    json_proper = False # bool | Should this be text/json (not json-encoded-as-a-string) (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.fetch_query_result_histogram(execution_id, timestamp_field_name, start_at=start_at, end_at=end_at, bucket_size=bucket_size, filter=filter, json_proper=json_proper, opts=opts)

        # FetchQueryResultHistogram: Construct a histogram of the result of a query
        api_response = api_instance.fetch_query_result_histogram(execution_id, timestamp_field_name, start_at=start_at, end_at=end_at, bucket_size=bucket_size, filter=filter, json_proper=json_proper)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlBackgroundExecutionApi->fetch_query_result_histogram: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 
 **timestamp_field_name** | **str**| Name of the timestamp field used in building the histogram | 
 **start_at** | **datetime**| Start point (of the timestampFieldName field) for the histogram | [optional] 
 **end_at** | **datetime**| End point (of the timestampFieldName field) for the histogram | [optional] 
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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **fetch_query_result_json**
> str fetch_query_result_json(execution_id, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, load_wait_milliseconds=load_wait_milliseconds)

FetchQueryResultJson: Fetch the result of a query as a JSON string

 *Please move to '/jsonProper' instead.  This may be marked as Deprecated in the future.*  Fetch the data in the format of the method's name (if available, or if not simply being informed it is not yet ready).  The following error codes are to be anticipated most with standard Problem Detail reports: - 400 BadRequest : Something failed with the execution of your query - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't (yet) exist or the calling user did not run the query. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlBackgroundExecutionApi
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
    api_instance = api_client_factory.build(SqlBackgroundExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query
    sort_by = 'sort_by_example' # str | Order the results by these fields.             Use the `-` sign to denote descending order, e.g. `-MyFieldName`.  Numeric indexes may be used also, e.g. `2,-3`.             Multiple fields can be denoted by a comma e.g. `-MyFieldName,AnotherFieldName,-AFurtherFieldName`.             Default is null, the sort order specified in the query itself. (optional)
    filter = 'filter_example' # str | An ODATA filter per Finbourne.Filtering syntax. (optional)
    select = 'select_example' # str | Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - `MyField` - `Max(x) FILTER (WHERE y > 12) as ABC` (max of a field, if another field lets it qualify, with a nice column name) - `count(*)` (count the rows for the given group, that would produce a rather ugly column name, but  it works) - `count(distinct x) as numOfXs` If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - `some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name`   where you would likely want to pass `1` as the `groupBy` also. (optional)
    group_by = 'group_by_example' # str | Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. `2,3`, `myColumn`.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \"select\" parameter fields.             Only specify this if you are selecting aggregations in the \"select\" parameter. (optional)
    limit = 0 # int | When paginating, only return this number of records, page should also be specified. (optional) (default to 0)
    page = 0 # int | 0-N based on chunk sized determined by the limit, ignored if limit < 1. (optional) (default to 0)
    load_wait_milliseconds = 0 # int | Optional maximum additional wait period for post execution platform processing. (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.fetch_query_result_json(execution_id, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, load_wait_milliseconds=load_wait_milliseconds, opts=opts)

        # FetchQueryResultJson: Fetch the result of a query as a JSON string
        api_response = api_instance.fetch_query_result_json(execution_id, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, load_wait_milliseconds=load_wait_milliseconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlBackgroundExecutionApi->fetch_query_result_json: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 
 **sort_by** | **str**| Order the results by these fields.             Use the &#x60;-&#x60; sign to denote descending order, e.g. &#x60;-MyFieldName&#x60;.  Numeric indexes may be used also, e.g. &#x60;2,-3&#x60;.             Multiple fields can be denoted by a comma e.g. &#x60;-MyFieldName,AnotherFieldName,-AFurtherFieldName&#x60;.             Default is null, the sort order specified in the query itself. | [optional] 
 **filter** | **str**| An ODATA filter per Finbourne.Filtering syntax. | [optional] 
 **select** | **str**| Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - &#x60;MyField&#x60; - &#x60;Max(x) FILTER (WHERE y &gt; 12) as ABC&#x60; (max of a field, if another field lets it qualify, with a nice column name) - &#x60;count(*)&#x60; (count the rows for the given group, that would produce a rather ugly column name, but  it works) - &#x60;count(distinct x) as numOfXs&#x60; If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - &#x60;some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name&#x60;   where you would likely want to pass &#x60;1&#x60; as the &#x60;groupBy&#x60; also. | [optional] 
 **group_by** | **str**| Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. &#x60;2,3&#x60;, &#x60;myColumn&#x60;.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \&quot;select\&quot; parameter fields.             Only specify this if you are selecting aggregations in the \&quot;select\&quot; parameter. | [optional] 
 **limit** | **int**| When paginating, only return this number of records, page should also be specified. | [optional] [default to 0]
 **page** | **int**| 0-N based on chunk sized determined by the limit, ignored if limit &lt; 1. | [optional] [default to 0]
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

# **fetch_query_result_json_proper**
> str fetch_query_result_json_proper(execution_id, download=download, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, load_wait_milliseconds=load_wait_milliseconds)

FetchQueryResultJsonProper: Fetch the result of a query as JSON

Fetch the data in the format of the method's name (if available, or if not simply being informed it is not yet ready).  The following error codes are to be anticipated most with standard Problem Detail reports: - 400 BadRequest : Something failed with the execution of your query - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't (yet) exist or the calling user did not run the query. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlBackgroundExecutionApi
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
    api_instance = api_client_factory.build(SqlBackgroundExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query
    download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
    sort_by = 'sort_by_example' # str | Order the results by these fields.             Use the `-` sign to denote descending order, e.g. `-MyFieldName`.  Numeric indexes may be used also, e.g. `2,-3`.             Multiple fields can be denoted by a comma e.g. `-MyFieldName,AnotherFieldName,-AFurtherFieldName`.             Default is null, the sort order specified in the query itself. (optional)
    filter = 'filter_example' # str | An ODATA filter per Finbourne.Filtering syntax. (optional)
    select = 'select_example' # str | Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - `MyField` - `Max(x) FILTER (WHERE y > 12) as ABC` (max of a field, if another field lets it qualify, with a nice column name) - `count(*)` (count the rows for the given group, that would produce a rather ugly column name, but  it works) - `count(distinct x) as numOfXs` If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - `some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name`   where you would likely want to pass `1` as the `groupBy` also. (optional)
    group_by = 'group_by_example' # str | Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. `2,3`, `myColumn`.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \"select\" parameter fields.             Only specify this if you are selecting aggregations in the \"select\" parameter. (optional)
    limit = 0 # int | When paginating, only return this number of records, page should also be specified. (optional) (default to 0)
    page = 0 # int | 0-N based on chunk sized determined by the limit, ignored if limit < 1. (optional) (default to 0)
    load_wait_milliseconds = 0 # int | Optional maximum additional wait period for post execution platform processing. (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.fetch_query_result_json_proper(execution_id, download=download, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, load_wait_milliseconds=load_wait_milliseconds, opts=opts)

        # FetchQueryResultJsonProper: Fetch the result of a query as JSON
        api_response = api_instance.fetch_query_result_json_proper(execution_id, download=download, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, load_wait_milliseconds=load_wait_milliseconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlBackgroundExecutionApi->fetch_query_result_json_proper: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **sort_by** | **str**| Order the results by these fields.             Use the &#x60;-&#x60; sign to denote descending order, e.g. &#x60;-MyFieldName&#x60;.  Numeric indexes may be used also, e.g. &#x60;2,-3&#x60;.             Multiple fields can be denoted by a comma e.g. &#x60;-MyFieldName,AnotherFieldName,-AFurtherFieldName&#x60;.             Default is null, the sort order specified in the query itself. | [optional] 
 **filter** | **str**| An ODATA filter per Finbourne.Filtering syntax. | [optional] 
 **select** | **str**| Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - &#x60;MyField&#x60; - &#x60;Max(x) FILTER (WHERE y &gt; 12) as ABC&#x60; (max of a field, if another field lets it qualify, with a nice column name) - &#x60;count(*)&#x60; (count the rows for the given group, that would produce a rather ugly column name, but  it works) - &#x60;count(distinct x) as numOfXs&#x60; If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - &#x60;some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name&#x60;   where you would likely want to pass &#x60;1&#x60; as the &#x60;groupBy&#x60; also. | [optional] 
 **group_by** | **str**| Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. &#x60;2,3&#x60;, &#x60;myColumn&#x60;.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \&quot;select\&quot; parameter fields.             Only specify this if you are selecting aggregations in the \&quot;select\&quot; parameter. | [optional] 
 **limit** | **int**| When paginating, only return this number of records, page should also be specified. | [optional] [default to 0]
 **page** | **int**| 0-N based on chunk sized determined by the limit, ignored if limit &lt; 1. | [optional] [default to 0]
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

# **fetch_query_result_parquet**
> bytearray fetch_query_result_parquet(execution_id, sort_by=sort_by, filter=filter, select=select, group_by=group_by, load_wait_milliseconds=load_wait_milliseconds)

FetchQueryResultParquet: Fetch the result of a query as Parquet

Fetch the data in the format of the method's name (if available, or if not simply being informed it is not yet ready).  The following error codes are to be anticipated most with standard Problem Detail reports: - 400 BadRequest : Something failed with the execution of your query - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't (yet) exist or the calling user did not run the query. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlBackgroundExecutionApi
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
    api_instance = api_client_factory.build(SqlBackgroundExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query
    sort_by = 'sort_by_example' # str | Order the results by these fields.             Use the `-` sign to denote descending order, e.g. `-MyFieldName`.  Numeric indexes may be used also, e.g. `2,-3`.             Multiple fields can be denoted by a comma e.g. `-MyFieldName,AnotherFieldName,-AFurtherFieldName`.             Default is null, the sort order specified in the query itself. (optional)
    filter = 'filter_example' # str | An ODATA filter per Finbourne.Filtering syntax. (optional)
    select = 'select_example' # str | Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - `MyField` - `Max(x) FILTER (WHERE y > 12) as ABC` (max of a field, if another field lets it qualify, with a nice column name) - `count(*)` (count the rows for the given group, that would produce a rather ugly column name, but  it works) - `count(distinct x) as numOfXs` If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - `some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name`   where you would likely want to pass `1` as the `groupBy` also. (optional)
    group_by = 'group_by_example' # str | Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. `2,3`, `myColumn`.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \"select\" parameter fields.             Only specify this if you are selecting aggregations in the \"select\" parameter. (optional)
    load_wait_milliseconds = 0 # int | Optional maximum additional wait period for post execution platform processing. (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.fetch_query_result_parquet(execution_id, sort_by=sort_by, filter=filter, select=select, group_by=group_by, load_wait_milliseconds=load_wait_milliseconds, opts=opts)

        # FetchQueryResultParquet: Fetch the result of a query as Parquet
        api_response = api_instance.fetch_query_result_parquet(execution_id, sort_by=sort_by, filter=filter, select=select, group_by=group_by, load_wait_milliseconds=load_wait_milliseconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlBackgroundExecutionApi->fetch_query_result_parquet: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 
 **sort_by** | **str**| Order the results by these fields.             Use the &#x60;-&#x60; sign to denote descending order, e.g. &#x60;-MyFieldName&#x60;.  Numeric indexes may be used also, e.g. &#x60;2,-3&#x60;.             Multiple fields can be denoted by a comma e.g. &#x60;-MyFieldName,AnotherFieldName,-AFurtherFieldName&#x60;.             Default is null, the sort order specified in the query itself. | [optional] 
 **filter** | **str**| An ODATA filter per Finbourne.Filtering syntax. | [optional] 
 **select** | **str**| Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - &#x60;MyField&#x60; - &#x60;Max(x) FILTER (WHERE y &gt; 12) as ABC&#x60; (max of a field, if another field lets it qualify, with a nice column name) - &#x60;count(*)&#x60; (count the rows for the given group, that would produce a rather ugly column name, but  it works) - &#x60;count(distinct x) as numOfXs&#x60; If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - &#x60;some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name&#x60;   where you would likely want to pass &#x60;1&#x60; as the &#x60;groupBy&#x60; also. | [optional] 
 **group_by** | **str**| Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. &#x60;2,3&#x60;, &#x60;myColumn&#x60;.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \&quot;select\&quot; parameter fields.             Only specify this if you are selecting aggregations in the \&quot;select\&quot; parameter. | [optional] 
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

# **fetch_query_result_pipe**
> str fetch_query_result_pipe(execution_id, download=download, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds)

FetchQueryResultPipe: Fetch the result of a query as pipe-delimited

Fetch the data in the format of the method's name (if available, or if not simply being informed it is not yet ready).  The following error codes are to be anticipated most with standard Problem Detail reports: - 400 BadRequest : Something failed with the execution of your query - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't (yet) exist or the calling user did not run the query. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlBackgroundExecutionApi
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
    api_instance = api_client_factory.build(SqlBackgroundExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query
    download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
    sort_by = 'sort_by_example' # str | Order the results by these fields.             Use the `-` sign to denote descending order, e.g. `-MyFieldName`.  Numeric indexes may be used also, e.g. `2,-3`.             Multiple fields can be denoted by a comma e.g. `-MyFieldName,AnotherFieldName,-AFurtherFieldName`.             Default is null, the sort order specified in the query itself. (optional)
    filter = 'filter_example' # str | An ODATA filter per Finbourne.Filtering syntax. (optional)
    select = 'select_example' # str | Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - `MyField` - `Max(x) FILTER (WHERE y > 12) as ABC` (max of a field, if another field lets it qualify, with a nice column name) - `count(*)` (count the rows for the given group, that would produce a rather ugly column name, but  it works) - `count(distinct x) as numOfXs` If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - `some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name`   where you would likely want to pass `1` as the `groupBy` also. (optional)
    group_by = 'group_by_example' # str | Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. `2,3`, `myColumn`.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \"select\" parameter fields.             Only specify this if you are selecting aggregations in the \"select\" parameter. (optional)
    limit = 0 # int | When paginating, only return this number of records, page should also be specified. (optional) (default to 0)
    page = 0 # int | 0-N based on chunk sized determined by the limit, ignored if limit < 1. (optional) (default to 0)
    date_time_format = 'date_time_format_example' # str | Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently `yyyy-MM-dd HH:mm:ss.fff` (optional)
    load_wait_milliseconds = 0 # int | Optional maximum additional wait period for post execution platform processing. (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.fetch_query_result_pipe(execution_id, download=download, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds, opts=opts)

        # FetchQueryResultPipe: Fetch the result of a query as pipe-delimited
        api_response = api_instance.fetch_query_result_pipe(execution_id, download=download, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlBackgroundExecutionApi->fetch_query_result_pipe: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **sort_by** | **str**| Order the results by these fields.             Use the &#x60;-&#x60; sign to denote descending order, e.g. &#x60;-MyFieldName&#x60;.  Numeric indexes may be used also, e.g. &#x60;2,-3&#x60;.             Multiple fields can be denoted by a comma e.g. &#x60;-MyFieldName,AnotherFieldName,-AFurtherFieldName&#x60;.             Default is null, the sort order specified in the query itself. | [optional] 
 **filter** | **str**| An ODATA filter per Finbourne.Filtering syntax. | [optional] 
 **select** | **str**| Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - &#x60;MyField&#x60; - &#x60;Max(x) FILTER (WHERE y &gt; 12) as ABC&#x60; (max of a field, if another field lets it qualify, with a nice column name) - &#x60;count(*)&#x60; (count the rows for the given group, that would produce a rather ugly column name, but  it works) - &#x60;count(distinct x) as numOfXs&#x60; If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - &#x60;some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name&#x60;   where you would likely want to pass &#x60;1&#x60; as the &#x60;groupBy&#x60; also. | [optional] 
 **group_by** | **str**| Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. &#x60;2,3&#x60;, &#x60;myColumn&#x60;.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \&quot;select\&quot; parameter fields.             Only specify this if you are selecting aggregations in the \&quot;select\&quot; parameter. | [optional] 
 **limit** | **int**| When paginating, only return this number of records, page should also be specified. | [optional] [default to 0]
 **page** | **int**| 0-N based on chunk sized determined by the limit, ignored if limit &lt; 1. | [optional] [default to 0]
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

# **fetch_query_result_sqlite**
> bytearray fetch_query_result_sqlite(execution_id, sort_by=sort_by, filter=filter, select=select, group_by=group_by, load_wait_milliseconds=load_wait_milliseconds)

FetchQueryResultSqlite: Fetch the result of a query as SqLite

Fetch the data in the format of the method's name (if available, or if not simply being informed it is not yet ready).  The following error codes are to be anticipated most with standard Problem Detail reports: - 400 BadRequest : Something failed with the execution of your query - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't (yet) exist or the calling user did not run the query. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlBackgroundExecutionApi
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
    api_instance = api_client_factory.build(SqlBackgroundExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query
    sort_by = 'sort_by_example' # str | Order the results by these fields.             Use the `-` sign to denote descending order, e.g. `-MyFieldName`.  Numeric indexes may be used also, e.g. `2,-3`.             Multiple fields can be denoted by a comma e.g. `-MyFieldName,AnotherFieldName,-AFurtherFieldName`.             Default is null, the sort order specified in the query itself. (optional)
    filter = 'filter_example' # str | An ODATA filter per Finbourne.Filtering syntax. (optional)
    select = 'select_example' # str | Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - `MyField` - `Max(x) FILTER (WHERE y > 12) as ABC` (max of a field, if another field lets it qualify, with a nice column name) - `count(*)` (count the rows for the given group, that would produce a rather ugly column name, but  it works) - `count(distinct x) as numOfXs` If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - `some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name`   where you would likely want to pass `1` as the `groupBy` also. (optional)
    group_by = 'group_by_example' # str | Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. `2,3`, `myColumn`.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \"select\" parameter fields.             Only specify this if you are selecting aggregations in the \"select\" parameter. (optional)
    load_wait_milliseconds = 0 # int | Optional maximum additional wait period for post execution platform processing. (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.fetch_query_result_sqlite(execution_id, sort_by=sort_by, filter=filter, select=select, group_by=group_by, load_wait_milliseconds=load_wait_milliseconds, opts=opts)

        # FetchQueryResultSqlite: Fetch the result of a query as SqLite
        api_response = api_instance.fetch_query_result_sqlite(execution_id, sort_by=sort_by, filter=filter, select=select, group_by=group_by, load_wait_milliseconds=load_wait_milliseconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlBackgroundExecutionApi->fetch_query_result_sqlite: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 
 **sort_by** | **str**| Order the results by these fields.             Use the &#x60;-&#x60; sign to denote descending order, e.g. &#x60;-MyFieldName&#x60;.  Numeric indexes may be used also, e.g. &#x60;2,-3&#x60;.             Multiple fields can be denoted by a comma e.g. &#x60;-MyFieldName,AnotherFieldName,-AFurtherFieldName&#x60;.             Default is null, the sort order specified in the query itself. | [optional] 
 **filter** | **str**| An ODATA filter per Finbourne.Filtering syntax. | [optional] 
 **select** | **str**| Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - &#x60;MyField&#x60; - &#x60;Max(x) FILTER (WHERE y &gt; 12) as ABC&#x60; (max of a field, if another field lets it qualify, with a nice column name) - &#x60;count(*)&#x60; (count the rows for the given group, that would produce a rather ugly column name, but  it works) - &#x60;count(distinct x) as numOfXs&#x60; If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - &#x60;some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name&#x60;   where you would likely want to pass &#x60;1&#x60; as the &#x60;groupBy&#x60; also. | [optional] 
 **group_by** | **str**| Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. &#x60;2,3&#x60;, &#x60;myColumn&#x60;.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \&quot;select\&quot; parameter fields.             Only specify this if you are selecting aggregations in the \&quot;select\&quot; parameter. | [optional] 
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

# **fetch_query_result_xml**
> str fetch_query_result_xml(execution_id, download=download, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, load_wait_milliseconds=load_wait_milliseconds)

FetchQueryResultXml: Fetch the result of a query as XML

Fetch the data in the format of the method's name (if available, or if not simply being informed it is not yet ready).  The following error codes are to be anticipated most with standard Problem Detail reports: - 400 BadRequest : Something failed with the execution of your query - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't (yet) exist or the calling user did not run the query. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlBackgroundExecutionApi
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
    api_instance = api_client_factory.build(SqlBackgroundExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query
    download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
    sort_by = 'sort_by_example' # str | Order the results by these fields.             Use the `-` sign to denote descending order, e.g. `-MyFieldName`.  Numeric indexes may be used also, e.g. `2,-3`.             Multiple fields can be denoted by a comma e.g. `-MyFieldName,AnotherFieldName,-AFurtherFieldName`.             Default is null, the sort order specified in the query itself. (optional)
    filter = 'filter_example' # str | An ODATA filter per Finbourne.Filtering syntax. (optional)
    select = 'select_example' # str | Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - `MyField` - `Max(x) FILTER (WHERE y > 12) as ABC` (max of a field, if another field lets it qualify, with a nice column name) - `count(*)` (count the rows for the given group, that would produce a rather ugly column name, but  it works) - `count(distinct x) as numOfXs` If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - `some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name`   where you would likely want to pass `1` as the `groupBy` also. (optional)
    group_by = 'group_by_example' # str | Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. `2,3`, `myColumn`.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \"select\" parameter fields.             Only specify this if you are selecting aggregations in the \"select\" parameter. (optional)
    limit = 0 # int | When paginating, only return this number of records, page should also be specified. (optional) (default to 0)
    page = 0 # int | 0-N based on chunk sized determined by the limit, ignored if limit < 1. (optional) (default to 0)
    load_wait_milliseconds = 0 # int | Optional maximum additional wait period for post execution platform processing. (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.fetch_query_result_xml(execution_id, download=download, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, load_wait_milliseconds=load_wait_milliseconds, opts=opts)

        # FetchQueryResultXml: Fetch the result of a query as XML
        api_response = api_instance.fetch_query_result_xml(execution_id, download=download, sort_by=sort_by, filter=filter, select=select, group_by=group_by, limit=limit, page=page, load_wait_milliseconds=load_wait_milliseconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlBackgroundExecutionApi->fetch_query_result_xml: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **sort_by** | **str**| Order the results by these fields.             Use the &#x60;-&#x60; sign to denote descending order, e.g. &#x60;-MyFieldName&#x60;.  Numeric indexes may be used also, e.g. &#x60;2,-3&#x60;.             Multiple fields can be denoted by a comma e.g. &#x60;-MyFieldName,AnotherFieldName,-AFurtherFieldName&#x60;.             Default is null, the sort order specified in the query itself. | [optional] 
 **filter** | **str**| An ODATA filter per Finbourne.Filtering syntax. | [optional] 
 **select** | **str**| Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited. The power of this comes in that you may aggregate the data if you wish (that is the main reason for allowing this, in fact). e.g.: - &#x60;MyField&#x60; - &#x60;Max(x) FILTER (WHERE y &gt; 12) as ABC&#x60; (max of a field, if another field lets it qualify, with a nice column name) - &#x60;count(*)&#x60; (count the rows for the given group, that would produce a rather ugly column name, but  it works) - &#x60;count(distinct x) as numOfXs&#x60; If there was an illegal character in a field you are selecting from, you are responsible for bracketing it with [ ].  e.g. - &#x60;some_field, count(*) as a, max(x) as b, min([column with space in name]) as nice_name&#x60;   where you would likely want to pass &#x60;1&#x60; as the &#x60;groupBy&#x60; also. | [optional] 
 **group_by** | **str**| Groups by the specified fields.             A comma delimited list of: 1 based numeric indexes (cleaner), or repeats of the select expressions (a bit verbose and must match exactly).             e.g. &#x60;2,3&#x60;, &#x60;myColumn&#x60;.             Default is null (meaning no grouping will be performed on the selected columns).             This applies only over the result set being requested here, meaning indexes into the \&quot;select\&quot; parameter fields.             Only specify this if you are selecting aggregations in the \&quot;select\&quot; parameter. | [optional] 
 **limit** | **int**| When paginating, only return this number of records, page should also be specified. | [optional] [default to 0]
 **page** | **int**| 0-N based on chunk sized determined by the limit, ignored if limit &lt; 1. | [optional] [default to 0]
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

# **get_historical_feedback**
> BackgroundQueryProgressResponse get_historical_feedback(execution_id)

GetHistoricalFeedback: View query progress up to this point

View full progress information, including historical feedback for queries which have passed their `keepForSeconds` time, so long as they were executed in the last 31 days. Unlike most methods here this may be called by a user that did not run the original query, as this is pure telemetry information.  The following error codes are to be anticipated most with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't exist and is not running. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlBackgroundExecutionApi
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
    api_instance = api_client_factory.build(SqlBackgroundExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_historical_feedback(execution_id, opts=opts)

        # GetHistoricalFeedback: View query progress up to this point
        api_response = api_instance.get_historical_feedback(execution_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlBackgroundExecutionApi->get_historical_feedback: %s\n" % e)

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
**200** | OK |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_progress_of**
> BackgroundQueryProgressResponse get_progress_of(execution_id, build_from_logs=build_from_logs)

GetProgressOf: View query progress up to this point.

View progress information (up until this point and starting from the last point requested) The following error codes are to be anticipated most with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't exist and is not running or the calling user did not run the query. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlBackgroundExecutionApi
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
    api_instance = api_client_factory.build(SqlBackgroundExecutionApi)
    execution_id = 'execution_id_example' # str | ExecutionId returned when starting the query
    build_from_logs = False # bool | Should the response state be build from query logs if missing from the shared-db-state?  Deprecated. Regardless of the value here it is now the case that:  False [and now even True] will mean `404 Not Found` in cases where it was a real query but has passed its `keepForSeconds` since the query completed (as well as 'this was not a query at all' of course) (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_progress_of(execution_id, build_from_logs=build_from_logs, opts=opts)

        # GetProgressOf: View query progress up to this point.
        api_response = api_instance.get_progress_of(execution_id, build_from_logs=build_from_logs)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlBackgroundExecutionApi->get_progress_of: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | 
 **build_from_logs** | **bool**| Should the response state be build from query logs if missing from the shared-db-state?  Deprecated. Regardless of the value here it is now the case that:  False [and now even True] will mean &#x60;404 Not Found&#x60; in cases where it was a real query but has passed its &#x60;keepForSeconds&#x60; since the query completed (as well as &#39;this was not a query at all&#39; of course) | [optional] [default to False]

### Return type

[**BackgroundQueryProgressResponse**](BackgroundQueryProgressResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **start_query**
> BackgroundQueryResponse start_query(body, execution_id=execution_id, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds, keep_for_seconds=keep_for_seconds)

StartQuery: Start to Execute Sql in the background

 Allow for starting a potentially long running query and getting back an immediate response with how to  - fetch the data in various formats (if available, or if not simply being informed it is not yet ready) - view progress information (up until this point) - cancel the query (if still running) / clear the data (if already returned)  This can still error on things like an outright syntax error, but more runtime errors (e.g. from providers) will not cause this to error (that will happen when attempting to fetch data)  Here is an example that intentionally takes one minute to run:  ```sql select Str, Takes500Ms from Testing1K where UseLinq = true and [Int] <= 120 ```  This is the only place in the Luminesce WebAPI where the following is supported. This will allow for the same user running a character-identical query not kick off a new query but simply be returned a reference  to the already running one for up to `N` seconds (where `N` should be `<=` `keepForSeconds`).  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - there was something wrong with your query syntax (the issue was detected at parse-time) - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlBackgroundExecutionApi
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
    api_instance = api_client_factory.build(SqlBackgroundExecutionApi)
    body = select Str, Takes500Ms from Testing1K where UseLinq = true and [Int] <= 120 # str | The LuminesceSql query to kick off.
    execution_id = '686a0b70-0e97-4187-a2ab-509cf6d1091b' # str | An explicit ExecutionId to use.  This must be blank OR assigned to a valid GUID-as-a-string. It might be ignored / replaced, for example if using the query cache and a cached query is found. (optional)
    scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
    query_name = 'Intentionally slow test query' # str | A name for this query.  This goes into logs and is available in `Sys.Logs.HcQueryStart`. (optional)
    timeout_seconds = 0 # int | Maximum time the query may run for, in seconds: <0 → ∞, 0 → 7200 (2h) (optional) (default to 0)
    keep_for_seconds = 0 # int | Maximum time the result may be kept for, in seconds: <0 → 1200 (20m), 0 → 28800 (8h), max = 2,678,400 (31d) (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.start_query(body, execution_id=execution_id, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds, keep_for_seconds=keep_for_seconds, opts=opts)

        # StartQuery: Start to Execute Sql in the background
        api_response = api_instance.start_query(body, execution_id=execution_id, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds, keep_for_seconds=keep_for_seconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlBackgroundExecutionApi->start_query: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| The LuminesceSql query to kick off. | 
 **execution_id** | **str**| An explicit ExecutionId to use.  This must be blank OR assigned to a valid GUID-as-a-string. It might be ignored / replaced, for example if using the query cache and a cached query is found. | [optional] 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| A name for this query.  This goes into logs and is available in &#x60;Sys.Logs.HcQueryStart&#x60;. | [optional] 
 **timeout_seconds** | **int**| Maximum time the query may run for, in seconds: &lt;0 → ∞, 0 → 7200 (2h) | [optional] [default to 0]
 **keep_for_seconds** | **int**| Maximum time the result may be kept for, in seconds: &lt;0 → 1200 (20m), 0 → 28800 (8h), max &#x3D; 2,678,400 (31d) | [optional] [default to 0]

### Return type

[**BackgroundQueryResponse**](BackgroundQueryResponse.md)

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

