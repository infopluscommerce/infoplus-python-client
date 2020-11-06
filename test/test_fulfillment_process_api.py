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
from Infoplus.api.fulfillment_process_api import FulfillmentProcessApi  # noqa: E501
from Infoplus.rest import ApiException


class TestFulfillmentProcessApi(unittest.TestCase):
    """FulfillmentProcessApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.fulfillment_process_api.FulfillmentProcessApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_fulfillment_process_audit(self):
        """Test case for add_fulfillment_process_audit

        Add new audit for a fulfillmentProcess  # noqa: E501
        """
        pass

    def test_add_fulfillment_process_file(self):
        """Test case for add_fulfillment_process_file

        Attach a file to a fulfillmentProcess  # noqa: E501
        """
        pass

    def test_add_fulfillment_process_file_by_url(self):
        """Test case for add_fulfillment_process_file_by_url

        Attach a file to a fulfillmentProcess by URL.  # noqa: E501
        """
        pass

    def test_add_fulfillment_process_tag(self):
        """Test case for add_fulfillment_process_tag

        Add new tags for a fulfillmentProcess.  # noqa: E501
        """
        pass

    def test_delete_fulfillment_process_file(self):
        """Test case for delete_fulfillment_process_file

        Delete a file for a fulfillmentProcess.  # noqa: E501
        """
        pass

    def test_delete_fulfillment_process_tag(self):
        """Test case for delete_fulfillment_process_tag

        Delete a tag for a fulfillmentProcess.  # noqa: E501
        """
        pass

    def test_get_duplicate_fulfillment_process_by_id(self):
        """Test case for get_duplicate_fulfillment_process_by_id

        Get a duplicated a fulfillmentProcess by id  # noqa: E501
        """
        pass

    def test_get_fulfillment_process_by_filter(self):
        """Test case for get_fulfillment_process_by_filter

        Search fulfillmentProcesses by filter  # noqa: E501
        """
        pass

    def test_get_fulfillment_process_by_id(self):
        """Test case for get_fulfillment_process_by_id

        Get a fulfillmentProcess by id  # noqa: E501
        """
        pass

    def test_get_fulfillment_process_files(self):
        """Test case for get_fulfillment_process_files

        Get the files for a fulfillmentProcess.  # noqa: E501
        """
        pass

    def test_get_fulfillment_process_tags(self):
        """Test case for get_fulfillment_process_tags

        Get the tags for a fulfillmentProcess.  # noqa: E501
        """
        pass

    def test_update_fulfillment_process_custom_fields(self):
        """Test case for update_fulfillment_process_custom_fields

        Update a fulfillmentProcess custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()