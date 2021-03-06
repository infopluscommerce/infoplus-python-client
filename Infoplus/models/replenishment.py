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


class Replenishment(object):
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
        'replenishment_process': 'int',
        'pick_face_assignment': 'int',
        'location_id': 'int',
        'quantity': 'int',
        'custom_fields': 'dict(str, object)',
        'sku': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'replenishment_process': 'replenishmentProcess',
        'pick_face_assignment': 'pickFaceAssignment',
        'location_id': 'locationId',
        'quantity': 'quantity',
        'custom_fields': 'customFields',
        'sku': 'sku'
    }

    def __init__(self, id=None, create_date=None, modify_date=None, replenishment_process=None, pick_face_assignment=None, location_id=None, quantity=None, custom_fields=None, sku=None):  # noqa: E501
        """Replenishment - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._replenishment_process = None
        self._pick_face_assignment = None
        self._location_id = None
        self._quantity = None
        self._custom_fields = None
        self._sku = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if replenishment_process is not None:
            self.replenishment_process = replenishment_process
        if pick_face_assignment is not None:
            self.pick_face_assignment = pick_face_assignment
        self.location_id = location_id
        if quantity is not None:
            self.quantity = quantity
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if sku is not None:
            self.sku = sku

    @property
    def id(self):
        """Gets the id of this Replenishment.  # noqa: E501


        :return: The id of this Replenishment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Replenishment.


        :param id: The id of this Replenishment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this Replenishment.  # noqa: E501


        :return: The create_date of this Replenishment.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this Replenishment.


        :param create_date: The create_date of this Replenishment.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this Replenishment.  # noqa: E501


        :return: The modify_date of this Replenishment.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this Replenishment.


        :param modify_date: The modify_date of this Replenishment.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def replenishment_process(self):
        """Gets the replenishment_process of this Replenishment.  # noqa: E501


        :return: The replenishment_process of this Replenishment.  # noqa: E501
        :rtype: int
        """
        return self._replenishment_process

    @replenishment_process.setter
    def replenishment_process(self, replenishment_process):
        """Sets the replenishment_process of this Replenishment.


        :param replenishment_process: The replenishment_process of this Replenishment.  # noqa: E501
        :type: int
        """

        self._replenishment_process = replenishment_process

    @property
    def pick_face_assignment(self):
        """Gets the pick_face_assignment of this Replenishment.  # noqa: E501


        :return: The pick_face_assignment of this Replenishment.  # noqa: E501
        :rtype: int
        """
        return self._pick_face_assignment

    @pick_face_assignment.setter
    def pick_face_assignment(self, pick_face_assignment):
        """Sets the pick_face_assignment of this Replenishment.


        :param pick_face_assignment: The pick_face_assignment of this Replenishment.  # noqa: E501
        :type: int
        """

        self._pick_face_assignment = pick_face_assignment

    @property
    def location_id(self):
        """Gets the location_id of this Replenishment.  # noqa: E501


        :return: The location_id of this Replenishment.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this Replenishment.


        :param location_id: The location_id of this Replenishment.  # noqa: E501
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def quantity(self):
        """Gets the quantity of this Replenishment.  # noqa: E501


        :return: The quantity of this Replenishment.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Replenishment.


        :param quantity: The quantity of this Replenishment.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Replenishment.  # noqa: E501


        :return: The custom_fields of this Replenishment.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Replenishment.


        :param custom_fields: The custom_fields of this Replenishment.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def sku(self):
        """Gets the sku of this Replenishment.  # noqa: E501


        :return: The sku of this Replenishment.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this Replenishment.


        :param sku: The sku of this Replenishment.  # noqa: E501
        :type: str
        """

        self._sku = sku

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
        if not isinstance(other, Replenishment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
