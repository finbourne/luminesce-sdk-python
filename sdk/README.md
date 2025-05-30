<a id="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://fbn-prd.lusid.com/honeycomb*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApplicationMetadataApi* | [**get_services_as_access_controlled_resources**](docs/ApplicationMetadataApi.md#get_services_as_access_controlled_resources) | **GET** /api/metadata/access/resources | GetServicesAsAccessControlledResources: Get resources available for access control
*BinaryDownloadingApi* | [**download_binary**](docs/BinaryDownloadingApi.md#download_binary) | **GET** /api/Download/download | DownloadBinary: Download a Luminesce Binary you may run on-site
*BinaryDownloadingApi* | [**get_binary_versions**](docs/BinaryDownloadingApi.md#get_binary_versions) | **GET** /api/Download/versions | GetBinaryVersions: List available versions of binaries
*CertificateManagementApi* | [**download_certificate**](docs/CertificateManagementApi.md#download_certificate) | **GET** /api/Certificate/certificate | DownloadCertificate: Download domain or your personal certificates
*CertificateManagementApi* | [**list_certificates**](docs/CertificateManagementApi.md#list_certificates) | **GET** /api/Certificate/certificates | ListCertificates: List previously minted certificates
*CertificateManagementApi* | [**manage_certificate**](docs/CertificateManagementApi.md#manage_certificate) | **PUT** /api/Certificate/manage | ManageCertificate: Create / Renew / Revoke a certificate
*CurrentTableFieldCatalogApi* | [**get_catalog**](docs/CurrentTableFieldCatalogApi.md#get_catalog) | **GET** /api/Catalog | GetCatalog: Get a Flattened Table/Field Catalog
*CurrentTableFieldCatalogApi* | [**get_fields**](docs/CurrentTableFieldCatalogApi.md#get_fields) | **GET** /api/Catalog/fields | GetFields: List field and parameters for providers
*CurrentTableFieldCatalogApi* | [**get_providers**](docs/CurrentTableFieldCatalogApi.md#get_providers) | **GET** /api/Catalog/providers | GetProviders: List available providers
*HealthCheckingEndpointApi* | [**fake_node_reclaim**](docs/HealthCheckingEndpointApi.md#fake_node_reclaim) | **GET** /fakeNodeReclaim | [INTERNAL] FakeNodeReclaim: Helps testing of AWS node reclaim behaviour
*HistoricallyExecutedQueriesApi* | [**cancel_history**](docs/HistoricallyExecutedQueriesApi.md#cancel_history) | **DELETE** /api/History/{executionId} | CancelHistory: Cancel / Clear data from a history search
*HistoricallyExecutedQueriesApi* | [**fetch_history_result_histogram**](docs/HistoricallyExecutedQueriesApi.md#fetch_history_result_histogram) | **GET** /api/History/{executionId}/histogram | FetchHistoryResultHistogram: Make a histogram of results of a history search
*HistoricallyExecutedQueriesApi* | [**fetch_history_result_json**](docs/HistoricallyExecutedQueriesApi.md#fetch_history_result_json) | **GET** /api/History/{executionId}/json | FetchHistoryResultJson: Fetch JSON results from a query history search
*HistoricallyExecutedQueriesApi* | [**get_history**](docs/HistoricallyExecutedQueriesApi.md#get_history) | **GET** /api/History | GetHistory: Start a background history search
*HistoricallyExecutedQueriesApi* | [**get_progress_of_history**](docs/HistoricallyExecutedQueriesApi.md#get_progress_of_history) | **GET** /api/History/{executionId} | GetProgressOfHistory: View progress of a history search
*MultiQueryExecutionApi* | [**cancel_multi_query**](docs/MultiQueryExecutionApi.md#cancel_multi_query) | **DELETE** /api/MultiQueryBackground/{executionId} | CancelMultiQuery: Cancel / Clear a previously started query-set
*MultiQueryExecutionApi* | [**get_progress_of_multi_query**](docs/MultiQueryExecutionApi.md#get_progress_of_multi_query) | **GET** /api/MultiQueryBackground/{executionId} | GetProgressOfMultiQuery: View progress of the entire query-set load
*MultiQueryExecutionApi* | [**start_queries**](docs/MultiQueryExecutionApi.md#start_queries) | **PUT** /api/MultiQueryBackground | StartQueries: Run a given set of Sql queries in the background
*SqlBackgroundExecutionApi* | [**cancel_query**](docs/SqlBackgroundExecutionApi.md#cancel_query) | **DELETE** /api/SqlBackground/{executionId} | CancelQuery: Cancel / Clear data from a previously run query
*SqlBackgroundExecutionApi* | [**fetch_query_result_csv**](docs/SqlBackgroundExecutionApi.md#fetch_query_result_csv) | **GET** /api/SqlBackground/{executionId}/csv | FetchQueryResultCsv: Fetch the result of a query as CSV
*SqlBackgroundExecutionApi* | [**fetch_query_result_excel**](docs/SqlBackgroundExecutionApi.md#fetch_query_result_excel) | **GET** /api/SqlBackground/{executionId}/excel | FetchQueryResultExcel: Fetch the result of a query as an Excel file
*SqlBackgroundExecutionApi* | [**fetch_query_result_histogram**](docs/SqlBackgroundExecutionApi.md#fetch_query_result_histogram) | **GET** /api/SqlBackground/{executionId}/histogram | FetchQueryResultHistogram: Construct a histogram of the result of a query
*SqlBackgroundExecutionApi* | [**fetch_query_result_json**](docs/SqlBackgroundExecutionApi.md#fetch_query_result_json) | **GET** /api/SqlBackground/{executionId}/json | FetchQueryResultJson: Fetch the result of a query as a JSON string
*SqlBackgroundExecutionApi* | [**fetch_query_result_json_proper**](docs/SqlBackgroundExecutionApi.md#fetch_query_result_json_proper) | **GET** /api/SqlBackground/{executionId}/jsonProper | FetchQueryResultJsonProper: Fetch the result of a query as JSON
*SqlBackgroundExecutionApi* | [**fetch_query_result_parquet**](docs/SqlBackgroundExecutionApi.md#fetch_query_result_parquet) | **GET** /api/SqlBackground/{executionId}/parquet | FetchQueryResultParquet: Fetch the result of a query as Parquet
*SqlBackgroundExecutionApi* | [**fetch_query_result_pipe**](docs/SqlBackgroundExecutionApi.md#fetch_query_result_pipe) | **GET** /api/SqlBackground/{executionId}/pipe | FetchQueryResultPipe: Fetch the result of a query as pipe-delimited
*SqlBackgroundExecutionApi* | [**fetch_query_result_sqlite**](docs/SqlBackgroundExecutionApi.md#fetch_query_result_sqlite) | **GET** /api/SqlBackground/{executionId}/sqlite | FetchQueryResultSqlite: Fetch the result of a query as SqLite
*SqlBackgroundExecutionApi* | [**fetch_query_result_xml**](docs/SqlBackgroundExecutionApi.md#fetch_query_result_xml) | **GET** /api/SqlBackground/{executionId}/xml | FetchQueryResultXml: Fetch the result of a query as XML
*SqlBackgroundExecutionApi* | [**get_progress_of**](docs/SqlBackgroundExecutionApi.md#get_progress_of) | **GET** /api/SqlBackground/{executionId} | GetProgressOf: View query progress up to this point
*SqlBackgroundExecutionApi* | [**start_query**](docs/SqlBackgroundExecutionApi.md#start_query) | **PUT** /api/SqlBackground | StartQuery: Start to Execute Sql in the background
*SqlDesignApi* | [**get_provider_template_for_export**](docs/SqlDesignApi.md#get_provider_template_for_export) | **GET** /api/Sql/providertemplateforexport | GetProviderTemplateForExport: Makes a fields template for file importing via a writer
*SqlDesignApi* | [**put_case_statement_design_sql_to_design**](docs/SqlDesignApi.md#put_case_statement_design_sql_to_design) | **PUT** /api/Sql/tocasestatementdesign | PutCaseStatementDesignSqlToDesign: Convert SQL to a case statement design object
*SqlDesignApi* | [**put_case_statement_design_to_sql**](docs/SqlDesignApi.md#put_case_statement_design_to_sql) | **PUT** /api/Sql/fromcasestatementdesign | PutCaseStatementDesignToSql: Convert a case statement design object to SQL
*SqlDesignApi* | [**put_file_read_design_to_sql**](docs/SqlDesignApi.md#put_file_read_design_to_sql) | **PUT** /api/Sql/fromfilereaddesign | PutFileReadDesignToSql: Make file read SQL from a design object
*SqlDesignApi* | [**put_inlined_properties_design_sql_to_design**](docs/SqlDesignApi.md#put_inlined_properties_design_sql_to_design) | **PUT** /api/Sql/toinlinedpropertiesdesign | PutInlinedPropertiesDesignSqlToDesign: Make an inlined properties design from SQL
*SqlDesignApi* | [**put_inlined_properties_design_to_sql**](docs/SqlDesignApi.md#put_inlined_properties_design_to_sql) | **PUT** /api/Sql/frominlinedpropertiesdesign | PutInlinedPropertiesDesignToSql: Make inlined properties SQL from a design object
*SqlDesignApi* | [**put_intellisense**](docs/SqlDesignApi.md#put_intellisense) | **PUT** /api/Sql/intellisense | PutIntellisense: Make intellisense prompts given an SQL snip-it
*SqlDesignApi* | [**put_intellisense_error**](docs/SqlDesignApi.md#put_intellisense_error) | **PUT** /api/Sql/intellisenseError | PutIntellisenseError: Get error ranges from SQL
*SqlDesignApi* | [**put_lusid_grid_to_query**](docs/SqlDesignApi.md#put_lusid_grid_to_query) | **PUT** /api/Sql/fromlusidgrid | [EXPERIMENTAL] PutLusidGridToQuery: Generates SQL from a dashboard view
*SqlDesignApi* | [**put_query_design_to_sql**](docs/SqlDesignApi.md#put_query_design_to_sql) | **PUT** /api/Sql/fromdesign | PutQueryDesignToSql: Make SQL from a structured query design
*SqlDesignApi* | [**put_query_to_format**](docs/SqlDesignApi.md#put_query_to_format) | **PUT** /api/Sql/pretty | PutQueryToFormat: Format SQL into a more readable form
*SqlDesignApi* | [**put_sql_to_extract_scalar_parameters**](docs/SqlDesignApi.md#put_sql_to_extract_scalar_parameters) | **PUT** /api/Sql/extractscalarparameters | PutSqlToExtractScalarParameters: Extract scalar parameter information from SQL
*SqlDesignApi* | [**put_sql_to_file_read_design**](docs/SqlDesignApi.md#put_sql_to_file_read_design) | **PUT** /api/Sql/tofilereaddesign | PutSqlToFileReadDesign: Make a design object from file-read SQL
*SqlDesignApi* | [**put_sql_to_query_design**](docs/SqlDesignApi.md#put_sql_to_query_design) | **PUT** /api/Sql/todesign | PutSqlToQueryDesign: Make a SQL-design object from SQL if possible
*SqlDesignApi* | [**put_sql_to_view_design**](docs/SqlDesignApi.md#put_sql_to_view_design) | **PUT** /api/Sql/toviewdesign | PutSqlToViewDesign: Make a view-design from view creation SQL
*SqlDesignApi* | [**put_sql_to_writer_design**](docs/SqlDesignApi.md#put_sql_to_writer_design) | **PUT** /api/Sql/towriterdesign | PutSqlToWriterDesign: Make a SQL-writer-design object from SQL
*SqlDesignApi* | [**put_view_design_to_sql**](docs/SqlDesignApi.md#put_view_design_to_sql) | **PUT** /api/Sql/fromviewdesign | PutViewDesignToSql: Make view creation sql from a view-design
*SqlDesignApi* | [**put_writer_design_to_sql**](docs/SqlDesignApi.md#put_writer_design_to_sql) | **PUT** /api/Sql/fromwriterdesign | PutWriterDesignToSql: Make writer SQL from a writer-design object
*SqlExecutionApi* | [**get_by_query_csv**](docs/SqlExecutionApi.md#get_by_query_csv) | **GET** /api/Sql/csv/{query} | GetByQueryCsv: Execute Sql from the url returning CSV
*SqlExecutionApi* | [**get_by_query_excel**](docs/SqlExecutionApi.md#get_by_query_excel) | **GET** /api/Sql/excel/{query} | GetByQueryExcel: Execute Sql from the url returning an Excel file
*SqlExecutionApi* | [**get_by_query_json**](docs/SqlExecutionApi.md#get_by_query_json) | **GET** /api/Sql/json/{query} | GetByQueryJson: Execute Sql from the url returning JSON
*SqlExecutionApi* | [**get_by_query_parquet**](docs/SqlExecutionApi.md#get_by_query_parquet) | **GET** /api/Sql/parquet/{query} | GetByQueryParquet: Execute Sql from the url returning a Parquet file
*SqlExecutionApi* | [**get_by_query_pipe**](docs/SqlExecutionApi.md#get_by_query_pipe) | **GET** /api/Sql/pipe/{query} | GetByQueryPipe: Execute Sql from the url returning pipe-delimited
*SqlExecutionApi* | [**get_by_query_sqlite**](docs/SqlExecutionApi.md#get_by_query_sqlite) | **GET** /api/Sql/sqlite/{query} | GetByQuerySqlite: Execute Sql from the url returning SqLite DB
*SqlExecutionApi* | [**get_by_query_xml**](docs/SqlExecutionApi.md#get_by_query_xml) | **GET** /api/Sql/xml/{query} | GetByQueryXml: Execute Sql from the url returning XML
*SqlExecutionApi* | [**put_by_query_csv**](docs/SqlExecutionApi.md#put_by_query_csv) | **PUT** /api/Sql/csv | PutByQueryCsv: Execute Sql from the body returning CSV
*SqlExecutionApi* | [**put_by_query_excel**](docs/SqlExecutionApi.md#put_by_query_excel) | **PUT** /api/Sql/excel | PutByQueryExcel: Execute Sql from the body making an Excel file
*SqlExecutionApi* | [**put_by_query_json**](docs/SqlExecutionApi.md#put_by_query_json) | **PUT** /api/Sql/json | PutByQueryJson: Execute Sql from the body returning JSON
*SqlExecutionApi* | [**put_by_query_parquet**](docs/SqlExecutionApi.md#put_by_query_parquet) | **PUT** /api/Sql/parquet | PutByQueryParquet: Execute Sql from the body making a Parquet file
*SqlExecutionApi* | [**put_by_query_pipe**](docs/SqlExecutionApi.md#put_by_query_pipe) | **PUT** /api/Sql/pipe | PutByQueryPipe: Execute Sql from the body making pipe-delimited
*SqlExecutionApi* | [**put_by_query_sqlite**](docs/SqlExecutionApi.md#put_by_query_sqlite) | **PUT** /api/Sql/sqlite | PutByQuerySqlite: Execute Sql from the body returning SqLite DB
*SqlExecutionApi* | [**put_by_query_xml**](docs/SqlExecutionApi.md#put_by_query_xml) | **PUT** /api/Sql/xml | PutByQueryXml: Execute Sql from the body returning XML


<a id="documentation-for-models"></a>
## Documentation for Models

 - [AccessControlledAction](docs/AccessControlledAction.md)
 - [AccessControlledResource](docs/AccessControlledResource.md)
 - [AccessControlledResourceIdentifierPartSchemaAttribute](docs/AccessControlledResourceIdentifierPartSchemaAttribute.md)
 - [ActionId](docs/ActionId.md)
 - [AggregateFunction](docs/AggregateFunction.md)
 - [Aggregation](docs/Aggregation.md)
 - [AutoDetectType](docs/AutoDetectType.md)
 - [AvailableField](docs/AvailableField.md)
 - [AvailableParameter](docs/AvailableParameter.md)
 - [BackgroundMultiQueryProgressResponse](docs/BackgroundMultiQueryProgressResponse.md)
 - [BackgroundMultiQueryResponse](docs/BackgroundMultiQueryResponse.md)
 - [BackgroundQueryCancelResponse](docs/BackgroundQueryCancelResponse.md)
 - [BackgroundQueryProgressResponse](docs/BackgroundQueryProgressResponse.md)
 - [BackgroundQueryResponse](docs/BackgroundQueryResponse.md)
 - [BackgroundQueryState](docs/BackgroundQueryState.md)
 - [CaseStatementDesign](docs/CaseStatementDesign.md)
 - [CaseStatementItem](docs/CaseStatementItem.md)
 - [CertificateAction](docs/CertificateAction.md)
 - [CertificateFileType](docs/CertificateFileType.md)
 - [CertificateState](docs/CertificateState.md)
 - [CertificateStatus](docs/CertificateStatus.md)
 - [CertificateType](docs/CertificateType.md)
 - [Column](docs/Column.md)
 - [ColumnInfo](docs/ColumnInfo.md)
 - [ColumnStateType](docs/ColumnStateType.md)
 - [ConditionAttributes](docs/ConditionAttributes.md)
 - [ConvertToViewData](docs/ConvertToViewData.md)
 - [CursorPosition](docs/CursorPosition.md)
 - [DashboardType](docs/DashboardType.md)
 - [DataType](docs/DataType.md)
 - [DateParameters](docs/DateParameters.md)
 - [ErrorHighlightItem](docs/ErrorHighlightItem.md)
 - [ErrorHighlightRequest](docs/ErrorHighlightRequest.md)
 - [ErrorHighlightResponse](docs/ErrorHighlightResponse.md)
 - [ExpressionWithAlias](docs/ExpressionWithAlias.md)
 - [FeedbackEventArgs](docs/FeedbackEventArgs.md)
 - [FeedbackLevel](docs/FeedbackLevel.md)
 - [FieldDesign](docs/FieldDesign.md)
 - [FieldType](docs/FieldType.md)
 - [FileReaderBuilderDef](docs/FileReaderBuilderDef.md)
 - [FileReaderBuilderResponse](docs/FileReaderBuilderResponse.md)
 - [FilterModel](docs/FilterModel.md)
 - [FilterTermDesign](docs/FilterTermDesign.md)
 - [FilterType](docs/FilterType.md)
 - [IdSelectorDefinition](docs/IdSelectorDefinition.md)
 - [InlinedPropertyDesign](docs/InlinedPropertyDesign.md)
 - [InlinedPropertyItem](docs/InlinedPropertyItem.md)
 - [IntellisenseItem](docs/IntellisenseItem.md)
 - [IntellisenseRequest](docs/IntellisenseRequest.md)
 - [IntellisenseResponse](docs/IntellisenseResponse.md)
 - [IntellisenseType](docs/IntellisenseType.md)
 - [Link](docs/Link.md)
 - [LuminesceBinaryType](docs/LuminesceBinaryType.md)
 - [LusidGridData](docs/LusidGridData.md)
 - [LusidProblemDetails](docs/LusidProblemDetails.md)
 - [MappableField](docs/MappableField.md)
 - [MappingFlags](docs/MappingFlags.md)
 - [MultiQueryDefinitionType](docs/MultiQueryDefinitionType.md)
 - [OptionsCsv](docs/OptionsCsv.md)
 - [OptionsExcel](docs/OptionsExcel.md)
 - [OptionsParquet](docs/OptionsParquet.md)
 - [OptionsSqLite](docs/OptionsSqLite.md)
 - [OptionsXml](docs/OptionsXml.md)
 - [OrderByDirection](docs/OrderByDirection.md)
 - [OrderByTermDesign](docs/OrderByTermDesign.md)
 - [QueryDesign](docs/QueryDesign.md)
 - [QueryDesignerBinaryOperator](docs/QueryDesignerBinaryOperator.md)
 - [ResourceId](docs/ResourceId.md)
 - [ResourceListOfAccessControlledResource](docs/ResourceListOfAccessControlledResource.md)
 - [ScalarParameter](docs/ScalarParameter.md)
 - [Source](docs/Source.md)
 - [SourceType](docs/SourceType.md)
 - [TableMeta](docs/TableMeta.md)
 - [TableView](docs/TableView.md)
 - [TaskStatus](docs/TaskStatus.md)
 - [Type](docs/Type.md)
 - [ViewParameter](docs/ViewParameter.md)
 - [WriterDesign](docs/WriterDesign.md)

