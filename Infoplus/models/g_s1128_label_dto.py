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


class GS1128LabelDTO(object):
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
        'gs1128_template_id': 'int',
        'no_of_copies': 'int',
        'lob_id': 'int',
        'order_no': 'float',
        'record_type': 'str',
        'pallet_load_id': 'int',
        'master_carton_load_id': 'int',
        'carton_id': 'int',
        'line_item_id': 'int',
        'line_item_unit_no': 'int',
        'modify_date': 'datetime',
        'sscc': 'str',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'create_date': 'createDate',
        'gs1128_template_id': 'gs1128TemplateId',
        'no_of_copies': 'noOfCopies',
        'lob_id': 'lobId',
        'order_no': 'orderNo',
        'record_type': 'recordType',
        'pallet_load_id': 'palletLoadId',
        'master_carton_load_id': 'masterCartonLoadId',
        'carton_id': 'cartonId',
        'line_item_id': 'lineItemId',
        'line_item_unit_no': 'lineItemUnitNo',
        'modify_date': 'modifyDate',
        'sscc': 'sscc',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, create_date=None, gs1128_template_id=None, no_of_copies=None, lob_id=None, order_no=None, record_type=None, pallet_load_id=None, master_carton_load_id=None, carton_id=None, line_item_id=None, line_item_unit_no=None, modify_date=None, sscc=None, custom_fields=None):  # noqa: E501
        """GS1128LabelDTO - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_date = None
        self._gs1128_template_id = None
        self._no_of_copies = None
        self._lob_id = None
        self._order_no = None
        self._record_type = None
        self._pallet_load_id = None
        self._master_carton_load_id = None
        self._carton_id = None
        self._line_item_id = None
        self._line_item_unit_no = None
        self._modify_date = None
        self._sscc = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if gs1128_template_id is not None:
            self.gs1128_template_id = gs1128_template_id
        if no_of_copies is not None:
            self.no_of_copies = no_of_copies
        self.lob_id = lob_id
        self.order_no = order_no
        if record_type is not None:
            self.record_type = record_type
        if pallet_load_id is not None:
            self.pallet_load_id = pallet_load_id
        if master_carton_load_id is not None:
            self.master_carton_load_id = master_carton_load_id
        if carton_id is not None:
            self.carton_id = carton_id
        if line_item_id is not None:
            self.line_item_id = line_item_id
        if line_item_unit_no is not None:
            self.line_item_unit_no = line_item_unit_no
        if modify_date is not None:
            self.modify_date = modify_date
        if sscc is not None:
            self.sscc = sscc
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this GS1128LabelDTO.  # noqa: E501


        :return: The id of this GS1128LabelDTO.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GS1128LabelDTO.


        :param id: The id of this GS1128LabelDTO.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this GS1128LabelDTO.  # noqa: E501


        :return: The create_date of this GS1128LabelDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this GS1128LabelDTO.


        :param create_date: The create_date of this GS1128LabelDTO.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def gs1128_template_id(self):
        """Gets the gs1128_template_id of this GS1128LabelDTO.  # noqa: E501


        :return: The gs1128_template_id of this GS1128LabelDTO.  # noqa: E501
        :rtype: int
        """
        return self._gs1128_template_id

    @gs1128_template_id.setter
    def gs1128_template_id(self, gs1128_template_id):
        """Sets the gs1128_template_id of this GS1128LabelDTO.


        :param gs1128_template_id: The gs1128_template_id of this GS1128LabelDTO.  # noqa: E501
        :type: int
        """

        self._gs1128_template_id = gs1128_template_id

    @property
    def no_of_copies(self):
        """Gets the no_of_copies of this GS1128LabelDTO.  # noqa: E501


        :return: The no_of_copies of this GS1128LabelDTO.  # noqa: E501
        :rtype: int
        """
        return self._no_of_copies

    @no_of_copies.setter
    def no_of_copies(self, no_of_copies):
        """Sets the no_of_copies of this GS1128LabelDTO.


        :param no_of_copies: The no_of_copies of this GS1128LabelDTO.  # noqa: E501
        :type: int
        """

        self._no_of_copies = no_of_copies

    @property
    def lob_id(self):
        """Gets the lob_id of this GS1128LabelDTO.  # noqa: E501


        :return: The lob_id of this GS1128LabelDTO.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this GS1128LabelDTO.


        :param lob_id: The lob_id of this GS1128LabelDTO.  # noqa: E501
        :type: int
        """
        if lob_id is None:
            raise ValueError("Invalid value for `lob_id`, must not be `None`")  # noqa: E501

        self._lob_id = lob_id

    @property
    def order_no(self):
        """Gets the order_no of this GS1128LabelDTO.  # noqa: E501


        :return: The order_no of this GS1128LabelDTO.  # noqa: E501
        :rtype: float
        """
        return self._order_no

    @order_no.setter
    def order_no(self, order_no):
        """Sets the order_no of this GS1128LabelDTO.


        :param order_no: The order_no of this GS1128LabelDTO.  # noqa: E501
        :type: float
        """
        if order_no is None:
            raise ValueError("Invalid value for `order_no`, must not be `None`")  # noqa: E501

        self._order_no = order_no

    @property
    def record_type(self):
        """Gets the record_type of this GS1128LabelDTO.  # noqa: E501


        :return: The record_type of this GS1128LabelDTO.  # noqa: E501
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this GS1128LabelDTO.


        :param record_type: The record_type of this GS1128LabelDTO.  # noqa: E501
        :type: str
        """

        self._record_type = record_type

    @property
    def pallet_load_id(self):
        """Gets the pallet_load_id of this GS1128LabelDTO.  # noqa: E501


        :return: The pallet_load_id of this GS1128LabelDTO.  # noqa: E501
        :rtype: int
        """
        return self._pallet_load_id

    @pallet_load_id.setter
    def pallet_load_id(self, pallet_load_id):
        """Sets the pallet_load_id of this GS1128LabelDTO.


        :param pallet_load_id: The pallet_load_id of this GS1128LabelDTO.  # noqa: E501
        :type: int
        """

        self._pallet_load_id = pallet_load_id

    @property
    def master_carton_load_id(self):
        """Gets the master_carton_load_id of this GS1128LabelDTO.  # noqa: E501


        :return: The master_carton_load_id of this GS1128LabelDTO.  # noqa: E501
        :rtype: int
        """
        return self._master_carton_load_id

    @master_carton_load_id.setter
    def master_carton_load_id(self, master_carton_load_id):
        """Sets the master_carton_load_id of this GS1128LabelDTO.


        :param master_carton_load_id: The master_carton_load_id of this GS1128LabelDTO.  # noqa: E501
        :type: int
        """

        self._master_carton_load_id = master_carton_load_id

    @property
    def carton_id(self):
        """Gets the carton_id of this GS1128LabelDTO.  # noqa: E501


        :return: The carton_id of this GS1128LabelDTO.  # noqa: E501
        :rtype: int
        """
        return self._carton_id

    @carton_id.setter
    def carton_id(self, carton_id):
        """Sets the carton_id of this GS1128LabelDTO.


        :param carton_id: The carton_id of this GS1128LabelDTO.  # noqa: E501
        :type: int
        """

        self._carton_id = carton_id

    @property
    def line_item_id(self):
        """Gets the line_item_id of this GS1128LabelDTO.  # noqa: E501


        :return: The line_item_id of this GS1128LabelDTO.  # noqa: E501
        :rtype: int
        """
        return self._line_item_id

    @line_item_id.setter
    def line_item_id(self, line_item_id):
        """Sets the line_item_id of this GS1128LabelDTO.


        :param line_item_id: The line_item_id of this GS1128LabelDTO.  # noqa: E501
        :type: int
        """

        self._line_item_id = line_item_id

    @property
    def line_item_unit_no(self):
        """Gets the line_item_unit_no of this GS1128LabelDTO.  # noqa: E501


        :return: The line_item_unit_no of this GS1128LabelDTO.  # noqa: E501
        :rtype: int
        """
        return self._line_item_unit_no

    @line_item_unit_no.setter
    def line_item_unit_no(self, line_item_unit_no):
        """Sets the line_item_unit_no of this GS1128LabelDTO.


        :param line_item_unit_no: The line_item_unit_no of this GS1128LabelDTO.  # noqa: E501
        :type: int
        """

        self._line_item_unit_no = line_item_unit_no

    @property
    def modify_date(self):
        """Gets the modify_date of this GS1128LabelDTO.  # noqa: E501


        :return: The modify_date of this GS1128LabelDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this GS1128LabelDTO.


        :param modify_date: The modify_date of this GS1128LabelDTO.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def sscc(self):
        """Gets the sscc of this GS1128LabelDTO.  # noqa: E501


        :return: The sscc of this GS1128LabelDTO.  # noqa: E501
        :rtype: str
        """
        return self._sscc

    @sscc.setter
    def sscc(self, sscc):
        """Sets the sscc of this GS1128LabelDTO.


        :param sscc: The sscc of this GS1128LabelDTO.  # noqa: E501
        :type: str
        """

        self._sscc = sscc

    @property
    def custom_fields(self):
        """Gets the custom_fields of this GS1128LabelDTO.  # noqa: E501


        :return: The custom_fields of this GS1128LabelDTO.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this GS1128LabelDTO.


        :param custom_fields: The custom_fields of this GS1128LabelDTO.  # noqa: E501
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
        if not isinstance(other, GS1128LabelDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
