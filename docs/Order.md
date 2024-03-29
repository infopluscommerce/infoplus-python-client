# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_no** | **float** |  | [optional] 
**customer_order_no** | **str** |  | [optional] 
**lob_id** | **int** |  | 
**warehouse_id** | **int** |  | 
**order_date** | **datetime** |  | [optional] 
**customer_no** | **str** |  | [optional] 
**use_order_no_root** | **int** |  | [optional] 
**shipping_method** | **str** |  | [optional] 
**first_ship_date** | **datetime** |  | [optional] 
**last_ship_date** | **datetime** |  | [optional] 
**deliver_on_date** | **datetime** |  | [optional] 
**need_by_date** | **datetime** |  | [optional] 
**carrier_id** | **int** |  | [optional] 
**ship_via** | **str** |  | [optional] 
**media_code** | **str** |  | [optional] 
**legacy_restriction_type** | **str** |  | [optional] 
**alcohol_order_type** | **str** |  | [optional] 
**alternate_usage** | **str** |  | [optional] 
**authorization_amount** | **float** |  | [optional] 
**authorized_by** | **str** |  | [optional] 
**balance_due** | **float** |  | [optional] 
**batch_no** | **str** |  | [optional] 
**bill_to_attention** | **str** |  | [optional] 
**bill_to_company** | **str** |  | [optional] 
**bill_to_street** | **str** |  | [optional] 
**bill_to_street2** | **str** |  | [optional] 
**bill_to_street3** | **str** |  | [optional] 
**bill_to_city** | **str** |  | [optional] 
**bill_to_state** | **str** |  | [optional] 
**bill_to_zip** | **str** |  | [optional] 
**bill_to_country** | **str** |  | [optional] 
**bill_to_phone** | **str** |  | [optional] 
**bill_to_email** | **str** |  | [optional] 
**number_of_cartons** | **int** |  | [optional] 
**number_of_pallets** | **int** |  | [optional] 
**completion_status** | **str** |  | [optional] 
**parcel_account_id** | **int** |  | [optional] 
**third_party_parcel_account_id** | **int** |  | [optional] 
**cost_center** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**customer_po_no** | **str** |  | [optional] 
**distribution_channel** | **str** |  | [optional] 
**distribution_charges** | **float** |  | [optional] 
**division** | **int** |  | [optional] 
**entered_by** | **str** |  | [optional] 
**pre_allocation_estimated_weight** | **float** |  | [optional] 
**estimated_weight_lbs** | **float** |  | [optional] 
**freight** | **float** |  | [optional] 
**fulfillability_details** | **str** |  | [optional] 
**gift_message_to** | **str** |  | [optional] 
**gift_message_from** | **str** |  | [optional] 
**gift_message** | **str** |  | [optional] 
**group_order_id** | **float** |  | [optional] 
**parent_kod_order_id** | **float** |  | [optional] 
**hold_code** | **str** |  | [optional] 
**integration_partner_id** | **int** |  | [optional] 
**number_of_line_items** | **int** |  | [optional] 
**estimated_number_of_picks** | **int** |  | [optional] 
**modify_date** | **datetime** |  | [optional] 
**oms_order_id** | **int** |  | [optional] 
**oms_order_no** | **int** |  | [optional] 
**oms_customer_id** | **int** |  | [optional] 
**order_load_program_id** | **int** |  | [optional] 
**order_message** | **str** |  | [optional] 
**order_reason** | **int** |  | [optional] 
**order_source_id** | **int** |  | [optional] 
**packing_slip_template_id** | **int** |  | [optional] 
**order_invoice_template_id** | **int** |  | [optional] 
**order_email_template_id** | **int** |  | [optional] 
**shipment_email_template_id** | **int** |  | [optional] 
**out_for_delivery_email_template_id** | **int** |  | [optional] 
**delivered_email_template_id** | **int** |  | [optional] 
**price_level** | **str** |  | [optional] 
**price_mode** | **str** |  | [optional] 
**priority_code** | **int** |  | [optional] 
**fulfillment_process_id** | **int** |  | [optional] 
**ship_by** | **datetime** |  | [optional] 
**ship_code** | **str** |  | [optional] 
**ship_date** | **datetime** |  | [optional] 
**shipped_date** | **datetime** |  | [optional] 
**ship_to_attention** | **str** |  | [optional] 
**ship_to_company** | **str** |  | [optional] 
**ship_to_street** | **str** |  | [optional] 
**ship_to_street2** | **str** |  | [optional] 
**ship_to_street3** | **str** |  | [optional] 
**ship_to_city** | **str** |  | [optional] 
**ship_to_state** | **str** |  | [optional] 
**ship_to_zip** | **str** |  | [optional] 
**ship_to_country** | **str** |  | [optional] 
**ship_to_phone** | **str** |  | [optional] 
**ship_to_email** | **str** |  | [optional] 
**shipping_charge** | **float** |  | [optional] 
**status** | **str** |  | [optional] 
**stop_back_orders** | **str** |  | [optional] 
**subtotal** | **float** |  | [optional] 
**tax** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_discount** | **float** |  | [optional] 
**total_paid** | **float** |  | [optional] 
**total_qty** | **int** |  | [optional] 
**weight_lbs** | **float** |  | [optional] 
**order_assembly_instructions** | **str** |  | [optional] 
**parcel_label_ref1** | **str** |  | [optional] 
**parcel_label_ref2** | **str** |  | [optional] 
**parcel_label_ref3** | **str** |  | [optional] 
**line_items** | [**list[OrderLine]**](OrderLine.md) |  | 
**requested_parcel_accessories** | [**list[ReqParcelAccessoryData]**](ReqParcelAccessoryData.md) |  | [optional] 
**extra_order_data** | [**list[OrderExtraOrderData]**](OrderExtraOrderData.md) |  | [optional] 
**extra_line_item_data** | [**list[OrderExtraLineItemData]**](OrderExtraLineItemData.md) |  | [optional] 
**external_shipping_system_id** | **int** |  | [optional] 
**service_type_id** | **str** |  | [optional] 
**warehouse_service_type_id** | **int** |  | [optional] 
**warehouse_service_level_id** | **int** |  | [optional] 
**sla_date** | **datetime** |  | [optional] 
**sla_status** | **str** |  | [optional] 
**production_type** | **str** |  | [optional] 
**back_order_status** | **str** |  | [optional] 
**back_order_release_date** | **datetime** |  | [optional] 
**estimated_number_of_cartons** | **int** |  | [optional] 
**estimated_cartonization_plan** | **str** |  | [optional] 
**manifest_script_id** | **int** |  | [optional] 
**store_no** | **str** |  | [optional] 
**store_name** | **str** |  | [optional] 
**department_no** | **str** |  | [optional] 
**department_name** | **str** |  | [optional] 
**vendor_no** | **str** |  | [optional] 
**internal_use91** | **str** |  | [optional] 
**delivery_days** | **int** |  | [optional] 
**delivery_date_guaranteed** | **bool** |  | [optional] [default to False]
**fulfillability** | **str** |  | [optional] 
**custom_fields** | **dict(str, object)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


