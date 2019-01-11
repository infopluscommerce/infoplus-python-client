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


class FulfillmentProcessLog(object):
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
        'process_no_id': 'int',
        'warehouse_id': 'int',
        'order_id': 'float',
        'lob_id': 'int',
        'sku_id': 'int',
        'location_id': 'int',
        'item_receipt_id': 'int',
        'allocation_issue_type': 'str',
        'message': 'str',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'process_no_id': 'processNoId',
        'warehouse_id': 'warehouseId',
        'order_id': 'orderId',
        'lob_id': 'lobId',
        'sku_id': 'skuId',
        'location_id': 'locationId',
        'item_receipt_id': 'itemReceiptId',
        'allocation_issue_type': 'allocationIssueType',
        'message': 'message',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, create_date=None, modify_date=None, process_no_id=None, warehouse_id=None, order_id=None, lob_id=None, sku_id=None, location_id=None, item_receipt_id=None, allocation_issue_type=None, message=None, custom_fields=None):  # noqa: E501
        """FulfillmentProcessLog - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._process_no_id = None
        self._warehouse_id = None
        self._order_id = None
        self._lob_id = None
        self._sku_id = None
        self._location_id = None
        self._item_receipt_id = None
        self._allocation_issue_type = None
        self._message = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if process_no_id is not None:
            self.process_no_id = process_no_id
        if warehouse_id is not None:
            self.warehouse_id = warehouse_id
        if order_id is not None:
            self.order_id = order_id
        if lob_id is not None:
            self.lob_id = lob_id
        if sku_id is not None:
            self.sku_id = sku_id
        if location_id is not None:
            self.location_id = location_id
        if item_receipt_id is not None:
            self.item_receipt_id = item_receipt_id
        if allocation_issue_type is not None:
            self.allocation_issue_type = allocation_issue_type
        if message is not None:
            self.message = message
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this FulfillmentProcessLog.  # noqa: E501


        :return: The id of this FulfillmentProcessLog.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FulfillmentProcessLog.


        :param id: The id of this FulfillmentProcessLog.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this FulfillmentProcessLog.  # noqa: E501


        :return: The create_date of this FulfillmentProcessLog.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this FulfillmentProcessLog.


        :param create_date: The create_date of this FulfillmentProcessLog.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this FulfillmentProcessLog.  # noqa: E501


        :return: The modify_date of this FulfillmentProcessLog.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this FulfillmentProcessLog.


        :param modify_date: The modify_date of this FulfillmentProcessLog.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def process_no_id(self):
        """Gets the process_no_id of this FulfillmentProcessLog.  # noqa: E501


        :return: The process_no_id of this FulfillmentProcessLog.  # noqa: E501
        :rtype: int
        """
        return self._process_no_id

    @process_no_id.setter
    def process_no_id(self, process_no_id):
        """Sets the process_no_id of this FulfillmentProcessLog.


        :param process_no_id: The process_no_id of this FulfillmentProcessLog.  # noqa: E501
        :type: int
        """

        self._process_no_id = process_no_id

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this FulfillmentProcessLog.  # noqa: E501


        :return: The warehouse_id of this FulfillmentProcessLog.  # noqa: E501
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this FulfillmentProcessLog.


        :param warehouse_id: The warehouse_id of this FulfillmentProcessLog.  # noqa: E501
        :type: int
        """

        self._warehouse_id = warehouse_id

    @property
    def order_id(self):
        """Gets the order_id of this FulfillmentProcessLog.  # noqa: E501


        :return: The order_id of this FulfillmentProcessLog.  # noqa: E501
        :rtype: float
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this FulfillmentProcessLog.


        :param order_id: The order_id of this FulfillmentProcessLog.  # noqa: E501
        :type: float
        """

        self._order_id = order_id

    @property
    def lob_id(self):
        """Gets the lob_id of this FulfillmentProcessLog.  # noqa: E501


        :return: The lob_id of this FulfillmentProcessLog.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this FulfillmentProcessLog.


        :param lob_id: The lob_id of this FulfillmentProcessLog.  # noqa: E501
        :type: int
        """

        self._lob_id = lob_id

    @property
    def sku_id(self):
        """Gets the sku_id of this FulfillmentProcessLog.  # noqa: E501


        :return: The sku_id of this FulfillmentProcessLog.  # noqa: E501
        :rtype: int
        """
        return self._sku_id

    @sku_id.setter
    def sku_id(self, sku_id):
        """Sets the sku_id of this FulfillmentProcessLog.


        :param sku_id: The sku_id of this FulfillmentProcessLog.  # noqa: E501
        :type: int
        """

        self._sku_id = sku_id

    @property
    def location_id(self):
        """Gets the location_id of this FulfillmentProcessLog.  # noqa: E501


        :return: The location_id of this FulfillmentProcessLog.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this FulfillmentProcessLog.


        :param location_id: The location_id of this FulfillmentProcessLog.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def item_receipt_id(self):
        """Gets the item_receipt_id of this FulfillmentProcessLog.  # noqa: E501


        :return: The item_receipt_id of this FulfillmentProcessLog.  # noqa: E501
        :rtype: int
        """
        return self._item_receipt_id

    @item_receipt_id.setter
    def item_receipt_id(self, item_receipt_id):
        """Sets the item_receipt_id of this FulfillmentProcessLog.


        :param item_receipt_id: The item_receipt_id of this FulfillmentProcessLog.  # noqa: E501
        :type: int
        """

        self._item_receipt_id = item_receipt_id

    @property
    def allocation_issue_type(self):
        """Gets the allocation_issue_type of this FulfillmentProcessLog.  # noqa: E501


        :return: The allocation_issue_type of this FulfillmentProcessLog.  # noqa: E501
        :rtype: str
        """
        return self._allocation_issue_type

    @allocation_issue_type.setter
    def allocation_issue_type(self, allocation_issue_type):
        """Sets the allocation_issue_type of this FulfillmentProcessLog.


        :param allocation_issue_type: The allocation_issue_type of this FulfillmentProcessLog.  # noqa: E501
        :type: str
        """

        self._allocation_issue_type = allocation_issue_type

    @property
    def message(self):
        """Gets the message of this FulfillmentProcessLog.  # noqa: E501


        :return: The message of this FulfillmentProcessLog.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this FulfillmentProcessLog.


        :param message: The message of this FulfillmentProcessLog.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def custom_fields(self):
        """Gets the custom_fields of this FulfillmentProcessLog.  # noqa: E501


        :return: The custom_fields of this FulfillmentProcessLog.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this FulfillmentProcessLog.


        :param custom_fields: The custom_fields of this FulfillmentProcessLog.  # noqa: E501
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
        if not isinstance(other, FulfillmentProcessLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
