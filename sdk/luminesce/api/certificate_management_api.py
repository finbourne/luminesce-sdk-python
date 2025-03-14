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

from pydantic.v1 import Field, StrictBool, StrictInt

from typing import List, Optional, Union

from luminesce.models.certificate_action import CertificateAction
from luminesce.models.certificate_file_type import CertificateFileType
from luminesce.models.certificate_state import CertificateState
from luminesce.models.certificate_type import CertificateType

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

class CertificateManagementApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @overload
    async def download_certificate(self, type : Annotated[Optional[str], Field( description="User or Domain level cert (Domain level requires additional entitlements)")] = None, file_type : Annotated[Optional[str], Field( description="Should the public key or private key be downloaded? (both must be in place to run providers)")] = None, may_auto_create : Annotated[Optional[StrictBool], Field(description="If no matching cert is available, should an attempt be made to Create/Renew it with default options?")] = None, **kwargs) -> bytearray:  # noqa: E501
        ...

    @overload
    def download_certificate(self, type : Annotated[Optional[str], Field( description="User or Domain level cert (Domain level requires additional entitlements)")] = None, file_type : Annotated[Optional[str], Field( description="Should the public key or private key be downloaded? (both must be in place to run providers)")] = None, may_auto_create : Annotated[Optional[StrictBool], Field(description="If no matching cert is available, should an attempt be made to Create/Renew it with default options?")] = None, async_req: Optional[bool]=True, **kwargs) -> bytearray:  # noqa: E501
        ...

    @validate_arguments
    def download_certificate(self, type : Annotated[Optional[str], Field( description="User or Domain level cert (Domain level requires additional entitlements)")] = None, file_type : Annotated[Optional[str], Field( description="Should the public key or private key be downloaded? (both must be in place to run providers)")] = None, may_auto_create : Annotated[Optional[StrictBool], Field(description="If no matching cert is available, should an attempt be made to Create/Renew it with default options?")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[bytearray, Awaitable[bytearray]]:  # noqa: E501
        """DownloadCertificate: Download domain or your personal certificates  # noqa: E501

         Downloads your latest Domain or your User certificate's public or private key - if any.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - certificate is not available for some reason - 401 Unauthorized - 403 Forbidden   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_certificate(type, file_type, may_auto_create, async_req=True)
        >>> result = thread.get()

        :param type: User or Domain level cert (Domain level requires additional entitlements)
        :type type: CertificateType
        :param file_type: Should the public key or private key be downloaded? (both must be in place to run providers)
        :type file_type: CertificateFileType
        :param may_auto_create: If no matching cert is available, should an attempt be made to Create/Renew it with default options?
        :type may_auto_create: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: bytearray
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the download_certificate_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.download_certificate_with_http_info(type, file_type, may_auto_create, **kwargs)  # noqa: E501

    @validate_arguments
    def download_certificate_with_http_info(self, type : Annotated[Optional[str], Field( description="User or Domain level cert (Domain level requires additional entitlements)")] = None, file_type : Annotated[Optional[str], Field( description="Should the public key or private key be downloaded? (both must be in place to run providers)")] = None, may_auto_create : Annotated[Optional[StrictBool], Field(description="If no matching cert is available, should an attempt be made to Create/Renew it with default options?")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """DownloadCertificate: Download domain or your personal certificates  # noqa: E501

         Downloads your latest Domain or your User certificate's public or private key - if any.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - certificate is not available for some reason - 401 Unauthorized - 403 Forbidden   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_certificate_with_http_info(type, file_type, may_auto_create, async_req=True)
        >>> result = thread.get()

        :param type: User or Domain level cert (Domain level requires additional entitlements)
        :type type: CertificateType
        :param file_type: Should the public key or private key be downloaded? (both must be in place to run providers)
        :type file_type: CertificateFileType
        :param may_auto_create: If no matching cert is available, should an attempt be made to Create/Renew it with default options?
        :type may_auto_create: bool
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
        :rtype: tuple(bytearray, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'type',
            'file_type',
            'may_auto_create'
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
                    " to method download_certificate" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('type') is not None:  # noqa: E501
            _query_params.append(('type', _params['type']))

        if _params.get('file_type') is not None:  # noqa: E501
            _query_params.append(('fileType', _params['file_type']))

        if _params.get('may_auto_create') is not None:  # noqa: E501
            _query_params.append(('mayAutoCreate', _params['may_auto_create']))

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
            '200': "bytearray",
            '400': "LusidProblemDetails",
            '403': "LusidProblemDetails",
        }

        return self.api_client.call_api(
            '/api/Certificate/certificate', 'GET',
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
    async def list_certificates(self, **kwargs) -> List[CertificateState]:  # noqa: E501
        ...

    @overload
    def list_certificates(self, async_req: Optional[bool]=True, **kwargs) -> List[CertificateState]:  # noqa: E501
        ...

    @validate_arguments
    def list_certificates(self, async_req: Optional[bool]=None, **kwargs) -> Union[List[CertificateState], Awaitable[List[CertificateState]]]:  # noqa: E501
        """ListCertificates: List previously minted certificates  # noqa: E501

         Lists all the certificates previously minted to which you have access.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_certificates(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[CertificateState]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_certificates_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.list_certificates_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def list_certificates_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """ListCertificates: List previously minted certificates  # noqa: E501

         Lists all the certificates previously minted to which you have access.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_certificates_with_http_info(async_req=True)
        >>> result = thread.get()

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
        :rtype: tuple(List[CertificateState], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
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
                    " to method list_certificates" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

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
            '200': "List[CertificateState]",
            '400': "LusidProblemDetails",
            '403': "LusidProblemDetails",
        }

        return self.api_client.call_api(
            '/api/Certificate/certificates', 'GET',
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
    async def manage_certificate(self, action : Annotated[Optional[str], Field( description="The Action to perform, e.g. Create / Renew / Revoke")] = None, type : Annotated[Optional[str], Field( description="User or Domain level cert (Domain level requires additional entitlements)")] = None, version : Annotated[Optional[StrictInt], Field(description="Version number of the cert, the request will fail to validate if incorrect")] = None, validity_start : Annotated[Optional[datetime], Field(description="When should the cert first be valid (defaults to the current time in UTC)")] = None, validity_end : Annotated[Optional[datetime], Field(description="When should the cert no longer be valid (defaults to 13 months from now)")] = None, dry_run : Annotated[Optional[StrictBool], Field(description="True will just validate the request, but perform no changes to any system")] = None, **kwargs) -> CertificateState:  # noqa: E501
        ...

    @overload
    def manage_certificate(self, action : Annotated[Optional[str], Field( description="The Action to perform, e.g. Create / Renew / Revoke")] = None, type : Annotated[Optional[str], Field( description="User or Domain level cert (Domain level requires additional entitlements)")] = None, version : Annotated[Optional[StrictInt], Field(description="Version number of the cert, the request will fail to validate if incorrect")] = None, validity_start : Annotated[Optional[datetime], Field(description="When should the cert first be valid (defaults to the current time in UTC)")] = None, validity_end : Annotated[Optional[datetime], Field(description="When should the cert no longer be valid (defaults to 13 months from now)")] = None, dry_run : Annotated[Optional[StrictBool], Field(description="True will just validate the request, but perform no changes to any system")] = None, async_req: Optional[bool]=True, **kwargs) -> CertificateState:  # noqa: E501
        ...

    @validate_arguments
    def manage_certificate(self, action : Annotated[Optional[str], Field( description="The Action to perform, e.g. Create / Renew / Revoke")] = None, type : Annotated[Optional[str], Field( description="User or Domain level cert (Domain level requires additional entitlements)")] = None, version : Annotated[Optional[StrictInt], Field(description="Version number of the cert, the request will fail to validate if incorrect")] = None, validity_start : Annotated[Optional[datetime], Field(description="When should the cert first be valid (defaults to the current time in UTC)")] = None, validity_end : Annotated[Optional[datetime], Field(description="When should the cert no longer be valid (defaults to 13 months from now)")] = None, dry_run : Annotated[Optional[StrictBool], Field(description="True will just validate the request, but perform no changes to any system")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[CertificateState, Awaitable[CertificateState]]:  # noqa: E501
        """ManageCertificate: Create / Renew / Revoke a certificate  # noqa: E501

         Manages a certificate.  This could be creating a new one, renewing an old one or revoking one explicitly.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something about the request cannot be processed - 401 Unauthorized - 403 Forbidden   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.manage_certificate(action, type, version, validity_start, validity_end, dry_run, async_req=True)
        >>> result = thread.get()

        :param action: The Action to perform, e.g. Create / Renew / Revoke
        :type action: CertificateAction
        :param type: User or Domain level cert (Domain level requires additional entitlements)
        :type type: CertificateType
        :param version: Version number of the cert, the request will fail to validate if incorrect
        :type version: int
        :param validity_start: When should the cert first be valid (defaults to the current time in UTC)
        :type validity_start: datetime
        :param validity_end: When should the cert no longer be valid (defaults to 13 months from now)
        :type validity_end: datetime
        :param dry_run: True will just validate the request, but perform no changes to any system
        :type dry_run: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CertificateState
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the manage_certificate_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.manage_certificate_with_http_info(action, type, version, validity_start, validity_end, dry_run, **kwargs)  # noqa: E501

    @validate_arguments
    def manage_certificate_with_http_info(self, action : Annotated[Optional[str], Field( description="The Action to perform, e.g. Create / Renew / Revoke")] = None, type : Annotated[Optional[str], Field( description="User or Domain level cert (Domain level requires additional entitlements)")] = None, version : Annotated[Optional[StrictInt], Field(description="Version number of the cert, the request will fail to validate if incorrect")] = None, validity_start : Annotated[Optional[datetime], Field(description="When should the cert first be valid (defaults to the current time in UTC)")] = None, validity_end : Annotated[Optional[datetime], Field(description="When should the cert no longer be valid (defaults to 13 months from now)")] = None, dry_run : Annotated[Optional[StrictBool], Field(description="True will just validate the request, but perform no changes to any system")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """ManageCertificate: Create / Renew / Revoke a certificate  # noqa: E501

         Manages a certificate.  This could be creating a new one, renewing an old one or revoking one explicitly.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something about the request cannot be processed - 401 Unauthorized - 403 Forbidden   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.manage_certificate_with_http_info(action, type, version, validity_start, validity_end, dry_run, async_req=True)
        >>> result = thread.get()

        :param action: The Action to perform, e.g. Create / Renew / Revoke
        :type action: CertificateAction
        :param type: User or Domain level cert (Domain level requires additional entitlements)
        :type type: CertificateType
        :param version: Version number of the cert, the request will fail to validate if incorrect
        :type version: int
        :param validity_start: When should the cert first be valid (defaults to the current time in UTC)
        :type validity_start: datetime
        :param validity_end: When should the cert no longer be valid (defaults to 13 months from now)
        :type validity_end: datetime
        :param dry_run: True will just validate the request, but perform no changes to any system
        :type dry_run: bool
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
        :rtype: tuple(CertificateState, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'action',
            'type',
            'version',
            'validity_start',
            'validity_end',
            'dry_run'
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
                    " to method manage_certificate" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('action') is not None:  # noqa: E501
            _query_params.append(('action', _params['action']))

        if _params.get('type') is not None:  # noqa: E501
            _query_params.append(('type', _params['type']))

        if _params.get('version') is not None:  # noqa: E501
            _query_params.append(('version', _params['version']))

        if _params.get('validity_start') is not None:  # noqa: E501
            if isinstance(_params['validity_start'], datetime):
                _query_params.append(('validityStart', _params['validity_start'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('validityStart', _params['validity_start']))

        if _params.get('validity_end') is not None:  # noqa: E501
            if isinstance(_params['validity_end'], datetime):
                _query_params.append(('validityEnd', _params['validity_end'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('validityEnd', _params['validity_end']))

        if _params.get('dry_run') is not None:  # noqa: E501
            _query_params.append(('dryRun', _params['dry_run']))

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
            '200': "CertificateState",
            '400': "LusidProblemDetails",
            '403': "LusidProblemDetails",
        }

        return self.api_client.call_api(
            '/api/Certificate/manage', 'PUT',
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
