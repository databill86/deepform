# coding: utf-8

"""
    OPIF Service Data API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def service_type_applications_facility_entity_id_format_get(self, service_type, entity_id, format, **kwargs):  # noqa: E501
        """Entity Applications  # noqa: E501

        Entity Applications  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_type_applications_facility_entity_id_format_get(service_type, entity_id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: serviceType.<br /><br />Valid values: tv, fm, am (required)
        :param str entity_id: Entity ID (required)
        :param str format: json,  xml (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_type_applications_facility_entity_id_format_get_with_http_info(service_type, entity_id, format, **kwargs)  # noqa: E501
        else:
            (data) = self.service_type_applications_facility_entity_id_format_get_with_http_info(service_type, entity_id, format, **kwargs)  # noqa: E501
            return data

    def service_type_applications_facility_entity_id_format_get_with_http_info(self, service_type, entity_id, format, **kwargs):  # noqa: E501
        """Entity Applications  # noqa: E501

        Entity Applications  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_type_applications_facility_entity_id_format_get_with_http_info(service_type, entity_id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: serviceType.<br /><br />Valid values: tv, fm, am (required)
        :param str entity_id: Entity ID (required)
        :param str format: json,  xml (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['service_type', 'entity_id', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_type_applications_facility_entity_id_format_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'service_type' is set
        if ('service_type' not in params or
                params['service_type'] is None):
            raise ValueError("Missing the required parameter `service_type` when calling `service_type_applications_facility_entity_id_format_get`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `service_type_applications_facility_entity_id_format_get`")  # noqa: E501
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `service_type_applications_facility_entity_id_format_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service_type' in params:
            path_params['serviceType'] = params['service_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityID'] = params['entity_id']  # noqa: E501
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{serviceType}/applications/facility/{entityID}.{format}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_type_eeo_facilityid_entity_id_format_get(self, service_type, entity_id, format, **kwargs):  # noqa: E501
        """Entity EEO  # noqa: E501

        Entity EEO  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_type_eeo_facilityid_entity_id_format_get(service_type, entity_id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: serviceType.<br /><br />Valid values: tv, fm, am (required)
        :param str entity_id: Entity ID (required)
        :param str format: json,  xml (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_type_eeo_facilityid_entity_id_format_get_with_http_info(service_type, entity_id, format, **kwargs)  # noqa: E501
        else:
            (data) = self.service_type_eeo_facilityid_entity_id_format_get_with_http_info(service_type, entity_id, format, **kwargs)  # noqa: E501
            return data

    def service_type_eeo_facilityid_entity_id_format_get_with_http_info(self, service_type, entity_id, format, **kwargs):  # noqa: E501
        """Entity EEO  # noqa: E501

        Entity EEO  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_type_eeo_facilityid_entity_id_format_get_with_http_info(service_type, entity_id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: serviceType.<br /><br />Valid values: tv, fm, am (required)
        :param str entity_id: Entity ID (required)
        :param str format: json,  xml (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['service_type', 'entity_id', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_type_eeo_facilityid_entity_id_format_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'service_type' is set
        if ('service_type' not in params or
                params['service_type'] is None):
            raise ValueError("Missing the required parameter `service_type` when calling `service_type_eeo_facilityid_entity_id_format_get`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `service_type_eeo_facilityid_entity_id_format_get`")  # noqa: E501
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `service_type_eeo_facilityid_entity_id_format_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service_type' in params:
            path_params['serviceType'] = params['service_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityID'] = params['entity_id']  # noqa: E501
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{serviceType}/eeo/facilityid/{entityID}.{format}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_type_facility_getall_format_get(self, service_type, format, **kwargs):  # noqa: E501
        """Get All  # noqa: E501

        Get All  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_type_facility_getall_format_get(service_type, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: serviceType.<br /><br />Valid values: tv, fm and am (required)
        :param str format: json,  xml (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_type_facility_getall_format_get_with_http_info(service_type, format, **kwargs)  # noqa: E501
        else:
            (data) = self.service_type_facility_getall_format_get_with_http_info(service_type, format, **kwargs)  # noqa: E501
            return data

    def service_type_facility_getall_format_get_with_http_info(self, service_type, format, **kwargs):  # noqa: E501
        """Get All  # noqa: E501

        Get All  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_type_facility_getall_format_get_with_http_info(service_type, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: serviceType.<br /><br />Valid values: tv, fm and am (required)
        :param str format: json,  xml (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['service_type', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_type_facility_getall_format_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'service_type' is set
        if ('service_type' not in params or
                params['service_type'] is None):
            raise ValueError("Missing the required parameter `service_type` when calling `service_type_facility_getall_format_get`")  # noqa: E501
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `service_type_facility_getall_format_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service_type' in params:
            path_params['serviceType'] = params['service_type']  # noqa: E501
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{serviceType}/facility/getall.{format}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_type_facility_id_entity_id_format_get(self, service_type, entity_id, format, **kwargs):  # noqa: E501
        """Entity Details  # noqa: E501

        Entity Details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_type_facility_id_entity_id_format_get(service_type, entity_id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: serviceType.<br /><br />Valid values: tv, fm, am (required)
        :param str entity_id: Entity ID (required)
        :param str format: json,  xml (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_type_facility_id_entity_id_format_get_with_http_info(service_type, entity_id, format, **kwargs)  # noqa: E501
        else:
            (data) = self.service_type_facility_id_entity_id_format_get_with_http_info(service_type, entity_id, format, **kwargs)  # noqa: E501
            return data

    def service_type_facility_id_entity_id_format_get_with_http_info(self, service_type, entity_id, format, **kwargs):  # noqa: E501
        """Entity Details  # noqa: E501

        Entity Details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_type_facility_id_entity_id_format_get_with_http_info(service_type, entity_id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: serviceType.<br /><br />Valid values: tv, fm, am (required)
        :param str entity_id: Entity ID (required)
        :param str format: json,  xml (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['service_type', 'entity_id', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_type_facility_id_entity_id_format_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'service_type' is set
        if ('service_type' not in params or
                params['service_type'] is None):
            raise ValueError("Missing the required parameter `service_type` when calling `service_type_facility_id_entity_id_format_get`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `service_type_facility_id_entity_id_format_get`")  # noqa: E501
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `service_type_facility_id_entity_id_format_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service_type' in params:
            path_params['serviceType'] = params['service_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityID'] = params['entity_id']  # noqa: E501
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{serviceType}/facility/id/{entityID}.{format}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_type_ownership_facilityid_entity_id_format_get(self, service_type, entity_id, format, **kwargs):  # noqa: E501
        """Entity Ownership  # noqa: E501

        Entity Ownership  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_type_ownership_facilityid_entity_id_format_get(service_type, entity_id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: serviceType.<br /><br />Valid values: tv, fm, am (required)
        :param str entity_id: Entity ID (required)
        :param str format: json,  xml (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_type_ownership_facilityid_entity_id_format_get_with_http_info(service_type, entity_id, format, **kwargs)  # noqa: E501
        else:
            (data) = self.service_type_ownership_facilityid_entity_id_format_get_with_http_info(service_type, entity_id, format, **kwargs)  # noqa: E501
            return data

    def service_type_ownership_facilityid_entity_id_format_get_with_http_info(self, service_type, entity_id, format, **kwargs):  # noqa: E501
        """Entity Ownership  # noqa: E501

        Entity Ownership  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_type_ownership_facilityid_entity_id_format_get_with_http_info(service_type, entity_id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: serviceType.<br /><br />Valid values: tv, fm, am (required)
        :param str entity_id: Entity ID (required)
        :param str format: json,  xml (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['service_type', 'entity_id', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_type_ownership_facilityid_entity_id_format_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'service_type' is set
        if ('service_type' not in params or
                params['service_type'] is None):
            raise ValueError("Missing the required parameter `service_type` when calling `service_type_ownership_facilityid_entity_id_format_get`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `service_type_ownership_facilityid_entity_id_format_get`")  # noqa: E501
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `service_type_ownership_facilityid_entity_id_format_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service_type' in params:
            path_params['serviceType'] = params['service_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityID'] = params['entity_id']  # noqa: E501
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{serviceType}/ownership/facilityid/{entityID}.{format}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_type_relationship_frn_frn_format_get(self, service_type, frn, format, **kwargs):  # noqa: E501
        """Relationship FRN  # noqa: E501

        Relationship FRN  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_type_relationship_frn_frn_format_get(service_type, frn, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: serviceType.<br /><br />Valid values: tv, fm, am (required)
        :param str frn: frn - length of 10 digits (required)
        :param str format: json, xml (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_type_relationship_frn_frn_format_get_with_http_info(service_type, frn, format, **kwargs)  # noqa: E501
        else:
            (data) = self.service_type_relationship_frn_frn_format_get_with_http_info(service_type, frn, format, **kwargs)  # noqa: E501
            return data

    def service_type_relationship_frn_frn_format_get_with_http_info(self, service_type, frn, format, **kwargs):  # noqa: E501
        """Relationship FRN  # noqa: E501

        Relationship FRN  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_type_relationship_frn_frn_format_get_with_http_info(service_type, frn, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: serviceType.<br /><br />Valid values: tv, fm, am (required)
        :param str frn: frn - length of 10 digits (required)
        :param str format: json, xml (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['service_type', 'frn', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_type_relationship_frn_frn_format_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'service_type' is set
        if ('service_type' not in params or
                params['service_type'] is None):
            raise ValueError("Missing the required parameter `service_type` when calling `service_type_relationship_frn_frn_format_get`")  # noqa: E501
        # verify the required parameter 'frn' is set
        if ('frn' not in params or
                params['frn'] is None):
            raise ValueError("Missing the required parameter `frn` when calling `service_type_relationship_frn_frn_format_get`")  # noqa: E501
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `service_type_relationship_frn_frn_format_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service_type' in params:
            path_params['serviceType'] = params['service_type']  # noqa: E501
        if 'frn' in params:
            path_params['frn'] = params['frn']  # noqa: E501
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{serviceType}/relationship/frn/{frn}.{format}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
