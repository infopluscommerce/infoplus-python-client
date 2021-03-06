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
from Infoplus.api.email_template_api import EmailTemplateApi  # noqa: E501
from Infoplus.rest import ApiException


class TestEmailTemplateApi(unittest.TestCase):
    """EmailTemplateApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.email_template_api.EmailTemplateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_email_template(self):
        """Test case for add_email_template

        Create an emailTemplate  # noqa: E501
        """
        pass

    def test_add_email_template_audit(self):
        """Test case for add_email_template_audit

        Add new audit for an emailTemplate  # noqa: E501
        """
        pass

    def test_add_email_template_file(self):
        """Test case for add_email_template_file

        Attach a file to an emailTemplate  # noqa: E501
        """
        pass

    def test_add_email_template_file_by_url(self):
        """Test case for add_email_template_file_by_url

        Attach a file to an emailTemplate by URL.  # noqa: E501
        """
        pass

    def test_add_email_template_tag(self):
        """Test case for add_email_template_tag

        Add new tags for an emailTemplate.  # noqa: E501
        """
        pass

    def test_delete_email_template(self):
        """Test case for delete_email_template

        Delete an emailTemplate  # noqa: E501
        """
        pass

    def test_delete_email_template_file(self):
        """Test case for delete_email_template_file

        Delete a file for an emailTemplate.  # noqa: E501
        """
        pass

    def test_delete_email_template_tag(self):
        """Test case for delete_email_template_tag

        Delete a tag for an emailTemplate.  # noqa: E501
        """
        pass

    def test_get_duplicate_email_template_by_id(self):
        """Test case for get_duplicate_email_template_by_id

        Get a duplicated an emailTemplate by id  # noqa: E501
        """
        pass

    def test_get_email_template_by_filter(self):
        """Test case for get_email_template_by_filter

        Search emailTemplates by filter  # noqa: E501
        """
        pass

    def test_get_email_template_by_id(self):
        """Test case for get_email_template_by_id

        Get an emailTemplate by id  # noqa: E501
        """
        pass

    def test_get_email_template_files(self):
        """Test case for get_email_template_files

        Get the files for an emailTemplate.  # noqa: E501
        """
        pass

    def test_get_email_template_tags(self):
        """Test case for get_email_template_tags

        Get the tags for an emailTemplate.  # noqa: E501
        """
        pass

    def test_update_email_template(self):
        """Test case for update_email_template

        Update an emailTemplate  # noqa: E501
        """
        pass

    def test_update_email_template_custom_fields(self):
        """Test case for update_email_template_custom_fields

        Update an emailTemplate custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
