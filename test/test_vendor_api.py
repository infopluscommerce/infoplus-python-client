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
from Infoplus.api.vendor_api import VendorApi  # noqa: E501
from Infoplus.rest import ApiException


class TestVendorApi(unittest.TestCase):
    """VendorApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.vendor_api.VendorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_vendor(self):
        """Test case for add_vendor

        Create a vendor  # noqa: E501
        """
        pass

    def test_add_vendor_audit(self):
        """Test case for add_vendor_audit

        Add new audit for a vendor  # noqa: E501
        """
        pass

    def test_add_vendor_file(self):
        """Test case for add_vendor_file

        Attach a file to a vendor  # noqa: E501
        """
        pass

    def test_add_vendor_file_by_url(self):
        """Test case for add_vendor_file_by_url

        Attach a file to a vendor by URL.  # noqa: E501
        """
        pass

    def test_add_vendor_tag(self):
        """Test case for add_vendor_tag

        Add new tags for a vendor.  # noqa: E501
        """
        pass

    def test_delete_vendor(self):
        """Test case for delete_vendor

        Delete a vendor  # noqa: E501
        """
        pass

    def test_delete_vendor_file(self):
        """Test case for delete_vendor_file

        Delete a file for a vendor.  # noqa: E501
        """
        pass

    def test_delete_vendor_tag(self):
        """Test case for delete_vendor_tag

        Delete a tag for a vendor.  # noqa: E501
        """
        pass

    def test_get_duplicate_vendor_by_id(self):
        """Test case for get_duplicate_vendor_by_id

        Get a duplicated a vendor by id  # noqa: E501
        """
        pass

    def test_get_vendor_by_filter(self):
        """Test case for get_vendor_by_filter

        Search vendors by filter  # noqa: E501
        """
        pass

    def test_get_vendor_by_id(self):
        """Test case for get_vendor_by_id

        Get a vendor by id  # noqa: E501
        """
        pass

    def test_get_vendor_files(self):
        """Test case for get_vendor_files

        Get the files for a vendor.  # noqa: E501
        """
        pass

    def test_get_vendor_tags(self):
        """Test case for get_vendor_tags

        Get the tags for a vendor.  # noqa: E501
        """
        pass

    def test_update_vendor(self):
        """Test case for update_vendor

        Update a vendor  # noqa: E501
        """
        pass

    def test_update_vendor_custom_fields(self):
        """Test case for update_vendor_custom_fields

        Update a vendor custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()