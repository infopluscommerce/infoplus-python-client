# Infoplus.WarehouseApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_warehouse**](WarehouseApi.md#add_warehouse) | **POST** /beta/warehouse | Create a warehouse
[**add_warehouse_audit**](WarehouseApi.md#add_warehouse_audit) | **PUT** /beta/warehouse/{warehouseId}/audit/{warehouseAudit} | Add new audit for a warehouse
[**add_warehouse_file**](WarehouseApi.md#add_warehouse_file) | **POST** /beta/warehouse/{warehouseId}/file/{fileName} | Attach a file to a warehouse
[**add_warehouse_file_by_url**](WarehouseApi.md#add_warehouse_file_by_url) | **POST** /beta/warehouse/{warehouseId}/file | Attach a file to a warehouse by URL.
[**add_warehouse_tag**](WarehouseApi.md#add_warehouse_tag) | **PUT** /beta/warehouse/{warehouseId}/tag/{warehouseTag} | Add new tags for a warehouse.
[**delete_warehouse_file**](WarehouseApi.md#delete_warehouse_file) | **DELETE** /beta/warehouse/{warehouseId}/file/{fileId} | Delete a file for a warehouse.
[**delete_warehouse_tag**](WarehouseApi.md#delete_warehouse_tag) | **DELETE** /beta/warehouse/{warehouseId}/tag/{warehouseTag} | Delete a tag for a warehouse.
[**get_duplicate_warehouse_by_id**](WarehouseApi.md#get_duplicate_warehouse_by_id) | **GET** /beta/warehouse/duplicate/{warehouseId} | Get a duplicated a warehouse by id
[**get_warehouse_by_filter**](WarehouseApi.md#get_warehouse_by_filter) | **GET** /beta/warehouse/search | Search warehouses by filter
[**get_warehouse_by_id**](WarehouseApi.md#get_warehouse_by_id) | **GET** /beta/warehouse/{warehouseId} | Get a warehouse by id
[**get_warehouse_files**](WarehouseApi.md#get_warehouse_files) | **GET** /beta/warehouse/{warehouseId}/file | Get the files for a warehouse.
[**get_warehouse_tags**](WarehouseApi.md#get_warehouse_tags) | **GET** /beta/warehouse/{warehouseId}/tag | Get the tags for a warehouse.
[**update_warehouse**](WarehouseApi.md#update_warehouse) | **PUT** /beta/warehouse | Update a warehouse
[**update_warehouse_custom_fields**](WarehouseApi.md#update_warehouse_custom_fields) | **PUT** /beta/warehouse/customFields | Update a warehouse custom fields


# **add_warehouse**
> Warehouse add_warehouse(body)

Create a warehouse

Inserts a new warehouse using the specified data.

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
api_instance = Infoplus.WarehouseApi(Infoplus.ApiClient(configuration))
body = Infoplus.Warehouse() # Warehouse | Warehouse to be inserted.

try:
    # Create a warehouse
    api_response = api_instance.add_warehouse(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseApi->add_warehouse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Warehouse**](Warehouse.md)| Warehouse to be inserted. | 

### Return type

[**Warehouse**](Warehouse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_warehouse_audit**
> add_warehouse_audit(warehouse_id, warehouse_audit)

Add new audit for a warehouse

Adds an audit to an existing warehouse.

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
api_instance = Infoplus.WarehouseApi(Infoplus.ApiClient(configuration))
warehouse_id = 56 # int | Id of the warehouse to add an audit to
warehouse_audit = 'warehouse_audit_example' # str | The audit to add

try:
    # Add new audit for a warehouse
    api_instance.add_warehouse_audit(warehouse_id, warehouse_audit)
except ApiException as e:
    print("Exception when calling WarehouseApi->add_warehouse_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **int**| Id of the warehouse to add an audit to | 
 **warehouse_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_warehouse_file**
> add_warehouse_file(warehouse_id, file_name)

Attach a file to a warehouse

Adds a file to an existing warehouse.

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
api_instance = Infoplus.WarehouseApi(Infoplus.ApiClient(configuration))
warehouse_id = 56 # int | Id of the warehouse to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a warehouse
    api_instance.add_warehouse_file(warehouse_id, file_name)
except ApiException as e:
    print("Exception when calling WarehouseApi->add_warehouse_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **int**| Id of the warehouse to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_warehouse_file_by_url**
> add_warehouse_file_by_url(body, warehouse_id)

Attach a file to a warehouse by URL.

Adds a file to an existing warehouse by URL.

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
api_instance = Infoplus.WarehouseApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
warehouse_id = 56 # int | Id of the warehouse to add an file to

try:
    # Attach a file to a warehouse by URL.
    api_instance.add_warehouse_file_by_url(body, warehouse_id)
except ApiException as e:
    print("Exception when calling WarehouseApi->add_warehouse_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **warehouse_id** | **int**| Id of the warehouse to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_warehouse_tag**
> add_warehouse_tag(warehouse_id, warehouse_tag)

Add new tags for a warehouse.

Adds a tag to an existing warehouse.

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
api_instance = Infoplus.WarehouseApi(Infoplus.ApiClient(configuration))
warehouse_id = 56 # int | Id of the warehouse to add a tag to
warehouse_tag = 'warehouse_tag_example' # str | The tag to add

try:
    # Add new tags for a warehouse.
    api_instance.add_warehouse_tag(warehouse_id, warehouse_tag)
except ApiException as e:
    print("Exception when calling WarehouseApi->add_warehouse_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **int**| Id of the warehouse to add a tag to | 
 **warehouse_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_warehouse_file**
> delete_warehouse_file(warehouse_id, file_id)

Delete a file for a warehouse.

Deletes an existing warehouse file using the specified data.

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
api_instance = Infoplus.WarehouseApi(Infoplus.ApiClient(configuration))
warehouse_id = 56 # int | Id of the warehouse to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a warehouse.
    api_instance.delete_warehouse_file(warehouse_id, file_id)
except ApiException as e:
    print("Exception when calling WarehouseApi->delete_warehouse_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **int**| Id of the warehouse to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_warehouse_tag**
> delete_warehouse_tag(warehouse_id, warehouse_tag)

Delete a tag for a warehouse.

Deletes an existing warehouse tag using the specified data.

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
api_instance = Infoplus.WarehouseApi(Infoplus.ApiClient(configuration))
warehouse_id = 56 # int | Id of the warehouse to remove tag from
warehouse_tag = 'warehouse_tag_example' # str | The tag to delete

try:
    # Delete a tag for a warehouse.
    api_instance.delete_warehouse_tag(warehouse_id, warehouse_tag)
except ApiException as e:
    print("Exception when calling WarehouseApi->delete_warehouse_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **int**| Id of the warehouse to remove tag from | 
 **warehouse_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_warehouse_by_id**
> Warehouse get_duplicate_warehouse_by_id(warehouse_id)

Get a duplicated a warehouse by id

Returns a duplicated warehouse identified by the specified id.

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
api_instance = Infoplus.WarehouseApi(Infoplus.ApiClient(configuration))
warehouse_id = 56 # int | Id of the warehouse to be duplicated.

try:
    # Get a duplicated a warehouse by id
    api_response = api_instance.get_duplicate_warehouse_by_id(warehouse_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseApi->get_duplicate_warehouse_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **int**| Id of the warehouse to be duplicated. | 

### Return type

[**Warehouse**](Warehouse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_by_filter**
> list[Warehouse] get_warehouse_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search warehouses by filter

Returns the list of warehouses that match the given filter.

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
api_instance = Infoplus.WarehouseApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search warehouses by filter
    api_response = api_instance.get_warehouse_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseApi->get_warehouse_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Warehouse]**](Warehouse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_by_id**
> Warehouse get_warehouse_by_id(warehouse_id)

Get a warehouse by id

Returns the warehouse identified by the specified id.

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
api_instance = Infoplus.WarehouseApi(Infoplus.ApiClient(configuration))
warehouse_id = 56 # int | Id of the warehouse to be returned.

try:
    # Get a warehouse by id
    api_response = api_instance.get_warehouse_by_id(warehouse_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseApi->get_warehouse_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **int**| Id of the warehouse to be returned. | 

### Return type

[**Warehouse**](Warehouse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_files**
> get_warehouse_files(warehouse_id)

Get the files for a warehouse.

Get all existing warehouse files.

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
api_instance = Infoplus.WarehouseApi(Infoplus.ApiClient(configuration))
warehouse_id = 56 # int | Id of the warehouse to get files for

try:
    # Get the files for a warehouse.
    api_instance.get_warehouse_files(warehouse_id)
except ApiException as e:
    print("Exception when calling WarehouseApi->get_warehouse_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **int**| Id of the warehouse to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_tags**
> get_warehouse_tags(warehouse_id)

Get the tags for a warehouse.

Get all existing warehouse tags.

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
api_instance = Infoplus.WarehouseApi(Infoplus.ApiClient(configuration))
warehouse_id = 56 # int | Id of the warehouse to get tags for

try:
    # Get the tags for a warehouse.
    api_instance.get_warehouse_tags(warehouse_id)
except ApiException as e:
    print("Exception when calling WarehouseApi->get_warehouse_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **int**| Id of the warehouse to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_warehouse**
> update_warehouse(body)

Update a warehouse

Updates an existing warehouse using the specified data.

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
api_instance = Infoplus.WarehouseApi(Infoplus.ApiClient(configuration))
body = Infoplus.Warehouse() # Warehouse | Warehouse to be updated.

try:
    # Update a warehouse
    api_instance.update_warehouse(body)
except ApiException as e:
    print("Exception when calling WarehouseApi->update_warehouse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Warehouse**](Warehouse.md)| Warehouse to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_warehouse_custom_fields**
> update_warehouse_custom_fields(body)

Update a warehouse custom fields

Updates an existing warehouse custom fields using the specified data.

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
api_instance = Infoplus.WarehouseApi(Infoplus.ApiClient(configuration))
body = Infoplus.Warehouse() # Warehouse | Warehouse to be updated.

try:
    # Update a warehouse custom fields
    api_instance.update_warehouse_custom_fields(body)
except ApiException as e:
    print("Exception when calling WarehouseApi->update_warehouse_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Warehouse**](Warehouse.md)| Warehouse to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

