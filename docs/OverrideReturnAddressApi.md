# Infoplus.OverrideReturnAddressApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_override_return_address**](OverrideReturnAddressApi.md#add_override_return_address) | **POST** /beta/overrideReturnAddress | Create an overrideReturnAddress
[**add_override_return_address_audit**](OverrideReturnAddressApi.md#add_override_return_address_audit) | **PUT** /beta/overrideReturnAddress/{overrideReturnAddressId}/audit/{overrideReturnAddressAudit} | Add new audit for an overrideReturnAddress
[**add_override_return_address_file**](OverrideReturnAddressApi.md#add_override_return_address_file) | **POST** /beta/overrideReturnAddress/{overrideReturnAddressId}/file/{fileName} | Attach a file to an overrideReturnAddress
[**add_override_return_address_file_by_url**](OverrideReturnAddressApi.md#add_override_return_address_file_by_url) | **POST** /beta/overrideReturnAddress/{overrideReturnAddressId}/file | Attach a file to an overrideReturnAddress by URL.
[**add_override_return_address_tag**](OverrideReturnAddressApi.md#add_override_return_address_tag) | **PUT** /beta/overrideReturnAddress/{overrideReturnAddressId}/tag/{overrideReturnAddressTag} | Add new tags for an overrideReturnAddress.
[**delete_override_return_address**](OverrideReturnAddressApi.md#delete_override_return_address) | **DELETE** /beta/overrideReturnAddress/{overrideReturnAddressId} | Delete an overrideReturnAddress
[**delete_override_return_address_file**](OverrideReturnAddressApi.md#delete_override_return_address_file) | **DELETE** /beta/overrideReturnAddress/{overrideReturnAddressId}/file/{fileId} | Delete a file for an overrideReturnAddress.
[**delete_override_return_address_tag**](OverrideReturnAddressApi.md#delete_override_return_address_tag) | **DELETE** /beta/overrideReturnAddress/{overrideReturnAddressId}/tag/{overrideReturnAddressTag} | Delete a tag for an overrideReturnAddress.
[**get_duplicate_override_return_address_by_id**](OverrideReturnAddressApi.md#get_duplicate_override_return_address_by_id) | **GET** /beta/overrideReturnAddress/duplicate/{overrideReturnAddressId} | Get a duplicated an overrideReturnAddress by id
[**get_override_return_address_by_filter**](OverrideReturnAddressApi.md#get_override_return_address_by_filter) | **GET** /beta/overrideReturnAddress/search | Search overrideReturnAddresses by filter
[**get_override_return_address_by_id**](OverrideReturnAddressApi.md#get_override_return_address_by_id) | **GET** /beta/overrideReturnAddress/{overrideReturnAddressId} | Get an overrideReturnAddress by id
[**get_override_return_address_files**](OverrideReturnAddressApi.md#get_override_return_address_files) | **GET** /beta/overrideReturnAddress/{overrideReturnAddressId}/file | Get the files for an overrideReturnAddress.
[**get_override_return_address_tags**](OverrideReturnAddressApi.md#get_override_return_address_tags) | **GET** /beta/overrideReturnAddress/{overrideReturnAddressId}/tag | Get the tags for an overrideReturnAddress.
[**update_override_return_address**](OverrideReturnAddressApi.md#update_override_return_address) | **PUT** /beta/overrideReturnAddress | Update an overrideReturnAddress
[**update_override_return_address_custom_fields**](OverrideReturnAddressApi.md#update_override_return_address_custom_fields) | **PUT** /beta/overrideReturnAddress/customFields | Update an overrideReturnAddress custom fields


# **add_override_return_address**
> OverrideReturnAddress add_override_return_address(body)

Create an overrideReturnAddress

Inserts a new overrideReturnAddress using the specified data.

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
api_instance = Infoplus.OverrideReturnAddressApi(Infoplus.ApiClient(configuration))
body = Infoplus.OverrideReturnAddress() # OverrideReturnAddress | OverrideReturnAddress to be inserted.

try:
    # Create an overrideReturnAddress
    api_response = api_instance.add_override_return_address(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverrideReturnAddressApi->add_override_return_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OverrideReturnAddress**](OverrideReturnAddress.md)| OverrideReturnAddress to be inserted. | 

### Return type

[**OverrideReturnAddress**](OverrideReturnAddress.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_override_return_address_audit**
> add_override_return_address_audit(override_return_address_id, override_return_address_audit)

Add new audit for an overrideReturnAddress

Adds an audit to an existing overrideReturnAddress.

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
api_instance = Infoplus.OverrideReturnAddressApi(Infoplus.ApiClient(configuration))
override_return_address_id = 56 # int | Id of the overrideReturnAddress to add an audit to
override_return_address_audit = 'override_return_address_audit_example' # str | The audit to add

try:
    # Add new audit for an overrideReturnAddress
    api_instance.add_override_return_address_audit(override_return_address_id, override_return_address_audit)
except ApiException as e:
    print("Exception when calling OverrideReturnAddressApi->add_override_return_address_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **override_return_address_id** | **int**| Id of the overrideReturnAddress to add an audit to | 
 **override_return_address_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_override_return_address_file**
> add_override_return_address_file(override_return_address_id, file_name)

Attach a file to an overrideReturnAddress

Adds a file to an existing overrideReturnAddress.

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
api_instance = Infoplus.OverrideReturnAddressApi(Infoplus.ApiClient(configuration))
override_return_address_id = 56 # int | Id of the overrideReturnAddress to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an overrideReturnAddress
    api_instance.add_override_return_address_file(override_return_address_id, file_name)
except ApiException as e:
    print("Exception when calling OverrideReturnAddressApi->add_override_return_address_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **override_return_address_id** | **int**| Id of the overrideReturnAddress to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_override_return_address_file_by_url**
> add_override_return_address_file_by_url(body, override_return_address_id)

Attach a file to an overrideReturnAddress by URL.

Adds a file to an existing overrideReturnAddress by URL.

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
api_instance = Infoplus.OverrideReturnAddressApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
override_return_address_id = 56 # int | Id of the overrideReturnAddress to add an file to

try:
    # Attach a file to an overrideReturnAddress by URL.
    api_instance.add_override_return_address_file_by_url(body, override_return_address_id)
except ApiException as e:
    print("Exception when calling OverrideReturnAddressApi->add_override_return_address_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **override_return_address_id** | **int**| Id of the overrideReturnAddress to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_override_return_address_tag**
> add_override_return_address_tag(override_return_address_id, override_return_address_tag)

Add new tags for an overrideReturnAddress.

Adds a tag to an existing overrideReturnAddress.

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
api_instance = Infoplus.OverrideReturnAddressApi(Infoplus.ApiClient(configuration))
override_return_address_id = 56 # int | Id of the overrideReturnAddress to add a tag to
override_return_address_tag = 'override_return_address_tag_example' # str | The tag to add

try:
    # Add new tags for an overrideReturnAddress.
    api_instance.add_override_return_address_tag(override_return_address_id, override_return_address_tag)
except ApiException as e:
    print("Exception when calling OverrideReturnAddressApi->add_override_return_address_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **override_return_address_id** | **int**| Id of the overrideReturnAddress to add a tag to | 
 **override_return_address_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_override_return_address**
> delete_override_return_address(override_return_address_id)

Delete an overrideReturnAddress

Deletes the overrideReturnAddress identified by the specified id.

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
api_instance = Infoplus.OverrideReturnAddressApi(Infoplus.ApiClient(configuration))
override_return_address_id = 56 # int | Id of the overrideReturnAddress to be deleted.

try:
    # Delete an overrideReturnAddress
    api_instance.delete_override_return_address(override_return_address_id)
except ApiException as e:
    print("Exception when calling OverrideReturnAddressApi->delete_override_return_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **override_return_address_id** | **int**| Id of the overrideReturnAddress to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_override_return_address_file**
> delete_override_return_address_file(override_return_address_id, file_id)

Delete a file for an overrideReturnAddress.

Deletes an existing overrideReturnAddress file using the specified data.

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
api_instance = Infoplus.OverrideReturnAddressApi(Infoplus.ApiClient(configuration))
override_return_address_id = 56 # int | Id of the overrideReturnAddress to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an overrideReturnAddress.
    api_instance.delete_override_return_address_file(override_return_address_id, file_id)
except ApiException as e:
    print("Exception when calling OverrideReturnAddressApi->delete_override_return_address_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **override_return_address_id** | **int**| Id of the overrideReturnAddress to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_override_return_address_tag**
> delete_override_return_address_tag(override_return_address_id, override_return_address_tag)

Delete a tag for an overrideReturnAddress.

Deletes an existing overrideReturnAddress tag using the specified data.

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
api_instance = Infoplus.OverrideReturnAddressApi(Infoplus.ApiClient(configuration))
override_return_address_id = 56 # int | Id of the overrideReturnAddress to remove tag from
override_return_address_tag = 'override_return_address_tag_example' # str | The tag to delete

try:
    # Delete a tag for an overrideReturnAddress.
    api_instance.delete_override_return_address_tag(override_return_address_id, override_return_address_tag)
except ApiException as e:
    print("Exception when calling OverrideReturnAddressApi->delete_override_return_address_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **override_return_address_id** | **int**| Id of the overrideReturnAddress to remove tag from | 
 **override_return_address_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_override_return_address_by_id**
> OverrideReturnAddress get_duplicate_override_return_address_by_id(override_return_address_id)

Get a duplicated an overrideReturnAddress by id

Returns a duplicated overrideReturnAddress identified by the specified id.

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
api_instance = Infoplus.OverrideReturnAddressApi(Infoplus.ApiClient(configuration))
override_return_address_id = 56 # int | Id of the overrideReturnAddress to be duplicated.

try:
    # Get a duplicated an overrideReturnAddress by id
    api_response = api_instance.get_duplicate_override_return_address_by_id(override_return_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverrideReturnAddressApi->get_duplicate_override_return_address_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **override_return_address_id** | **int**| Id of the overrideReturnAddress to be duplicated. | 

### Return type

[**OverrideReturnAddress**](OverrideReturnAddress.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_override_return_address_by_filter**
> list[OverrideReturnAddress] get_override_return_address_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search overrideReturnAddresses by filter

Returns the list of overrideReturnAddresses that match the given filter.

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
api_instance = Infoplus.OverrideReturnAddressApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search overrideReturnAddresses by filter
    api_response = api_instance.get_override_return_address_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverrideReturnAddressApi->get_override_return_address_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[OverrideReturnAddress]**](OverrideReturnAddress.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_override_return_address_by_id**
> OverrideReturnAddress get_override_return_address_by_id(override_return_address_id)

Get an overrideReturnAddress by id

Returns the overrideReturnAddress identified by the specified id.

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
api_instance = Infoplus.OverrideReturnAddressApi(Infoplus.ApiClient(configuration))
override_return_address_id = 56 # int | Id of the overrideReturnAddress to be returned.

try:
    # Get an overrideReturnAddress by id
    api_response = api_instance.get_override_return_address_by_id(override_return_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverrideReturnAddressApi->get_override_return_address_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **override_return_address_id** | **int**| Id of the overrideReturnAddress to be returned. | 

### Return type

[**OverrideReturnAddress**](OverrideReturnAddress.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_override_return_address_files**
> get_override_return_address_files(override_return_address_id)

Get the files for an overrideReturnAddress.

Get all existing overrideReturnAddress files.

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
api_instance = Infoplus.OverrideReturnAddressApi(Infoplus.ApiClient(configuration))
override_return_address_id = 56 # int | Id of the overrideReturnAddress to get files for

try:
    # Get the files for an overrideReturnAddress.
    api_instance.get_override_return_address_files(override_return_address_id)
except ApiException as e:
    print("Exception when calling OverrideReturnAddressApi->get_override_return_address_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **override_return_address_id** | **int**| Id of the overrideReturnAddress to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_override_return_address_tags**
> get_override_return_address_tags(override_return_address_id)

Get the tags for an overrideReturnAddress.

Get all existing overrideReturnAddress tags.

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
api_instance = Infoplus.OverrideReturnAddressApi(Infoplus.ApiClient(configuration))
override_return_address_id = 56 # int | Id of the overrideReturnAddress to get tags for

try:
    # Get the tags for an overrideReturnAddress.
    api_instance.get_override_return_address_tags(override_return_address_id)
except ApiException as e:
    print("Exception when calling OverrideReturnAddressApi->get_override_return_address_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **override_return_address_id** | **int**| Id of the overrideReturnAddress to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_override_return_address**
> update_override_return_address(body)

Update an overrideReturnAddress

Updates an existing overrideReturnAddress using the specified data.

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
api_instance = Infoplus.OverrideReturnAddressApi(Infoplus.ApiClient(configuration))
body = Infoplus.OverrideReturnAddress() # OverrideReturnAddress | OverrideReturnAddress to be updated.

try:
    # Update an overrideReturnAddress
    api_instance.update_override_return_address(body)
except ApiException as e:
    print("Exception when calling OverrideReturnAddressApi->update_override_return_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OverrideReturnAddress**](OverrideReturnAddress.md)| OverrideReturnAddress to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_override_return_address_custom_fields**
> update_override_return_address_custom_fields(body)

Update an overrideReturnAddress custom fields

Updates an existing overrideReturnAddress custom fields using the specified data.

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
api_instance = Infoplus.OverrideReturnAddressApi(Infoplus.ApiClient(configuration))
body = Infoplus.OverrideReturnAddress() # OverrideReturnAddress | OverrideReturnAddress to be updated.

try:
    # Update an overrideReturnAddress custom fields
    api_instance.update_override_return_address_custom_fields(body)
except ApiException as e:
    print("Exception when calling OverrideReturnAddressApi->update_override_return_address_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OverrideReturnAddress**](OverrideReturnAddress.md)| OverrideReturnAddress to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

