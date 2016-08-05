# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class OverrideReturnAddress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OverrideReturnAddress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
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
            'city': 'str',
            'state': 'str',
            'zip': 'str',
            'country': 'str',
            'phone': 'str',
            'custom_fields': 'dict(str, object)'
        }

        self.attribute_map = {
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
            'city': 'city',
            'state': 'state',
            'zip': 'zip',
            'country': 'country',
            'phone': 'phone',
            'custom_fields': 'customFields'
        }

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
        self._city = None
        self._state = None
        self._zip = None
        self._country = None
        self._phone = None
        self._custom_fields = None

    @property
    def id(self):
        """
        Gets the id of this OverrideReturnAddress.


        :return: The id of this OverrideReturnAddress.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OverrideReturnAddress.


        :param id: The id of this OverrideReturnAddress.
        :type: int
        """
        self._id = id

    @property
    def create_date(self):
        """
        Gets the create_date of this OverrideReturnAddress.


        :return: The create_date of this OverrideReturnAddress.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this OverrideReturnAddress.


        :param create_date: The create_date of this OverrideReturnAddress.
        :type: datetime
        """
        self._create_date = create_date

    @property
    def modify_date(self):
        """
        Gets the modify_date of this OverrideReturnAddress.


        :return: The modify_date of this OverrideReturnAddress.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this OverrideReturnAddress.


        :param modify_date: The modify_date of this OverrideReturnAddress.
        :type: datetime
        """
        self._modify_date = modify_date

    @property
    def lob_id(self):
        """
        Gets the lob_id of this OverrideReturnAddress.


        :return: The lob_id of this OverrideReturnAddress.
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """
        Sets the lob_id of this OverrideReturnAddress.


        :param lob_id: The lob_id of this OverrideReturnAddress.
        :type: int
        """
        self._lob_id = lob_id

    @property
    def warehouse_id(self):
        """
        Gets the warehouse_id of this OverrideReturnAddress.


        :return: The warehouse_id of this OverrideReturnAddress.
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """
        Sets the warehouse_id of this OverrideReturnAddress.


        :param warehouse_id: The warehouse_id of this OverrideReturnAddress.
        :type: int
        """
        self._warehouse_id = warehouse_id

    @property
    def order_source_id(self):
        """
        Gets the order_source_id of this OverrideReturnAddress.


        :return: The order_source_id of this OverrideReturnAddress.
        :rtype: int
        """
        return self._order_source_id

    @order_source_id.setter
    def order_source_id(self, order_source_id):
        """
        Sets the order_source_id of this OverrideReturnAddress.


        :param order_source_id: The order_source_id of this OverrideReturnAddress.
        :type: int
        """
        self._order_source_id = order_source_id

    @property
    def name(self):
        """
        Gets the name of this OverrideReturnAddress.


        :return: The name of this OverrideReturnAddress.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OverrideReturnAddress.


        :param name: The name of this OverrideReturnAddress.
        :type: str
        """
        self._name = name

    @property
    def attention(self):
        """
        Gets the attention of this OverrideReturnAddress.


        :return: The attention of this OverrideReturnAddress.
        :rtype: str
        """
        return self._attention

    @attention.setter
    def attention(self, attention):
        """
        Sets the attention of this OverrideReturnAddress.


        :param attention: The attention of this OverrideReturnAddress.
        :type: str
        """
        self._attention = attention

    @property
    def street(self):
        """
        Gets the street of this OverrideReturnAddress.


        :return: The street of this OverrideReturnAddress.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """
        Sets the street of this OverrideReturnAddress.


        :param street: The street of this OverrideReturnAddress.
        :type: str
        """
        self._street = street

    @property
    def street2(self):
        """
        Gets the street2 of this OverrideReturnAddress.


        :return: The street2 of this OverrideReturnAddress.
        :rtype: str
        """
        return self._street2

    @street2.setter
    def street2(self, street2):
        """
        Sets the street2 of this OverrideReturnAddress.


        :param street2: The street2 of this OverrideReturnAddress.
        :type: str
        """
        self._street2 = street2

    @property
    def city(self):
        """
        Gets the city of this OverrideReturnAddress.


        :return: The city of this OverrideReturnAddress.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this OverrideReturnAddress.


        :param city: The city of this OverrideReturnAddress.
        :type: str
        """
        self._city = city

    @property
    def state(self):
        """
        Gets the state of this OverrideReturnAddress.


        :return: The state of this OverrideReturnAddress.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this OverrideReturnAddress.


        :param state: The state of this OverrideReturnAddress.
        :type: str
        """
        self._state = state

    @property
    def zip(self):
        """
        Gets the zip of this OverrideReturnAddress.


        :return: The zip of this OverrideReturnAddress.
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """
        Sets the zip of this OverrideReturnAddress.


        :param zip: The zip of this OverrideReturnAddress.
        :type: str
        """
        self._zip = zip

    @property
    def country(self):
        """
        Gets the country of this OverrideReturnAddress.


        :return: The country of this OverrideReturnAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this OverrideReturnAddress.


        :param country: The country of this OverrideReturnAddress.
        :type: str
        """
        self._country = country

    @property
    def phone(self):
        """
        Gets the phone of this OverrideReturnAddress.


        :return: The phone of this OverrideReturnAddress.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this OverrideReturnAddress.


        :param phone: The phone of this OverrideReturnAddress.
        :type: str
        """
        self._phone = phone

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this OverrideReturnAddress.


        :return: The custom_fields of this OverrideReturnAddress.
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this OverrideReturnAddress.


        :param custom_fields: The custom_fields of this OverrideReturnAddress.
        :type: dict(str, object)
        """
        self._custom_fields = custom_fields

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

