# Infoplus.ItemCategoryApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_category**](ItemCategoryApi.md#add_item_category) | **POST** /beta/itemCategory | Create an itemCategory
[**add_item_category_audit**](ItemCategoryApi.md#add_item_category_audit) | **PUT** /beta/itemCategory/{itemCategoryId}/audit/{itemCategoryAudit} | Add new audit for an itemCategory
[**add_item_category_file**](ItemCategoryApi.md#add_item_category_file) | **POST** /beta/itemCategory/{itemCategoryId}/file/{fileName} | Attach a file to an itemCategory
[**add_item_category_file_by_url**](ItemCategoryApi.md#add_item_category_file_by_url) | **POST** /beta/itemCategory/{itemCategoryId}/file | Attach a file to an itemCategory by URL.
[**add_item_category_tag**](ItemCategoryApi.md#add_item_category_tag) | **PUT** /beta/itemCategory/{itemCategoryId}/tag/{itemCategoryTag} | Add new tags for an itemCategory.
[**delete_item_category**](ItemCategoryApi.md#delete_item_category) | **DELETE** /beta/itemCategory/{itemCategoryId} | Delete an itemCategory
[**delete_item_category_file**](ItemCategoryApi.md#delete_item_category_file) | **DELETE** /beta/itemCategory/{itemCategoryId}/file/{fileId} | Delete a file for an itemCategory.
[**delete_item_category_tag**](ItemCategoryApi.md#delete_item_category_tag) | **DELETE** /beta/itemCategory/{itemCategoryId}/tag/{itemCategoryTag} | Delete a tag for an itemCategory.
[**get_duplicate_item_category_by_id**](ItemCategoryApi.md#get_duplicate_item_category_by_id) | **GET** /beta/itemCategory/duplicate/{itemCategoryId} | Get a duplicated an itemCategory by id
[**get_item_category_by_filter**](ItemCategoryApi.md#get_item_category_by_filter) | **GET** /beta/itemCategory/search | Search itemCategorys by filter
[**get_item_category_by_id**](ItemCategoryApi.md#get_item_category_by_id) | **GET** /beta/itemCategory/{itemCategoryId} | Get an itemCategory by id
[**get_item_category_files**](ItemCategoryApi.md#get_item_category_files) | **GET** /beta/itemCategory/{itemCategoryId}/file | Get the files for an itemCategory.
[**get_item_category_tags**](ItemCategoryApi.md#get_item_category_tags) | **GET** /beta/itemCategory/{itemCategoryId}/tag | Get the tags for an itemCategory.
[**update_item_category**](ItemCategoryApi.md#update_item_category) | **PUT** /beta/itemCategory | Update an itemCategory


# **add_item_category**
> ItemCategory add_item_category(body)

Create an itemCategory

Inserts a new itemCategory using the specified data.

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
api_instance = Infoplus.ItemCategoryApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemCategory() # ItemCategory | ItemCategory to be inserted.

try:
    # Create an itemCategory
    api_response = api_instance.add_item_category(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemCategoryApi->add_item_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemCategory**](ItemCategory.md)| ItemCategory to be inserted. | 

### Return type

[**ItemCategory**](ItemCategory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_category_audit**
> add_item_category_audit(item_category_id, item_category_audit)

Add new audit for an itemCategory

Adds an audit to an existing itemCategory.

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
api_instance = Infoplus.ItemCategoryApi(Infoplus.ApiClient(configuration))
item_category_id = 56 # int | Id of the itemCategory to add an audit to
item_category_audit = 'item_category_audit_example' # str | The audit to add

try:
    # Add new audit for an itemCategory
    api_instance.add_item_category_audit(item_category_id, item_category_audit)
except ApiException as e:
    print("Exception when calling ItemCategoryApi->add_item_category_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_category_id** | **int**| Id of the itemCategory to add an audit to | 
 **item_category_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_category_file**
> add_item_category_file(item_category_id, file_name)

Attach a file to an itemCategory

Adds a file to an existing itemCategory.

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
api_instance = Infoplus.ItemCategoryApi(Infoplus.ApiClient(configuration))
item_category_id = 56 # int | Id of the itemCategory to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an itemCategory
    api_instance.add_item_category_file(item_category_id, file_name)
except ApiException as e:
    print("Exception when calling ItemCategoryApi->add_item_category_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_category_id** | **int**| Id of the itemCategory to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_category_file_by_url**
> add_item_category_file_by_url(body, item_category_id)

Attach a file to an itemCategory by URL.

Adds a file to an existing itemCategory by URL.

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
api_instance = Infoplus.ItemCategoryApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
item_category_id = 56 # int | Id of the itemCategory to add an file to

try:
    # Attach a file to an itemCategory by URL.
    api_instance.add_item_category_file_by_url(body, item_category_id)
except ApiException as e:
    print("Exception when calling ItemCategoryApi->add_item_category_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **item_category_id** | **int**| Id of the itemCategory to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_category_tag**
> add_item_category_tag(item_category_id, item_category_tag)

Add new tags for an itemCategory.

Adds a tag to an existing itemCategory.

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
api_instance = Infoplus.ItemCategoryApi(Infoplus.ApiClient(configuration))
item_category_id = 56 # int | Id of the itemCategory to add a tag to
item_category_tag = 'item_category_tag_example' # str | The tag to add

try:
    # Add new tags for an itemCategory.
    api_instance.add_item_category_tag(item_category_id, item_category_tag)
except ApiException as e:
    print("Exception when calling ItemCategoryApi->add_item_category_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_category_id** | **int**| Id of the itemCategory to add a tag to | 
 **item_category_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_category**
> delete_item_category(item_category_id)

Delete an itemCategory

Deletes the itemCategory identified by the specified id.

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
api_instance = Infoplus.ItemCategoryApi(Infoplus.ApiClient(configuration))
item_category_id = 56 # int | Id of the itemCategory to be deleted.

try:
    # Delete an itemCategory
    api_instance.delete_item_category(item_category_id)
except ApiException as e:
    print("Exception when calling ItemCategoryApi->delete_item_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_category_id** | **int**| Id of the itemCategory to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_category_file**
> delete_item_category_file(item_category_id, file_id)

Delete a file for an itemCategory.

Deletes an existing itemCategory file using the specified data.

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
api_instance = Infoplus.ItemCategoryApi(Infoplus.ApiClient(configuration))
item_category_id = 56 # int | Id of the itemCategory to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an itemCategory.
    api_instance.delete_item_category_file(item_category_id, file_id)
except ApiException as e:
    print("Exception when calling ItemCategoryApi->delete_item_category_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_category_id** | **int**| Id of the itemCategory to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_category_tag**
> delete_item_category_tag(item_category_id, item_category_tag)

Delete a tag for an itemCategory.

Deletes an existing itemCategory tag using the specified data.

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
api_instance = Infoplus.ItemCategoryApi(Infoplus.ApiClient(configuration))
item_category_id = 56 # int | Id of the itemCategory to remove tag from
item_category_tag = 'item_category_tag_example' # str | The tag to delete

try:
    # Delete a tag for an itemCategory.
    api_instance.delete_item_category_tag(item_category_id, item_category_tag)
except ApiException as e:
    print("Exception when calling ItemCategoryApi->delete_item_category_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_category_id** | **int**| Id of the itemCategory to remove tag from | 
 **item_category_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_item_category_by_id**
> ItemCategory get_duplicate_item_category_by_id(item_category_id)

Get a duplicated an itemCategory by id

Returns a duplicated itemCategory identified by the specified id.

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
api_instance = Infoplus.ItemCategoryApi(Infoplus.ApiClient(configuration))
item_category_id = 56 # int | Id of the itemCategory to be duplicated.

try:
    # Get a duplicated an itemCategory by id
    api_response = api_instance.get_duplicate_item_category_by_id(item_category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemCategoryApi->get_duplicate_item_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_category_id** | **int**| Id of the itemCategory to be duplicated. | 

### Return type

[**ItemCategory**](ItemCategory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_category_by_filter**
> list[ItemCategory] get_item_category_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search itemCategorys by filter

Returns the list of itemCategorys that match the given filter.

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
api_instance = Infoplus.ItemCategoryApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search itemCategorys by filter
    api_response = api_instance.get_item_category_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemCategoryApi->get_item_category_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ItemCategory]**](ItemCategory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_category_by_id**
> ItemCategory get_item_category_by_id(item_category_id)

Get an itemCategory by id

Returns the itemCategory identified by the specified id.

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
api_instance = Infoplus.ItemCategoryApi(Infoplus.ApiClient(configuration))
item_category_id = 56 # int | Id of the itemCategory to be returned.

try:
    # Get an itemCategory by id
    api_response = api_instance.get_item_category_by_id(item_category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemCategoryApi->get_item_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_category_id** | **int**| Id of the itemCategory to be returned. | 

### Return type

[**ItemCategory**](ItemCategory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_category_files**
> get_item_category_files(item_category_id)

Get the files for an itemCategory.

Get all existing itemCategory files.

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
api_instance = Infoplus.ItemCategoryApi(Infoplus.ApiClient(configuration))
item_category_id = 56 # int | Id of the itemCategory to get files for

try:
    # Get the files for an itemCategory.
    api_instance.get_item_category_files(item_category_id)
except ApiException as e:
    print("Exception when calling ItemCategoryApi->get_item_category_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_category_id** | **int**| Id of the itemCategory to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_category_tags**
> get_item_category_tags(item_category_id)

Get the tags for an itemCategory.

Get all existing itemCategory tags.

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
api_instance = Infoplus.ItemCategoryApi(Infoplus.ApiClient(configuration))
item_category_id = 56 # int | Id of the itemCategory to get tags for

try:
    # Get the tags for an itemCategory.
    api_instance.get_item_category_tags(item_category_id)
except ApiException as e:
    print("Exception when calling ItemCategoryApi->get_item_category_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_category_id** | **int**| Id of the itemCategory to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_category**
> update_item_category(body)

Update an itemCategory

Updates an existing itemCategory using the specified data.

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
api_instance = Infoplus.ItemCategoryApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemCategory() # ItemCategory | ItemCategory to be updated.

try:
    # Update an itemCategory
    api_instance.update_item_category(body)
except ApiException as e:
    print("Exception when calling ItemCategoryApi->update_item_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemCategory**](ItemCategory.md)| ItemCategory to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

