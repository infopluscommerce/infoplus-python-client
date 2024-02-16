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
from Infoplus.api.replenishment_api import ReplenishmentApi  # noqa: E501
from Infoplus.rest import ApiException


class TestReplenishmentApi(unittest.TestCase):
    """ReplenishmentApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.replenishment_api.ReplenishmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_replenishment_audit(self):
        """Test case for add_replenishment_audit

        Add new audit for a replenishment  # noqa: E501
        """
        pass

    def test_add_replenishment_file(self):
        """Test case for add_replenishment_file

        Attach a file to a replenishment  # noqa: E501
        """
        pass

    def test_add_replenishment_file_by_url(self):
        """Test case for add_replenishment_file_by_url

        Attach a file to a replenishment by URL.  # noqa: E501
        """
        pass

    def test_add_replenishment_tag(self):
        """Test case for add_replenishment_tag

        Add new tags for a replenishment.  # noqa: E501
        """
        pass

    def test_delete_replenishment_file(self):
        """Test case for delete_replenishment_file

        Delete a file for a replenishment.  # noqa: E501
        """
        pass

    def test_delete_replenishment_tag(self):
        """Test case for delete_replenishment_tag

        Delete a tag for a replenishment.  # noqa: E501
        """
        pass

    def test_get_duplicate_replenishment_by_id(self):
        """Test case for get_duplicate_replenishment_by_id

        Get a duplicated a replenishment by id  # noqa: E501
        """
        pass

    def test_get_replenishment_by_filter(self):
        """Test case for get_replenishment_by_filter

        Search replenishments by filter  # noqa: E501
        """
        pass

    def test_get_replenishment_by_id(self):
        """Test case for get_replenishment_by_id

        Get a replenishment by id  # noqa: E501
        """
        pass

    def test_get_replenishment_files(self):
        """Test case for get_replenishment_files

        Get the files for a replenishment.  # noqa: E501
        """
        pass

    def test_get_replenishment_tags(self):
        """Test case for get_replenishment_tags

        Get the tags for a replenishment.  # noqa: E501
        """
        pass

    def test_update_replenishment_custom_fields(self):
        """Test case for update_replenishment_custom_fields

        Update a replenishment custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
