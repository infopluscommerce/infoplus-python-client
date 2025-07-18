# Infoplus.ReturnOrderApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_return_order_audit**](ReturnOrderApi.md#add_return_order_audit) | **PUT** /beta/returnOrder/{returnOrderId}/audit/{returnOrderAudit} | Add new audit for a returnOrder
[**add_return_order_file**](ReturnOrderApi.md#add_return_order_file) | **POST** /beta/returnOrder/{returnOrderId}/file/{fileName} | Attach a file to a returnOrder
[**add_return_order_file_by_url**](ReturnOrderApi.md#add_return_order_file_by_url) | **POST** /beta/returnOrder/{returnOrderId}/file | Attach a file to a returnOrder by URL.
[**add_return_order_tag**](ReturnOrderApi.md#add_return_order_tag) | **PUT** /beta/returnOrder/{returnOrderId}/tag/{returnOrderTag} | Add new tags for a returnOrder.
[**delete_return_order_file**](ReturnOrderApi.md#delete_return_order_file) | **DELETE** /beta/returnOrder/{returnOrderId}/file/{fileId} | Delete a file for a returnOrder.
[**delete_return_order_tag**](ReturnOrderApi.md#delete_return_order_tag) | **DELETE** /beta/returnOrder/{returnOrderId}/tag/{returnOrderTag} | Delete a tag for a returnOrder.
[**get_duplicate_return_order_by_id**](ReturnOrderApi.md#get_duplicate_return_order_by_id) | **GET** /beta/returnOrder/duplicate/{returnOrderId} | Get a duplicated a returnOrder by id
[**get_return_order_by_filter**](ReturnOrderApi.md#get_return_order_by_filter) | **GET** /beta/returnOrder/search | Search returnOrders by filter
[**get_return_order_by_id**](ReturnOrderApi.md#get_return_order_by_id) | **GET** /beta/returnOrder/{returnOrderId} | Get a returnOrder by id
[**get_return_order_files**](ReturnOrderApi.md#get_return_order_files) | **GET** /beta/returnOrder/{returnOrderId}/file | Get the files for a returnOrder.
[**get_return_order_tags**](ReturnOrderApi.md#get_return_order_tags) | **GET** /beta/returnOrder/{returnOrderId}/tag | Get the tags for a returnOrder.
[**update_return_order**](ReturnOrderApi.md#update_return_order) | **PUT** /beta/returnOrder | Update a returnOrder
[**update_return_order_custom_fields**](ReturnOrderApi.md#update_return_order_custom_fields) | **PUT** /beta/returnOrder/customFields | Update a returnOrder custom fields


# **add_return_order_audit**
> add_return_order_audit(return_order_id, return_order_audit)

Add new audit for a returnOrder

Adds an audit to an existing returnOrder.

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
api_instance = Infoplus.ReturnOrderApi(Infoplus.ApiClient(configuration))
return_order_id = 56 # int | Id of the returnOrder to add an audit to
return_order_audit = 'return_order_audit_example' # str | The audit to add

try:
    # Add new audit for a returnOrder
    api_instance.add_return_order_audit(return_order_id, return_order_audit)
except ApiException as e:
    print("Exception when calling ReturnOrderApi->add_return_order_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_id** | **int**| Id of the returnOrder to add an audit to | 
 **return_order_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_return_order_file**
> add_return_order_file(return_order_id, file_name)

Attach a file to a returnOrder

Adds a file to an existing returnOrder.

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
api_instance = Infoplus.ReturnOrderApi(Infoplus.ApiClient(configuration))
return_order_id = 56 # int | Id of the returnOrder to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a returnOrder
    api_instance.add_return_order_file(return_order_id, file_name)
except ApiException as e:
    print("Exception when calling ReturnOrderApi->add_return_order_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_id** | **int**| Id of the returnOrder to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_return_order_file_by_url**
> add_return_order_file_by_url(body, return_order_id)

Attach a file to a returnOrder by URL.

Adds a file to an existing returnOrder by URL.

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
api_instance = Infoplus.ReturnOrderApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
return_order_id = 56 # int | Id of the returnOrder to add an file to

try:
    # Attach a file to a returnOrder by URL.
    api_instance.add_return_order_file_by_url(body, return_order_id)
except ApiException as e:
    print("Exception when calling ReturnOrderApi->add_return_order_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **return_order_id** | **int**| Id of the returnOrder to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_return_order_tag**
> add_return_order_tag(return_order_id, return_order_tag)

Add new tags for a returnOrder.

Adds a tag to an existing returnOrder.

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
api_instance = Infoplus.ReturnOrderApi(Infoplus.ApiClient(configuration))
return_order_id = 56 # int | Id of the returnOrder to add a tag to
return_order_tag = 'return_order_tag_example' # str | The tag to add

try:
    # Add new tags for a returnOrder.
    api_instance.add_return_order_tag(return_order_id, return_order_tag)
except ApiException as e:
    print("Exception when calling ReturnOrderApi->add_return_order_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_id** | **int**| Id of the returnOrder to add a tag to | 
 **return_order_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_return_order_file**
> delete_return_order_file(return_order_id, file_id)

Delete a file for a returnOrder.

Deletes an existing returnOrder file using the specified data.

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
api_instance = Infoplus.ReturnOrderApi(Infoplus.ApiClient(configuration))
return_order_id = 56 # int | Id of the returnOrder to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a returnOrder.
    api_instance.delete_return_order_file(return_order_id, file_id)
except ApiException as e:
    print("Exception when calling ReturnOrderApi->delete_return_order_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_id** | **int**| Id of the returnOrder to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_return_order_tag**
> delete_return_order_tag(return_order_id, return_order_tag)

Delete a tag for a returnOrder.

Deletes an existing returnOrder tag using the specified data.

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
api_instance = Infoplus.ReturnOrderApi(Infoplus.ApiClient(configuration))
return_order_id = 56 # int | Id of the returnOrder to remove tag from
return_order_tag = 'return_order_tag_example' # str | The tag to delete

try:
    # Delete a tag for a returnOrder.
    api_instance.delete_return_order_tag(return_order_id, return_order_tag)
except ApiException as e:
    print("Exception when calling ReturnOrderApi->delete_return_order_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_id** | **int**| Id of the returnOrder to remove tag from | 
 **return_order_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_return_order_by_id**
> ReturnOrder get_duplicate_return_order_by_id(return_order_id)

Get a duplicated a returnOrder by id

Returns a duplicated returnOrder identified by the specified id.

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
api_instance = Infoplus.ReturnOrderApi(Infoplus.ApiClient(configuration))
return_order_id = 56 # int | Id of the returnOrder to be duplicated.

try:
    # Get a duplicated a returnOrder by id
    api_response = api_instance.get_duplicate_return_order_by_id(return_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnOrderApi->get_duplicate_return_order_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_id** | **int**| Id of the returnOrder to be duplicated. | 

### Return type

[**ReturnOrder**](ReturnOrder.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_order_by_filter**
> list[ReturnOrder] get_return_order_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search returnOrders by filter

Returns the list of returnOrders that match the given filter.

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
api_instance = Infoplus.ReturnOrderApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search returnOrders by filter
    api_response = api_instance.get_return_order_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnOrderApi->get_return_order_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ReturnOrder]**](ReturnOrder.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_order_by_id**
> ReturnOrder get_return_order_by_id(return_order_id)

Get a returnOrder by id

Returns the returnOrder identified by the specified id.

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
api_instance = Infoplus.ReturnOrderApi(Infoplus.ApiClient(configuration))
return_order_id = 56 # int | Id of the returnOrder to be returned.

try:
    # Get a returnOrder by id
    api_response = api_instance.get_return_order_by_id(return_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnOrderApi->get_return_order_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_id** | **int**| Id of the returnOrder to be returned. | 

### Return type

[**ReturnOrder**](ReturnOrder.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_order_files**
> get_return_order_files(return_order_id)

Get the files for a returnOrder.

Get all existing returnOrder files.

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
api_instance = Infoplus.ReturnOrderApi(Infoplus.ApiClient(configuration))
return_order_id = 56 # int | Id of the returnOrder to get files for

try:
    # Get the files for a returnOrder.
    api_instance.get_return_order_files(return_order_id)
except ApiException as e:
    print("Exception when calling ReturnOrderApi->get_return_order_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_id** | **int**| Id of the returnOrder to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_order_tags**
> get_return_order_tags(return_order_id)

Get the tags for a returnOrder.

Get all existing returnOrder tags.

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
api_instance = Infoplus.ReturnOrderApi(Infoplus.ApiClient(configuration))
return_order_id = 56 # int | Id of the returnOrder to get tags for

try:
    # Get the tags for a returnOrder.
    api_instance.get_return_order_tags(return_order_id)
except ApiException as e:
    print("Exception when calling ReturnOrderApi->get_return_order_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_id** | **int**| Id of the returnOrder to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_return_order**
> update_return_order(body)

Update a returnOrder

Updates an existing returnOrder using the specified data.

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
api_instance = Infoplus.ReturnOrderApi(Infoplus.ApiClient(configuration))
body = Infoplus.ReturnOrder() # ReturnOrder | ReturnOrder to be updated.

try:
    # Update a returnOrder
    api_instance.update_return_order(body)
except ApiException as e:
    print("Exception when calling ReturnOrderApi->update_return_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReturnOrder**](ReturnOrder.md)| ReturnOrder to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_return_order_custom_fields**
> update_return_order_custom_fields(body)

Update a returnOrder custom fields

Updates an existing returnOrder custom fields using the specified data.

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
api_instance = Infoplus.ReturnOrderApi(Infoplus.ApiClient(configuration))
body = Infoplus.ReturnOrder() # ReturnOrder | ReturnOrder to be updated.

try:
    # Update a returnOrder custom fields
    api_instance.update_return_order_custom_fields(body)
except ApiException as e:
    print("Exception when calling ReturnOrderApi->update_return_order_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReturnOrder**](ReturnOrder.md)| ReturnOrder to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

