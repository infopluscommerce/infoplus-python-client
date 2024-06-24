# Infoplus.ItemReceiptApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_receipt_audit**](ItemReceiptApi.md#add_item_receipt_audit) | **PUT** /beta/itemReceipt/{itemReceiptId}/audit/{itemReceiptAudit} | Add new audit for an itemReceipt
[**add_item_receipt_file**](ItemReceiptApi.md#add_item_receipt_file) | **POST** /beta/itemReceipt/{itemReceiptId}/file/{fileName} | Attach a file to an itemReceipt
[**add_item_receipt_file_by_url**](ItemReceiptApi.md#add_item_receipt_file_by_url) | **POST** /beta/itemReceipt/{itemReceiptId}/file | Attach a file to an itemReceipt by URL.
[**add_item_receipt_tag**](ItemReceiptApi.md#add_item_receipt_tag) | **PUT** /beta/itemReceipt/{itemReceiptId}/tag/{itemReceiptTag} | Add new tags for an itemReceipt.
[**delete_item_receipt_file**](ItemReceiptApi.md#delete_item_receipt_file) | **DELETE** /beta/itemReceipt/{itemReceiptId}/file/{fileId} | Delete a file for an itemReceipt.
[**delete_item_receipt_tag**](ItemReceiptApi.md#delete_item_receipt_tag) | **DELETE** /beta/itemReceipt/{itemReceiptId}/tag/{itemReceiptTag} | Delete a tag for an itemReceipt.
[**get_duplicate_item_receipt_by_id**](ItemReceiptApi.md#get_duplicate_item_receipt_by_id) | **GET** /beta/itemReceipt/duplicate/{itemReceiptId} | Get a duplicated an itemReceipt by id
[**get_item_receipt_by_filter**](ItemReceiptApi.md#get_item_receipt_by_filter) | **GET** /beta/itemReceipt/search | Search itemReceipts by filter
[**get_item_receipt_by_id**](ItemReceiptApi.md#get_item_receipt_by_id) | **GET** /beta/itemReceipt/{itemReceiptId} | Get an itemReceipt by id
[**get_item_receipt_files**](ItemReceiptApi.md#get_item_receipt_files) | **GET** /beta/itemReceipt/{itemReceiptId}/file | Get the files for an itemReceipt.
[**get_item_receipt_tags**](ItemReceiptApi.md#get_item_receipt_tags) | **GET** /beta/itemReceipt/{itemReceiptId}/tag | Get the tags for an itemReceipt.
[**update_item_receipt**](ItemReceiptApi.md#update_item_receipt) | **PUT** /beta/itemReceipt | Update an itemReceipt
[**update_item_receipt_custom_fields**](ItemReceiptApi.md#update_item_receipt_custom_fields) | **PUT** /beta/itemReceipt/customFields | Update an itemReceipt custom fields


# **add_item_receipt_audit**
> add_item_receipt_audit(item_receipt_id, item_receipt_audit)

Add new audit for an itemReceipt

Adds an audit to an existing itemReceipt.

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
api_instance = Infoplus.ItemReceiptApi(Infoplus.ApiClient(configuration))
item_receipt_id = 56 # int | Id of the itemReceipt to add an audit to
item_receipt_audit = 'item_receipt_audit_example' # str | The audit to add

try:
    # Add new audit for an itemReceipt
    api_instance.add_item_receipt_audit(item_receipt_id, item_receipt_audit)
except ApiException as e:
    print("Exception when calling ItemReceiptApi->add_item_receipt_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_id** | **int**| Id of the itemReceipt to add an audit to | 
 **item_receipt_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_receipt_file**
> add_item_receipt_file(item_receipt_id, file_name)

Attach a file to an itemReceipt

Adds a file to an existing itemReceipt.

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
api_instance = Infoplus.ItemReceiptApi(Infoplus.ApiClient(configuration))
item_receipt_id = 56 # int | Id of the itemReceipt to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an itemReceipt
    api_instance.add_item_receipt_file(item_receipt_id, file_name)
except ApiException as e:
    print("Exception when calling ItemReceiptApi->add_item_receipt_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_id** | **int**| Id of the itemReceipt to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_receipt_file_by_url**
> add_item_receipt_file_by_url(body, item_receipt_id)

Attach a file to an itemReceipt by URL.

Adds a file to an existing itemReceipt by URL.

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
api_instance = Infoplus.ItemReceiptApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
item_receipt_id = 56 # int | Id of the itemReceipt to add an file to

try:
    # Attach a file to an itemReceipt by URL.
    api_instance.add_item_receipt_file_by_url(body, item_receipt_id)
except ApiException as e:
    print("Exception when calling ItemReceiptApi->add_item_receipt_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **item_receipt_id** | **int**| Id of the itemReceipt to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_receipt_tag**
> add_item_receipt_tag(item_receipt_id, item_receipt_tag)

Add new tags for an itemReceipt.

Adds a tag to an existing itemReceipt.

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
api_instance = Infoplus.ItemReceiptApi(Infoplus.ApiClient(configuration))
item_receipt_id = 56 # int | Id of the itemReceipt to add a tag to
item_receipt_tag = 'item_receipt_tag_example' # str | The tag to add

try:
    # Add new tags for an itemReceipt.
    api_instance.add_item_receipt_tag(item_receipt_id, item_receipt_tag)
except ApiException as e:
    print("Exception when calling ItemReceiptApi->add_item_receipt_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_id** | **int**| Id of the itemReceipt to add a tag to | 
 **item_receipt_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_receipt_file**
> delete_item_receipt_file(item_receipt_id, file_id)

Delete a file for an itemReceipt.

Deletes an existing itemReceipt file using the specified data.

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
api_instance = Infoplus.ItemReceiptApi(Infoplus.ApiClient(configuration))
item_receipt_id = 56 # int | Id of the itemReceipt to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an itemReceipt.
    api_instance.delete_item_receipt_file(item_receipt_id, file_id)
except ApiException as e:
    print("Exception when calling ItemReceiptApi->delete_item_receipt_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_id** | **int**| Id of the itemReceipt to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_receipt_tag**
> delete_item_receipt_tag(item_receipt_id, item_receipt_tag)

Delete a tag for an itemReceipt.

Deletes an existing itemReceipt tag using the specified data.

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
api_instance = Infoplus.ItemReceiptApi(Infoplus.ApiClient(configuration))
item_receipt_id = 56 # int | Id of the itemReceipt to remove tag from
item_receipt_tag = 'item_receipt_tag_example' # str | The tag to delete

try:
    # Delete a tag for an itemReceipt.
    api_instance.delete_item_receipt_tag(item_receipt_id, item_receipt_tag)
except ApiException as e:
    print("Exception when calling ItemReceiptApi->delete_item_receipt_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_id** | **int**| Id of the itemReceipt to remove tag from | 
 **item_receipt_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_item_receipt_by_id**
> ItemReceipt get_duplicate_item_receipt_by_id(item_receipt_id)

Get a duplicated an itemReceipt by id

Returns a duplicated itemReceipt identified by the specified id.

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
api_instance = Infoplus.ItemReceiptApi(Infoplus.ApiClient(configuration))
item_receipt_id = 56 # int | Id of the itemReceipt to be duplicated.

try:
    # Get a duplicated an itemReceipt by id
    api_response = api_instance.get_duplicate_item_receipt_by_id(item_receipt_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemReceiptApi->get_duplicate_item_receipt_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_id** | **int**| Id of the itemReceipt to be duplicated. | 

### Return type

[**ItemReceipt**](ItemReceipt.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_receipt_by_filter**
> list[ItemReceipt] get_item_receipt_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search itemReceipts by filter

Returns the list of itemReceipts that match the given filter.

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
api_instance = Infoplus.ItemReceiptApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search itemReceipts by filter
    api_response = api_instance.get_item_receipt_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemReceiptApi->get_item_receipt_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ItemReceipt]**](ItemReceipt.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_receipt_by_id**
> ItemReceipt get_item_receipt_by_id(item_receipt_id)

Get an itemReceipt by id

Returns the itemReceipt identified by the specified id.

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
api_instance = Infoplus.ItemReceiptApi(Infoplus.ApiClient(configuration))
item_receipt_id = 56 # int | Id of the itemReceipt to be returned.

try:
    # Get an itemReceipt by id
    api_response = api_instance.get_item_receipt_by_id(item_receipt_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemReceiptApi->get_item_receipt_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_id** | **int**| Id of the itemReceipt to be returned. | 

### Return type

[**ItemReceipt**](ItemReceipt.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_receipt_files**
> get_item_receipt_files(item_receipt_id)

Get the files for an itemReceipt.

Get all existing itemReceipt files.

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
api_instance = Infoplus.ItemReceiptApi(Infoplus.ApiClient(configuration))
item_receipt_id = 56 # int | Id of the itemReceipt to get files for

try:
    # Get the files for an itemReceipt.
    api_instance.get_item_receipt_files(item_receipt_id)
except ApiException as e:
    print("Exception when calling ItemReceiptApi->get_item_receipt_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_id** | **int**| Id of the itemReceipt to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_receipt_tags**
> get_item_receipt_tags(item_receipt_id)

Get the tags for an itemReceipt.

Get all existing itemReceipt tags.

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
api_instance = Infoplus.ItemReceiptApi(Infoplus.ApiClient(configuration))
item_receipt_id = 56 # int | Id of the itemReceipt to get tags for

try:
    # Get the tags for an itemReceipt.
    api_instance.get_item_receipt_tags(item_receipt_id)
except ApiException as e:
    print("Exception when calling ItemReceiptApi->get_item_receipt_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_id** | **int**| Id of the itemReceipt to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_receipt**
> update_item_receipt(body)

Update an itemReceipt

Updates an existing itemReceipt using the specified data.

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
api_instance = Infoplus.ItemReceiptApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemReceipt() # ItemReceipt | ItemReceipt to be updated.

try:
    # Update an itemReceipt
    api_instance.update_item_receipt(body)
except ApiException as e:
    print("Exception when calling ItemReceiptApi->update_item_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemReceipt**](ItemReceipt.md)| ItemReceipt to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_receipt_custom_fields**
> update_item_receipt_custom_fields(body)

Update an itemReceipt custom fields

Updates an existing itemReceipt custom fields using the specified data.

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
api_instance = Infoplus.ItemReceiptApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemReceipt() # ItemReceipt | ItemReceipt to be updated.

try:
    # Update an itemReceipt custom fields
    api_instance.update_item_receipt_custom_fields(body)
except ApiException as e:
    print("Exception when calling ItemReceiptApi->update_item_receipt_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemReceipt**](ItemReceipt.md)| ItemReceipt to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

