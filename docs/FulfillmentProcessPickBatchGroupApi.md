# Infoplus.FulfillmentProcessPickBatchGroupApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fulfillment_process_group_picks_by_by_id**](FulfillmentProcessPickBatchGroupApi.md#get_fulfillment_process_group_picks_by_by_id) | **GET** /beta/fulfillmentProcessPickBatchGroup/{fulfillmentProcessPickBatchGroupId} | Get a fulfillmentProcessPickBatchGroup by id
[**get_fulfillment_process_pick_batch_group_by_search_text**](FulfillmentProcessPickBatchGroupApi.md#get_fulfillment_process_pick_batch_group_by_search_text) | **GET** /beta/fulfillmentProcessPickBatchGroup/search | Search fulfillmentProcessPickBatchGroups


# **get_fulfillment_process_group_picks_by_by_id**
> FulfillmentProcessPickBatchGroup get_fulfillment_process_group_picks_by_by_id(fulfillment_process_pick_batch_group_id)

Get a fulfillmentProcessPickBatchGroup by id

Returns the fulfillmentProcessPickBatchGroup identified by the specified id.

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
api_instance = Infoplus.FulfillmentProcessPickBatchGroupApi(Infoplus.ApiClient(configuration))
fulfillment_process_pick_batch_group_id = 'fulfillment_process_pick_batch_group_id_example' # str | Id of fulfillmentProcessPickBatchGroup to be returned.

try:
    # Get a fulfillmentProcessPickBatchGroup by id
    api_response = api_instance.get_fulfillment_process_group_picks_by_by_id(fulfillment_process_pick_batch_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentProcessPickBatchGroupApi->get_fulfillment_process_group_picks_by_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_pick_batch_group_id** | **str**| Id of fulfillmentProcessPickBatchGroup to be returned. | 

### Return type

[**FulfillmentProcessPickBatchGroup**](FulfillmentProcessPickBatchGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_process_pick_batch_group_by_search_text**
> list[FulfillmentProcessPickBatchGroup] get_fulfillment_process_pick_batch_group_by_search_text(search_text=search_text, page=page, limit=limit)

Search fulfillmentProcessPickBatchGroups

Returns the list of fulfillmentProcessPickBatchGroups that match the given searchText.

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
api_instance = Infoplus.FulfillmentProcessPickBatchGroupApi(Infoplus.ApiClient(configuration))
search_text = 'search_text_example' # str | Search text, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)

try:
    # Search fulfillmentProcessPickBatchGroups
    api_response = api_instance.get_fulfillment_process_pick_batch_group_by_search_text(search_text=search_text, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentProcessPickBatchGroupApi->get_fulfillment_process_pick_batch_group_by_search_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | **str**| Search text, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 

### Return type

[**list[FulfillmentProcessPickBatchGroup]**](FulfillmentProcessPickBatchGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

