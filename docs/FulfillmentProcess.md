# FulfillmentProcess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**modify_date** | **datetime** |  | [optional] 
**process_no** | **int** |  | [optional] 
**work_batch_id** | **int** |  | [optional] 
**warehouse_id** | **int** |  | 
**fulfillment_plan_id** | **int** |  | 
**pick_scan_scheme_id** | **int** |  | 
**status** | **str** |  | 
**order_smart_filter_id** | **int** |  | [optional] 
**location_smart_filter_id** | **int** |  | [optional] 
**max_orders** | **int** |  | [optional] 
**batch_max_size** | **int** |  | [optional] 
**batch_min_size** | **int** |  | [optional] 
**max_sk_us** | **int** |  | [optional] 
**max_cartons** | **int** |  | [optional] 
**version** | **str** |  | [optional] 
**fulfillment_process_group** | **int** |  | [optional] 
**is_mass_distribution** | **bool** |  | [optional] [default to False]
**priority_code** | **int** |  | [optional] 
**number_of_orders** | **int** |  | [optional] 
**number_of_lines** | **int** |  | [optional] 
**number_of_sk_us** | **int** |  | [optional] 
**completed_picks** | **int** |  | [optional] 
**total_picks** | **int** |  | [optional] 
**shipped_casebreaks** | **int** |  | [optional] 
**total_casebreaks_to_ship** | **int** |  | [optional] 
**shipped_orders** | **int** |  | [optional] 
**total_orders_to_ship** | **int** |  | [optional] 
**completed_to_do** | **int** |  | [optional] 
**total_to_do** | **int** |  | [optional] 
**create_pick_work** | **bool** |  | [optional] [default to False]
**picking_rule** | **str** |  | [optional] 
**layout_rule** | **str** |  | [optional] 
**pick_sort_rule** | **str** |  | [optional] 
**location_sort** | **str** |  | [optional] 
**first_pick_position** | **int** |  | [optional] 
**pick_list_format** | **str** |  | [optional] 
**pick_list_layout** | **str** |  | [optional] 
**pick_list_group** | **str** |  | [optional] 
**pick_list_sort** | **str** |  | [optional] 
**pick_list_location_sort** | **str** |  | [optional] 
**pick_summary_format** | **str** |  | [optional] 
**pick_summary_layout** | **str** |  | [optional] 
**pick_summary_sort** | **str** |  | [optional] 
**create_pick_summary** | **bool** |  | [optional] [default to False]
**create_pick_list** | **bool** |  | [optional] [default to False]
**pre_generate_parcel_labels** | **bool** |  | [optional] [default to False]
**label_sort** | **str** |  | [optional] 
**ship_date** | **datetime** |  | [optional] 
**auto_ship_casebreak_cartons** | **bool** |  | [optional] [default to False]
**auto_ship_orders** | **bool** |  | [optional] [default to False]
**cartonize_orders** | **bool** |  | [optional] [default to False]
**cartonization_script_id** | **int** |  | [optional] 
**create_packing_slip** | **str** |  | 
**override_packing_slip_template_id** | **int** |  | [optional] 
**create_order_assembly_guide** | **bool** |  | [optional] [default to False]
**create_order_invoice** | **str** |  | 
**override_order_invoice_template_id** | **int** |  | [optional] 
**send_to_external_shipping_system** | **bool** |  | [default to False]
**external_shipping_system_id** | **int** |  | [optional] 
**custom_fields** | **dict(str, object)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


