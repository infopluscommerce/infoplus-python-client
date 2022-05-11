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
from Infoplus.api.location_api import LocationApi  # noqa: E501
from Infoplus.rest import ApiException


class TestLocationApi(unittest.TestCase):
    """LocationApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.location_api.LocationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_location(self):
        """Test case for add_location

        Create a location  # noqa: E501
        """
        pass

    def test_add_location_audit(self):
        """Test case for add_location_audit

        Add new audit for a location  # noqa: E501
        """
        pass

    def test_add_location_file(self):
        """Test case for add_location_file

        Attach a file to a location  # noqa: E501
        """
        pass

    def test_add_location_file_by_url(self):
        """Test case for add_location_file_by_url

        Attach a file to a location by URL.  # noqa: E501
        """
        pass

    def test_add_location_tag(self):
        """Test case for add_location_tag

        Add new tags for a location.  # noqa: E501
        """
        pass

    def test_delete_location(self):
        """Test case for delete_location

        Delete a location  # noqa: E501
        """
        pass

    def test_delete_location_file(self):
        """Test case for delete_location_file

        Delete a file for a location.  # noqa: E501
        """
        pass

    def test_delete_location_tag(self):
        """Test case for delete_location_tag

        Delete a tag for a location.  # noqa: E501
        """
        pass

    def test_get_duplicate_location_by_id(self):
        """Test case for get_duplicate_location_by_id

        Get a duplicated a location by id  # noqa: E501
        """
        pass

    def test_get_location_by_filter(self):
        """Test case for get_location_by_filter

        Search locations by filter  # noqa: E501
        """
        pass

    def test_get_location_by_id(self):
        """Test case for get_location_by_id

        Get a location by id  # noqa: E501
        """
        pass

    def test_get_location_files(self):
        """Test case for get_location_files

        Get the files for a location.  # noqa: E501
        """
        pass

    def test_get_location_tags(self):
        """Test case for get_location_tags

        Get the tags for a location.  # noqa: E501
        """
        pass

    def test_update_location(self):
        """Test case for update_location

        Update a location  # noqa: E501
        """
        pass

    def test_update_location_custom_fields(self):
        """Test case for update_location_custom_fields

        Update a location custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
