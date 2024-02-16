# JobRecipe

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**modify_date** | **datetime** |  | [optional] 
**warehouse_id** | **int** |  | [optional] 
**lob_id** | **int** |  | 
**name** | **str** |  | 
**assembly_instructions** | **str** |  | [optional] 
**inputs** | [**list[JobRecipeInput]**](JobRecipeInput.md) |  | [optional] 
**outputs** | [**list[JobRecipeOutput]**](JobRecipeOutput.md) |  | [optional] 
**steps** | [**list[JobRecipeStep]**](JobRecipeStep.md) |  | [optional] 
**fulfillment_plan_id** | **int** |  | 
**layout** | **str** |  | 
**track_assemblies** | **bool** |  | [default to False]
**track_steps** | **bool** |  | [default to False]
**custom_fields** | **dict(str, object)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


