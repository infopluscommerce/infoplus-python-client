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


class OverrideReturnAddress(object):
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
        'lob_id': 'int',
        'warehouse_id': 'int',
        'order_source_id': 'int',
        'name': 'str',
        'attention': 'str',
        'street': 'str',
        'street2': 'str',
        'street3_province': 'str',
        'city': 'str',
        'state': 'str',
        'zip': 'str',
        'country': 'str',
        'phone': 'str',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'lob_id': 'lobId',
        'warehouse_id': 'warehouseId',
        'order_source_id': 'orderSourceId',
        'name': 'name',
        'attention': 'attention',
        'street': 'street',
        'street2': 'street2',
        'street3_province': 'street3Province',
        'city': 'city',
        'state': 'state',
        'zip': 'zip',
        'country': 'country',
        'phone': 'phone',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, create_date=None, modify_date=None, lob_id=None, warehouse_id=None, order_source_id=None, name=None, attention=None, street=None, street2=None, street3_province=None, city=None, state=None, zip=None, country=None, phone=None, custom_fields=None):  # noqa: E501
        """OverrideReturnAddress - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._lob_id = None
        self._warehouse_id = None
        self._order_source_id = None
        self._name = None
        self._attention = None
        self._street = None
        self._street2 = None
        self._street3_province = None
        self._city = None
        self._state = None
        self._zip = None
        self._country = None
        self._phone = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        self.lob_id = lob_id
        self.warehouse_id = warehouse_id
        self.order_source_id = order_source_id
        self.name = name
        if attention is not None:
            self.attention = attention
        self.street = street
        if street2 is not None:
            self.street2 = street2
        if street3_province is not None:
            self.street3_province = street3_province
        self.city = city
        if state is not None:
            self.state = state
        self.zip = zip
        self.country = country
        self.phone = phone
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this OverrideReturnAddress.  # noqa: E501


        :return: The id of this OverrideReturnAddress.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OverrideReturnAddress.


        :param id: The id of this OverrideReturnAddress.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this OverrideReturnAddress.  # noqa: E501


        :return: The create_date of this OverrideReturnAddress.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this OverrideReturnAddress.


        :param create_date: The create_date of this OverrideReturnAddress.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this OverrideReturnAddress.  # noqa: E501


        :return: The modify_date of this OverrideReturnAddress.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this OverrideReturnAddress.


        :param modify_date: The modify_date of this OverrideReturnAddress.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def lob_id(self):
        """Gets the lob_id of this OverrideReturnAddress.  # noqa: E501


        :return: The lob_id of this OverrideReturnAddress.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this OverrideReturnAddress.


        :param lob_id: The lob_id of this OverrideReturnAddress.  # noqa: E501
        :type: int
        """
        if lob_id is None:
            raise ValueError("Invalid value for `lob_id`, must not be `None`")  # noqa: E501

        self._lob_id = lob_id

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this OverrideReturnAddress.  # noqa: E501


        :return: The warehouse_id of this OverrideReturnAddress.  # noqa: E501
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this OverrideReturnAddress.


        :param warehouse_id: The warehouse_id of this OverrideReturnAddress.  # noqa: E501
        :type: int
        """
        if warehouse_id is None:
            raise ValueError("Invalid value for `warehouse_id`, must not be `None`")  # noqa: E501

        self._warehouse_id = warehouse_id

    @property
    def order_source_id(self):
        """Gets the order_source_id of this OverrideReturnAddress.  # noqa: E501


        :return: The order_source_id of this OverrideReturnAddress.  # noqa: E501
        :rtype: int
        """
        return self._order_source_id

    @order_source_id.setter
    def order_source_id(self, order_source_id):
        """Sets the order_source_id of this OverrideReturnAddress.


        :param order_source_id: The order_source_id of this OverrideReturnAddress.  # noqa: E501
        :type: int
        """
        if order_source_id is None:
            raise ValueError("Invalid value for `order_source_id`, must not be `None`")  # noqa: E501

        self._order_source_id = order_source_id

    @property
    def name(self):
        """Gets the name of this OverrideReturnAddress.  # noqa: E501


        :return: The name of this OverrideReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OverrideReturnAddress.


        :param name: The name of this OverrideReturnAddress.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def attention(self):
        """Gets the attention of this OverrideReturnAddress.  # noqa: E501


        :return: The attention of this OverrideReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._attention

    @attention.setter
    def attention(self, attention):
        """Sets the attention of this OverrideReturnAddress.


        :param attention: The attention of this OverrideReturnAddress.  # noqa: E501
        :type: str
        """

        self._attention = attention

    @property
    def street(self):
        """Gets the street of this OverrideReturnAddress.  # noqa: E501


        :return: The street of this OverrideReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this OverrideReturnAddress.


        :param street: The street of this OverrideReturnAddress.  # noqa: E501
        :type: str
        """
        if street is None:
            raise ValueError("Invalid value for `street`, must not be `None`")  # noqa: E501

        self._street = street

    @property
    def street2(self):
        """Gets the street2 of this OverrideReturnAddress.  # noqa: E501


        :return: The street2 of this OverrideReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._street2

    @street2.setter
    def street2(self, street2):
        """Sets the street2 of this OverrideReturnAddress.


        :param street2: The street2 of this OverrideReturnAddress.  # noqa: E501
        :type: str
        """

        self._street2 = street2

    @property
    def street3_province(self):
        """Gets the street3_province of this OverrideReturnAddress.  # noqa: E501


        :return: The street3_province of this OverrideReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._street3_province

    @street3_province.setter
    def street3_province(self, street3_province):
        """Sets the street3_province of this OverrideReturnAddress.


        :param street3_province: The street3_province of this OverrideReturnAddress.  # noqa: E501
        :type: str
        """

        self._street3_province = street3_province

    @property
    def city(self):
        """Gets the city of this OverrideReturnAddress.  # noqa: E501


        :return: The city of this OverrideReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this OverrideReturnAddress.


        :param city: The city of this OverrideReturnAddress.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def state(self):
        """Gets the state of this OverrideReturnAddress.  # noqa: E501


        :return: The state of this OverrideReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this OverrideReturnAddress.


        :param state: The state of this OverrideReturnAddress.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this OverrideReturnAddress.  # noqa: E501


        :return: The zip of this OverrideReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this OverrideReturnAddress.


        :param zip: The zip of this OverrideReturnAddress.  # noqa: E501
        :type: str
        """
        if zip is None:
            raise ValueError("Invalid value for `zip`, must not be `None`")  # noqa: E501

        self._zip = zip

    @property
    def country(self):
        """Gets the country of this OverrideReturnAddress.  # noqa: E501


        :return: The country of this OverrideReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this OverrideReturnAddress.


        :param country: The country of this OverrideReturnAddress.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def phone(self):
        """Gets the phone of this OverrideReturnAddress.  # noqa: E501


        :return: The phone of this OverrideReturnAddress.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this OverrideReturnAddress.


        :param phone: The phone of this OverrideReturnAddress.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

    @property
    def custom_fields(self):
        """Gets the custom_fields of this OverrideReturnAddress.  # noqa: E501


        :return: The custom_fields of this OverrideReturnAddress.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this OverrideReturnAddress.


        :param custom_fields: The custom_fields of this OverrideReturnAddress.  # noqa: E501
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
        if not isinstance(other, OverrideReturnAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
