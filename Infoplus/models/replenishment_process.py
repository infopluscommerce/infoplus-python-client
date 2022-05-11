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


class ReplenishmentProcess(object):
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
        'warehouse_id': 'int',
        'replenishment_plan_id': 'int',
        'status': 'str',
        'estimated_work': 'int',
        'work_batch_id': 'int',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'warehouse_id': 'warehouseId',
        'replenishment_plan_id': 'replenishmentPlanId',
        'status': 'status',
        'estimated_work': 'estimatedWork',
        'work_batch_id': 'workBatchId',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, create_date=None, modify_date=None, warehouse_id=None, replenishment_plan_id=None, status=None, estimated_work=None, work_batch_id=None, custom_fields=None):  # noqa: E501
        """ReplenishmentProcess - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._warehouse_id = None
        self._replenishment_plan_id = None
        self._status = None
        self._estimated_work = None
        self._work_batch_id = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        self.warehouse_id = warehouse_id
        self.replenishment_plan_id = replenishment_plan_id
        self.status = status
        if estimated_work is not None:
            self.estimated_work = estimated_work
        if work_batch_id is not None:
            self.work_batch_id = work_batch_id
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this ReplenishmentProcess.  # noqa: E501


        :return: The id of this ReplenishmentProcess.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReplenishmentProcess.


        :param id: The id of this ReplenishmentProcess.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this ReplenishmentProcess.  # noqa: E501


        :return: The create_date of this ReplenishmentProcess.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this ReplenishmentProcess.


        :param create_date: The create_date of this ReplenishmentProcess.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this ReplenishmentProcess.  # noqa: E501


        :return: The modify_date of this ReplenishmentProcess.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this ReplenishmentProcess.


        :param modify_date: The modify_date of this ReplenishmentProcess.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this ReplenishmentProcess.  # noqa: E501


        :return: The warehouse_id of this ReplenishmentProcess.  # noqa: E501
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this ReplenishmentProcess.


        :param warehouse_id: The warehouse_id of this ReplenishmentProcess.  # noqa: E501
        :type: int
        """
        if warehouse_id is None:
            raise ValueError("Invalid value for `warehouse_id`, must not be `None`")  # noqa: E501

        self._warehouse_id = warehouse_id

    @property
    def replenishment_plan_id(self):
        """Gets the replenishment_plan_id of this ReplenishmentProcess.  # noqa: E501


        :return: The replenishment_plan_id of this ReplenishmentProcess.  # noqa: E501
        :rtype: int
        """
        return self._replenishment_plan_id

    @replenishment_plan_id.setter
    def replenishment_plan_id(self, replenishment_plan_id):
        """Sets the replenishment_plan_id of this ReplenishmentProcess.


        :param replenishment_plan_id: The replenishment_plan_id of this ReplenishmentProcess.  # noqa: E501
        :type: int
        """
        if replenishment_plan_id is None:
            raise ValueError("Invalid value for `replenishment_plan_id`, must not be `None`")  # noqa: E501

        self._replenishment_plan_id = replenishment_plan_id

    @property
    def status(self):
        """Gets the status of this ReplenishmentProcess.  # noqa: E501


        :return: The status of this ReplenishmentProcess.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ReplenishmentProcess.


        :param status: The status of this ReplenishmentProcess.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def estimated_work(self):
        """Gets the estimated_work of this ReplenishmentProcess.  # noqa: E501


        :return: The estimated_work of this ReplenishmentProcess.  # noqa: E501
        :rtype: int
        """
        return self._estimated_work

    @estimated_work.setter
    def estimated_work(self, estimated_work):
        """Sets the estimated_work of this ReplenishmentProcess.


        :param estimated_work: The estimated_work of this ReplenishmentProcess.  # noqa: E501
        :type: int
        """

        self._estimated_work = estimated_work

    @property
    def work_batch_id(self):
        """Gets the work_batch_id of this ReplenishmentProcess.  # noqa: E501


        :return: The work_batch_id of this ReplenishmentProcess.  # noqa: E501
        :rtype: int
        """
        return self._work_batch_id

    @work_batch_id.setter
    def work_batch_id(self, work_batch_id):
        """Sets the work_batch_id of this ReplenishmentProcess.


        :param work_batch_id: The work_batch_id of this ReplenishmentProcess.  # noqa: E501
        :type: int
        """

        self._work_batch_id = work_batch_id

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ReplenishmentProcess.  # noqa: E501


        :return: The custom_fields of this ReplenishmentProcess.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ReplenishmentProcess.


        :param custom_fields: The custom_fields of this ReplenishmentProcess.  # noqa: E501
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
        if not isinstance(other, ReplenishmentProcess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
