# Infoplus.ItemApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item**](ItemApi.md#add_item) | **POST** /v3.0/item | Create an item
[**add_item_audit**](ItemApi.md#add_item_audit) | **PUT** /v3.0/item/{itemId}/audit/{itemAudit} | Add new audit for an item
[**add_item_file**](ItemApi.md#add_item_file) | **POST** /v3.0/item/{itemId}/file/{fileName} | Attach a file to an item
[**add_item_file_by_url**](ItemApi.md#add_item_file_by_url) | **POST** /v3.0/item/{itemId}/file | Attach a file to an item by URL.
[**add_item_tag**](ItemApi.md#add_item_tag) | **PUT** /v3.0/item/{itemId}/tag/{itemTag} | Add new tags for an item.
[**delete_item**](ItemApi.md#delete_item) | **DELETE** /v3.0/item/{itemId} | Delete an item
[**delete_item_file**](ItemApi.md#delete_item_file) | **DELETE** /v3.0/item/{itemId}/file/{fileId} | Delete a file for an item.
[**delete_item_tag**](ItemApi.md#delete_item_tag) | **DELETE** /v3.0/item/{itemId}/tag/{itemTag} | Delete a tag for an item.
[**get_by_sku**](ItemApi.md#get_by_sku) | **GET** /v3.0/item/getBySKU | Get an item by SKU
[**get_duplicate_item_by_id**](ItemApi.md#get_duplicate_item_by_id) | **GET** /v3.0/item/duplicate/{itemId} | Get a duplicated an item by id
[**get_item_by_filter**](ItemApi.md#get_item_by_filter) | **GET** /v3.0/item/search | Search items by filter
[**get_item_by_id**](ItemApi.md#get_item_by_id) | **GET** /v3.0/item/{itemId} | Get an item by id
[**get_item_files**](ItemApi.md#get_item_files) | **GET** /v3.0/item/{itemId}/file | Get the files for an item.
[**get_item_tags**](ItemApi.md#get_item_tags) | **GET** /v3.0/item/{itemId}/tag | Get the tags for an item.
[**update_item**](ItemApi.md#update_item) | **PUT** /v3.0/item | Update an item
[**update_item_custom_fields**](ItemApi.md#update_item_custom_fields) | **PUT** /v3.0/item/customFields | Update an item custom fields


# **add_item**
> Item add_item(body)

Create an item

Inserts a new item using the specified data.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
body = Infoplus.Item() # Item | Item to be inserted.

try:
    # Create an item
    api_response = api_instance.add_item(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->add_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Item**](Item.md)| Item to be inserted. | 

### Return type

[**Item**](Item.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_audit**
> add_item_audit(item_id, item_audit)

Add new audit for an item

Adds an audit to an existing item.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
item_id = 56 # int | Id of the item to add an audit to
item_audit = 'item_audit_example' # str | The audit to add

try:
    # Add new audit for an item
    api_instance.add_item_audit(item_id, item_audit)
except ApiException as e:
    print("Exception when calling ItemApi->add_item_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Id of the item to add an audit to | 
 **item_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_file**
> add_item_file(item_id, file_name)

Attach a file to an item

Adds a file to an existing item.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
item_id = 56 # int | Id of the item to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an item
    api_instance.add_item_file(item_id, file_name)
except ApiException as e:
    print("Exception when calling ItemApi->add_item_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Id of the item to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_file_by_url**
> add_item_file_by_url(body, item_id)

Attach a file to an item by URL.

Adds a file to an existing item by URL.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
item_id = 56 # int | Id of the item to add an file to

try:
    # Attach a file to an item by URL.
    api_instance.add_item_file_by_url(body, item_id)
except ApiException as e:
    print("Exception when calling ItemApi->add_item_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **item_id** | **int**| Id of the item to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_tag**
> add_item_tag(item_id, item_tag)

Add new tags for an item.

Adds a tag to an existing item.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
item_id = 56 # int | Id of the item to add a tag to
item_tag = 'item_tag_example' # str | The tag to add

try:
    # Add new tags for an item.
    api_instance.add_item_tag(item_id, item_tag)
except ApiException as e:
    print("Exception when calling ItemApi->add_item_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Id of the item to add a tag to | 
 **item_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item**
> delete_item(item_id)

Delete an item

Deletes the item identified by the specified id.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
item_id = 56 # int | Id of the item to be deleted.

try:
    # Delete an item
    api_instance.delete_item(item_id)
except ApiException as e:
    print("Exception when calling ItemApi->delete_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Id of the item to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_file**
> delete_item_file(item_id, file_id)

Delete a file for an item.

Deletes an existing item file using the specified data.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
item_id = 56 # int | Id of the item to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an item.
    api_instance.delete_item_file(item_id, file_id)
except ApiException as e:
    print("Exception when calling ItemApi->delete_item_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Id of the item to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_tag**
> delete_item_tag(item_id, item_tag)

Delete a tag for an item.

Deletes an existing item tag using the specified data.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
item_id = 56 # int | Id of the item to remove tag from
item_tag = 'item_tag_example' # str | The tag to delete

try:
    # Delete a tag for an item.
    api_instance.delete_item_tag(item_id, item_tag)
except ApiException as e:
    print("Exception when calling ItemApi->delete_item_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Id of the item to remove tag from | 
 **item_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_sku**
> Item get_by_sku(lob_id, sku)

Get an item by SKU

Returns the item identified by the specified parameters.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
lob_id = 56 # int | lobId of the item to be returned.
sku = 'sku_example' # str | sku of the item to be returned.

try:
    # Get an item by SKU
    api_response = api_instance.get_by_sku(lob_id, sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_by_sku: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lob_id** | **int**| lobId of the item to be returned. | 
 **sku** | **str**| sku of the item to be returned. | 

### Return type

[**Item**](Item.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_item_by_id**
> Item get_duplicate_item_by_id(item_id)

Get a duplicated an item by id

Returns a duplicated item identified by the specified id.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
item_id = 56 # int | Id of the item to be duplicated.

try:
    # Get a duplicated an item by id
    api_response = api_instance.get_duplicate_item_by_id(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_duplicate_item_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Id of the item to be duplicated. | 

### Return type

[**Item**](Item.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_by_filter**
> list[Item] get_item_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search items by filter

Returns the list of items that match the given filter.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search items by filter
    api_response = api_instance.get_item_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_item_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Item]**](Item.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_by_id**
> Item get_item_by_id(item_id)

Get an item by id

Returns the item identified by the specified id.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
item_id = 56 # int | Id of the item to be returned.

try:
    # Get an item by id
    api_response = api_instance.get_item_by_id(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_item_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Id of the item to be returned. | 

### Return type

[**Item**](Item.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_files**
> get_item_files(item_id)

Get the files for an item.

Get all existing item files.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
item_id = 56 # int | Id of the item to get files for

try:
    # Get the files for an item.
    api_instance.get_item_files(item_id)
except ApiException as e:
    print("Exception when calling ItemApi->get_item_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Id of the item to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_tags**
> get_item_tags(item_id)

Get the tags for an item.

Get all existing item tags.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
item_id = 56 # int | Id of the item to get tags for

try:
    # Get the tags for an item.
    api_instance.get_item_tags(item_id)
except ApiException as e:
    print("Exception when calling ItemApi->get_item_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Id of the item to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item**
> update_item(body)

Update an item

Updates an existing item using the specified data.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
body = Infoplus.Item() # Item | Item to be updated.

try:
    # Update an item
    api_instance.update_item(body)
except ApiException as e:
    print("Exception when calling ItemApi->update_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Item**](Item.md)| Item to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_custom_fields**
> update_item_custom_fields(body)

Update an item custom fields

Updates an existing item custom fields using the specified data.

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
api_instance = Infoplus.ItemApi(Infoplus.ApiClient(configuration))
body = Infoplus.Item() # Item | Item to be updated.

try:
    # Update an item custom fields
    api_instance.update_item_custom_fields(body)
except ApiException as e:
    print("Exception when calling ItemApi->update_item_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Item**](Item.md)| Item to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

