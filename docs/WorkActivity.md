# WorkActivity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**imported_record_id** | **int** |  | [optional] 
**lob_id** | **int** |  | 
**create_date** | **datetime** |  | [optional] 
**modify_date** | **datetime** |  | [optional] 
**user_id** | **int** |  | 
**email** | **str** |  | 
**type** | **str** |  | 
**type_name** | **str** |  | 
**status** | **str** |  | 
**status_name** | **str** |  | 
**work_batch_id** | **int** |  | [optional] 
**work_parent_id** | **int** |  | [optional] 
**priority_code** | **int** |  | 
**foreign_id** | **int** |  | [optional] 
**source_warehouse_id** | **int** |  | 
**source_warehouse_name** | **str** |  | 
**source_location** | **str** |  | 
**source_building_id** | **int** |  | 
**source_building_name** | **str** |  | 
**source_zone_id** | **int** |  | [optional] 
**source_zone_name** | **str** |  | 
**source_aisle_id** | **int** |  | [optional] 
**source_aisle_address** | **str** |  | 
**source_origin** | **int** |  | [optional] 
**source_origin_name** | **str** |  | 
**source_billing_type_id** | **int** |  | 
**source_billing_type_name** | **str** |  | 
**source_behavior_type** | **str** |  | 
**source_behavior_type_name** | **str** |  | 
**source_footprint_id** | **int** |  | 
**source_footprint_name** | **str** |  | 
**source_footprint_height** | **int** |  | [optional] 
**source_footprint_width** | **int** |  | [optional] 
**source_footprint_depth** | **int** |  | [optional] 
**source_address_scheme_id** | **int** |  | [optional] 
**source_address_scheme_name** | **str** |  | 
**source_level** | **int** |  | [optional] 
**source_bay** | **int** |  | [optional] 
**source_number** | **int** |  | [optional] 
**source_online** | **bool** |  | [default to False]
**source_priority_code** | **int** |  | [optional] 
**source_cost** | **int** |  | [optional] 
**source_allow_item_mixing** | **bool** |  | [default to False]
**destination_warehouse_id** | **int** |  | 
**destination_warehouse_name** | **str** |  | 
**destination_location** | **str** |  | 
**destination_building_id** | **int** |  | 
**destination_building_name** | **str** |  | 
**destination_zone_id** | **int** |  | [optional] 
**destination_zone_name** | **str** |  | 
**destination_aisle_id** | **int** |  | [optional] 
**destination_aisle_address** | **str** |  | 
**destination_origin** | **int** |  | [optional] 
**destination_origin_name** | **str** |  | 
**destination_billing_type_id** | **int** |  | 
**destination_billing_type_name** | **str** |  | 
**destination_behavior_type** | **str** |  | 
**destination_behavior_type_name** | **str** |  | 
**destination_footprint_id** | **int** |  | 
**destination_footprint_name** | **str** |  | 
**destination_footprint_height** | **int** |  | [optional] 
**destination_footprint_width** | **int** |  | [optional] 
**destination_footprint_depth** | **int** |  | [optional] 
**destination_address_scheme_id** | **int** |  | [optional] 
**destination_address_scheme_name** | **str** |  | 
**destination_level** | **int** |  | [optional] 
**destination_bay** | **int** |  | [optional] 
**destination_number** | **int** |  | [optional] 
**destination_online** | **bool** |  | [default to False]
**destination_priority_code** | **int** |  | [optional] 
**destination_cost** | **int** |  | [optional] 
**destination_allow_item_mixing** | **bool** |  | [default to False]
**work_create_date** | **datetime** |  | [optional] 
**work_modify_date** | **datetime** |  | [optional] 
**master_ref** | **int** |  | [optional] 
**weight_per_wrap** | **float** |  | [optional] 
**sku** | **str** |  | 
**numeric_sort_order** | **int** |  | [optional] 
**item_description** | **str** |  | 
**additional_description** | **str** |  | [optional] 
**unit_code** | **str** |  | 
**wrap_code** | **str** |  | 
**units_per_wrap** | **int** |  | 
**quantity** | **int** |  | [optional] 
**number_of_wraps** | **int** |  | [optional] 
**number_of_cases** | **int** |  | [optional] 
**pick_touches** | **int** |  | [optional] 
**class_restriction** | **str** |  | 
**max_cycle** | **int** |  | 
**max_interim** | **int** |  | 
**seasonal_item** | **str** |  | 
**secure** | **str** |  | 
**product_type** | **int** |  | [optional] 
**item_status** | **str** |  | 
**overall_lead_time** | **int** |  | [optional] 
**overall_fixed_reorder_point** | **int** |  | [optional] 
**quality_control_indicator** | **str** |  | 
**lot_control_flag** | **str** |  | [optional] 
**product_code_flag** | **str** |  | 
**charge_code** | **str** |  | 
**pod_rev_date** | **str** |  | [optional] 
**pod_order_suffix** | **int** |  | [optional] 
**serial_code** | **str** |  | 
**asset_code** | **str** |  | [optional] 
**backorder** | **str** |  | 
**absolute_max** | **str** |  | [optional] 
**account_code_id** | **int** |  | [optional] 
**summary_code_id** | **int** |  | [optional] 
**low_stock_contact_id** | **int** |  | [optional] 
**legacy_low_level_contact_id** | **int** |  | [optional] 
**low_stock_code_id** | **int** |  | [optional] 
**major_group_id** | **int** |  | 
**sub_group_id** | **int** |  | 
**product_code_id** | **int** |  | [optional] 
**buyer_id** | **int** |  | [optional] 
**vendor_sku** | **str** |  | [optional] 
**upc** | **str** |  | [optional] 
**packing_slip_description** | **str** |  | [optional] 
**commodity_code_id** | **int** |  | [optional] 
**comp_code** | **int** |  | [optional] 
**critical_amount** | **int** |  | 
**list_price** | **float** |  | [optional] 
**outside_vendor** | **int** |  | [optional] 
**pick_no** | **str** |  | [optional] 
**requires_production_lot** | **str** |  | [optional] 
**sector** | **str** |  | [optional] 
**void_date** | **datetime** |  | [optional] 
**extrinsic_text1** | **str** |  | [optional] 
**extrinsic_text2** | **str** |  | [optional] 
**extrinsic_text3** | **str** |  | [optional] 
**extrinsic_number1** | **int** |  | [optional] 
**extrinsic_number2** | **int** |  | [optional] 
**extrinsic_decimal1** | **float** |  | [optional] 
**extrinsic_decimal2** | **float** |  | [optional] 
**casebreak_enabled** | **str** |  | [optional] 
**alcohol_type_id** | **int** |  | [optional] 
**alcohol_type_name** | **str** |  | [optional] 
**alcohol_content** | **float** |  | [optional] 
**alcohol_container_id** | **int** |  | [optional] 
**alcohol_container_name** | **str** |  | [optional] 
**alcohol_container_volume** | **int** |  | [optional] 
**alcohol_vintage_year** | **str** |  | [optional] 
**alcohol_country_id** | **int** |  | [optional] 
**alcohol_country_name** | **str** |  | [optional] 
**alcohol_state** | **str** |  | [optional] 
**alcohol_region** | **str** |  | [optional] 
**alcohol_brand** | **str** |  | [optional] 
**alcohol_upc_code** | **str** |  | [optional] 
**alcohol_nabca_code** | **str** |  | [optional] 
**alcohol_unimerc_code** | **str** |  | [optional] 
**alcohol_scc_code** | **str** |  | [optional] 
**billing_quantity** | **float** |  | [optional] 
**charge_rate** | **float** |  | [optional] 
**extended_charge** | **float** |  | [optional] 
**custom_fields** | **dict(str, object)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


