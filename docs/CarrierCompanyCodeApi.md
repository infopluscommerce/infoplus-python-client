# Infoplus.CarrierCompanyCodeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_carrier_company_code_by_id**](CarrierCompanyCodeApi.md#get_carrier_company_code_by_id) | **GET** /beta/carrierCompanyCode/{carrierCompanyCodeId} | Get a carrierCompanyCode by id
[**get_carrier_company_code_by_search_text**](CarrierCompanyCodeApi.md#get_carrier_company_code_by_search_text) | **GET** /beta/carrierCompanyCode/search | Search carrierCompanyCodes


# **get_carrier_company_code_by_id**
> CarrierCompanyCode get_carrier_company_code_by_id(carrier_company_code_id)

Get a carrierCompanyCode by id

Returns the carrierCompanyCode identified by the specified id.

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
api_instance = Infoplus.CarrierCompanyCodeApi(Infoplus.ApiClient(configuration))
carrier_company_code_id = 'carrier_company_code_id_example' # str | Id of carrierCompanyCode to be returned.

try:
    # Get a carrierCompanyCode by id
    api_response = api_instance.get_carrier_company_code_by_id(carrier_company_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarrierCompanyCodeApi->get_carrier_company_code_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier_company_code_id** | **str**| Id of carrierCompanyCode to be returned. | 

### Return type

[**CarrierCompanyCode**](CarrierCompanyCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carrier_company_code_by_search_text**
> list[CarrierCompanyCode] get_carrier_company_code_by_search_text(search_text=search_text, page=page, limit=limit)

Search carrierCompanyCodes

Returns the list of carrierCompanyCodes that match the given searchText.

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
api_instance = Infoplus.CarrierCompanyCodeApi(Infoplus.ApiClient(configuration))
search_text = 'search_text_example' # str | Search text, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)

try:
    # Search carrierCompanyCodes
    api_response = api_instance.get_carrier_company_code_by_search_text(search_text=search_text, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarrierCompanyCodeApi->get_carrier_company_code_by_search_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | **str**| Search text, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 

### Return type

[**list[CarrierCompanyCode]**](CarrierCompanyCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

