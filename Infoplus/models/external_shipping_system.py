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


class ExternalShippingSystem(object):
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
        'name': 'str',
        'system_type': 'str',
        'script_id': 'int',
        'explode_all_kit_contents': 'bool',
        'api_key': 'str',
        'api_secret': 'str',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'system_type': 'systemType',
        'script_id': 'scriptId',
        'explode_all_kit_contents': 'explodeAllKitContents',
        'api_key': 'apiKey',
        'api_secret': 'apiSecret',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, name=None, system_type=None, script_id=None, explode_all_kit_contents=False, api_key=None, api_secret=None, create_date=None, modify_date=None, custom_fields=None):  # noqa: E501
        """ExternalShippingSystem - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._system_type = None
        self._script_id = None
        self._explode_all_kit_contents = None
        self._api_key = None
        self._api_secret = None
        self._create_date = None
        self._modify_date = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.system_type = system_type
        if script_id is not None:
            self.script_id = script_id
        self.explode_all_kit_contents = explode_all_kit_contents
        self.api_key = api_key
        self.api_secret = api_secret
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this ExternalShippingSystem.  # noqa: E501


        :return: The id of this ExternalShippingSystem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalShippingSystem.


        :param id: The id of this ExternalShippingSystem.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ExternalShippingSystem.  # noqa: E501


        :return: The name of this ExternalShippingSystem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExternalShippingSystem.


        :param name: The name of this ExternalShippingSystem.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def system_type(self):
        """Gets the system_type of this ExternalShippingSystem.  # noqa: E501


        :return: The system_type of this ExternalShippingSystem.  # noqa: E501
        :rtype: str
        """
        return self._system_type

    @system_type.setter
    def system_type(self, system_type):
        """Sets the system_type of this ExternalShippingSystem.


        :param system_type: The system_type of this ExternalShippingSystem.  # noqa: E501
        :type: str
        """
        if system_type is None:
            raise ValueError("Invalid value for `system_type`, must not be `None`")  # noqa: E501

        self._system_type = system_type

    @property
    def script_id(self):
        """Gets the script_id of this ExternalShippingSystem.  # noqa: E501


        :return: The script_id of this ExternalShippingSystem.  # noqa: E501
        :rtype: int
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this ExternalShippingSystem.


        :param script_id: The script_id of this ExternalShippingSystem.  # noqa: E501
        :type: int
        """

        self._script_id = script_id

    @property
    def explode_all_kit_contents(self):
        """Gets the explode_all_kit_contents of this ExternalShippingSystem.  # noqa: E501


        :return: The explode_all_kit_contents of this ExternalShippingSystem.  # noqa: E501
        :rtype: bool
        """
        return self._explode_all_kit_contents

    @explode_all_kit_contents.setter
    def explode_all_kit_contents(self, explode_all_kit_contents):
        """Sets the explode_all_kit_contents of this ExternalShippingSystem.


        :param explode_all_kit_contents: The explode_all_kit_contents of this ExternalShippingSystem.  # noqa: E501
        :type: bool
        """
        if explode_all_kit_contents is None:
            raise ValueError("Invalid value for `explode_all_kit_contents`, must not be `None`")  # noqa: E501

        self._explode_all_kit_contents = explode_all_kit_contents

    @property
    def api_key(self):
        """Gets the api_key of this ExternalShippingSystem.  # noqa: E501


        :return: The api_key of this ExternalShippingSystem.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this ExternalShippingSystem.


        :param api_key: The api_key of this ExternalShippingSystem.  # noqa: E501
        :type: str
        """
        if api_key is None:
            raise ValueError("Invalid value for `api_key`, must not be `None`")  # noqa: E501

        self._api_key = api_key

    @property
    def api_secret(self):
        """Gets the api_secret of this ExternalShippingSystem.  # noqa: E501


        :return: The api_secret of this ExternalShippingSystem.  # noqa: E501
        :rtype: str
        """
        return self._api_secret

    @api_secret.setter
    def api_secret(self, api_secret):
        """Sets the api_secret of this ExternalShippingSystem.


        :param api_secret: The api_secret of this ExternalShippingSystem.  # noqa: E501
        :type: str
        """
        if api_secret is None:
            raise ValueError("Invalid value for `api_secret`, must not be `None`")  # noqa: E501

        self._api_secret = api_secret

    @property
    def create_date(self):
        """Gets the create_date of this ExternalShippingSystem.  # noqa: E501


        :return: The create_date of this ExternalShippingSystem.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this ExternalShippingSystem.


        :param create_date: The create_date of this ExternalShippingSystem.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this ExternalShippingSystem.  # noqa: E501


        :return: The modify_date of this ExternalShippingSystem.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this ExternalShippingSystem.


        :param modify_date: The modify_date of this ExternalShippingSystem.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ExternalShippingSystem.  # noqa: E501


        :return: The custom_fields of this ExternalShippingSystem.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ExternalShippingSystem.


        :param custom_fields: The custom_fields of this ExternalShippingSystem.  # noqa: E501
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
        if not isinstance(other, ExternalShippingSystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
