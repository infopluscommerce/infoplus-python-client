# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: v3.0
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from Infoplus.models.receiving_worksheet_line_item import ReceivingWorksheetLineItem  # noqa: F401,E501


class ReceivingWorksheet(object):
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
        'warehouse_id': 'int',
        'po_no_id': 'int',
        'lob_id': 'int',
        'vendor_id': 'int',
        'status': 'str',
        'service_level': 'str',
        'receiving_process_id': 'int',
        'dock_date': 'datetime',
        'created_by': 'int',
        'worksheet_name': 'str',
        'carrier': 'str',
        'on_the_dock': 'bool',
        'auto_commit': 'bool',
        'line_items': 'list[ReceivingWorksheetLineItem]',
        'notes': 'str',
        'work_batch_id': 'int',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'warehouse_id': 'warehouseId',
        'po_no_id': 'poNoId',
        'lob_id': 'lobId',
        'vendor_id': 'vendorId',
        'status': 'status',
        'service_level': 'serviceLevel',
        'receiving_process_id': 'receivingProcessId',
        'dock_date': 'dockDate',
        'created_by': 'createdBy',
        'worksheet_name': 'worksheetName',
        'carrier': 'carrier',
        'on_the_dock': 'onTheDock',
        'auto_commit': 'autoCommit',
        'line_items': 'lineItems',
        'notes': 'notes',
        'work_batch_id': 'workBatchId',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, warehouse_id=None, po_no_id=None, lob_id=None, vendor_id=None, status=None, service_level=None, receiving_process_id=None, dock_date=None, created_by=None, worksheet_name=None, carrier=None, on_the_dock=False, auto_commit=False, line_items=None, notes=None, work_batch_id=None, create_date=None, modify_date=None, custom_fields=None):  # noqa: E501
        """ReceivingWorksheet - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._warehouse_id = None
        self._po_no_id = None
        self._lob_id = None
        self._vendor_id = None
        self._status = None
        self._service_level = None
        self._receiving_process_id = None
        self._dock_date = None
        self._created_by = None
        self._worksheet_name = None
        self._carrier = None
        self._on_the_dock = None
        self._auto_commit = None
        self._line_items = None
        self._notes = None
        self._work_batch_id = None
        self._create_date = None
        self._modify_date = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.warehouse_id = warehouse_id
        if po_no_id is not None:
            self.po_no_id = po_no_id
        if lob_id is not None:
            self.lob_id = lob_id
        if vendor_id is not None:
            self.vendor_id = vendor_id
        if status is not None:
            self.status = status
        self.service_level = service_level
        if receiving_process_id is not None:
            self.receiving_process_id = receiving_process_id
        if dock_date is not None:
            self.dock_date = dock_date
        if created_by is not None:
            self.created_by = created_by
        self.worksheet_name = worksheet_name
        if carrier is not None:
            self.carrier = carrier
        if on_the_dock is not None:
            self.on_the_dock = on_the_dock
        self.auto_commit = auto_commit
        if line_items is not None:
            self.line_items = line_items
        if notes is not None:
            self.notes = notes
        if work_batch_id is not None:
            self.work_batch_id = work_batch_id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this ReceivingWorksheet.  # noqa: E501


        :return: The id of this ReceivingWorksheet.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReceivingWorksheet.


        :param id: The id of this ReceivingWorksheet.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this ReceivingWorksheet.  # noqa: E501


        :return: The warehouse_id of this ReceivingWorksheet.  # noqa: E501
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this ReceivingWorksheet.


        :param warehouse_id: The warehouse_id of this ReceivingWorksheet.  # noqa: E501
        :type: int
        """
        if warehouse_id is None:
            raise ValueError("Invalid value for `warehouse_id`, must not be `None`")  # noqa: E501

        self._warehouse_id = warehouse_id

    @property
    def po_no_id(self):
        """Gets the po_no_id of this ReceivingWorksheet.  # noqa: E501


        :return: The po_no_id of this ReceivingWorksheet.  # noqa: E501
        :rtype: int
        """
        return self._po_no_id

    @po_no_id.setter
    def po_no_id(self, po_no_id):
        """Sets the po_no_id of this ReceivingWorksheet.


        :param po_no_id: The po_no_id of this ReceivingWorksheet.  # noqa: E501
        :type: int
        """

        self._po_no_id = po_no_id

    @property
    def lob_id(self):
        """Gets the lob_id of this ReceivingWorksheet.  # noqa: E501


        :return: The lob_id of this ReceivingWorksheet.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this ReceivingWorksheet.


        :param lob_id: The lob_id of this ReceivingWorksheet.  # noqa: E501
        :type: int
        """

        self._lob_id = lob_id

    @property
    def vendor_id(self):
        """Gets the vendor_id of this ReceivingWorksheet.  # noqa: E501


        :return: The vendor_id of this ReceivingWorksheet.  # noqa: E501
        :rtype: int
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this ReceivingWorksheet.


        :param vendor_id: The vendor_id of this ReceivingWorksheet.  # noqa: E501
        :type: int
        """

        self._vendor_id = vendor_id

    @property
    def status(self):
        """Gets the status of this ReceivingWorksheet.  # noqa: E501


        :return: The status of this ReceivingWorksheet.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ReceivingWorksheet.


        :param status: The status of this ReceivingWorksheet.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def service_level(self):
        """Gets the service_level of this ReceivingWorksheet.  # noqa: E501


        :return: The service_level of this ReceivingWorksheet.  # noqa: E501
        :rtype: str
        """
        return self._service_level

    @service_level.setter
    def service_level(self, service_level):
        """Sets the service_level of this ReceivingWorksheet.


        :param service_level: The service_level of this ReceivingWorksheet.  # noqa: E501
        :type: str
        """
        if service_level is None:
            raise ValueError("Invalid value for `service_level`, must not be `None`")  # noqa: E501

        self._service_level = service_level

    @property
    def receiving_process_id(self):
        """Gets the receiving_process_id of this ReceivingWorksheet.  # noqa: E501


        :return: The receiving_process_id of this ReceivingWorksheet.  # noqa: E501
        :rtype: int
        """
        return self._receiving_process_id

    @receiving_process_id.setter
    def receiving_process_id(self, receiving_process_id):
        """Sets the receiving_process_id of this ReceivingWorksheet.


        :param receiving_process_id: The receiving_process_id of this ReceivingWorksheet.  # noqa: E501
        :type: int
        """

        self._receiving_process_id = receiving_process_id

    @property
    def dock_date(self):
        """Gets the dock_date of this ReceivingWorksheet.  # noqa: E501


        :return: The dock_date of this ReceivingWorksheet.  # noqa: E501
        :rtype: datetime
        """
        return self._dock_date

    @dock_date.setter
    def dock_date(self, dock_date):
        """Sets the dock_date of this ReceivingWorksheet.


        :param dock_date: The dock_date of this ReceivingWorksheet.  # noqa: E501
        :type: datetime
        """

        self._dock_date = dock_date

    @property
    def created_by(self):
        """Gets the created_by of this ReceivingWorksheet.  # noqa: E501


        :return: The created_by of this ReceivingWorksheet.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ReceivingWorksheet.


        :param created_by: The created_by of this ReceivingWorksheet.  # noqa: E501
        :type: int
        """

        self._created_by = created_by

    @property
    def worksheet_name(self):
        """Gets the worksheet_name of this ReceivingWorksheet.  # noqa: E501


        :return: The worksheet_name of this ReceivingWorksheet.  # noqa: E501
        :rtype: str
        """
        return self._worksheet_name

    @worksheet_name.setter
    def worksheet_name(self, worksheet_name):
        """Sets the worksheet_name of this ReceivingWorksheet.


        :param worksheet_name: The worksheet_name of this ReceivingWorksheet.  # noqa: E501
        :type: str
        """
        if worksheet_name is None:
            raise ValueError("Invalid value for `worksheet_name`, must not be `None`")  # noqa: E501

        self._worksheet_name = worksheet_name

    @property
    def carrier(self):
        """Gets the carrier of this ReceivingWorksheet.  # noqa: E501


        :return: The carrier of this ReceivingWorksheet.  # noqa: E501
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this ReceivingWorksheet.


        :param carrier: The carrier of this ReceivingWorksheet.  # noqa: E501
        :type: str
        """

        self._carrier = carrier

    @property
    def on_the_dock(self):
        """Gets the on_the_dock of this ReceivingWorksheet.  # noqa: E501


        :return: The on_the_dock of this ReceivingWorksheet.  # noqa: E501
        :rtype: bool
        """
        return self._on_the_dock

    @on_the_dock.setter
    def on_the_dock(self, on_the_dock):
        """Sets the on_the_dock of this ReceivingWorksheet.


        :param on_the_dock: The on_the_dock of this ReceivingWorksheet.  # noqa: E501
        :type: bool
        """

        self._on_the_dock = on_the_dock

    @property
    def auto_commit(self):
        """Gets the auto_commit of this ReceivingWorksheet.  # noqa: E501


        :return: The auto_commit of this ReceivingWorksheet.  # noqa: E501
        :rtype: bool
        """
        return self._auto_commit

    @auto_commit.setter
    def auto_commit(self, auto_commit):
        """Sets the auto_commit of this ReceivingWorksheet.


        :param auto_commit: The auto_commit of this ReceivingWorksheet.  # noqa: E501
        :type: bool
        """
        if auto_commit is None:
            raise ValueError("Invalid value for `auto_commit`, must not be `None`")  # noqa: E501

        self._auto_commit = auto_commit

    @property
    def line_items(self):
        """Gets the line_items of this ReceivingWorksheet.  # noqa: E501


        :return: The line_items of this ReceivingWorksheet.  # noqa: E501
        :rtype: list[ReceivingWorksheetLineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this ReceivingWorksheet.


        :param line_items: The line_items of this ReceivingWorksheet.  # noqa: E501
        :type: list[ReceivingWorksheetLineItem]
        """

        self._line_items = line_items

    @property
    def notes(self):
        """Gets the notes of this ReceivingWorksheet.  # noqa: E501


        :return: The notes of this ReceivingWorksheet.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ReceivingWorksheet.


        :param notes: The notes of this ReceivingWorksheet.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def work_batch_id(self):
        """Gets the work_batch_id of this ReceivingWorksheet.  # noqa: E501


        :return: The work_batch_id of this ReceivingWorksheet.  # noqa: E501
        :rtype: int
        """
        return self._work_batch_id

    @work_batch_id.setter
    def work_batch_id(self, work_batch_id):
        """Sets the work_batch_id of this ReceivingWorksheet.


        :param work_batch_id: The work_batch_id of this ReceivingWorksheet.  # noqa: E501
        :type: int
        """

        self._work_batch_id = work_batch_id

    @property
    def create_date(self):
        """Gets the create_date of this ReceivingWorksheet.  # noqa: E501


        :return: The create_date of this ReceivingWorksheet.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this ReceivingWorksheet.


        :param create_date: The create_date of this ReceivingWorksheet.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this ReceivingWorksheet.  # noqa: E501


        :return: The modify_date of this ReceivingWorksheet.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this ReceivingWorksheet.


        :param modify_date: The modify_date of this ReceivingWorksheet.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ReceivingWorksheet.  # noqa: E501


        :return: The custom_fields of this ReceivingWorksheet.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ReceivingWorksheet.


        :param custom_fields: The custom_fields of this ReceivingWorksheet.  # noqa: E501
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
        if not isinstance(other, ReceivingWorksheet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
