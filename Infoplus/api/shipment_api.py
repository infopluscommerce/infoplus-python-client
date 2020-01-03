# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: beta
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from Infoplus.api_client import ApiClient


class ShipmentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_shipment_audit(self, shipment_id, shipment_audit, **kwargs):  # noqa: E501
        """Add new audit for a shipment  # noqa: E501

        Adds an audit to an existing shipment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_shipment_audit(shipment_id, shipment_audit, async=True)
        >>> result = thread.get()

        :param async bool
        :param int shipment_id: Id of the shipment to add an audit to (required)
        :param str shipment_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_shipment_audit_with_http_info(shipment_id, shipment_audit, **kwargs)  # noqa: E501
        else:
            (data) = self.add_shipment_audit_with_http_info(shipment_id, shipment_audit, **kwargs)  # noqa: E501
            return data

    def add_shipment_audit_with_http_info(self, shipment_id, shipment_audit, **kwargs):  # noqa: E501
        """Add new audit for a shipment  # noqa: E501

        Adds an audit to an existing shipment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_shipment_audit_with_http_info(shipment_id, shipment_audit, async=True)
        >>> result = thread.get()

        :param async bool
        :param int shipment_id: Id of the shipment to add an audit to (required)
        :param str shipment_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shipment_id', 'shipment_audit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_shipment_audit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shipment_id' is set
        if ('shipment_id' not in params or
                params['shipment_id'] is None):
            raise ValueError("Missing the required parameter `shipment_id` when calling `add_shipment_audit`")  # noqa: E501
        # verify the required parameter 'shipment_audit' is set
        if ('shipment_audit' not in params or
                params['shipment_audit'] is None):
            raise ValueError("Missing the required parameter `shipment_audit` when calling `add_shipment_audit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shipment_id' in params:
            path_params['shipmentId'] = params['shipment_id']  # noqa: E501
        if 'shipment_audit' in params:
            path_params['shipmentAudit'] = params['shipment_audit']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/shipment/{shipmentId}/audit/{shipmentAudit}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_shipment_file(self, shipment_id, file_name, **kwargs):  # noqa: E501
        """Attach a file to a shipment  # noqa: E501

        Adds a file to an existing shipment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_shipment_file(shipment_id, file_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param int shipment_id: Id of the shipment to add a file to (required)
        :param str file_name: Name of file (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_shipment_file_with_http_info(shipment_id, file_name, **kwargs)  # noqa: E501
        else:
            (data) = self.add_shipment_file_with_http_info(shipment_id, file_name, **kwargs)  # noqa: E501
            return data

    def add_shipment_file_with_http_info(self, shipment_id, file_name, **kwargs):  # noqa: E501
        """Attach a file to a shipment  # noqa: E501

        Adds a file to an existing shipment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_shipment_file_with_http_info(shipment_id, file_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param int shipment_id: Id of the shipment to add a file to (required)
        :param str file_name: Name of file (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shipment_id', 'file_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_shipment_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shipment_id' is set
        if ('shipment_id' not in params or
                params['shipment_id'] is None):
            raise ValueError("Missing the required parameter `shipment_id` when calling `add_shipment_file`")  # noqa: E501
        # verify the required parameter 'file_name' is set
        if ('file_name' not in params or
                params['file_name'] is None):
            raise ValueError("Missing the required parameter `file_name` when calling `add_shipment_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shipment_id' in params:
            path_params['shipmentId'] = params['shipment_id']  # noqa: E501
        if 'file_name' in params:
            path_params['fileName'] = params['file_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/shipment/{shipmentId}/file/{fileName}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_shipment_tag(self, shipment_id, shipment_tag, **kwargs):  # noqa: E501
        """Add new tags for a shipment.  # noqa: E501

        Adds a tag to an existing shipment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_shipment_tag(shipment_id, shipment_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int shipment_id: Id of the shipment to add a tag to (required)
        :param str shipment_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_shipment_tag_with_http_info(shipment_id, shipment_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.add_shipment_tag_with_http_info(shipment_id, shipment_tag, **kwargs)  # noqa: E501
            return data

    def add_shipment_tag_with_http_info(self, shipment_id, shipment_tag, **kwargs):  # noqa: E501
        """Add new tags for a shipment.  # noqa: E501

        Adds a tag to an existing shipment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_shipment_tag_with_http_info(shipment_id, shipment_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int shipment_id: Id of the shipment to add a tag to (required)
        :param str shipment_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shipment_id', 'shipment_tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_shipment_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shipment_id' is set
        if ('shipment_id' not in params or
                params['shipment_id'] is None):
            raise ValueError("Missing the required parameter `shipment_id` when calling `add_shipment_tag`")  # noqa: E501
        # verify the required parameter 'shipment_tag' is set
        if ('shipment_tag' not in params or
                params['shipment_tag'] is None):
            raise ValueError("Missing the required parameter `shipment_tag` when calling `add_shipment_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shipment_id' in params:
            path_params['shipmentId'] = params['shipment_id']  # noqa: E501
        if 'shipment_tag' in params:
            path_params['shipmentTag'] = params['shipment_tag']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/shipment/{shipmentId}/tag/{shipmentTag}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_shipment_tag(self, shipment_id, shipment_tag, **kwargs):  # noqa: E501
        """Delete a tag for a shipment.  # noqa: E501

        Deletes an existing shipment tag using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_shipment_tag(shipment_id, shipment_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int shipment_id: Id of the shipment to remove tag from (required)
        :param str shipment_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_shipment_tag_with_http_info(shipment_id, shipment_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_shipment_tag_with_http_info(shipment_id, shipment_tag, **kwargs)  # noqa: E501
            return data

    def delete_shipment_tag_with_http_info(self, shipment_id, shipment_tag, **kwargs):  # noqa: E501
        """Delete a tag for a shipment.  # noqa: E501

        Deletes an existing shipment tag using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_shipment_tag_with_http_info(shipment_id, shipment_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int shipment_id: Id of the shipment to remove tag from (required)
        :param str shipment_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shipment_id', 'shipment_tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_shipment_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shipment_id' is set
        if ('shipment_id' not in params or
                params['shipment_id'] is None):
            raise ValueError("Missing the required parameter `shipment_id` when calling `delete_shipment_tag`")  # noqa: E501
        # verify the required parameter 'shipment_tag' is set
        if ('shipment_tag' not in params or
                params['shipment_tag'] is None):
            raise ValueError("Missing the required parameter `shipment_tag` when calling `delete_shipment_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shipment_id' in params:
            path_params['shipmentId'] = params['shipment_id']  # noqa: E501
        if 'shipment_tag' in params:
            path_params['shipmentTag'] = params['shipment_tag']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/shipment/{shipmentId}/tag/{shipmentTag}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_duplicate_shipment_by_id(self, shipment_id, **kwargs):  # noqa: E501
        """Get a duplicated a shipment by id  # noqa: E501

        Returns a duplicated shipment identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_duplicate_shipment_by_id(shipment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int shipment_id: Id of the shipment to be duplicated. (required)
        :return: Shipment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_duplicate_shipment_by_id_with_http_info(shipment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_duplicate_shipment_by_id_with_http_info(shipment_id, **kwargs)  # noqa: E501
            return data

    def get_duplicate_shipment_by_id_with_http_info(self, shipment_id, **kwargs):  # noqa: E501
        """Get a duplicated a shipment by id  # noqa: E501

        Returns a duplicated shipment identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_duplicate_shipment_by_id_with_http_info(shipment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int shipment_id: Id of the shipment to be duplicated. (required)
        :return: Shipment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shipment_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_duplicate_shipment_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shipment_id' is set
        if ('shipment_id' not in params or
                params['shipment_id'] is None):
            raise ValueError("Missing the required parameter `shipment_id` when calling `get_duplicate_shipment_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shipment_id' in params:
            path_params['shipmentId'] = params['shipment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/shipment/duplicate/{shipmentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Shipment',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_shipment_by_filter(self, **kwargs):  # noqa: E501
        """Search shipments by filter  # noqa: E501

        Returns the list of shipments that match the given filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_shipment_by_filter(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[Shipment]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_shipment_by_filter_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_shipment_by_filter_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_shipment_by_filter_with_http_info(self, **kwargs):  # noqa: E501
        """Search shipments by filter  # noqa: E501

        Returns the list of shipments that match the given filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_shipment_by_filter_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[Shipment]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'page', 'limit', 'sort']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shipment_by_filter" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/shipment/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Shipment]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_shipment_by_id(self, shipment_id, **kwargs):  # noqa: E501
        """Get a shipment by id  # noqa: E501

        Returns the shipment identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_shipment_by_id(shipment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int shipment_id: Id of the shipment to be returned. (required)
        :return: Shipment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_shipment_by_id_with_http_info(shipment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_shipment_by_id_with_http_info(shipment_id, **kwargs)  # noqa: E501
            return data

    def get_shipment_by_id_with_http_info(self, shipment_id, **kwargs):  # noqa: E501
        """Get a shipment by id  # noqa: E501

        Returns the shipment identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_shipment_by_id_with_http_info(shipment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int shipment_id: Id of the shipment to be returned. (required)
        :return: Shipment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shipment_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shipment_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shipment_id' is set
        if ('shipment_id' not in params or
                params['shipment_id'] is None):
            raise ValueError("Missing the required parameter `shipment_id` when calling `get_shipment_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shipment_id' in params:
            path_params['shipmentId'] = params['shipment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/shipment/{shipmentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Shipment',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_shipment_tags(self, shipment_id, **kwargs):  # noqa: E501
        """Get the tags for a shipment.  # noqa: E501

        Get all existing shipment tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_shipment_tags(shipment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int shipment_id: Id of the shipment to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_shipment_tags_with_http_info(shipment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_shipment_tags_with_http_info(shipment_id, **kwargs)  # noqa: E501
            return data

    def get_shipment_tags_with_http_info(self, shipment_id, **kwargs):  # noqa: E501
        """Get the tags for a shipment.  # noqa: E501

        Get all existing shipment tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_shipment_tags_with_http_info(shipment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int shipment_id: Id of the shipment to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shipment_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shipment_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shipment_id' is set
        if ('shipment_id' not in params or
                params['shipment_id'] is None):
            raise ValueError("Missing the required parameter `shipment_id` when calling `get_shipment_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shipment_id' in params:
            path_params['shipmentId'] = params['shipment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/shipment/{shipmentId}/tag', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_shipment_custom_fields(self, body, **kwargs):  # noqa: E501
        """Update a shipment custom fields  # noqa: E501

        Updates an existing shipment custom fields using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_shipment_custom_fields(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Shipment body: Shipment to be updated. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_shipment_custom_fields_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_shipment_custom_fields_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_shipment_custom_fields_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update a shipment custom fields  # noqa: E501

        Updates an existing shipment custom fields using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_shipment_custom_fields_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Shipment body: Shipment to be updated. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_shipment_custom_fields" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_shipment_custom_fields`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/shipment/customFields', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)