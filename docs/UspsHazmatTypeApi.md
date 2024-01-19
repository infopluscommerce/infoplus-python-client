# Infoplus.UspsHazmatTypeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usps_hazmat_type_by_id**](UspsHazmatTypeApi.md#get_usps_hazmat_type_by_id) | **GET** /beta/uspsHazmatType/{uspsHazmatTypeId} | Get an uspsHazmatType by id
[**get_usps_hazmat_type_by_search_text**](UspsHazmatTypeApi.md#get_usps_hazmat_type_by_search_text) | **GET** /beta/uspsHazmatType/search | Search uspsHazmatTypes


# **get_usps_hazmat_type_by_id**
> UspsHazmatType get_usps_hazmat_type_by_id(usps_hazmat_type_id)

Get an uspsHazmatType by id

Returns the uspsHazmatType identified by the specified id.

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
api_instance = Infoplus.UspsHazmatTypeApi(Infoplus.ApiClient(configuration))
usps_hazmat_type_id = 'usps_hazmat_type_id_example' # str | Id of uspsHazmatType to be returned.

try:
    # Get an uspsHazmatType by id
    api_response = api_instance.get_usps_hazmat_type_by_id(usps_hazmat_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UspsHazmatTypeApi->get_usps_hazmat_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usps_hazmat_type_id** | **str**| Id of uspsHazmatType to be returned. | 

### Return type

[**UspsHazmatType**](UspsHazmatType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usps_hazmat_type_by_search_text**
> list[UspsHazmatType] get_usps_hazmat_type_by_search_text(search_text=search_text, page=page, limit=limit)

Search uspsHazmatTypes

Returns the list of uspsHazmatTypes that match the given searchText.

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
api_instance = Infoplus.UspsHazmatTypeApi(Infoplus.ApiClient(configuration))
search_text = 'search_text_example' # str | Search text, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)

try:
    # Search uspsHazmatTypes
    api_response = api_instance.get_usps_hazmat_type_by_search_text(search_text=search_text, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UspsHazmatTypeApi->get_usps_hazmat_type_by_search_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | **str**| Search text, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 

### Return type

[**list[UspsHazmatType]**](UspsHazmatType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

