# Infoplus.ItemProductCodeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_product_code**](ItemProductCodeApi.md#add_item_product_code) | **POST** /beta/itemProductCode | Create an itemProductCode
[**add_item_product_code_audit**](ItemProductCodeApi.md#add_item_product_code_audit) | **PUT** /beta/itemProductCode/{itemProductCodeId}/audit/{itemProductCodeAudit} | Add new audit for an itemProductCode
[**add_item_product_code_file**](ItemProductCodeApi.md#add_item_product_code_file) | **POST** /beta/itemProductCode/{itemProductCodeId}/file/{fileName} | Attach a file to an itemProductCode
[**add_item_product_code_file_by_url**](ItemProductCodeApi.md#add_item_product_code_file_by_url) | **POST** /beta/itemProductCode/{itemProductCodeId}/file | Attach a file to an itemProductCode by URL.
[**add_item_product_code_tag**](ItemProductCodeApi.md#add_item_product_code_tag) | **PUT** /beta/itemProductCode/{itemProductCodeId}/tag/{itemProductCodeTag} | Add new tags for an itemProductCode.
[**delete_item_product_code**](ItemProductCodeApi.md#delete_item_product_code) | **DELETE** /beta/itemProductCode/{itemProductCodeId} | Delete an itemProductCode
[**delete_item_product_code_file**](ItemProductCodeApi.md#delete_item_product_code_file) | **DELETE** /beta/itemProductCode/{itemProductCodeId}/file/{fileId} | Delete a file for an itemProductCode.
[**delete_item_product_code_tag**](ItemProductCodeApi.md#delete_item_product_code_tag) | **DELETE** /beta/itemProductCode/{itemProductCodeId}/tag/{itemProductCodeTag} | Delete a tag for an itemProductCode.
[**get_duplicate_item_product_code_by_id**](ItemProductCodeApi.md#get_duplicate_item_product_code_by_id) | **GET** /beta/itemProductCode/duplicate/{itemProductCodeId} | Get a duplicated an itemProductCode by id
[**get_item_product_code_by_filter**](ItemProductCodeApi.md#get_item_product_code_by_filter) | **GET** /beta/itemProductCode/search | Search itemProductCodes by filter
[**get_item_product_code_by_id**](ItemProductCodeApi.md#get_item_product_code_by_id) | **GET** /beta/itemProductCode/{itemProductCodeId} | Get an itemProductCode by id
[**get_item_product_code_files**](ItemProductCodeApi.md#get_item_product_code_files) | **GET** /beta/itemProductCode/{itemProductCodeId}/file | Get the files for an itemProductCode.
[**get_item_product_code_tags**](ItemProductCodeApi.md#get_item_product_code_tags) | **GET** /beta/itemProductCode/{itemProductCodeId}/tag | Get the tags for an itemProductCode.
[**update_item_product_code**](ItemProductCodeApi.md#update_item_product_code) | **PUT** /beta/itemProductCode | Update an itemProductCode


# **add_item_product_code**
> ItemProductCode add_item_product_code(body)

Create an itemProductCode

Inserts a new itemProductCode using the specified data.

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
api_instance = Infoplus.ItemProductCodeApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemProductCode() # ItemProductCode | ItemProductCode to be inserted.

try:
    # Create an itemProductCode
    api_response = api_instance.add_item_product_code(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemProductCodeApi->add_item_product_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemProductCode**](ItemProductCode.md)| ItemProductCode to be inserted. | 

### Return type

[**ItemProductCode**](ItemProductCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_product_code_audit**
> add_item_product_code_audit(item_product_code_id, item_product_code_audit)

Add new audit for an itemProductCode

Adds an audit to an existing itemProductCode.

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
api_instance = Infoplus.ItemProductCodeApi(Infoplus.ApiClient(configuration))
item_product_code_id = 56 # int | Id of the itemProductCode to add an audit to
item_product_code_audit = 'item_product_code_audit_example' # str | The audit to add

try:
    # Add new audit for an itemProductCode
    api_instance.add_item_product_code_audit(item_product_code_id, item_product_code_audit)
except ApiException as e:
    print("Exception when calling ItemProductCodeApi->add_item_product_code_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_product_code_id** | **int**| Id of the itemProductCode to add an audit to | 
 **item_product_code_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_product_code_file**
> add_item_product_code_file(item_product_code_id, file_name)

Attach a file to an itemProductCode

Adds a file to an existing itemProductCode.

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
api_instance = Infoplus.ItemProductCodeApi(Infoplus.ApiClient(configuration))
item_product_code_id = 56 # int | Id of the itemProductCode to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an itemProductCode
    api_instance.add_item_product_code_file(item_product_code_id, file_name)
except ApiException as e:
    print("Exception when calling ItemProductCodeApi->add_item_product_code_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_product_code_id** | **int**| Id of the itemProductCode to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_product_code_file_by_url**
> add_item_product_code_file_by_url(body, item_product_code_id)

Attach a file to an itemProductCode by URL.

Adds a file to an existing itemProductCode by URL.

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
api_instance = Infoplus.ItemProductCodeApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
item_product_code_id = 56 # int | Id of the itemProductCode to add an file to

try:
    # Attach a file to an itemProductCode by URL.
    api_instance.add_item_product_code_file_by_url(body, item_product_code_id)
except ApiException as e:
    print("Exception when calling ItemProductCodeApi->add_item_product_code_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **item_product_code_id** | **int**| Id of the itemProductCode to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_product_code_tag**
> add_item_product_code_tag(item_product_code_id, item_product_code_tag)

Add new tags for an itemProductCode.

Adds a tag to an existing itemProductCode.

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
api_instance = Infoplus.ItemProductCodeApi(Infoplus.ApiClient(configuration))
item_product_code_id = 56 # int | Id of the itemProductCode to add a tag to
item_product_code_tag = 'item_product_code_tag_example' # str | The tag to add

try:
    # Add new tags for an itemProductCode.
    api_instance.add_item_product_code_tag(item_product_code_id, item_product_code_tag)
except ApiException as e:
    print("Exception when calling ItemProductCodeApi->add_item_product_code_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_product_code_id** | **int**| Id of the itemProductCode to add a tag to | 
 **item_product_code_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_product_code**
> delete_item_product_code(item_product_code_id)

Delete an itemProductCode

Deletes the itemProductCode identified by the specified id.

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
api_instance = Infoplus.ItemProductCodeApi(Infoplus.ApiClient(configuration))
item_product_code_id = 56 # int | Id of the itemProductCode to be deleted.

try:
    # Delete an itemProductCode
    api_instance.delete_item_product_code(item_product_code_id)
except ApiException as e:
    print("Exception when calling ItemProductCodeApi->delete_item_product_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_product_code_id** | **int**| Id of the itemProductCode to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_product_code_file**
> delete_item_product_code_file(item_product_code_id, file_id)

Delete a file for an itemProductCode.

Deletes an existing itemProductCode file using the specified data.

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
api_instance = Infoplus.ItemProductCodeApi(Infoplus.ApiClient(configuration))
item_product_code_id = 56 # int | Id of the itemProductCode to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an itemProductCode.
    api_instance.delete_item_product_code_file(item_product_code_id, file_id)
except ApiException as e:
    print("Exception when calling ItemProductCodeApi->delete_item_product_code_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_product_code_id** | **int**| Id of the itemProductCode to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_product_code_tag**
> delete_item_product_code_tag(item_product_code_id, item_product_code_tag)

Delete a tag for an itemProductCode.

Deletes an existing itemProductCode tag using the specified data.

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
api_instance = Infoplus.ItemProductCodeApi(Infoplus.ApiClient(configuration))
item_product_code_id = 56 # int | Id of the itemProductCode to remove tag from
item_product_code_tag = 'item_product_code_tag_example' # str | The tag to delete

try:
    # Delete a tag for an itemProductCode.
    api_instance.delete_item_product_code_tag(item_product_code_id, item_product_code_tag)
except ApiException as e:
    print("Exception when calling ItemProductCodeApi->delete_item_product_code_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_product_code_id** | **int**| Id of the itemProductCode to remove tag from | 
 **item_product_code_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_item_product_code_by_id**
> ItemProductCode get_duplicate_item_product_code_by_id(item_product_code_id)

Get a duplicated an itemProductCode by id

Returns a duplicated itemProductCode identified by the specified id.

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
api_instance = Infoplus.ItemProductCodeApi(Infoplus.ApiClient(configuration))
item_product_code_id = 56 # int | Id of the itemProductCode to be duplicated.

try:
    # Get a duplicated an itemProductCode by id
    api_response = api_instance.get_duplicate_item_product_code_by_id(item_product_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemProductCodeApi->get_duplicate_item_product_code_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_product_code_id** | **int**| Id of the itemProductCode to be duplicated. | 

### Return type

[**ItemProductCode**](ItemProductCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_product_code_by_filter**
> list[ItemProductCode] get_item_product_code_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search itemProductCodes by filter

Returns the list of itemProductCodes that match the given filter.

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
api_instance = Infoplus.ItemProductCodeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search itemProductCodes by filter
    api_response = api_instance.get_item_product_code_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemProductCodeApi->get_item_product_code_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ItemProductCode]**](ItemProductCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_product_code_by_id**
> ItemProductCode get_item_product_code_by_id(item_product_code_id)

Get an itemProductCode by id

Returns the itemProductCode identified by the specified id.

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
api_instance = Infoplus.ItemProductCodeApi(Infoplus.ApiClient(configuration))
item_product_code_id = 56 # int | Id of the itemProductCode to be returned.

try:
    # Get an itemProductCode by id
    api_response = api_instance.get_item_product_code_by_id(item_product_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemProductCodeApi->get_item_product_code_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_product_code_id** | **int**| Id of the itemProductCode to be returned. | 

### Return type

[**ItemProductCode**](ItemProductCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_product_code_files**
> get_item_product_code_files(item_product_code_id)

Get the files for an itemProductCode.

Get all existing itemProductCode files.

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
api_instance = Infoplus.ItemProductCodeApi(Infoplus.ApiClient(configuration))
item_product_code_id = 56 # int | Id of the itemProductCode to get files for

try:
    # Get the files for an itemProductCode.
    api_instance.get_item_product_code_files(item_product_code_id)
except ApiException as e:
    print("Exception when calling ItemProductCodeApi->get_item_product_code_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_product_code_id** | **int**| Id of the itemProductCode to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_product_code_tags**
> get_item_product_code_tags(item_product_code_id)

Get the tags for an itemProductCode.

Get all existing itemProductCode tags.

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
api_instance = Infoplus.ItemProductCodeApi(Infoplus.ApiClient(configuration))
item_product_code_id = 56 # int | Id of the itemProductCode to get tags for

try:
    # Get the tags for an itemProductCode.
    api_instance.get_item_product_code_tags(item_product_code_id)
except ApiException as e:
    print("Exception when calling ItemProductCodeApi->get_item_product_code_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_product_code_id** | **int**| Id of the itemProductCode to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_product_code**
> update_item_product_code(body)

Update an itemProductCode

Updates an existing itemProductCode using the specified data.

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
api_instance = Infoplus.ItemProductCodeApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemProductCode() # ItemProductCode | ItemProductCode to be updated.

try:
    # Update an itemProductCode
    api_instance.update_item_product_code(body)
except ApiException as e:
    print("Exception when calling ItemProductCodeApi->update_item_product_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemProductCode**](ItemProductCode.md)| ItemProductCode to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

