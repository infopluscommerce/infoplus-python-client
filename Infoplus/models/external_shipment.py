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


class ExternalShipment(object):
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
        'order_id': 'float',
        'carrier_id': 'int',
        'parcel_account_id': 'int',
        'third_party_parcel_account_id': 'int',
        'freight': 'float',
        'tracking_no': 'str',
        'dim1_in': 'float',
        'dim2_in': 'float',
        'dim3_in': 'float',
        'weight_lbs': 'float',
        'dim_weight': 'float',
        'residential': 'bool',
        'lob_id': 'int',
        'zone': 'str',
        'ship_date': 'datetime',
        'status': 'str',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'order_id': 'orderId',
        'carrier_id': 'carrierId',
        'parcel_account_id': 'parcelAccountId',
        'third_party_parcel_account_id': 'thirdPartyParcelAccountId',
        'freight': 'freight',
        'tracking_no': 'trackingNo',
        'dim1_in': 'dim1In',
        'dim2_in': 'dim2In',
        'dim3_in': 'dim3In',
        'weight_lbs': 'weightLbs',
        'dim_weight': 'dimWeight',
        'residential': 'residential',
        'lob_id': 'lobId',
        'zone': 'zone',
        'ship_date': 'shipDate',
        'status': 'status',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, create_date=None, modify_date=None, order_id=None, carrier_id=None, parcel_account_id=None, third_party_parcel_account_id=None, freight=None, tracking_no=None, dim1_in=None, dim2_in=None, dim3_in=None, weight_lbs=None, dim_weight=None, residential=False, lob_id=None, zone=None, ship_date=None, status=None, custom_fields=None):  # noqa: E501
        """ExternalShipment - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._order_id = None
        self._carrier_id = None
        self._parcel_account_id = None
        self._third_party_parcel_account_id = None
        self._freight = None
        self._tracking_no = None
        self._dim1_in = None
        self._dim2_in = None
        self._dim3_in = None
        self._weight_lbs = None
        self._dim_weight = None
        self._residential = None
        self._lob_id = None
        self._zone = None
        self._ship_date = None
        self._status = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        self.order_id = order_id
        self.carrier_id = carrier_id
        self.parcel_account_id = parcel_account_id
        if third_party_parcel_account_id is not None:
            self.third_party_parcel_account_id = third_party_parcel_account_id
        if freight is not None:
            self.freight = freight
        self.tracking_no = tracking_no
        if dim1_in is not None:
            self.dim1_in = dim1_in
        if dim2_in is not None:
            self.dim2_in = dim2_in
        if dim3_in is not None:
            self.dim3_in = dim3_in
        if weight_lbs is not None:
            self.weight_lbs = weight_lbs
        if dim_weight is not None:
            self.dim_weight = dim_weight
        if residential is not None:
            self.residential = residential
        self.lob_id = lob_id
        if zone is not None:
            self.zone = zone
        if ship_date is not None:
            self.ship_date = ship_date
        if status is not None:
            self.status = status
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this ExternalShipment.  # noqa: E501


        :return: The id of this ExternalShipment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalShipment.


        :param id: The id of this ExternalShipment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this ExternalShipment.  # noqa: E501


        :return: The create_date of this ExternalShipment.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this ExternalShipment.


        :param create_date: The create_date of this ExternalShipment.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this ExternalShipment.  # noqa: E501


        :return: The modify_date of this ExternalShipment.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this ExternalShipment.


        :param modify_date: The modify_date of this ExternalShipment.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def order_id(self):
        """Gets the order_id of this ExternalShipment.  # noqa: E501


        :return: The order_id of this ExternalShipment.  # noqa: E501
        :rtype: float
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ExternalShipment.


        :param order_id: The order_id of this ExternalShipment.  # noqa: E501
        :type: float
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def carrier_id(self):
        """Gets the carrier_id of this ExternalShipment.  # noqa: E501


        :return: The carrier_id of this ExternalShipment.  # noqa: E501
        :rtype: int
        """
        return self._carrier_id

    @carrier_id.setter
    def carrier_id(self, carrier_id):
        """Sets the carrier_id of this ExternalShipment.


        :param carrier_id: The carrier_id of this ExternalShipment.  # noqa: E501
        :type: int
        """
        if carrier_id is None:
            raise ValueError("Invalid value for `carrier_id`, must not be `None`")  # noqa: E501

        self._carrier_id = carrier_id

    @property
    def parcel_account_id(self):
        """Gets the parcel_account_id of this ExternalShipment.  # noqa: E501


        :return: The parcel_account_id of this ExternalShipment.  # noqa: E501
        :rtype: int
        """
        return self._parcel_account_id

    @parcel_account_id.setter
    def parcel_account_id(self, parcel_account_id):
        """Sets the parcel_account_id of this ExternalShipment.


        :param parcel_account_id: The parcel_account_id of this ExternalShipment.  # noqa: E501
        :type: int
        """
        if parcel_account_id is None:
            raise ValueError("Invalid value for `parcel_account_id`, must not be `None`")  # noqa: E501

        self._parcel_account_id = parcel_account_id

    @property
    def third_party_parcel_account_id(self):
        """Gets the third_party_parcel_account_id of this ExternalShipment.  # noqa: E501


        :return: The third_party_parcel_account_id of this ExternalShipment.  # noqa: E501
        :rtype: int
        """
        return self._third_party_parcel_account_id

    @third_party_parcel_account_id.setter
    def third_party_parcel_account_id(self, third_party_parcel_account_id):
        """Sets the third_party_parcel_account_id of this ExternalShipment.


        :param third_party_parcel_account_id: The third_party_parcel_account_id of this ExternalShipment.  # noqa: E501
        :type: int
        """

        self._third_party_parcel_account_id = third_party_parcel_account_id

    @property
    def freight(self):
        """Gets the freight of this ExternalShipment.  # noqa: E501


        :return: The freight of this ExternalShipment.  # noqa: E501
        :rtype: float
        """
        return self._freight

    @freight.setter
    def freight(self, freight):
        """Sets the freight of this ExternalShipment.


        :param freight: The freight of this ExternalShipment.  # noqa: E501
        :type: float
        """

        self._freight = freight

    @property
    def tracking_no(self):
        """Gets the tracking_no of this ExternalShipment.  # noqa: E501


        :return: The tracking_no of this ExternalShipment.  # noqa: E501
        :rtype: str
        """
        return self._tracking_no

    @tracking_no.setter
    def tracking_no(self, tracking_no):
        """Sets the tracking_no of this ExternalShipment.


        :param tracking_no: The tracking_no of this ExternalShipment.  # noqa: E501
        :type: str
        """
        if tracking_no is None:
            raise ValueError("Invalid value for `tracking_no`, must not be `None`")  # noqa: E501

        self._tracking_no = tracking_no

    @property
    def dim1_in(self):
        """Gets the dim1_in of this ExternalShipment.  # noqa: E501


        :return: The dim1_in of this ExternalShipment.  # noqa: E501
        :rtype: float
        """
        return self._dim1_in

    @dim1_in.setter
    def dim1_in(self, dim1_in):
        """Sets the dim1_in of this ExternalShipment.


        :param dim1_in: The dim1_in of this ExternalShipment.  # noqa: E501
        :type: float
        """

        self._dim1_in = dim1_in

    @property
    def dim2_in(self):
        """Gets the dim2_in of this ExternalShipment.  # noqa: E501


        :return: The dim2_in of this ExternalShipment.  # noqa: E501
        :rtype: float
        """
        return self._dim2_in

    @dim2_in.setter
    def dim2_in(self, dim2_in):
        """Sets the dim2_in of this ExternalShipment.


        :param dim2_in: The dim2_in of this ExternalShipment.  # noqa: E501
        :type: float
        """

        self._dim2_in = dim2_in

    @property
    def dim3_in(self):
        """Gets the dim3_in of this ExternalShipment.  # noqa: E501


        :return: The dim3_in of this ExternalShipment.  # noqa: E501
        :rtype: float
        """
        return self._dim3_in

    @dim3_in.setter
    def dim3_in(self, dim3_in):
        """Sets the dim3_in of this ExternalShipment.


        :param dim3_in: The dim3_in of this ExternalShipment.  # noqa: E501
        :type: float
        """

        self._dim3_in = dim3_in

    @property
    def weight_lbs(self):
        """Gets the weight_lbs of this ExternalShipment.  # noqa: E501


        :return: The weight_lbs of this ExternalShipment.  # noqa: E501
        :rtype: float
        """
        return self._weight_lbs

    @weight_lbs.setter
    def weight_lbs(self, weight_lbs):
        """Sets the weight_lbs of this ExternalShipment.


        :param weight_lbs: The weight_lbs of this ExternalShipment.  # noqa: E501
        :type: float
        """

        self._weight_lbs = weight_lbs

    @property
    def dim_weight(self):
        """Gets the dim_weight of this ExternalShipment.  # noqa: E501


        :return: The dim_weight of this ExternalShipment.  # noqa: E501
        :rtype: float
        """
        return self._dim_weight

    @dim_weight.setter
    def dim_weight(self, dim_weight):
        """Sets the dim_weight of this ExternalShipment.


        :param dim_weight: The dim_weight of this ExternalShipment.  # noqa: E501
        :type: float
        """

        self._dim_weight = dim_weight

    @property
    def residential(self):
        """Gets the residential of this ExternalShipment.  # noqa: E501


        :return: The residential of this ExternalShipment.  # noqa: E501
        :rtype: bool
        """
        return self._residential

    @residential.setter
    def residential(self, residential):
        """Sets the residential of this ExternalShipment.


        :param residential: The residential of this ExternalShipment.  # noqa: E501
        :type: bool
        """

        self._residential = residential

    @property
    def lob_id(self):
        """Gets the lob_id of this ExternalShipment.  # noqa: E501


        :return: The lob_id of this ExternalShipment.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this ExternalShipment.


        :param lob_id: The lob_id of this ExternalShipment.  # noqa: E501
        :type: int
        """
        if lob_id is None:
            raise ValueError("Invalid value for `lob_id`, must not be `None`")  # noqa: E501

        self._lob_id = lob_id

    @property
    def zone(self):
        """Gets the zone of this ExternalShipment.  # noqa: E501


        :return: The zone of this ExternalShipment.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this ExternalShipment.


        :param zone: The zone of this ExternalShipment.  # noqa: E501
        :type: str
        """

        self._zone = zone

    @property
    def ship_date(self):
        """Gets the ship_date of this ExternalShipment.  # noqa: E501


        :return: The ship_date of this ExternalShipment.  # noqa: E501
        :rtype: datetime
        """
        return self._ship_date

    @ship_date.setter
    def ship_date(self, ship_date):
        """Sets the ship_date of this ExternalShipment.


        :param ship_date: The ship_date of this ExternalShipment.  # noqa: E501
        :type: datetime
        """

        self._ship_date = ship_date

    @property
    def status(self):
        """Gets the status of this ExternalShipment.  # noqa: E501


        :return: The status of this ExternalShipment.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExternalShipment.


        :param status: The status of this ExternalShipment.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ExternalShipment.  # noqa: E501


        :return: The custom_fields of this ExternalShipment.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ExternalShipment.


        :param custom_fields: The custom_fields of this ExternalShipment.  # noqa: E501
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
        if not isinstance(other, ExternalShipment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
