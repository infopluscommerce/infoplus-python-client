# Infoplus.WarehouseServiceTypeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_warehouse_service_type**](WarehouseServiceTypeApi.md#add_warehouse_service_type) | **POST** /beta/warehouseServiceType | Create a warehouseServiceType
[**add_warehouse_service_type_audit**](WarehouseServiceTypeApi.md#add_warehouse_service_type_audit) | **PUT** /beta/warehouseServiceType/{warehouseServiceTypeId}/audit/{warehouseServiceTypeAudit} | Add new audit for a warehouseServiceType
[**add_warehouse_service_type_file**](WarehouseServiceTypeApi.md#add_warehouse_service_type_file) | **POST** /beta/warehouseServiceType/{warehouseServiceTypeId}/file/{fileName} | Attach a file to a warehouseServiceType
[**add_warehouse_service_type_file_by_url**](WarehouseServiceTypeApi.md#add_warehouse_service_type_file_by_url) | **POST** /beta/warehouseServiceType/{warehouseServiceTypeId}/file | Attach a file to a warehouseServiceType by URL.
[**add_warehouse_service_type_tag**](WarehouseServiceTypeApi.md#add_warehouse_service_type_tag) | **PUT** /beta/warehouseServiceType/{warehouseServiceTypeId}/tag/{warehouseServiceTypeTag} | Add new tags for a warehouseServiceType.
[**delete_warehouse_service_type**](WarehouseServiceTypeApi.md#delete_warehouse_service_type) | **DELETE** /beta/warehouseServiceType/{warehouseServiceTypeId} | Delete a warehouseServiceType
[**delete_warehouse_service_type_file**](WarehouseServiceTypeApi.md#delete_warehouse_service_type_file) | **DELETE** /beta/warehouseServiceType/{warehouseServiceTypeId}/file/{fileId} | Delete a file for a warehouseServiceType.
[**delete_warehouse_service_type_tag**](WarehouseServiceTypeApi.md#delete_warehouse_service_type_tag) | **DELETE** /beta/warehouseServiceType/{warehouseServiceTypeId}/tag/{warehouseServiceTypeTag} | Delete a tag for a warehouseServiceType.
[**get_duplicate_warehouse_service_type_by_id**](WarehouseServiceTypeApi.md#get_duplicate_warehouse_service_type_by_id) | **GET** /beta/warehouseServiceType/duplicate/{warehouseServiceTypeId} | Get a duplicated a warehouseServiceType by id
[**get_warehouse_service_type_by_filter**](WarehouseServiceTypeApi.md#get_warehouse_service_type_by_filter) | **GET** /beta/warehouseServiceType/search | Search warehouseServiceTypes by filter
[**get_warehouse_service_type_by_id**](WarehouseServiceTypeApi.md#get_warehouse_service_type_by_id) | **GET** /beta/warehouseServiceType/{warehouseServiceTypeId} | Get a warehouseServiceType by id
[**get_warehouse_service_type_files**](WarehouseServiceTypeApi.md#get_warehouse_service_type_files) | **GET** /beta/warehouseServiceType/{warehouseServiceTypeId}/file | Get the files for a warehouseServiceType.
[**get_warehouse_service_type_tags**](WarehouseServiceTypeApi.md#get_warehouse_service_type_tags) | **GET** /beta/warehouseServiceType/{warehouseServiceTypeId}/tag | Get the tags for a warehouseServiceType.
[**update_warehouse_service_type**](WarehouseServiceTypeApi.md#update_warehouse_service_type) | **PUT** /beta/warehouseServiceType | Update a warehouseServiceType
[**update_warehouse_service_type_custom_fields**](WarehouseServiceTypeApi.md#update_warehouse_service_type_custom_fields) | **PUT** /beta/warehouseServiceType/customFields | Update a warehouseServiceType custom fields


# **add_warehouse_service_type**
> WarehouseServiceType add_warehouse_service_type(body)

Create a warehouseServiceType

Inserts a new warehouseServiceType using the specified data.

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
api_instance = Infoplus.WarehouseServiceTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.WarehouseServiceType() # WarehouseServiceType | WarehouseServiceType to be inserted.

try:
    # Create a warehouseServiceType
    api_response = api_instance.add_warehouse_service_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseServiceTypeApi->add_warehouse_service_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WarehouseServiceType**](WarehouseServiceType.md)| WarehouseServiceType to be inserted. | 

### Return type

[**WarehouseServiceType**](WarehouseServiceType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_warehouse_service_type_audit**
> add_warehouse_service_type_audit(warehouse_service_type_id, warehouse_service_type_audit)

Add new audit for a warehouseServiceType

Adds an audit to an existing warehouseServiceType.

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
api_instance = Infoplus.WarehouseServiceTypeApi(Infoplus.ApiClient(configuration))
warehouse_service_type_id = 56 # int | Id of the warehouseServiceType to add an audit to
warehouse_service_type_audit = 'warehouse_service_type_audit_example' # str | The audit to add

try:
    # Add new audit for a warehouseServiceType
    api_instance.add_warehouse_service_type_audit(warehouse_service_type_id, warehouse_service_type_audit)
except ApiException as e:
    print("Exception when calling WarehouseServiceTypeApi->add_warehouse_service_type_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_service_type_id** | **int**| Id of the warehouseServiceType to add an audit to | 
 **warehouse_service_type_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_warehouse_service_type_file**
> add_warehouse_service_type_file(warehouse_service_type_id, file_name)

Attach a file to a warehouseServiceType

Adds a file to an existing warehouseServiceType.

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
api_instance = Infoplus.WarehouseServiceTypeApi(Infoplus.ApiClient(configuration))
warehouse_service_type_id = 56 # int | Id of the warehouseServiceType to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a warehouseServiceType
    api_instance.add_warehouse_service_type_file(warehouse_service_type_id, file_name)
except ApiException as e:
    print("Exception when calling WarehouseServiceTypeApi->add_warehouse_service_type_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_service_type_id** | **int**| Id of the warehouseServiceType to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_warehouse_service_type_file_by_url**
> add_warehouse_service_type_file_by_url(body, warehouse_service_type_id)

Attach a file to a warehouseServiceType by URL.

Adds a file to an existing warehouseServiceType by URL.

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
api_instance = Infoplus.WarehouseServiceTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
warehouse_service_type_id = 56 # int | Id of the warehouseServiceType to add an file to

try:
    # Attach a file to a warehouseServiceType by URL.
    api_instance.add_warehouse_service_type_file_by_url(body, warehouse_service_type_id)
except ApiException as e:
    print("Exception when calling WarehouseServiceTypeApi->add_warehouse_service_type_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **warehouse_service_type_id** | **int**| Id of the warehouseServiceType to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_warehouse_service_type_tag**
> add_warehouse_service_type_tag(warehouse_service_type_id, warehouse_service_type_tag)

Add new tags for a warehouseServiceType.

Adds a tag to an existing warehouseServiceType.

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
api_instance = Infoplus.WarehouseServiceTypeApi(Infoplus.ApiClient(configuration))
warehouse_service_type_id = 56 # int | Id of the warehouseServiceType to add a tag to
warehouse_service_type_tag = 'warehouse_service_type_tag_example' # str | The tag to add

try:
    # Add new tags for a warehouseServiceType.
    api_instance.add_warehouse_service_type_tag(warehouse_service_type_id, warehouse_service_type_tag)
except ApiException as e:
    print("Exception when calling WarehouseServiceTypeApi->add_warehouse_service_type_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_service_type_id** | **int**| Id of the warehouseServiceType to add a tag to | 
 **warehouse_service_type_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_warehouse_service_type**
> delete_warehouse_service_type(warehouse_service_type_id)

Delete a warehouseServiceType

Deletes the warehouseServiceType identified by the specified id.

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
api_instance = Infoplus.WarehouseServiceTypeApi(Infoplus.ApiClient(configuration))
warehouse_service_type_id = 56 # int | Id of the warehouseServiceType to be deleted.

try:
    # Delete a warehouseServiceType
    api_instance.delete_warehouse_service_type(warehouse_service_type_id)
except ApiException as e:
    print("Exception when calling WarehouseServiceTypeApi->delete_warehouse_service_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_service_type_id** | **int**| Id of the warehouseServiceType to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_warehouse_service_type_file**
> delete_warehouse_service_type_file(warehouse_service_type_id, file_id)

Delete a file for a warehouseServiceType.

Deletes an existing warehouseServiceType file using the specified data.

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
api_instance = Infoplus.WarehouseServiceTypeApi(Infoplus.ApiClient(configuration))
warehouse_service_type_id = 56 # int | Id of the warehouseServiceType to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a warehouseServiceType.
    api_instance.delete_warehouse_service_type_file(warehouse_service_type_id, file_id)
except ApiException as e:
    print("Exception when calling WarehouseServiceTypeApi->delete_warehouse_service_type_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_service_type_id** | **int**| Id of the warehouseServiceType to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_warehouse_service_type_tag**
> delete_warehouse_service_type_tag(warehouse_service_type_id, warehouse_service_type_tag)

Delete a tag for a warehouseServiceType.

Deletes an existing warehouseServiceType tag using the specified data.

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
api_instance = Infoplus.WarehouseServiceTypeApi(Infoplus.ApiClient(configuration))
warehouse_service_type_id = 56 # int | Id of the warehouseServiceType to remove tag from
warehouse_service_type_tag = 'warehouse_service_type_tag_example' # str | The tag to delete

try:
    # Delete a tag for a warehouseServiceType.
    api_instance.delete_warehouse_service_type_tag(warehouse_service_type_id, warehouse_service_type_tag)
except ApiException as e:
    print("Exception when calling WarehouseServiceTypeApi->delete_warehouse_service_type_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_service_type_id** | **int**| Id of the warehouseServiceType to remove tag from | 
 **warehouse_service_type_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_warehouse_service_type_by_id**
> WarehouseServiceType get_duplicate_warehouse_service_type_by_id(warehouse_service_type_id)

Get a duplicated a warehouseServiceType by id

Returns a duplicated warehouseServiceType identified by the specified id.

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
api_instance = Infoplus.WarehouseServiceTypeApi(Infoplus.ApiClient(configuration))
warehouse_service_type_id = 56 # int | Id of the warehouseServiceType to be duplicated.

try:
    # Get a duplicated a warehouseServiceType by id
    api_response = api_instance.get_duplicate_warehouse_service_type_by_id(warehouse_service_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseServiceTypeApi->get_duplicate_warehouse_service_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_service_type_id** | **int**| Id of the warehouseServiceType to be duplicated. | 

### Return type

[**WarehouseServiceType**](WarehouseServiceType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_service_type_by_filter**
> list[WarehouseServiceType] get_warehouse_service_type_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search warehouseServiceTypes by filter

Returns the list of warehouseServiceTypes that match the given filter.

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
api_instance = Infoplus.WarehouseServiceTypeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search warehouseServiceTypes by filter
    api_response = api_instance.get_warehouse_service_type_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseServiceTypeApi->get_warehouse_service_type_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[WarehouseServiceType]**](WarehouseServiceType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_service_type_by_id**
> WarehouseServiceType get_warehouse_service_type_by_id(warehouse_service_type_id)

Get a warehouseServiceType by id

Returns the warehouseServiceType identified by the specified id.

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
api_instance = Infoplus.WarehouseServiceTypeApi(Infoplus.ApiClient(configuration))
warehouse_service_type_id = 56 # int | Id of the warehouseServiceType to be returned.

try:
    # Get a warehouseServiceType by id
    api_response = api_instance.get_warehouse_service_type_by_id(warehouse_service_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseServiceTypeApi->get_warehouse_service_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_service_type_id** | **int**| Id of the warehouseServiceType to be returned. | 

### Return type

[**WarehouseServiceType**](WarehouseServiceType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_service_type_files**
> get_warehouse_service_type_files(warehouse_service_type_id)

Get the files for a warehouseServiceType.

Get all existing warehouseServiceType files.

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
api_instance = Infoplus.WarehouseServiceTypeApi(Infoplus.ApiClient(configuration))
warehouse_service_type_id = 56 # int | Id of the warehouseServiceType to get files for

try:
    # Get the files for a warehouseServiceType.
    api_instance.get_warehouse_service_type_files(warehouse_service_type_id)
except ApiException as e:
    print("Exception when calling WarehouseServiceTypeApi->get_warehouse_service_type_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_service_type_id** | **int**| Id of the warehouseServiceType to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_service_type_tags**
> get_warehouse_service_type_tags(warehouse_service_type_id)

Get the tags for a warehouseServiceType.

Get all existing warehouseServiceType tags.

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
api_instance = Infoplus.WarehouseServiceTypeApi(Infoplus.ApiClient(configuration))
warehouse_service_type_id = 56 # int | Id of the warehouseServiceType to get tags for

try:
    # Get the tags for a warehouseServiceType.
    api_instance.get_warehouse_service_type_tags(warehouse_service_type_id)
except ApiException as e:
    print("Exception when calling WarehouseServiceTypeApi->get_warehouse_service_type_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_service_type_id** | **int**| Id of the warehouseServiceType to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_warehouse_service_type**
> update_warehouse_service_type(body)

Update a warehouseServiceType

Updates an existing warehouseServiceType using the specified data.

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
api_instance = Infoplus.WarehouseServiceTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.WarehouseServiceType() # WarehouseServiceType | WarehouseServiceType to be updated.

try:
    # Update a warehouseServiceType
    api_instance.update_warehouse_service_type(body)
except ApiException as e:
    print("Exception when calling WarehouseServiceTypeApi->update_warehouse_service_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WarehouseServiceType**](WarehouseServiceType.md)| WarehouseServiceType to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_warehouse_service_type_custom_fields**
> update_warehouse_service_type_custom_fields(body)

Update a warehouseServiceType custom fields

Updates an existing warehouseServiceType custom fields using the specified data.

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
api_instance = Infoplus.WarehouseServiceTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.WarehouseServiceType() # WarehouseServiceType | WarehouseServiceType to be updated.

try:
    # Update a warehouseServiceType custom fields
    api_instance.update_warehouse_service_type_custom_fields(body)
except ApiException as e:
    print("Exception when calling WarehouseServiceTypeApi->update_warehouse_service_type_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WarehouseServiceType**](WarehouseServiceType.md)| WarehouseServiceType to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

