# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: beta
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import Infoplus
from Infoplus.api.warehouse_service_type_api import WarehouseServiceTypeApi  # noqa: E501
from Infoplus.rest import ApiException


class TestWarehouseServiceTypeApi(unittest.TestCase):
    """WarehouseServiceTypeApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.warehouse_service_type_api.WarehouseServiceTypeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_warehouse_service_type(self):
        """Test case for add_warehouse_service_type

        Create a warehouseServiceType  # noqa: E501
        """
        pass

    def test_add_warehouse_service_type_audit(self):
        """Test case for add_warehouse_service_type_audit

        Add new audit for a warehouseServiceType  # noqa: E501
        """
        pass

    def test_add_warehouse_service_type_file(self):
        """Test case for add_warehouse_service_type_file

        Attach a file to a warehouseServiceType  # noqa: E501
        """
        pass

    def test_add_warehouse_service_type_file_by_url(self):
        """Test case for add_warehouse_service_type_file_by_url

        Attach a file to a warehouseServiceType by URL.  # noqa: E501
        """
        pass

    def test_add_warehouse_service_type_tag(self):
        """Test case for add_warehouse_service_type_tag

        Add new tags for a warehouseServiceType.  # noqa: E501
        """
        pass

    def test_delete_warehouse_service_type(self):
        """Test case for delete_warehouse_service_type

        Delete a warehouseServiceType  # noqa: E501
        """
        pass

    def test_delete_warehouse_service_type_file(self):
        """Test case for delete_warehouse_service_type_file

        Delete a file for a warehouseServiceType.  # noqa: E501
        """
        pass

    def test_delete_warehouse_service_type_tag(self):
        """Test case for delete_warehouse_service_type_tag

        Delete a tag for a warehouseServiceType.  # noqa: E501
        """
        pass

    def test_get_duplicate_warehouse_service_type_by_id(self):
        """Test case for get_duplicate_warehouse_service_type_by_id

        Get a duplicated a warehouseServiceType by id  # noqa: E501
        """
        pass

    def test_get_warehouse_service_type_by_filter(self):
        """Test case for get_warehouse_service_type_by_filter

        Search warehouseServiceTypes by filter  # noqa: E501
        """
        pass

    def test_get_warehouse_service_type_by_id(self):
        """Test case for get_warehouse_service_type_by_id

        Get a warehouseServiceType by id  # noqa: E501
        """
        pass

    def test_get_warehouse_service_type_files(self):
        """Test case for get_warehouse_service_type_files

        Get the files for a warehouseServiceType.  # noqa: E501
        """
        pass

    def test_get_warehouse_service_type_tags(self):
        """Test case for get_warehouse_service_type_tags

        Get the tags for a warehouseServiceType.  # noqa: E501
        """
        pass

    def test_update_warehouse_service_type(self):
        """Test case for update_warehouse_service_type

        Update a warehouseServiceType  # noqa: E501
        """
        pass

    def test_update_warehouse_service_type_custom_fields(self):
        """Test case for update_warehouse_service_type_custom_fields

        Update a warehouseServiceType custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
