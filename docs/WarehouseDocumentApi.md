# Infoplus.WarehouseDocumentApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_warehouse_document_audit**](WarehouseDocumentApi.md#add_warehouse_document_audit) | **PUT** /beta/warehouseDocument/{warehouseDocumentId}/audit/{warehouseDocumentAudit} | Add new audit for a warehouseDocument
[**add_warehouse_document_tag**](WarehouseDocumentApi.md#add_warehouse_document_tag) | **PUT** /beta/warehouseDocument/{warehouseDocumentId}/tag/{warehouseDocumentTag} | Add new tags for a warehouseDocument.
[**delete_warehouse_document_tag**](WarehouseDocumentApi.md#delete_warehouse_document_tag) | **DELETE** /beta/warehouseDocument/{warehouseDocumentId}/tag/{warehouseDocumentTag} | Delete a tag for a warehouseDocument.
[**get_duplicate_warehouse_document_by_id**](WarehouseDocumentApi.md#get_duplicate_warehouse_document_by_id) | **GET** /beta/warehouseDocument/duplicate/{warehouseDocumentId} | Get a duplicated a warehouseDocument by id
[**get_warehouse_document_by_filter**](WarehouseDocumentApi.md#get_warehouse_document_by_filter) | **GET** /beta/warehouseDocument/search | Search warehouseDocuments by filter
[**get_warehouse_document_by_id**](WarehouseDocumentApi.md#get_warehouse_document_by_id) | **GET** /beta/warehouseDocument/{warehouseDocumentId} | Get a warehouseDocument by id
[**get_warehouse_document_tags**](WarehouseDocumentApi.md#get_warehouse_document_tags) | **GET** /beta/warehouseDocument/{warehouseDocumentId}/tag | Get the tags for a warehouseDocument.
[**update_warehouse_document_custom_fields**](WarehouseDocumentApi.md#update_warehouse_document_custom_fields) | **PUT** /beta/warehouseDocument/customFields | Update a warehouseDocument custom fields


# **add_warehouse_document_audit**
> add_warehouse_document_audit(warehouse_document_id, warehouse_document_audit)

Add new audit for a warehouseDocument

Adds an audit to an existing warehouseDocument.

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
api_instance = Infoplus.WarehouseDocumentApi(Infoplus.ApiClient(configuration))
warehouse_document_id = 56 # int | Id of the warehouseDocument to add an audit to
warehouse_document_audit = 'warehouse_document_audit_example' # str | The audit to add

try:
    # Add new audit for a warehouseDocument
    api_instance.add_warehouse_document_audit(warehouse_document_id, warehouse_document_audit)
except ApiException as e:
    print("Exception when calling WarehouseDocumentApi->add_warehouse_document_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_document_id** | **int**| Id of the warehouseDocument to add an audit to | 
 **warehouse_document_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_warehouse_document_tag**
> add_warehouse_document_tag(warehouse_document_id, warehouse_document_tag)

Add new tags for a warehouseDocument.

Adds a tag to an existing warehouseDocument.

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
api_instance = Infoplus.WarehouseDocumentApi(Infoplus.ApiClient(configuration))
warehouse_document_id = 56 # int | Id of the warehouseDocument to add a tag to
warehouse_document_tag = 'warehouse_document_tag_example' # str | The tag to add

try:
    # Add new tags for a warehouseDocument.
    api_instance.add_warehouse_document_tag(warehouse_document_id, warehouse_document_tag)
except ApiException as e:
    print("Exception when calling WarehouseDocumentApi->add_warehouse_document_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_document_id** | **int**| Id of the warehouseDocument to add a tag to | 
 **warehouse_document_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_warehouse_document_tag**
> delete_warehouse_document_tag(warehouse_document_id, warehouse_document_tag)

Delete a tag for a warehouseDocument.

Deletes an existing warehouseDocument tag using the specified data.

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
api_instance = Infoplus.WarehouseDocumentApi(Infoplus.ApiClient(configuration))
warehouse_document_id = 56 # int | Id of the warehouseDocument to remove tag from
warehouse_document_tag = 'warehouse_document_tag_example' # str | The tag to delete

try:
    # Delete a tag for a warehouseDocument.
    api_instance.delete_warehouse_document_tag(warehouse_document_id, warehouse_document_tag)
except ApiException as e:
    print("Exception when calling WarehouseDocumentApi->delete_warehouse_document_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_document_id** | **int**| Id of the warehouseDocument to remove tag from | 
 **warehouse_document_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_warehouse_document_by_id**
> WarehouseDocument get_duplicate_warehouse_document_by_id(warehouse_document_id)

Get a duplicated a warehouseDocument by id

Returns a duplicated warehouseDocument identified by the specified id.

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
api_instance = Infoplus.WarehouseDocumentApi(Infoplus.ApiClient(configuration))
warehouse_document_id = 56 # int | Id of the warehouseDocument to be duplicated.

try:
    # Get a duplicated a warehouseDocument by id
    api_response = api_instance.get_duplicate_warehouse_document_by_id(warehouse_document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseDocumentApi->get_duplicate_warehouse_document_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_document_id** | **int**| Id of the warehouseDocument to be duplicated. | 

### Return type

[**WarehouseDocument**](WarehouseDocument.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_document_by_filter**
> list[WarehouseDocument] get_warehouse_document_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search warehouseDocuments by filter

Returns the list of warehouseDocuments that match the given filter.

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
api_instance = Infoplus.WarehouseDocumentApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search warehouseDocuments by filter
    api_response = api_instance.get_warehouse_document_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseDocumentApi->get_warehouse_document_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[WarehouseDocument]**](WarehouseDocument.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_document_by_id**
> WarehouseDocument get_warehouse_document_by_id(warehouse_document_id)

Get a warehouseDocument by id

Returns the warehouseDocument identified by the specified id.

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
api_instance = Infoplus.WarehouseDocumentApi(Infoplus.ApiClient(configuration))
warehouse_document_id = 56 # int | Id of the warehouseDocument to be returned.

try:
    # Get a warehouseDocument by id
    api_response = api_instance.get_warehouse_document_by_id(warehouse_document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarehouseDocumentApi->get_warehouse_document_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_document_id** | **int**| Id of the warehouseDocument to be returned. | 

### Return type

[**WarehouseDocument**](WarehouseDocument.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warehouse_document_tags**
> get_warehouse_document_tags(warehouse_document_id)

Get the tags for a warehouseDocument.

Get all existing warehouseDocument tags.

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
api_instance = Infoplus.WarehouseDocumentApi(Infoplus.ApiClient(configuration))
warehouse_document_id = 56 # int | Id of the warehouseDocument to get tags for

try:
    # Get the tags for a warehouseDocument.
    api_instance.get_warehouse_document_tags(warehouse_document_id)
except ApiException as e:
    print("Exception when calling WarehouseDocumentApi->get_warehouse_document_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_document_id** | **int**| Id of the warehouseDocument to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_warehouse_document_custom_fields**
> update_warehouse_document_custom_fields(body)

Update a warehouseDocument custom fields

Updates an existing warehouseDocument custom fields using the specified data.

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
api_instance = Infoplus.WarehouseDocumentApi(Infoplus.ApiClient(configuration))
body = Infoplus.WarehouseDocument() # WarehouseDocument | WarehouseDocument to be updated.

try:
    # Update a warehouseDocument custom fields
    api_instance.update_warehouse_document_custom_fields(body)
except ApiException as e:
    print("Exception when calling WarehouseDocumentApi->update_warehouse_document_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WarehouseDocument**](WarehouseDocument.md)| WarehouseDocument to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

