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
from Infoplus.api.scheduled_plan_log_api import ScheduledPlanLogApi  # noqa: E501
from Infoplus.rest import ApiException


class TestScheduledPlanLogApi(unittest.TestCase):
    """ScheduledPlanLogApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.scheduled_plan_log_api.ScheduledPlanLogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_scheduled_plan_log_audit(self):
        """Test case for add_scheduled_plan_log_audit

        Add new audit for a scheduledPlanLog  # noqa: E501
        """
        pass

    def test_add_scheduled_plan_log_file(self):
        """Test case for add_scheduled_plan_log_file

        Attach a file to a scheduledPlanLog  # noqa: E501
        """
        pass

    def test_add_scheduled_plan_log_file_by_url(self):
        """Test case for add_scheduled_plan_log_file_by_url

        Attach a file to a scheduledPlanLog by URL.  # noqa: E501
        """
        pass

    def test_add_scheduled_plan_log_tag(self):
        """Test case for add_scheduled_plan_log_tag

        Add new tags for a scheduledPlanLog.  # noqa: E501
        """
        pass

    def test_delete_scheduled_plan_log_file(self):
        """Test case for delete_scheduled_plan_log_file

        Delete a file for a scheduledPlanLog.  # noqa: E501
        """
        pass

    def test_delete_scheduled_plan_log_tag(self):
        """Test case for delete_scheduled_plan_log_tag

        Delete a tag for a scheduledPlanLog.  # noqa: E501
        """
        pass

    def test_get_duplicate_scheduled_plan_log_by_id(self):
        """Test case for get_duplicate_scheduled_plan_log_by_id

        Get a duplicated a scheduledPlanLog by id  # noqa: E501
        """
        pass

    def test_get_scheduled_plan_log_by_filter(self):
        """Test case for get_scheduled_plan_log_by_filter

        Search scheduledPlanLogs by filter  # noqa: E501
        """
        pass

    def test_get_scheduled_plan_log_by_id(self):
        """Test case for get_scheduled_plan_log_by_id

        Get a scheduledPlanLog by id  # noqa: E501
        """
        pass

    def test_get_scheduled_plan_log_files(self):
        """Test case for get_scheduled_plan_log_files

        Get the files for a scheduledPlanLog.  # noqa: E501
        """
        pass

    def test_get_scheduled_plan_log_tags(self):
        """Test case for get_scheduled_plan_log_tags

        Get the tags for a scheduledPlanLog.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
