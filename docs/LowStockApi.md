# Infoplus.LowStockApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_low_stock_audit**](LowStockApi.md#add_low_stock_audit) | **PUT** /beta/lowStock/{lowStockId}/audit/{lowStockAudit} | Add new audit for a lowStock
[**add_low_stock_tag**](LowStockApi.md#add_low_stock_tag) | **PUT** /beta/lowStock/{lowStockId}/tag/{lowStockTag} | Add new tags for a lowStock.
[**delete_low_stock_tag**](LowStockApi.md#delete_low_stock_tag) | **DELETE** /beta/lowStock/{lowStockId}/tag/{lowStockTag} | Delete a tag for a lowStock.
[**get_duplicate_low_stock_by_id**](LowStockApi.md#get_duplicate_low_stock_by_id) | **GET** /beta/lowStock/duplicate/{lowStockId} | Get a duplicated a lowStock by id
[**get_low_stock_by_filter**](LowStockApi.md#get_low_stock_by_filter) | **GET** /beta/lowStock/search | Search lowStocks by filter
[**get_low_stock_by_id**](LowStockApi.md#get_low_stock_by_id) | **GET** /beta/lowStock/{lowStockId} | Get a lowStock by id
[**get_low_stock_tags**](LowStockApi.md#get_low_stock_tags) | **GET** /beta/lowStock/{lowStockId}/tag | Get the tags for a lowStock.


# **add_low_stock_audit**
> add_low_stock_audit(low_stock_id, low_stock_audit)

Add new audit for a lowStock

Adds an audit to an existing lowStock.

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
api_instance = Infoplus.LowStockApi(Infoplus.ApiClient(configuration))
low_stock_id = 56 # int | Id of the lowStock to add an audit to
low_stock_audit = 'low_stock_audit_example' # str | The audit to add

try:
    # Add new audit for a lowStock
    api_instance.add_low_stock_audit(low_stock_id, low_stock_audit)
except ApiException as e:
    print("Exception when calling LowStockApi->add_low_stock_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **low_stock_id** | **int**| Id of the lowStock to add an audit to | 
 **low_stock_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_low_stock_tag**
> add_low_stock_tag(low_stock_id, low_stock_tag)

Add new tags for a lowStock.

Adds a tag to an existing lowStock.

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
api_instance = Infoplus.LowStockApi(Infoplus.ApiClient(configuration))
low_stock_id = 56 # int | Id of the lowStock to add a tag to
low_stock_tag = 'low_stock_tag_example' # str | The tag to add

try:
    # Add new tags for a lowStock.
    api_instance.add_low_stock_tag(low_stock_id, low_stock_tag)
except ApiException as e:
    print("Exception when calling LowStockApi->add_low_stock_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **low_stock_id** | **int**| Id of the lowStock to add a tag to | 
 **low_stock_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_low_stock_tag**
> delete_low_stock_tag(low_stock_id, low_stock_tag)

Delete a tag for a lowStock.

Deletes an existing lowStock tag using the specified data.

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
api_instance = Infoplus.LowStockApi(Infoplus.ApiClient(configuration))
low_stock_id = 56 # int | Id of the lowStock to remove tag from
low_stock_tag = 'low_stock_tag_example' # str | The tag to delete

try:
    # Delete a tag for a lowStock.
    api_instance.delete_low_stock_tag(low_stock_id, low_stock_tag)
except ApiException as e:
    print("Exception when calling LowStockApi->delete_low_stock_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **low_stock_id** | **int**| Id of the lowStock to remove tag from | 
 **low_stock_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_low_stock_by_id**
> LowStock get_duplicate_low_stock_by_id(low_stock_id)

Get a duplicated a lowStock by id

Returns a duplicated lowStock identified by the specified id.

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
api_instance = Infoplus.LowStockApi(Infoplus.ApiClient(configuration))
low_stock_id = 56 # int | Id of the lowStock to be duplicated.

try:
    # Get a duplicated a lowStock by id
    api_response = api_instance.get_duplicate_low_stock_by_id(low_stock_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LowStockApi->get_duplicate_low_stock_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **low_stock_id** | **int**| Id of the lowStock to be duplicated. | 

### Return type

[**LowStock**](LowStock.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_low_stock_by_filter**
> list[LowStock] get_low_stock_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search lowStocks by filter

Returns the list of lowStocks that match the given filter.

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
api_instance = Infoplus.LowStockApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search lowStocks by filter
    api_response = api_instance.get_low_stock_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LowStockApi->get_low_stock_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[LowStock]**](LowStock.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_low_stock_by_id**
> LowStock get_low_stock_by_id(low_stock_id)

Get a lowStock by id

Returns the lowStock identified by the specified id.

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
api_instance = Infoplus.LowStockApi(Infoplus.ApiClient(configuration))
low_stock_id = 56 # int | Id of the lowStock to be returned.

try:
    # Get a lowStock by id
    api_response = api_instance.get_low_stock_by_id(low_stock_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LowStockApi->get_low_stock_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **low_stock_id** | **int**| Id of the lowStock to be returned. | 

### Return type

[**LowStock**](LowStock.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_low_stock_tags**
> get_low_stock_tags(low_stock_id)

Get the tags for a lowStock.

Get all existing lowStock tags.

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
api_instance = Infoplus.LowStockApi(Infoplus.ApiClient(configuration))
low_stock_id = 56 # int | Id of the lowStock to get tags for

try:
    # Get the tags for a lowStock.
    api_instance.get_low_stock_tags(low_stock_id)
except ApiException as e:
    print("Exception when calling LowStockApi->get_low_stock_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **low_stock_id** | **int**| Id of the lowStock to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

