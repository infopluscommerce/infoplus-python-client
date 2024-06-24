# Infoplus.LoggedTimeTypeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_logged_time_type_by_id**](LoggedTimeTypeApi.md#get_logged_time_type_by_id) | **GET** /beta/loggedTimeType/{loggedTimeTypeId} | Get a loggedTimeType by id
[**get_logged_time_type_by_search_text**](LoggedTimeTypeApi.md#get_logged_time_type_by_search_text) | **GET** /beta/loggedTimeType/search | Search loggedTimeTypes


# **get_logged_time_type_by_id**
> LoggedTimeType get_logged_time_type_by_id(logged_time_type_id)

Get a loggedTimeType by id

Returns the loggedTimeType identified by the specified id.

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
api_instance = Infoplus.LoggedTimeTypeApi(Infoplus.ApiClient(configuration))
logged_time_type_id = 'logged_time_type_id_example' # str | Id of loggedTimeType to be returned.

try:
    # Get a loggedTimeType by id
    api_response = api_instance.get_logged_time_type_by_id(logged_time_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggedTimeTypeApi->get_logged_time_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logged_time_type_id** | **str**| Id of loggedTimeType to be returned. | 

### Return type

[**LoggedTimeType**](LoggedTimeType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logged_time_type_by_search_text**
> list[LoggedTimeType] get_logged_time_type_by_search_text(search_text=search_text, page=page, limit=limit)

Search loggedTimeTypes

Returns the list of loggedTimeTypes that match the given searchText.

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
api_instance = Infoplus.LoggedTimeTypeApi(Infoplus.ApiClient(configuration))
search_text = 'search_text_example' # str | Search text, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)

try:
    # Search loggedTimeTypes
    api_response = api_instance.get_logged_time_type_by_search_text(search_text=search_text, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggedTimeTypeApi->get_logged_time_type_by_search_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | **str**| Search text, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 

### Return type

[**list[LoggedTimeType]**](LoggedTimeType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

