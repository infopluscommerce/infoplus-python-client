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
from Infoplus.api.alert_api import AlertApi  # noqa: E501
from Infoplus.rest import ApiException


class TestAlertApi(unittest.TestCase):
    """AlertApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.alert_api.AlertApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_alert(self):
        """Test case for add_alert

        Create an alert  # noqa: E501
        """
        pass

    def test_add_alert_audit(self):
        """Test case for add_alert_audit

        Add new audit for an alert  # noqa: E501
        """
        pass

    def test_add_alert_file(self):
        """Test case for add_alert_file

        Attach a file to an alert  # noqa: E501
        """
        pass

    def test_add_alert_file_by_url(self):
        """Test case for add_alert_file_by_url

        Attach a file to an alert by URL.  # noqa: E501
        """
        pass

    def test_add_alert_tag(self):
        """Test case for add_alert_tag

        Add new tags for an alert.  # noqa: E501
        """
        pass

    def test_delete_alert_file(self):
        """Test case for delete_alert_file

        Delete a file for an alert.  # noqa: E501
        """
        pass

    def test_delete_alert_tag(self):
        """Test case for delete_alert_tag

        Delete a tag for an alert.  # noqa: E501
        """
        pass

    def test_get_alert_by_filter(self):
        """Test case for get_alert_by_filter

        Search alerts by filter  # noqa: E501
        """
        pass

    def test_get_alert_by_id(self):
        """Test case for get_alert_by_id

        Get an alert by id  # noqa: E501
        """
        pass

    def test_get_alert_files(self):
        """Test case for get_alert_files

        Get the files for an alert.  # noqa: E501
        """
        pass

    def test_get_alert_tags(self):
        """Test case for get_alert_tags

        Get the tags for an alert.  # noqa: E501
        """
        pass

    def test_get_duplicate_alert_by_id(self):
        """Test case for get_duplicate_alert_by_id

        Get a duplicated an alert by id  # noqa: E501
        """
        pass

    def test_update_alert_custom_fields(self):
        """Test case for update_alert_custom_fields

        Update an alert custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
