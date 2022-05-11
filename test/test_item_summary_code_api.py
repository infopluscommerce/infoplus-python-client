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
from Infoplus.api.item_summary_code_api import ItemSummaryCodeApi  # noqa: E501
from Infoplus.rest import ApiException


class TestItemSummaryCodeApi(unittest.TestCase):
    """ItemSummaryCodeApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.item_summary_code_api.ItemSummaryCodeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_item_summary_code(self):
        """Test case for add_item_summary_code

        Create an itemSummaryCode  # noqa: E501
        """
        pass

    def test_add_item_summary_code_audit(self):
        """Test case for add_item_summary_code_audit

        Add new audit for an itemSummaryCode  # noqa: E501
        """
        pass

    def test_add_item_summary_code_file(self):
        """Test case for add_item_summary_code_file

        Attach a file to an itemSummaryCode  # noqa: E501
        """
        pass

    def test_add_item_summary_code_file_by_url(self):
        """Test case for add_item_summary_code_file_by_url

        Attach a file to an itemSummaryCode by URL.  # noqa: E501
        """
        pass

    def test_add_item_summary_code_tag(self):
        """Test case for add_item_summary_code_tag

        Add new tags for an itemSummaryCode.  # noqa: E501
        """
        pass

    def test_delete_item_summary_code(self):
        """Test case for delete_item_summary_code

        Delete an itemSummaryCode  # noqa: E501
        """
        pass

    def test_delete_item_summary_code_file(self):
        """Test case for delete_item_summary_code_file

        Delete a file for an itemSummaryCode.  # noqa: E501
        """
        pass

    def test_delete_item_summary_code_tag(self):
        """Test case for delete_item_summary_code_tag

        Delete a tag for an itemSummaryCode.  # noqa: E501
        """
        pass

    def test_get_duplicate_item_summary_code_by_id(self):
        """Test case for get_duplicate_item_summary_code_by_id

        Get a duplicated an itemSummaryCode by id  # noqa: E501
        """
        pass

    def test_get_item_summary_code_by_filter(self):
        """Test case for get_item_summary_code_by_filter

        Search itemSummaryCodes by filter  # noqa: E501
        """
        pass

    def test_get_item_summary_code_by_id(self):
        """Test case for get_item_summary_code_by_id

        Get an itemSummaryCode by id  # noqa: E501
        """
        pass

    def test_get_item_summary_code_files(self):
        """Test case for get_item_summary_code_files

        Get the files for an itemSummaryCode.  # noqa: E501
        """
        pass

    def test_get_item_summary_code_tags(self):
        """Test case for get_item_summary_code_tags

        Get the tags for an itemSummaryCode.  # noqa: E501
        """
        pass

    def test_update_item_summary_code(self):
        """Test case for update_item_summary_code

        Update an itemSummaryCode  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
