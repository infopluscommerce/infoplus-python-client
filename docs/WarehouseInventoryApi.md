# Infoplus.WarehouseInventoryApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_warehouse_inventory_audit**](WarehouseInventoryApi.md#add_warehouse_inventory_audit) | **PUT** /beta/warehouseInventory/{warehouseInventoryId}/audit/{warehouseInventoryAudit} | Add new audit for a warehouseInventory
[**add_warehouse_inventory_file**](WarehouseInventoryApi.md#add_warehouse_inventory_file) | **POST** /beta/warehouseInventory/{warehouseInventoryId}/file/{fileName} | Attach a file to a warehouseInventory
[**add_warehouse_inventory_file_by_url**](WarehouseInventoryApi.md#add_warehouse_inventory_file_by_url) | **POST** /beta/warehouseInventory/{warehouseInventoryId}/file | Attach a file to a warehouseInventory by URL.
[**add_warehouse_inventory_tag**](WarehouseInventoryApi.md#add_warehouse_inventory_tag) | **PUT** /beta/warehouseInventory/{warehouseInventoryId}/tag/{warehouseInventoryTag} | Add new tags for a warehouseInventory.
[**delete_warehouse_inventory_file**](WarehouseInventoryApi.md#delete_warehouse_inventory_file) | **DELETE** /beta/warehouseInventory/{warehouseInventoryId}/file/{fileId} | Delete a file for a warehouseInventory.
[**delete_warehouse_inventory_tag**](WarehouseInventoryApi.md#delete_warehouse_inventory_tag) | **DELETE** /beta/warehouseInventory/{warehouseInventoryId}/tag/{warehouseInventoryTag} | Delete a tag for a warehouseInventory.
[**get_duplicate_warehouse_inventory_by_id**](WarehouseInventoryApi.md#get_duplicate_warehouse_inventory_by_id) | **GET** /beta/warehouseInventory/duplicate/{warehouseInventoryId} | Get a duplicated a warehouseInventory by id
[**get_warehouse_inventory_by_filter**](WarehouseInventoryApi.md#get_warehouse_inventory_by_filter) | **GET** /beta/warehouseInventory/search | Search warehouseInventorys by filter
[**get_warehouse_inventory_by_id**](WarehouseInventoryApi.md#get_warehouse_inventory_by_id) | **GET** /beta/warehouseInventory/{warehouseInventoryId} | Get a warehouseInventory by id
[**get_warehouse_inventory_files**](WarehouseInventoryApi.md#get_warehouse_inventory_files) | **GET** /beta/warehouseInventory/{warehouseInventoryId}/file | Get the files for a warehouseInventory.
[**get_warehouse_inventory_tags**](WarehouseInventoryApi.md#get_warehouse_inventory_tags) | **GET** /beta/warehouseInventory/{warehouseInventoryId}/tag | Get the tags for a warehouseInventory.


# **add_warehouse_inventory_audit**
> add_warehouse_inventory_audit(warehouse_inventory_id, warehouse_inventory_audit)

Add new audit for a warehouseInventory

Adds an audit to an existing warehouseInventory.

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
api_instance = Infoplus.WarehouseInventoryApi(Infoplus.ApiClient(configuration))
warehouse_inventory_id = 56 # int | Id of the warehouseInventory to add an audit to
warehouse_inventory_audit = 'warehouse_inventory_audit_example' # str | The audit to add

try:
    # Add new audit for a warehouseInventory
    api_instance.add_warehouse_inventory_audit(warehouse_inventory_id, warehouse_inventory_audit)
except ApiException as e:
    print("Exception when calling WarehouseInventoryApi->add_warehouse_inventory_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_inventory_id** | **int**| Id of the warehouseInventory to add an audit to | 
 **warehouse_inventory_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_warehouse_inventory_file**
> add_warehouse_inventory_file(warehouse_inventory_id, file_name)

Attach a file to a warehouseInventory

Adds a file to an existing warehouseInventory.

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
api_instance = Infoplus.WarehouseInventoryApi(Infoplus.ApiClient(configuration))
warehouse_inventory_id = 56 # int | Id of the warehouseInventory to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a warehouseInventory
    api_instance.add_warehouse_inventory_file(warehouse_inventory_id, file_name)
except ApiException as e:
    print("Exception when calling WarehouseInventoryApi->add_warehouse_inventory_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_inventory_id** | **int**| Id of the warehouseInventory to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_warehouse_inventory_file_by_url**
> add_warehouse_inventory_file_by_url(body, warehouse_inventory_id)

Attach a file to a warehouseInventory by URL.

Adds a file to an existing warehouseInventory by URL.

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
api_instance = Infoplus.WarehouseInventoryApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
warehouse_inventory_id = 56 # int | Id of the warehouseInventory to add an file to

try:
    # Attach a file to a warehouseInventory by URL.
    api_instance.add_warehouse_inventory_file_by_url(body, warehouse_inventory_id)
except ApiException as e:
    print("Exception when calling WarehouseInventoryApi->add_warehouse_inventory_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **warehouse_inventory_id** | **int**| Id of the warehouseInventory to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_warehouse_inventory_tag**
> add_warehouse_inventory_tag(warehouse_inventory_id, warehouse_inventory_tag)

Add new tags for a warehouseInventory.

Adds a tag to an existing warehouseInventory.

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
api_instance = Infoplus.WarehouseInventoryApi(Infoplus.ApiClient(configuration))
warehouse_inventory_id = 56 # int | Id of the warehouseInventory to add a tag to
warehouse_inventory_tag = 'warehouse_inventory_tag_example' # str | The tag to add

try:
    # Add new tags for a warehouseInventory.
    api_instance.add_warehouse_inventory_tag(warehouse_inventory_id, warehouse_inventory_tag)
except ApiException as e:
    print("Exception when calling WarehouseInventoryApi->add_warehouse_inventory_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_inventory_id** | **int**| Id of the warehouseInventory to add a tag to | 
 **warehouse_inventory_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_warehouse_inventory_file**
> delete_warehouse_inventory_file(warehouse_inventory_id, file_id)

Delete a file for a warehouseInventory.

Deletes an existing warehouseInventory file using the specified data.

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
api_instance = Infoplus.WarehouseInventoryApi(Infoplus.ApiClient(configuration))
warehouse_inventory_id = 56 # int | Id of the warehouseInventory to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a warehouseInventory.
    api_instance.delete_warehouse_inventory_file(warehouse_inventory_id, file_id)
except ApiException as e:
    print("Exception when calling WarehouseInventoryApi->delete_warehouse_inventory_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_inventory_id** | **int**| Id of the warehouseInventory to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_warehouse_inventory_tag**
> delete_warehouse_inventory_tag(warehouse_inventory_id, warehouse_inventory_tag)

Delete a tag for a warehouseInventory.

Deletes an existing warehouseInventory tag using the specified data.

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
api_instance = Infoplus.WarehouseInventoryApi(Infoplus.ApiClient(configuration))
warehouse_inventory_id = 56 # int | Id of the warehouseInventory to remove tag from
warehouse_inventory_tag = 'warehouse_inventory_tag_example' # str | The tag to delete

try:
    # Delete a tag for a warehouseInventory.
    api_instance.delete_warehouse_inventory_tag(warehouse_inventory_id, warehouse_inventory_tag)
except ApiException as e:
    print("Exception when calling WarehouseInventoryApi->delete_warehouse_inventory_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_inventory_id** | **int**| Id of the warehouseInventory to remove tag from | 
 **warehouse_inventory_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_warehouse_inventory_by_id**
> WarehouseInventory get_duplicate_warehouse_inventory_by_id(warehouse_inventory_id)

Get a duplicated a warehouseInventory by id

Returns a duplicated warehouseInventory identified by the specified id.

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
api_instance = Infoplus.WarehouseInventoryApi(Infoplus.ApiClient(configuration))
warehouse_inventory_id = 56 # int | Id of the warehouseInventory to be duplicated.

try:
    # Get a duplicated a warehouseInventory by id
    api_response = api_instance.get_duplicate_warehouse_inventory_by_id(warehouse_inventory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseInventoryApi->get_duplicate_warehouse_inventory_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_inventory_id** | **int**| Id of the warehouseInventory to be duplicated. | 

### Return type

[**WarehouseInventory**](WarehouseInventory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_inventory_by_filter**
> list[WarehouseInventory] get_warehouse_inventory_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search warehouseInventorys by filter

Returns the list of warehouseInventorys that match the given filter.

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
api_instance = Infoplus.WarehouseInventoryApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search warehouseInventorys by filter
    api_response = api_instance.get_warehouse_inventory_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseInventoryApi->get_warehouse_inventory_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[WarehouseInventory]**](WarehouseInventory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_inventory_by_id**
> WarehouseInventory get_warehouse_inventory_by_id(warehouse_inventory_id)

Get a warehouseInventory by id

Returns the warehouseInventory identified by the specified id.

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
api_instance = Infoplus.WarehouseInventoryApi(Infoplus.ApiClient(configuration))
warehouse_inventory_id = 56 # int | Id of the warehouseInventory to be returned.

try:
    # Get a warehouseInventory by id
    api_response = api_instance.get_warehouse_inventory_by_id(warehouse_inventory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseInventoryApi->get_warehouse_inventory_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_inventory_id** | **int**| Id of the warehouseInventory to be returned. | 

### Return type

[**WarehouseInventory**](WarehouseInventory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_inventory_files**
> get_warehouse_inventory_files(warehouse_inventory_id)

Get the files for a warehouseInventory.

Get all existing warehouseInventory files.

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
api_instance = Infoplus.WarehouseInventoryApi(Infoplus.ApiClient(configuration))
warehouse_inventory_id = 56 # int | Id of the warehouseInventory to get files for

try:
    # Get the files for a warehouseInventory.
    api_instance.get_warehouse_inventory_files(warehouse_inventory_id)
except ApiException as e:
    print("Exception when calling WarehouseInventoryApi->get_warehouse_inventory_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_inventory_id** | **int**| Id of the warehouseInventory to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_inventory_tags**
> get_warehouse_inventory_tags(warehouse_inventory_id)

Get the tags for a warehouseInventory.

Get all existing warehouseInventory tags.

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
api_instance = Infoplus.WarehouseInventoryApi(Infoplus.ApiClient(configuration))
warehouse_inventory_id = 56 # int | Id of the warehouseInventory to get tags for

try:
    # Get the tags for a warehouseInventory.
    api_instance.get_warehouse_inventory_tags(warehouse_inventory_id)
except ApiException as e:
    print("Exception when calling WarehouseInventoryApi->get_warehouse_inventory_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_inventory_id** | **int**| Id of the warehouseInventory to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

