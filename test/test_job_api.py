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
from Infoplus.api.job_api import JobApi  # noqa: E501
from Infoplus.rest import ApiException


class TestJobApi(unittest.TestCase):
    """JobApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.job_api.JobApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_job(self):
        """Test case for add_job

        Create a job  # noqa: E501
        """
        pass

    def test_add_job_audit(self):
        """Test case for add_job_audit

        Add new audit for a job  # noqa: E501
        """
        pass

    def test_add_job_file(self):
        """Test case for add_job_file

        Attach a file to a job  # noqa: E501
        """
        pass

    def test_add_job_file_by_url(self):
        """Test case for add_job_file_by_url

        Attach a file to a job by URL.  # noqa: E501
        """
        pass

    def test_add_job_tag(self):
        """Test case for add_job_tag

        Add new tags for a job.  # noqa: E501
        """
        pass

    def test_delete_job(self):
        """Test case for delete_job

        Delete a job  # noqa: E501
        """
        pass

    def test_delete_job_file(self):
        """Test case for delete_job_file

        Delete a file for a job.  # noqa: E501
        """
        pass

    def test_delete_job_tag(self):
        """Test case for delete_job_tag

        Delete a tag for a job.  # noqa: E501
        """
        pass

    def test_execute_job(self):
        """Test case for execute_job

        Run the ExecuteJob process.  # noqa: E501
        """
        pass

    def test_get_duplicate_job_by_id(self):
        """Test case for get_duplicate_job_by_id

        Get a duplicated a job by id  # noqa: E501
        """
        pass

    def test_get_job_by_filter(self):
        """Test case for get_job_by_filter

        Search jobs by filter  # noqa: E501
        """
        pass

    def test_get_job_by_id(self):
        """Test case for get_job_by_id

        Get a job by id  # noqa: E501
        """
        pass

    def test_get_job_files(self):
        """Test case for get_job_files

        Get the files for a job.  # noqa: E501
        """
        pass

    def test_get_job_tags(self):
        """Test case for get_job_tags

        Get the tags for a job.  # noqa: E501
        """
        pass

    def test_update_job(self):
        """Test case for update_job

        Update a job  # noqa: E501
        """
        pass

    def test_update_job_custom_fields(self):
        """Test case for update_job_custom_fields

        Update a job custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
