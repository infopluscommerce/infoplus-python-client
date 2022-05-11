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


class OrderExtraLineItemData(object):
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
        'sku': 'str',
        'category': 'str',
        'code': 'str',
        'value': 'str',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'sku': 'sku',
        'category': 'category',
        'code': 'code',
        'value': 'value',
        'custom_fields': 'customFields'
    }

    def __init__(self, sku=None, category=None, code=None, value=None, custom_fields=None):  # noqa: E501
        """OrderExtraLineItemData - a model defined in Swagger"""  # noqa: E501

        self._sku = None
        self._category = None
        self._code = None
        self._value = None
        self._custom_fields = None
        self.discriminator = None

        if sku is not None:
            self.sku = sku
        if category is not None:
            self.category = category
        if code is not None:
            self.code = code
        if value is not None:
            self.value = value
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def sku(self):
        """Gets the sku of this OrderExtraLineItemData.  # noqa: E501


        :return: The sku of this OrderExtraLineItemData.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this OrderExtraLineItemData.


        :param sku: The sku of this OrderExtraLineItemData.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def category(self):
        """Gets the category of this OrderExtraLineItemData.  # noqa: E501


        :return: The category of this OrderExtraLineItemData.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this OrderExtraLineItemData.


        :param category: The category of this OrderExtraLineItemData.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def code(self):
        """Gets the code of this OrderExtraLineItemData.  # noqa: E501


        :return: The code of this OrderExtraLineItemData.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this OrderExtraLineItemData.


        :param code: The code of this OrderExtraLineItemData.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def value(self):
        """Gets the value of this OrderExtraLineItemData.  # noqa: E501


        :return: The value of this OrderExtraLineItemData.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OrderExtraLineItemData.


        :param value: The value of this OrderExtraLineItemData.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def custom_fields(self):
        """Gets the custom_fields of this OrderExtraLineItemData.  # noqa: E501


        :return: The custom_fields of this OrderExtraLineItemData.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this OrderExtraLineItemData.


        :param custom_fields: The custom_fields of this OrderExtraLineItemData.  # noqa: E501
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
        if not isinstance(other, OrderExtraLineItemData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
