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
from Infoplus.api.item_buyer_api import ItemBuyerApi  # noqa: E501
from Infoplus.rest import ApiException


class TestItemBuyerApi(unittest.TestCase):
    """ItemBuyerApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.item_buyer_api.ItemBuyerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_item_buyer(self):
        """Test case for add_item_buyer

        Create an itemBuyer  # noqa: E501
        """
        pass

    def test_add_item_buyer_audit(self):
        """Test case for add_item_buyer_audit

        Add new audit for an itemBuyer  # noqa: E501
        """
        pass

    def test_add_item_buyer_tag(self):
        """Test case for add_item_buyer_tag

        Add new tags for an itemBuyer.  # noqa: E501
        """
        pass

    def test_delete_item_buyer(self):
        """Test case for delete_item_buyer

        Delete an itemBuyer  # noqa: E501
        """
        pass

    def test_delete_item_buyer_tag(self):
        """Test case for delete_item_buyer_tag

        Delete a tag for an itemBuyer.  # noqa: E501
        """
        pass

    def test_get_duplicate_item_buyer_by_id(self):
        """Test case for get_duplicate_item_buyer_by_id

        Get a duplicated an itemBuyer by id  # noqa: E501
        """
        pass

    def test_get_item_buyer_by_filter(self):
        """Test case for get_item_buyer_by_filter

        Search itemBuyers by filter  # noqa: E501
        """
        pass

    def test_get_item_buyer_by_id(self):
        """Test case for get_item_buyer_by_id

        Get an itemBuyer by id  # noqa: E501
        """
        pass

    def test_get_item_buyer_tags(self):
        """Test case for get_item_buyer_tags

        Get the tags for an itemBuyer.  # noqa: E501
        """
        pass

    def test_update_item_buyer(self):
        """Test case for update_item_buyer

        Update an itemBuyer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
