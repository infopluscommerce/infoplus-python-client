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
from Infoplus.api.job_recipe_api import JobRecipeApi  # noqa: E501
from Infoplus.rest import ApiException


class TestJobRecipeApi(unittest.TestCase):
    """JobRecipeApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.job_recipe_api.JobRecipeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_job_recipe(self):
        """Test case for add_job_recipe

        Create a jobRecipe  # noqa: E501
        """
        pass

    def test_add_job_recipe_audit(self):
        """Test case for add_job_recipe_audit

        Add new audit for a jobRecipe  # noqa: E501
        """
        pass

    def test_add_job_recipe_tag(self):
        """Test case for add_job_recipe_tag

        Add new tags for a jobRecipe.  # noqa: E501
        """
        pass

    def test_delete_job_recipe(self):
        """Test case for delete_job_recipe

        Delete a jobRecipe  # noqa: E501
        """
        pass

    def test_delete_job_recipe_tag(self):
        """Test case for delete_job_recipe_tag

        Delete a tag for a jobRecipe.  # noqa: E501
        """
        pass

    def test_get_duplicate_job_recipe_by_id(self):
        """Test case for get_duplicate_job_recipe_by_id

        Get a duplicated a jobRecipe by id  # noqa: E501
        """
        pass

    def test_get_job_recipe_by_filter(self):
        """Test case for get_job_recipe_by_filter

        Search jobRecipes by filter  # noqa: E501
        """
        pass

    def test_get_job_recipe_by_id(self):
        """Test case for get_job_recipe_by_id

        Get a jobRecipe by id  # noqa: E501
        """
        pass

    def test_get_job_recipe_tags(self):
        """Test case for get_job_recipe_tags

        Get the tags for a jobRecipe.  # noqa: E501
        """
        pass

    def test_update_job_recipe(self):
        """Test case for update_job_recipe

        Update a jobRecipe  # noqa: E501
        """
        pass

    def test_update_job_recipe_custom_fields(self):
        """Test case for update_job_recipe_custom_fields

        Update a jobRecipe custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
