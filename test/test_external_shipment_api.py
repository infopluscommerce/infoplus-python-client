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
from Infoplus.api.external_shipment_api import ExternalShipmentApi  # noqa: E501
from Infoplus.rest import ApiException


class TestExternalShipmentApi(unittest.TestCase):
    """ExternalShipmentApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.external_shipment_api.ExternalShipmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_external_shipment(self):
        """Test case for add_external_shipment

        Create an externalShipment  # noqa: E501
        """
        pass

    def test_add_external_shipment_audit(self):
        """Test case for add_external_shipment_audit

        Add new audit for an externalShipment  # noqa: E501
        """
        pass

    def test_add_external_shipment_file(self):
        """Test case for add_external_shipment_file

        Attach a file to an externalShipment  # noqa: E501
        """
        pass

    def test_add_external_shipment_file_by_url(self):
        """Test case for add_external_shipment_file_by_url

        Attach a file to an externalShipment by URL.  # noqa: E501
        """
        pass

    def test_add_external_shipment_tag(self):
        """Test case for add_external_shipment_tag

        Add new tags for an externalShipment.  # noqa: E501
        """
        pass

    def test_delete_external_shipment(self):
        """Test case for delete_external_shipment

        Delete an externalShipment  # noqa: E501
        """
        pass

    def test_delete_external_shipment_file(self):
        """Test case for delete_external_shipment_file

        Delete a file for an externalShipment.  # noqa: E501
        """
        pass

    def test_delete_external_shipment_tag(self):
        """Test case for delete_external_shipment_tag

        Delete a tag for an externalShipment.  # noqa: E501
        """
        pass

    def test_get_duplicate_external_shipment_by_id(self):
        """Test case for get_duplicate_external_shipment_by_id

        Get a duplicated an externalShipment by id  # noqa: E501
        """
        pass

    def test_get_external_shipment_by_filter(self):
        """Test case for get_external_shipment_by_filter

        Search externalShipments by filter  # noqa: E501
        """
        pass

    def test_get_external_shipment_by_id(self):
        """Test case for get_external_shipment_by_id

        Get an externalShipment by id  # noqa: E501
        """
        pass

    def test_get_external_shipment_files(self):
        """Test case for get_external_shipment_files

        Get the files for an externalShipment.  # noqa: E501
        """
        pass

    def test_get_external_shipment_tags(self):
        """Test case for get_external_shipment_tags

        Get the tags for an externalShipment.  # noqa: E501
        """
        pass

    def test_update_external_shipment(self):
        """Test case for update_external_shipment

        Update an externalShipment  # noqa: E501
        """
        pass

    def test_update_external_shipment_custom_fields(self):
        """Test case for update_external_shipment_custom_fields

        Update an externalShipment custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
