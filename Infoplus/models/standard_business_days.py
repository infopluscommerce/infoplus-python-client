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


class StandardBusinessDays(object):
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
        'sunday': 'bool',
        'monday': 'bool',
        'tuesday': 'bool',
        'wednesday': 'bool',
        'thursday': 'bool',
        'friday': 'bool',
        'saturday': 'bool',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'sunday': 'sunday',
        'monday': 'monday',
        'tuesday': 'tuesday',
        'wednesday': 'wednesday',
        'thursday': 'thursday',
        'friday': 'friday',
        'saturday': 'saturday',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, sunday=False, monday=False, tuesday=False, wednesday=False, thursday=False, friday=False, saturday=False, create_date=None, modify_date=None, custom_fields=None):  # noqa: E501
        """StandardBusinessDays - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._sunday = None
        self._monday = None
        self._tuesday = None
        self._wednesday = None
        self._thursday = None
        self._friday = None
        self._saturday = None
        self._create_date = None
        self._modify_date = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sunday is not None:
            self.sunday = sunday
        if monday is not None:
            self.monday = monday
        if tuesday is not None:
            self.tuesday = tuesday
        if wednesday is not None:
            self.wednesday = wednesday
        if thursday is not None:
            self.thursday = thursday
        if friday is not None:
            self.friday = friday
        if saturday is not None:
            self.saturday = saturday
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this StandardBusinessDays.  # noqa: E501


        :return: The id of this StandardBusinessDays.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StandardBusinessDays.


        :param id: The id of this StandardBusinessDays.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def sunday(self):
        """Gets the sunday of this StandardBusinessDays.  # noqa: E501


        :return: The sunday of this StandardBusinessDays.  # noqa: E501
        :rtype: bool
        """
        return self._sunday

    @sunday.setter
    def sunday(self, sunday):
        """Sets the sunday of this StandardBusinessDays.


        :param sunday: The sunday of this StandardBusinessDays.  # noqa: E501
        :type: bool
        """

        self._sunday = sunday

    @property
    def monday(self):
        """Gets the monday of this StandardBusinessDays.  # noqa: E501


        :return: The monday of this StandardBusinessDays.  # noqa: E501
        :rtype: bool
        """
        return self._monday

    @monday.setter
    def monday(self, monday):
        """Sets the monday of this StandardBusinessDays.


        :param monday: The monday of this StandardBusinessDays.  # noqa: E501
        :type: bool
        """

        self._monday = monday

    @property
    def tuesday(self):
        """Gets the tuesday of this StandardBusinessDays.  # noqa: E501


        :return: The tuesday of this StandardBusinessDays.  # noqa: E501
        :rtype: bool
        """
        return self._tuesday

    @tuesday.setter
    def tuesday(self, tuesday):
        """Sets the tuesday of this StandardBusinessDays.


        :param tuesday: The tuesday of this StandardBusinessDays.  # noqa: E501
        :type: bool
        """

        self._tuesday = tuesday

    @property
    def wednesday(self):
        """Gets the wednesday of this StandardBusinessDays.  # noqa: E501


        :return: The wednesday of this StandardBusinessDays.  # noqa: E501
        :rtype: bool
        """
        return self._wednesday

    @wednesday.setter
    def wednesday(self, wednesday):
        """Sets the wednesday of this StandardBusinessDays.


        :param wednesday: The wednesday of this StandardBusinessDays.  # noqa: E501
        :type: bool
        """

        self._wednesday = wednesday

    @property
    def thursday(self):
        """Gets the thursday of this StandardBusinessDays.  # noqa: E501


        :return: The thursday of this StandardBusinessDays.  # noqa: E501
        :rtype: bool
        """
        return self._thursday

    @thursday.setter
    def thursday(self, thursday):
        """Sets the thursday of this StandardBusinessDays.


        :param thursday: The thursday of this StandardBusinessDays.  # noqa: E501
        :type: bool
        """

        self._thursday = thursday

    @property
    def friday(self):
        """Gets the friday of this StandardBusinessDays.  # noqa: E501


        :return: The friday of this StandardBusinessDays.  # noqa: E501
        :rtype: bool
        """
        return self._friday

    @friday.setter
    def friday(self, friday):
        """Sets the friday of this StandardBusinessDays.


        :param friday: The friday of this StandardBusinessDays.  # noqa: E501
        :type: bool
        """

        self._friday = friday

    @property
    def saturday(self):
        """Gets the saturday of this StandardBusinessDays.  # noqa: E501


        :return: The saturday of this StandardBusinessDays.  # noqa: E501
        :rtype: bool
        """
        return self._saturday

    @saturday.setter
    def saturday(self, saturday):
        """Sets the saturday of this StandardBusinessDays.


        :param saturday: The saturday of this StandardBusinessDays.  # noqa: E501
        :type: bool
        """

        self._saturday = saturday

    @property
    def create_date(self):
        """Gets the create_date of this StandardBusinessDays.  # noqa: E501


        :return: The create_date of this StandardBusinessDays.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this StandardBusinessDays.


        :param create_date: The create_date of this StandardBusinessDays.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this StandardBusinessDays.  # noqa: E501


        :return: The modify_date of this StandardBusinessDays.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this StandardBusinessDays.


        :param modify_date: The modify_date of this StandardBusinessDays.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def custom_fields(self):
        """Gets the custom_fields of this StandardBusinessDays.  # noqa: E501


        :return: The custom_fields of this StandardBusinessDays.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this StandardBusinessDays.


        :param custom_fields: The custom_fields of this StandardBusinessDays.  # noqa: E501
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
        if not isinstance(other, StandardBusinessDays):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
