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


class WorkBatch(object):
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
        'batch_priority_code': 'int',
        'description': 'str',
        'assigned_user_id': 'int',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'warehouse_id': 'warehouseId',
        'batch_priority_code': 'batchPriorityCode',
        'description': 'description',
        'assigned_user_id': 'assignedUserId',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, warehouse_id=None, batch_priority_code=None, description=None, assigned_user_id=None, create_date=None, modify_date=None, custom_fields=None):  # noqa: E501
        """WorkBatch - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._warehouse_id = None
        self._batch_priority_code = None
        self._description = None
        self._assigned_user_id = None
        self._create_date = None
        self._modify_date = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.warehouse_id = warehouse_id
        if batch_priority_code is not None:
            self.batch_priority_code = batch_priority_code
        if description is not None:
            self.description = description
        if assigned_user_id is not None:
            self.assigned_user_id = assigned_user_id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this WorkBatch.  # noqa: E501


        :return: The id of this WorkBatch.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkBatch.


        :param id: The id of this WorkBatch.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this WorkBatch.  # noqa: E501


        :return: The warehouse_id of this WorkBatch.  # noqa: E501
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this WorkBatch.


        :param warehouse_id: The warehouse_id of this WorkBatch.  # noqa: E501
        :type: int
        """
        if warehouse_id is None:
            raise ValueError("Invalid value for `warehouse_id`, must not be `None`")  # noqa: E501

        self._warehouse_id = warehouse_id

    @property
    def batch_priority_code(self):
        """Gets the batch_priority_code of this WorkBatch.  # noqa: E501


        :return: The batch_priority_code of this WorkBatch.  # noqa: E501
        :rtype: int
        """
        return self._batch_priority_code

    @batch_priority_code.setter
    def batch_priority_code(self, batch_priority_code):
        """Sets the batch_priority_code of this WorkBatch.


        :param batch_priority_code: The batch_priority_code of this WorkBatch.  # noqa: E501
        :type: int
        """

        self._batch_priority_code = batch_priority_code

    @property
    def description(self):
        """Gets the description of this WorkBatch.  # noqa: E501


        :return: The description of this WorkBatch.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkBatch.


        :param description: The description of this WorkBatch.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def assigned_user_id(self):
        """Gets the assigned_user_id of this WorkBatch.  # noqa: E501


        :return: The assigned_user_id of this WorkBatch.  # noqa: E501
        :rtype: int
        """
        return self._assigned_user_id

    @assigned_user_id.setter
    def assigned_user_id(self, assigned_user_id):
        """Sets the assigned_user_id of this WorkBatch.


        :param assigned_user_id: The assigned_user_id of this WorkBatch.  # noqa: E501
        :type: int
        """

        self._assigned_user_id = assigned_user_id

    @property
    def create_date(self):
        """Gets the create_date of this WorkBatch.  # noqa: E501


        :return: The create_date of this WorkBatch.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this WorkBatch.


        :param create_date: The create_date of this WorkBatch.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this WorkBatch.  # noqa: E501


        :return: The modify_date of this WorkBatch.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this WorkBatch.


        :param modify_date: The modify_date of this WorkBatch.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def custom_fields(self):
        """Gets the custom_fields of this WorkBatch.  # noqa: E501


        :return: The custom_fields of this WorkBatch.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this WorkBatch.


        :param custom_fields: The custom_fields of this WorkBatch.  # noqa: E501
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
        if not isinstance(other, WorkBatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
