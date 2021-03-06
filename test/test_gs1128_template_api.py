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
from Infoplus.api.gs1128_template_api import Gs1128TemplateApi  # noqa: E501
from Infoplus.rest import ApiException


class TestGs1128TemplateApi(unittest.TestCase):
    """Gs1128TemplateApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.gs1128_template_api.Gs1128TemplateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_gs1128_template(self):
        """Test case for add_gs1128_template

        Create a gs1128Template  # noqa: E501
        """
        pass

    def test_add_gs1128_template_audit(self):
        """Test case for add_gs1128_template_audit

        Add new audit for a gs1128Template  # noqa: E501
        """
        pass

    def test_add_gs1128_template_file(self):
        """Test case for add_gs1128_template_file

        Attach a file to a gs1128Template  # noqa: E501
        """
        pass

    def test_add_gs1128_template_file_by_url(self):
        """Test case for add_gs1128_template_file_by_url

        Attach a file to a gs1128Template by URL.  # noqa: E501
        """
        pass

    def test_add_gs1128_template_tag(self):
        """Test case for add_gs1128_template_tag

        Add new tags for a gs1128Template.  # noqa: E501
        """
        pass

    def test_delete_gs1128_template(self):
        """Test case for delete_gs1128_template

        Delete a gs1128Template  # noqa: E501
        """
        pass

    def test_delete_gs1128_template_file(self):
        """Test case for delete_gs1128_template_file

        Delete a file for a gs1128Template.  # noqa: E501
        """
        pass

    def test_delete_gs1128_template_tag(self):
        """Test case for delete_gs1128_template_tag

        Delete a tag for a gs1128Template.  # noqa: E501
        """
        pass

    def test_get_duplicate_gs1128_template_by_id(self):
        """Test case for get_duplicate_gs1128_template_by_id

        Get a duplicated a gs1128Template by id  # noqa: E501
        """
        pass

    def test_get_gs1128_template_by_filter(self):
        """Test case for get_gs1128_template_by_filter

        Search gs1128Templates by filter  # noqa: E501
        """
        pass

    def test_get_gs1128_template_by_id(self):
        """Test case for get_gs1128_template_by_id

        Get a gs1128Template by id  # noqa: E501
        """
        pass

    def test_get_gs1128_template_files(self):
        """Test case for get_gs1128_template_files

        Get the files for a gs1128Template.  # noqa: E501
        """
        pass

    def test_get_gs1128_template_tags(self):
        """Test case for get_gs1128_template_tags

        Get the tags for a gs1128Template.  # noqa: E501
        """
        pass

    def test_update_gs1128_template(self):
        """Test case for update_gs1128_template

        Update a gs1128Template  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
