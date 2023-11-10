# Infoplus.PackingSlipTemplateLineExtraDataEnumApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_packing_slip_template_line_extra_data_enum_by_id**](PackingSlipTemplateLineExtraDataEnumApi.md#get_packing_slip_template_line_extra_data_enum_by_id) | **GET** /beta/packingSlipTemplateLineExtraDataEnum/{packingSlipTemplateLineExtraDataEnumId} | Get a packingSlipTemplateLineExtraDataEnum by id
[**get_packing_slip_template_line_extra_data_enum_by_search_text**](PackingSlipTemplateLineExtraDataEnumApi.md#get_packing_slip_template_line_extra_data_enum_by_search_text) | **GET** /beta/packingSlipTemplateLineExtraDataEnum/search | Search packingSlipTemplateLineExtraDataEnums


# **get_packing_slip_template_line_extra_data_enum_by_id**
> PackingSlipTemplateLineExtraDataEnum get_packing_slip_template_line_extra_data_enum_by_id(packing_slip_template_line_extra_data_enum_id)

Get a packingSlipTemplateLineExtraDataEnum by id

Returns the packingSlipTemplateLineExtraDataEnum identified by the specified id.

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
api_instance = Infoplus.PackingSlipTemplateLineExtraDataEnumApi(Infoplus.ApiClient(configuration))
packing_slip_template_line_extra_data_enum_id = 'packing_slip_template_line_extra_data_enum_id_example' # str | Id of packingSlipTemplateLineExtraDataEnum to be returned.

try:
    # Get a packingSlipTemplateLineExtraDataEnum by id
    api_response = api_instance.get_packing_slip_template_line_extra_data_enum_by_id(packing_slip_template_line_extra_data_enum_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackingSlipTemplateLineExtraDataEnumApi->get_packing_slip_template_line_extra_data_enum_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_slip_template_line_extra_data_enum_id** | **str**| Id of packingSlipTemplateLineExtraDataEnum to be returned. | 

### Return type

[**PackingSlipTemplateLineExtraDataEnum**](PackingSlipTemplateLineExtraDataEnum.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packing_slip_template_line_extra_data_enum_by_search_text**
> list[PackingSlipTemplateLineExtraDataEnum] get_packing_slip_template_line_extra_data_enum_by_search_text(search_text=search_text, page=page, limit=limit)

Search packingSlipTemplateLineExtraDataEnums

Returns the list of packingSlipTemplateLineExtraDataEnums that match the given searchText.

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
api_instance = Infoplus.PackingSlipTemplateLineExtraDataEnumApi(Infoplus.ApiClient(configuration))
search_text = 'search_text_example' # str | Search text, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)

try:
    # Search packingSlipTemplateLineExtraDataEnums
    api_response = api_instance.get_packing_slip_template_line_extra_data_enum_by_search_text(search_text=search_text, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackingSlipTemplateLineExtraDataEnumApi->get_packing_slip_template_line_extra_data_enum_by_search_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | **str**| Search text, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 

### Return type

[**list[PackingSlipTemplateLineExtraDataEnum]**](PackingSlipTemplateLineExtraDataEnum.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

