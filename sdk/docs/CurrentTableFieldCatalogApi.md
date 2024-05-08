# luminesce.CurrentTableFieldCatalogApi

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog**](CurrentTableFieldCatalogApi.md#get_catalog) | **GET** /api/Catalog | GetCatalog: Shows Table and Field level information on Providers that are currently running that you have access to (in Json format)


# **get_catalog**
> str get_catalog(free_text_search=free_text_search, json_proper=json_proper)

GetCatalog: Shows Table and Field level information on Providers that are currently running that you have access to (in Json format)

 The following LuminesceSql is executed to return this information:  ```sql @reg = select     Name,     min(Description) as Description,     min(DocumentationLink) as DocumentationLink,     iif(Category = 'View' and Client is not null, true, false) as IsView from     Sys.Registration where     Type in ('DirectProvider', 'DataProvider')     and      ShowAll = false group by     1     ;  @fld = select     TableName,     FieldName,     DataType,     FieldType,     IsPrimaryKey,     IsMain,     Description,     ParamDefaultValue,     TableParamColumns from     Sys.Field     ;  @x = select     coalesce(f.TableName, r.Name) as TableName,     coalesce(f.FieldName, 'N/A') as FieldName,     f.DataType,     f.FieldType,     f.IsPrimaryKey,     f.IsMain,     case          when f.TableName is not null then             f.Description         else             r.Name || ' returns a different set of columns depending on use.'         end as Description,     f.ParamDefaultValue,     f.TableParamColumns,     r.Description as ProviderDescription,     r.DocumentationLink,     r.IsView from     @reg r     left outer join @fld f         on r.Name = f.TableName order by     1, 5 desc, 6 desc, 2     ;     ```  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

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
    CurrentTableFieldCatalogApi,
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
    api_instance = api_client_factory.build(luminesce.CurrentTableFieldCatalogApi)
    free_text_search = 'free_text_search_example' # str | Limit the catalog to only things in some way dealing with the passed in text string (optional)
    json_proper = False # bool | Should this be text/json (not json-encoded-as-a-string) (optional) (default to False)

    try:
        # GetCatalog: Shows Table and Field level information on Providers that are currently running that you have access to (in Json format)
        api_response = await api_instance.get_catalog(free_text_search=free_text_search, json_proper=json_proper)
        print("The response of CurrentTableFieldCatalogApi->get_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrentTableFieldCatalogApi->get_catalog: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **free_text_search** | **str**| Limit the catalog to only things in some way dealing with the passed in text string | [optional] 
 **json_proper** | **bool**| Should this be text/json (not json-encoded-as-a-string) | [optional] [default to False]

### Return type

**str**

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

