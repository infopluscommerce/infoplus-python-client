# ReceivingWorksheet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**warehouse_id** | **int** |  | 
**po_no_id** | **int** |  | [optional] 
**lob_id** | **int** |  | [optional] 
**vendor_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**service_level** | **str** |  | 
**receiving_process_id** | **int** |  | [optional] 
**dock_date** | **datetime** |  | [optional] 
**created_by** | **int** |  | [optional] 
**worksheet_name** | **str** |  | 
**carrier** | **str** |  | [optional] 
**on_the_dock** | **bool** |  | [optional] [default to False]
**auto_commit** | **bool** |  | [default to False]
**line_items** | [**list[ReceivingWorksheetLineItem]**](ReceivingWorksheetLineItem.md) |  | [optional] 
**notes** | **str** |  | [optional] 
**work_batch_id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**modify_date** | **datetime** |  | [optional] 
**custom_fields** | **dict(str, object)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


