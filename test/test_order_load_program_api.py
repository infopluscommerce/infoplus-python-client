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
from Infoplus.api.order_load_program_api import OrderLoadProgramApi  # noqa: E501
from Infoplus.rest import ApiException


class TestOrderLoadProgramApi(unittest.TestCase):
    """OrderLoadProgramApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.order_load_program_api.OrderLoadProgramApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_order_load_program_by_search_text(self):
        """Test case for get_order_load_program_by_search_text

        Search orderLoadPrograms  # noqa: E501
        """
        pass

    def test_get_req_load_program_by_id(self):
        """Test case for get_req_load_program_by_id

        Get an orderLoadProgram by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
