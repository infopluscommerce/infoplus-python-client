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


class Warehouse(object):
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
        'client': 'int',
        'name': 'str',
        'address': 'str',
        'company': 'str',
        'street1': 'str',
        'street2': 'str',
        'street3': 'str',
        'city': 'str',
        'state': 'str',
        'zip': 'str',
        'country': 'str',
        'phone': 'str',
        'location_barcode_prefix': 'str',
        'lpn_prefix': 'str',
        'time_zone': 'str',
        'pack_station_allow_packing_before_pick_work_is_complete': 'bool',
        'pack_station_skip_carton_lpn': 'bool',
        'pack_station_require_confirm_on_error': 'bool',
        'pack_station_allow_scanning_sku_to_identify_orders': 'bool',
        'pack_station_allow_entry_of_item_quantities': 'bool',
        'pack_station_allow_add_all_items': 'bool',
        'ship_station_weight_check_packed_orders': 'bool',
        'ship_station_show_user_weight_check_exceptions': 'bool',
        'ship_station_auto_print_pre_generated_labels': 'bool',
        'ship_station_allow_scanning_sku_to_identify_orders': 'bool',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'client': 'client',
        'name': 'name',
        'address': 'address',
        'company': 'company',
        'street1': 'street1',
        'street2': 'street2',
        'street3': 'street3',
        'city': 'city',
        'state': 'state',
        'zip': 'zip',
        'country': 'country',
        'phone': 'phone',
        'location_barcode_prefix': 'locationBarcodePrefix',
        'lpn_prefix': 'lpnPrefix',
        'time_zone': 'timeZone',
        'pack_station_allow_packing_before_pick_work_is_complete': 'packStationAllowPackingBeforePickWorkIsComplete',
        'pack_station_skip_carton_lpn': 'packStationSkipCartonLPN',
        'pack_station_require_confirm_on_error': 'packStationRequireConfirmOnError',
        'pack_station_allow_scanning_sku_to_identify_orders': 'packStationAllowScanningSKUToIdentifyOrders',
        'pack_station_allow_entry_of_item_quantities': 'packStationAllowEntryOfItemQuantities',
        'pack_station_allow_add_all_items': 'packStationAllowAddAllItems',
        'ship_station_weight_check_packed_orders': 'shipStationWeightCheckPackedOrders',
        'ship_station_show_user_weight_check_exceptions': 'shipStationShowUserWeightCheckExceptions',
        'ship_station_auto_print_pre_generated_labels': 'shipStationAutoPrintPreGeneratedLabels',
        'ship_station_allow_scanning_sku_to_identify_orders': 'shipStationAllowScanningSKUToIdentifyOrders',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, client=None, name=None, address=None, company=None, street1=None, street2=None, street3=None, city=None, state=None, zip=None, country=None, phone=None, location_barcode_prefix=None, lpn_prefix=None, time_zone=None, pack_station_allow_packing_before_pick_work_is_complete=False, pack_station_skip_carton_lpn=False, pack_station_require_confirm_on_error=False, pack_station_allow_scanning_sku_to_identify_orders=False, pack_station_allow_entry_of_item_quantities=False, pack_station_allow_add_all_items=False, ship_station_weight_check_packed_orders=False, ship_station_show_user_weight_check_exceptions=False, ship_station_auto_print_pre_generated_labels=False, ship_station_allow_scanning_sku_to_identify_orders=False, create_date=None, modify_date=None, custom_fields=None):  # noqa: E501
        """Warehouse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._client = None
        self._name = None
        self._address = None
        self._company = None
        self._street1 = None
        self._street2 = None
        self._street3 = None
        self._city = None
        self._state = None
        self._zip = None
        self._country = None
        self._phone = None
        self._location_barcode_prefix = None
        self._lpn_prefix = None
        self._time_zone = None
        self._pack_station_allow_packing_before_pick_work_is_complete = None
        self._pack_station_skip_carton_lpn = None
        self._pack_station_require_confirm_on_error = None
        self._pack_station_allow_scanning_sku_to_identify_orders = None
        self._pack_station_allow_entry_of_item_quantities = None
        self._pack_station_allow_add_all_items = None
        self._ship_station_weight_check_packed_orders = None
        self._ship_station_show_user_weight_check_exceptions = None
        self._ship_station_auto_print_pre_generated_labels = None
        self._ship_station_allow_scanning_sku_to_identify_orders = None
        self._create_date = None
        self._modify_date = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.client = client
        self.name = name
        if address is not None:
            self.address = address
        self.company = company
        self.street1 = street1
        if street2 is not None:
            self.street2 = street2
        if street3 is not None:
            self.street3 = street3
        self.city = city
        if state is not None:
            self.state = state
        self.zip = zip
        self.country = country
        self.phone = phone
        if location_barcode_prefix is not None:
            self.location_barcode_prefix = location_barcode_prefix
        if lpn_prefix is not None:
            self.lpn_prefix = lpn_prefix
        if time_zone is not None:
            self.time_zone = time_zone
        self.pack_station_allow_packing_before_pick_work_is_complete = pack_station_allow_packing_before_pick_work_is_complete
        self.pack_station_skip_carton_lpn = pack_station_skip_carton_lpn
        self.pack_station_require_confirm_on_error = pack_station_require_confirm_on_error
        self.pack_station_allow_scanning_sku_to_identify_orders = pack_station_allow_scanning_sku_to_identify_orders
        self.pack_station_allow_entry_of_item_quantities = pack_station_allow_entry_of_item_quantities
        if pack_station_allow_add_all_items is not None:
            self.pack_station_allow_add_all_items = pack_station_allow_add_all_items
        self.ship_station_weight_check_packed_orders = ship_station_weight_check_packed_orders
        self.ship_station_show_user_weight_check_exceptions = ship_station_show_user_weight_check_exceptions
        self.ship_station_auto_print_pre_generated_labels = ship_station_auto_print_pre_generated_labels
        self.ship_station_allow_scanning_sku_to_identify_orders = ship_station_allow_scanning_sku_to_identify_orders
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this Warehouse.  # noqa: E501


        :return: The id of this Warehouse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Warehouse.


        :param id: The id of this Warehouse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def client(self):
        """Gets the client of this Warehouse.  # noqa: E501


        :return: The client of this Warehouse.  # noqa: E501
        :rtype: int
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this Warehouse.


        :param client: The client of this Warehouse.  # noqa: E501
        :type: int
        """
        if client is None:
            raise ValueError("Invalid value for `client`, must not be `None`")  # noqa: E501

        self._client = client

    @property
    def name(self):
        """Gets the name of this Warehouse.  # noqa: E501


        :return: The name of this Warehouse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Warehouse.


        :param name: The name of this Warehouse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def address(self):
        """Gets the address of this Warehouse.  # noqa: E501


        :return: The address of this Warehouse.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Warehouse.


        :param address: The address of this Warehouse.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def company(self):
        """Gets the company of this Warehouse.  # noqa: E501


        :return: The company of this Warehouse.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Warehouse.


        :param company: The company of this Warehouse.  # noqa: E501
        :type: str
        """
        if company is None:
            raise ValueError("Invalid value for `company`, must not be `None`")  # noqa: E501

        self._company = company

    @property
    def street1(self):
        """Gets the street1 of this Warehouse.  # noqa: E501


        :return: The street1 of this Warehouse.  # noqa: E501
        :rtype: str
        """
        return self._street1

    @street1.setter
    def street1(self, street1):
        """Sets the street1 of this Warehouse.


        :param street1: The street1 of this Warehouse.  # noqa: E501
        :type: str
        """
        if street1 is None:
            raise ValueError("Invalid value for `street1`, must not be `None`")  # noqa: E501

        self._street1 = street1

    @property
    def street2(self):
        """Gets the street2 of this Warehouse.  # noqa: E501


        :return: The street2 of this Warehouse.  # noqa: E501
        :rtype: str
        """
        return self._street2

    @street2.setter
    def street2(self, street2):
        """Sets the street2 of this Warehouse.


        :param street2: The street2 of this Warehouse.  # noqa: E501
        :type: str
        """

        self._street2 = street2

    @property
    def street3(self):
        """Gets the street3 of this Warehouse.  # noqa: E501


        :return: The street3 of this Warehouse.  # noqa: E501
        :rtype: str
        """
        return self._street3

    @street3.setter
    def street3(self, street3):
        """Sets the street3 of this Warehouse.


        :param street3: The street3 of this Warehouse.  # noqa: E501
        :type: str
        """

        self._street3 = street3

    @property
    def city(self):
        """Gets the city of this Warehouse.  # noqa: E501


        :return: The city of this Warehouse.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Warehouse.


        :param city: The city of this Warehouse.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def state(self):
        """Gets the state of this Warehouse.  # noqa: E501


        :return: The state of this Warehouse.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Warehouse.


        :param state: The state of this Warehouse.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this Warehouse.  # noqa: E501


        :return: The zip of this Warehouse.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this Warehouse.


        :param zip: The zip of this Warehouse.  # noqa: E501
        :type: str
        """
        if zip is None:
            raise ValueError("Invalid value for `zip`, must not be `None`")  # noqa: E501

        self._zip = zip

    @property
    def country(self):
        """Gets the country of this Warehouse.  # noqa: E501


        :return: The country of this Warehouse.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Warehouse.


        :param country: The country of this Warehouse.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def phone(self):
        """Gets the phone of this Warehouse.  # noqa: E501


        :return: The phone of this Warehouse.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Warehouse.


        :param phone: The phone of this Warehouse.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

    @property
    def location_barcode_prefix(self):
        """Gets the location_barcode_prefix of this Warehouse.  # noqa: E501


        :return: The location_barcode_prefix of this Warehouse.  # noqa: E501
        :rtype: str
        """
        return self._location_barcode_prefix

    @location_barcode_prefix.setter
    def location_barcode_prefix(self, location_barcode_prefix):
        """Sets the location_barcode_prefix of this Warehouse.


        :param location_barcode_prefix: The location_barcode_prefix of this Warehouse.  # noqa: E501
        :type: str
        """

        self._location_barcode_prefix = location_barcode_prefix

    @property
    def lpn_prefix(self):
        """Gets the lpn_prefix of this Warehouse.  # noqa: E501


        :return: The lpn_prefix of this Warehouse.  # noqa: E501
        :rtype: str
        """
        return self._lpn_prefix

    @lpn_prefix.setter
    def lpn_prefix(self, lpn_prefix):
        """Sets the lpn_prefix of this Warehouse.


        :param lpn_prefix: The lpn_prefix of this Warehouse.  # noqa: E501
        :type: str
        """

        self._lpn_prefix = lpn_prefix

    @property
    def time_zone(self):
        """Gets the time_zone of this Warehouse.  # noqa: E501


        :return: The time_zone of this Warehouse.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this Warehouse.


        :param time_zone: The time_zone of this Warehouse.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def pack_station_allow_packing_before_pick_work_is_complete(self):
        """Gets the pack_station_allow_packing_before_pick_work_is_complete of this Warehouse.  # noqa: E501


        :return: The pack_station_allow_packing_before_pick_work_is_complete of this Warehouse.  # noqa: E501
        :rtype: bool
        """
        return self._pack_station_allow_packing_before_pick_work_is_complete

    @pack_station_allow_packing_before_pick_work_is_complete.setter
    def pack_station_allow_packing_before_pick_work_is_complete(self, pack_station_allow_packing_before_pick_work_is_complete):
        """Sets the pack_station_allow_packing_before_pick_work_is_complete of this Warehouse.


        :param pack_station_allow_packing_before_pick_work_is_complete: The pack_station_allow_packing_before_pick_work_is_complete of this Warehouse.  # noqa: E501
        :type: bool
        """
        if pack_station_allow_packing_before_pick_work_is_complete is None:
            raise ValueError("Invalid value for `pack_station_allow_packing_before_pick_work_is_complete`, must not be `None`")  # noqa: E501

        self._pack_station_allow_packing_before_pick_work_is_complete = pack_station_allow_packing_before_pick_work_is_complete

    @property
    def pack_station_skip_carton_lpn(self):
        """Gets the pack_station_skip_carton_lpn of this Warehouse.  # noqa: E501


        :return: The pack_station_skip_carton_lpn of this Warehouse.  # noqa: E501
        :rtype: bool
        """
        return self._pack_station_skip_carton_lpn

    @pack_station_skip_carton_lpn.setter
    def pack_station_skip_carton_lpn(self, pack_station_skip_carton_lpn):
        """Sets the pack_station_skip_carton_lpn of this Warehouse.


        :param pack_station_skip_carton_lpn: The pack_station_skip_carton_lpn of this Warehouse.  # noqa: E501
        :type: bool
        """
        if pack_station_skip_carton_lpn is None:
            raise ValueError("Invalid value for `pack_station_skip_carton_lpn`, must not be `None`")  # noqa: E501

        self._pack_station_skip_carton_lpn = pack_station_skip_carton_lpn

    @property
    def pack_station_require_confirm_on_error(self):
        """Gets the pack_station_require_confirm_on_error of this Warehouse.  # noqa: E501


        :return: The pack_station_require_confirm_on_error of this Warehouse.  # noqa: E501
        :rtype: bool
        """
        return self._pack_station_require_confirm_on_error

    @pack_station_require_confirm_on_error.setter
    def pack_station_require_confirm_on_error(self, pack_station_require_confirm_on_error):
        """Sets the pack_station_require_confirm_on_error of this Warehouse.


        :param pack_station_require_confirm_on_error: The pack_station_require_confirm_on_error of this Warehouse.  # noqa: E501
        :type: bool
        """
        if pack_station_require_confirm_on_error is None:
            raise ValueError("Invalid value for `pack_station_require_confirm_on_error`, must not be `None`")  # noqa: E501

        self._pack_station_require_confirm_on_error = pack_station_require_confirm_on_error

    @property
    def pack_station_allow_scanning_sku_to_identify_orders(self):
        """Gets the pack_station_allow_scanning_sku_to_identify_orders of this Warehouse.  # noqa: E501


        :return: The pack_station_allow_scanning_sku_to_identify_orders of this Warehouse.  # noqa: E501
        :rtype: bool
        """
        return self._pack_station_allow_scanning_sku_to_identify_orders

    @pack_station_allow_scanning_sku_to_identify_orders.setter
    def pack_station_allow_scanning_sku_to_identify_orders(self, pack_station_allow_scanning_sku_to_identify_orders):
        """Sets the pack_station_allow_scanning_sku_to_identify_orders of this Warehouse.


        :param pack_station_allow_scanning_sku_to_identify_orders: The pack_station_allow_scanning_sku_to_identify_orders of this Warehouse.  # noqa: E501
        :type: bool
        """
        if pack_station_allow_scanning_sku_to_identify_orders is None:
            raise ValueError("Invalid value for `pack_station_allow_scanning_sku_to_identify_orders`, must not be `None`")  # noqa: E501

        self._pack_station_allow_scanning_sku_to_identify_orders = pack_station_allow_scanning_sku_to_identify_orders

    @property
    def pack_station_allow_entry_of_item_quantities(self):
        """Gets the pack_station_allow_entry_of_item_quantities of this Warehouse.  # noqa: E501


        :return: The pack_station_allow_entry_of_item_quantities of this Warehouse.  # noqa: E501
        :rtype: bool
        """
        return self._pack_station_allow_entry_of_item_quantities

    @pack_station_allow_entry_of_item_quantities.setter
    def pack_station_allow_entry_of_item_quantities(self, pack_station_allow_entry_of_item_quantities):
        """Sets the pack_station_allow_entry_of_item_quantities of this Warehouse.


        :param pack_station_allow_entry_of_item_quantities: The pack_station_allow_entry_of_item_quantities of this Warehouse.  # noqa: E501
        :type: bool
        """
        if pack_station_allow_entry_of_item_quantities is None:
            raise ValueError("Invalid value for `pack_station_allow_entry_of_item_quantities`, must not be `None`")  # noqa: E501

        self._pack_station_allow_entry_of_item_quantities = pack_station_allow_entry_of_item_quantities

    @property
    def pack_station_allow_add_all_items(self):
        """Gets the pack_station_allow_add_all_items of this Warehouse.  # noqa: E501


        :return: The pack_station_allow_add_all_items of this Warehouse.  # noqa: E501
        :rtype: bool
        """
        return self._pack_station_allow_add_all_items

    @pack_station_allow_add_all_items.setter
    def pack_station_allow_add_all_items(self, pack_station_allow_add_all_items):
        """Sets the pack_station_allow_add_all_items of this Warehouse.


        :param pack_station_allow_add_all_items: The pack_station_allow_add_all_items of this Warehouse.  # noqa: E501
        :type: bool
        """

        self._pack_station_allow_add_all_items = pack_station_allow_add_all_items

    @property
    def ship_station_weight_check_packed_orders(self):
        """Gets the ship_station_weight_check_packed_orders of this Warehouse.  # noqa: E501


        :return: The ship_station_weight_check_packed_orders of this Warehouse.  # noqa: E501
        :rtype: bool
        """
        return self._ship_station_weight_check_packed_orders

    @ship_station_weight_check_packed_orders.setter
    def ship_station_weight_check_packed_orders(self, ship_station_weight_check_packed_orders):
        """Sets the ship_station_weight_check_packed_orders of this Warehouse.


        :param ship_station_weight_check_packed_orders: The ship_station_weight_check_packed_orders of this Warehouse.  # noqa: E501
        :type: bool
        """
        if ship_station_weight_check_packed_orders is None:
            raise ValueError("Invalid value for `ship_station_weight_check_packed_orders`, must not be `None`")  # noqa: E501

        self._ship_station_weight_check_packed_orders = ship_station_weight_check_packed_orders

    @property
    def ship_station_show_user_weight_check_exceptions(self):
        """Gets the ship_station_show_user_weight_check_exceptions of this Warehouse.  # noqa: E501


        :return: The ship_station_show_user_weight_check_exceptions of this Warehouse.  # noqa: E501
        :rtype: bool
        """
        return self._ship_station_show_user_weight_check_exceptions

    @ship_station_show_user_weight_check_exceptions.setter
    def ship_station_show_user_weight_check_exceptions(self, ship_station_show_user_weight_check_exceptions):
        """Sets the ship_station_show_user_weight_check_exceptions of this Warehouse.


        :param ship_station_show_user_weight_check_exceptions: The ship_station_show_user_weight_check_exceptions of this Warehouse.  # noqa: E501
        :type: bool
        """
        if ship_station_show_user_weight_check_exceptions is None:
            raise ValueError("Invalid value for `ship_station_show_user_weight_check_exceptions`, must not be `None`")  # noqa: E501

        self._ship_station_show_user_weight_check_exceptions = ship_station_show_user_weight_check_exceptions

    @property
    def ship_station_auto_print_pre_generated_labels(self):
        """Gets the ship_station_auto_print_pre_generated_labels of this Warehouse.  # noqa: E501


        :return: The ship_station_auto_print_pre_generated_labels of this Warehouse.  # noqa: E501
        :rtype: bool
        """
        return self._ship_station_auto_print_pre_generated_labels

    @ship_station_auto_print_pre_generated_labels.setter
    def ship_station_auto_print_pre_generated_labels(self, ship_station_auto_print_pre_generated_labels):
        """Sets the ship_station_auto_print_pre_generated_labels of this Warehouse.


        :param ship_station_auto_print_pre_generated_labels: The ship_station_auto_print_pre_generated_labels of this Warehouse.  # noqa: E501
        :type: bool
        """
        if ship_station_auto_print_pre_generated_labels is None:
            raise ValueError("Invalid value for `ship_station_auto_print_pre_generated_labels`, must not be `None`")  # noqa: E501

        self._ship_station_auto_print_pre_generated_labels = ship_station_auto_print_pre_generated_labels

    @property
    def ship_station_allow_scanning_sku_to_identify_orders(self):
        """Gets the ship_station_allow_scanning_sku_to_identify_orders of this Warehouse.  # noqa: E501


        :return: The ship_station_allow_scanning_sku_to_identify_orders of this Warehouse.  # noqa: E501
        :rtype: bool
        """
        return self._ship_station_allow_scanning_sku_to_identify_orders

    @ship_station_allow_scanning_sku_to_identify_orders.setter
    def ship_station_allow_scanning_sku_to_identify_orders(self, ship_station_allow_scanning_sku_to_identify_orders):
        """Sets the ship_station_allow_scanning_sku_to_identify_orders of this Warehouse.


        :param ship_station_allow_scanning_sku_to_identify_orders: The ship_station_allow_scanning_sku_to_identify_orders of this Warehouse.  # noqa: E501
        :type: bool
        """
        if ship_station_allow_scanning_sku_to_identify_orders is None:
            raise ValueError("Invalid value for `ship_station_allow_scanning_sku_to_identify_orders`, must not be `None`")  # noqa: E501

        self._ship_station_allow_scanning_sku_to_identify_orders = ship_station_allow_scanning_sku_to_identify_orders

    @property
    def create_date(self):
        """Gets the create_date of this Warehouse.  # noqa: E501


        :return: The create_date of this Warehouse.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this Warehouse.


        :param create_date: The create_date of this Warehouse.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this Warehouse.  # noqa: E501


        :return: The modify_date of this Warehouse.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this Warehouse.


        :param modify_date: The modify_date of this Warehouse.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Warehouse.  # noqa: E501


        :return: The custom_fields of this Warehouse.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Warehouse.


        :param custom_fields: The custom_fields of this Warehouse.  # noqa: E501
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
        if not isinstance(other, Warehouse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
