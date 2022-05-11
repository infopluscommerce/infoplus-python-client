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


class Zone(object):
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
        'warehouse_id': 'int',
        'name': 'str',
        'address': 'str',
        'is_climate_controlled': 'bool',
        'is_food_grade': 'bool',
        'is_secure': 'bool',
        'is_frozen': 'bool',
        'is_refrigerated': 'bool',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'warehouse_id': 'warehouseId',
        'name': 'name',
        'address': 'address',
        'is_climate_controlled': 'isClimateControlled',
        'is_food_grade': 'isFoodGrade',
        'is_secure': 'isSecure',
        'is_frozen': 'isFrozen',
        'is_refrigerated': 'isRefrigerated',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, warehouse_id=None, name=None, address=None, is_climate_controlled=False, is_food_grade=False, is_secure=False, is_frozen=False, is_refrigerated=False, create_date=None, modify_date=None, custom_fields=None):  # noqa: E501
        """Zone - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._warehouse_id = None
        self._name = None
        self._address = None
        self._is_climate_controlled = None
        self._is_food_grade = None
        self._is_secure = None
        self._is_frozen = None
        self._is_refrigerated = None
        self._create_date = None
        self._modify_date = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.warehouse_id = warehouse_id
        self.name = name
        if address is not None:
            self.address = address
        if is_climate_controlled is not None:
            self.is_climate_controlled = is_climate_controlled
        if is_food_grade is not None:
            self.is_food_grade = is_food_grade
        if is_secure is not None:
            self.is_secure = is_secure
        if is_frozen is not None:
            self.is_frozen = is_frozen
        if is_refrigerated is not None:
            self.is_refrigerated = is_refrigerated
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this Zone.  # noqa: E501


        :return: The id of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Zone.


        :param id: The id of this Zone.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this Zone.  # noqa: E501


        :return: The warehouse_id of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this Zone.


        :param warehouse_id: The warehouse_id of this Zone.  # noqa: E501
        :type: int
        """
        if warehouse_id is None:
            raise ValueError("Invalid value for `warehouse_id`, must not be `None`")  # noqa: E501

        self._warehouse_id = warehouse_id

    @property
    def name(self):
        """Gets the name of this Zone.  # noqa: E501


        :return: The name of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Zone.


        :param name: The name of this Zone.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def address(self):
        """Gets the address of this Zone.  # noqa: E501


        :return: The address of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Zone.


        :param address: The address of this Zone.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def is_climate_controlled(self):
        """Gets the is_climate_controlled of this Zone.  # noqa: E501


        :return: The is_climate_controlled of this Zone.  # noqa: E501
        :rtype: bool
        """
        return self._is_climate_controlled

    @is_climate_controlled.setter
    def is_climate_controlled(self, is_climate_controlled):
        """Sets the is_climate_controlled of this Zone.


        :param is_climate_controlled: The is_climate_controlled of this Zone.  # noqa: E501
        :type: bool
        """

        self._is_climate_controlled = is_climate_controlled

    @property
    def is_food_grade(self):
        """Gets the is_food_grade of this Zone.  # noqa: E501


        :return: The is_food_grade of this Zone.  # noqa: E501
        :rtype: bool
        """
        return self._is_food_grade

    @is_food_grade.setter
    def is_food_grade(self, is_food_grade):
        """Sets the is_food_grade of this Zone.


        :param is_food_grade: The is_food_grade of this Zone.  # noqa: E501
        :type: bool
        """

        self._is_food_grade = is_food_grade

    @property
    def is_secure(self):
        """Gets the is_secure of this Zone.  # noqa: E501


        :return: The is_secure of this Zone.  # noqa: E501
        :rtype: bool
        """
        return self._is_secure

    @is_secure.setter
    def is_secure(self, is_secure):
        """Sets the is_secure of this Zone.


        :param is_secure: The is_secure of this Zone.  # noqa: E501
        :type: bool
        """

        self._is_secure = is_secure

    @property
    def is_frozen(self):
        """Gets the is_frozen of this Zone.  # noqa: E501


        :return: The is_frozen of this Zone.  # noqa: E501
        :rtype: bool
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this Zone.


        :param is_frozen: The is_frozen of this Zone.  # noqa: E501
        :type: bool
        """

        self._is_frozen = is_frozen

    @property
    def is_refrigerated(self):
        """Gets the is_refrigerated of this Zone.  # noqa: E501


        :return: The is_refrigerated of this Zone.  # noqa: E501
        :rtype: bool
        """
        return self._is_refrigerated

    @is_refrigerated.setter
    def is_refrigerated(self, is_refrigerated):
        """Sets the is_refrigerated of this Zone.


        :param is_refrigerated: The is_refrigerated of this Zone.  # noqa: E501
        :type: bool
        """

        self._is_refrigerated = is_refrigerated

    @property
    def create_date(self):
        """Gets the create_date of this Zone.  # noqa: E501


        :return: The create_date of this Zone.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this Zone.


        :param create_date: The create_date of this Zone.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this Zone.  # noqa: E501


        :return: The modify_date of this Zone.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this Zone.


        :param modify_date: The modify_date of this Zone.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Zone.  # noqa: E501


        :return: The custom_fields of this Zone.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Zone.


        :param custom_fields: The custom_fields of this Zone.  # noqa: E501
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
        if not isinstance(other, Zone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
