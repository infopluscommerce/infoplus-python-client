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


class ItemSubCategory(object):
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
        'lob_id': 'int',
        'internal_id': 'int',
        'id': 'str',
        'name': 'str',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'lob_id': 'lobId',
        'internal_id': 'internalId',
        'id': 'id',
        'name': 'name',
        'custom_fields': 'customFields'
    }

    def __init__(self, lob_id=None, internal_id=None, id=None, name=None, custom_fields=None):  # noqa: E501
        """ItemSubCategory - a model defined in Swagger"""  # noqa: E501

        self._lob_id = None
        self._internal_id = None
        self._id = None
        self._name = None
        self._custom_fields = None
        self.discriminator = None

        self.lob_id = lob_id
        if internal_id is not None:
            self.internal_id = internal_id
        self.id = id
        self.name = name
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def lob_id(self):
        """Gets the lob_id of this ItemSubCategory.  # noqa: E501


        :return: The lob_id of this ItemSubCategory.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this ItemSubCategory.


        :param lob_id: The lob_id of this ItemSubCategory.  # noqa: E501
        :type: int
        """
        if lob_id is None:
            raise ValueError("Invalid value for `lob_id`, must not be `None`")  # noqa: E501

        self._lob_id = lob_id

    @property
    def internal_id(self):
        """Gets the internal_id of this ItemSubCategory.  # noqa: E501


        :return: The internal_id of this ItemSubCategory.  # noqa: E501
        :rtype: int
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """Sets the internal_id of this ItemSubCategory.


        :param internal_id: The internal_id of this ItemSubCategory.  # noqa: E501
        :type: int
        """

        self._internal_id = internal_id

    @property
    def id(self):
        """Gets the id of this ItemSubCategory.  # noqa: E501


        :return: The id of this ItemSubCategory.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ItemSubCategory.


        :param id: The id of this ItemSubCategory.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this ItemSubCategory.  # noqa: E501


        :return: The name of this ItemSubCategory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemSubCategory.


        :param name: The name of this ItemSubCategory.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ItemSubCategory.  # noqa: E501


        :return: The custom_fields of this ItemSubCategory.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ItemSubCategory.


        :param custom_fields: The custom_fields of this ItemSubCategory.  # noqa: E501
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
        if not isinstance(other, ItemSubCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
