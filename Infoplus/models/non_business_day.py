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


class NonBusinessDay(object):
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
        'date': 'datetime',
        'note': 'str',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'date': 'date',
        'note': 'note',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, date=None, note=None, create_date=None, modify_date=None, custom_fields=None):  # noqa: E501
        """NonBusinessDay - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._date = None
        self._note = None
        self._create_date = None
        self._modify_date = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if date is not None:
            self.date = date
        if note is not None:
            self.note = note
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this NonBusinessDay.  # noqa: E501


        :return: The id of this NonBusinessDay.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NonBusinessDay.


        :param id: The id of this NonBusinessDay.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def date(self):
        """Gets the date of this NonBusinessDay.  # noqa: E501


        :return: The date of this NonBusinessDay.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this NonBusinessDay.


        :param date: The date of this NonBusinessDay.  # noqa: E501
        :type: datetime
        """

        self._date = date

    @property
    def note(self):
        """Gets the note of this NonBusinessDay.  # noqa: E501


        :return: The note of this NonBusinessDay.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this NonBusinessDay.


        :param note: The note of this NonBusinessDay.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def create_date(self):
        """Gets the create_date of this NonBusinessDay.  # noqa: E501


        :return: The create_date of this NonBusinessDay.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this NonBusinessDay.


        :param create_date: The create_date of this NonBusinessDay.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this NonBusinessDay.  # noqa: E501


        :return: The modify_date of this NonBusinessDay.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this NonBusinessDay.


        :param modify_date: The modify_date of this NonBusinessDay.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def custom_fields(self):
        """Gets the custom_fields of this NonBusinessDay.  # noqa: E501


        :return: The custom_fields of this NonBusinessDay.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this NonBusinessDay.


        :param custom_fields: The custom_fields of this NonBusinessDay.  # noqa: E501
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
        if not isinstance(other, NonBusinessDay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other