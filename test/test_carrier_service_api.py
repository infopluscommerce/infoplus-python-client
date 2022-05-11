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
from Infoplus.api.carrier_service_api import CarrierServiceApi  # noqa: E501
from Infoplus.rest import ApiException


class TestCarrierServiceApi(unittest.TestCase):
    """CarrierServiceApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.carrier_service_api.CarrierServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_carrier_service_by_id(self):
        """Test case for get_carrier_service_by_id

        Get a carrierService by id  # noqa: E501
        """
        pass

    def test_get_carrier_service_by_search_text(self):
        """Test case for get_carrier_service_by_search_text

        Search carrierServices  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
