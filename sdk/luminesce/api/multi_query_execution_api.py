# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic.v1 import validate_arguments, ValidationError
from typing import overload, Optional, Union, Awaitable

from typing_extensions import Annotated
from datetime import datetime

from pydantic.v1 import Field, StrictInt, StrictStr

from typing import Optional

from luminesce.models.background_multi_query_progress_response import BackgroundMultiQueryProgressResponse
from luminesce.models.background_multi_query_response import BackgroundMultiQueryResponse
from luminesce.models.background_query_cancel_response import BackgroundQueryCancelResponse
from luminesce.models.multi_query_definition_type import MultiQueryDefinitionType

from luminesce.api_client import ApiClient
from luminesce.api_response import ApiResponse
from luminesce.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from luminesce.extensions.configuration_options import ConfigurationOptions


class MultiQueryExecutionApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def cancel_multi_query(self, execution_id : Annotated[StrictStr, Field(..., description="ExecutionId returned when starting the query")], **kwargs) -> BackgroundQueryCancelResponse:  # noqa: E501
        ...

    @overload
    def cancel_multi_query(self, execution_id : Annotated[StrictStr, Field(..., description="ExecutionId returned when starting the query")], async_req: Optional[bool]=True, **kwargs) -> BackgroundQueryCancelResponse:  # noqa: E501
        ...

    @validate_arguments
    def cancel_multi_query(self, execution_id : Annotated[StrictStr, Field(..., description="ExecutionId returned when starting the query")], async_req: Optional[bool]=None, **kwargs) -> Union[BackgroundQueryCancelResponse, Awaitable[BackgroundQueryCancelResponse]]:  # noqa: E501
        """CancelMultiQuery: Cancel / Clear a previously started query-set  # noqa: E501

        Cancel the query-set (if still running) / clear the data (if already returned) The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't exist and is not running.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cancel_multi_query(execution_id, async_req=True)
        >>> result = thread.get()

        :param execution_id: ExecutionId returned when starting the query (required)
        :type execution_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: BackgroundQueryCancelResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the cancel_multi_query_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.cancel_multi_query_with_http_info(execution_id, **kwargs)  # noqa: E501

    @validate_arguments
    def cancel_multi_query_with_http_info(self, execution_id : Annotated[StrictStr, Field(..., description="ExecutionId returned when starting the query")], **kwargs) -> ApiResponse:  # noqa: E501
        """CancelMultiQuery: Cancel / Clear a previously started query-set  # noqa: E501

        Cancel the query-set (if still running) / clear the data (if already returned) The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't exist and is not running.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cancel_multi_query_with_http_info(execution_id, async_req=True)
        >>> result = thread.get()

        :param execution_id: ExecutionId returned when starting the query (required)
        :type execution_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(BackgroundQueryCancelResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'execution_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_multi_query" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['execution_id']:
            _path_params['executionId'] = _params['execution_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "BackgroundQueryCancelResponse",
        }

        return self.api_client.call_api(
            '/api/MultiQueryBackground/{executionId}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def get_progress_of_multi_query(self, execution_id : Annotated[StrictStr, Field(..., description="ExecutionId returned when starting the query")], **kwargs) -> BackgroundMultiQueryProgressResponse:  # noqa: E501
        ...

    @overload
    def get_progress_of_multi_query(self, execution_id : Annotated[StrictStr, Field(..., description="ExecutionId returned when starting the query")], async_req: Optional[bool]=True, **kwargs) -> BackgroundMultiQueryProgressResponse:  # noqa: E501
        ...

    @validate_arguments
    def get_progress_of_multi_query(self, execution_id : Annotated[StrictStr, Field(..., description="ExecutionId returned when starting the query")], async_req: Optional[bool]=None, **kwargs) -> Union[BackgroundMultiQueryProgressResponse, Awaitable[BackgroundMultiQueryProgressResponse]]:  # noqa: E501
        """GetProgressOfMultiQuery: View progress of the entire query-set load  # noqa: E501

        View progress information (up until this point) for the entire query-set The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't exist and is not running. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_progress_of_multi_query(execution_id, async_req=True)
        >>> result = thread.get()

        :param execution_id: ExecutionId returned when starting the query (required)
        :type execution_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: BackgroundMultiQueryProgressResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_progress_of_multi_query_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_progress_of_multi_query_with_http_info(execution_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_progress_of_multi_query_with_http_info(self, execution_id : Annotated[StrictStr, Field(..., description="ExecutionId returned when starting the query")], **kwargs) -> ApiResponse:  # noqa: E501
        """GetProgressOfMultiQuery: View progress of the entire query-set load  # noqa: E501

        View progress information (up until this point) for the entire query-set The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't exist and is not running. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_progress_of_multi_query_with_http_info(execution_id, async_req=True)
        >>> result = thread.get()

        :param execution_id: ExecutionId returned when starting the query (required)
        :type execution_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(BackgroundMultiQueryProgressResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'execution_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_progress_of_multi_query" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['execution_id']:
            _path_params['executionId'] = _params['execution_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "BackgroundMultiQueryProgressResponse",
        }

        return self.api_client.call_api(
            '/api/MultiQueryBackground/{executionId}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def start_queries(self, type : Annotated[MultiQueryDefinitionType, Field(..., description="An enum value defining the set of statements being executed")], body : Annotated[StrictStr, Field(..., description="A \"search\" value (e.g. 'Apple' on an instrument search, a `Finbourne.Filtering` expression of Insights, etc.)  In the cases where \"Nothing\" is valid for a `Finbourne.Filtering` expression, pass `True`.")], as_at : Annotated[Optional[datetime], Field(description="The AsAt time used by any bitemporal provider in the queries.")] = None, effective_at : Annotated[Optional[datetime], Field(description="The EffectiveAt time used by any bitemporal provider in the queries.")] = None, limit1 : Annotated[Optional[StrictInt], Field(description="A limit that is applied to first-level queries (e.g. Instruments themselves)")] = None, limit2 : Annotated[Optional[StrictInt], Field(description="A limit that is applied to second-level queries (e.g. Holdings based on the set of Instruments found)")] = None, input1 : Annotated[Optional[StrictStr], Field(description="A value available to queries, these vary by 'type' and are only used by some types at all.  e.g. a start-date of some sort")] = None, input2 : Annotated[Optional[StrictStr], Field(description="A second value available to queries, these vary by 'type' and are only used by some types at all.")] = None, input3 : Annotated[Optional[StrictStr], Field(description="A third value available to queries, these vary by 'type' and are only used by some types at all.")] = None, timeout_seconds : Annotated[Optional[StrictInt], Field(description="Maximum time the query may run for, in seconds: <0 → ∞, 0 → 1200s (20m)")] = None, keep_for_seconds : Annotated[Optional[StrictInt], Field(description="Maximum time the result may be kept for, in seconds: <0 → 1200 (20m), 0 → 28800 (8h), max = 2,678,400 (31d)")] = None, **kwargs) -> BackgroundMultiQueryResponse:  # noqa: E501
        ...

    @overload
    def start_queries(self, type : Annotated[MultiQueryDefinitionType, Field(..., description="An enum value defining the set of statements being executed")], body : Annotated[StrictStr, Field(..., description="A \"search\" value (e.g. 'Apple' on an instrument search, a `Finbourne.Filtering` expression of Insights, etc.)  In the cases where \"Nothing\" is valid for a `Finbourne.Filtering` expression, pass `True`.")], as_at : Annotated[Optional[datetime], Field(description="The AsAt time used by any bitemporal provider in the queries.")] = None, effective_at : Annotated[Optional[datetime], Field(description="The EffectiveAt time used by any bitemporal provider in the queries.")] = None, limit1 : Annotated[Optional[StrictInt], Field(description="A limit that is applied to first-level queries (e.g. Instruments themselves)")] = None, limit2 : Annotated[Optional[StrictInt], Field(description="A limit that is applied to second-level queries (e.g. Holdings based on the set of Instruments found)")] = None, input1 : Annotated[Optional[StrictStr], Field(description="A value available to queries, these vary by 'type' and are only used by some types at all.  e.g. a start-date of some sort")] = None, input2 : Annotated[Optional[StrictStr], Field(description="A second value available to queries, these vary by 'type' and are only used by some types at all.")] = None, input3 : Annotated[Optional[StrictStr], Field(description="A third value available to queries, these vary by 'type' and are only used by some types at all.")] = None, timeout_seconds : Annotated[Optional[StrictInt], Field(description="Maximum time the query may run for, in seconds: <0 → ∞, 0 → 1200s (20m)")] = None, keep_for_seconds : Annotated[Optional[StrictInt], Field(description="Maximum time the result may be kept for, in seconds: <0 → 1200 (20m), 0 → 28800 (8h), max = 2,678,400 (31d)")] = None, async_req: Optional[bool]=True, **kwargs) -> BackgroundMultiQueryResponse:  # noqa: E501
        ...

    @validate_arguments
    def start_queries(self, type : Annotated[MultiQueryDefinitionType, Field(..., description="An enum value defining the set of statements being executed")], body : Annotated[StrictStr, Field(..., description="A \"search\" value (e.g. 'Apple' on an instrument search, a `Finbourne.Filtering` expression of Insights, etc.)  In the cases where \"Nothing\" is valid for a `Finbourne.Filtering` expression, pass `True`.")], as_at : Annotated[Optional[datetime], Field(description="The AsAt time used by any bitemporal provider in the queries.")] = None, effective_at : Annotated[Optional[datetime], Field(description="The EffectiveAt time used by any bitemporal provider in the queries.")] = None, limit1 : Annotated[Optional[StrictInt], Field(description="A limit that is applied to first-level queries (e.g. Instruments themselves)")] = None, limit2 : Annotated[Optional[StrictInt], Field(description="A limit that is applied to second-level queries (e.g. Holdings based on the set of Instruments found)")] = None, input1 : Annotated[Optional[StrictStr], Field(description="A value available to queries, these vary by 'type' and are only used by some types at all.  e.g. a start-date of some sort")] = None, input2 : Annotated[Optional[StrictStr], Field(description="A second value available to queries, these vary by 'type' and are only used by some types at all.")] = None, input3 : Annotated[Optional[StrictStr], Field(description="A third value available to queries, these vary by 'type' and are only used by some types at all.")] = None, timeout_seconds : Annotated[Optional[StrictInt], Field(description="Maximum time the query may run for, in seconds: <0 → ∞, 0 → 1200s (20m)")] = None, keep_for_seconds : Annotated[Optional[StrictInt], Field(description="Maximum time the result may be kept for, in seconds: <0 → 1200 (20m), 0 → 28800 (8h), max = 2,678,400 (31d)")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[BackgroundMultiQueryResponse, Awaitable[BackgroundMultiQueryResponse]]:  # noqa: E501
        """StartQueries: Run a given set of Sql queries in the background  # noqa: E501

         Allow for starting a potentially long running query and getting back an immediate response with how to  - fetch the data in various formats (if available, or if not simply being informed it is not yet ready), on a per result basis - view progress information (up until this point), for all results in one go - cancel the queries (if still running) / clear the data (if already returned)  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - there was something wrong with your query syntax (the issue was detected at parse-time) - 401 Unauthorized - 403 Forbidden   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.start_queries(type, body, as_at, effective_at, limit1, limit2, input1, input2, input3, timeout_seconds, keep_for_seconds, async_req=True)
        >>> result = thread.get()

        :param type: An enum value defining the set of statements being executed (required)
        :type type: MultiQueryDefinitionType
        :param body: A \"search\" value (e.g. 'Apple' on an instrument search, a `Finbourne.Filtering` expression of Insights, etc.)  In the cases where \"Nothing\" is valid for a `Finbourne.Filtering` expression, pass `True`. (required)
        :type body: str
        :param as_at: The AsAt time used by any bitemporal provider in the queries.
        :type as_at: datetime
        :param effective_at: The EffectiveAt time used by any bitemporal provider in the queries.
        :type effective_at: datetime
        :param limit1: A limit that is applied to first-level queries (e.g. Instruments themselves)
        :type limit1: int
        :param limit2: A limit that is applied to second-level queries (e.g. Holdings based on the set of Instruments found)
        :type limit2: int
        :param input1: A value available to queries, these vary by 'type' and are only used by some types at all.  e.g. a start-date of some sort
        :type input1: str
        :param input2: A second value available to queries, these vary by 'type' and are only used by some types at all.
        :type input2: str
        :param input3: A third value available to queries, these vary by 'type' and are only used by some types at all.
        :type input3: str
        :param timeout_seconds: Maximum time the query may run for, in seconds: <0 → ∞, 0 → 1200s (20m)
        :type timeout_seconds: int
        :param keep_for_seconds: Maximum time the result may be kept for, in seconds: <0 → 1200 (20m), 0 → 28800 (8h), max = 2,678,400 (31d)
        :type keep_for_seconds: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: BackgroundMultiQueryResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the start_queries_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.start_queries_with_http_info(type, body, as_at, effective_at, limit1, limit2, input1, input2, input3, timeout_seconds, keep_for_seconds, **kwargs)  # noqa: E501

    @validate_arguments
    def start_queries_with_http_info(self, type : Annotated[MultiQueryDefinitionType, Field(..., description="An enum value defining the set of statements being executed")], body : Annotated[StrictStr, Field(..., description="A \"search\" value (e.g. 'Apple' on an instrument search, a `Finbourne.Filtering` expression of Insights, etc.)  In the cases where \"Nothing\" is valid for a `Finbourne.Filtering` expression, pass `True`.")], as_at : Annotated[Optional[datetime], Field(description="The AsAt time used by any bitemporal provider in the queries.")] = None, effective_at : Annotated[Optional[datetime], Field(description="The EffectiveAt time used by any bitemporal provider in the queries.")] = None, limit1 : Annotated[Optional[StrictInt], Field(description="A limit that is applied to first-level queries (e.g. Instruments themselves)")] = None, limit2 : Annotated[Optional[StrictInt], Field(description="A limit that is applied to second-level queries (e.g. Holdings based on the set of Instruments found)")] = None, input1 : Annotated[Optional[StrictStr], Field(description="A value available to queries, these vary by 'type' and are only used by some types at all.  e.g. a start-date of some sort")] = None, input2 : Annotated[Optional[StrictStr], Field(description="A second value available to queries, these vary by 'type' and are only used by some types at all.")] = None, input3 : Annotated[Optional[StrictStr], Field(description="A third value available to queries, these vary by 'type' and are only used by some types at all.")] = None, timeout_seconds : Annotated[Optional[StrictInt], Field(description="Maximum time the query may run for, in seconds: <0 → ∞, 0 → 1200s (20m)")] = None, keep_for_seconds : Annotated[Optional[StrictInt], Field(description="Maximum time the result may be kept for, in seconds: <0 → 1200 (20m), 0 → 28800 (8h), max = 2,678,400 (31d)")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """StartQueries: Run a given set of Sql queries in the background  # noqa: E501

         Allow for starting a potentially long running query and getting back an immediate response with how to  - fetch the data in various formats (if available, or if not simply being informed it is not yet ready), on a per result basis - view progress information (up until this point), for all results in one go - cancel the queries (if still running) / clear the data (if already returned)  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - there was something wrong with your query syntax (the issue was detected at parse-time) - 401 Unauthorized - 403 Forbidden   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.start_queries_with_http_info(type, body, as_at, effective_at, limit1, limit2, input1, input2, input3, timeout_seconds, keep_for_seconds, async_req=True)
        >>> result = thread.get()

        :param type: An enum value defining the set of statements being executed (required)
        :type type: MultiQueryDefinitionType
        :param body: A \"search\" value (e.g. 'Apple' on an instrument search, a `Finbourne.Filtering` expression of Insights, etc.)  In the cases where \"Nothing\" is valid for a `Finbourne.Filtering` expression, pass `True`. (required)
        :type body: str
        :param as_at: The AsAt time used by any bitemporal provider in the queries.
        :type as_at: datetime
        :param effective_at: The EffectiveAt time used by any bitemporal provider in the queries.
        :type effective_at: datetime
        :param limit1: A limit that is applied to first-level queries (e.g. Instruments themselves)
        :type limit1: int
        :param limit2: A limit that is applied to second-level queries (e.g. Holdings based on the set of Instruments found)
        :type limit2: int
        :param input1: A value available to queries, these vary by 'type' and are only used by some types at all.  e.g. a start-date of some sort
        :type input1: str
        :param input2: A second value available to queries, these vary by 'type' and are only used by some types at all.
        :type input2: str
        :param input3: A third value available to queries, these vary by 'type' and are only used by some types at all.
        :type input3: str
        :param timeout_seconds: Maximum time the query may run for, in seconds: <0 → ∞, 0 → 1200s (20m)
        :type timeout_seconds: int
        :param keep_for_seconds: Maximum time the result may be kept for, in seconds: <0 → 1200 (20m), 0 → 28800 (8h), max = 2,678,400 (31d)
        :type keep_for_seconds: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(BackgroundMultiQueryResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'type',
            'body',
            'as_at',
            'effective_at',
            'limit1',
            'limit2',
            'input1',
            'input2',
            'input3',
            'timeout_seconds',
            'keep_for_seconds'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_queries" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('type') is not None:  # noqa: E501
            _query_params.append(('type', _params['type'].value))

        if _params.get('as_at') is not None:  # noqa: E501
            if isinstance(_params['as_at'], datetime):
                _query_params.append(('asAt', _params['as_at'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('asAt', _params['as_at']))

        if _params.get('effective_at') is not None:  # noqa: E501
            if isinstance(_params['effective_at'], datetime):
                _query_params.append(('effectiveAt', _params['effective_at'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('effectiveAt', _params['effective_at']))

        if _params.get('limit1') is not None:  # noqa: E501
            _query_params.append(('limit1', _params['limit1']))

        if _params.get('limit2') is not None:  # noqa: E501
            _query_params.append(('limit2', _params['limit2']))

        if _params.get('input1') is not None:  # noqa: E501
            _query_params.append(('input1', _params['input1']))

        if _params.get('input2') is not None:  # noqa: E501
            _query_params.append(('input2', _params['input2']))

        if _params.get('input3') is not None:  # noqa: E501
            _query_params.append(('input3', _params['input3']))

        if _params.get('timeout_seconds') is not None:  # noqa: E501
            _query_params.append(('timeoutSeconds', _params['timeout_seconds']))

        if _params.get('keep_for_seconds') is not None:  # noqa: E501
            _query_params.append(('keepForSeconds', _params['keep_for_seconds']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['body'] is not None:
            _body_params = _params['body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['text/plain']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '202': "BackgroundMultiQueryResponse",
            '400': "LusidProblemDetails",
            '403': "LusidProblemDetails",
        }

        return self.api_client.call_api(
            '/api/MultiQueryBackground', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
