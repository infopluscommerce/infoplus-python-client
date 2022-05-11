# Infoplus.LoadApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_load_audit**](LoadApi.md#add_load_audit) | **PUT** /v3.0/load/{loadId}/audit/{loadAudit} | Add new audit for a load
[**add_load_file**](LoadApi.md#add_load_file) | **POST** /v3.0/load/{loadId}/file/{fileName} | Attach a file to a load
[**add_load_file_by_url**](LoadApi.md#add_load_file_by_url) | **POST** /v3.0/load/{loadId}/file | Attach a file to a load by URL.
[**add_load_tag**](LoadApi.md#add_load_tag) | **PUT** /v3.0/load/{loadId}/tag/{loadTag} | Add new tags for a load.
[**delete_load_file**](LoadApi.md#delete_load_file) | **DELETE** /v3.0/load/{loadId}/file/{fileId} | Delete a file for a load.
[**delete_load_tag**](LoadApi.md#delete_load_tag) | **DELETE** /v3.0/load/{loadId}/tag/{loadTag} | Delete a tag for a load.
[**get_duplicate_load_by_id**](LoadApi.md#get_duplicate_load_by_id) | **GET** /v3.0/load/duplicate/{loadId} | Get a duplicated a load by id
[**get_load_by_filter**](LoadApi.md#get_load_by_filter) | **GET** /v3.0/load/search | Search loads by filter
[**get_load_by_id**](LoadApi.md#get_load_by_id) | **GET** /v3.0/load/{loadId} | Get a load by id
[**get_load_files**](LoadApi.md#get_load_files) | **GET** /v3.0/load/{loadId}/file | Get the files for a load.
[**get_load_tags**](LoadApi.md#get_load_tags) | **GET** /v3.0/load/{loadId}/tag | Get the tags for a load.
[**update_load_custom_fields**](LoadApi.md#update_load_custom_fields) | **PUT** /v3.0/load/customFields | Update a load custom fields


# **add_load_audit**
> add_load_audit(load_id, load_audit)

Add new audit for a load

Adds an audit to an existing load.

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
api_instance = Infoplus.LoadApi(Infoplus.ApiClient(configuration))
load_id = 56 # int | Id of the load to add an audit to
load_audit = 'load_audit_example' # str | The audit to add

try:
    # Add new audit for a load
    api_instance.add_load_audit(load_id, load_audit)
except ApiException as e:
    print("Exception when calling LoadApi->add_load_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_id** | **int**| Id of the load to add an audit to | 
 **load_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_load_file**
> add_load_file(load_id, file_name)

Attach a file to a load

Adds a file to an existing load.

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
api_instance = Infoplus.LoadApi(Infoplus.ApiClient(configuration))
load_id = 56 # int | Id of the load to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a load
    api_instance.add_load_file(load_id, file_name)
except ApiException as e:
    print("Exception when calling LoadApi->add_load_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_id** | **int**| Id of the load to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_load_file_by_url**
> add_load_file_by_url(body, load_id)

Attach a file to a load by URL.

Adds a file to an existing load by URL.

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
api_instance = Infoplus.LoadApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
load_id = 56 # int | Id of the load to add an file to

try:
    # Attach a file to a load by URL.
    api_instance.add_load_file_by_url(body, load_id)
except ApiException as e:
    print("Exception when calling LoadApi->add_load_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **load_id** | **int**| Id of the load to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_load_tag**
> add_load_tag(load_id, load_tag)

Add new tags for a load.

Adds a tag to an existing load.

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
api_instance = Infoplus.LoadApi(Infoplus.ApiClient(configuration))
load_id = 56 # int | Id of the load to add a tag to
load_tag = 'load_tag_example' # str | The tag to add

try:
    # Add new tags for a load.
    api_instance.add_load_tag(load_id, load_tag)
except ApiException as e:
    print("Exception when calling LoadApi->add_load_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_id** | **int**| Id of the load to add a tag to | 
 **load_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_file**
> delete_load_file(load_id, file_id)

Delete a file for a load.

Deletes an existing load file using the specified data.

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
api_instance = Infoplus.LoadApi(Infoplus.ApiClient(configuration))
load_id = 56 # int | Id of the load to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a load.
    api_instance.delete_load_file(load_id, file_id)
except ApiException as e:
    print("Exception when calling LoadApi->delete_load_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_id** | **int**| Id of the load to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_tag**
> delete_load_tag(load_id, load_tag)

Delete a tag for a load.

Deletes an existing load tag using the specified data.

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
api_instance = Infoplus.LoadApi(Infoplus.ApiClient(configuration))
load_id = 56 # int | Id of the load to remove tag from
load_tag = 'load_tag_example' # str | The tag to delete

try:
    # Delete a tag for a load.
    api_instance.delete_load_tag(load_id, load_tag)
except ApiException as e:
    print("Exception when calling LoadApi->delete_load_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_id** | **int**| Id of the load to remove tag from | 
 **load_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_load_by_id**
> Load get_duplicate_load_by_id(load_id)

Get a duplicated a load by id

Returns a duplicated load identified by the specified id.

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
api_instance = Infoplus.LoadApi(Infoplus.ApiClient(configuration))
load_id = 56 # int | Id of the load to be duplicated.

try:
    # Get a duplicated a load by id
    api_response = api_instance.get_duplicate_load_by_id(load_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadApi->get_duplicate_load_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_id** | **int**| Id of the load to be duplicated. | 

### Return type

[**Load**](Load.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_by_filter**
> list[Load] get_load_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search loads by filter

Returns the list of loads that match the given filter.

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
api_instance = Infoplus.LoadApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search loads by filter
    api_response = api_instance.get_load_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadApi->get_load_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Load]**](Load.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_by_id**
> Load get_load_by_id(load_id)

Get a load by id

Returns the load identified by the specified id.

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
api_instance = Infoplus.LoadApi(Infoplus.ApiClient(configuration))
load_id = 56 # int | Id of the load to be returned.

try:
    # Get a load by id
    api_response = api_instance.get_load_by_id(load_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadApi->get_load_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_id** | **int**| Id of the load to be returned. | 

### Return type

[**Load**](Load.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_files**
> get_load_files(load_id)

Get the files for a load.

Get all existing load files.

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
api_instance = Infoplus.LoadApi(Infoplus.ApiClient(configuration))
load_id = 56 # int | Id of the load to get files for

try:
    # Get the files for a load.
    api_instance.get_load_files(load_id)
except ApiException as e:
    print("Exception when calling LoadApi->get_load_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_id** | **int**| Id of the load to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_tags**
> get_load_tags(load_id)

Get the tags for a load.

Get all existing load tags.

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
api_instance = Infoplus.LoadApi(Infoplus.ApiClient(configuration))
load_id = 56 # int | Id of the load to get tags for

try:
    # Get the tags for a load.
    api_instance.get_load_tags(load_id)
except ApiException as e:
    print("Exception when calling LoadApi->get_load_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_id** | **int**| Id of the load to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_load_custom_fields**
> update_load_custom_fields(body)

Update a load custom fields

Updates an existing load custom fields using the specified data.

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
api_instance = Infoplus.LoadApi(Infoplus.ApiClient(configuration))
body = Infoplus.Load() # Load | Load to be updated.

try:
    # Update a load custom fields
    api_instance.update_load_custom_fields(body)
except ApiException as e:
    print("Exception when calling LoadApi->update_load_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Load**](Load.md)| Load to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

