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

from Infoplus.models.gs1128_label_dto import GS1128LabelDTO  # noqa: F401,E501


class PackingDetail(object):
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
        'order_id': 'float',
        'pallet_id': 'int',
        'master_carton_id': 'int',
        'carton_id': 'int',
        'sku': 'str',
        'item_receipt_id': 'int',
        'line_item_id': 'int',
        'quantity': 'int',
        'carton_gs1128_label': 'list[GS1128LabelDTO]',
        'pallet_gs1128_label': 'list[GS1128LabelDTO]',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'lob_id': 'lobId',
        'order_id': 'orderId',
        'pallet_id': 'palletId',
        'master_carton_id': 'masterCartonId',
        'carton_id': 'cartonId',
        'sku': 'sku',
        'item_receipt_id': 'itemReceiptId',
        'line_item_id': 'lineItemId',
        'quantity': 'quantity',
        'carton_gs1128_label': 'cartonGS1128Label',
        'pallet_gs1128_label': 'palletGS1128Label',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, create_date=None, modify_date=None, lob_id=None, order_id=None, pallet_id=None, master_carton_id=None, carton_id=None, sku=None, item_receipt_id=None, line_item_id=None, quantity=None, carton_gs1128_label=None, pallet_gs1128_label=None, custom_fields=None):  # noqa: E501
        """PackingDetail - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._lob_id = None
        self._order_id = None
        self._pallet_id = None
        self._master_carton_id = None
        self._carton_id = None
        self._sku = None
        self._item_receipt_id = None
        self._line_item_id = None
        self._quantity = None
        self._carton_gs1128_label = None
        self._pallet_gs1128_label = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if lob_id is not None:
            self.lob_id = lob_id
        if order_id is not None:
            self.order_id = order_id
        if pallet_id is not None:
            self.pallet_id = pallet_id
        if master_carton_id is not None:
            self.master_carton_id = master_carton_id
        if carton_id is not None:
            self.carton_id = carton_id
        if sku is not None:
            self.sku = sku
        if item_receipt_id is not None:
            self.item_receipt_id = item_receipt_id
        if line_item_id is not None:
            self.line_item_id = line_item_id
        if quantity is not None:
            self.quantity = quantity
        if carton_gs1128_label is not None:
            self.carton_gs1128_label = carton_gs1128_label
        if pallet_gs1128_label is not None:
            self.pallet_gs1128_label = pallet_gs1128_label
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this PackingDetail.  # noqa: E501


        :return: The id of this PackingDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PackingDetail.


        :param id: The id of this PackingDetail.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this PackingDetail.  # noqa: E501


        :return: The create_date of this PackingDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this PackingDetail.


        :param create_date: The create_date of this PackingDetail.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this PackingDetail.  # noqa: E501


        :return: The modify_date of this PackingDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this PackingDetail.


        :param modify_date: The modify_date of this PackingDetail.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def lob_id(self):
        """Gets the lob_id of this PackingDetail.  # noqa: E501


        :return: The lob_id of this PackingDetail.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this PackingDetail.


        :param lob_id: The lob_id of this PackingDetail.  # noqa: E501
        :type: int
        """

        self._lob_id = lob_id

    @property
    def order_id(self):
        """Gets the order_id of this PackingDetail.  # noqa: E501


        :return: The order_id of this PackingDetail.  # noqa: E501
        :rtype: float
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PackingDetail.


        :param order_id: The order_id of this PackingDetail.  # noqa: E501
        :type: float
        """

        self._order_id = order_id

    @property
    def pallet_id(self):
        """Gets the pallet_id of this PackingDetail.  # noqa: E501


        :return: The pallet_id of this PackingDetail.  # noqa: E501
        :rtype: int
        """
        return self._pallet_id

    @pallet_id.setter
    def pallet_id(self, pallet_id):
        """Sets the pallet_id of this PackingDetail.


        :param pallet_id: The pallet_id of this PackingDetail.  # noqa: E501
        :type: int
        """

        self._pallet_id = pallet_id

    @property
    def master_carton_id(self):
        """Gets the master_carton_id of this PackingDetail.  # noqa: E501


        :return: The master_carton_id of this PackingDetail.  # noqa: E501
        :rtype: int
        """
        return self._master_carton_id

    @master_carton_id.setter
    def master_carton_id(self, master_carton_id):
        """Sets the master_carton_id of this PackingDetail.


        :param master_carton_id: The master_carton_id of this PackingDetail.  # noqa: E501
        :type: int
        """

        self._master_carton_id = master_carton_id

    @property
    def carton_id(self):
        """Gets the carton_id of this PackingDetail.  # noqa: E501


        :return: The carton_id of this PackingDetail.  # noqa: E501
        :rtype: int
        """
        return self._carton_id

    @carton_id.setter
    def carton_id(self, carton_id):
        """Sets the carton_id of this PackingDetail.


        :param carton_id: The carton_id of this PackingDetail.  # noqa: E501
        :type: int
        """

        self._carton_id = carton_id

    @property
    def sku(self):
        """Gets the sku of this PackingDetail.  # noqa: E501


        :return: The sku of this PackingDetail.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this PackingDetail.


        :param sku: The sku of this PackingDetail.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def item_receipt_id(self):
        """Gets the item_receipt_id of this PackingDetail.  # noqa: E501


        :return: The item_receipt_id of this PackingDetail.  # noqa: E501
        :rtype: int
        """
        return self._item_receipt_id

    @item_receipt_id.setter
    def item_receipt_id(self, item_receipt_id):
        """Sets the item_receipt_id of this PackingDetail.


        :param item_receipt_id: The item_receipt_id of this PackingDetail.  # noqa: E501
        :type: int
        """

        self._item_receipt_id = item_receipt_id

    @property
    def line_item_id(self):
        """Gets the line_item_id of this PackingDetail.  # noqa: E501


        :return: The line_item_id of this PackingDetail.  # noqa: E501
        :rtype: int
        """
        return self._line_item_id

    @line_item_id.setter
    def line_item_id(self, line_item_id):
        """Sets the line_item_id of this PackingDetail.


        :param line_item_id: The line_item_id of this PackingDetail.  # noqa: E501
        :type: int
        """

        self._line_item_id = line_item_id

    @property
    def quantity(self):
        """Gets the quantity of this PackingDetail.  # noqa: E501


        :return: The quantity of this PackingDetail.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PackingDetail.


        :param quantity: The quantity of this PackingDetail.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def carton_gs1128_label(self):
        """Gets the carton_gs1128_label of this PackingDetail.  # noqa: E501


        :return: The carton_gs1128_label of this PackingDetail.  # noqa: E501
        :rtype: list[GS1128LabelDTO]
        """
        return self._carton_gs1128_label

    @carton_gs1128_label.setter
    def carton_gs1128_label(self, carton_gs1128_label):
        """Sets the carton_gs1128_label of this PackingDetail.


        :param carton_gs1128_label: The carton_gs1128_label of this PackingDetail.  # noqa: E501
        :type: list[GS1128LabelDTO]
        """

        self._carton_gs1128_label = carton_gs1128_label

    @property
    def pallet_gs1128_label(self):
        """Gets the pallet_gs1128_label of this PackingDetail.  # noqa: E501


        :return: The pallet_gs1128_label of this PackingDetail.  # noqa: E501
        :rtype: list[GS1128LabelDTO]
        """
        return self._pallet_gs1128_label

    @pallet_gs1128_label.setter
    def pallet_gs1128_label(self, pallet_gs1128_label):
        """Sets the pallet_gs1128_label of this PackingDetail.


        :param pallet_gs1128_label: The pallet_gs1128_label of this PackingDetail.  # noqa: E501
        :type: list[GS1128LabelDTO]
        """

        self._pallet_gs1128_label = pallet_gs1128_label

    @property
    def custom_fields(self):
        """Gets the custom_fields of this PackingDetail.  # noqa: E501


        :return: The custom_fields of this PackingDetail.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this PackingDetail.


        :param custom_fields: The custom_fields of this PackingDetail.  # noqa: E501
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
        if not isinstance(other, PackingDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other