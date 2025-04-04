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
from pydantic.v1 import Field, StrictInt

from typing import Any, Dict, Optional


from luminesce.api_client import ApiClient
from luminesce.api_response import ApiResponse
from luminesce.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from luminesce.extensions.configuration_options import ConfigurationOptions

# ensure templated type usages are imported
from pydantic.v1 import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated

class HealthCheckingEndpointApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @overload
    async def fake_node_reclaim(self, seconds_until_reclaim : Annotated[Optional[StrictInt], Field(description="the number of seconds from which to assume node termination")] = None, **kwargs) -> object:  # noqa: E501
        ...

    @overload
    def fake_node_reclaim(self, seconds_until_reclaim : Annotated[Optional[StrictInt], Field(description="the number of seconds from which to assume node termination")] = None, async_req: Optional[bool]=True, **kwargs) -> object:  # noqa: E501
        ...

    @validate_arguments
    def fake_node_reclaim(self, seconds_until_reclaim : Annotated[Optional[StrictInt], Field(description="the number of seconds from which to assume node termination")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[object, Awaitable[object]]:  # noqa: E501
        """[INTERNAL] FakeNodeReclaim: Helps testing of AWS node reclaim behaviour  # noqa: E501

         An internal Method used to mark the next SIGTERM as though an Aws Node reclaim were about to take place. Simulates having received an AWS node reclaim warning, or similar.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fake_node_reclaim(seconds_until_reclaim, async_req=True)
        >>> result = thread.get()

        :param seconds_until_reclaim: the number of seconds from which to assume node termination
        :type seconds_until_reclaim: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the fake_node_reclaim_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.fake_node_reclaim_with_http_info(seconds_until_reclaim, **kwargs)  # noqa: E501

    @validate_arguments
    def fake_node_reclaim_with_http_info(self, seconds_until_reclaim : Annotated[Optional[StrictInt], Field(description="the number of seconds from which to assume node termination")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """[INTERNAL] FakeNodeReclaim: Helps testing of AWS node reclaim behaviour  # noqa: E501

         An internal Method used to mark the next SIGTERM as though an Aws Node reclaim were about to take place. Simulates having received an AWS node reclaim warning, or similar.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fake_node_reclaim_with_http_info(seconds_until_reclaim, async_req=True)
        >>> result = thread.get()

        :param seconds_until_reclaim: the number of seconds from which to assume node termination
        :type seconds_until_reclaim: int
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'seconds_until_reclaim'
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
                    " to method fake_node_reclaim" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('seconds_until_reclaim') is not None:  # noqa: E501
            _query_params.append(('secondsUntilReclaim', _params['seconds_until_reclaim']))

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
            '200': "object",
        }

        return self.api_client.call_api(
            '/fakeNodeReclaim', 'GET',
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
