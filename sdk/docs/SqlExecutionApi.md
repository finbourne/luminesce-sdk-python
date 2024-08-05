# luminesce.SqlExecutionApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_by_query_csv**](SqlExecutionApi.md#get_by_query_csv) | **GET** /api/Sql/csv/{query} | GetByQueryCsv: Executes Sql, returned in CSV format, where the sql is simply in the url.
[**get_by_query_excel**](SqlExecutionApi.md#get_by_query_excel) | **GET** /api/Sql/excel/{query} | GetByQueryExcel: Executes Sql, returned in Excel (xlsx) format (as a file to be downloaded) format, where the sql is simply in the url.
[**get_by_query_json**](SqlExecutionApi.md#get_by_query_json) | **GET** /api/Sql/json/{query} | GetByQueryJson: Executes Sql, returned in JSON format, where the sql is simply in the url.
[**get_by_query_parquet**](SqlExecutionApi.md#get_by_query_parquet) | **GET** /api/Sql/parquet/{query} | GetByQueryParquet: Executes Sql, returned in Parquet (.parquet) format (as a file to be downloaded) format, where the sql is simply in the url.
[**get_by_query_pipe**](SqlExecutionApi.md#get_by_query_pipe) | **GET** /api/Sql/pipe/{query} | GetByQueryPipe: Executes Sql, returned in pipe-delimited format, where the sql is simply in the url.
[**get_by_query_sqlite**](SqlExecutionApi.md#get_by_query_sqlite) | **GET** /api/Sql/sqlite/{query} | GetByQuerySqlite: Executes Sql, returned in SqLite DB (sqlite3) format (as a file to be downloaded) format, where the sql is simply in the url.
[**get_by_query_xml**](SqlExecutionApi.md#get_by_query_xml) | **GET** /api/Sql/xml/{query} | GetByQueryXml: Executes Sql, returned in Xml format, where the sql is simply in the url.
[**put_by_query_csv**](SqlExecutionApi.md#put_by_query_csv) | **PUT** /api/Sql/csv | PutByQueryCsv: Executes Sql, returned in CSV format, where the sql is the post-body url.
[**put_by_query_excel**](SqlExecutionApi.md#put_by_query_excel) | **PUT** /api/Sql/excel | PutByQueryExcel: Executes Sql, returned in Excel (xlsx) format (as a file to be downloaded), where the sql is the post-body url.
[**put_by_query_json**](SqlExecutionApi.md#put_by_query_json) | **PUT** /api/Sql/json | PutByQueryJson: Executes Sql, returned in JSON format, where the sql is the post-body url.
[**put_by_query_parquet**](SqlExecutionApi.md#put_by_query_parquet) | **PUT** /api/Sql/parquet | PutByQueryParquet: Executes Sql, returned in Parquet format, where the sql is the post-body url.
[**put_by_query_pipe**](SqlExecutionApi.md#put_by_query_pipe) | **PUT** /api/Sql/pipe | PutByQueryPipe: Executes Sql, returned in pipe-delimited format, where the sql is the post-body url.
[**put_by_query_sqlite**](SqlExecutionApi.md#put_by_query_sqlite) | **PUT** /api/Sql/sqlite | PutByQuerySqlite: Executes Sql, returned in SqLite DB (sqlite3) format (as a file to be downloaded), where the sql is the post-body url.
[**put_by_query_xml**](SqlExecutionApi.md#put_by_query_xml) | **PUT** /api/Sql/xml | PutByQueryXml: Executes Sql, returned in Xml format, where the sql is the post-body url.


# **get_by_query_csv**
> str get_by_query_csv(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout, delimiter=delimiter, escape=escape)

GetByQueryCsv: Executes Sql, returned in CSV format, where the sql is simply in the url.

 For simple single-line query execution via the url. e.g. `select ^ from Sys.Field order by 1, 2`  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlExecutionApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
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
            # GetByQueryCsv: Executes Sql, returned in CSV format, where the sql is simply in the url.
            api_response = await api_instance.get_by_query_csv(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout, delimiter=delimiter, escape=escape)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlExecutionApi->get_by_query_csv: %s\n" % e)

asyncio.run(main())
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_by_query_excel**
> bytearray get_by_query_excel(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)

GetByQueryExcel: Executes Sql, returned in Excel (xlsx) format (as a file to be downloaded) format, where the sql is simply in the url.

 For simple single-line query execution via the url. e.g. `select ^ from Sys.Field order by 1, 2`  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlExecutionApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SqlExecutionApi)
        query = 'select ^ from Sys.Field order by 1, 2' # str | LuminesceSql to Execute (must be one line only)
        scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
        query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
        timeout = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

        try:
            # GetByQueryExcel: Executes Sql, returned in Excel (xlsx) format (as a file to be downloaded) format, where the sql is simply in the url.
            api_response = await api_instance.get_by_query_excel(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlExecutionApi->get_by_query_excel: %s\n" % e)

asyncio.run(main())
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_by_query_json**
> str get_by_query_json(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout, json_proper=json_proper)

GetByQueryJson: Executes Sql, returned in JSON format, where the sql is simply in the url.

 For simple single-line query execution via the url. e.g. `select ^ from Sys.Field order by 1, 2`  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlExecutionApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SqlExecutionApi)
        query = 'select ^ from Sys.Field order by 1, 2' # str | LuminesceSql to Execute (must be one line only)
        scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
        query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
        timeout = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)
        json_proper = False # bool | Should this be text/json (not json-encoded-as-a-string) (optional) (default to False)

        try:
            # GetByQueryJson: Executes Sql, returned in JSON format, where the sql is simply in the url.
            api_response = await api_instance.get_by_query_json(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout, json_proper=json_proper)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlExecutionApi->get_by_query_json: %s\n" % e)

asyncio.run(main())
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_by_query_parquet**
> bytearray get_by_query_parquet(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)

GetByQueryParquet: Executes Sql, returned in Parquet (.parquet) format (as a file to be downloaded) format, where the sql is simply in the url.

 For simple single-line query execution via the url. e.g. `select ^ from Sys.Field order by 1, 2`  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlExecutionApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SqlExecutionApi)
        query = 'select ^ from Sys.Field order by 1, 2' # str | LuminesceSql to Execute (must be one line only)
        scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
        query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
        timeout = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

        try:
            # GetByQueryParquet: Executes Sql, returned in Parquet (.parquet) format (as a file to be downloaded) format, where the sql is simply in the url.
            api_response = await api_instance.get_by_query_parquet(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlExecutionApi->get_by_query_parquet: %s\n" % e)

asyncio.run(main())
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_by_query_pipe**
> str get_by_query_pipe(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout)

GetByQueryPipe: Executes Sql, returned in pipe-delimited format, where the sql is simply in the url.

 For simple single-line query execution via the url. e.g. `select ^ from Sys.Field order by 1, 2`  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlExecutionApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SqlExecutionApi)
        query = 'select ^ from Sys.Field order by 1, 2' # str | LuminesceSql to Execute (must be one line only)
        scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
        query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
        download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
        timeout = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

        try:
            # GetByQueryPipe: Executes Sql, returned in pipe-delimited format, where the sql is simply in the url.
            api_response = await api_instance.get_by_query_pipe(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlExecutionApi->get_by_query_pipe: %s\n" % e)

asyncio.run(main())
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_by_query_sqlite**
> bytearray get_by_query_sqlite(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)

GetByQuerySqlite: Executes Sql, returned in SqLite DB (sqlite3) format (as a file to be downloaded) format, where the sql is simply in the url.

 For simple single-line query execution via the url. e.g. `select ^ from Sys.Field order by 1, 2`  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlExecutionApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SqlExecutionApi)
        query = 'select ^ from Sys.Field order by 1, 2' # str | LuminesceSql to Execute (must be one line only)
        scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
        query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
        timeout = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

        try:
            # GetByQuerySqlite: Executes Sql, returned in SqLite DB (sqlite3) format (as a file to be downloaded) format, where the sql is simply in the url.
            api_response = await api_instance.get_by_query_sqlite(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlExecutionApi->get_by_query_sqlite: %s\n" % e)

asyncio.run(main())
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_by_query_xml**
> str get_by_query_xml(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout)

GetByQueryXml: Executes Sql, returned in Xml format, where the sql is simply in the url.

 For simple single-line query execution via the url. e.g. `select ^ from Sys.Field order by 1, 2`  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlExecutionApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SqlExecutionApi)
        query = 'select ^ from Sys.Field order by 1, 2' # str | LuminesceSql to Execute (must be one line only)
        scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
        query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
        download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
        timeout = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

        try:
            # GetByQueryXml: Executes Sql, returned in Xml format, where the sql is simply in the url.
            api_response = await api_instance.get_by_query_xml(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlExecutionApi->get_by_query_xml: %s\n" % e)

asyncio.run(main())
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_by_query_csv**
> str put_by_query_csv(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds, delimiter=delimiter, escape=escape)

PutByQueryCsv: Executes Sql, returned in CSV format, where the sql is the post-body url.

 For more complex LuminesceSql a PUT will allow for longer Sql. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlExecutionApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
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
            # PutByQueryCsv: Executes Sql, returned in CSV format, where the sql is the post-body url.
            api_response = await api_instance.put_by_query_csv(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds, delimiter=delimiter, escape=escape)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlExecutionApi->put_by_query_csv: %s\n" % e)

asyncio.run(main())
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_by_query_excel**
> bytearray put_by_query_excel(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)

PutByQueryExcel: Executes Sql, returned in Excel (xlsx) format (as a file to be downloaded), where the sql is the post-body url.

 For more complex LuminesceSql a PUT will allow for longer Sql. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlExecutionApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SqlExecutionApi)
        body = select * from sys.field # str | LuminesceSql to Execute (may be multi-line)
        scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
        query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
        timeout_seconds = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

        try:
            # PutByQueryExcel: Executes Sql, returned in Excel (xlsx) format (as a file to be downloaded), where the sql is the post-body url.
            api_response = await api_instance.put_by_query_excel(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlExecutionApi->put_by_query_excel: %s\n" % e)

asyncio.run(main())
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_by_query_json**
> str put_by_query_json(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds, json_proper=json_proper)

PutByQueryJson: Executes Sql, returned in JSON format, where the sql is the post-body url.

 For more complex LuminesceSql a PUT will allow for longer Sql. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlExecutionApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SqlExecutionApi)
        body = select * from sys.field # str | LuminesceSql to Execute (may be multi-line)
        scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
        query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
        timeout_seconds = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)
        json_proper = False # bool | Should this be text/json (not json-encoded-as-a-string) (optional) (default to False)

        try:
            # PutByQueryJson: Executes Sql, returned in JSON format, where the sql is the post-body url.
            api_response = await api_instance.put_by_query_json(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds, json_proper=json_proper)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlExecutionApi->put_by_query_json: %s\n" % e)

asyncio.run(main())
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_by_query_parquet**
> bytearray put_by_query_parquet(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)

PutByQueryParquet: Executes Sql, returned in Parquet format, where the sql is the post-body url.

 For more complex LuminesceSql a PUT will allow for longer Sql. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlExecutionApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SqlExecutionApi)
        body = select * from sys.field # str | LuminesceSql to Execute (may be multi-line)
        scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
        query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
        timeout_seconds = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

        try:
            # PutByQueryParquet: Executes Sql, returned in Parquet format, where the sql is the post-body url.
            api_response = await api_instance.put_by_query_parquet(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlExecutionApi->put_by_query_parquet: %s\n" % e)

asyncio.run(main())
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_by_query_pipe**
> str put_by_query_pipe(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds)

PutByQueryPipe: Executes Sql, returned in pipe-delimited format, where the sql is the post-body url.

 For more complex LuminesceSql a PUT will allow for longer Sql. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlExecutionApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SqlExecutionApi)
        body = select * from sys.field # str | LuminesceSql to Execute (may be multi-line)
        scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
        query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
        download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
        timeout_seconds = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

        try:
            # PutByQueryPipe: Executes Sql, returned in pipe-delimited format, where the sql is the post-body url.
            api_response = await api_instance.put_by_query_pipe(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlExecutionApi->put_by_query_pipe: %s\n" % e)

asyncio.run(main())
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_by_query_sqlite**
> bytearray put_by_query_sqlite(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)

PutByQuerySqlite: Executes Sql, returned in SqLite DB (sqlite3) format (as a file to be downloaded), where the sql is the post-body url.

 For more complex LuminesceSql a PUT will allow for longer Sql. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlExecutionApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SqlExecutionApi)
        body = select * from sys.field # str | LuminesceSql to Execute (may be multi-line)
        scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
        query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
        timeout_seconds = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

        try:
            # PutByQuerySqlite: Executes Sql, returned in SqLite DB (sqlite3) format (as a file to be downloaded), where the sql is the post-body url.
            api_response = await api_instance.put_by_query_sqlite(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlExecutionApi->put_by_query_sqlite: %s\n" % e)

asyncio.run(main())
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_by_query_xml**
> str put_by_query_xml(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds)

PutByQueryXml: Executes Sql, returned in Xml format, where the sql is the post-body url.

 For more complex LuminesceSql a PUT will allow for longer Sql. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlExecutionApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(SqlExecutionApi)
        body = select * from sys.field # str | LuminesceSql to Execute (may be multi-line)
        scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] | Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. (optional)
        query_name = 'Get tables/fields' # str | Name to apply to the query in logs and `Sys.Logs.HcQueryStart` (optional)
        download = False # bool | Makes this a file-download request (as opposed to returning the data in the response-body) (optional) (default to False)
        timeout_seconds = 0 # int | In seconds: <0 → ∞, 0 → 120s (optional) (default to 0)

        try:
            # PutByQueryXml: Executes Sql, returned in Xml format, where the sql is the post-body url.
            api_response = await api_instance.put_by_query_xml(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlExecutionApi->put_by_query_xml: %s\n" % e)

asyncio.run(main())
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

