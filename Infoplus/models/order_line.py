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

from Infoplus.models.dynamic_kit_component_line import DynamicKitComponentLine  # noqa: F401,E501
from Infoplus.models.override_receipts_for_fulfillment import OverrideReceiptsForFulfillment  # noqa: F401,E501


class OrderLine(object):
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
        'line_item_id': 'int',
        'customer_line_item_no': 'str',
        'order_no': 'float',
        'lob_id': 'int',
        'sku': 'str',
        'po_no_id': 'int',
        'ordered_qty': 'int',
        'allowed_qty': 'int',
        'shipped_qty': 'int',
        'backorder_qty': 'int',
        'number_of_wraps': 'int',
        'number_of_cases': 'int',
        'number_of_inner_packs': 'int',
        'rev_date': 'str',
        'charge_code': 'str',
        'distribution_code': 'str',
        'upc': 'str',
        'vendor_sku': 'str',
        'order_source_sku': 'str',
        'unit_cost': 'float',
        'unit_sell': 'float',
        'unit_discount': 'float',
        'unit_declared_value_override': 'float',
        'extended_cost': 'float',
        'extended_sell': 'float',
        'extended_discount': 'float',
        'nc_extended_sell': 'float',
        'extended_declared_value_override': 'float',
        'item_weight': 'float',
        'production_lot': 'str',
        'product_id_tag': 'str',
        'expiration_date': 'datetime',
        'weight_per_wrap': 'float',
        'sector': 'str',
        'order_assembly_instructions': 'str',
        'item_account_code_id': 'int',
        'item_legacy_low_stock_contact_id': 'int',
        'item_major_group_id': 'int',
        'item_sub_group_id': 'int',
        'item_product_code_id': 'int',
        'item_summary_code_id': 'int',
        'fulfillment_channel': 'str',
        'dynamic_kit_component_list': 'list[DynamicKitComponentLine]',
        'override_receipts_for_fulfillment_list': 'list[OverrideReceiptsForFulfillment]',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'line_item_id': 'lineItemId',
        'customer_line_item_no': 'customerLineItemNo',
        'order_no': 'orderNo',
        'lob_id': 'lobId',
        'sku': 'sku',
        'po_no_id': 'poNoId',
        'ordered_qty': 'orderedQty',
        'allowed_qty': 'allowedQty',
        'shipped_qty': 'shippedQty',
        'backorder_qty': 'backorderQty',
        'number_of_wraps': 'numberOfWraps',
        'number_of_cases': 'numberOfCases',
        'number_of_inner_packs': 'numberOfInnerPacks',
        'rev_date': 'revDate',
        'charge_code': 'chargeCode',
        'distribution_code': 'distributionCode',
        'upc': 'upc',
        'vendor_sku': 'vendorSKU',
        'order_source_sku': 'orderSourceSKU',
        'unit_cost': 'unitCost',
        'unit_sell': 'unitSell',
        'unit_discount': 'unitDiscount',
        'unit_declared_value_override': 'unitDeclaredValueOverride',
        'extended_cost': 'extendedCost',
        'extended_sell': 'extendedSell',
        'extended_discount': 'extendedDiscount',
        'nc_extended_sell': 'ncExtendedSell',
        'extended_declared_value_override': 'extendedDeclaredValueOverride',
        'item_weight': 'itemWeight',
        'production_lot': 'productionLot',
        'product_id_tag': 'productIdTag',
        'expiration_date': 'expirationDate',
        'weight_per_wrap': 'weightPerWrap',
        'sector': 'sector',
        'order_assembly_instructions': 'orderAssemblyInstructions',
        'item_account_code_id': 'itemAccountCodeId',
        'item_legacy_low_stock_contact_id': 'itemLegacyLowStockContactId',
        'item_major_group_id': 'itemMajorGroupId',
        'item_sub_group_id': 'itemSubGroupId',
        'item_product_code_id': 'itemProductCodeId',
        'item_summary_code_id': 'itemSummaryCodeId',
        'fulfillment_channel': 'fulfillmentChannel',
        'dynamic_kit_component_list': 'dynamicKitComponentList',
        'override_receipts_for_fulfillment_list': 'overrideReceiptsForFulfillmentList',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, line_item_id=None, customer_line_item_no=None, order_no=None, lob_id=None, sku=None, po_no_id=None, ordered_qty=None, allowed_qty=None, shipped_qty=None, backorder_qty=None, number_of_wraps=None, number_of_cases=None, number_of_inner_packs=None, rev_date=None, charge_code=None, distribution_code=None, upc=None, vendor_sku=None, order_source_sku=None, unit_cost=None, unit_sell=None, unit_discount=None, unit_declared_value_override=None, extended_cost=None, extended_sell=None, extended_discount=None, nc_extended_sell=None, extended_declared_value_override=None, item_weight=None, production_lot=None, product_id_tag=None, expiration_date=None, weight_per_wrap=None, sector=None, order_assembly_instructions=None, item_account_code_id=None, item_legacy_low_stock_contact_id=None, item_major_group_id=None, item_sub_group_id=None, item_product_code_id=None, item_summary_code_id=None, fulfillment_channel=None, dynamic_kit_component_list=None, override_receipts_for_fulfillment_list=None, custom_fields=None):  # noqa: E501
        """OrderLine - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._line_item_id = None
        self._customer_line_item_no = None
        self._order_no = None
        self._lob_id = None
        self._sku = None
        self._po_no_id = None
        self._ordered_qty = None
        self._allowed_qty = None
        self._shipped_qty = None
        self._backorder_qty = None
        self._number_of_wraps = None
        self._number_of_cases = None
        self._number_of_inner_packs = None
        self._rev_date = None
        self._charge_code = None
        self._distribution_code = None
        self._upc = None
        self._vendor_sku = None
        self._order_source_sku = None
        self._unit_cost = None
        self._unit_sell = None
        self._unit_discount = None
        self._unit_declared_value_override = None
        self._extended_cost = None
        self._extended_sell = None
        self._extended_discount = None
        self._nc_extended_sell = None
        self._extended_declared_value_override = None
        self._item_weight = None
        self._production_lot = None
        self._product_id_tag = None
        self._expiration_date = None
        self._weight_per_wrap = None
        self._sector = None
        self._order_assembly_instructions = None
        self._item_account_code_id = None
        self._item_legacy_low_stock_contact_id = None
        self._item_major_group_id = None
        self._item_sub_group_id = None
        self._item_product_code_id = None
        self._item_summary_code_id = None
        self._fulfillment_channel = None
        self._dynamic_kit_component_list = None
        self._override_receipts_for_fulfillment_list = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if line_item_id is not None:
            self.line_item_id = line_item_id
        if customer_line_item_no is not None:
            self.customer_line_item_no = customer_line_item_no
        if order_no is not None:
            self.order_no = order_no
        self.lob_id = lob_id
        self.sku = sku
        if po_no_id is not None:
            self.po_no_id = po_no_id
        self.ordered_qty = ordered_qty
        if allowed_qty is not None:
            self.allowed_qty = allowed_qty
        if shipped_qty is not None:
            self.shipped_qty = shipped_qty
        if backorder_qty is not None:
            self.backorder_qty = backorder_qty
        if number_of_wraps is not None:
            self.number_of_wraps = number_of_wraps
        if number_of_cases is not None:
            self.number_of_cases = number_of_cases
        if number_of_inner_packs is not None:
            self.number_of_inner_packs = number_of_inner_packs
        if rev_date is not None:
            self.rev_date = rev_date
        if charge_code is not None:
            self.charge_code = charge_code
        if distribution_code is not None:
            self.distribution_code = distribution_code
        if upc is not None:
            self.upc = upc
        if vendor_sku is not None:
            self.vendor_sku = vendor_sku
        if order_source_sku is not None:
            self.order_source_sku = order_source_sku
        if unit_cost is not None:
            self.unit_cost = unit_cost
        if unit_sell is not None:
            self.unit_sell = unit_sell
        if unit_discount is not None:
            self.unit_discount = unit_discount
        if unit_declared_value_override is not None:
            self.unit_declared_value_override = unit_declared_value_override
        if extended_cost is not None:
            self.extended_cost = extended_cost
        if extended_sell is not None:
            self.extended_sell = extended_sell
        if extended_discount is not None:
            self.extended_discount = extended_discount
        if nc_extended_sell is not None:
            self.nc_extended_sell = nc_extended_sell
        if extended_declared_value_override is not None:
            self.extended_declared_value_override = extended_declared_value_override
        if item_weight is not None:
            self.item_weight = item_weight
        if production_lot is not None:
            self.production_lot = production_lot
        if product_id_tag is not None:
            self.product_id_tag = product_id_tag
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if weight_per_wrap is not None:
            self.weight_per_wrap = weight_per_wrap
        if sector is not None:
            self.sector = sector
        if order_assembly_instructions is not None:
            self.order_assembly_instructions = order_assembly_instructions
        if item_account_code_id is not None:
            self.item_account_code_id = item_account_code_id
        if item_legacy_low_stock_contact_id is not None:
            self.item_legacy_low_stock_contact_id = item_legacy_low_stock_contact_id
        if item_major_group_id is not None:
            self.item_major_group_id = item_major_group_id
        if item_sub_group_id is not None:
            self.item_sub_group_id = item_sub_group_id
        if item_product_code_id is not None:
            self.item_product_code_id = item_product_code_id
        if item_summary_code_id is not None:
            self.item_summary_code_id = item_summary_code_id
        if fulfillment_channel is not None:
            self.fulfillment_channel = fulfillment_channel
        if dynamic_kit_component_list is not None:
            self.dynamic_kit_component_list = dynamic_kit_component_list
        if override_receipts_for_fulfillment_list is not None:
            self.override_receipts_for_fulfillment_list = override_receipts_for_fulfillment_list
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this OrderLine.  # noqa: E501


        :return: The id of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderLine.


        :param id: The id of this OrderLine.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def line_item_id(self):
        """Gets the line_item_id of this OrderLine.  # noqa: E501


        :return: The line_item_id of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._line_item_id

    @line_item_id.setter
    def line_item_id(self, line_item_id):
        """Sets the line_item_id of this OrderLine.


        :param line_item_id: The line_item_id of this OrderLine.  # noqa: E501
        :type: int
        """

        self._line_item_id = line_item_id

    @property
    def customer_line_item_no(self):
        """Gets the customer_line_item_no of this OrderLine.  # noqa: E501


        :return: The customer_line_item_no of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._customer_line_item_no

    @customer_line_item_no.setter
    def customer_line_item_no(self, customer_line_item_no):
        """Sets the customer_line_item_no of this OrderLine.


        :param customer_line_item_no: The customer_line_item_no of this OrderLine.  # noqa: E501
        :type: str
        """

        self._customer_line_item_no = customer_line_item_no

    @property
    def order_no(self):
        """Gets the order_no of this OrderLine.  # noqa: E501


        :return: The order_no of this OrderLine.  # noqa: E501
        :rtype: float
        """
        return self._order_no

    @order_no.setter
    def order_no(self, order_no):
        """Sets the order_no of this OrderLine.


        :param order_no: The order_no of this OrderLine.  # noqa: E501
        :type: float
        """

        self._order_no = order_no

    @property
    def lob_id(self):
        """Gets the lob_id of this OrderLine.  # noqa: E501


        :return: The lob_id of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this OrderLine.


        :param lob_id: The lob_id of this OrderLine.  # noqa: E501
        :type: int
        """
        if lob_id is None:
            raise ValueError("Invalid value for `lob_id`, must not be `None`")  # noqa: E501

        self._lob_id = lob_id

    @property
    def sku(self):
        """Gets the sku of this OrderLine.  # noqa: E501


        :return: The sku of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this OrderLine.


        :param sku: The sku of this OrderLine.  # noqa: E501
        :type: str
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")  # noqa: E501

        self._sku = sku

    @property
    def po_no_id(self):
        """Gets the po_no_id of this OrderLine.  # noqa: E501


        :return: The po_no_id of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._po_no_id

    @po_no_id.setter
    def po_no_id(self, po_no_id):
        """Sets the po_no_id of this OrderLine.


        :param po_no_id: The po_no_id of this OrderLine.  # noqa: E501
        :type: int
        """

        self._po_no_id = po_no_id

    @property
    def ordered_qty(self):
        """Gets the ordered_qty of this OrderLine.  # noqa: E501


        :return: The ordered_qty of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._ordered_qty

    @ordered_qty.setter
    def ordered_qty(self, ordered_qty):
        """Sets the ordered_qty of this OrderLine.


        :param ordered_qty: The ordered_qty of this OrderLine.  # noqa: E501
        :type: int
        """
        if ordered_qty is None:
            raise ValueError("Invalid value for `ordered_qty`, must not be `None`")  # noqa: E501

        self._ordered_qty = ordered_qty

    @property
    def allowed_qty(self):
        """Gets the allowed_qty of this OrderLine.  # noqa: E501


        :return: The allowed_qty of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._allowed_qty

    @allowed_qty.setter
    def allowed_qty(self, allowed_qty):
        """Sets the allowed_qty of this OrderLine.


        :param allowed_qty: The allowed_qty of this OrderLine.  # noqa: E501
        :type: int
        """

        self._allowed_qty = allowed_qty

    @property
    def shipped_qty(self):
        """Gets the shipped_qty of this OrderLine.  # noqa: E501


        :return: The shipped_qty of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._shipped_qty

    @shipped_qty.setter
    def shipped_qty(self, shipped_qty):
        """Sets the shipped_qty of this OrderLine.


        :param shipped_qty: The shipped_qty of this OrderLine.  # noqa: E501
        :type: int
        """

        self._shipped_qty = shipped_qty

    @property
    def backorder_qty(self):
        """Gets the backorder_qty of this OrderLine.  # noqa: E501


        :return: The backorder_qty of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._backorder_qty

    @backorder_qty.setter
    def backorder_qty(self, backorder_qty):
        """Sets the backorder_qty of this OrderLine.


        :param backorder_qty: The backorder_qty of this OrderLine.  # noqa: E501
        :type: int
        """

        self._backorder_qty = backorder_qty

    @property
    def number_of_wraps(self):
        """Gets the number_of_wraps of this OrderLine.  # noqa: E501


        :return: The number_of_wraps of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._number_of_wraps

    @number_of_wraps.setter
    def number_of_wraps(self, number_of_wraps):
        """Sets the number_of_wraps of this OrderLine.


        :param number_of_wraps: The number_of_wraps of this OrderLine.  # noqa: E501
        :type: int
        """

        self._number_of_wraps = number_of_wraps

    @property
    def number_of_cases(self):
        """Gets the number_of_cases of this OrderLine.  # noqa: E501


        :return: The number_of_cases of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._number_of_cases

    @number_of_cases.setter
    def number_of_cases(self, number_of_cases):
        """Sets the number_of_cases of this OrderLine.


        :param number_of_cases: The number_of_cases of this OrderLine.  # noqa: E501
        :type: int
        """

        self._number_of_cases = number_of_cases

    @property
    def number_of_inner_packs(self):
        """Gets the number_of_inner_packs of this OrderLine.  # noqa: E501


        :return: The number_of_inner_packs of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._number_of_inner_packs

    @number_of_inner_packs.setter
    def number_of_inner_packs(self, number_of_inner_packs):
        """Sets the number_of_inner_packs of this OrderLine.


        :param number_of_inner_packs: The number_of_inner_packs of this OrderLine.  # noqa: E501
        :type: int
        """

        self._number_of_inner_packs = number_of_inner_packs

    @property
    def rev_date(self):
        """Gets the rev_date of this OrderLine.  # noqa: E501


        :return: The rev_date of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._rev_date

    @rev_date.setter
    def rev_date(self, rev_date):
        """Sets the rev_date of this OrderLine.


        :param rev_date: The rev_date of this OrderLine.  # noqa: E501
        :type: str
        """

        self._rev_date = rev_date

    @property
    def charge_code(self):
        """Gets the charge_code of this OrderLine.  # noqa: E501


        :return: The charge_code of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._charge_code

    @charge_code.setter
    def charge_code(self, charge_code):
        """Sets the charge_code of this OrderLine.


        :param charge_code: The charge_code of this OrderLine.  # noqa: E501
        :type: str
        """

        self._charge_code = charge_code

    @property
    def distribution_code(self):
        """Gets the distribution_code of this OrderLine.  # noqa: E501


        :return: The distribution_code of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._distribution_code

    @distribution_code.setter
    def distribution_code(self, distribution_code):
        """Sets the distribution_code of this OrderLine.


        :param distribution_code: The distribution_code of this OrderLine.  # noqa: E501
        :type: str
        """

        self._distribution_code = distribution_code

    @property
    def upc(self):
        """Gets the upc of this OrderLine.  # noqa: E501


        :return: The upc of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._upc

    @upc.setter
    def upc(self, upc):
        """Sets the upc of this OrderLine.


        :param upc: The upc of this OrderLine.  # noqa: E501
        :type: str
        """

        self._upc = upc

    @property
    def vendor_sku(self):
        """Gets the vendor_sku of this OrderLine.  # noqa: E501


        :return: The vendor_sku of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._vendor_sku

    @vendor_sku.setter
    def vendor_sku(self, vendor_sku):
        """Sets the vendor_sku of this OrderLine.


        :param vendor_sku: The vendor_sku of this OrderLine.  # noqa: E501
        :type: str
        """

        self._vendor_sku = vendor_sku

    @property
    def order_source_sku(self):
        """Gets the order_source_sku of this OrderLine.  # noqa: E501


        :return: The order_source_sku of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._order_source_sku

    @order_source_sku.setter
    def order_source_sku(self, order_source_sku):
        """Sets the order_source_sku of this OrderLine.


        :param order_source_sku: The order_source_sku of this OrderLine.  # noqa: E501
        :type: str
        """

        self._order_source_sku = order_source_sku

    @property
    def unit_cost(self):
        """Gets the unit_cost of this OrderLine.  # noqa: E501


        :return: The unit_cost of this OrderLine.  # noqa: E501
        :rtype: float
        """
        return self._unit_cost

    @unit_cost.setter
    def unit_cost(self, unit_cost):
        """Sets the unit_cost of this OrderLine.


        :param unit_cost: The unit_cost of this OrderLine.  # noqa: E501
        :type: float
        """

        self._unit_cost = unit_cost

    @property
    def unit_sell(self):
        """Gets the unit_sell of this OrderLine.  # noqa: E501


        :return: The unit_sell of this OrderLine.  # noqa: E501
        :rtype: float
        """
        return self._unit_sell

    @unit_sell.setter
    def unit_sell(self, unit_sell):
        """Sets the unit_sell of this OrderLine.


        :param unit_sell: The unit_sell of this OrderLine.  # noqa: E501
        :type: float
        """

        self._unit_sell = unit_sell

    @property
    def unit_discount(self):
        """Gets the unit_discount of this OrderLine.  # noqa: E501


        :return: The unit_discount of this OrderLine.  # noqa: E501
        :rtype: float
        """
        return self._unit_discount

    @unit_discount.setter
    def unit_discount(self, unit_discount):
        """Sets the unit_discount of this OrderLine.


        :param unit_discount: The unit_discount of this OrderLine.  # noqa: E501
        :type: float
        """

        self._unit_discount = unit_discount

    @property
    def unit_declared_value_override(self):
        """Gets the unit_declared_value_override of this OrderLine.  # noqa: E501


        :return: The unit_declared_value_override of this OrderLine.  # noqa: E501
        :rtype: float
        """
        return self._unit_declared_value_override

    @unit_declared_value_override.setter
    def unit_declared_value_override(self, unit_declared_value_override):
        """Sets the unit_declared_value_override of this OrderLine.


        :param unit_declared_value_override: The unit_declared_value_override of this OrderLine.  # noqa: E501
        :type: float
        """

        self._unit_declared_value_override = unit_declared_value_override

    @property
    def extended_cost(self):
        """Gets the extended_cost of this OrderLine.  # noqa: E501


        :return: The extended_cost of this OrderLine.  # noqa: E501
        :rtype: float
        """
        return self._extended_cost

    @extended_cost.setter
    def extended_cost(self, extended_cost):
        """Sets the extended_cost of this OrderLine.


        :param extended_cost: The extended_cost of this OrderLine.  # noqa: E501
        :type: float
        """

        self._extended_cost = extended_cost

    @property
    def extended_sell(self):
        """Gets the extended_sell of this OrderLine.  # noqa: E501


        :return: The extended_sell of this OrderLine.  # noqa: E501
        :rtype: float
        """
        return self._extended_sell

    @extended_sell.setter
    def extended_sell(self, extended_sell):
        """Sets the extended_sell of this OrderLine.


        :param extended_sell: The extended_sell of this OrderLine.  # noqa: E501
        :type: float
        """

        self._extended_sell = extended_sell

    @property
    def extended_discount(self):
        """Gets the extended_discount of this OrderLine.  # noqa: E501


        :return: The extended_discount of this OrderLine.  # noqa: E501
        :rtype: float
        """
        return self._extended_discount

    @extended_discount.setter
    def extended_discount(self, extended_discount):
        """Sets the extended_discount of this OrderLine.


        :param extended_discount: The extended_discount of this OrderLine.  # noqa: E501
        :type: float
        """

        self._extended_discount = extended_discount

    @property
    def nc_extended_sell(self):
        """Gets the nc_extended_sell of this OrderLine.  # noqa: E501


        :return: The nc_extended_sell of this OrderLine.  # noqa: E501
        :rtype: float
        """
        return self._nc_extended_sell

    @nc_extended_sell.setter
    def nc_extended_sell(self, nc_extended_sell):
        """Sets the nc_extended_sell of this OrderLine.


        :param nc_extended_sell: The nc_extended_sell of this OrderLine.  # noqa: E501
        :type: float
        """

        self._nc_extended_sell = nc_extended_sell

    @property
    def extended_declared_value_override(self):
        """Gets the extended_declared_value_override of this OrderLine.  # noqa: E501


        :return: The extended_declared_value_override of this OrderLine.  # noqa: E501
        :rtype: float
        """
        return self._extended_declared_value_override

    @extended_declared_value_override.setter
    def extended_declared_value_override(self, extended_declared_value_override):
        """Sets the extended_declared_value_override of this OrderLine.


        :param extended_declared_value_override: The extended_declared_value_override of this OrderLine.  # noqa: E501
        :type: float
        """

        self._extended_declared_value_override = extended_declared_value_override

    @property
    def item_weight(self):
        """Gets the item_weight of this OrderLine.  # noqa: E501


        :return: The item_weight of this OrderLine.  # noqa: E501
        :rtype: float
        """
        return self._item_weight

    @item_weight.setter
    def item_weight(self, item_weight):
        """Sets the item_weight of this OrderLine.


        :param item_weight: The item_weight of this OrderLine.  # noqa: E501
        :type: float
        """

        self._item_weight = item_weight

    @property
    def production_lot(self):
        """Gets the production_lot of this OrderLine.  # noqa: E501


        :return: The production_lot of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._production_lot

    @production_lot.setter
    def production_lot(self, production_lot):
        """Sets the production_lot of this OrderLine.


        :param production_lot: The production_lot of this OrderLine.  # noqa: E501
        :type: str
        """

        self._production_lot = production_lot

    @property
    def product_id_tag(self):
        """Gets the product_id_tag of this OrderLine.  # noqa: E501


        :return: The product_id_tag of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._product_id_tag

    @product_id_tag.setter
    def product_id_tag(self, product_id_tag):
        """Sets the product_id_tag of this OrderLine.


        :param product_id_tag: The product_id_tag of this OrderLine.  # noqa: E501
        :type: str
        """

        self._product_id_tag = product_id_tag

    @property
    def expiration_date(self):
        """Gets the expiration_date of this OrderLine.  # noqa: E501


        :return: The expiration_date of this OrderLine.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this OrderLine.


        :param expiration_date: The expiration_date of this OrderLine.  # noqa: E501
        :type: datetime
        """

        self._expiration_date = expiration_date

    @property
    def weight_per_wrap(self):
        """Gets the weight_per_wrap of this OrderLine.  # noqa: E501


        :return: The weight_per_wrap of this OrderLine.  # noqa: E501
        :rtype: float
        """
        return self._weight_per_wrap

    @weight_per_wrap.setter
    def weight_per_wrap(self, weight_per_wrap):
        """Sets the weight_per_wrap of this OrderLine.


        :param weight_per_wrap: The weight_per_wrap of this OrderLine.  # noqa: E501
        :type: float
        """

        self._weight_per_wrap = weight_per_wrap

    @property
    def sector(self):
        """Gets the sector of this OrderLine.  # noqa: E501


        :return: The sector of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this OrderLine.


        :param sector: The sector of this OrderLine.  # noqa: E501
        :type: str
        """

        self._sector = sector

    @property
    def order_assembly_instructions(self):
        """Gets the order_assembly_instructions of this OrderLine.  # noqa: E501


        :return: The order_assembly_instructions of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._order_assembly_instructions

    @order_assembly_instructions.setter
    def order_assembly_instructions(self, order_assembly_instructions):
        """Sets the order_assembly_instructions of this OrderLine.


        :param order_assembly_instructions: The order_assembly_instructions of this OrderLine.  # noqa: E501
        :type: str
        """

        self._order_assembly_instructions = order_assembly_instructions

    @property
    def item_account_code_id(self):
        """Gets the item_account_code_id of this OrderLine.  # noqa: E501


        :return: The item_account_code_id of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._item_account_code_id

    @item_account_code_id.setter
    def item_account_code_id(self, item_account_code_id):
        """Sets the item_account_code_id of this OrderLine.


        :param item_account_code_id: The item_account_code_id of this OrderLine.  # noqa: E501
        :type: int
        """

        self._item_account_code_id = item_account_code_id

    @property
    def item_legacy_low_stock_contact_id(self):
        """Gets the item_legacy_low_stock_contact_id of this OrderLine.  # noqa: E501


        :return: The item_legacy_low_stock_contact_id of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._item_legacy_low_stock_contact_id

    @item_legacy_low_stock_contact_id.setter
    def item_legacy_low_stock_contact_id(self, item_legacy_low_stock_contact_id):
        """Sets the item_legacy_low_stock_contact_id of this OrderLine.


        :param item_legacy_low_stock_contact_id: The item_legacy_low_stock_contact_id of this OrderLine.  # noqa: E501
        :type: int
        """

        self._item_legacy_low_stock_contact_id = item_legacy_low_stock_contact_id

    @property
    def item_major_group_id(self):
        """Gets the item_major_group_id of this OrderLine.  # noqa: E501


        :return: The item_major_group_id of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._item_major_group_id

    @item_major_group_id.setter
    def item_major_group_id(self, item_major_group_id):
        """Sets the item_major_group_id of this OrderLine.


        :param item_major_group_id: The item_major_group_id of this OrderLine.  # noqa: E501
        :type: int
        """

        self._item_major_group_id = item_major_group_id

    @property
    def item_sub_group_id(self):
        """Gets the item_sub_group_id of this OrderLine.  # noqa: E501


        :return: The item_sub_group_id of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._item_sub_group_id

    @item_sub_group_id.setter
    def item_sub_group_id(self, item_sub_group_id):
        """Sets the item_sub_group_id of this OrderLine.


        :param item_sub_group_id: The item_sub_group_id of this OrderLine.  # noqa: E501
        :type: int
        """

        self._item_sub_group_id = item_sub_group_id

    @property
    def item_product_code_id(self):
        """Gets the item_product_code_id of this OrderLine.  # noqa: E501


        :return: The item_product_code_id of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._item_product_code_id

    @item_product_code_id.setter
    def item_product_code_id(self, item_product_code_id):
        """Sets the item_product_code_id of this OrderLine.


        :param item_product_code_id: The item_product_code_id of this OrderLine.  # noqa: E501
        :type: int
        """

        self._item_product_code_id = item_product_code_id

    @property
    def item_summary_code_id(self):
        """Gets the item_summary_code_id of this OrderLine.  # noqa: E501


        :return: The item_summary_code_id of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._item_summary_code_id

    @item_summary_code_id.setter
    def item_summary_code_id(self, item_summary_code_id):
        """Sets the item_summary_code_id of this OrderLine.


        :param item_summary_code_id: The item_summary_code_id of this OrderLine.  # noqa: E501
        :type: int
        """

        self._item_summary_code_id = item_summary_code_id

    @property
    def fulfillment_channel(self):
        """Gets the fulfillment_channel of this OrderLine.  # noqa: E501


        :return: The fulfillment_channel of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._fulfillment_channel

    @fulfillment_channel.setter
    def fulfillment_channel(self, fulfillment_channel):
        """Sets the fulfillment_channel of this OrderLine.


        :param fulfillment_channel: The fulfillment_channel of this OrderLine.  # noqa: E501
        :type: str
        """

        self._fulfillment_channel = fulfillment_channel

    @property
    def dynamic_kit_component_list(self):
        """Gets the dynamic_kit_component_list of this OrderLine.  # noqa: E501


        :return: The dynamic_kit_component_list of this OrderLine.  # noqa: E501
        :rtype: list[DynamicKitComponentLine]
        """
        return self._dynamic_kit_component_list

    @dynamic_kit_component_list.setter
    def dynamic_kit_component_list(self, dynamic_kit_component_list):
        """Sets the dynamic_kit_component_list of this OrderLine.


        :param dynamic_kit_component_list: The dynamic_kit_component_list of this OrderLine.  # noqa: E501
        :type: list[DynamicKitComponentLine]
        """

        self._dynamic_kit_component_list = dynamic_kit_component_list

    @property
    def override_receipts_for_fulfillment_list(self):
        """Gets the override_receipts_for_fulfillment_list of this OrderLine.  # noqa: E501


        :return: The override_receipts_for_fulfillment_list of this OrderLine.  # noqa: E501
        :rtype: list[OverrideReceiptsForFulfillment]
        """
        return self._override_receipts_for_fulfillment_list

    @override_receipts_for_fulfillment_list.setter
    def override_receipts_for_fulfillment_list(self, override_receipts_for_fulfillment_list):
        """Sets the override_receipts_for_fulfillment_list of this OrderLine.


        :param override_receipts_for_fulfillment_list: The override_receipts_for_fulfillment_list of this OrderLine.  # noqa: E501
        :type: list[OverrideReceiptsForFulfillment]
        """

        self._override_receipts_for_fulfillment_list = override_receipts_for_fulfillment_list

    @property
    def custom_fields(self):
        """Gets the custom_fields of this OrderLine.  # noqa: E501


        :return: The custom_fields of this OrderLine.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this OrderLine.


        :param custom_fields: The custom_fields of this OrderLine.  # noqa: E501
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
        if not isinstance(other, OrderLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
