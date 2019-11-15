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


class EdiDocumentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_edi_document(self, body, **kwargs):  # noqa: E501
        """Create an ediDocument  # noqa: E501

        Inserts a new ediDocument using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_edi_document(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param EdiDocument body: EdiDocument to be inserted. (required)
        :return: EdiDocument
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_edi_document_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_edi_document_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_edi_document_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create an ediDocument  # noqa: E501

        Inserts a new ediDocument using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_edi_document_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param EdiDocument body: EdiDocument to be inserted. (required)
        :return: EdiDocument
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
                    " to method add_edi_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_edi_document`")  # noqa: E501

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
            '/beta/ediDocument', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EdiDocument',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_edi_document_audit(self, edi_document_id, edi_document_audit, **kwargs):  # noqa: E501
        """Add new audit for an ediDocument  # noqa: E501

        Adds an audit to an existing ediDocument.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_edi_document_audit(edi_document_id, edi_document_audit, async=True)
        >>> result = thread.get()

        :param async bool
        :param int edi_document_id: Id of the ediDocument to add an audit to (required)
        :param str edi_document_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_edi_document_audit_with_http_info(edi_document_id, edi_document_audit, **kwargs)  # noqa: E501
        else:
            (data) = self.add_edi_document_audit_with_http_info(edi_document_id, edi_document_audit, **kwargs)  # noqa: E501
            return data

    def add_edi_document_audit_with_http_info(self, edi_document_id, edi_document_audit, **kwargs):  # noqa: E501
        """Add new audit for an ediDocument  # noqa: E501

        Adds an audit to an existing ediDocument.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_edi_document_audit_with_http_info(edi_document_id, edi_document_audit, async=True)
        >>> result = thread.get()

        :param async bool
        :param int edi_document_id: Id of the ediDocument to add an audit to (required)
        :param str edi_document_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['edi_document_id', 'edi_document_audit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_edi_document_audit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'edi_document_id' is set
        if ('edi_document_id' not in params or
                params['edi_document_id'] is None):
            raise ValueError("Missing the required parameter `edi_document_id` when calling `add_edi_document_audit`")  # noqa: E501
        # verify the required parameter 'edi_document_audit' is set
        if ('edi_document_audit' not in params or
                params['edi_document_audit'] is None):
            raise ValueError("Missing the required parameter `edi_document_audit` when calling `add_edi_document_audit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'edi_document_id' in params:
            path_params['ediDocumentId'] = params['edi_document_id']  # noqa: E501
        if 'edi_document_audit' in params:
            path_params['ediDocumentAudit'] = params['edi_document_audit']  # noqa: E501

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
            '/beta/ediDocument/{ediDocumentId}/audit/{ediDocumentAudit}', 'PUT',
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

    def add_edi_document_file(self, edi_document_id, file_name, **kwargs):  # noqa: E501
        """Attach a file to an ediDocument  # noqa: E501

        Adds a file to an existing ediDocument.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_edi_document_file(edi_document_id, file_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param int edi_document_id: Id of the ediDocument to add a file to (required)
        :param str file_name: Name of file (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_edi_document_file_with_http_info(edi_document_id, file_name, **kwargs)  # noqa: E501
        else:
            (data) = self.add_edi_document_file_with_http_info(edi_document_id, file_name, **kwargs)  # noqa: E501
            return data

    def add_edi_document_file_with_http_info(self, edi_document_id, file_name, **kwargs):  # noqa: E501
        """Attach a file to an ediDocument  # noqa: E501

        Adds a file to an existing ediDocument.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_edi_document_file_with_http_info(edi_document_id, file_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param int edi_document_id: Id of the ediDocument to add a file to (required)
        :param str file_name: Name of file (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['edi_document_id', 'file_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_edi_document_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'edi_document_id' is set
        if ('edi_document_id' not in params or
                params['edi_document_id'] is None):
            raise ValueError("Missing the required parameter `edi_document_id` when calling `add_edi_document_file`")  # noqa: E501
        # verify the required parameter 'file_name' is set
        if ('file_name' not in params or
                params['file_name'] is None):
            raise ValueError("Missing the required parameter `file_name` when calling `add_edi_document_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'edi_document_id' in params:
            path_params['ediDocumentId'] = params['edi_document_id']  # noqa: E501
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
            '/beta/ediDocument/{ediDocumentId}/file/{fileName}', 'POST',
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

    def add_edi_document_tag(self, edi_document_id, edi_document_tag, **kwargs):  # noqa: E501
        """Add new tags for an ediDocument.  # noqa: E501

        Adds a tag to an existing ediDocument.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_edi_document_tag(edi_document_id, edi_document_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int edi_document_id: Id of the ediDocument to add a tag to (required)
        :param str edi_document_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_edi_document_tag_with_http_info(edi_document_id, edi_document_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.add_edi_document_tag_with_http_info(edi_document_id, edi_document_tag, **kwargs)  # noqa: E501
            return data

    def add_edi_document_tag_with_http_info(self, edi_document_id, edi_document_tag, **kwargs):  # noqa: E501
        """Add new tags for an ediDocument.  # noqa: E501

        Adds a tag to an existing ediDocument.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_edi_document_tag_with_http_info(edi_document_id, edi_document_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int edi_document_id: Id of the ediDocument to add a tag to (required)
        :param str edi_document_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['edi_document_id', 'edi_document_tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_edi_document_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'edi_document_id' is set
        if ('edi_document_id' not in params or
                params['edi_document_id'] is None):
            raise ValueError("Missing the required parameter `edi_document_id` when calling `add_edi_document_tag`")  # noqa: E501
        # verify the required parameter 'edi_document_tag' is set
        if ('edi_document_tag' not in params or
                params['edi_document_tag'] is None):
            raise ValueError("Missing the required parameter `edi_document_tag` when calling `add_edi_document_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'edi_document_id' in params:
            path_params['ediDocumentId'] = params['edi_document_id']  # noqa: E501
        if 'edi_document_tag' in params:
            path_params['ediDocumentTag'] = params['edi_document_tag']  # noqa: E501

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
            '/beta/ediDocument/{ediDocumentId}/tag/{ediDocumentTag}', 'PUT',
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

    def delete_edi_document_tag(self, edi_document_id, edi_document_tag, **kwargs):  # noqa: E501
        """Delete a tag for an ediDocument.  # noqa: E501

        Deletes an existing ediDocument tag using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_edi_document_tag(edi_document_id, edi_document_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int edi_document_id: Id of the ediDocument to remove tag from (required)
        :param str edi_document_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_edi_document_tag_with_http_info(edi_document_id, edi_document_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_edi_document_tag_with_http_info(edi_document_id, edi_document_tag, **kwargs)  # noqa: E501
            return data

    def delete_edi_document_tag_with_http_info(self, edi_document_id, edi_document_tag, **kwargs):  # noqa: E501
        """Delete a tag for an ediDocument.  # noqa: E501

        Deletes an existing ediDocument tag using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_edi_document_tag_with_http_info(edi_document_id, edi_document_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int edi_document_id: Id of the ediDocument to remove tag from (required)
        :param str edi_document_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['edi_document_id', 'edi_document_tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_edi_document_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'edi_document_id' is set
        if ('edi_document_id' not in params or
                params['edi_document_id'] is None):
            raise ValueError("Missing the required parameter `edi_document_id` when calling `delete_edi_document_tag`")  # noqa: E501
        # verify the required parameter 'edi_document_tag' is set
        if ('edi_document_tag' not in params or
                params['edi_document_tag'] is None):
            raise ValueError("Missing the required parameter `edi_document_tag` when calling `delete_edi_document_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'edi_document_id' in params:
            path_params['ediDocumentId'] = params['edi_document_id']  # noqa: E501
        if 'edi_document_tag' in params:
            path_params['ediDocumentTag'] = params['edi_document_tag']  # noqa: E501

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
            '/beta/ediDocument/{ediDocumentId}/tag/{ediDocumentTag}', 'DELETE',
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

    def get_duplicate_edi_document_by_id(self, edi_document_id, **kwargs):  # noqa: E501
        """Get a duplicated an ediDocument by id  # noqa: E501

        Returns a duplicated ediDocument identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_duplicate_edi_document_by_id(edi_document_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int edi_document_id: Id of the ediDocument to be duplicated. (required)
        :return: EdiDocument
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_duplicate_edi_document_by_id_with_http_info(edi_document_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_duplicate_edi_document_by_id_with_http_info(edi_document_id, **kwargs)  # noqa: E501
            return data

    def get_duplicate_edi_document_by_id_with_http_info(self, edi_document_id, **kwargs):  # noqa: E501
        """Get a duplicated an ediDocument by id  # noqa: E501

        Returns a duplicated ediDocument identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_duplicate_edi_document_by_id_with_http_info(edi_document_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int edi_document_id: Id of the ediDocument to be duplicated. (required)
        :return: EdiDocument
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['edi_document_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_duplicate_edi_document_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'edi_document_id' is set
        if ('edi_document_id' not in params or
                params['edi_document_id'] is None):
            raise ValueError("Missing the required parameter `edi_document_id` when calling `get_duplicate_edi_document_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'edi_document_id' in params:
            path_params['ediDocumentId'] = params['edi_document_id']  # noqa: E501

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
            '/beta/ediDocument/duplicate/{ediDocumentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EdiDocument',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_edi_document_by_filter(self, **kwargs):  # noqa: E501
        """Search ediDocuments by filter  # noqa: E501

        Returns the list of ediDocuments that match the given filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_edi_document_by_filter(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[EdiDocument]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_edi_document_by_filter_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_edi_document_by_filter_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_edi_document_by_filter_with_http_info(self, **kwargs):  # noqa: E501
        """Search ediDocuments by filter  # noqa: E501

        Returns the list of ediDocuments that match the given filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_edi_document_by_filter_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[EdiDocument]
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
                    " to method get_edi_document_by_filter" % key
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
            '/beta/ediDocument/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EdiDocument]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_edi_document_by_id(self, edi_document_id, **kwargs):  # noqa: E501
        """Get an ediDocument by id  # noqa: E501

        Returns the ediDocument identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_edi_document_by_id(edi_document_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int edi_document_id: Id of the ediDocument to be returned. (required)
        :return: EdiDocument
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_edi_document_by_id_with_http_info(edi_document_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_edi_document_by_id_with_http_info(edi_document_id, **kwargs)  # noqa: E501
            return data

    def get_edi_document_by_id_with_http_info(self, edi_document_id, **kwargs):  # noqa: E501
        """Get an ediDocument by id  # noqa: E501

        Returns the ediDocument identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_edi_document_by_id_with_http_info(edi_document_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int edi_document_id: Id of the ediDocument to be returned. (required)
        :return: EdiDocument
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['edi_document_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_edi_document_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'edi_document_id' is set
        if ('edi_document_id' not in params or
                params['edi_document_id'] is None):
            raise ValueError("Missing the required parameter `edi_document_id` when calling `get_edi_document_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'edi_document_id' in params:
            path_params['ediDocumentId'] = params['edi_document_id']  # noqa: E501

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
            '/beta/ediDocument/{ediDocumentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EdiDocument',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_edi_document_tags(self, edi_document_id, **kwargs):  # noqa: E501
        """Get the tags for an ediDocument.  # noqa: E501

        Get all existing ediDocument tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_edi_document_tags(edi_document_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int edi_document_id: Id of the ediDocument to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_edi_document_tags_with_http_info(edi_document_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_edi_document_tags_with_http_info(edi_document_id, **kwargs)  # noqa: E501
            return data

    def get_edi_document_tags_with_http_info(self, edi_document_id, **kwargs):  # noqa: E501
        """Get the tags for an ediDocument.  # noqa: E501

        Get all existing ediDocument tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_edi_document_tags_with_http_info(edi_document_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int edi_document_id: Id of the ediDocument to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['edi_document_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_edi_document_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'edi_document_id' is set
        if ('edi_document_id' not in params or
                params['edi_document_id'] is None):
            raise ValueError("Missing the required parameter `edi_document_id` when calling `get_edi_document_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'edi_document_id' in params:
            path_params['ediDocumentId'] = params['edi_document_id']  # noqa: E501

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
            '/beta/ediDocument/{ediDocumentId}/tag', 'GET',
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
