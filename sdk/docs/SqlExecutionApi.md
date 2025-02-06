# luminesce.SqlExecutionApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_by_query_csv**](SqlExecutionApi.md#get_by_query_csv) | **GET** /api/Sql/csv/{query} | GetByQueryCsv: Execute Sql from the url returning CSV
[**get_by_query_excel**](SqlExecutionApi.md#get_by_query_excel) | **GET** /api/Sql/excel/{query} | GetByQueryExcel: Execute Sql from the url returning an Excel file
[**get_by_query_json**](SqlExecutionApi.md#get_by_query_json) | **GET** /api/Sql/json/{query} | GetByQueryJson: Execute Sql from the url returning JSON
[**get_by_query_parquet**](SqlExecutionApi.md#get_by_query_parquet) | **GET** /api/Sql/parquet/{query} | GetByQueryParquet: Execute Sql from the url returning a Parquet file
[**get_by_query_pipe**](SqlExecutionApi.md#get_by_query_pipe) | **GET** /api/Sql/pipe/{query} | GetByQueryPipe: Execute Sql from the url returning pipe-delimited
[**get_by_query_sqlite**](SqlExecutionApi.md#get_by_query_sqlite) | **GET** /api/Sql/sqlite/{query} | GetByQuerySqlite: Execute Sql from the url returning SqLite DB
[**get_by_query_xml**](SqlExecutionApi.md#get_by_query_xml) | **GET** /api/Sql/xml/{query} | GetByQueryXml: Execute Sql from the url returning XML
[**put_by_query_csv**](SqlExecutionApi.md#put_by_query_csv) | **PUT** /api/Sql/csv | PutByQueryCsv: Execute Sql from the body returning CSV
[**put_by_query_excel**](SqlExecutionApi.md#put_by_query_excel) | **PUT** /api/Sql/excel | PutByQueryExcel: Execute Sql from the body making an Excel file
[**put_by_query_json**](SqlExecutionApi.md#put_by_query_json) | **PUT** /api/Sql/json | PutByQueryJson: Execute Sql from the body returning JSON
[**put_by_query_parquet**](SqlExecutionApi.md#put_by_query_parquet) | **PUT** /api/Sql/parquet | PutByQueryParquet: Execute Sql from the body making a Parquet file
[**put_by_query_pipe**](SqlExecutionApi.md#put_by_query_pipe) | **PUT** /api/Sql/pipe | PutByQueryPipe: Execute Sql from the body making pipe-delimited
[**put_by_query_sqlite**](SqlExecutionApi.md#put_by_query_sqlite) | **PUT** /api/Sql/sqlite | PutByQuerySqlite: Execute Sql from the body returning SqLite DB
[**put_by_query_xml**](SqlExecutionApi.md#put_by_query_xml) | **PUT** /api/Sql/xml | PutByQueryXml: Execute Sql from the body returning XML


# **get_by_query_csv**
> str get_by_query_csv(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout, delimiter=delimiter, escape=escape)

GetByQueryCsv: Execute Sql from the url returning CSV

 Returns data from a simple single-line query execution which is specified on the url. e.g. `select ^ from Sys.Field order by 1, 2`, returned in the format of the method name.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlExecutionApi
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
    api_instance = api_client_factory.build(SqlExecutionApi)
    query = 'select ^ from Sys.Field order by 1, 2' # str | LuminesceSql to Execute (must be one line only)
    scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
    query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
    download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
    timeout = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)
    delimiter = 'delimiter_example' # str | Delimiter string to override the default (optional)
    escape = 'escape_example' # str | Escape character to override the default (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_by_query_csv(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout, delimiter=delimiter, escape=escape, opts=opts)

        # GetByQueryCsv: Execute Sql from the url returning CSV
        api_response = api_instance.get_by_query_csv(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout, delimiter=delimiter, escape=escape)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlExecutionApi->get_by_query_csv: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| LuminesceSql to Execute (must be one line only) | 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **timeout** | **int**| In seconds: &lt;0 → ∞, 0 → 120s | [optional] [default to 0]
 **delimiter** | **str**| Delimiter string to override the default | [optional] 
 **escape** | **str**| Escape character to override the default | [optional] 

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

# **get_by_query_excel**
> bytearray get_by_query_excel(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)

GetByQueryExcel: Execute Sql from the url returning an Excel file

 Returns data from a simple single-line query execution which is specified on the url. e.g. `select ^ from Sys.Field order by 1, 2`, returned in the format of the method name.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlExecutionApi
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
    api_instance = api_client_factory.build(SqlExecutionApi)
    query = 'select ^ from Sys.Field order by 1, 2' # str | LuminesceSql to Execute (must be one line only)
    scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
    query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
    timeout = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_by_query_excel(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout, opts=opts)

        # GetByQueryExcel: Execute Sql from the url returning an Excel file
        api_response = api_instance.get_by_query_excel(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlExecutionApi->get_by_query_excel: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| LuminesceSql to Execute (must be one line only) | 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout** | **int**| In seconds: &lt;0 → ∞, 0 → 120s | [optional] [default to 0]

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

# **get_by_query_json**
> str get_by_query_json(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout, json_proper=json_proper)

GetByQueryJson: Execute Sql from the url returning JSON

 Returns data from a simple single-line query execution which is specified on the url. e.g. `select ^ from Sys.Field order by 1, 2`, returned in the format of the method name.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlExecutionApi
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
    api_instance = api_client_factory.build(SqlExecutionApi)
    query = 'select ^ from Sys.Field order by 1, 2' # str | LuminesceSql to Execute (must be one line only)
    scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
    query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
    timeout = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)
    json_proper = False # bool | Should this be text/json (not json-encoded-as-a-string) (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_by_query_json(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout, json_proper=json_proper, opts=opts)

        # GetByQueryJson: Execute Sql from the url returning JSON
        api_response = api_instance.get_by_query_json(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout, json_proper=json_proper)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlExecutionApi->get_by_query_json: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| LuminesceSql to Execute (must be one line only) | 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout** | **int**| In seconds: &lt;0 → ∞, 0 → 120s | [optional] [default to 0]
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

# **get_by_query_parquet**
> bytearray get_by_query_parquet(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)

GetByQueryParquet: Execute Sql from the url returning a Parquet file

 Returns data from a simple single-line query execution which is specified on the url. e.g. `select ^ from Sys.Field order by 1, 2`, returned in the format of the method name.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlExecutionApi
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
    api_instance = api_client_factory.build(SqlExecutionApi)
    query = 'select ^ from Sys.Field order by 1, 2' # str | LuminesceSql to Execute (must be one line only)
    scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
    query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
    timeout = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_by_query_parquet(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout, opts=opts)

        # GetByQueryParquet: Execute Sql from the url returning a Parquet file
        api_response = api_instance.get_by_query_parquet(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlExecutionApi->get_by_query_parquet: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| LuminesceSql to Execute (must be one line only) | 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout** | **int**| In seconds: &lt;0 → ∞, 0 → 120s | [optional] [default to 0]

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

# **get_by_query_pipe**
> str get_by_query_pipe(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout)

GetByQueryPipe: Execute Sql from the url returning pipe-delimited

 Returns data from a simple single-line query execution which is specified on the url. e.g. `select ^ from Sys.Field order by 1, 2`, returned in the format of the method name.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlExecutionApi
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
    api_instance = api_client_factory.build(SqlExecutionApi)
    query = 'select ^ from Sys.Field order by 1, 2' # str | LuminesceSql to Execute (must be one line only)
    scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
    query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
    download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
    timeout = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_by_query_pipe(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout, opts=opts)

        # GetByQueryPipe: Execute Sql from the url returning pipe-delimited
        api_response = api_instance.get_by_query_pipe(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlExecutionApi->get_by_query_pipe: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| LuminesceSql to Execute (must be one line only) | 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **timeout** | **int**| In seconds: &lt;0 → ∞, 0 → 120s | [optional] [default to 0]

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

# **get_by_query_sqlite**
> bytearray get_by_query_sqlite(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)

GetByQuerySqlite: Execute Sql from the url returning SqLite DB

 Returns data from a simple single-line query execution which is specified on the url. e.g. `select ^ from Sys.Field order by 1, 2`, returned in the format of the method name.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlExecutionApi
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
    api_instance = api_client_factory.build(SqlExecutionApi)
    query = 'select ^ from Sys.Field order by 1, 2' # str | LuminesceSql to Execute (must be one line only)
    scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
    query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
    timeout = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_by_query_sqlite(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout, opts=opts)

        # GetByQuerySqlite: Execute Sql from the url returning SqLite DB
        api_response = api_instance.get_by_query_sqlite(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlExecutionApi->get_by_query_sqlite: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| LuminesceSql to Execute (must be one line only) | 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout** | **int**| In seconds: &lt;0 → ∞, 0 → 120s | [optional] [default to 0]

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

# **get_by_query_xml**
> str get_by_query_xml(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout)

GetByQueryXml: Execute Sql from the url returning XML

 Returns data from a simple single-line query execution which is specified on the url. e.g. `select ^ from Sys.Field order by 1, 2`, returned in the format of the method name.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlExecutionApi
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
    api_instance = api_client_factory.build(SqlExecutionApi)
    query = 'select ^ from Sys.Field order by 1, 2' # str | LuminesceSql to Execute (must be one line only)
    scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
    query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
    download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
    timeout = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_by_query_xml(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout, opts=opts)

        # GetByQueryXml: Execute Sql from the url returning XML
        api_response = api_instance.get_by_query_xml(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlExecutionApi->get_by_query_xml: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| LuminesceSql to Execute (must be one line only) | 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **timeout** | **int**| In seconds: &lt;0 → ∞, 0 → 120s | [optional] [default to 0]

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

# **put_by_query_csv**
> str put_by_query_csv(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds, delimiter=delimiter, escape=escape)

PutByQueryCsv: Execute Sql from the body returning CSV

 For more complex LuminesceSql a PUT will allow for longer and line break delimited Sql, whic will be returned in the format of the method name. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlExecutionApi
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
    api_instance = api_client_factory.build(SqlExecutionApi)
    body = select * from sys.field # str | LuminesceSql to Execute (may be multi-line)
    scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
    query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
    download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
    timeout_seconds = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)
    delimiter = 'delimiter_example' # str | Delimiter string to override the default (optional)
    escape = 'escape_example' # str | Escape character to override the default (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.put_by_query_csv(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds, delimiter=delimiter, escape=escape, opts=opts)

        # PutByQueryCsv: Execute Sql from the body returning CSV
        api_response = api_instance.put_by_query_csv(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds, delimiter=delimiter, escape=escape)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlExecutionApi->put_by_query_csv: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| LuminesceSql to Execute (may be multi-line) | 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **timeout_seconds** | **int**| In seconds: &lt;0 → ∞, 0 → 120s | [optional] [default to 0]
 **delimiter** | **str**| Delimiter string to override the default | [optional] 
 **escape** | **str**| Escape character to override the default | [optional] 

### Return type

**str**

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_by_query_excel**
> bytearray put_by_query_excel(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)

PutByQueryExcel: Execute Sql from the body making an Excel file

 For more complex LuminesceSql a PUT will allow for longer and line break delimited Sql, whic will be returned in the format of the method name. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlExecutionApi
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
    api_instance = api_client_factory.build(SqlExecutionApi)
    body = select * from sys.field # str | LuminesceSql to Execute (may be multi-line)
    scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
    query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
    timeout_seconds = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.put_by_query_excel(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds, opts=opts)

        # PutByQueryExcel: Execute Sql from the body making an Excel file
        api_response = api_instance.put_by_query_excel(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlExecutionApi->put_by_query_excel: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| LuminesceSql to Execute (may be multi-line) | 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout_seconds** | **int**| In seconds: &lt;0 → ∞, 0 → 120s | [optional] [default to 0]

### Return type

**bytearray**

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_by_query_json**
> str put_by_query_json(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds, json_proper=json_proper)

PutByQueryJson: Execute Sql from the body returning JSON

 For more complex LuminesceSql a PUT will allow for longer and line break delimited Sql, whic will be returned in the format of the method name. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlExecutionApi
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
    api_instance = api_client_factory.build(SqlExecutionApi)
    body = select * from sys.field # str | LuminesceSql to Execute (may be multi-line)
    scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
    query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
    timeout_seconds = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)
    json_proper = False # bool | Should this be text/json (not json-encoded-as-a-string) (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.put_by_query_json(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds, json_proper=json_proper, opts=opts)

        # PutByQueryJson: Execute Sql from the body returning JSON
        api_response = api_instance.put_by_query_json(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds, json_proper=json_proper)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlExecutionApi->put_by_query_json: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| LuminesceSql to Execute (may be multi-line) | 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout_seconds** | **int**| In seconds: &lt;0 → ∞, 0 → 120s | [optional] [default to 0]
 **json_proper** | **bool**| Should this be text/json (not json-encoded-as-a-string) | [optional] [default to False]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_by_query_parquet**
> bytearray put_by_query_parquet(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)

PutByQueryParquet: Execute Sql from the body making a Parquet file

 For more complex LuminesceSql a PUT will allow for longer and line break delimited Sql, whic will be returned in the format of the method name. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlExecutionApi
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
    api_instance = api_client_factory.build(SqlExecutionApi)
    body = select * from sys.field # str | LuminesceSql to Execute (may be multi-line)
    scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
    query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
    timeout_seconds = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.put_by_query_parquet(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds, opts=opts)

        # PutByQueryParquet: Execute Sql from the body making a Parquet file
        api_response = api_instance.put_by_query_parquet(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlExecutionApi->put_by_query_parquet: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| LuminesceSql to Execute (may be multi-line) | 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout_seconds** | **int**| In seconds: &lt;0 → ∞, 0 → 120s | [optional] [default to 0]

### Return type

**bytearray**

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_by_query_pipe**
> str put_by_query_pipe(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds)

PutByQueryPipe: Execute Sql from the body making pipe-delimited

 For more complex LuminesceSql a PUT will allow for longer and line break delimited Sql, whic will be returned in the format of the method name. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlExecutionApi
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
    api_instance = api_client_factory.build(SqlExecutionApi)
    body = select * from sys.field # str | LuminesceSql to Execute (may be multi-line)
    scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
    query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
    download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
    timeout_seconds = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.put_by_query_pipe(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds, opts=opts)

        # PutByQueryPipe: Execute Sql from the body making pipe-delimited
        api_response = api_instance.put_by_query_pipe(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlExecutionApi->put_by_query_pipe: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| LuminesceSql to Execute (may be multi-line) | 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **timeout_seconds** | **int**| In seconds: &lt;0 → ∞, 0 → 120s | [optional] [default to 0]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_by_query_sqlite**
> bytearray put_by_query_sqlite(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)

PutByQuerySqlite: Execute Sql from the body returning SqLite DB

 For more complex LuminesceSql a PUT will allow for longer and line break delimited Sql, whic will be returned in the format of the method name. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlExecutionApi
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
    api_instance = api_client_factory.build(SqlExecutionApi)
    body = select * from sys.field # str | LuminesceSql to Execute (may be multi-line)
    scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
    query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
    timeout_seconds = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.put_by_query_sqlite(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds, opts=opts)

        # PutByQuerySqlite: Execute Sql from the body returning SqLite DB
        api_response = api_instance.put_by_query_sqlite(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlExecutionApi->put_by_query_sqlite: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| LuminesceSql to Execute (may be multi-line) | 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout_seconds** | **int**| In seconds: &lt;0 → ∞, 0 → 120s | [optional] [default to 0]

### Return type

**bytearray**

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_by_query_xml**
> str put_by_query_xml(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds)

PutByQueryXml: Execute Sql from the body returning XML

 For more complex LuminesceSql a PUT will allow for longer and line break delimited Sql, whic will be returned in the format of the method name. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    SyncApiClientFactory,
    SqlExecutionApi
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
    api_instance = api_client_factory.build(SqlExecutionApi)
    body = select * from sys.field # str | LuminesceSql to Execute (may be multi-line)
    scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
    query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
    download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
    timeout_seconds = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.put_by_query_xml(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds, opts=opts)

        # PutByQueryXml: Execute Sql from the body returning XML
        api_response = api_instance.put_by_query_xml(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SqlExecutionApi->put_by_query_xml: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| LuminesceSql to Execute (may be multi-line) | 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **timeout_seconds** | **int**| In seconds: &lt;0 → ∞, 0 → 120s | [optional] [default to 0]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

