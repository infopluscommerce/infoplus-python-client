# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: beta
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EmailTemplate(object):
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
        'lob_id': 'int',
        'subject': 'str',
        'name': 'str',
        'from_name': 'str',
        'from_address': 'str',
        'to_name': 'str',
        'to_address': 'str',
        'cc_address': 'str',
        'bcc_address': 'str',
        'email_template_type': 'str',
        'record_type': 'str',
        'api_version': 'str',
        'script_id': 'int',
        'send_to_bill_to': 'bool',
        'send_to_ship_to': 'bool',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'lob_id': 'lobId',
        'subject': 'subject',
        'name': 'name',
        'from_name': 'fromName',
        'from_address': 'fromAddress',
        'to_name': 'toName',
        'to_address': 'toAddress',
        'cc_address': 'ccAddress',
        'bcc_address': 'bccAddress',
        'email_template_type': 'emailTemplateType',
        'record_type': 'recordType',
        'api_version': 'apiVersion',
        'script_id': 'scriptId',
        'send_to_bill_to': 'sendToBillTo',
        'send_to_ship_to': 'sendToShipTo',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, lob_id=None, subject=None, name=None, from_name=None, from_address=None, to_name=None, to_address=None, cc_address=None, bcc_address=None, email_template_type=None, record_type=None, api_version=None, script_id=None, send_to_bill_to=False, send_to_ship_to=False, create_date=None, modify_date=None, custom_fields=None):  # noqa: E501
        """EmailTemplate - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._lob_id = None
        self._subject = None
        self._name = None
        self._from_name = None
        self._from_address = None
        self._to_name = None
        self._to_address = None
        self._cc_address = None
        self._bcc_address = None
        self._email_template_type = None
        self._record_type = None
        self._api_version = None
        self._script_id = None
        self._send_to_bill_to = None
        self._send_to_ship_to = None
        self._create_date = None
        self._modify_date = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.lob_id = lob_id
        self.subject = subject
        self.name = name
        self.from_name = from_name
        self.from_address = from_address
        if to_name is not None:
            self.to_name = to_name
        if to_address is not None:
            self.to_address = to_address
        if cc_address is not None:
            self.cc_address = cc_address
        if bcc_address is not None:
            self.bcc_address = bcc_address
        self.email_template_type = email_template_type
        if record_type is not None:
            self.record_type = record_type
        if api_version is not None:
            self.api_version = api_version
        if script_id is not None:
            self.script_id = script_id
        if send_to_bill_to is not None:
            self.send_to_bill_to = send_to_bill_to
        if send_to_ship_to is not None:
            self.send_to_ship_to = send_to_ship_to
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this EmailTemplate.  # noqa: E501


        :return: The id of this EmailTemplate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmailTemplate.


        :param id: The id of this EmailTemplate.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def lob_id(self):
        """Gets the lob_id of this EmailTemplate.  # noqa: E501


        :return: The lob_id of this EmailTemplate.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this EmailTemplate.


        :param lob_id: The lob_id of this EmailTemplate.  # noqa: E501
        :type: int
        """
        if lob_id is None:
            raise ValueError("Invalid value for `lob_id`, must not be `None`")  # noqa: E501

        self._lob_id = lob_id

    @property
    def subject(self):
        """Gets the subject of this EmailTemplate.  # noqa: E501


        :return: The subject of this EmailTemplate.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this EmailTemplate.


        :param subject: The subject of this EmailTemplate.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def name(self):
        """Gets the name of this EmailTemplate.  # noqa: E501


        :return: The name of this EmailTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmailTemplate.


        :param name: The name of this EmailTemplate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def from_name(self):
        """Gets the from_name of this EmailTemplate.  # noqa: E501


        :return: The from_name of this EmailTemplate.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this EmailTemplate.


        :param from_name: The from_name of this EmailTemplate.  # noqa: E501
        :type: str
        """
        if from_name is None:
            raise ValueError("Invalid value for `from_name`, must not be `None`")  # noqa: E501

        self._from_name = from_name

    @property
    def from_address(self):
        """Gets the from_address of this EmailTemplate.  # noqa: E501


        :return: The from_address of this EmailTemplate.  # noqa: E501
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """Sets the from_address of this EmailTemplate.


        :param from_address: The from_address of this EmailTemplate.  # noqa: E501
        :type: str
        """
        if from_address is None:
            raise ValueError("Invalid value for `from_address`, must not be `None`")  # noqa: E501

        self._from_address = from_address

    @property
    def to_name(self):
        """Gets the to_name of this EmailTemplate.  # noqa: E501


        :return: The to_name of this EmailTemplate.  # noqa: E501
        :rtype: str
        """
        return self._to_name

    @to_name.setter
    def to_name(self, to_name):
        """Sets the to_name of this EmailTemplate.


        :param to_name: The to_name of this EmailTemplate.  # noqa: E501
        :type: str
        """

        self._to_name = to_name

    @property
    def to_address(self):
        """Gets the to_address of this EmailTemplate.  # noqa: E501


        :return: The to_address of this EmailTemplate.  # noqa: E501
        :rtype: str
        """
        return self._to_address

    @to_address.setter
    def to_address(self, to_address):
        """Sets the to_address of this EmailTemplate.


        :param to_address: The to_address of this EmailTemplate.  # noqa: E501
        :type: str
        """

        self._to_address = to_address

    @property
    def cc_address(self):
        """Gets the cc_address of this EmailTemplate.  # noqa: E501


        :return: The cc_address of this EmailTemplate.  # noqa: E501
        :rtype: str
        """
        return self._cc_address

    @cc_address.setter
    def cc_address(self, cc_address):
        """Sets the cc_address of this EmailTemplate.


        :param cc_address: The cc_address of this EmailTemplate.  # noqa: E501
        :type: str
        """

        self._cc_address = cc_address

    @property
    def bcc_address(self):
        """Gets the bcc_address of this EmailTemplate.  # noqa: E501


        :return: The bcc_address of this EmailTemplate.  # noqa: E501
        :rtype: str
        """
        return self._bcc_address

    @bcc_address.setter
    def bcc_address(self, bcc_address):
        """Sets the bcc_address of this EmailTemplate.


        :param bcc_address: The bcc_address of this EmailTemplate.  # noqa: E501
        :type: str
        """

        self._bcc_address = bcc_address

    @property
    def email_template_type(self):
        """Gets the email_template_type of this EmailTemplate.  # noqa: E501


        :return: The email_template_type of this EmailTemplate.  # noqa: E501
        :rtype: str
        """
        return self._email_template_type

    @email_template_type.setter
    def email_template_type(self, email_template_type):
        """Sets the email_template_type of this EmailTemplate.


        :param email_template_type: The email_template_type of this EmailTemplate.  # noqa: E501
        :type: str
        """
        if email_template_type is None:
            raise ValueError("Invalid value for `email_template_type`, must not be `None`")  # noqa: E501

        self._email_template_type = email_template_type

    @property
    def record_type(self):
        """Gets the record_type of this EmailTemplate.  # noqa: E501


        :return: The record_type of this EmailTemplate.  # noqa: E501
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this EmailTemplate.


        :param record_type: The record_type of this EmailTemplate.  # noqa: E501
        :type: str
        """

        self._record_type = record_type

    @property
    def api_version(self):
        """Gets the api_version of this EmailTemplate.  # noqa: E501


        :return: The api_version of this EmailTemplate.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this EmailTemplate.


        :param api_version: The api_version of this EmailTemplate.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def script_id(self):
        """Gets the script_id of this EmailTemplate.  # noqa: E501


        :return: The script_id of this EmailTemplate.  # noqa: E501
        :rtype: int
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this EmailTemplate.


        :param script_id: The script_id of this EmailTemplate.  # noqa: E501
        :type: int
        """

        self._script_id = script_id

    @property
    def send_to_bill_to(self):
        """Gets the send_to_bill_to of this EmailTemplate.  # noqa: E501


        :return: The send_to_bill_to of this EmailTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._send_to_bill_to

    @send_to_bill_to.setter
    def send_to_bill_to(self, send_to_bill_to):
        """Sets the send_to_bill_to of this EmailTemplate.


        :param send_to_bill_to: The send_to_bill_to of this EmailTemplate.  # noqa: E501
        :type: bool
        """

        self._send_to_bill_to = send_to_bill_to

    @property
    def send_to_ship_to(self):
        """Gets the send_to_ship_to of this EmailTemplate.  # noqa: E501


        :return: The send_to_ship_to of this EmailTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._send_to_ship_to

    @send_to_ship_to.setter
    def send_to_ship_to(self, send_to_ship_to):
        """Sets the send_to_ship_to of this EmailTemplate.


        :param send_to_ship_to: The send_to_ship_to of this EmailTemplate.  # noqa: E501
        :type: bool
        """

        self._send_to_ship_to = send_to_ship_to

    @property
    def create_date(self):
        """Gets the create_date of this EmailTemplate.  # noqa: E501


        :return: The create_date of this EmailTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this EmailTemplate.


        :param create_date: The create_date of this EmailTemplate.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this EmailTemplate.  # noqa: E501


        :return: The modify_date of this EmailTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this EmailTemplate.


        :param modify_date: The modify_date of this EmailTemplate.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def custom_fields(self):
        """Gets the custom_fields of this EmailTemplate.  # noqa: E501


        :return: The custom_fields of this EmailTemplate.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this EmailTemplate.


        :param custom_fields: The custom_fields of this EmailTemplate.  # noqa: E501
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
        if not isinstance(other, EmailTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
