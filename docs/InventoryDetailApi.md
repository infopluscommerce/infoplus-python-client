# Infoplus.InventoryDetailApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_inventory_detail_audit**](InventoryDetailApi.md#add_inventory_detail_audit) | **PUT** /beta/inventoryDetail/{inventoryDetailId}/audit/{inventoryDetailAudit} | Add new audit for an inventoryDetail
[**add_inventory_detail_tag**](InventoryDetailApi.md#add_inventory_detail_tag) | **PUT** /beta/inventoryDetail/{inventoryDetailId}/tag/{inventoryDetailTag} | Add new tags for an inventoryDetail.
[**delete_inventory_detail_tag**](InventoryDetailApi.md#delete_inventory_detail_tag) | **DELETE** /beta/inventoryDetail/{inventoryDetailId}/tag/{inventoryDetailTag} | Delete a tag for an inventoryDetail.
[**get_duplicate_inventory_detail_by_id**](InventoryDetailApi.md#get_duplicate_inventory_detail_by_id) | **GET** /beta/inventoryDetail/duplicate/{inventoryDetailId} | Get a duplicated an inventoryDetail by id
[**get_inventory_detail_by_filter**](InventoryDetailApi.md#get_inventory_detail_by_filter) | **GET** /beta/inventoryDetail/search | Search inventoryDetails by filter
[**get_inventory_detail_by_id**](InventoryDetailApi.md#get_inventory_detail_by_id) | **GET** /beta/inventoryDetail/{inventoryDetailId} | Get an inventoryDetail by id
[**get_inventory_detail_tags**](InventoryDetailApi.md#get_inventory_detail_tags) | **GET** /beta/inventoryDetail/{inventoryDetailId}/tag | Get the tags for an inventoryDetail.
[**update_inventory_detail_custom_fields**](InventoryDetailApi.md#update_inventory_detail_custom_fields) | **PUT** /beta/inventoryDetail/customFields | Update an inventoryDetail custom fields


# **add_inventory_detail_audit**
> add_inventory_detail_audit(inventory_detail_id, inventory_detail_audit)

Add new audit for an inventoryDetail

Adds an audit to an existing inventoryDetail.

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
api_instance = Infoplus.InventoryDetailApi(Infoplus.ApiClient(configuration))
inventory_detail_id = 56 # int | Id of the inventoryDetail to add an audit to
inventory_detail_audit = 'inventory_detail_audit_example' # str | The audit to add

try:
    # Add new audit for an inventoryDetail
    api_instance.add_inventory_detail_audit(inventory_detail_id, inventory_detail_audit)
except ApiException as e:
    print("Exception when calling InventoryDetailApi->add_inventory_detail_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_detail_id** | **int**| Id of the inventoryDetail to add an audit to | 
 **inventory_detail_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_inventory_detail_tag**
> add_inventory_detail_tag(inventory_detail_id, inventory_detail_tag)

Add new tags for an inventoryDetail.

Adds a tag to an existing inventoryDetail.

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
api_instance = Infoplus.InventoryDetailApi(Infoplus.ApiClient(configuration))
inventory_detail_id = 56 # int | Id of the inventoryDetail to add a tag to
inventory_detail_tag = 'inventory_detail_tag_example' # str | The tag to add

try:
    # Add new tags for an inventoryDetail.
    api_instance.add_inventory_detail_tag(inventory_detail_id, inventory_detail_tag)
except ApiException as e:
    print("Exception when calling InventoryDetailApi->add_inventory_detail_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_detail_id** | **int**| Id of the inventoryDetail to add a tag to | 
 **inventory_detail_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inventory_detail_tag**
> delete_inventory_detail_tag(inventory_detail_id, inventory_detail_tag)

Delete a tag for an inventoryDetail.

Deletes an existing inventoryDetail tag using the specified data.

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
api_instance = Infoplus.InventoryDetailApi(Infoplus.ApiClient(configuration))
inventory_detail_id = 56 # int | Id of the inventoryDetail to remove tag from
inventory_detail_tag = 'inventory_detail_tag_example' # str | The tag to delete

try:
    # Delete a tag for an inventoryDetail.
    api_instance.delete_inventory_detail_tag(inventory_detail_id, inventory_detail_tag)
except ApiException as e:
    print("Exception when calling InventoryDetailApi->delete_inventory_detail_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_detail_id** | **int**| Id of the inventoryDetail to remove tag from | 
 **inventory_detail_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_inventory_detail_by_id**
> InventoryDetail get_duplicate_inventory_detail_by_id(inventory_detail_id)

Get a duplicated an inventoryDetail by id

Returns a duplicated inventoryDetail identified by the specified id.

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
api_instance = Infoplus.InventoryDetailApi(Infoplus.ApiClient(configuration))
inventory_detail_id = 56 # int | Id of the inventoryDetail to be duplicated.

try:
    # Get a duplicated an inventoryDetail by id
    api_response = api_instance.get_duplicate_inventory_detail_by_id(inventory_detail_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryDetailApi->get_duplicate_inventory_detail_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_detail_id** | **int**| Id of the inventoryDetail to be duplicated. | 

### Return type

[**InventoryDetail**](InventoryDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_detail_by_filter**
> list[InventoryDetail] get_inventory_detail_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search inventoryDetails by filter

Returns the list of inventoryDetails that match the given filter.

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
api_instance = Infoplus.InventoryDetailApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search inventoryDetails by filter
    api_response = api_instance.get_inventory_detail_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryDetailApi->get_inventory_detail_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[InventoryDetail]**](InventoryDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_detail_by_id**
> InventoryDetail get_inventory_detail_by_id(inventory_detail_id)

Get an inventoryDetail by id

Returns the inventoryDetail identified by the specified id.

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
api_instance = Infoplus.InventoryDetailApi(Infoplus.ApiClient(configuration))
inventory_detail_id = 56 # int | Id of the inventoryDetail to be returned.

try:
    # Get an inventoryDetail by id
    api_response = api_instance.get_inventory_detail_by_id(inventory_detail_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryDetailApi->get_inventory_detail_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_detail_id** | **int**| Id of the inventoryDetail to be returned. | 

### Return type

[**InventoryDetail**](InventoryDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_detail_tags**
> get_inventory_detail_tags(inventory_detail_id)

Get the tags for an inventoryDetail.

Get all existing inventoryDetail tags.

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
api_instance = Infoplus.InventoryDetailApi(Infoplus.ApiClient(configuration))
inventory_detail_id = 56 # int | Id of the inventoryDetail to get tags for

try:
    # Get the tags for an inventoryDetail.
    api_instance.get_inventory_detail_tags(inventory_detail_id)
except ApiException as e:
    print("Exception when calling InventoryDetailApi->get_inventory_detail_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_detail_id** | **int**| Id of the inventoryDetail to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inventory_detail_custom_fields**
> update_inventory_detail_custom_fields(body)

Update an inventoryDetail custom fields

Updates an existing inventoryDetail custom fields using the specified data.

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
api_instance = Infoplus.InventoryDetailApi(Infoplus.ApiClient(configuration))
body = Infoplus.InventoryDetail() # InventoryDetail | InventoryDetail to be updated.

try:
    # Update an inventoryDetail custom fields
    api_instance.update_inventory_detail_custom_fields(body)
except ApiException as e:
    print("Exception when calling InventoryDetailApi->update_inventory_detail_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryDetail**](InventoryDetail.md)| InventoryDetail to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

