# Infoplus.ItemSectorApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_sector**](ItemSectorApi.md#add_item_sector) | **POST** /v3.0/itemSector | Create an itemSector
[**add_item_sector_audit**](ItemSectorApi.md#add_item_sector_audit) | **PUT** /v3.0/itemSector/{itemSectorId}/audit/{itemSectorAudit} | Add new audit for an itemSector
[**add_item_sector_file**](ItemSectorApi.md#add_item_sector_file) | **POST** /v3.0/itemSector/{itemSectorId}/file/{fileName} | Attach a file to an itemSector
[**add_item_sector_file_by_url**](ItemSectorApi.md#add_item_sector_file_by_url) | **POST** /v3.0/itemSector/{itemSectorId}/file | Attach a file to an itemSector by URL.
[**add_item_sector_tag**](ItemSectorApi.md#add_item_sector_tag) | **PUT** /v3.0/itemSector/{itemSectorId}/tag/{itemSectorTag} | Add new tags for an itemSector.
[**delete_item_sector**](ItemSectorApi.md#delete_item_sector) | **DELETE** /v3.0/itemSector/{itemSectorId} | Delete an itemSector
[**delete_item_sector_file**](ItemSectorApi.md#delete_item_sector_file) | **DELETE** /v3.0/itemSector/{itemSectorId}/file/{fileId} | Delete a file for an itemSector.
[**delete_item_sector_tag**](ItemSectorApi.md#delete_item_sector_tag) | **DELETE** /v3.0/itemSector/{itemSectorId}/tag/{itemSectorTag} | Delete a tag for an itemSector.
[**get_duplicate_item_sector_by_id**](ItemSectorApi.md#get_duplicate_item_sector_by_id) | **GET** /v3.0/itemSector/duplicate/{itemSectorId} | Get a duplicated an itemSector by id
[**get_item_sector_by_filter**](ItemSectorApi.md#get_item_sector_by_filter) | **GET** /v3.0/itemSector/search | Search itemSectors by filter
[**get_item_sector_by_id**](ItemSectorApi.md#get_item_sector_by_id) | **GET** /v3.0/itemSector/{itemSectorId} | Get an itemSector by id
[**get_item_sector_files**](ItemSectorApi.md#get_item_sector_files) | **GET** /v3.0/itemSector/{itemSectorId}/file | Get the files for an itemSector.
[**get_item_sector_tags**](ItemSectorApi.md#get_item_sector_tags) | **GET** /v3.0/itemSector/{itemSectorId}/tag | Get the tags for an itemSector.
[**update_item_sector**](ItemSectorApi.md#update_item_sector) | **PUT** /v3.0/itemSector | Update an itemSector


# **add_item_sector**
> ItemSector add_item_sector(body)

Create an itemSector

Inserts a new itemSector using the specified data.

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
api_instance = Infoplus.ItemSectorApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemSector() # ItemSector | ItemSector to be inserted.

try:
    # Create an itemSector
    api_response = api_instance.add_item_sector(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSectorApi->add_item_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemSector**](ItemSector.md)| ItemSector to be inserted. | 

### Return type

[**ItemSector**](ItemSector.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_sector_audit**
> add_item_sector_audit(item_sector_id, item_sector_audit)

Add new audit for an itemSector

Adds an audit to an existing itemSector.

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
api_instance = Infoplus.ItemSectorApi(Infoplus.ApiClient(configuration))
item_sector_id = 56 # int | Id of the itemSector to add an audit to
item_sector_audit = 'item_sector_audit_example' # str | The audit to add

try:
    # Add new audit for an itemSector
    api_instance.add_item_sector_audit(item_sector_id, item_sector_audit)
except ApiException as e:
    print("Exception when calling ItemSectorApi->add_item_sector_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sector_id** | **int**| Id of the itemSector to add an audit to | 
 **item_sector_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_sector_file**
> add_item_sector_file(item_sector_id, file_name)

Attach a file to an itemSector

Adds a file to an existing itemSector.

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
api_instance = Infoplus.ItemSectorApi(Infoplus.ApiClient(configuration))
item_sector_id = 56 # int | Id of the itemSector to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an itemSector
    api_instance.add_item_sector_file(item_sector_id, file_name)
except ApiException as e:
    print("Exception when calling ItemSectorApi->add_item_sector_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sector_id** | **int**| Id of the itemSector to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_sector_file_by_url**
> add_item_sector_file_by_url(body, item_sector_id)

Attach a file to an itemSector by URL.

Adds a file to an existing itemSector by URL.

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
api_instance = Infoplus.ItemSectorApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
item_sector_id = 56 # int | Id of the itemSector to add an file to

try:
    # Attach a file to an itemSector by URL.
    api_instance.add_item_sector_file_by_url(body, item_sector_id)
except ApiException as e:
    print("Exception when calling ItemSectorApi->add_item_sector_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **item_sector_id** | **int**| Id of the itemSector to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_sector_tag**
> add_item_sector_tag(item_sector_id, item_sector_tag)

Add new tags for an itemSector.

Adds a tag to an existing itemSector.

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
api_instance = Infoplus.ItemSectorApi(Infoplus.ApiClient(configuration))
item_sector_id = 56 # int | Id of the itemSector to add a tag to
item_sector_tag = 'item_sector_tag_example' # str | The tag to add

try:
    # Add new tags for an itemSector.
    api_instance.add_item_sector_tag(item_sector_id, item_sector_tag)
except ApiException as e:
    print("Exception when calling ItemSectorApi->add_item_sector_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sector_id** | **int**| Id of the itemSector to add a tag to | 
 **item_sector_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_sector**
> delete_item_sector(item_sector_id)

Delete an itemSector

Deletes the itemSector identified by the specified id.

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
api_instance = Infoplus.ItemSectorApi(Infoplus.ApiClient(configuration))
item_sector_id = 56 # int | Id of the itemSector to be deleted.

try:
    # Delete an itemSector
    api_instance.delete_item_sector(item_sector_id)
except ApiException as e:
    print("Exception when calling ItemSectorApi->delete_item_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sector_id** | **int**| Id of the itemSector to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_sector_file**
> delete_item_sector_file(item_sector_id, file_id)

Delete a file for an itemSector.

Deletes an existing itemSector file using the specified data.

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
api_instance = Infoplus.ItemSectorApi(Infoplus.ApiClient(configuration))
item_sector_id = 56 # int | Id of the itemSector to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an itemSector.
    api_instance.delete_item_sector_file(item_sector_id, file_id)
except ApiException as e:
    print("Exception when calling ItemSectorApi->delete_item_sector_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sector_id** | **int**| Id of the itemSector to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_sector_tag**
> delete_item_sector_tag(item_sector_id, item_sector_tag)

Delete a tag for an itemSector.

Deletes an existing itemSector tag using the specified data.

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
api_instance = Infoplus.ItemSectorApi(Infoplus.ApiClient(configuration))
item_sector_id = 56 # int | Id of the itemSector to remove tag from
item_sector_tag = 'item_sector_tag_example' # str | The tag to delete

try:
    # Delete a tag for an itemSector.
    api_instance.delete_item_sector_tag(item_sector_id, item_sector_tag)
except ApiException as e:
    print("Exception when calling ItemSectorApi->delete_item_sector_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sector_id** | **int**| Id of the itemSector to remove tag from | 
 **item_sector_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_item_sector_by_id**
> ItemSector get_duplicate_item_sector_by_id(item_sector_id)

Get a duplicated an itemSector by id

Returns a duplicated itemSector identified by the specified id.

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
api_instance = Infoplus.ItemSectorApi(Infoplus.ApiClient(configuration))
item_sector_id = 56 # int | Id of the itemSector to be duplicated.

try:
    # Get a duplicated an itemSector by id
    api_response = api_instance.get_duplicate_item_sector_by_id(item_sector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSectorApi->get_duplicate_item_sector_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sector_id** | **int**| Id of the itemSector to be duplicated. | 

### Return type

[**ItemSector**](ItemSector.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_sector_by_filter**
> list[ItemSector] get_item_sector_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search itemSectors by filter

Returns the list of itemSectors that match the given filter.

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
api_instance = Infoplus.ItemSectorApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search itemSectors by filter
    api_response = api_instance.get_item_sector_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSectorApi->get_item_sector_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ItemSector]**](ItemSector.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_sector_by_id**
> ItemSector get_item_sector_by_id(item_sector_id)

Get an itemSector by id

Returns the itemSector identified by the specified id.

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
api_instance = Infoplus.ItemSectorApi(Infoplus.ApiClient(configuration))
item_sector_id = 56 # int | Id of the itemSector to be returned.

try:
    # Get an itemSector by id
    api_response = api_instance.get_item_sector_by_id(item_sector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSectorApi->get_item_sector_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sector_id** | **int**| Id of the itemSector to be returned. | 

### Return type

[**ItemSector**](ItemSector.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_sector_files**
> get_item_sector_files(item_sector_id)

Get the files for an itemSector.

Get all existing itemSector files.

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
api_instance = Infoplus.ItemSectorApi(Infoplus.ApiClient(configuration))
item_sector_id = 56 # int | Id of the itemSector to get files for

try:
    # Get the files for an itemSector.
    api_instance.get_item_sector_files(item_sector_id)
except ApiException as e:
    print("Exception when calling ItemSectorApi->get_item_sector_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sector_id** | **int**| Id of the itemSector to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_sector_tags**
> get_item_sector_tags(item_sector_id)

Get the tags for an itemSector.

Get all existing itemSector tags.

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
api_instance = Infoplus.ItemSectorApi(Infoplus.ApiClient(configuration))
item_sector_id = 56 # int | Id of the itemSector to get tags for

try:
    # Get the tags for an itemSector.
    api_instance.get_item_sector_tags(item_sector_id)
except ApiException as e:
    print("Exception when calling ItemSectorApi->get_item_sector_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_sector_id** | **int**| Id of the itemSector to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_sector**
> update_item_sector(body)

Update an itemSector

Updates an existing itemSector using the specified data.

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
api_instance = Infoplus.ItemSectorApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemSector() # ItemSector | ItemSector to be updated.

try:
    # Update an itemSector
    api_instance.update_item_sector(body)
except ApiException as e:
    print("Exception when calling ItemSectorApi->update_item_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemSector**](ItemSector.md)| ItemSector to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

