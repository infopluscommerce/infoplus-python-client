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


class OrderSourceStockStatus(object):
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
        'order_source_id': 'int',
        'lob_id': 'int',
        'total_reserved_quantity': 'int',
        'demand': 'int',
        'reserved_quantity': 'int',
        'quantity_available': 'int',
        'orderable_quantity': 'int',
        'unreserved_quantity_available': 'int',
        'net_reservation': 'int',
        'custom_fields': 'dict(str, object)',
        'sku': 'str'
    }

    attribute_map = {
        'id': 'id',
        'order_source_id': 'orderSourceId',
        'lob_id': 'lobId',
        'total_reserved_quantity': 'totalReservedQuantity',
        'demand': 'demand',
        'reserved_quantity': 'reservedQuantity',
        'quantity_available': 'quantityAvailable',
        'orderable_quantity': 'orderableQuantity',
        'unreserved_quantity_available': 'unreservedQuantityAvailable',
        'net_reservation': 'netReservation',
        'custom_fields': 'customFields',
        'sku': 'sku'
    }

    def __init__(self, id=None, order_source_id=None, lob_id=None, total_reserved_quantity=None, demand=None, reserved_quantity=None, quantity_available=None, orderable_quantity=None, unreserved_quantity_available=None, net_reservation=None, custom_fields=None, sku=None):  # noqa: E501
        """OrderSourceStockStatus - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._order_source_id = None
        self._lob_id = None
        self._total_reserved_quantity = None
        self._demand = None
        self._reserved_quantity = None
        self._quantity_available = None
        self._orderable_quantity = None
        self._unreserved_quantity_available = None
        self._net_reservation = None
        self._custom_fields = None
        self._sku = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.order_source_id = order_source_id
        if lob_id is not None:
            self.lob_id = lob_id
        if total_reserved_quantity is not None:
            self.total_reserved_quantity = total_reserved_quantity
        if demand is not None:
            self.demand = demand
        if reserved_quantity is not None:
            self.reserved_quantity = reserved_quantity
        if quantity_available is not None:
            self.quantity_available = quantity_available
        if orderable_quantity is not None:
            self.orderable_quantity = orderable_quantity
        if unreserved_quantity_available is not None:
            self.unreserved_quantity_available = unreserved_quantity_available
        if net_reservation is not None:
            self.net_reservation = net_reservation
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if sku is not None:
            self.sku = sku

    @property
    def id(self):
        """Gets the id of this OrderSourceStockStatus.  # noqa: E501


        :return: The id of this OrderSourceStockStatus.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderSourceStockStatus.


        :param id: The id of this OrderSourceStockStatus.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def order_source_id(self):
        """Gets the order_source_id of this OrderSourceStockStatus.  # noqa: E501


        :return: The order_source_id of this OrderSourceStockStatus.  # noqa: E501
        :rtype: int
        """
        return self._order_source_id

    @order_source_id.setter
    def order_source_id(self, order_source_id):
        """Sets the order_source_id of this OrderSourceStockStatus.


        :param order_source_id: The order_source_id of this OrderSourceStockStatus.  # noqa: E501
        :type: int
        """
        if order_source_id is None:
            raise ValueError("Invalid value for `order_source_id`, must not be `None`")  # noqa: E501

        self._order_source_id = order_source_id

    @property
    def lob_id(self):
        """Gets the lob_id of this OrderSourceStockStatus.  # noqa: E501


        :return: The lob_id of this OrderSourceStockStatus.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this OrderSourceStockStatus.


        :param lob_id: The lob_id of this OrderSourceStockStatus.  # noqa: E501
        :type: int
        """

        self._lob_id = lob_id

    @property
    def total_reserved_quantity(self):
        """Gets the total_reserved_quantity of this OrderSourceStockStatus.  # noqa: E501


        :return: The total_reserved_quantity of this OrderSourceStockStatus.  # noqa: E501
        :rtype: int
        """
        return self._total_reserved_quantity

    @total_reserved_quantity.setter
    def total_reserved_quantity(self, total_reserved_quantity):
        """Sets the total_reserved_quantity of this OrderSourceStockStatus.


        :param total_reserved_quantity: The total_reserved_quantity of this OrderSourceStockStatus.  # noqa: E501
        :type: int
        """

        self._total_reserved_quantity = total_reserved_quantity

    @property
    def demand(self):
        """Gets the demand of this OrderSourceStockStatus.  # noqa: E501


        :return: The demand of this OrderSourceStockStatus.  # noqa: E501
        :rtype: int
        """
        return self._demand

    @demand.setter
    def demand(self, demand):
        """Sets the demand of this OrderSourceStockStatus.


        :param demand: The demand of this OrderSourceStockStatus.  # noqa: E501
        :type: int
        """

        self._demand = demand

    @property
    def reserved_quantity(self):
        """Gets the reserved_quantity of this OrderSourceStockStatus.  # noqa: E501


        :return: The reserved_quantity of this OrderSourceStockStatus.  # noqa: E501
        :rtype: int
        """
        return self._reserved_quantity

    @reserved_quantity.setter
    def reserved_quantity(self, reserved_quantity):
        """Sets the reserved_quantity of this OrderSourceStockStatus.


        :param reserved_quantity: The reserved_quantity of this OrderSourceStockStatus.  # noqa: E501
        :type: int
        """

        self._reserved_quantity = reserved_quantity

    @property
    def quantity_available(self):
        """Gets the quantity_available of this OrderSourceStockStatus.  # noqa: E501


        :return: The quantity_available of this OrderSourceStockStatus.  # noqa: E501
        :rtype: int
        """
        return self._quantity_available

    @quantity_available.setter
    def quantity_available(self, quantity_available):
        """Sets the quantity_available of this OrderSourceStockStatus.


        :param quantity_available: The quantity_available of this OrderSourceStockStatus.  # noqa: E501
        :type: int
        """

        self._quantity_available = quantity_available

    @property
    def orderable_quantity(self):
        """Gets the orderable_quantity of this OrderSourceStockStatus.  # noqa: E501


        :return: The orderable_quantity of this OrderSourceStockStatus.  # noqa: E501
        :rtype: int
        """
        return self._orderable_quantity

    @orderable_quantity.setter
    def orderable_quantity(self, orderable_quantity):
        """Sets the orderable_quantity of this OrderSourceStockStatus.


        :param orderable_quantity: The orderable_quantity of this OrderSourceStockStatus.  # noqa: E501
        :type: int
        """

        self._orderable_quantity = orderable_quantity

    @property
    def unreserved_quantity_available(self):
        """Gets the unreserved_quantity_available of this OrderSourceStockStatus.  # noqa: E501


        :return: The unreserved_quantity_available of this OrderSourceStockStatus.  # noqa: E501
        :rtype: int
        """
        return self._unreserved_quantity_available

    @unreserved_quantity_available.setter
    def unreserved_quantity_available(self, unreserved_quantity_available):
        """Sets the unreserved_quantity_available of this OrderSourceStockStatus.


        :param unreserved_quantity_available: The unreserved_quantity_available of this OrderSourceStockStatus.  # noqa: E501
        :type: int
        """

        self._unreserved_quantity_available = unreserved_quantity_available

    @property
    def net_reservation(self):
        """Gets the net_reservation of this OrderSourceStockStatus.  # noqa: E501


        :return: The net_reservation of this OrderSourceStockStatus.  # noqa: E501
        :rtype: int
        """
        return self._net_reservation

    @net_reservation.setter
    def net_reservation(self, net_reservation):
        """Sets the net_reservation of this OrderSourceStockStatus.


        :param net_reservation: The net_reservation of this OrderSourceStockStatus.  # noqa: E501
        :type: int
        """

        self._net_reservation = net_reservation

    @property
    def custom_fields(self):
        """Gets the custom_fields of this OrderSourceStockStatus.  # noqa: E501


        :return: The custom_fields of this OrderSourceStockStatus.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this OrderSourceStockStatus.


        :param custom_fields: The custom_fields of this OrderSourceStockStatus.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def sku(self):
        """Gets the sku of this OrderSourceStockStatus.  # noqa: E501


        :return: The sku of this OrderSourceStockStatus.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this OrderSourceStockStatus.


        :param sku: The sku of this OrderSourceStockStatus.  # noqa: E501
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
        if not isinstance(other, OrderSourceStockStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
