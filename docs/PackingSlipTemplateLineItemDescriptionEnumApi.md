# Infoplus.PackingSlipTemplateLineItemDescriptionEnumApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_packing_slip_template_line_item_description_enum_by_id**](PackingSlipTemplateLineItemDescriptionEnumApi.md#get_packing_slip_template_line_item_description_enum_by_id) | **GET** /beta/packingSlipTemplateLineItemDescriptionEnum/{packingSlipTemplateLineItemDescriptionEnumId} | Get a packingSlipTemplateLineItemDescriptionEnum by id
[**get_packing_slip_template_line_item_description_enum_by_search_text**](PackingSlipTemplateLineItemDescriptionEnumApi.md#get_packing_slip_template_line_item_description_enum_by_search_text) | **GET** /beta/packingSlipTemplateLineItemDescriptionEnum/search | Search packingSlipTemplateLineItemDescriptionEnums


# **get_packing_slip_template_line_item_description_enum_by_id**
> PackingSlipTemplateLineItemDescriptionEnum get_packing_slip_template_line_item_description_enum_by_id(packing_slip_template_line_item_description_enum_id)

Get a packingSlipTemplateLineItemDescriptionEnum by id

Returns the packingSlipTemplateLineItemDescriptionEnum identified by the specified id.

### Example
```python
from __future__ import print_function
import time
import Infoplus
from Infoplus.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = Infoplus.Configuration()
configuration.api_key['API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = Infoplus.PackingSlipTemplateLineItemDescriptionEnumApi(Infoplus.ApiClient(configuration))
packing_slip_template_line_item_description_enum_id = 'packing_slip_template_line_item_description_enum_id_example' # str | Id of packingSlipTemplateLineItemDescriptionEnum to be returned.

try:
    # Get a packingSlipTemplateLineItemDescriptionEnum by id
    api_response = api_instance.get_packing_slip_template_line_item_description_enum_by_id(packing_slip_template_line_item_description_enum_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackingSlipTemplateLineItemDescriptionEnumApi->get_packing_slip_template_line_item_description_enum_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_slip_template_line_item_description_enum_id** | **str**| Id of packingSlipTemplateLineItemDescriptionEnum to be returned. | 

### Return type

[**PackingSlipTemplateLineItemDescriptionEnum**](PackingSlipTemplateLineItemDescriptionEnum.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packing_slip_template_line_item_description_enum_by_search_text**
> list[PackingSlipTemplateLineItemDescriptionEnum] get_packing_slip_template_line_item_description_enum_by_search_text(search_text=search_text, page=page, limit=limit)

Search packingSlipTemplateLineItemDescriptionEnums

Returns the list of packingSlipTemplateLineItemDescriptionEnums that match the given searchText.

### Example
```python
from __future__ import print_function
import time
import Infoplus
from Infoplus.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = Infoplus.Configuration()
configuration.api_key['API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = Infoplus.PackingSlipTemplateLineItemDescriptionEnumApi(Infoplus.ApiClient(configuration))
search_text = 'search_text_example' # str | Search text, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)

try:
    # Search packingSlipTemplateLineItemDescriptionEnums
    api_response = api_instance.get_packing_slip_template_line_item_description_enum_by_search_text(search_text=search_text, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackingSlipTemplateLineItemDescriptionEnumApi->get_packing_slip_template_line_item_description_enum_by_search_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | **str**| Search text, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 

### Return type

[**list[PackingSlipTemplateLineItemDescriptionEnum]**](PackingSlipTemplateLineItemDescriptionEnum.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

