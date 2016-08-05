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


class ReplenishmentPlan(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ReplenishmentPlan - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'create_date': 'datetime',
            'modify_date': 'datetime',
            'warehouse_id': 'int',
            'pick_face_assignment_smart_filter_id': 'int',
            'name': 'str',
            'custom_fields': 'dict(str, object)'
        }

        self.attribute_map = {
            'id': 'id',
            'create_date': 'createDate',
            'modify_date': 'modifyDate',
            'warehouse_id': 'warehouseId',
            'pick_face_assignment_smart_filter_id': 'pickFaceAssignmentSmartFilterId',
            'name': 'name',
            'custom_fields': 'customFields'
        }

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._warehouse_id = None
        self._pick_face_assignment_smart_filter_id = None
        self._name = None
        self._custom_fields = None

    @property
    def id(self):
        """
        Gets the id of this ReplenishmentPlan.


        :return: The id of this ReplenishmentPlan.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ReplenishmentPlan.


        :param id: The id of this ReplenishmentPlan.
        :type: int
        """
        self._id = id

    @property
    def create_date(self):
        """
        Gets the create_date of this ReplenishmentPlan.


        :return: The create_date of this ReplenishmentPlan.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this ReplenishmentPlan.


        :param create_date: The create_date of this ReplenishmentPlan.
        :type: datetime
        """
        self._create_date = create_date

    @property
    def modify_date(self):
        """
        Gets the modify_date of this ReplenishmentPlan.


        :return: The modify_date of this ReplenishmentPlan.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this ReplenishmentPlan.


        :param modify_date: The modify_date of this ReplenishmentPlan.
        :type: datetime
        """
        self._modify_date = modify_date

    @property
    def warehouse_id(self):
        """
        Gets the warehouse_id of this ReplenishmentPlan.


        :return: The warehouse_id of this ReplenishmentPlan.
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """
        Sets the warehouse_id of this ReplenishmentPlan.


        :param warehouse_id: The warehouse_id of this ReplenishmentPlan.
        :type: int
        """
        self._warehouse_id = warehouse_id

    @property
    def pick_face_assignment_smart_filter_id(self):
        """
        Gets the pick_face_assignment_smart_filter_id of this ReplenishmentPlan.


        :return: The pick_face_assignment_smart_filter_id of this ReplenishmentPlan.
        :rtype: int
        """
        return self._pick_face_assignment_smart_filter_id

    @pick_face_assignment_smart_filter_id.setter
    def pick_face_assignment_smart_filter_id(self, pick_face_assignment_smart_filter_id):
        """
        Sets the pick_face_assignment_smart_filter_id of this ReplenishmentPlan.


        :param pick_face_assignment_smart_filter_id: The pick_face_assignment_smart_filter_id of this ReplenishmentPlan.
        :type: int
        """
        self._pick_face_assignment_smart_filter_id = pick_face_assignment_smart_filter_id

    @property
    def name(self):
        """
        Gets the name of this ReplenishmentPlan.


        :return: The name of this ReplenishmentPlan.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReplenishmentPlan.


        :param name: The name of this ReplenishmentPlan.
        :type: str
        """
        self._name = name

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this ReplenishmentPlan.


        :return: The custom_fields of this ReplenishmentPlan.
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this ReplenishmentPlan.


        :param custom_fields: The custom_fields of this ReplenishmentPlan.
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

