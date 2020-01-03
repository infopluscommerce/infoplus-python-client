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
from Infoplus.api.edi_document_api import EdiDocumentApi  # noqa: E501
from Infoplus.rest import ApiException


class TestEdiDocumentApi(unittest.TestCase):
    """EdiDocumentApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.edi_document_api.EdiDocumentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_edi_document(self):
        """Test case for add_edi_document

        Create an ediDocument  # noqa: E501
        """
        pass

    def test_add_edi_document_audit(self):
        """Test case for add_edi_document_audit

        Add new audit for an ediDocument  # noqa: E501
        """
        pass

    def test_add_edi_document_file(self):
        """Test case for add_edi_document_file

        Attach a file to an ediDocument  # noqa: E501
        """
        pass

    def test_add_edi_document_tag(self):
        """Test case for add_edi_document_tag

        Add new tags for an ediDocument.  # noqa: E501
        """
        pass

    def test_delete_edi_document_tag(self):
        """Test case for delete_edi_document_tag

        Delete a tag for an ediDocument.  # noqa: E501
        """
        pass

    def test_get_duplicate_edi_document_by_id(self):
        """Test case for get_duplicate_edi_document_by_id

        Get a duplicated an ediDocument by id  # noqa: E501
        """
        pass

    def test_get_edi_document_by_filter(self):
        """Test case for get_edi_document_by_filter

        Search ediDocuments by filter  # noqa: E501
        """
        pass

    def test_get_edi_document_by_id(self):
        """Test case for get_edi_document_by_id

        Get an ediDocument by id  # noqa: E501
        """
        pass

    def test_get_edi_document_tags(self):
        """Test case for get_edi_document_tags

        Get the tags for an ediDocument.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()