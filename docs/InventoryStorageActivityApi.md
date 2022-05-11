# Infoplus.InventoryStorageActivityApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_inventory_storage_activity**](InventoryStorageActivityApi.md#add_inventory_storage_activity) | **POST** /v3.0/inventoryStorageActivity | Create an inventoryStorageActivity
[**add_inventory_storage_activity_audit**](InventoryStorageActivityApi.md#add_inventory_storage_activity_audit) | **PUT** /v3.0/inventoryStorageActivity/{inventoryStorageActivityId}/audit/{inventoryStorageActivityAudit} | Add new audit for an inventoryStorageActivity
[**add_inventory_storage_activity_file**](InventoryStorageActivityApi.md#add_inventory_storage_activity_file) | **POST** /v3.0/inventoryStorageActivity/{inventoryStorageActivityId}/file/{fileName} | Attach a file to an inventoryStorageActivity
[**add_inventory_storage_activity_file_by_url**](InventoryStorageActivityApi.md#add_inventory_storage_activity_file_by_url) | **POST** /v3.0/inventoryStorageActivity/{inventoryStorageActivityId}/file | Attach a file to an inventoryStorageActivity by URL.
[**add_inventory_storage_activity_tag**](InventoryStorageActivityApi.md#add_inventory_storage_activity_tag) | **PUT** /v3.0/inventoryStorageActivity/{inventoryStorageActivityId}/tag/{inventoryStorageActivityTag} | Add new tags for an inventoryStorageActivity.
[**delete_inventory_storage_activity**](InventoryStorageActivityApi.md#delete_inventory_storage_activity) | **DELETE** /v3.0/inventoryStorageActivity/{inventoryStorageActivityId} | Delete an inventoryStorageActivity
[**delete_inventory_storage_activity_file**](InventoryStorageActivityApi.md#delete_inventory_storage_activity_file) | **DELETE** /v3.0/inventoryStorageActivity/{inventoryStorageActivityId}/file/{fileId} | Delete a file for an inventoryStorageActivity.
[**delete_inventory_storage_activity_tag**](InventoryStorageActivityApi.md#delete_inventory_storage_activity_tag) | **DELETE** /v3.0/inventoryStorageActivity/{inventoryStorageActivityId}/tag/{inventoryStorageActivityTag} | Delete a tag for an inventoryStorageActivity.
[**get_duplicate_inventory_storage_activity_by_id**](InventoryStorageActivityApi.md#get_duplicate_inventory_storage_activity_by_id) | **GET** /v3.0/inventoryStorageActivity/duplicate/{inventoryStorageActivityId} | Get a duplicated an inventoryStorageActivity by id
[**get_inventory_storage_activity_by_filter**](InventoryStorageActivityApi.md#get_inventory_storage_activity_by_filter) | **GET** /v3.0/inventoryStorageActivity/search | Search inventoryStorageActivitys by filter
[**get_inventory_storage_activity_by_id**](InventoryStorageActivityApi.md#get_inventory_storage_activity_by_id) | **GET** /v3.0/inventoryStorageActivity/{inventoryStorageActivityId} | Get an inventoryStorageActivity by id
[**get_inventory_storage_activity_files**](InventoryStorageActivityApi.md#get_inventory_storage_activity_files) | **GET** /v3.0/inventoryStorageActivity/{inventoryStorageActivityId}/file | Get the files for an inventoryStorageActivity.
[**get_inventory_storage_activity_tags**](InventoryStorageActivityApi.md#get_inventory_storage_activity_tags) | **GET** /v3.0/inventoryStorageActivity/{inventoryStorageActivityId}/tag | Get the tags for an inventoryStorageActivity.
[**update_inventory_storage_activity**](InventoryStorageActivityApi.md#update_inventory_storage_activity) | **PUT** /v3.0/inventoryStorageActivity | Update an inventoryStorageActivity


# **add_inventory_storage_activity**
> InventoryStorageActivity add_inventory_storage_activity(body)

Create an inventoryStorageActivity

Inserts a new inventoryStorageActivity using the specified data.

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
api_instance = Infoplus.InventoryStorageActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.InventoryStorageActivity() # InventoryStorageActivity | InventoryStorageActivity to be inserted.

try:
    # Create an inventoryStorageActivity
    api_response = api_instance.add_inventory_storage_activity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryStorageActivityApi->add_inventory_storage_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryStorageActivity**](InventoryStorageActivity.md)| InventoryStorageActivity to be inserted. | 

### Return type

[**InventoryStorageActivity**](InventoryStorageActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_inventory_storage_activity_audit**
> add_inventory_storage_activity_audit(inventory_storage_activity_id, inventory_storage_activity_audit)

Add new audit for an inventoryStorageActivity

Adds an audit to an existing inventoryStorageActivity.

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
api_instance = Infoplus.InventoryStorageActivityApi(Infoplus.ApiClient(configuration))
inventory_storage_activity_id = 56 # int | Id of the inventoryStorageActivity to add an audit to
inventory_storage_activity_audit = 'inventory_storage_activity_audit_example' # str | The audit to add

try:
    # Add new audit for an inventoryStorageActivity
    api_instance.add_inventory_storage_activity_audit(inventory_storage_activity_id, inventory_storage_activity_audit)
except ApiException as e:
    print("Exception when calling InventoryStorageActivityApi->add_inventory_storage_activity_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_storage_activity_id** | **int**| Id of the inventoryStorageActivity to add an audit to | 
 **inventory_storage_activity_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_inventory_storage_activity_file**
> add_inventory_storage_activity_file(inventory_storage_activity_id, file_name)

Attach a file to an inventoryStorageActivity

Adds a file to an existing inventoryStorageActivity.

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
api_instance = Infoplus.InventoryStorageActivityApi(Infoplus.ApiClient(configuration))
inventory_storage_activity_id = 56 # int | Id of the inventoryStorageActivity to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an inventoryStorageActivity
    api_instance.add_inventory_storage_activity_file(inventory_storage_activity_id, file_name)
except ApiException as e:
    print("Exception when calling InventoryStorageActivityApi->add_inventory_storage_activity_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_storage_activity_id** | **int**| Id of the inventoryStorageActivity to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_inventory_storage_activity_file_by_url**
> add_inventory_storage_activity_file_by_url(body, inventory_storage_activity_id)

Attach a file to an inventoryStorageActivity by URL.

Adds a file to an existing inventoryStorageActivity by URL.

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
api_instance = Infoplus.InventoryStorageActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
inventory_storage_activity_id = 56 # int | Id of the inventoryStorageActivity to add an file to

try:
    # Attach a file to an inventoryStorageActivity by URL.
    api_instance.add_inventory_storage_activity_file_by_url(body, inventory_storage_activity_id)
except ApiException as e:
    print("Exception when calling InventoryStorageActivityApi->add_inventory_storage_activity_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **inventory_storage_activity_id** | **int**| Id of the inventoryStorageActivity to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_inventory_storage_activity_tag**
> add_inventory_storage_activity_tag(inventory_storage_activity_id, inventory_storage_activity_tag)

Add new tags for an inventoryStorageActivity.

Adds a tag to an existing inventoryStorageActivity.

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
api_instance = Infoplus.InventoryStorageActivityApi(Infoplus.ApiClient(configuration))
inventory_storage_activity_id = 56 # int | Id of the inventoryStorageActivity to add a tag to
inventory_storage_activity_tag = 'inventory_storage_activity_tag_example' # str | The tag to add

try:
    # Add new tags for an inventoryStorageActivity.
    api_instance.add_inventory_storage_activity_tag(inventory_storage_activity_id, inventory_storage_activity_tag)
except ApiException as e:
    print("Exception when calling InventoryStorageActivityApi->add_inventory_storage_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_storage_activity_id** | **int**| Id of the inventoryStorageActivity to add a tag to | 
 **inventory_storage_activity_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inventory_storage_activity**
> delete_inventory_storage_activity(inventory_storage_activity_id)

Delete an inventoryStorageActivity

Deletes the inventoryStorageActivity identified by the specified id.

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
api_instance = Infoplus.InventoryStorageActivityApi(Infoplus.ApiClient(configuration))
inventory_storage_activity_id = 56 # int | Id of the inventoryStorageActivity to be deleted.

try:
    # Delete an inventoryStorageActivity
    api_instance.delete_inventory_storage_activity(inventory_storage_activity_id)
except ApiException as e:
    print("Exception when calling InventoryStorageActivityApi->delete_inventory_storage_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_storage_activity_id** | **int**| Id of the inventoryStorageActivity to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inventory_storage_activity_file**
> delete_inventory_storage_activity_file(inventory_storage_activity_id, file_id)

Delete a file for an inventoryStorageActivity.

Deletes an existing inventoryStorageActivity file using the specified data.

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
api_instance = Infoplus.InventoryStorageActivityApi(Infoplus.ApiClient(configuration))
inventory_storage_activity_id = 56 # int | Id of the inventoryStorageActivity to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an inventoryStorageActivity.
    api_instance.delete_inventory_storage_activity_file(inventory_storage_activity_id, file_id)
except ApiException as e:
    print("Exception when calling InventoryStorageActivityApi->delete_inventory_storage_activity_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_storage_activity_id** | **int**| Id of the inventoryStorageActivity to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inventory_storage_activity_tag**
> delete_inventory_storage_activity_tag(inventory_storage_activity_id, inventory_storage_activity_tag)

Delete a tag for an inventoryStorageActivity.

Deletes an existing inventoryStorageActivity tag using the specified data.

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
api_instance = Infoplus.InventoryStorageActivityApi(Infoplus.ApiClient(configuration))
inventory_storage_activity_id = 56 # int | Id of the inventoryStorageActivity to remove tag from
inventory_storage_activity_tag = 'inventory_storage_activity_tag_example' # str | The tag to delete

try:
    # Delete a tag for an inventoryStorageActivity.
    api_instance.delete_inventory_storage_activity_tag(inventory_storage_activity_id, inventory_storage_activity_tag)
except ApiException as e:
    print("Exception when calling InventoryStorageActivityApi->delete_inventory_storage_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_storage_activity_id** | **int**| Id of the inventoryStorageActivity to remove tag from | 
 **inventory_storage_activity_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_inventory_storage_activity_by_id**
> InventoryStorageActivity get_duplicate_inventory_storage_activity_by_id(inventory_storage_activity_id)

Get a duplicated an inventoryStorageActivity by id

Returns a duplicated inventoryStorageActivity identified by the specified id.

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
api_instance = Infoplus.InventoryStorageActivityApi(Infoplus.ApiClient(configuration))
inventory_storage_activity_id = 56 # int | Id of the inventoryStorageActivity to be duplicated.

try:
    # Get a duplicated an inventoryStorageActivity by id
    api_response = api_instance.get_duplicate_inventory_storage_activity_by_id(inventory_storage_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryStorageActivityApi->get_duplicate_inventory_storage_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_storage_activity_id** | **int**| Id of the inventoryStorageActivity to be duplicated. | 

### Return type

[**InventoryStorageActivity**](InventoryStorageActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_storage_activity_by_filter**
> list[InventoryStorageActivity] get_inventory_storage_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search inventoryStorageActivitys by filter

Returns the list of inventoryStorageActivitys that match the given filter.

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
api_instance = Infoplus.InventoryStorageActivityApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search inventoryStorageActivitys by filter
    api_response = api_instance.get_inventory_storage_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryStorageActivityApi->get_inventory_storage_activity_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[InventoryStorageActivity]**](InventoryStorageActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_storage_activity_by_id**
> InventoryStorageActivity get_inventory_storage_activity_by_id(inventory_storage_activity_id)

Get an inventoryStorageActivity by id

Returns the inventoryStorageActivity identified by the specified id.

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
api_instance = Infoplus.InventoryStorageActivityApi(Infoplus.ApiClient(configuration))
inventory_storage_activity_id = 56 # int | Id of the inventoryStorageActivity to be returned.

try:
    # Get an inventoryStorageActivity by id
    api_response = api_instance.get_inventory_storage_activity_by_id(inventory_storage_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryStorageActivityApi->get_inventory_storage_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_storage_activity_id** | **int**| Id of the inventoryStorageActivity to be returned. | 

### Return type

[**InventoryStorageActivity**](InventoryStorageActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_storage_activity_files**
> get_inventory_storage_activity_files(inventory_storage_activity_id)

Get the files for an inventoryStorageActivity.

Get all existing inventoryStorageActivity files.

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
api_instance = Infoplus.InventoryStorageActivityApi(Infoplus.ApiClient(configuration))
inventory_storage_activity_id = 56 # int | Id of the inventoryStorageActivity to get files for

try:
    # Get the files for an inventoryStorageActivity.
    api_instance.get_inventory_storage_activity_files(inventory_storage_activity_id)
except ApiException as e:
    print("Exception when calling InventoryStorageActivityApi->get_inventory_storage_activity_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_storage_activity_id** | **int**| Id of the inventoryStorageActivity to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_storage_activity_tags**
> get_inventory_storage_activity_tags(inventory_storage_activity_id)

Get the tags for an inventoryStorageActivity.

Get all existing inventoryStorageActivity tags.

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
api_instance = Infoplus.InventoryStorageActivityApi(Infoplus.ApiClient(configuration))
inventory_storage_activity_id = 56 # int | Id of the inventoryStorageActivity to get tags for

try:
    # Get the tags for an inventoryStorageActivity.
    api_instance.get_inventory_storage_activity_tags(inventory_storage_activity_id)
except ApiException as e:
    print("Exception when calling InventoryStorageActivityApi->get_inventory_storage_activity_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_storage_activity_id** | **int**| Id of the inventoryStorageActivity to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inventory_storage_activity**
> update_inventory_storage_activity(body)

Update an inventoryStorageActivity

Updates an existing inventoryStorageActivity using the specified data.

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
api_instance = Infoplus.InventoryStorageActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.InventoryStorageActivity() # InventoryStorageActivity | InventoryStorageActivity to be updated.

try:
    # Update an inventoryStorageActivity
    api_instance.update_inventory_storage_activity(body)
except ApiException as e:
    print("Exception when calling InventoryStorageActivityApi->update_inventory_storage_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryStorageActivity**](InventoryStorageActivity.md)| InventoryStorageActivity to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

