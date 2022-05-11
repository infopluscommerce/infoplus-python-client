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


class ProcessOutputAPIModel(object):
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
        'id': 'object',
        'status': 'str',
        'entity': 'object',
        'message_list': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'entity': 'entity',
        'message_list': 'messageList'
    }

    def __init__(self, id=None, status=None, entity=None, message_list=None):  # noqa: E501
        """ProcessOutputAPIModel - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._status = None
        self._entity = None
        self._message_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if entity is not None:
            self.entity = entity
        if message_list is not None:
            self.message_list = message_list

    @property
    def id(self):
        """Gets the id of this ProcessOutputAPIModel.  # noqa: E501


        :return: The id of this ProcessOutputAPIModel.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProcessOutputAPIModel.


        :param id: The id of this ProcessOutputAPIModel.  # noqa: E501
        :type: object
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this ProcessOutputAPIModel.  # noqa: E501


        :return: The status of this ProcessOutputAPIModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProcessOutputAPIModel.


        :param status: The status of this ProcessOutputAPIModel.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def entity(self):
        """Gets the entity of this ProcessOutputAPIModel.  # noqa: E501


        :return: The entity of this ProcessOutputAPIModel.  # noqa: E501
        :rtype: object
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this ProcessOutputAPIModel.


        :param entity: The entity of this ProcessOutputAPIModel.  # noqa: E501
        :type: object
        """

        self._entity = entity

    @property
    def message_list(self):
        """Gets the message_list of this ProcessOutputAPIModel.  # noqa: E501


        :return: The message_list of this ProcessOutputAPIModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._message_list

    @message_list.setter
    def message_list(self, message_list):
        """Sets the message_list of this ProcessOutputAPIModel.


        :param message_list: The message_list of this ProcessOutputAPIModel.  # noqa: E501
        :type: list[str]
        """

        self._message_list = message_list

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
        if not isinstance(other, ProcessOutputAPIModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
