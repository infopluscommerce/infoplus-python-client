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
from Infoplus.api.order_activity_api import OrderActivityApi  # noqa: E501
from Infoplus.rest import ApiException


class TestOrderActivityApi(unittest.TestCase):
    """OrderActivityApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.order_activity_api.OrderActivityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_order_activity(self):
        """Test case for add_order_activity

        Create an orderActivity  # noqa: E501
        """
        pass

    def test_add_order_activity_audit(self):
        """Test case for add_order_activity_audit

        Add new audit for an orderActivity  # noqa: E501
        """
        pass

    def test_add_order_activity_file(self):
        """Test case for add_order_activity_file

        Attach a file to an orderActivity  # noqa: E501
        """
        pass

    def test_add_order_activity_file_by_url(self):
        """Test case for add_order_activity_file_by_url

        Attach a file to an orderActivity by URL.  # noqa: E501
        """
        pass

    def test_add_order_activity_tag(self):
        """Test case for add_order_activity_tag

        Add new tags for an orderActivity.  # noqa: E501
        """
        pass

    def test_delete_order_activity(self):
        """Test case for delete_order_activity

        Delete an orderActivity  # noqa: E501
        """
        pass

    def test_delete_order_activity_file(self):
        """Test case for delete_order_activity_file

        Delete a file for an orderActivity.  # noqa: E501
        """
        pass

    def test_delete_order_activity_tag(self):
        """Test case for delete_order_activity_tag

        Delete a tag for an orderActivity.  # noqa: E501
        """
        pass

    def test_get_duplicate_order_activity_by_id(self):
        """Test case for get_duplicate_order_activity_by_id

        Get a duplicated an orderActivity by id  # noqa: E501
        """
        pass

    def test_get_order_activity_by_filter(self):
        """Test case for get_order_activity_by_filter

        Search orderActivitys by filter  # noqa: E501
        """
        pass

    def test_get_order_activity_by_id(self):
        """Test case for get_order_activity_by_id

        Get an orderActivity by id  # noqa: E501
        """
        pass

    def test_get_order_activity_files(self):
        """Test case for get_order_activity_files

        Get the files for an orderActivity.  # noqa: E501
        """
        pass

    def test_get_order_activity_tags(self):
        """Test case for get_order_activity_tags

        Get the tags for an orderActivity.  # noqa: E501
        """
        pass

    def test_update_order_activity(self):
        """Test case for update_order_activity

        Update an orderActivity  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
