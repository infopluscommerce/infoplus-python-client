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


class OrderWarehouseFulfillmentRawData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OrderWarehouseFulfillmentRawData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'warehouse_id': 'int',
            'can_fulfill': 'bool',
            'sku_map': 'dict(str, OrderWarehouseFulfillmentRawSkuData)'
        }

        self.attribute_map = {
            'warehouse_id': 'warehouseId',
            'can_fulfill': 'canFulfill',
            'sku_map': 'skuMap'
        }

        self._warehouse_id = None
        self._can_fulfill = False
        self._sku_map = None

    @property
    def warehouse_id(self):
        """
        Gets the warehouse_id of this OrderWarehouseFulfillmentRawData.


        :return: The warehouse_id of this OrderWarehouseFulfillmentRawData.
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """
        Sets the warehouse_id of this OrderWarehouseFulfillmentRawData.


        :param warehouse_id: The warehouse_id of this OrderWarehouseFulfillmentRawData.
        :type: int
        """
        self._warehouse_id = warehouse_id

    @property
    def can_fulfill(self):
        """
        Gets the can_fulfill of this OrderWarehouseFulfillmentRawData.


        :return: The can_fulfill of this OrderWarehouseFulfillmentRawData.
        :rtype: bool
        """
        return self._can_fulfill

    @can_fulfill.setter
    def can_fulfill(self, can_fulfill):
        """
        Sets the can_fulfill of this OrderWarehouseFulfillmentRawData.


        :param can_fulfill: The can_fulfill of this OrderWarehouseFulfillmentRawData.
        :type: bool
        """
        self._can_fulfill = can_fulfill

    @property
    def sku_map(self):
        """
        Gets the sku_map of this OrderWarehouseFulfillmentRawData.


        :return: The sku_map of this OrderWarehouseFulfillmentRawData.
        :rtype: dict(str, OrderWarehouseFulfillmentRawSkuData)
        """
        return self._sku_map

    @sku_map.setter
    def sku_map(self, sku_map):
        """
        Sets the sku_map of this OrderWarehouseFulfillmentRawData.


        :param sku_map: The sku_map of this OrderWarehouseFulfillmentRawData.
        :type: dict(str, OrderWarehouseFulfillmentRawSkuData)
        """
        self._sku_map = sku_map

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
