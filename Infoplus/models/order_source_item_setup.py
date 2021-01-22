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


class OrderSourceItemSetup(object):
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
        'modify_date': 'datetime',
        'create_date': 'datetime',
        'lob_id': 'int',
        'sku': 'str',
        'order_source_id': 'int',
        'packing_notes': 'str',
        'sku_translation': 'str',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'modify_date': 'modifyDate',
        'create_date': 'createDate',
        'lob_id': 'lobId',
        'sku': 'sku',
        'order_source_id': 'orderSourceId',
        'packing_notes': 'packingNotes',
        'sku_translation': 'skuTranslation',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, modify_date=None, create_date=None, lob_id=None, sku=None, order_source_id=None, packing_notes=None, sku_translation=None, custom_fields=None):  # noqa: E501
        """OrderSourceItemSetup - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._modify_date = None
        self._create_date = None
        self._lob_id = None
        self._sku = None
        self._order_source_id = None
        self._packing_notes = None
        self._sku_translation = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if modify_date is not None:
            self.modify_date = modify_date
        if create_date is not None:
            self.create_date = create_date
        self.lob_id = lob_id
        self.sku = sku
        self.order_source_id = order_source_id
        if packing_notes is not None:
            self.packing_notes = packing_notes
        if sku_translation is not None:
            self.sku_translation = sku_translation
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this OrderSourceItemSetup.  # noqa: E501


        :return: The id of this OrderSourceItemSetup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderSourceItemSetup.


        :param id: The id of this OrderSourceItemSetup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def modify_date(self):
        """Gets the modify_date of this OrderSourceItemSetup.  # noqa: E501


        :return: The modify_date of this OrderSourceItemSetup.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this OrderSourceItemSetup.


        :param modify_date: The modify_date of this OrderSourceItemSetup.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def create_date(self):
        """Gets the create_date of this OrderSourceItemSetup.  # noqa: E501


        :return: The create_date of this OrderSourceItemSetup.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this OrderSourceItemSetup.


        :param create_date: The create_date of this OrderSourceItemSetup.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def lob_id(self):
        """Gets the lob_id of this OrderSourceItemSetup.  # noqa: E501


        :return: The lob_id of this OrderSourceItemSetup.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this OrderSourceItemSetup.


        :param lob_id: The lob_id of this OrderSourceItemSetup.  # noqa: E501
        :type: int
        """
        if lob_id is None:
            raise ValueError("Invalid value for `lob_id`, must not be `None`")  # noqa: E501

        self._lob_id = lob_id

    @property
    def sku(self):
        """Gets the sku of this OrderSourceItemSetup.  # noqa: E501


        :return: The sku of this OrderSourceItemSetup.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this OrderSourceItemSetup.


        :param sku: The sku of this OrderSourceItemSetup.  # noqa: E501
        :type: str
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")  # noqa: E501

        self._sku = sku

    @property
    def order_source_id(self):
        """Gets the order_source_id of this OrderSourceItemSetup.  # noqa: E501


        :return: The order_source_id of this OrderSourceItemSetup.  # noqa: E501
        :rtype: int
        """
        return self._order_source_id

    @order_source_id.setter
    def order_source_id(self, order_source_id):
        """Sets the order_source_id of this OrderSourceItemSetup.


        :param order_source_id: The order_source_id of this OrderSourceItemSetup.  # noqa: E501
        :type: int
        """
        if order_source_id is None:
            raise ValueError("Invalid value for `order_source_id`, must not be `None`")  # noqa: E501

        self._order_source_id = order_source_id

    @property
    def packing_notes(self):
        """Gets the packing_notes of this OrderSourceItemSetup.  # noqa: E501


        :return: The packing_notes of this OrderSourceItemSetup.  # noqa: E501
        :rtype: str
        """
        return self._packing_notes

    @packing_notes.setter
    def packing_notes(self, packing_notes):
        """Sets the packing_notes of this OrderSourceItemSetup.


        :param packing_notes: The packing_notes of this OrderSourceItemSetup.  # noqa: E501
        :type: str
        """

        self._packing_notes = packing_notes

    @property
    def sku_translation(self):
        """Gets the sku_translation of this OrderSourceItemSetup.  # noqa: E501


        :return: The sku_translation of this OrderSourceItemSetup.  # noqa: E501
        :rtype: str
        """
        return self._sku_translation

    @sku_translation.setter
    def sku_translation(self, sku_translation):
        """Sets the sku_translation of this OrderSourceItemSetup.


        :param sku_translation: The sku_translation of this OrderSourceItemSetup.  # noqa: E501
        :type: str
        """

        self._sku_translation = sku_translation

    @property
    def custom_fields(self):
        """Gets the custom_fields of this OrderSourceItemSetup.  # noqa: E501


        :return: The custom_fields of this OrderSourceItemSetup.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this OrderSourceItemSetup.


        :param custom_fields: The custom_fields of this OrderSourceItemSetup.  # noqa: E501
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
        if not isinstance(other, OrderSourceItemSetup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
