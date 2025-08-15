# Infoplus.DropshipApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dropship_audit**](DropshipApi.md#add_dropship_audit) | **PUT** /beta/dropship/{dropshipId}/audit/{dropshipAudit} | Add new audit for a dropship
[**add_dropship_file**](DropshipApi.md#add_dropship_file) | **POST** /beta/dropship/{dropshipId}/file/{fileName} | Attach a file to a dropship
[**add_dropship_file_by_url**](DropshipApi.md#add_dropship_file_by_url) | **POST** /beta/dropship/{dropshipId}/file | Attach a file to a dropship by URL.
[**add_dropship_tag**](DropshipApi.md#add_dropship_tag) | **PUT** /beta/dropship/{dropshipId}/tag/{dropshipTag} | Add new tags for a dropship.
[**delete_dropship_file**](DropshipApi.md#delete_dropship_file) | **DELETE** /beta/dropship/{dropshipId}/file/{fileId} | Delete a file for a dropship.
[**delete_dropship_tag**](DropshipApi.md#delete_dropship_tag) | **DELETE** /beta/dropship/{dropshipId}/tag/{dropshipTag} | Delete a tag for a dropship.
[**get_dropship_by_filter**](DropshipApi.md#get_dropship_by_filter) | **GET** /beta/dropship/search | Search dropships by filter
[**get_dropship_by_id**](DropshipApi.md#get_dropship_by_id) | **GET** /beta/dropship/{dropshipId} | Get a dropship by id
[**get_dropship_files**](DropshipApi.md#get_dropship_files) | **GET** /beta/dropship/{dropshipId}/file | Get the files for a dropship.
[**get_dropship_tags**](DropshipApi.md#get_dropship_tags) | **GET** /beta/dropship/{dropshipId}/tag | Get the tags for a dropship.
[**get_duplicate_dropship_by_id**](DropshipApi.md#get_duplicate_dropship_by_id) | **GET** /beta/dropship/duplicate/{dropshipId} | Get a duplicated a dropship by id
[**update_dropship**](DropshipApi.md#update_dropship) | **PUT** /beta/dropship | Update a dropship


# **add_dropship_audit**
> add_dropship_audit(dropship_id, dropship_audit)

Add new audit for a dropship

Adds an audit to an existing dropship.

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
api_instance = Infoplus.DropshipApi(Infoplus.ApiClient(configuration))
dropship_id = 56 # int | Id of the dropship to add an audit to
dropship_audit = 'dropship_audit_example' # str | The audit to add

try:
    # Add new audit for a dropship
    api_instance.add_dropship_audit(dropship_id, dropship_audit)
except ApiException as e:
    print("Exception when calling DropshipApi->add_dropship_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dropship_id** | **int**| Id of the dropship to add an audit to | 
 **dropship_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dropship_file**
> add_dropship_file(dropship_id, file_name)

Attach a file to a dropship

Adds a file to an existing dropship.

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
api_instance = Infoplus.DropshipApi(Infoplus.ApiClient(configuration))
dropship_id = 56 # int | Id of the dropship to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a dropship
    api_instance.add_dropship_file(dropship_id, file_name)
except ApiException as e:
    print("Exception when calling DropshipApi->add_dropship_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dropship_id** | **int**| Id of the dropship to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dropship_file_by_url**
> add_dropship_file_by_url(body, dropship_id)

Attach a file to a dropship by URL.

Adds a file to an existing dropship by URL.

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
api_instance = Infoplus.DropshipApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
dropship_id = 56 # int | Id of the dropship to add an file to

try:
    # Attach a file to a dropship by URL.
    api_instance.add_dropship_file_by_url(body, dropship_id)
except ApiException as e:
    print("Exception when calling DropshipApi->add_dropship_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **dropship_id** | **int**| Id of the dropship to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dropship_tag**
> add_dropship_tag(dropship_id, dropship_tag)

Add new tags for a dropship.

Adds a tag to an existing dropship.

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
api_instance = Infoplus.DropshipApi(Infoplus.ApiClient(configuration))
dropship_id = 56 # int | Id of the dropship to add a tag to
dropship_tag = 'dropship_tag_example' # str | The tag to add

try:
    # Add new tags for a dropship.
    api_instance.add_dropship_tag(dropship_id, dropship_tag)
except ApiException as e:
    print("Exception when calling DropshipApi->add_dropship_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dropship_id** | **int**| Id of the dropship to add a tag to | 
 **dropship_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dropship_file**
> delete_dropship_file(dropship_id, file_id)

Delete a file for a dropship.

Deletes an existing dropship file using the specified data.

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
api_instance = Infoplus.DropshipApi(Infoplus.ApiClient(configuration))
dropship_id = 56 # int | Id of the dropship to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a dropship.
    api_instance.delete_dropship_file(dropship_id, file_id)
except ApiException as e:
    print("Exception when calling DropshipApi->delete_dropship_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dropship_id** | **int**| Id of the dropship to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dropship_tag**
> delete_dropship_tag(dropship_id, dropship_tag)

Delete a tag for a dropship.

Deletes an existing dropship tag using the specified data.

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
api_instance = Infoplus.DropshipApi(Infoplus.ApiClient(configuration))
dropship_id = 56 # int | Id of the dropship to remove tag from
dropship_tag = 'dropship_tag_example' # str | The tag to delete

try:
    # Delete a tag for a dropship.
    api_instance.delete_dropship_tag(dropship_id, dropship_tag)
except ApiException as e:
    print("Exception when calling DropshipApi->delete_dropship_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dropship_id** | **int**| Id of the dropship to remove tag from | 
 **dropship_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dropship_by_filter**
> list[Dropship] get_dropship_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search dropships by filter

Returns the list of dropships that match the given filter.

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
api_instance = Infoplus.DropshipApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search dropships by filter
    api_response = api_instance.get_dropship_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DropshipApi->get_dropship_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Dropship]**](Dropship.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dropship_by_id**
> Dropship get_dropship_by_id(dropship_id)

Get a dropship by id

Returns the dropship identified by the specified id.

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
api_instance = Infoplus.DropshipApi(Infoplus.ApiClient(configuration))
dropship_id = 56 # int | Id of the dropship to be returned.

try:
    # Get a dropship by id
    api_response = api_instance.get_dropship_by_id(dropship_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DropshipApi->get_dropship_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dropship_id** | **int**| Id of the dropship to be returned. | 

### Return type

[**Dropship**](Dropship.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dropship_files**
> get_dropship_files(dropship_id)

Get the files for a dropship.

Get all existing dropship files.

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
api_instance = Infoplus.DropshipApi(Infoplus.ApiClient(configuration))
dropship_id = 56 # int | Id of the dropship to get files for

try:
    # Get the files for a dropship.
    api_instance.get_dropship_files(dropship_id)
except ApiException as e:
    print("Exception when calling DropshipApi->get_dropship_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dropship_id** | **int**| Id of the dropship to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dropship_tags**
> get_dropship_tags(dropship_id)

Get the tags for a dropship.

Get all existing dropship tags.

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
api_instance = Infoplus.DropshipApi(Infoplus.ApiClient(configuration))
dropship_id = 56 # int | Id of the dropship to get tags for

try:
    # Get the tags for a dropship.
    api_instance.get_dropship_tags(dropship_id)
except ApiException as e:
    print("Exception when calling DropshipApi->get_dropship_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dropship_id** | **int**| Id of the dropship to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_dropship_by_id**
> Dropship get_duplicate_dropship_by_id(dropship_id)

Get a duplicated a dropship by id

Returns a duplicated dropship identified by the specified id.

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
api_instance = Infoplus.DropshipApi(Infoplus.ApiClient(configuration))
dropship_id = 56 # int | Id of the dropship to be duplicated.

try:
    # Get a duplicated a dropship by id
    api_response = api_instance.get_duplicate_dropship_by_id(dropship_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DropshipApi->get_duplicate_dropship_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dropship_id** | **int**| Id of the dropship to be duplicated. | 

### Return type

[**Dropship**](Dropship.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dropship**
> update_dropship(body)

Update a dropship

Updates an existing dropship using the specified data.

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
api_instance = Infoplus.DropshipApi(Infoplus.ApiClient(configuration))
body = Infoplus.Dropship() # Dropship | Dropship to be updated.

try:
    # Update a dropship
    api_instance.update_dropship(body)
except ApiException as e:
    print("Exception when calling DropshipApi->update_dropship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dropship**](Dropship.md)| Dropship to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

