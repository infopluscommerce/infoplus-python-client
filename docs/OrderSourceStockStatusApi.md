# Infoplus.OrderSourceStockStatusApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_order_source_stock_status_audit**](OrderSourceStockStatusApi.md#add_order_source_stock_status_audit) | **PUT** /beta/orderSourceStockStatus/{orderSourceStockStatusId}/audit/{orderSourceStockStatusAudit} | Add new audit for an orderSourceStockStatus
[**add_order_source_stock_status_file**](OrderSourceStockStatusApi.md#add_order_source_stock_status_file) | **POST** /beta/orderSourceStockStatus/{orderSourceStockStatusId}/file/{fileName} | Attach a file to an orderSourceStockStatus
[**add_order_source_stock_status_tag**](OrderSourceStockStatusApi.md#add_order_source_stock_status_tag) | **PUT** /beta/orderSourceStockStatus/{orderSourceStockStatusId}/tag/{orderSourceStockStatusTag} | Add new tags for an orderSourceStockStatus.
[**delete_order_source_stock_status_tag**](OrderSourceStockStatusApi.md#delete_order_source_stock_status_tag) | **DELETE** /beta/orderSourceStockStatus/{orderSourceStockStatusId}/tag/{orderSourceStockStatusTag} | Delete a tag for an orderSourceStockStatus.
[**get_duplicate_order_source_stock_status_by_id**](OrderSourceStockStatusApi.md#get_duplicate_order_source_stock_status_by_id) | **GET** /beta/orderSourceStockStatus/duplicate/{orderSourceStockStatusId} | Get a duplicated an orderSourceStockStatus by id
[**get_order_source_stock_status_by_filter**](OrderSourceStockStatusApi.md#get_order_source_stock_status_by_filter) | **GET** /beta/orderSourceStockStatus/search | Search orderSourceStockStatuses by filter
[**get_order_source_stock_status_by_id**](OrderSourceStockStatusApi.md#get_order_source_stock_status_by_id) | **GET** /beta/orderSourceStockStatus/{orderSourceStockStatusId} | Get an orderSourceStockStatus by id
[**get_order_source_stock_status_tags**](OrderSourceStockStatusApi.md#get_order_source_stock_status_tags) | **GET** /beta/orderSourceStockStatus/{orderSourceStockStatusId}/tag | Get the tags for an orderSourceStockStatus.


# **add_order_source_stock_status_audit**
> add_order_source_stock_status_audit(order_source_stock_status_id, order_source_stock_status_audit)

Add new audit for an orderSourceStockStatus

Adds an audit to an existing orderSourceStockStatus.

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
api_instance = Infoplus.OrderSourceStockStatusApi(Infoplus.ApiClient(configuration))
order_source_stock_status_id = 56 # int | Id of the orderSourceStockStatus to add an audit to
order_source_stock_status_audit = 'order_source_stock_status_audit_example' # str | The audit to add

try:
    # Add new audit for an orderSourceStockStatus
    api_instance.add_order_source_stock_status_audit(order_source_stock_status_id, order_source_stock_status_audit)
except ApiException as e:
    print("Exception when calling OrderSourceStockStatusApi->add_order_source_stock_status_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_stock_status_id** | **int**| Id of the orderSourceStockStatus to add an audit to | 
 **order_source_stock_status_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_source_stock_status_file**
> add_order_source_stock_status_file(order_source_stock_status_id, file_name)

Attach a file to an orderSourceStockStatus

Adds a file to an existing orderSourceStockStatus.

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
api_instance = Infoplus.OrderSourceStockStatusApi(Infoplus.ApiClient(configuration))
order_source_stock_status_id = 56 # int | Id of the orderSourceStockStatus to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an orderSourceStockStatus
    api_instance.add_order_source_stock_status_file(order_source_stock_status_id, file_name)
except ApiException as e:
    print("Exception when calling OrderSourceStockStatusApi->add_order_source_stock_status_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_stock_status_id** | **int**| Id of the orderSourceStockStatus to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_source_stock_status_tag**
> add_order_source_stock_status_tag(order_source_stock_status_id, order_source_stock_status_tag)

Add new tags for an orderSourceStockStatus.

Adds a tag to an existing orderSourceStockStatus.

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
api_instance = Infoplus.OrderSourceStockStatusApi(Infoplus.ApiClient(configuration))
order_source_stock_status_id = 56 # int | Id of the orderSourceStockStatus to add a tag to
order_source_stock_status_tag = 'order_source_stock_status_tag_example' # str | The tag to add

try:
    # Add new tags for an orderSourceStockStatus.
    api_instance.add_order_source_stock_status_tag(order_source_stock_status_id, order_source_stock_status_tag)
except ApiException as e:
    print("Exception when calling OrderSourceStockStatusApi->add_order_source_stock_status_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_stock_status_id** | **int**| Id of the orderSourceStockStatus to add a tag to | 
 **order_source_stock_status_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_source_stock_status_tag**
> delete_order_source_stock_status_tag(order_source_stock_status_id, order_source_stock_status_tag)

Delete a tag for an orderSourceStockStatus.

Deletes an existing orderSourceStockStatus tag using the specified data.

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
api_instance = Infoplus.OrderSourceStockStatusApi(Infoplus.ApiClient(configuration))
order_source_stock_status_id = 56 # int | Id of the orderSourceStockStatus to remove tag from
order_source_stock_status_tag = 'order_source_stock_status_tag_example' # str | The tag to delete

try:
    # Delete a tag for an orderSourceStockStatus.
    api_instance.delete_order_source_stock_status_tag(order_source_stock_status_id, order_source_stock_status_tag)
except ApiException as e:
    print("Exception when calling OrderSourceStockStatusApi->delete_order_source_stock_status_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_stock_status_id** | **int**| Id of the orderSourceStockStatus to remove tag from | 
 **order_source_stock_status_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_order_source_stock_status_by_id**
> OrderSourceStockStatus get_duplicate_order_source_stock_status_by_id(order_source_stock_status_id)

Get a duplicated an orderSourceStockStatus by id

Returns a duplicated orderSourceStockStatus identified by the specified id.

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
api_instance = Infoplus.OrderSourceStockStatusApi(Infoplus.ApiClient(configuration))
order_source_stock_status_id = 56 # int | Id of the orderSourceStockStatus to be duplicated.

try:
    # Get a duplicated an orderSourceStockStatus by id
    api_response = api_instance.get_duplicate_order_source_stock_status_by_id(order_source_stock_status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderSourceStockStatusApi->get_duplicate_order_source_stock_status_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_stock_status_id** | **int**| Id of the orderSourceStockStatus to be duplicated. | 

### Return type

[**OrderSourceStockStatus**](OrderSourceStockStatus.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_source_stock_status_by_filter**
> list[OrderSourceStockStatus] get_order_source_stock_status_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search orderSourceStockStatuses by filter

Returns the list of orderSourceStockStatuses that match the given filter.

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
api_instance = Infoplus.OrderSourceStockStatusApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search orderSourceStockStatuses by filter
    api_response = api_instance.get_order_source_stock_status_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderSourceStockStatusApi->get_order_source_stock_status_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[OrderSourceStockStatus]**](OrderSourceStockStatus.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_source_stock_status_by_id**
> OrderSourceStockStatus get_order_source_stock_status_by_id(order_source_stock_status_id)

Get an orderSourceStockStatus by id

Returns the orderSourceStockStatus identified by the specified id.

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
api_instance = Infoplus.OrderSourceStockStatusApi(Infoplus.ApiClient(configuration))
order_source_stock_status_id = 56 # int | Id of the orderSourceStockStatus to be returned.

try:
    # Get an orderSourceStockStatus by id
    api_response = api_instance.get_order_source_stock_status_by_id(order_source_stock_status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderSourceStockStatusApi->get_order_source_stock_status_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_stock_status_id** | **int**| Id of the orderSourceStockStatus to be returned. | 

### Return type

[**OrderSourceStockStatus**](OrderSourceStockStatus.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_source_stock_status_tags**
> get_order_source_stock_status_tags(order_source_stock_status_id)

Get the tags for an orderSourceStockStatus.

Get all existing orderSourceStockStatus tags.

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
api_instance = Infoplus.OrderSourceStockStatusApi(Infoplus.ApiClient(configuration))
order_source_stock_status_id = 56 # int | Id of the orderSourceStockStatus to get tags for

try:
    # Get the tags for an orderSourceStockStatus.
    api_instance.get_order_source_stock_status_tags(order_source_stock_status_id)
except ApiException as e:
    print("Exception when calling OrderSourceStockStatusApi->get_order_source_stock_status_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_stock_status_id** | **int**| Id of the orderSourceStockStatus to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

