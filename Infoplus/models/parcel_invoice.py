# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: v3.0
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ParcelInvoice(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'carrier': 'str',
        'invoice_no': 'str',
        'account_no': 'str',
        'invoice_date': 'datetime',
        'invoice_amount': 'float',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'carrier': 'carrier',
        'invoice_no': 'invoiceNo',
        'account_no': 'accountNo',
        'invoice_date': 'invoiceDate',
        'invoice_amount': 'invoiceAmount',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, create_date=None, modify_date=None, carrier=None, invoice_no=None, account_no=None, invoice_date=None, invoice_amount=None, custom_fields=None):  # noqa: E501
        """ParcelInvoice - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._carrier = None
        self._invoice_no = None
        self._account_no = None
        self._invoice_date = None
        self._invoice_amount = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if carrier is not None:
            self.carrier = carrier
        if invoice_no is not None:
            self.invoice_no = invoice_no
        if account_no is not None:
            self.account_no = account_no
        if invoice_date is not None:
            self.invoice_date = invoice_date
        if invoice_amount is not None:
            self.invoice_amount = invoice_amount
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this ParcelInvoice.  # noqa: E501


        :return: The id of this ParcelInvoice.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ParcelInvoice.


        :param id: The id of this ParcelInvoice.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this ParcelInvoice.  # noqa: E501


        :return: The create_date of this ParcelInvoice.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this ParcelInvoice.


        :param create_date: The create_date of this ParcelInvoice.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this ParcelInvoice.  # noqa: E501


        :return: The modify_date of this ParcelInvoice.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this ParcelInvoice.


        :param modify_date: The modify_date of this ParcelInvoice.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def carrier(self):
        """Gets the carrier of this ParcelInvoice.  # noqa: E501


        :return: The carrier of this ParcelInvoice.  # noqa: E501
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this ParcelInvoice.


        :param carrier: The carrier of this ParcelInvoice.  # noqa: E501
        :type: str
        """

        self._carrier = carrier

    @property
    def invoice_no(self):
        """Gets the invoice_no of this ParcelInvoice.  # noqa: E501


        :return: The invoice_no of this ParcelInvoice.  # noqa: E501
        :rtype: str
        """
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, invoice_no):
        """Sets the invoice_no of this ParcelInvoice.


        :param invoice_no: The invoice_no of this ParcelInvoice.  # noqa: E501
        :type: str
        """

        self._invoice_no = invoice_no

    @property
    def account_no(self):
        """Gets the account_no of this ParcelInvoice.  # noqa: E501


        :return: The account_no of this ParcelInvoice.  # noqa: E501
        :rtype: str
        """
        return self._account_no

    @account_no.setter
    def account_no(self, account_no):
        """Sets the account_no of this ParcelInvoice.


        :param account_no: The account_no of this ParcelInvoice.  # noqa: E501
        :type: str
        """

        self._account_no = account_no

    @property
    def invoice_date(self):
        """Gets the invoice_date of this ParcelInvoice.  # noqa: E501


        :return: The invoice_date of this ParcelInvoice.  # noqa: E501
        :rtype: datetime
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """Sets the invoice_date of this ParcelInvoice.


        :param invoice_date: The invoice_date of this ParcelInvoice.  # noqa: E501
        :type: datetime
        """

        self._invoice_date = invoice_date

    @property
    def invoice_amount(self):
        """Gets the invoice_amount of this ParcelInvoice.  # noqa: E501


        :return: The invoice_amount of this ParcelInvoice.  # noqa: E501
        :rtype: float
        """
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, invoice_amount):
        """Sets the invoice_amount of this ParcelInvoice.


        :param invoice_amount: The invoice_amount of this ParcelInvoice.  # noqa: E501
        :type: float
        """

        self._invoice_amount = invoice_amount

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ParcelInvoice.  # noqa: E501


        :return: The custom_fields of this ParcelInvoice.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ParcelInvoice.


        :param custom_fields: The custom_fields of this ParcelInvoice.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ParcelInvoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
