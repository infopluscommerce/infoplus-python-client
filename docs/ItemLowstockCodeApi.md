# Infoplus.ItemLowstockCodeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_lowstock_code**](ItemLowstockCodeApi.md#add_item_lowstock_code) | **POST** /v3.0/itemLowstockCode | Create an itemLowstockCode
[**add_item_lowstock_code_audit**](ItemLowstockCodeApi.md#add_item_lowstock_code_audit) | **PUT** /v3.0/itemLowstockCode/{itemLowstockCodeId}/audit/{itemLowstockCodeAudit} | Add new audit for an itemLowstockCode
[**add_item_lowstock_code_file**](ItemLowstockCodeApi.md#add_item_lowstock_code_file) | **POST** /v3.0/itemLowstockCode/{itemLowstockCodeId}/file/{fileName} | Attach a file to an itemLowstockCode
[**add_item_lowstock_code_file_by_url**](ItemLowstockCodeApi.md#add_item_lowstock_code_file_by_url) | **POST** /v3.0/itemLowstockCode/{itemLowstockCodeId}/file | Attach a file to an itemLowstockCode by URL.
[**add_item_lowstock_code_tag**](ItemLowstockCodeApi.md#add_item_lowstock_code_tag) | **PUT** /v3.0/itemLowstockCode/{itemLowstockCodeId}/tag/{itemLowstockCodeTag} | Add new tags for an itemLowstockCode.
[**delete_item_lowstock_code**](ItemLowstockCodeApi.md#delete_item_lowstock_code) | **DELETE** /v3.0/itemLowstockCode/{itemLowstockCodeId} | Delete an itemLowstockCode
[**delete_item_lowstock_code_file**](ItemLowstockCodeApi.md#delete_item_lowstock_code_file) | **DELETE** /v3.0/itemLowstockCode/{itemLowstockCodeId}/file/{fileId} | Delete a file for an itemLowstockCode.
[**delete_item_lowstock_code_tag**](ItemLowstockCodeApi.md#delete_item_lowstock_code_tag) | **DELETE** /v3.0/itemLowstockCode/{itemLowstockCodeId}/tag/{itemLowstockCodeTag} | Delete a tag for an itemLowstockCode.
[**get_duplicate_item_lowstock_code_by_id**](ItemLowstockCodeApi.md#get_duplicate_item_lowstock_code_by_id) | **GET** /v3.0/itemLowstockCode/duplicate/{itemLowstockCodeId} | Get a duplicated an itemLowstockCode by id
[**get_item_lowstock_code_by_filter**](ItemLowstockCodeApi.md#get_item_lowstock_code_by_filter) | **GET** /v3.0/itemLowstockCode/search | Search itemLowstockCodes by filter
[**get_item_lowstock_code_by_id**](ItemLowstockCodeApi.md#get_item_lowstock_code_by_id) | **GET** /v3.0/itemLowstockCode/{itemLowstockCodeId} | Get an itemLowstockCode by id
[**get_item_lowstock_code_files**](ItemLowstockCodeApi.md#get_item_lowstock_code_files) | **GET** /v3.0/itemLowstockCode/{itemLowstockCodeId}/file | Get the files for an itemLowstockCode.
[**get_item_lowstock_code_tags**](ItemLowstockCodeApi.md#get_item_lowstock_code_tags) | **GET** /v3.0/itemLowstockCode/{itemLowstockCodeId}/tag | Get the tags for an itemLowstockCode.
[**update_item_lowstock_code**](ItemLowstockCodeApi.md#update_item_lowstock_code) | **PUT** /v3.0/itemLowstockCode | Update an itemLowstockCode


# **add_item_lowstock_code**
> ItemLowstockCode add_item_lowstock_code(body)

Create an itemLowstockCode

Inserts a new itemLowstockCode using the specified data.

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
api_instance = Infoplus.ItemLowstockCodeApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemLowstockCode() # ItemLowstockCode | ItemLowstockCode to be inserted.

try:
    # Create an itemLowstockCode
    api_response = api_instance.add_item_lowstock_code(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLowstockCodeApi->add_item_lowstock_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemLowstockCode**](ItemLowstockCode.md)| ItemLowstockCode to be inserted. | 

### Return type

[**ItemLowstockCode**](ItemLowstockCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_lowstock_code_audit**
> add_item_lowstock_code_audit(item_lowstock_code_id, item_lowstock_code_audit)

Add new audit for an itemLowstockCode

Adds an audit to an existing itemLowstockCode.

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
api_instance = Infoplus.ItemLowstockCodeApi(Infoplus.ApiClient(configuration))
item_lowstock_code_id = 56 # int | Id of the itemLowstockCode to add an audit to
item_lowstock_code_audit = 'item_lowstock_code_audit_example' # str | The audit to add

try:
    # Add new audit for an itemLowstockCode
    api_instance.add_item_lowstock_code_audit(item_lowstock_code_id, item_lowstock_code_audit)
except ApiException as e:
    print("Exception when calling ItemLowstockCodeApi->add_item_lowstock_code_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_lowstock_code_id** | **int**| Id of the itemLowstockCode to add an audit to | 
 **item_lowstock_code_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_lowstock_code_file**
> add_item_lowstock_code_file(item_lowstock_code_id, file_name)

Attach a file to an itemLowstockCode

Adds a file to an existing itemLowstockCode.

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
api_instance = Infoplus.ItemLowstockCodeApi(Infoplus.ApiClient(configuration))
item_lowstock_code_id = 56 # int | Id of the itemLowstockCode to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an itemLowstockCode
    api_instance.add_item_lowstock_code_file(item_lowstock_code_id, file_name)
except ApiException as e:
    print("Exception when calling ItemLowstockCodeApi->add_item_lowstock_code_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_lowstock_code_id** | **int**| Id of the itemLowstockCode to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_lowstock_code_file_by_url**
> add_item_lowstock_code_file_by_url(body, item_lowstock_code_id)

Attach a file to an itemLowstockCode by URL.

Adds a file to an existing itemLowstockCode by URL.

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
api_instance = Infoplus.ItemLowstockCodeApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
item_lowstock_code_id = 56 # int | Id of the itemLowstockCode to add an file to

try:
    # Attach a file to an itemLowstockCode by URL.
    api_instance.add_item_lowstock_code_file_by_url(body, item_lowstock_code_id)
except ApiException as e:
    print("Exception when calling ItemLowstockCodeApi->add_item_lowstock_code_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **item_lowstock_code_id** | **int**| Id of the itemLowstockCode to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_lowstock_code_tag**
> add_item_lowstock_code_tag(item_lowstock_code_id, item_lowstock_code_tag)

Add new tags for an itemLowstockCode.

Adds a tag to an existing itemLowstockCode.

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
api_instance = Infoplus.ItemLowstockCodeApi(Infoplus.ApiClient(configuration))
item_lowstock_code_id = 56 # int | Id of the itemLowstockCode to add a tag to
item_lowstock_code_tag = 'item_lowstock_code_tag_example' # str | The tag to add

try:
    # Add new tags for an itemLowstockCode.
    api_instance.add_item_lowstock_code_tag(item_lowstock_code_id, item_lowstock_code_tag)
except ApiException as e:
    print("Exception when calling ItemLowstockCodeApi->add_item_lowstock_code_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_lowstock_code_id** | **int**| Id of the itemLowstockCode to add a tag to | 
 **item_lowstock_code_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_lowstock_code**
> delete_item_lowstock_code(item_lowstock_code_id)

Delete an itemLowstockCode

Deletes the itemLowstockCode identified by the specified id.

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
api_instance = Infoplus.ItemLowstockCodeApi(Infoplus.ApiClient(configuration))
item_lowstock_code_id = 56 # int | Id of the itemLowstockCode to be deleted.

try:
    # Delete an itemLowstockCode
    api_instance.delete_item_lowstock_code(item_lowstock_code_id)
except ApiException as e:
    print("Exception when calling ItemLowstockCodeApi->delete_item_lowstock_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_lowstock_code_id** | **int**| Id of the itemLowstockCode to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_lowstock_code_file**
> delete_item_lowstock_code_file(item_lowstock_code_id, file_id)

Delete a file for an itemLowstockCode.

Deletes an existing itemLowstockCode file using the specified data.

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
api_instance = Infoplus.ItemLowstockCodeApi(Infoplus.ApiClient(configuration))
item_lowstock_code_id = 56 # int | Id of the itemLowstockCode to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an itemLowstockCode.
    api_instance.delete_item_lowstock_code_file(item_lowstock_code_id, file_id)
except ApiException as e:
    print("Exception when calling ItemLowstockCodeApi->delete_item_lowstock_code_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_lowstock_code_id** | **int**| Id of the itemLowstockCode to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_lowstock_code_tag**
> delete_item_lowstock_code_tag(item_lowstock_code_id, item_lowstock_code_tag)

Delete a tag for an itemLowstockCode.

Deletes an existing itemLowstockCode tag using the specified data.

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
api_instance = Infoplus.ItemLowstockCodeApi(Infoplus.ApiClient(configuration))
item_lowstock_code_id = 56 # int | Id of the itemLowstockCode to remove tag from
item_lowstock_code_tag = 'item_lowstock_code_tag_example' # str | The tag to delete

try:
    # Delete a tag for an itemLowstockCode.
    api_instance.delete_item_lowstock_code_tag(item_lowstock_code_id, item_lowstock_code_tag)
except ApiException as e:
    print("Exception when calling ItemLowstockCodeApi->delete_item_lowstock_code_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_lowstock_code_id** | **int**| Id of the itemLowstockCode to remove tag from | 
 **item_lowstock_code_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_item_lowstock_code_by_id**
> ItemLowstockCode get_duplicate_item_lowstock_code_by_id(item_lowstock_code_id)

Get a duplicated an itemLowstockCode by id

Returns a duplicated itemLowstockCode identified by the specified id.

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
api_instance = Infoplus.ItemLowstockCodeApi(Infoplus.ApiClient(configuration))
item_lowstock_code_id = 56 # int | Id of the itemLowstockCode to be duplicated.

try:
    # Get a duplicated an itemLowstockCode by id
    api_response = api_instance.get_duplicate_item_lowstock_code_by_id(item_lowstock_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLowstockCodeApi->get_duplicate_item_lowstock_code_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_lowstock_code_id** | **int**| Id of the itemLowstockCode to be duplicated. | 

### Return type

[**ItemLowstockCode**](ItemLowstockCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_lowstock_code_by_filter**
> list[ItemLowstockCode] get_item_lowstock_code_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search itemLowstockCodes by filter

Returns the list of itemLowstockCodes that match the given filter.

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
api_instance = Infoplus.ItemLowstockCodeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search itemLowstockCodes by filter
    api_response = api_instance.get_item_lowstock_code_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLowstockCodeApi->get_item_lowstock_code_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ItemLowstockCode]**](ItemLowstockCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_lowstock_code_by_id**
> ItemLowstockCode get_item_lowstock_code_by_id(item_lowstock_code_id)

Get an itemLowstockCode by id

Returns the itemLowstockCode identified by the specified id.

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
api_instance = Infoplus.ItemLowstockCodeApi(Infoplus.ApiClient(configuration))
item_lowstock_code_id = 56 # int | Id of the itemLowstockCode to be returned.

try:
    # Get an itemLowstockCode by id
    api_response = api_instance.get_item_lowstock_code_by_id(item_lowstock_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLowstockCodeApi->get_item_lowstock_code_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_lowstock_code_id** | **int**| Id of the itemLowstockCode to be returned. | 

### Return type

[**ItemLowstockCode**](ItemLowstockCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_lowstock_code_files**
> get_item_lowstock_code_files(item_lowstock_code_id)

Get the files for an itemLowstockCode.

Get all existing itemLowstockCode files.

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
api_instance = Infoplus.ItemLowstockCodeApi(Infoplus.ApiClient(configuration))
item_lowstock_code_id = 56 # int | Id of the itemLowstockCode to get files for

try:
    # Get the files for an itemLowstockCode.
    api_instance.get_item_lowstock_code_files(item_lowstock_code_id)
except ApiException as e:
    print("Exception when calling ItemLowstockCodeApi->get_item_lowstock_code_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_lowstock_code_id** | **int**| Id of the itemLowstockCode to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_lowstock_code_tags**
> get_item_lowstock_code_tags(item_lowstock_code_id)

Get the tags for an itemLowstockCode.

Get all existing itemLowstockCode tags.

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
api_instance = Infoplus.ItemLowstockCodeApi(Infoplus.ApiClient(configuration))
item_lowstock_code_id = 56 # int | Id of the itemLowstockCode to get tags for

try:
    # Get the tags for an itemLowstockCode.
    api_instance.get_item_lowstock_code_tags(item_lowstock_code_id)
except ApiException as e:
    print("Exception when calling ItemLowstockCodeApi->get_item_lowstock_code_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_lowstock_code_id** | **int**| Id of the itemLowstockCode to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_lowstock_code**
> update_item_lowstock_code(body)

Update an itemLowstockCode

Updates an existing itemLowstockCode using the specified data.

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
api_instance = Infoplus.ItemLowstockCodeApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemLowstockCode() # ItemLowstockCode | ItemLowstockCode to be updated.

try:
    # Update an itemLowstockCode
    api_instance.update_item_lowstock_code(body)
except ApiException as e:
    print("Exception when calling ItemLowstockCodeApi->update_item_lowstock_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemLowstockCode**](ItemLowstockCode.md)| ItemLowstockCode to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

