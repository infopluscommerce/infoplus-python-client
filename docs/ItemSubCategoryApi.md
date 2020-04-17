# Infoplus.ItemSubCategoryApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_sub_category**](ItemSubCategoryApi.md#add_item_sub_category) | **POST** /beta/itemSubCategory | Create an itemSubCategory
[**add_item_sub_category_audit**](ItemSubCategoryApi.md#add_item_sub_category_audit) | **PUT** /beta/itemSubCategory/{itemSubCategoryId}/audit/{itemSubCategoryAudit} | Add new audit for an itemSubCategory
[**add_item_sub_category_file**](ItemSubCategoryApi.md#add_item_sub_category_file) | **POST** /beta/itemSubCategory/{itemSubCategoryId}/file/{fileName} | Attach a file to an itemSubCategory
[**add_item_sub_category_file_by_url**](ItemSubCategoryApi.md#add_item_sub_category_file_by_url) | **POST** /beta/itemSubCategory/{itemSubCategoryId}/file | Attach a file to an itemSubCategory by URL.
[**add_item_sub_category_tag**](ItemSubCategoryApi.md#add_item_sub_category_tag) | **PUT** /beta/itemSubCategory/{itemSubCategoryId}/tag/{itemSubCategoryTag} | Add new tags for an itemSubCategory.
[**delete_item_sub_category**](ItemSubCategoryApi.md#delete_item_sub_category) | **DELETE** /beta/itemSubCategory/{itemSubCategoryId} | Delete an itemSubCategory
[**delete_item_sub_category_file**](ItemSubCategoryApi.md#delete_item_sub_category_file) | **DELETE** /beta/itemSubCategory/{itemSubCategoryId}/file/{fileId} | Delete a file for an itemSubCategory.
[**delete_item_sub_category_tag**](ItemSubCategoryApi.md#delete_item_sub_category_tag) | **DELETE** /beta/itemSubCategory/{itemSubCategoryId}/tag/{itemSubCategoryTag} | Delete a tag for an itemSubCategory.
[**get_duplicate_item_sub_category_by_id**](ItemSubCategoryApi.md#get_duplicate_item_sub_category_by_id) | **GET** /beta/itemSubCategory/duplicate/{itemSubCategoryId} | Get a duplicated an itemSubCategory by id
[**get_item_sub_category_by_filter**](ItemSubCategoryApi.md#get_item_sub_category_by_filter) | **GET** /beta/itemSubCategory/search | Search itemSubCategorys by filter
[**get_item_sub_category_by_id**](ItemSubCategoryApi.md#get_item_sub_category_by_id) | **GET** /beta/itemSubCategory/{itemSubCategoryId} | Get an itemSubCategory by id
[**get_item_sub_category_files**](ItemSubCategoryApi.md#get_item_sub_category_files) | **GET** /beta/itemSubCategory/{itemSubCategoryId}/file | Get the files for an itemSubCategory.
[**get_item_sub_category_tags**](ItemSubCategoryApi.md#get_item_sub_category_tags) | **GET** /beta/itemSubCategory/{itemSubCategoryId}/tag | Get the tags for an itemSubCategory.
[**update_item_sub_category**](ItemSubCategoryApi.md#update_item_sub_category) | **PUT** /beta/itemSubCategory | Update an itemSubCategory


# **add_item_sub_category**
> ItemSubCategory add_item_sub_category(body)

Create an itemSubCategory

Inserts a new itemSubCategory using the specified data.

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
api_instance = Infoplus.ItemSubCategoryApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemSubCategory() # ItemSubCategory | ItemSubCategory to be inserted.

try:
    # Create an itemSubCategory
    api_response = api_instance.add_item_sub_category(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSubCategoryApi->add_item_sub_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemSubCategory**](ItemSubCategory.md)| ItemSubCategory to be inserted. | 

### Return type

[**ItemSubCategory**](ItemSubCategory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_sub_category_audit**
> add_item_sub_category_audit(item_sub_category_id, item_sub_category_audit)

Add new audit for an itemSubCategory

Adds an audit to an existing itemSubCategory.

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
api_instance = Infoplus.ItemSubCategoryApi(Infoplus.ApiClient(configuration))
item_sub_category_id = 56 # int | Id of the itemSubCategory to add an audit to
item_sub_category_audit = 'item_sub_category_audit_example' # str | The audit to add

try:
    # Add new audit for an itemSubCategory
    api_instance.add_item_sub_category_audit(item_sub_category_id, item_sub_category_audit)
except ApiException as e:
    print("Exception when calling ItemSubCategoryApi->add_item_sub_category_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sub_category_id** | **int**| Id of the itemSubCategory to add an audit to | 
 **item_sub_category_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_sub_category_file**
> add_item_sub_category_file(item_sub_category_id, file_name)

Attach a file to an itemSubCategory

Adds a file to an existing itemSubCategory.

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
api_instance = Infoplus.ItemSubCategoryApi(Infoplus.ApiClient(configuration))
item_sub_category_id = 56 # int | Id of the itemSubCategory to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an itemSubCategory
    api_instance.add_item_sub_category_file(item_sub_category_id, file_name)
except ApiException as e:
    print("Exception when calling ItemSubCategoryApi->add_item_sub_category_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sub_category_id** | **int**| Id of the itemSubCategory to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_sub_category_file_by_url**
> add_item_sub_category_file_by_url(body, item_sub_category_id)

Attach a file to an itemSubCategory by URL.

Adds a file to an existing itemSubCategory by URL.

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
api_instance = Infoplus.ItemSubCategoryApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
item_sub_category_id = 56 # int | Id of the itemSubCategory to add an file to

try:
    # Attach a file to an itemSubCategory by URL.
    api_instance.add_item_sub_category_file_by_url(body, item_sub_category_id)
except ApiException as e:
    print("Exception when calling ItemSubCategoryApi->add_item_sub_category_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **item_sub_category_id** | **int**| Id of the itemSubCategory to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_sub_category_tag**
> add_item_sub_category_tag(item_sub_category_id, item_sub_category_tag)

Add new tags for an itemSubCategory.

Adds a tag to an existing itemSubCategory.

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
api_instance = Infoplus.ItemSubCategoryApi(Infoplus.ApiClient(configuration))
item_sub_category_id = 56 # int | Id of the itemSubCategory to add a tag to
item_sub_category_tag = 'item_sub_category_tag_example' # str | The tag to add

try:
    # Add new tags for an itemSubCategory.
    api_instance.add_item_sub_category_tag(item_sub_category_id, item_sub_category_tag)
except ApiException as e:
    print("Exception when calling ItemSubCategoryApi->add_item_sub_category_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sub_category_id** | **int**| Id of the itemSubCategory to add a tag to | 
 **item_sub_category_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_sub_category**
> delete_item_sub_category(item_sub_category_id)

Delete an itemSubCategory

Deletes the itemSubCategory identified by the specified id.

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
api_instance = Infoplus.ItemSubCategoryApi(Infoplus.ApiClient(configuration))
item_sub_category_id = 56 # int | Id of the itemSubCategory to be deleted.

try:
    # Delete an itemSubCategory
    api_instance.delete_item_sub_category(item_sub_category_id)
except ApiException as e:
    print("Exception when calling ItemSubCategoryApi->delete_item_sub_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sub_category_id** | **int**| Id of the itemSubCategory to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_sub_category_file**
> delete_item_sub_category_file(item_sub_category_id, file_id)

Delete a file for an itemSubCategory.

Deletes an existing itemSubCategory file using the specified data.

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
api_instance = Infoplus.ItemSubCategoryApi(Infoplus.ApiClient(configuration))
item_sub_category_id = 56 # int | Id of the itemSubCategory to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an itemSubCategory.
    api_instance.delete_item_sub_category_file(item_sub_category_id, file_id)
except ApiException as e:
    print("Exception when calling ItemSubCategoryApi->delete_item_sub_category_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sub_category_id** | **int**| Id of the itemSubCategory to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_sub_category_tag**
> delete_item_sub_category_tag(item_sub_category_id, item_sub_category_tag)

Delete a tag for an itemSubCategory.

Deletes an existing itemSubCategory tag using the specified data.

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
api_instance = Infoplus.ItemSubCategoryApi(Infoplus.ApiClient(configuration))
item_sub_category_id = 56 # int | Id of the itemSubCategory to remove tag from
item_sub_category_tag = 'item_sub_category_tag_example' # str | The tag to delete

try:
    # Delete a tag for an itemSubCategory.
    api_instance.delete_item_sub_category_tag(item_sub_category_id, item_sub_category_tag)
except ApiException as e:
    print("Exception when calling ItemSubCategoryApi->delete_item_sub_category_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sub_category_id** | **int**| Id of the itemSubCategory to remove tag from | 
 **item_sub_category_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_item_sub_category_by_id**
> ItemSubCategory get_duplicate_item_sub_category_by_id(item_sub_category_id)

Get a duplicated an itemSubCategory by id

Returns a duplicated itemSubCategory identified by the specified id.

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
api_instance = Infoplus.ItemSubCategoryApi(Infoplus.ApiClient(configuration))
item_sub_category_id = 56 # int | Id of the itemSubCategory to be duplicated.

try:
    # Get a duplicated an itemSubCategory by id
    api_response = api_instance.get_duplicate_item_sub_category_by_id(item_sub_category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSubCategoryApi->get_duplicate_item_sub_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sub_category_id** | **int**| Id of the itemSubCategory to be duplicated. | 

### Return type

[**ItemSubCategory**](ItemSubCategory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_sub_category_by_filter**
> list[ItemSubCategory] get_item_sub_category_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search itemSubCategorys by filter

Returns the list of itemSubCategorys that match the given filter.

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
api_instance = Infoplus.ItemSubCategoryApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search itemSubCategorys by filter
    api_response = api_instance.get_item_sub_category_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSubCategoryApi->get_item_sub_category_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ItemSubCategory]**](ItemSubCategory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_sub_category_by_id**
> ItemSubCategory get_item_sub_category_by_id(item_sub_category_id)

Get an itemSubCategory by id

Returns the itemSubCategory identified by the specified id.

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
api_instance = Infoplus.ItemSubCategoryApi(Infoplus.ApiClient(configuration))
item_sub_category_id = 56 # int | Id of the itemSubCategory to be returned.

try:
    # Get an itemSubCategory by id
    api_response = api_instance.get_item_sub_category_by_id(item_sub_category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSubCategoryApi->get_item_sub_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sub_category_id** | **int**| Id of the itemSubCategory to be returned. | 

### Return type

[**ItemSubCategory**](ItemSubCategory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_sub_category_files**
> get_item_sub_category_files(item_sub_category_id)

Get the files for an itemSubCategory.

Get all existing itemSubCategory files.

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
api_instance = Infoplus.ItemSubCategoryApi(Infoplus.ApiClient(configuration))
item_sub_category_id = 56 # int | Id of the itemSubCategory to get files for

try:
    # Get the files for an itemSubCategory.
    api_instance.get_item_sub_category_files(item_sub_category_id)
except ApiException as e:
    print("Exception when calling ItemSubCategoryApi->get_item_sub_category_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sub_category_id** | **int**| Id of the itemSubCategory to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_sub_category_tags**
> get_item_sub_category_tags(item_sub_category_id)

Get the tags for an itemSubCategory.

Get all existing itemSubCategory tags.

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
api_instance = Infoplus.ItemSubCategoryApi(Infoplus.ApiClient(configuration))
item_sub_category_id = 56 # int | Id of the itemSubCategory to get tags for

try:
    # Get the tags for an itemSubCategory.
    api_instance.get_item_sub_category_tags(item_sub_category_id)
except ApiException as e:
    print("Exception when calling ItemSubCategoryApi->get_item_sub_category_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sub_category_id** | **int**| Id of the itemSubCategory to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_sub_category**
> update_item_sub_category(body)

Update an itemSubCategory

Updates an existing itemSubCategory using the specified data.

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
api_instance = Infoplus.ItemSubCategoryApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemSubCategory() # ItemSubCategory | ItemSubCategory to be updated.

try:
    # Update an itemSubCategory
    api_instance.update_item_sub_category(body)
except ApiException as e:
    print("Exception when calling ItemSubCategoryApi->update_item_sub_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemSubCategory**](ItemSubCategory.md)| ItemSubCategory to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

