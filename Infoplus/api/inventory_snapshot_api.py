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


class InventorySnapshotApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_inventory_snapshot_audit(self, inventory_snapshot_id, inventory_snapshot_audit, **kwargs):  # noqa: E501
        """Add new audit for an inventorySnapshot  # noqa: E501

        Adds an audit to an existing inventorySnapshot.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_inventory_snapshot_audit(inventory_snapshot_id, inventory_snapshot_audit, async=True)
        >>> result = thread.get()

        :param async bool
        :param int inventory_snapshot_id: Id of the inventorySnapshot to add an audit to (required)
        :param str inventory_snapshot_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_inventory_snapshot_audit_with_http_info(inventory_snapshot_id, inventory_snapshot_audit, **kwargs)  # noqa: E501
        else:
            (data) = self.add_inventory_snapshot_audit_with_http_info(inventory_snapshot_id, inventory_snapshot_audit, **kwargs)  # noqa: E501
            return data

    def add_inventory_snapshot_audit_with_http_info(self, inventory_snapshot_id, inventory_snapshot_audit, **kwargs):  # noqa: E501
        """Add new audit for an inventorySnapshot  # noqa: E501

        Adds an audit to an existing inventorySnapshot.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_inventory_snapshot_audit_with_http_info(inventory_snapshot_id, inventory_snapshot_audit, async=True)
        >>> result = thread.get()

        :param async bool
        :param int inventory_snapshot_id: Id of the inventorySnapshot to add an audit to (required)
        :param str inventory_snapshot_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inventory_snapshot_id', 'inventory_snapshot_audit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_inventory_snapshot_audit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inventory_snapshot_id' is set
        if ('inventory_snapshot_id' not in params or
                params['inventory_snapshot_id'] is None):
            raise ValueError("Missing the required parameter `inventory_snapshot_id` when calling `add_inventory_snapshot_audit`")  # noqa: E501
        # verify the required parameter 'inventory_snapshot_audit' is set
        if ('inventory_snapshot_audit' not in params or
                params['inventory_snapshot_audit'] is None):
            raise ValueError("Missing the required parameter `inventory_snapshot_audit` when calling `add_inventory_snapshot_audit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inventory_snapshot_id' in params:
            path_params['inventorySnapshotId'] = params['inventory_snapshot_id']  # noqa: E501
        if 'inventory_snapshot_audit' in params:
            path_params['inventorySnapshotAudit'] = params['inventory_snapshot_audit']  # noqa: E501

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
            '/beta/inventorySnapshot/{inventorySnapshotId}/audit/{inventorySnapshotAudit}', 'PUT',
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

    def add_inventory_snapshot_tag(self, inventory_snapshot_id, inventory_snapshot_tag, **kwargs):  # noqa: E501
        """Add new tags for an inventorySnapshot.  # noqa: E501

        Adds a tag to an existing inventorySnapshot.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_inventory_snapshot_tag(inventory_snapshot_id, inventory_snapshot_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int inventory_snapshot_id: Id of the inventorySnapshot to add a tag to (required)
        :param str inventory_snapshot_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_inventory_snapshot_tag_with_http_info(inventory_snapshot_id, inventory_snapshot_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.add_inventory_snapshot_tag_with_http_info(inventory_snapshot_id, inventory_snapshot_tag, **kwargs)  # noqa: E501
            return data

    def add_inventory_snapshot_tag_with_http_info(self, inventory_snapshot_id, inventory_snapshot_tag, **kwargs):  # noqa: E501
        """Add new tags for an inventorySnapshot.  # noqa: E501

        Adds a tag to an existing inventorySnapshot.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_inventory_snapshot_tag_with_http_info(inventory_snapshot_id, inventory_snapshot_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int inventory_snapshot_id: Id of the inventorySnapshot to add a tag to (required)
        :param str inventory_snapshot_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inventory_snapshot_id', 'inventory_snapshot_tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_inventory_snapshot_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inventory_snapshot_id' is set
        if ('inventory_snapshot_id' not in params or
                params['inventory_snapshot_id'] is None):
            raise ValueError("Missing the required parameter `inventory_snapshot_id` when calling `add_inventory_snapshot_tag`")  # noqa: E501
        # verify the required parameter 'inventory_snapshot_tag' is set
        if ('inventory_snapshot_tag' not in params or
                params['inventory_snapshot_tag'] is None):
            raise ValueError("Missing the required parameter `inventory_snapshot_tag` when calling `add_inventory_snapshot_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inventory_snapshot_id' in params:
            path_params['inventorySnapshotId'] = params['inventory_snapshot_id']  # noqa: E501
        if 'inventory_snapshot_tag' in params:
            path_params['inventorySnapshotTag'] = params['inventory_snapshot_tag']  # noqa: E501

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
            '/beta/inventorySnapshot/{inventorySnapshotId}/tag/{inventorySnapshotTag}', 'PUT',
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

    def delete_inventory_snapshot_tag(self, inventory_snapshot_id, inventory_snapshot_tag, **kwargs):  # noqa: E501
        """Delete a tag for an inventorySnapshot.  # noqa: E501

        Deletes an existing inventorySnapshot tag using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_inventory_snapshot_tag(inventory_snapshot_id, inventory_snapshot_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int inventory_snapshot_id: Id of the inventorySnapshot to remove tag from (required)
        :param str inventory_snapshot_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_inventory_snapshot_tag_with_http_info(inventory_snapshot_id, inventory_snapshot_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_inventory_snapshot_tag_with_http_info(inventory_snapshot_id, inventory_snapshot_tag, **kwargs)  # noqa: E501
            return data

    def delete_inventory_snapshot_tag_with_http_info(self, inventory_snapshot_id, inventory_snapshot_tag, **kwargs):  # noqa: E501
        """Delete a tag for an inventorySnapshot.  # noqa: E501

        Deletes an existing inventorySnapshot tag using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_inventory_snapshot_tag_with_http_info(inventory_snapshot_id, inventory_snapshot_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int inventory_snapshot_id: Id of the inventorySnapshot to remove tag from (required)
        :param str inventory_snapshot_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inventory_snapshot_id', 'inventory_snapshot_tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_inventory_snapshot_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inventory_snapshot_id' is set
        if ('inventory_snapshot_id' not in params or
                params['inventory_snapshot_id'] is None):
            raise ValueError("Missing the required parameter `inventory_snapshot_id` when calling `delete_inventory_snapshot_tag`")  # noqa: E501
        # verify the required parameter 'inventory_snapshot_tag' is set
        if ('inventory_snapshot_tag' not in params or
                params['inventory_snapshot_tag'] is None):
            raise ValueError("Missing the required parameter `inventory_snapshot_tag` when calling `delete_inventory_snapshot_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inventory_snapshot_id' in params:
            path_params['inventorySnapshotId'] = params['inventory_snapshot_id']  # noqa: E501
        if 'inventory_snapshot_tag' in params:
            path_params['inventorySnapshotTag'] = params['inventory_snapshot_tag']  # noqa: E501

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
            '/beta/inventorySnapshot/{inventorySnapshotId}/tag/{inventorySnapshotTag}', 'DELETE',
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

    def get_duplicate_inventory_snapshot_by_id(self, inventory_snapshot_id, **kwargs):  # noqa: E501
        """Get a duplicated an inventorySnapshot by id  # noqa: E501

        Returns a duplicated inventorySnapshot identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_duplicate_inventory_snapshot_by_id(inventory_snapshot_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int inventory_snapshot_id: Id of the inventorySnapshot to be duplicated. (required)
        :return: InventorySnapshot
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_duplicate_inventory_snapshot_by_id_with_http_info(inventory_snapshot_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_duplicate_inventory_snapshot_by_id_with_http_info(inventory_snapshot_id, **kwargs)  # noqa: E501
            return data

    def get_duplicate_inventory_snapshot_by_id_with_http_info(self, inventory_snapshot_id, **kwargs):  # noqa: E501
        """Get a duplicated an inventorySnapshot by id  # noqa: E501

        Returns a duplicated inventorySnapshot identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_duplicate_inventory_snapshot_by_id_with_http_info(inventory_snapshot_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int inventory_snapshot_id: Id of the inventorySnapshot to be duplicated. (required)
        :return: InventorySnapshot
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inventory_snapshot_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_duplicate_inventory_snapshot_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inventory_snapshot_id' is set
        if ('inventory_snapshot_id' not in params or
                params['inventory_snapshot_id'] is None):
            raise ValueError("Missing the required parameter `inventory_snapshot_id` when calling `get_duplicate_inventory_snapshot_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inventory_snapshot_id' in params:
            path_params['inventorySnapshotId'] = params['inventory_snapshot_id']  # noqa: E501

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
            '/beta/inventorySnapshot/duplicate/{inventorySnapshotId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InventorySnapshot',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_inventory_snapshot_by_filter(self, **kwargs):  # noqa: E501
        """Search inventorySnapshots by filter  # noqa: E501

        Returns the list of inventorySnapshots that match the given filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_inventory_snapshot_by_filter(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[InventorySnapshot]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_inventory_snapshot_by_filter_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_inventory_snapshot_by_filter_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_inventory_snapshot_by_filter_with_http_info(self, **kwargs):  # noqa: E501
        """Search inventorySnapshots by filter  # noqa: E501

        Returns the list of inventorySnapshots that match the given filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_inventory_snapshot_by_filter_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[InventorySnapshot]
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
                    " to method get_inventory_snapshot_by_filter" % key
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
            '/beta/inventorySnapshot/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InventorySnapshot]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_inventory_snapshot_by_id(self, inventory_snapshot_id, **kwargs):  # noqa: E501
        """Get an inventorySnapshot by id  # noqa: E501

        Returns the inventorySnapshot identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_inventory_snapshot_by_id(inventory_snapshot_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int inventory_snapshot_id: Id of the inventorySnapshot to be returned. (required)
        :return: InventorySnapshot
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_inventory_snapshot_by_id_with_http_info(inventory_snapshot_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_inventory_snapshot_by_id_with_http_info(inventory_snapshot_id, **kwargs)  # noqa: E501
            return data

    def get_inventory_snapshot_by_id_with_http_info(self, inventory_snapshot_id, **kwargs):  # noqa: E501
        """Get an inventorySnapshot by id  # noqa: E501

        Returns the inventorySnapshot identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_inventory_snapshot_by_id_with_http_info(inventory_snapshot_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int inventory_snapshot_id: Id of the inventorySnapshot to be returned. (required)
        :return: InventorySnapshot
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inventory_snapshot_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_inventory_snapshot_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inventory_snapshot_id' is set
        if ('inventory_snapshot_id' not in params or
                params['inventory_snapshot_id'] is None):
            raise ValueError("Missing the required parameter `inventory_snapshot_id` when calling `get_inventory_snapshot_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inventory_snapshot_id' in params:
            path_params['inventorySnapshotId'] = params['inventory_snapshot_id']  # noqa: E501

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
            '/beta/inventorySnapshot/{inventorySnapshotId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InventorySnapshot',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_inventory_snapshot_tags(self, inventory_snapshot_id, **kwargs):  # noqa: E501
        """Get the tags for an inventorySnapshot.  # noqa: E501

        Get all existing inventorySnapshot tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_inventory_snapshot_tags(inventory_snapshot_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int inventory_snapshot_id: Id of the inventorySnapshot to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_inventory_snapshot_tags_with_http_info(inventory_snapshot_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_inventory_snapshot_tags_with_http_info(inventory_snapshot_id, **kwargs)  # noqa: E501
            return data

    def get_inventory_snapshot_tags_with_http_info(self, inventory_snapshot_id, **kwargs):  # noqa: E501
        """Get the tags for an inventorySnapshot.  # noqa: E501

        Get all existing inventorySnapshot tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_inventory_snapshot_tags_with_http_info(inventory_snapshot_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int inventory_snapshot_id: Id of the inventorySnapshot to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inventory_snapshot_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_inventory_snapshot_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inventory_snapshot_id' is set
        if ('inventory_snapshot_id' not in params or
                params['inventory_snapshot_id'] is None):
            raise ValueError("Missing the required parameter `inventory_snapshot_id` when calling `get_inventory_snapshot_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inventory_snapshot_id' in params:
            path_params['inventorySnapshotId'] = params['inventory_snapshot_id']  # noqa: E501

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
            '/beta/inventorySnapshot/{inventorySnapshotId}/tag', 'GET',
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
