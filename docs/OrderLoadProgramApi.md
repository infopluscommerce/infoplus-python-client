# Infoplus.OrderLoadProgramApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_order_load_program_by_search_text**](OrderLoadProgramApi.md#get_order_load_program_by_search_text) | **GET** /v3.0/orderLoadProgram/search | Search orderLoadPrograms
[**get_req_load_program_by_id**](OrderLoadProgramApi.md#get_req_load_program_by_id) | **GET** /v3.0/orderLoadProgram/{orderLoadProgramId} | Get an orderLoadProgram by id


# **get_order_load_program_by_search_text**
> list[OrderLoadProgram] get_order_load_program_by_search_text(search_text=search_text, page=page, limit=limit)

Search orderLoadPrograms

Returns the list of orderLoadPrograms that match the given searchText.

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
api_instance = Infoplus.OrderLoadProgramApi(Infoplus.ApiClient(configuration))
search_text = 'search_text_example' # str | Search text, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)

try:
    # Search orderLoadPrograms
    api_response = api_instance.get_order_load_program_by_search_text(search_text=search_text, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderLoadProgramApi->get_order_load_program_by_search_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | **str**| Search text, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 

### Return type

[**list[OrderLoadProgram]**](OrderLoadProgram.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_req_load_program_by_id**
> OrderLoadProgram get_req_load_program_by_id(order_load_program_id)

Get an orderLoadProgram by id

Returns the orderLoadProgram identified by the specified id.

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
api_instance = Infoplus.OrderLoadProgramApi(Infoplus.ApiClient(configuration))
order_load_program_id = 'order_load_program_id_example' # str | Id of orderLoadProgram to be returned.

try:
    # Get an orderLoadProgram by id
    api_response = api_instance.get_req_load_program_by_id(order_load_program_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderLoadProgramApi->get_req_load_program_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_load_program_id** | **str**| Id of orderLoadProgram to be returned. | 

### Return type

[**OrderLoadProgram**](OrderLoadProgram.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

