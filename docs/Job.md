# Job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**modify_date** | **datetime** |  | [optional] 
**source_job_recipe_id** | **int** |  | [optional] 
**assembly_quantity** | **int** |  | 
**warehouse_id** | **int** |  | 
**lob_id** | **int** |  | 
**status** | **str** |  | [optional] 
**order_no_id** | **float** |  | [optional] 
**po_no_id** | **int** |  | [optional] 
**work_batch_id** | **int** |  | [optional] 
**layout** | **str** |  | 
**track_assemblies** | **bool** |  | [default to False]
**track_steps** | **bool** |  | [default to False]
**job_no** | **str** |  | [optional] 
**assembly_instructions** | **str** |  | [optional] 
**inputs** | [**list[JobInput]**](JobInput.md) |  | [optional] 
**outputs** | [**list[JobOutput]**](JobOutput.md) |  | [optional] 
**steps** | [**list[JobStep]**](JobStep.md) |  | [optional] 
**fulfillment_plan_id** | **int** |  | 
**total_picks** | **int** |  | [optional] 
**completed_picks** | **int** |  | [optional] 
**total_assemblies** | **int** |  | [optional] 
**completed_assemblies** | **int** |  | [optional] 
**total_steps** | **int** |  | [optional] 
**completed_steps** | **int** |  | [optional] 
**total_receipts** | **int** |  | [optional] 
**completed_receipts** | **int** |  | [optional] 
**total_to_do** | **int** |  | [optional] 
**completed_to_do** | **int** |  | [optional] 
**custom_fields** | **dict(str, object)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


