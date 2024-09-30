# luminesce.SqlDesignApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_provider_template_for_export**](SqlDesignApi.md#get_provider_template_for_export) | **GET** /api/Sql/providertemplateforexport | GetProviderTemplateForExport: Makes a fields template for file importing via a writer
[**put_case_statement_design_sql_to_design**](SqlDesignApi.md#put_case_statement_design_sql_to_design) | **PUT** /api/Sql/tocasestatementdesign | [EXPERIMENTAL] PutCaseStatementDesignSqlToDesign: Convert SQL to a case statement design object
[**put_case_statement_design_to_sql**](SqlDesignApi.md#put_case_statement_design_to_sql) | **PUT** /api/Sql/fromcasestatementdesign | [EXPERIMENTAL] PutCaseStatementDesignToSql: Convert a case statement design object to SQL
[**put_file_read_design_to_sql**](SqlDesignApi.md#put_file_read_design_to_sql) | **PUT** /api/Sql/fromfilereaddesign | [EXPERIMENTAL] PutFileReadDesignToSql: Make file read SQL from a design object
[**put_inlined_properties_design_sql_to_design**](SqlDesignApi.md#put_inlined_properties_design_sql_to_design) | **PUT** /api/Sql/toinlinedpropertiesdesign | [EXPERIMENTAL] PutInlinedPropertiesDesignSqlToDesign: Make an inlined properties design from SQL
[**put_inlined_properties_design_to_sql**](SqlDesignApi.md#put_inlined_properties_design_to_sql) | **PUT** /api/Sql/frominlinedpropertiesdesign | [EXPERIMENTAL] PutInlinedPropertiesDesignToSql: Make inlined properties SQL from a design object
[**put_intellisense**](SqlDesignApi.md#put_intellisense) | **PUT** /api/Sql/intellisense | PutIntellisense: Make intellisense prompts given an SQL snip-it
[**put_intellisense_error**](SqlDesignApi.md#put_intellisense_error) | **PUT** /api/Sql/intellisenseError | PutIntellisenseError: Get error ranges from SQL
[**put_query_design_to_sql**](SqlDesignApi.md#put_query_design_to_sql) | **PUT** /api/Sql/fromdesign | [EXPERIMENTAL] PutQueryDesignToSql: Make SQL from a structured query design
[**put_query_to_format**](SqlDesignApi.md#put_query_to_format) | **PUT** /api/Sql/pretty | PutQueryToFormat: Format SQL into a more readable form
[**put_sql_to_extract_scalar_parameters**](SqlDesignApi.md#put_sql_to_extract_scalar_parameters) | **PUT** /api/Sql/extractscalarparameters | [EXPERIMENTAL] PutSqlToExtractScalarParameters: Extract scalar parameter information from SQL
[**put_sql_to_file_read_design**](SqlDesignApi.md#put_sql_to_file_read_design) | **PUT** /api/Sql/tofilereaddesign | [EXPERIMENTAL] PutSqlToFileReadDesign: Make a design object from file-read SQL
[**put_sql_to_query_design**](SqlDesignApi.md#put_sql_to_query_design) | **PUT** /api/Sql/todesign | [EXPERIMENTAL] PutSqlToQueryDesign: Make a SQL-design object from SQL if possible
[**put_sql_to_view_design**](SqlDesignApi.md#put_sql_to_view_design) | **PUT** /api/Sql/toviewdesign | [EXPERIMENTAL] PutSqlToViewDesign: Make a view-design from view creation SQL
[**put_sql_to_writer_design**](SqlDesignApi.md#put_sql_to_writer_design) | **PUT** /api/Sql/towriterdesign | [EXPERIMENTAL] PutSqlToWriterDesign: Make a SQL-writer-design object from SQL
[**put_view_design_to_sql**](SqlDesignApi.md#put_view_design_to_sql) | **PUT** /api/Sql/fromviewdesign | [EXPERIMENTAL] PutViewDesignToSql: Make view creation sql from a view-design
[**put_writer_design_to_sql**](SqlDesignApi.md#put_writer_design_to_sql) | **PUT** /api/Sql/fromwriterdesign | [EXPERIMENTAL] PutWriterDesignToSql: Make writer SQL from a writer-design object


# **get_provider_template_for_export**
> bytearray get_provider_template_for_export(provider, content_type)

GetProviderTemplateForExport: Makes a fields template for file importing via a writer

Generates a template file for all the writable fields for a given provider returned in CSV or Excel (xlsx) format (as a file to be downloaded)

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)
        provider = 'provider_example' # str | Name of the provider for which this template is for
        content_type = 'content_type_example' # str | File content type for the Template. csv or excel

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_provider_template_for_export(provider, content_type, opts=opts)

            # GetProviderTemplateForExport: Makes a fields template for file importing via a writer
            api_response = await api_instance.get_provider_template_for_export(provider, content_type)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->get_provider_template_for_export: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Name of the provider for which this template is for | 
 **content_type** | **str**| File content type for the Template. csv or excel | 

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

# **put_case_statement_design_sql_to_design**
> CaseStatementDesign put_case_statement_design_sql_to_design(body=body)

[EXPERIMENTAL] PutCaseStatementDesignSqlToDesign: Convert SQL to a case statement design object

Converts a SQL query to a CaseStatementDesign object  > This method is generally only intended for IDE generation purposes.  > It is largely internal to the Finbourne web user interfaces and subject to change without notice. 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)
        body = CASE 
 WHEN [currency] = 'US' THEN 'USD' 
 WHEN [currency] = 'Gb' THEN 'GBP' 
 ELSE [currency] 
 END # str | SQL to attempt to create an case statement Design object from (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_case_statement_design_sql_to_design(body=body, opts=opts)

            # [EXPERIMENTAL] PutCaseStatementDesignSqlToDesign: Convert SQL to a case statement design object
            api_response = await api_instance.put_case_statement_design_sql_to_design(body=body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_case_statement_design_sql_to_design: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| SQL to attempt to create an case statement Design object from | [optional] 

### Return type

[**CaseStatementDesign**](CaseStatementDesign.md)

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

# **put_case_statement_design_to_sql**
> str put_case_statement_design_to_sql(case_statement_design)

[EXPERIMENTAL] PutCaseStatementDesignToSql: Convert a case statement design object to SQL

Generates a SQL case statement query from a structured CaseStatementDesign object  > This method is generally only intended for IDE generation purposes.  > It is largely internal to the Finbourne web user interfaces and subject to change without notice. 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # case_statement_design = CaseStatementDesign()
        # case_statement_design = CaseStatementDesign.from_json("")
        case_statement_design = CaseStatementDesign.from_dict({"selectedField":"currency","caseStatementItems":[{"filter":"Eq","source":"USD","target":"US"}]}) # CaseStatementDesign | CaseStatementDesign object to try and create a SQL query from

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_case_statement_design_to_sql(case_statement_design, opts=opts)

            # [EXPERIMENTAL] PutCaseStatementDesignToSql: Convert a case statement design object to SQL
            api_response = await api_instance.put_case_statement_design_to_sql(case_statement_design)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_case_statement_design_to_sql: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_statement_design** | [**CaseStatementDesign**](CaseStatementDesign.md)| CaseStatementDesign object to try and create a SQL query from | 

### Return type

**str**

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_file_read_design_to_sql**
> FileReaderBuilderResponse put_file_read_design_to_sql(file_reader_builder_def, execute_query=execute_query)

[EXPERIMENTAL] PutFileReadDesignToSql: Make file read SQL from a design object

Generates SQL from a FileReaderBuilderDef object  > This method is generally only intended for IDE generation purposes.  > It is largely internal to the Finbourne web user interfaces and subject to change without notice. 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # file_reader_builder_def = FileReaderBuilderDef()
        # file_reader_builder_def = FileReaderBuilderDef.from_json("")
        file_reader_builder_def = FileReaderBuilderDef.from_dict({"limit":0,"source":{"location":"Drive","type":"Csv"},"filePath":"/some/folder","folderFilter":".*\\.csv","addFileName":true}) # FileReaderBuilderDef | Structured file read design object to generate SQL from
        execute_query = True # bool | Should the generated query be executed to build preview data or determine errors.> (optional) (default to True)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_file_read_design_to_sql(file_reader_builder_def, execute_query=execute_query, opts=opts)

            # [EXPERIMENTAL] PutFileReadDesignToSql: Make file read SQL from a design object
            api_response = await api_instance.put_file_read_design_to_sql(file_reader_builder_def, execute_query=execute_query)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_file_read_design_to_sql: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_reader_builder_def** | [**FileReaderBuilderDef**](FileReaderBuilderDef.md)| Structured file read design object to generate SQL from | 
 **execute_query** | **bool**| Should the generated query be executed to build preview data or determine errors.&gt; | [optional] [default to True]

### Return type

[**FileReaderBuilderResponse**](FileReaderBuilderResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_inlined_properties_design_sql_to_design**
> InlinedPropertyDesign put_inlined_properties_design_sql_to_design(body=body)

[EXPERIMENTAL] PutInlinedPropertiesDesignSqlToDesign: Make an inlined properties design from SQL

Generates a SQL-inlined-properties-design object from SQL string, if possible.  > This method is generally only intended for IDE generation purposes.  > It is largely internal to the Finbourne web user interfaces and subject to change without notice. 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)
        body = @keysToCatalog = values('Portfolio/3897-78d4-e91c-26/location', 'PortfolioLocation', false, '');
 @config = select column1 as [Key], column2 as Name, column3 as IsMain, column4 as Description from @keysToCatalog; 
 select * from Sys.Admin.Lusid.Provider.Configure where Provider = 'Lusid.Portfolio' and Configuration = @config; # str | SQL query to attempt to generate the inlined properties design object from (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_inlined_properties_design_sql_to_design(body=body, opts=opts)

            # [EXPERIMENTAL] PutInlinedPropertiesDesignSqlToDesign: Make an inlined properties design from SQL
            api_response = await api_instance.put_inlined_properties_design_sql_to_design(body=body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_inlined_properties_design_sql_to_design: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| SQL query to attempt to generate the inlined properties design object from | [optional] 

### Return type

[**InlinedPropertyDesign**](InlinedPropertyDesign.md)

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

# **put_inlined_properties_design_to_sql**
> str put_inlined_properties_design_to_sql(inlined_property_design)

[EXPERIMENTAL] PutInlinedPropertiesDesignToSql: Make inlined properties SQL from a design object

Generates inlined properties SQL from a structured design  > This method is generally only intended for IDE generation purposes.  > It is largely internal to the Finbourne web user interfaces and subject to change without notice. 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # inlined_property_design = InlinedPropertyDesign()
        # inlined_property_design = InlinedPropertyDesign.from_json("")
        inlined_property_design = InlinedPropertyDesign.from_dict({"providerName":"Lusid.portfolio","inlinedPropertyItems":[{"key":"fieldKey","name":"fieldName","isMain":true,"description":"some description"}]}) # InlinedPropertyDesign | Inlined properties Designer specification to generate SQL from

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_inlined_properties_design_to_sql(inlined_property_design, opts=opts)

            # [EXPERIMENTAL] PutInlinedPropertiesDesignToSql: Make inlined properties SQL from a design object
            api_response = await api_instance.put_inlined_properties_design_to_sql(inlined_property_design)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_inlined_properties_design_to_sql: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inlined_property_design** | [**InlinedPropertyDesign**](InlinedPropertyDesign.md)| Inlined properties Designer specification to generate SQL from | 

### Return type

**str**

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_intellisense**
> IntellisenseResponse put_intellisense(intellisense_request)

PutIntellisense: Make intellisense prompts given an SQL snip-it

Generate a set of possible intellisense prompts given a SQL snip-it (in need not yet be valid SQL) and cursor location  > This method is generally only intended for IDE generation purposes.  > It is largely internal to the Finbourne web user interfaces and subject to change without notice. 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # intellisense_request = IntellisenseRequest()
        # intellisense_request = IntellisenseRequest.from_json("")
        intellisense_request = IntellisenseRequest.from_dict({"lines":["select *","from somewhere"],"position":{"row":0,"column":4}}) # IntellisenseRequest | SQL and a row/colum position within it from which to determine intellisense options for the user to potentially choose from.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_intellisense(intellisense_request, opts=opts)

            # PutIntellisense: Make intellisense prompts given an SQL snip-it
            api_response = await api_instance.put_intellisense(intellisense_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_intellisense: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intellisense_request** | [**IntellisenseRequest**](IntellisenseRequest.md)| SQL and a row/colum position within it from which to determine intellisense options for the user to potentially choose from. | 

### Return type

[**IntellisenseResponse**](IntellisenseResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_intellisense_error**
> ErrorHighlightResponse put_intellisense_error(error_highlight_request)

PutIntellisenseError: Get error ranges from SQL

Generate a set of error ranges, if any, in the given SQL (expressed as Lines)  > This method is generally only intended for IDE generation purposes.  > It is largely internal to the Finbourne web user interfaces and subject to change without notice. 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # error_highlight_request = ErrorHighlightRequest()
        # error_highlight_request = ErrorHighlightRequest.from_json("")
        error_highlight_request = ErrorHighlightRequest.from_dict({"lines":["select mx(x) x from y"],"ensureSomeTextIsSelected":false}) # ErrorHighlightRequest | SQL (by line) to syntax check and return error ranges from within, if any.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_intellisense_error(error_highlight_request, opts=opts)

            # PutIntellisenseError: Get error ranges from SQL
            api_response = await api_instance.put_intellisense_error(error_highlight_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_intellisense_error: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_highlight_request** | [**ErrorHighlightRequest**](ErrorHighlightRequest.md)| SQL (by line) to syntax check and return error ranges from within, if any. | 

### Return type

[**ErrorHighlightResponse**](ErrorHighlightResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_query_design_to_sql**
> str put_query_design_to_sql(query_design)

[EXPERIMENTAL] PutQueryDesignToSql: Make SQL from a structured query design

Generates SQL from a QueryDesign object  > This method is generally only intended for IDE generation purposes.  > It is largely internal to the Finbourne web user interfaces and subject to change without notice. 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # query_design = QueryDesign()
        # query_design = QueryDesign.from_json("")
        query_design = QueryDesign.from_dict({"tableName":"Sys.Field","fields":[{"name":"TableName","dataType":"Text","shouldSelect":true,"filters":[{"operator":"Eq","value":"Sys.Registration"}],"aggregations":[]},{"name":"FieldName","dataType":"Text","shouldSelect":true,"filters":[],"aggregations":[{"type":"count_distinct","alias":"NumberOfFields"}]}],"orderBy":[{"field":"DataType","direction":"asc"}],"limit":42,"warnings":[],"availableFields":[]}) # QueryDesign | Structured Query design object to generate SQL from

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_query_design_to_sql(query_design, opts=opts)

            # [EXPERIMENTAL] PutQueryDesignToSql: Make SQL from a structured query design
            api_response = await api_instance.put_query_design_to_sql(query_design)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_query_design_to_sql: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_design** | [**QueryDesign**](QueryDesign.md)| Structured Query design object to generate SQL from | 

### Return type

**str**

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_query_to_format**
> str put_query_to_format(body, trailing_commas=trailing_commas, uppercase_keywords=uppercase_keywords, break_join_on_sections=break_join_on_sections, space_after_expanded_comma=space_after_expanded_comma, keyword_standardization=keyword_standardization, expand_comma_lists=expand_comma_lists, expand_in_lists=expand_in_lists, expand_boolean_expressions=expand_boolean_expressions, expand_between_conditions=expand_between_conditions, expand_case_statements=expand_case_statements, max_line_width=max_line_width, space_before_trailing_single_line_comments=space_before_trailing_single_line_comments, multiline_comment_extra_line_break=multiline_comment_extra_line_break)

PutQueryToFormat: Format SQL into a more readable form

 This formats SQL (given a set of options as to how to do so), a.k.a. Pretty-Print the SQL. It takes some SQL (or a fragment thereof, it need not fully parse as yet and certainly need not execute correctly) and returns the reformatted version. e.g. ```sql select x,y,z from a inner join b on a.x=b.x where x>y or y!=z ``` becomes ```sql select x, y, z from a inner join b    on a.x = b.x where x > y    or y != z ``` 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)
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
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_query_to_format(body, trailing_commas=trailing_commas, uppercase_keywords=uppercase_keywords, break_join_on_sections=break_join_on_sections, space_after_expanded_comma=space_after_expanded_comma, keyword_standardization=keyword_standardization, expand_comma_lists=expand_comma_lists, expand_in_lists=expand_in_lists, expand_boolean_expressions=expand_boolean_expressions, expand_between_conditions=expand_between_conditions, expand_case_statements=expand_case_statements, max_line_width=max_line_width, space_before_trailing_single_line_comments=space_before_trailing_single_line_comments, multiline_comment_extra_line_break=multiline_comment_extra_line_break, opts=opts)

            # PutQueryToFormat: Format SQL into a more readable form
            api_response = await api_instance.put_query_to_format(body, trailing_commas=trailing_commas, uppercase_keywords=uppercase_keywords, break_join_on_sections=break_join_on_sections, space_after_expanded_comma=space_after_expanded_comma, keyword_standardization=keyword_standardization, expand_comma_lists=expand_comma_lists, expand_in_lists=expand_in_lists, expand_boolean_expressions=expand_boolean_expressions, expand_between_conditions=expand_between_conditions, expand_case_statements=expand_case_statements, max_line_width=max_line_width, space_before_trailing_single_line_comments=space_before_trailing_single_line_comments, multiline_comment_extra_line_break=multiline_comment_extra_line_break)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_query_to_format: %s\n" % e)

asyncio.run(main())
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

# **put_sql_to_extract_scalar_parameters**
> List[ScalarParameter] put_sql_to_extract_scalar_parameters(body)

[EXPERIMENTAL] PutSqlToExtractScalarParameters: Extract scalar parameter information from SQL

Extracts information about all the scalar parameters defined in the given SQL statement  > This method is generally only intended for IDE generation purposes.  > It is largely internal to the Finbourne web user interfaces and subject to change without notice. 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)
        body = select abc, :p1:'this' as c1 from xxx where abc = :abcP:123 or xyz in (:p2:, 'zzz') # str | SQL query to generate the design object from

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_sql_to_extract_scalar_parameters(body, opts=opts)

            # [EXPERIMENTAL] PutSqlToExtractScalarParameters: Extract scalar parameter information from SQL
            api_response = await api_instance.put_sql_to_extract_scalar_parameters(body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_sql_to_extract_scalar_parameters: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| SQL query to generate the design object from | 

### Return type

[**List[ScalarParameter]**](ScalarParameter.md)

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

# **put_sql_to_file_read_design**
> FileReaderBuilderDef put_sql_to_file_read_design(determine_available_sources=determine_available_sources, body=body)

[EXPERIMENTAL] PutSqlToFileReadDesign: Make a design object from file-read SQL

Generates a SQL-file-read-design object from SQL string, if possible.  > This method is generally only intended for IDE generation purposes.  > It is largely internal to the Finbourne web user interfaces and subject to change without notice. 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)
        determine_available_sources = True # bool | Should the available sources be determined from `Sys.Registration` (optional) (default to True)
        body = @x = 
use Drive.Csv
  --file=/some/folder/somefile.csv
enduse;

select * from @x; # str | SQL query to generate the file read design object from (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_sql_to_file_read_design(determine_available_sources=determine_available_sources, body=body, opts=opts)

            # [EXPERIMENTAL] PutSqlToFileReadDesign: Make a design object from file-read SQL
            api_response = await api_instance.put_sql_to_file_read_design(determine_available_sources=determine_available_sources, body=body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_sql_to_file_read_design: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **determine_available_sources** | **bool**| Should the available sources be determined from &#x60;Sys.Registration&#x60; | [optional] [default to True]
 **body** | **str**| SQL query to generate the file read design object from | [optional] 

### Return type

[**FileReaderBuilderDef**](FileReaderBuilderDef.md)

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

# **put_sql_to_query_design**
> QueryDesign put_sql_to_query_design(body, validate_with_metadata=validate_with_metadata)

[EXPERIMENTAL] PutSqlToQueryDesign: Make a SQL-design object from SQL if possible

Generates a QueryDesign object from simple SQL if possible  > This method is generally only intended for IDE generation purposes.  > It is largely internal to the Finbourne web user interfaces and subject to change without notice. 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)
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
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_sql_to_query_design(body, validate_with_metadata=validate_with_metadata, opts=opts)

            # [EXPERIMENTAL] PutSqlToQueryDesign: Make a SQL-design object from SQL if possible
            api_response = await api_instance.put_sql_to_query_design(body, validate_with_metadata=validate_with_metadata)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_sql_to_query_design: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| SQL query to generate the design object from | 
 **validate_with_metadata** | **bool**| Should the table be validated against the users&#39; view of Sys.Field to fill in DataTypes, etc.? | [optional] [default to True]

### Return type

[**QueryDesign**](QueryDesign.md)

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

# **put_sql_to_view_design**
> ConvertToViewData put_sql_to_view_design(body)

[EXPERIMENTAL] PutSqlToViewDesign: Make a view-design from view creation SQL

Converts SQL which creates a view into a structured ConvertToViewData object  > This method is generally only intended for IDE generation purposes.  > It is largely internal to the Finbourne web user interfaces and subject to change without notice. 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)
        body = @x = 
use Sys.Admin.SetupView
  --provider=YourView
----
select * from Lusid.Instrument
enduse;

select * from @x; # str | SQL Query to generate the ConvertToViewData object from

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_sql_to_view_design(body, opts=opts)

            # [EXPERIMENTAL] PutSqlToViewDesign: Make a view-design from view creation SQL
            api_response = await api_instance.put_sql_to_view_design(body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_sql_to_view_design: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| SQL Query to generate the ConvertToViewData object from | 

### Return type

[**ConvertToViewData**](ConvertToViewData.md)

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

# **put_sql_to_writer_design**
> WriterDesign put_sql_to_writer_design(body, merge_additional_mapping_fields=merge_additional_mapping_fields)

[EXPERIMENTAL] PutSqlToWriterDesign: Make a SQL-writer-design object from SQL

Generates a SQL-writer-design object (WriterDesign) from a SQL query, if possible  > This method is generally only intended for IDE generation purposes.  > It is largely internal to the Finbourne web user interfaces and subject to change without notice. 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)
        body = Select abc from xyz # str | SQL query to generate the writer design object from
        merge_additional_mapping_fields = False # bool | Should `Sys.Field` be used to find additional potential fields to map from? (not always possible) (optional) (default to False)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_sql_to_writer_design(body, merge_additional_mapping_fields=merge_additional_mapping_fields, opts=opts)

            # [EXPERIMENTAL] PutSqlToWriterDesign: Make a SQL-writer-design object from SQL
            api_response = await api_instance.put_sql_to_writer_design(body, merge_additional_mapping_fields=merge_additional_mapping_fields)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_sql_to_writer_design: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| SQL query to generate the writer design object from | 
 **merge_additional_mapping_fields** | **bool**| Should &#x60;Sys.Field&#x60; be used to find additional potential fields to map from? (not always possible) | [optional] [default to False]

### Return type

[**WriterDesign**](WriterDesign.md)

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

# **put_view_design_to_sql**
> str put_view_design_to_sql(convert_to_view_data)

[EXPERIMENTAL] PutViewDesignToSql: Make view creation sql from a view-design

Converts a ConvertToView specification into SQL that creates a view  > This method is generally only intended for IDE generation purposes.  > It is largely internal to the Finbourne web user interfaces and subject to change without notice. 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # convert_to_view_data = ConvertToViewData()
        # convert_to_view_data = ConvertToViewData.from_json("")
        convert_to_view_data = ConvertToViewData.from_dict({"query":"select * from Lusid.Instrument.bond","name":"Views.MyView","description":"This is a tooltip for the view as a whole","documentationLink":"https://mydocumentationlink.com","viewParameters":[{"name":"MyTextParam","dataType":"Text","value":"Portfolio","isTableDataMandatory":false,"description":"This is a parameter tooltip"},{"name":"EffectiveAt","dataType":"Date","value":"2023-05-03","isTableDataMandatory":false,"description":"This is a parameter tooltip"},{"name":"IsActive","dataType":"Boolean","value":"true","isTableDataMandatory":true,"description":"This is a parameter tooltip"},{"name":"EndUserTable","dataType":"Table","value":"@end_user_table","isTableDataMandatory":true,"description":"This is a parameter tooltip"}],"otherParameters":{}}) # ConvertToViewData | Structured Query design object to generate SQL from

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_view_design_to_sql(convert_to_view_data, opts=opts)

            # [EXPERIMENTAL] PutViewDesignToSql: Make view creation sql from a view-design
            api_response = await api_instance.put_view_design_to_sql(convert_to_view_data)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_view_design_to_sql: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **convert_to_view_data** | [**ConvertToViewData**](ConvertToViewData.md)| Structured Query design object to generate SQL from | 

### Return type

**str**

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **put_writer_design_to_sql**
> str put_writer_design_to_sql(writer_design)

[EXPERIMENTAL] PutWriterDesignToSql: Make writer SQL from a writer-design object

Generates writer SQL from a valid WriterDesign structure  > This method is generally only intended for IDE generation purposes.  > It is largely internal to the Finbourne web user interfaces and subject to change without notice. 

### Example

```python
import asyncio
from luminesce.exceptions import ApiException
from luminesce.extensions.configuration_options import ConfigurationOptions
from luminesce.models import *
from pprint import pprint
from luminesce import (
    ApiClientFactory,
    SqlDesignApi
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
        api_instance = api_client_factory.build(SqlDesignApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # writer_design = WriterDesign()
        # writer_design = WriterDesign.from_json("")
        writer_design = WriterDesign.from_dict({"sql":"\n@x = select SomeScope as Scope from Somewhere;\nselect * from Lusid.Instrument.Bond where ToWriter = @x","availableToMapFrom":[{"expression":"SomeScope","alias":"Scope","flags":"None"}],"parameter":{"providerName":"Lusid.Instrument.Bond","parameterName":"ToWrite","fields":[{"name":"Scope","type":"Text","description":"Scope of the instrument","mapping":{"expression":"SomeScope","alias":"Scope","flags":"None"}},{"name":"DisplayName","type":"Text"}]},"availableParameters":[{"providerName":"Lusid.Instrument.Bond","parameterName":"ToWrite","fields":[{"name":"Scope","type":"Text","description":"Scope of the instrument","mapping":{"expression":"SomeScope","alias":"Scope","flags":"None"}},{"name":"DisplayName","type":"Text"}]},{"providerName":"Email.Send","parameterName":"ToSend","fields":[{"name":"Subject","type":"Text"},{"name":"Body","type":"Text"}]}]}) # WriterDesign | Structured Writer Design design object to generate Writer SQL from

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.put_writer_design_to_sql(writer_design, opts=opts)

            # [EXPERIMENTAL] PutWriterDesignToSql: Make writer SQL from a writer-design object
            api_response = await api_instance.put_writer_design_to_sql(writer_design)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SqlDesignApi->put_writer_design_to_sql: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **writer_design** | [**WriterDesign**](WriterDesign.md)| Structured Writer Design design object to generate Writer SQL from | 

### Return type

**str**

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

