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


class BillingCode(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BillingCode - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'create_date': 'datetime',
            'modify_date': 'datetime',
            'quantity': 'int',
            'date': 'datetime',
            'user_id': 'int',
            'lob_id': 'int',
            'billing_code_type_id': 'int',
            'note': 'str',
            'custom_fields': 'dict(str, object)'
        }

        self.attribute_map = {
            'id': 'id',
            'create_date': 'createDate',
            'modify_date': 'modifyDate',
            'quantity': 'quantity',
            'date': 'date',
            'user_id': 'userId',
            'lob_id': 'lobId',
            'billing_code_type_id': 'billingCodeTypeId',
            'note': 'note',
            'custom_fields': 'customFields'
        }

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._quantity = None
        self._date = None
        self._user_id = None
        self._lob_id = None
        self._billing_code_type_id = None
        self._note = None
        self._custom_fields = None

    @property
    def id(self):
        """
        Gets the id of this BillingCode.


        :return: The id of this BillingCode.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BillingCode.


        :param id: The id of this BillingCode.
        :type: int
        """
        self._id = id

    @property
    def create_date(self):
        """
        Gets the create_date of this BillingCode.


        :return: The create_date of this BillingCode.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this BillingCode.


        :param create_date: The create_date of this BillingCode.
        :type: datetime
        """
        self._create_date = create_date

    @property
    def modify_date(self):
        """
        Gets the modify_date of this BillingCode.


        :return: The modify_date of this BillingCode.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this BillingCode.


        :param modify_date: The modify_date of this BillingCode.
        :type: datetime
        """
        self._modify_date = modify_date

    @property
    def quantity(self):
        """
        Gets the quantity of this BillingCode.


        :return: The quantity of this BillingCode.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this BillingCode.


        :param quantity: The quantity of this BillingCode.
        :type: int
        """
        self._quantity = quantity

    @property
    def date(self):
        """
        Gets the date of this BillingCode.


        :return: The date of this BillingCode.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this BillingCode.


        :param date: The date of this BillingCode.
        :type: datetime
        """
        self._date = date

    @property
    def user_id(self):
        """
        Gets the user_id of this BillingCode.


        :return: The user_id of this BillingCode.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this BillingCode.


        :param user_id: The user_id of this BillingCode.
        :type: int
        """
        self._user_id = user_id

    @property
    def lob_id(self):
        """
        Gets the lob_id of this BillingCode.


        :return: The lob_id of this BillingCode.
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """
        Sets the lob_id of this BillingCode.


        :param lob_id: The lob_id of this BillingCode.
        :type: int
        """
        self._lob_id = lob_id

    @property
    def billing_code_type_id(self):
        """
        Gets the billing_code_type_id of this BillingCode.


        :return: The billing_code_type_id of this BillingCode.
        :rtype: int
        """
        return self._billing_code_type_id

    @billing_code_type_id.setter
    def billing_code_type_id(self, billing_code_type_id):
        """
        Sets the billing_code_type_id of this BillingCode.


        :param billing_code_type_id: The billing_code_type_id of this BillingCode.
        :type: int
        """
        self._billing_code_type_id = billing_code_type_id

    @property
    def note(self):
        """
        Gets the note of this BillingCode.


        :return: The note of this BillingCode.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this BillingCode.


        :param note: The note of this BillingCode.
        :type: str
        """
        self._note = note

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this BillingCode.


        :return: The custom_fields of this BillingCode.
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this BillingCode.


        :param custom_fields: The custom_fields of this BillingCode.
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

