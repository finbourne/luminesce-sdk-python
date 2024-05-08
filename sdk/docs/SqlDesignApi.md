# luminesce.SqlDesignApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**put_file_read_design_to_sql**](SqlDesignApi.md#put_file_read_design_to_sql) | **PUT** /api/Sql/fromfilereaddesign | [EXPERIMENTAL] PutFileReadDesignToSql: Generates file read SQL from a structured query design
[**put_intellisense**](SqlDesignApi.md#put_intellisense) | **PUT** /api/Sql/intellisense | [EXPERIMENTAL] PutIntellisense: Generate a set of possible intellisense prompts given a SQL snip-it (in need not yet be valid) and cursor location
[**put_intellisense_error**](SqlDesignApi.md#put_intellisense_error) | **PUT** /api/Sql/intellisenseError | [EXPERIMENTAL] PutIntellisenseError: Generate a set of error ranges, if any, in the given SQL (expressed as Lines)
[**put_query_design_to_sql**](SqlDesignApi.md#put_query_design_to_sql) | **PUT** /api/Sql/fromdesign | [EXPERIMENTAL] PutQueryDesignToSql: Generates SQL from a structured query design
[**put_query_to_format**](SqlDesignApi.md#put_query_to_format) | **PUT** /api/Sql/pretty | PutQueryToFormat: Formats SQL into a more readable form, a.k.a. Pretty-Print the SQL.
[**put_sql_to_file_read_design**](SqlDesignApi.md#put_sql_to_file_read_design) | **PUT** /api/Sql/tofilereaddesign | [EXPERIMENTAL] PutSqlToFileReadDesign: Generates a SQL-file-read-design object from SQL string, if possible.
[**put_sql_to_query_design**](SqlDesignApi.md#put_sql_to_query_design) | **PUT** /api/Sql/todesign | [EXPERIMENTAL] PutSqlToQueryDesign: Generates a SQL-design object from SQL string, if possible.
[**put_sql_to_view_design**](SqlDesignApi.md#put_sql_to_view_design) | **PUT** /api/Sql/toviewdesign | [EXPERIMENTAL] PutSqlToViewDesign: Generates a structured view creation design from existing view creation SQL.
[**put_sql_to_writer_design**](SqlDesignApi.md#put_sql_to_writer_design) | **PUT** /api/Sql/towriterdesign | [EXPERIMENTAL] PutSqlToWriterDesign: Generates a SQL-writer-design object from SQL string, if possible.
[**put_view_design_to_sql**](SqlDesignApi.md#put_view_design_to_sql) | **PUT** /api/Sql/fromviewdesign | [EXPERIMENTAL] PutViewDesignToSql: Generates view creation sql from a structured view creation design
[**put_writer_design_to_sql**](SqlDesignApi.md#put_writer_design_to_sql) | **PUT** /api/Sql/fromwriterdesign | [EXPERIMENTAL] PutWriterDesignToSql: Generates writer SQL from a valid writer-design structure


# **put_file_read_design_to_sql**
> FileReaderBuilderResponse put_file_read_design_to_sql(file_reader_builder_def, execute_query=execute_query)

[EXPERIMENTAL] PutFileReadDesignToSql: Generates file read SQL from a structured query design

SQL Designer specification to generate SQL from

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from luminesce.models.file_reader_builder_def import FileReaderBuilderDef
from luminesce.models.file_reader_builder_response import FileReaderBuilderResponse
from pprint import pprint

import os
from luminesce import (
    ApiClientFactory,
    SqlDesignApi,
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
    api_instance = api_client_factory.build(luminesce.SqlDesignApi)
    file_reader_builder_def = {"limit":0,"source":{"location":"Drive","type":"Csv"},"filePath":"/some/folder","folderFilter":".*\\.csv","addFileName":true} # FileReaderBuilderDef | Structured file read design object to generate SQL from
    execute_query = True # bool | Should the generated query be executed to build preview data or determine errors.> (optional) (default to True)

    try:
        # [EXPERIMENTAL] PutFileReadDesignToSql: Generates file read SQL from a structured query design
        api_response = await api_instance.put_file_read_design_to_sql(file_reader_builder_def, execute_query=execute_query)
        print("The response of SqlDesignApi->put_file_read_design_to_sql:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlDesignApi->put_file_read_design_to_sql: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_reader_builder_def** | [**FileReaderBuilderDef**](FileReaderBuilderDef.md)| Structured file read design object to generate SQL from | 
 **execute_query** | **bool**| Should the generated query be executed to build preview data or determine errors.&gt; | [optional] [default to True]

### Return type

[**FileReaderBuilderResponse**](FileReaderBuilderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_intellisense**
> IntellisenseResponse put_intellisense(intellisense_request)

[EXPERIMENTAL] PutIntellisense: Generate a set of possible intellisense prompts given a SQL snip-it (in need not yet be valid) and cursor location

SQL and a row/colum position within it from which to determine intellisense options for the user to potentially choose from.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from luminesce.models.intellisense_request import IntellisenseRequest
from luminesce.models.intellisense_response import IntellisenseResponse
from pprint import pprint

import os
from luminesce import (
    ApiClientFactory,
    SqlDesignApi,
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
    api_instance = api_client_factory.build(luminesce.SqlDesignApi)
    intellisense_request = {"lines":["select *","from somewhere"],"position":{"row":0,"column":4}} # IntellisenseRequest | 

    try:
        # [EXPERIMENTAL] PutIntellisense: Generate a set of possible intellisense prompts given a SQL snip-it (in need not yet be valid) and cursor location
        api_response = await api_instance.put_intellisense(intellisense_request)
        print("The response of SqlDesignApi->put_intellisense:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlDesignApi->put_intellisense: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intellisense_request** | [**IntellisenseRequest**](IntellisenseRequest.md)|  | 

### Return type

[**IntellisenseResponse**](IntellisenseResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_intellisense_error**
> ErrorHighlightResponse put_intellisense_error(error_highlight_request)

[EXPERIMENTAL] PutIntellisenseError: Generate a set of error ranges, if any, in the given SQL (expressed as Lines)

SQL (by line) to syntax check and return error ranges from within, if any.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from luminesce.models.error_highlight_request import ErrorHighlightRequest
from luminesce.models.error_highlight_response import ErrorHighlightResponse
from pprint import pprint

import os
from luminesce import (
    ApiClientFactory,
    SqlDesignApi,
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
    api_instance = api_client_factory.build(luminesce.SqlDesignApi)
    error_highlight_request = {"lines":["select mx(x) x from y"],"ensureSomeTextIsSelected":false} # ErrorHighlightRequest | 

    try:
        # [EXPERIMENTAL] PutIntellisenseError: Generate a set of error ranges, if any, in the given SQL (expressed as Lines)
        api_response = await api_instance.put_intellisense_error(error_highlight_request)
        print("The response of SqlDesignApi->put_intellisense_error:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlDesignApi->put_intellisense_error: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_highlight_request** | [**ErrorHighlightRequest**](ErrorHighlightRequest.md)|  | 

### Return type

[**ErrorHighlightResponse**](ErrorHighlightResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_query_design_to_sql**
> str put_query_design_to_sql(query_design)

[EXPERIMENTAL] PutQueryDesignToSql: Generates SQL from a structured query design

SQL Designer specification to generate SQL from

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from luminesce.models.query_design import QueryDesign
from pprint import pprint

import os
from luminesce import (
    ApiClientFactory,
    SqlDesignApi,
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
    api_instance = api_client_factory.build(luminesce.SqlDesignApi)
    query_design = {"tableName":"Sys.Field","fields":[{"name":"TableName","dataType":"Text","shouldSelect":true,"filters":[{"operator":"Eq","value":"Sys.Registration"}],"aggregations":[]},{"name":"FieldName","dataType":"Text","shouldSelect":true,"filters":[],"aggregations":[{"type":"count_distinct","alias":"NumberOfFields"}]}],"orderBy":[{"field":"DataType","direction":"asc"}],"limit":42,"warnings":[],"availableFields":[]} # QueryDesign | Structured Query design object to generate SQL from

    try:
        # [EXPERIMENTAL] PutQueryDesignToSql: Generates SQL from a structured query design
        api_response = await api_instance.put_query_design_to_sql(query_design)
        print("The response of SqlDesignApi->put_query_design_to_sql:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlDesignApi->put_query_design_to_sql: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_design** | [**QueryDesign**](QueryDesign.md)| Structured Query design object to generate SQL from | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_query_to_format**
> str put_query_to_format(body, trailing_commas=trailing_commas, uppercase_keywords=uppercase_keywords, break_join_on_sections=break_join_on_sections, space_after_expanded_comma=space_after_expanded_comma, keyword_standardization=keyword_standardization, expand_comma_lists=expand_comma_lists, expand_in_lists=expand_in_lists, expand_boolean_expressions=expand_boolean_expressions, expand_between_conditions=expand_between_conditions, expand_case_statements=expand_case_statements, max_line_width=max_line_width, space_before_trailing_single_line_comments=space_before_trailing_single_line_comments, multiline_comment_extra_line_break=multiline_comment_extra_line_break)

PutQueryToFormat: Formats SQL into a more readable form, a.k.a. Pretty-Print the SQL.

 This formats SQL (given a set of options as to how to do so). It takes some SQL (or a fragment thereof, it need not fully parse as yet and certainly need not execute correctly) and returns the reformatted version. e.g. ```sql select x,y,z from a inner join b on a.x=b.x where x>y or y!=z ``` becomes ```sql select x, y, z from a inner join b    on a.x = b.x where x > y    or y != z ``` 

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
    SqlDesignApi,
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
    api_instance = api_client_factory.build(luminesce.SqlDesignApi)
    body = select * from sys.field # str | LuminesceSql to Pretty-Print. Even if it doesn't parse an attempt will be made to format it
    trailing_commas = True # bool | Should commas be after an expression (as opposed to before) (optional) (default to True)
    uppercase_keywords = False # bool | Should key words be capitalized (optional) (default to False)
    break_join_on_sections = True # bool | Should clauses on joins be given line breaks? (optional) (default to True)
    space_after_expanded_comma = True # bool | Should comma-lists have spaces after the commas? (optional) (default to True)
    keyword_standardization = True # bool | Should the \"nicest\" key words be used? (e.g. JOIN -> INNER JOIN) (optional) (default to True)
    expand_comma_lists = False # bool | Should comma-lists (e.g. select a,b,c) have line breaks added? (optional) (default to False)
    expand_in_lists = False # bool | Should IN-lists have line breaks added? (optional) (default to False)
    expand_boolean_expressions = True # bool | Should boolean expressions have line breaks added? (optional) (default to True)
    expand_between_conditions = True # bool | Should between conditions have line breaks added? (optional) (default to True)
    expand_case_statements = True # bool | Should case-statements have line breaks added? (optional) (default to True)
    max_line_width = 120 # int | Maximum number of characters to allow on one line (if possible) (optional) (default to 120)
    space_before_trailing_single_line_comments = True # bool | Should the be a space before trailing single line comments? (optional) (default to True)
    multiline_comment_extra_line_break = False # bool | Should an additional line break be added after multi-line comments? (optional) (default to False)

    try:
        # PutQueryToFormat: Formats SQL into a more readable form, a.k.a. Pretty-Print the SQL.
        api_response = await api_instance.put_query_to_format(body, trailing_commas=trailing_commas, uppercase_keywords=uppercase_keywords, break_join_on_sections=break_join_on_sections, space_after_expanded_comma=space_after_expanded_comma, keyword_standardization=keyword_standardization, expand_comma_lists=expand_comma_lists, expand_in_lists=expand_in_lists, expand_boolean_expressions=expand_boolean_expressions, expand_between_conditions=expand_between_conditions, expand_case_statements=expand_case_statements, max_line_width=max_line_width, space_before_trailing_single_line_comments=space_before_trailing_single_line_comments, multiline_comment_extra_line_break=multiline_comment_extra_line_break)
        print("The response of SqlDesignApi->put_query_to_format:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlDesignApi->put_query_to_format: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| LuminesceSql to Pretty-Print. Even if it doesn&#39;t parse an attempt will be made to format it | 
 **trailing_commas** | **bool**| Should commas be after an expression (as opposed to before) | [optional] [default to True]
 **uppercase_keywords** | **bool**| Should key words be capitalized | [optional] [default to False]
 **break_join_on_sections** | **bool**| Should clauses on joins be given line breaks? | [optional] [default to True]
 **space_after_expanded_comma** | **bool**| Should comma-lists have spaces after the commas? | [optional] [default to True]
 **keyword_standardization** | **bool**| Should the \&quot;nicest\&quot; key words be used? (e.g. JOIN -&gt; INNER JOIN) | [optional] [default to True]
 **expand_comma_lists** | **bool**| Should comma-lists (e.g. select a,b,c) have line breaks added? | [optional] [default to False]
 **expand_in_lists** | **bool**| Should IN-lists have line breaks added? | [optional] [default to False]
 **expand_boolean_expressions** | **bool**| Should boolean expressions have line breaks added? | [optional] [default to True]
 **expand_between_conditions** | **bool**| Should between conditions have line breaks added? | [optional] [default to True]
 **expand_case_statements** | **bool**| Should case-statements have line breaks added? | [optional] [default to True]
 **max_line_width** | **int**| Maximum number of characters to allow on one line (if possible) | [optional] [default to 120]
 **space_before_trailing_single_line_comments** | **bool**| Should the be a space before trailing single line comments? | [optional] [default to True]
 **multiline_comment_extra_line_break** | **bool**| Should an additional line break be added after multi-line comments? | [optional] [default to False]

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sql_to_file_read_design**
> FileReaderBuilderDef put_sql_to_file_read_design(determine_available_sources=determine_available_sources, body=body)

[EXPERIMENTAL] PutSqlToFileReadDesign: Generates a SQL-file-read-design object from SQL string, if possible.

SQL to attempt to create a Design object from

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from luminesce.models.file_reader_builder_def import FileReaderBuilderDef
from pprint import pprint

import os
from luminesce import (
    ApiClientFactory,
    SqlDesignApi,
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
    api_instance = api_client_factory.build(luminesce.SqlDesignApi)
    determine_available_sources = True # bool | Should the available sources be determined from `Sys.Registration` (optional) (default to True)
    body = @x = 
use Drive.Csv
  --file=/some/folder/somefile.csv
enduse;

select * from @x; # str | SQL query to generate the file read design object from (optional)

    try:
        # [EXPERIMENTAL] PutSqlToFileReadDesign: Generates a SQL-file-read-design object from SQL string, if possible.
        api_response = await api_instance.put_sql_to_file_read_design(determine_available_sources=determine_available_sources, body=body)
        print("The response of SqlDesignApi->put_sql_to_file_read_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlDesignApi->put_sql_to_file_read_design: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **determine_available_sources** | **bool**| Should the available sources be determined from &#x60;Sys.Registration&#x60; | [optional] [default to True]
 **body** | **str**| SQL query to generate the file read design object from | [optional] 

### Return type

[**FileReaderBuilderDef**](FileReaderBuilderDef.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sql_to_query_design**
> QueryDesign put_sql_to_query_design(body, validate_with_metadata=validate_with_metadata)

[EXPERIMENTAL] PutSqlToQueryDesign: Generates a SQL-design object from SQL string, if possible.

SQL to attempt to create a Design object from

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from luminesce.models.query_design import QueryDesign
from pprint import pprint

import os
from luminesce import (
    ApiClientFactory,
    SqlDesignApi,
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
    api_instance = api_client_factory.build(luminesce.SqlDesignApi)
    body = SELECT
    [TableName],
    Count(distinct [FieldName]) as [NumberOfFields]
FROM
    [Sys.Field]
WHERE
    ([TableName] = 'Sys.Registration')
GROUP BY
    [TableName]
ORDER BY
    [DataType]
LIMIT 42 # str | SQL query to generate the design object from
    validate_with_metadata = True # bool | Should the table be validated against the users' view of Sys.Field to fill in DataTypes, etc.? (optional) (default to True)

    try:
        # [EXPERIMENTAL] PutSqlToQueryDesign: Generates a SQL-design object from SQL string, if possible.
        api_response = await api_instance.put_sql_to_query_design(body, validate_with_metadata=validate_with_metadata)
        print("The response of SqlDesignApi->put_sql_to_query_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlDesignApi->put_sql_to_query_design: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| SQL query to generate the design object from | 
 **validate_with_metadata** | **bool**| Should the table be validated against the users&#39; view of Sys.Field to fill in DataTypes, etc.? | [optional] [default to True]

### Return type

[**QueryDesign**](QueryDesign.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sql_to_view_design**
> ConvertToViewData put_sql_to_view_design(body)

[EXPERIMENTAL] PutSqlToViewDesign: Generates a structured view creation design from existing view creation SQL.

SQL which creates a view into a structured ConvertToViewData object

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from luminesce.models.convert_to_view_data import ConvertToViewData
from pprint import pprint

import os
from luminesce import (
    ApiClientFactory,
    SqlDesignApi,
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
    api_instance = api_client_factory.build(luminesce.SqlDesignApi)
    body = @x = 
use Sys.Admin.SetupView
  --provider=YourView
----
select * from Lusid.Instrument
enduse;

select * from @x; # str | SQL Query to generate the ConvertToViewData object from

    try:
        # [EXPERIMENTAL] PutSqlToViewDesign: Generates a structured view creation design from existing view creation SQL.
        api_response = await api_instance.put_sql_to_view_design(body)
        print("The response of SqlDesignApi->put_sql_to_view_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlDesignApi->put_sql_to_view_design: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| SQL Query to generate the ConvertToViewData object from | 

### Return type

[**ConvertToViewData**](ConvertToViewData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sql_to_writer_design**
> WriterDesign put_sql_to_writer_design(body, merge_additional_mapping_fields=merge_additional_mapping_fields)

[EXPERIMENTAL] PutSqlToWriterDesign: Generates a SQL-writer-design object from SQL string, if possible.

SQL to attempt to create a Writer Design object from

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from luminesce.models.writer_design import WriterDesign
from pprint import pprint

import os
from luminesce import (
    ApiClientFactory,
    SqlDesignApi,
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
    api_instance = api_client_factory.build(luminesce.SqlDesignApi)
    body = Select abc from xyz # str | SQL query to generate the writer design object from
    merge_additional_mapping_fields = False # bool | Should `Sys.Field` be used to find additional potential fields to map from? (not always possible) (optional) (default to False)

    try:
        # [EXPERIMENTAL] PutSqlToWriterDesign: Generates a SQL-writer-design object from SQL string, if possible.
        api_response = await api_instance.put_sql_to_writer_design(body, merge_additional_mapping_fields=merge_additional_mapping_fields)
        print("The response of SqlDesignApi->put_sql_to_writer_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlDesignApi->put_sql_to_writer_design: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| SQL query to generate the writer design object from | 
 **merge_additional_mapping_fields** | **bool**| Should &#x60;Sys.Field&#x60; be used to find additional potential fields to map from? (not always possible) | [optional] [default to False]

### Return type

[**WriterDesign**](WriterDesign.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_view_design_to_sql**
> str put_view_design_to_sql(convert_to_view_data)

[EXPERIMENTAL] PutViewDesignToSql: Generates view creation sql from a structured view creation design

Converts a ConvertToView specification into SQL that creates a view

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from luminesce.models.convert_to_view_data import ConvertToViewData
from pprint import pprint

import os
from luminesce import (
    ApiClientFactory,
    SqlDesignApi,
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
    api_instance = api_client_factory.build(luminesce.SqlDesignApi)
    convert_to_view_data = {"query":"select * from Lusid.Instrument.bond","name":"Views.MyView","description":"This is a tooltip for the view as a whole","documentationLink":"https://mydocumentationlink.com","viewParameters":[{"name":"MyTextParam","dataType":"Text","value":"Portfolio","isTableDataMandatory":false,"description":"This is a parameter tooltip"},{"name":"EffectiveAt","dataType":"Date","value":"2023-05-03","isTableDataMandatory":false,"description":"This is a parameter tooltip"},{"name":"IsActive","dataType":"Boolean","value":"true","isTableDataMandatory":true,"description":"This is a parameter tooltip"},{"name":"EndUserTable","dataType":"Table","value":"@end_user_table","isTableDataMandatory":true,"description":"This is a parameter tooltip"}],"otherParameters":{}} # ConvertToViewData | Structured Query design object to generate SQL from

    try:
        # [EXPERIMENTAL] PutViewDesignToSql: Generates view creation sql from a structured view creation design
        api_response = await api_instance.put_view_design_to_sql(convert_to_view_data)
        print("The response of SqlDesignApi->put_view_design_to_sql:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlDesignApi->put_view_design_to_sql: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **convert_to_view_data** | [**ConvertToViewData**](ConvertToViewData.md)| Structured Query design object to generate SQL from | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_writer_design_to_sql**
> str put_writer_design_to_sql(writer_design)

[EXPERIMENTAL] PutWriterDesignToSql: Generates writer SQL from a valid writer-design structure

SQL Writer Design specification to generate Writer SQL from

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import luminesce
from luminesce.rest import ApiException
from luminesce.models.writer_design import WriterDesign
from pprint import pprint

import os
from luminesce import (
    ApiClientFactory,
    SqlDesignApi,
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
    api_instance = api_client_factory.build(luminesce.SqlDesignApi)
    writer_design = {"sql":"\n@x = select SomeScope as Scope from Somewhere;\nselect * from Lusid.Instrument.Bond where ToWriter = @x","availableToMapFrom":[{"expression":"SomeScope","alias":"Scope","flags":"None"}],"parameter":{"providerName":"Lusid.Instrument.Bond","parameterName":"ToWrite","fields":[{"name":"Scope","type":"Text","description":"Scope of the instrument","mapping":{"expression":"SomeScope","alias":"Scope","flags":"None"}},{"name":"DisplayName","type":"Text"}]},"availableParameters":[{"providerName":"Lusid.Instrument.Bond","parameterName":"ToWrite","fields":[{"name":"Scope","type":"Text","description":"Scope of the instrument","mapping":{"expression":"SomeScope","alias":"Scope","flags":"None"}},{"name":"DisplayName","type":"Text"}]},{"providerName":"Email.Send","parameterName":"ToSend","fields":[{"name":"Subject","type":"Text"},{"name":"Body","type":"Text"}]}]} # WriterDesign | Structured Writer Design design object to generate Writer SQL from

    try:
        # [EXPERIMENTAL] PutWriterDesignToSql: Generates writer SQL from a valid writer-design structure
        api_response = await api_instance.put_writer_design_to_sql(writer_design)
        print("The response of SqlDesignApi->put_writer_design_to_sql:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlDesignApi->put_writer_design_to_sql: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **writer_design** | [**WriterDesign**](WriterDesign.md)| Structured Writer Design design object to generate Writer SQL from | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

