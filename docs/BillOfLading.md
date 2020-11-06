# BillOfLading

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**modify_date** | **datetime** |  | [optional] 
**lob_id** | **int** |  | 
**order_no** | **float** |  | [optional] 
**bol_no** | **str** |  | 
**bol_date** | **datetime** |  | [optional] 
**ship_from_name** | **str** |  | [optional] 
**ship_from_attention** | **str** |  | [optional] 
**ship_from_address** | **str** |  | [optional] 
**ship_from_city** | **str** |  | [optional] 
**ship_from_state** | **str** |  | [optional] 
**ship_from_zip** | **str** |  | [optional] 
**ship_from_country** | **str** |  | [optional] 
**sid** | **str** |  | [optional] 
**is_ship_from_fob** | **bool** |  | [optional] [default to False]
**ship_to_name** | **str** |  | [optional] 
**ship_to_attention** | **str** |  | [optional] 
**ship_to_address** | **str** |  | [optional] 
**ship_to_city** | **str** |  | [optional] 
**ship_to_state** | **str** |  | [optional] 
**ship_to_zip** | **str** |  | [optional] 
**ship_to_country** | **str** |  | [optional] 
**ship_to_location_no** | **str** |  | [optional] 
**cid** | **str** |  | [optional] 
**is_ship_to_fob** | **bool** |  | [optional] [default to False]
**bill_to_name** | **str** |  | [optional] 
**bill_to_attention** | **str** |  | [optional] 
**bill_to_address** | **str** |  | [optional] 
**bill_to_city** | **str** |  | [optional] 
**bill_to_state** | **str** |  | [optional] 
**bill_to_zip** | **str** |  | [optional] 
**bill_to_country** | **str** |  | [optional] 
**is_trailer_loaded_by_shipper** | **bool** |  | [optional] [default to False]
**by_driver** | **bool** |  | [optional] [default to False]
**cod_amount** | **float** |  | [optional] 
**fee_terms_collect** | **bool** |  | [optional] [default to False]
**fee_terms_prepaid** | **bool** |  | [optional] [default to False]
**customer_check_acceptable** | **bool** |  | [optional] [default to False]
**carrier_name** | **str** |  | [optional] 
**trailer_no** | **str** |  | [optional] 
**seal_no** | **str** |  | [optional] 
**scac** | **str** |  | [optional] 
**pro_no** | **str** |  | [optional] 
**prepaid** | **bool** |  | [optional] [default to False]
**collect** | **bool** |  | [optional] [default to False]
**third_party** | **bool** |  | [optional] [default to False]
**is_this_a_master_bol** | **bool** |  | [optional] [default to False]
**master_bol_id** | **int** |  | [optional] 
**is_freight_counted_by_shipper** | **bool** |  | [optional] [default to False]
**by_driver_pallets** | **bool** |  | [optional] [default to False]
**by_driver_pieces** | **bool** |  | [optional] [default to False]
**special_instructions** | **str** |  | [optional] 
**order_info_lines** | [**list[BillOfLadingOrderInfoLine]**](BillOfLadingOrderInfoLine.md) |  | [optional] 
**carrier_info_lines** | [**list[BillOfLadingCarrierInfoLine]**](BillOfLadingCarrierInfoLine.md) |  | [optional] 
**custom_fields** | **dict(str, object)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

