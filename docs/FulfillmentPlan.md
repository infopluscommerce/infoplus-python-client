# FulfillmentPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**modify_date** | **datetime** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**warehouse_id** | **int** |  | 
**priority_code** | **int** |  | [optional] 
**last_run_time** | **datetime** |  | [optional] 
**order_smart_filter_id** | **int** |  | 
**location_smart_filter_id** | **int** |  | [optional] 
**max_orders** | **int** |  | [optional] 
**batch_size_max** | **int** |  | [optional] 
**batch_size_min** | **int** |  | [optional] 
**max_cartons** | **int** |  | [optional] 
**version** | **str** |  | [optional] 
**is_mass_distribution** | **bool** |  | [optional] [default to False]
**create_pick_work** | **bool** |  | [default to False]
**picking_rule** | **str** |  | [optional] 
**pick_batch_group_id** | **str** |  | [optional] 
**max_sk_us_per_batch** | **int** |  | [optional] 
**layout_rule** | **str** |  | [optional] 
**pick_sort_rule** | **str** |  | [optional] 
**location_sort** | **str** |  | [optional] 
**create_pick_list** | **bool** |  | [optional] [default to False]
**pick_list_format** | **str** |  | [optional] 
**pick_list_layout** | **str** |  | [optional] 
**pick_list_group** | **str** |  | [optional] 
**pick_list_sort** | **str** |  | [optional] 
**pick_list_location_sort** | **str** |  | [optional] 
**create_pick_summary** | **bool** |  | [optional] [default to False]
**pick_summary_format** | **str** |  | [optional] 
**pick_summary_layout** | **str** |  | [optional] 
**pick_summary_sort** | **str** |  | [optional] 
**pick_scan_scheme_id** | **int** |  | 
**cartonize_orders** | **bool** |  | [default to False]
**cartonization_script_id** | **int** |  | [optional] 
**auto_ship_casebreak_cartons** | **bool** |  | [optional] [default to False]
**auto_ship_orders** | **bool** |  | [optional] [default to False]
**pre_generate_parcel_labels** | **bool** |  | [optional] [default to False]
**label_sort** | **str** |  | [optional] 
**create_packing_slip** | **str** |  | 
**override_packing_slip_template_id** | **int** |  | [optional] 
**create_order_assembly_guide** | **bool** |  | [optional] [default to False]
**create_order_invoice** | **str** |  | 
**override_order_invoice_template_id** | **int** |  | [optional] 
**send_to_external_shipping_system** | **bool** |  | [default to False]
**external_shipping_system_id** | **int** |  | [optional] 
**custom_fields** | **dict(str, object)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


