# CustomerInvoiceTemplateLine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**modify_date** | **datetime** |  | [optional] 
**lob_id** | **int** |  | 
**description** | **str** |  | [optional] 
**seq_no** | **int** |  | [optional] 
**account_code** | **str** |  | [optional] 
**active** | **bool** |  | [default to False]
**include_if_zero** | **bool** |  | [default to False]
**department** | **str** |  | [optional] 
**item_code** | **str** |  | [optional] 
**invoice_template_id** | **int** |  | [optional] 
**billing_rule_id** | **int** |  | 
**price_level_mode** | **str** |  | 
**script_id** | **int** |  | [optional] 
**price_level_list** | [**list[InvoiceTemplateLinePriceLevel]**](InvoiceTemplateLinePriceLevel.md) |  | [optional] 
**custom_fields** | **dict(str, object)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


