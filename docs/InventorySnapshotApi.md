# Infoplus.InventorySnapshotApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_inventory_snapshot_audit**](InventorySnapshotApi.md#add_inventory_snapshot_audit) | **PUT** /v3.0/inventorySnapshot/{inventorySnapshotId}/audit/{inventorySnapshotAudit} | Add new audit for an inventorySnapshot
[**add_inventory_snapshot_file**](InventorySnapshotApi.md#add_inventory_snapshot_file) | **POST** /v3.0/inventorySnapshot/{inventorySnapshotId}/file/{fileName} | Attach a file to an inventorySnapshot
[**add_inventory_snapshot_file_by_url**](InventorySnapshotApi.md#add_inventory_snapshot_file_by_url) | **POST** /v3.0/inventorySnapshot/{inventorySnapshotId}/file | Attach a file to an inventorySnapshot by URL.
[**add_inventory_snapshot_tag**](InventorySnapshotApi.md#add_inventory_snapshot_tag) | **PUT** /v3.0/inventorySnapshot/{inventorySnapshotId}/tag/{inventorySnapshotTag} | Add new tags for an inventorySnapshot.
[**delete_inventory_snapshot_file**](InventorySnapshotApi.md#delete_inventory_snapshot_file) | **DELETE** /v3.0/inventorySnapshot/{inventorySnapshotId}/file/{fileId} | Delete a file for an inventorySnapshot.
[**delete_inventory_snapshot_tag**](InventorySnapshotApi.md#delete_inventory_snapshot_tag) | **DELETE** /v3.0/inventorySnapshot/{inventorySnapshotId}/tag/{inventorySnapshotTag} | Delete a tag for an inventorySnapshot.
[**get_duplicate_inventory_snapshot_by_id**](InventorySnapshotApi.md#get_duplicate_inventory_snapshot_by_id) | **GET** /v3.0/inventorySnapshot/duplicate/{inventorySnapshotId} | Get a duplicated an inventorySnapshot by id
[**get_inventory_snapshot_by_filter**](InventorySnapshotApi.md#get_inventory_snapshot_by_filter) | **GET** /v3.0/inventorySnapshot/search | Search inventorySnapshots by filter
[**get_inventory_snapshot_by_id**](InventorySnapshotApi.md#get_inventory_snapshot_by_id) | **GET** /v3.0/inventorySnapshot/{inventorySnapshotId} | Get an inventorySnapshot by id
[**get_inventory_snapshot_files**](InventorySnapshotApi.md#get_inventory_snapshot_files) | **GET** /v3.0/inventorySnapshot/{inventorySnapshotId}/file | Get the files for an inventorySnapshot.
[**get_inventory_snapshot_tags**](InventorySnapshotApi.md#get_inventory_snapshot_tags) | **GET** /v3.0/inventorySnapshot/{inventorySnapshotId}/tag | Get the tags for an inventorySnapshot.


# **add_inventory_snapshot_audit**
> add_inventory_snapshot_audit(inventory_snapshot_id, inventory_snapshot_audit)

Add new audit for an inventorySnapshot

Adds an audit to an existing inventorySnapshot.

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
api_instance = Infoplus.InventorySnapshotApi(Infoplus.ApiClient(configuration))
inventory_snapshot_id = 56 # int | Id of the inventorySnapshot to add an audit to
inventory_snapshot_audit = 'inventory_snapshot_audit_example' # str | The audit to add

try:
    # Add new audit for an inventorySnapshot
    api_instance.add_inventory_snapshot_audit(inventory_snapshot_id, inventory_snapshot_audit)
except ApiException as e:
    print("Exception when calling InventorySnapshotApi->add_inventory_snapshot_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_snapshot_id** | **int**| Id of the inventorySnapshot to add an audit to | 
 **inventory_snapshot_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_inventory_snapshot_file**
> add_inventory_snapshot_file(inventory_snapshot_id, file_name)

Attach a file to an inventorySnapshot

Adds a file to an existing inventorySnapshot.

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
api_instance = Infoplus.InventorySnapshotApi(Infoplus.ApiClient(configuration))
inventory_snapshot_id = 56 # int | Id of the inventorySnapshot to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an inventorySnapshot
    api_instance.add_inventory_snapshot_file(inventory_snapshot_id, file_name)
except ApiException as e:
    print("Exception when calling InventorySnapshotApi->add_inventory_snapshot_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_snapshot_id** | **int**| Id of the inventorySnapshot to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_inventory_snapshot_file_by_url**
> add_inventory_snapshot_file_by_url(body, inventory_snapshot_id)

Attach a file to an inventorySnapshot by URL.

Adds a file to an existing inventorySnapshot by URL.

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
api_instance = Infoplus.InventorySnapshotApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
inventory_snapshot_id = 56 # int | Id of the inventorySnapshot to add an file to

try:
    # Attach a file to an inventorySnapshot by URL.
    api_instance.add_inventory_snapshot_file_by_url(body, inventory_snapshot_id)
except ApiException as e:
    print("Exception when calling InventorySnapshotApi->add_inventory_snapshot_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **inventory_snapshot_id** | **int**| Id of the inventorySnapshot to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_inventory_snapshot_tag**
> add_inventory_snapshot_tag(inventory_snapshot_id, inventory_snapshot_tag)

Add new tags for an inventorySnapshot.

Adds a tag to an existing inventorySnapshot.

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
api_instance = Infoplus.InventorySnapshotApi(Infoplus.ApiClient(configuration))
inventory_snapshot_id = 56 # int | Id of the inventorySnapshot to add a tag to
inventory_snapshot_tag = 'inventory_snapshot_tag_example' # str | The tag to add

try:
    # Add new tags for an inventorySnapshot.
    api_instance.add_inventory_snapshot_tag(inventory_snapshot_id, inventory_snapshot_tag)
except ApiException as e:
    print("Exception when calling InventorySnapshotApi->add_inventory_snapshot_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_snapshot_id** | **int**| Id of the inventorySnapshot to add a tag to | 
 **inventory_snapshot_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inventory_snapshot_file**
> delete_inventory_snapshot_file(inventory_snapshot_id, file_id)

Delete a file for an inventorySnapshot.

Deletes an existing inventorySnapshot file using the specified data.

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
api_instance = Infoplus.InventorySnapshotApi(Infoplus.ApiClient(configuration))
inventory_snapshot_id = 56 # int | Id of the inventorySnapshot to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an inventorySnapshot.
    api_instance.delete_inventory_snapshot_file(inventory_snapshot_id, file_id)
except ApiException as e:
    print("Exception when calling InventorySnapshotApi->delete_inventory_snapshot_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_snapshot_id** | **int**| Id of the inventorySnapshot to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inventory_snapshot_tag**
> delete_inventory_snapshot_tag(inventory_snapshot_id, inventory_snapshot_tag)

Delete a tag for an inventorySnapshot.

Deletes an existing inventorySnapshot tag using the specified data.

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
api_instance = Infoplus.InventorySnapshotApi(Infoplus.ApiClient(configuration))
inventory_snapshot_id = 56 # int | Id of the inventorySnapshot to remove tag from
inventory_snapshot_tag = 'inventory_snapshot_tag_example' # str | The tag to delete

try:
    # Delete a tag for an inventorySnapshot.
    api_instance.delete_inventory_snapshot_tag(inventory_snapshot_id, inventory_snapshot_tag)
except ApiException as e:
    print("Exception when calling InventorySnapshotApi->delete_inventory_snapshot_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_snapshot_id** | **int**| Id of the inventorySnapshot to remove tag from | 
 **inventory_snapshot_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_inventory_snapshot_by_id**
> InventorySnapshot get_duplicate_inventory_snapshot_by_id(inventory_snapshot_id)

Get a duplicated an inventorySnapshot by id

Returns a duplicated inventorySnapshot identified by the specified id.

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
api_instance = Infoplus.InventorySnapshotApi(Infoplus.ApiClient(configuration))
inventory_snapshot_id = 56 # int | Id of the inventorySnapshot to be duplicated.

try:
    # Get a duplicated an inventorySnapshot by id
    api_response = api_instance.get_duplicate_inventory_snapshot_by_id(inventory_snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventorySnapshotApi->get_duplicate_inventory_snapshot_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_snapshot_id** | **int**| Id of the inventorySnapshot to be duplicated. | 

### Return type

[**InventorySnapshot**](InventorySnapshot.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_snapshot_by_filter**
> list[InventorySnapshot] get_inventory_snapshot_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search inventorySnapshots by filter

Returns the list of inventorySnapshots that match the given filter.

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
api_instance = Infoplus.InventorySnapshotApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search inventorySnapshots by filter
    api_response = api_instance.get_inventory_snapshot_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventorySnapshotApi->get_inventory_snapshot_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[InventorySnapshot]**](InventorySnapshot.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_snapshot_by_id**
> InventorySnapshot get_inventory_snapshot_by_id(inventory_snapshot_id)

Get an inventorySnapshot by id

Returns the inventorySnapshot identified by the specified id.

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
api_instance = Infoplus.InventorySnapshotApi(Infoplus.ApiClient(configuration))
inventory_snapshot_id = 56 # int | Id of the inventorySnapshot to be returned.

try:
    # Get an inventorySnapshot by id
    api_response = api_instance.get_inventory_snapshot_by_id(inventory_snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventorySnapshotApi->get_inventory_snapshot_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_snapshot_id** | **int**| Id of the inventorySnapshot to be returned. | 

### Return type

[**InventorySnapshot**](InventorySnapshot.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_snapshot_files**
> get_inventory_snapshot_files(inventory_snapshot_id)

Get the files for an inventorySnapshot.

Get all existing inventorySnapshot files.

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
api_instance = Infoplus.InventorySnapshotApi(Infoplus.ApiClient(configuration))
inventory_snapshot_id = 56 # int | Id of the inventorySnapshot to get files for

try:
    # Get the files for an inventorySnapshot.
    api_instance.get_inventory_snapshot_files(inventory_snapshot_id)
except ApiException as e:
    print("Exception when calling InventorySnapshotApi->get_inventory_snapshot_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_snapshot_id** | **int**| Id of the inventorySnapshot to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_snapshot_tags**
> get_inventory_snapshot_tags(inventory_snapshot_id)

Get the tags for an inventorySnapshot.

Get all existing inventorySnapshot tags.

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
api_instance = Infoplus.InventorySnapshotApi(Infoplus.ApiClient(configuration))
inventory_snapshot_id = 56 # int | Id of the inventorySnapshot to get tags for

try:
    # Get the tags for an inventorySnapshot.
    api_instance.get_inventory_snapshot_tags(inventory_snapshot_id)
except ApiException as e:
    print("Exception when calling InventorySnapshotApi->get_inventory_snapshot_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_snapshot_id** | **int**| Id of the inventorySnapshot to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

