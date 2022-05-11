# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: v3.0
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import Infoplus
from Infoplus.api.warehouse_document_api import WarehouseDocumentApi  # noqa: E501
from Infoplus.rest import ApiException


class TestWarehouseDocumentApi(unittest.TestCase):
    """WarehouseDocumentApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.warehouse_document_api.WarehouseDocumentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_warehouse_document_audit(self):
        """Test case for add_warehouse_document_audit

        Add new audit for a warehouseDocument  # noqa: E501
        """
        pass

    def test_add_warehouse_document_file(self):
        """Test case for add_warehouse_document_file

        Attach a file to a warehouseDocument  # noqa: E501
        """
        pass

    def test_add_warehouse_document_file_by_url(self):
        """Test case for add_warehouse_document_file_by_url

        Attach a file to a warehouseDocument by URL.  # noqa: E501
        """
        pass

    def test_add_warehouse_document_tag(self):
        """Test case for add_warehouse_document_tag

        Add new tags for a warehouseDocument.  # noqa: E501
        """
        pass

    def test_delete_warehouse_document_file(self):
        """Test case for delete_warehouse_document_file

        Delete a file for a warehouseDocument.  # noqa: E501
        """
        pass

    def test_delete_warehouse_document_tag(self):
        """Test case for delete_warehouse_document_tag

        Delete a tag for a warehouseDocument.  # noqa: E501
        """
        pass

    def test_get_duplicate_warehouse_document_by_id(self):
        """Test case for get_duplicate_warehouse_document_by_id

        Get a duplicated a warehouseDocument by id  # noqa: E501
        """
        pass

    def test_get_warehouse_document_by_filter(self):
        """Test case for get_warehouse_document_by_filter

        Search warehouseDocuments by filter  # noqa: E501
        """
        pass

    def test_get_warehouse_document_by_id(self):
        """Test case for get_warehouse_document_by_id

        Get a warehouseDocument by id  # noqa: E501
        """
        pass

    def test_get_warehouse_document_files(self):
        """Test case for get_warehouse_document_files

        Get the files for a warehouseDocument.  # noqa: E501
        """
        pass

    def test_get_warehouse_document_tags(self):
        """Test case for get_warehouse_document_tags

        Get the tags for a warehouseDocument.  # noqa: E501
        """
        pass

    def test_update_warehouse_document_custom_fields(self):
        """Test case for update_warehouse_document_custom_fields

        Update a warehouseDocument custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
