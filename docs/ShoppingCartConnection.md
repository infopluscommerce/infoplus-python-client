# ShoppingCartConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**modify_date** | **datetime** |  | [optional] 
**client_id** | **int** |  | [optional] 
**nonce** | **str** |  | [optional] 
**lob_id** | **int** |  | 
**order_source_id** | **int** |  | 
**integration_partner_id** | **int** |  | 
**connection_type** | **str** |  | 
**item_filter_id** | **int** |  | [optional] 
**infoplus_sku_field_to_map** | **str** |  | 
**shopping_cart_sku_field_to_map** | **str** |  | 
**script_id** | **int** |  | [optional] 
**name** | **str** |  | 
**shopping_cart_store_url** | **str** |  | 
**access_code** | **str** |  | 
**access_token** | **str** |  | 
**username** | **str** |  | 
**password** | **str** |  | 
**default_carrier_id** | **int** |  | [optional] 
**order_shipment_level** | **str** |  | 
**create_invoices** | **bool** |  | [optional] [default to False]
**sync_orders** | **bool** |  | [default to False]
**sync_inventory** | **bool** |  | [default to False]
**sync_tracking_data** | **bool** |  | [default to False]
**fulfill_all_items** | **bool** |  | [default to False]
**sync_inventory_levels_last_run_time** | **datetime** |  | [optional] 
**sync_orders_last_run_time** | **datetime** |  | [optional] 
**inventory_level_warehouse_controls** | **str** |  | 
**warehouse_list** | [**list[Warehouse]**](Warehouse.md) |  | [optional] 
**inventory_level_store_controls** | **str** |  | 
**store_list** | [**list[Store]**](Store.md) |  | [optional] 
**custom_fields** | **dict(str, object)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


