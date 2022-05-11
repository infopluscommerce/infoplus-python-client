# Infoplus.WarehouseDocumentTypeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_warehouse_document_type_audit**](WarehouseDocumentTypeApi.md#add_warehouse_document_type_audit) | **PUT** /v3.0/warehouseDocumentType/{warehouseDocumentTypeId}/audit/{warehouseDocumentTypeAudit} | Add new audit for a warehouseDocumentType
[**add_warehouse_document_type_file**](WarehouseDocumentTypeApi.md#add_warehouse_document_type_file) | **POST** /v3.0/warehouseDocumentType/{warehouseDocumentTypeId}/file/{fileName} | Attach a file to a warehouseDocumentType
[**add_warehouse_document_type_file_by_url**](WarehouseDocumentTypeApi.md#add_warehouse_document_type_file_by_url) | **POST** /v3.0/warehouseDocumentType/{warehouseDocumentTypeId}/file | Attach a file to a warehouseDocumentType by URL.
[**add_warehouse_document_type_tag**](WarehouseDocumentTypeApi.md#add_warehouse_document_type_tag) | **PUT** /v3.0/warehouseDocumentType/{warehouseDocumentTypeId}/tag/{warehouseDocumentTypeTag} | Add new tags for a warehouseDocumentType.
[**delete_warehouse_document_type_file**](WarehouseDocumentTypeApi.md#delete_warehouse_document_type_file) | **DELETE** /v3.0/warehouseDocumentType/{warehouseDocumentTypeId}/file/{fileId} | Delete a file for a warehouseDocumentType.
[**delete_warehouse_document_type_tag**](WarehouseDocumentTypeApi.md#delete_warehouse_document_type_tag) | **DELETE** /v3.0/warehouseDocumentType/{warehouseDocumentTypeId}/tag/{warehouseDocumentTypeTag} | Delete a tag for a warehouseDocumentType.
[**get_duplicate_warehouse_document_type_by_id**](WarehouseDocumentTypeApi.md#get_duplicate_warehouse_document_type_by_id) | **GET** /v3.0/warehouseDocumentType/duplicate/{warehouseDocumentTypeId} | Get a duplicated a warehouseDocumentType by id
[**get_warehouse_document_type_by_filter**](WarehouseDocumentTypeApi.md#get_warehouse_document_type_by_filter) | **GET** /v3.0/warehouseDocumentType/search | Search warehouseDocumentTypes by filter
[**get_warehouse_document_type_by_id**](WarehouseDocumentTypeApi.md#get_warehouse_document_type_by_id) | **GET** /v3.0/warehouseDocumentType/{warehouseDocumentTypeId} | Get a warehouseDocumentType by id
[**get_warehouse_document_type_files**](WarehouseDocumentTypeApi.md#get_warehouse_document_type_files) | **GET** /v3.0/warehouseDocumentType/{warehouseDocumentTypeId}/file | Get the files for a warehouseDocumentType.
[**get_warehouse_document_type_tags**](WarehouseDocumentTypeApi.md#get_warehouse_document_type_tags) | **GET** /v3.0/warehouseDocumentType/{warehouseDocumentTypeId}/tag | Get the tags for a warehouseDocumentType.


# **add_warehouse_document_type_audit**
> add_warehouse_document_type_audit(warehouse_document_type_id, warehouse_document_type_audit)

Add new audit for a warehouseDocumentType

Adds an audit to an existing warehouseDocumentType.

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
api_instance = Infoplus.WarehouseDocumentTypeApi(Infoplus.ApiClient(configuration))
warehouse_document_type_id = 56 # int | Id of the warehouseDocumentType to add an audit to
warehouse_document_type_audit = 'warehouse_document_type_audit_example' # str | The audit to add

try:
    # Add new audit for a warehouseDocumentType
    api_instance.add_warehouse_document_type_audit(warehouse_document_type_id, warehouse_document_type_audit)
except ApiException as e:
    print("Exception when calling WarehouseDocumentTypeApi->add_warehouse_document_type_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_document_type_id** | **int**| Id of the warehouseDocumentType to add an audit to | 
 **warehouse_document_type_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_warehouse_document_type_file**
> add_warehouse_document_type_file(warehouse_document_type_id, file_name)

Attach a file to a warehouseDocumentType

Adds a file to an existing warehouseDocumentType.

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
api_instance = Infoplus.WarehouseDocumentTypeApi(Infoplus.ApiClient(configuration))
warehouse_document_type_id = 56 # int | Id of the warehouseDocumentType to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a warehouseDocumentType
    api_instance.add_warehouse_document_type_file(warehouse_document_type_id, file_name)
except ApiException as e:
    print("Exception when calling WarehouseDocumentTypeApi->add_warehouse_document_type_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_document_type_id** | **int**| Id of the warehouseDocumentType to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_warehouse_document_type_file_by_url**
> add_warehouse_document_type_file_by_url(body, warehouse_document_type_id)

Attach a file to a warehouseDocumentType by URL.

Adds a file to an existing warehouseDocumentType by URL.

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
api_instance = Infoplus.WarehouseDocumentTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
warehouse_document_type_id = 56 # int | Id of the warehouseDocumentType to add an file to

try:
    # Attach a file to a warehouseDocumentType by URL.
    api_instance.add_warehouse_document_type_file_by_url(body, warehouse_document_type_id)
except ApiException as e:
    print("Exception when calling WarehouseDocumentTypeApi->add_warehouse_document_type_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **warehouse_document_type_id** | **int**| Id of the warehouseDocumentType to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_warehouse_document_type_tag**
> add_warehouse_document_type_tag(warehouse_document_type_id, warehouse_document_type_tag)

Add new tags for a warehouseDocumentType.

Adds a tag to an existing warehouseDocumentType.

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
api_instance = Infoplus.WarehouseDocumentTypeApi(Infoplus.ApiClient(configuration))
warehouse_document_type_id = 56 # int | Id of the warehouseDocumentType to add a tag to
warehouse_document_type_tag = 'warehouse_document_type_tag_example' # str | The tag to add

try:
    # Add new tags for a warehouseDocumentType.
    api_instance.add_warehouse_document_type_tag(warehouse_document_type_id, warehouse_document_type_tag)
except ApiException as e:
    print("Exception when calling WarehouseDocumentTypeApi->add_warehouse_document_type_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_document_type_id** | **int**| Id of the warehouseDocumentType to add a tag to | 
 **warehouse_document_type_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_warehouse_document_type_file**
> delete_warehouse_document_type_file(warehouse_document_type_id, file_id)

Delete a file for a warehouseDocumentType.

Deletes an existing warehouseDocumentType file using the specified data.

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
api_instance = Infoplus.WarehouseDocumentTypeApi(Infoplus.ApiClient(configuration))
warehouse_document_type_id = 56 # int | Id of the warehouseDocumentType to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a warehouseDocumentType.
    api_instance.delete_warehouse_document_type_file(warehouse_document_type_id, file_id)
except ApiException as e:
    print("Exception when calling WarehouseDocumentTypeApi->delete_warehouse_document_type_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_document_type_id** | **int**| Id of the warehouseDocumentType to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_warehouse_document_type_tag**
> delete_warehouse_document_type_tag(warehouse_document_type_id, warehouse_document_type_tag)

Delete a tag for a warehouseDocumentType.

Deletes an existing warehouseDocumentType tag using the specified data.

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
api_instance = Infoplus.WarehouseDocumentTypeApi(Infoplus.ApiClient(configuration))
warehouse_document_type_id = 56 # int | Id of the warehouseDocumentType to remove tag from
warehouse_document_type_tag = 'warehouse_document_type_tag_example' # str | The tag to delete

try:
    # Delete a tag for a warehouseDocumentType.
    api_instance.delete_warehouse_document_type_tag(warehouse_document_type_id, warehouse_document_type_tag)
except ApiException as e:
    print("Exception when calling WarehouseDocumentTypeApi->delete_warehouse_document_type_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_document_type_id** | **int**| Id of the warehouseDocumentType to remove tag from | 
 **warehouse_document_type_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_warehouse_document_type_by_id**
> WarehouseDocumentType get_duplicate_warehouse_document_type_by_id(warehouse_document_type_id)

Get a duplicated a warehouseDocumentType by id

Returns a duplicated warehouseDocumentType identified by the specified id.

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
api_instance = Infoplus.WarehouseDocumentTypeApi(Infoplus.ApiClient(configuration))
warehouse_document_type_id = 56 # int | Id of the warehouseDocumentType to be duplicated.

try:
    # Get a duplicated a warehouseDocumentType by id
    api_response = api_instance.get_duplicate_warehouse_document_type_by_id(warehouse_document_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseDocumentTypeApi->get_duplicate_warehouse_document_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_document_type_id** | **int**| Id of the warehouseDocumentType to be duplicated. | 

### Return type

[**WarehouseDocumentType**](WarehouseDocumentType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_document_type_by_filter**
> list[WarehouseDocumentType] get_warehouse_document_type_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search warehouseDocumentTypes by filter

Returns the list of warehouseDocumentTypes that match the given filter.

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
api_instance = Infoplus.WarehouseDocumentTypeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search warehouseDocumentTypes by filter
    api_response = api_instance.get_warehouse_document_type_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseDocumentTypeApi->get_warehouse_document_type_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[WarehouseDocumentType]**](WarehouseDocumentType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_document_type_by_id**
> WarehouseDocumentType get_warehouse_document_type_by_id(warehouse_document_type_id)

Get a warehouseDocumentType by id

Returns the warehouseDocumentType identified by the specified id.

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
api_instance = Infoplus.WarehouseDocumentTypeApi(Infoplus.ApiClient(configuration))
warehouse_document_type_id = 56 # int | Id of the warehouseDocumentType to be returned.

try:
    # Get a warehouseDocumentType by id
    api_response = api_instance.get_warehouse_document_type_by_id(warehouse_document_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseDocumentTypeApi->get_warehouse_document_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_document_type_id** | **int**| Id of the warehouseDocumentType to be returned. | 

### Return type

[**WarehouseDocumentType**](WarehouseDocumentType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_document_type_files**
> get_warehouse_document_type_files(warehouse_document_type_id)

Get the files for a warehouseDocumentType.

Get all existing warehouseDocumentType files.

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
api_instance = Infoplus.WarehouseDocumentTypeApi(Infoplus.ApiClient(configuration))
warehouse_document_type_id = 56 # int | Id of the warehouseDocumentType to get files for

try:
    # Get the files for a warehouseDocumentType.
    api_instance.get_warehouse_document_type_files(warehouse_document_type_id)
except ApiException as e:
    print("Exception when calling WarehouseDocumentTypeApi->get_warehouse_document_type_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_document_type_id** | **int**| Id of the warehouseDocumentType to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_document_type_tags**
> get_warehouse_document_type_tags(warehouse_document_type_id)

Get the tags for a warehouseDocumentType.

Get all existing warehouseDocumentType tags.

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
api_instance = Infoplus.WarehouseDocumentTypeApi(Infoplus.ApiClient(configuration))
warehouse_document_type_id = 56 # int | Id of the warehouseDocumentType to get tags for

try:
    # Get the tags for a warehouseDocumentType.
    api_instance.get_warehouse_document_type_tags(warehouse_document_type_id)
except ApiException as e:
    print("Exception when calling WarehouseDocumentTypeApi->get_warehouse_document_type_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_document_type_id** | **int**| Id of the warehouseDocumentType to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

