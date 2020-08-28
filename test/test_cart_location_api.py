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
from Infoplus.api.cart_location_api import CartLocationApi  # noqa: E501
from Infoplus.rest import ApiException


class TestCartLocationApi(unittest.TestCase):
    """CartLocationApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.cart_location_api.CartLocationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_cart_location_audit(self):
        """Test case for add_cart_location_audit

        Add new audit for a cartLocation  # noqa: E501
        """
        pass

    def test_add_cart_location_file(self):
        """Test case for add_cart_location_file

        Attach a file to a cartLocation  # noqa: E501
        """
        pass

    def test_add_cart_location_file_by_url(self):
        """Test case for add_cart_location_file_by_url

        Attach a file to a cartLocation by URL.  # noqa: E501
        """
        pass

    def test_add_cart_location_tag(self):
        """Test case for add_cart_location_tag

        Add new tags for a cartLocation.  # noqa: E501
        """
        pass

    def test_delete_cart_location_file(self):
        """Test case for delete_cart_location_file

        Delete a file for a cartLocation.  # noqa: E501
        """
        pass

    def test_delete_cart_location_tag(self):
        """Test case for delete_cart_location_tag

        Delete a tag for a cartLocation.  # noqa: E501
        """
        pass

    def test_get_cart_location_by_filter(self):
        """Test case for get_cart_location_by_filter

        Search cartLocations by filter  # noqa: E501
        """
        pass

    def test_get_cart_location_by_id(self):
        """Test case for get_cart_location_by_id

        Get a cartLocation by id  # noqa: E501
        """
        pass

    def test_get_cart_location_files(self):
        """Test case for get_cart_location_files

        Get the files for a cartLocation.  # noqa: E501
        """
        pass

    def test_get_cart_location_tags(self):
        """Test case for get_cart_location_tags

        Get the tags for a cartLocation.  # noqa: E501
        """
        pass

    def test_get_duplicate_cart_location_by_id(self):
        """Test case for get_duplicate_cart_location_by_id

        Get a duplicated a cartLocation by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
