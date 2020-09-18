# Infoplus.ItemSerialApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_serial**](ItemSerialApi.md#add_item_serial) | **POST** /beta/itemSerial | Create an itemSerial
[**add_item_serial_audit**](ItemSerialApi.md#add_item_serial_audit) | **PUT** /beta/itemSerial/{itemSerialId}/audit/{itemSerialAudit} | Add new audit for an itemSerial
[**add_item_serial_file**](ItemSerialApi.md#add_item_serial_file) | **POST** /beta/itemSerial/{itemSerialId}/file/{fileName} | Attach a file to an itemSerial
[**add_item_serial_file_by_url**](ItemSerialApi.md#add_item_serial_file_by_url) | **POST** /beta/itemSerial/{itemSerialId}/file | Attach a file to an itemSerial by URL.
[**add_item_serial_tag**](ItemSerialApi.md#add_item_serial_tag) | **PUT** /beta/itemSerial/{itemSerialId}/tag/{itemSerialTag} | Add new tags for an itemSerial.
[**delete_item_serial**](ItemSerialApi.md#delete_item_serial) | **DELETE** /beta/itemSerial/{itemSerialId} | Delete an itemSerial
[**delete_item_serial_file**](ItemSerialApi.md#delete_item_serial_file) | **DELETE** /beta/itemSerial/{itemSerialId}/file/{fileId} | Delete a file for an itemSerial.
[**delete_item_serial_tag**](ItemSerialApi.md#delete_item_serial_tag) | **DELETE** /beta/itemSerial/{itemSerialId}/tag/{itemSerialTag} | Delete a tag for an itemSerial.
[**get_duplicate_item_serial_by_id**](ItemSerialApi.md#get_duplicate_item_serial_by_id) | **GET** /beta/itemSerial/duplicate/{itemSerialId} | Get a duplicated an itemSerial by id
[**get_item_serial_by_filter**](ItemSerialApi.md#get_item_serial_by_filter) | **GET** /beta/itemSerial/search | Search itemSerials by filter
[**get_item_serial_by_id**](ItemSerialApi.md#get_item_serial_by_id) | **GET** /beta/itemSerial/{itemSerialId} | Get an itemSerial by id
[**get_item_serial_files**](ItemSerialApi.md#get_item_serial_files) | **GET** /beta/itemSerial/{itemSerialId}/file | Get the files for an itemSerial.
[**get_item_serial_tags**](ItemSerialApi.md#get_item_serial_tags) | **GET** /beta/itemSerial/{itemSerialId}/tag | Get the tags for an itemSerial.
[**update_item_serial**](ItemSerialApi.md#update_item_serial) | **PUT** /beta/itemSerial | Update an itemSerial


# **add_item_serial**
> ItemSerial add_item_serial(body)

Create an itemSerial

Inserts a new itemSerial using the specified data.

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
api_instance = Infoplus.ItemSerialApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemSerial() # ItemSerial | ItemSerial to be inserted.

try:
    # Create an itemSerial
    api_response = api_instance.add_item_serial(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSerialApi->add_item_serial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemSerial**](ItemSerial.md)| ItemSerial to be inserted. | 

### Return type

[**ItemSerial**](ItemSerial.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_serial_audit**
> add_item_serial_audit(item_serial_id, item_serial_audit)

Add new audit for an itemSerial

Adds an audit to an existing itemSerial.

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
api_instance = Infoplus.ItemSerialApi(Infoplus.ApiClient(configuration))
item_serial_id = 56 # int | Id of the itemSerial to add an audit to
item_serial_audit = 'item_serial_audit_example' # str | The audit to add

try:
    # Add new audit for an itemSerial
    api_instance.add_item_serial_audit(item_serial_id, item_serial_audit)
except ApiException as e:
    print("Exception when calling ItemSerialApi->add_item_serial_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_id** | **int**| Id of the itemSerial to add an audit to | 
 **item_serial_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_serial_file**
> add_item_serial_file(item_serial_id, file_name)

Attach a file to an itemSerial

Adds a file to an existing itemSerial.

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
api_instance = Infoplus.ItemSerialApi(Infoplus.ApiClient(configuration))
item_serial_id = 56 # int | Id of the itemSerial to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an itemSerial
    api_instance.add_item_serial_file(item_serial_id, file_name)
except ApiException as e:
    print("Exception when calling ItemSerialApi->add_item_serial_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_id** | **int**| Id of the itemSerial to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_serial_file_by_url**
> add_item_serial_file_by_url(body, item_serial_id)

Attach a file to an itemSerial by URL.

Adds a file to an existing itemSerial by URL.

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
api_instance = Infoplus.ItemSerialApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
item_serial_id = 56 # int | Id of the itemSerial to add an file to

try:
    # Attach a file to an itemSerial by URL.
    api_instance.add_item_serial_file_by_url(body, item_serial_id)
except ApiException as e:
    print("Exception when calling ItemSerialApi->add_item_serial_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **item_serial_id** | **int**| Id of the itemSerial to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_serial_tag**
> add_item_serial_tag(item_serial_id, item_serial_tag)

Add new tags for an itemSerial.

Adds a tag to an existing itemSerial.

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
api_instance = Infoplus.ItemSerialApi(Infoplus.ApiClient(configuration))
item_serial_id = 56 # int | Id of the itemSerial to add a tag to
item_serial_tag = 'item_serial_tag_example' # str | The tag to add

try:
    # Add new tags for an itemSerial.
    api_instance.add_item_serial_tag(item_serial_id, item_serial_tag)
except ApiException as e:
    print("Exception when calling ItemSerialApi->add_item_serial_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_id** | **int**| Id of the itemSerial to add a tag to | 
 **item_serial_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_serial**
> delete_item_serial(item_serial_id)

Delete an itemSerial

Deletes the itemSerial identified by the specified id.

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
api_instance = Infoplus.ItemSerialApi(Infoplus.ApiClient(configuration))
item_serial_id = 56 # int | Id of the itemSerial to be deleted.

try:
    # Delete an itemSerial
    api_instance.delete_item_serial(item_serial_id)
except ApiException as e:
    print("Exception when calling ItemSerialApi->delete_item_serial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_id** | **int**| Id of the itemSerial to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_serial_file**
> delete_item_serial_file(item_serial_id, file_id)

Delete a file for an itemSerial.

Deletes an existing itemSerial file using the specified data.

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
api_instance = Infoplus.ItemSerialApi(Infoplus.ApiClient(configuration))
item_serial_id = 56 # int | Id of the itemSerial to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an itemSerial.
    api_instance.delete_item_serial_file(item_serial_id, file_id)
except ApiException as e:
    print("Exception when calling ItemSerialApi->delete_item_serial_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_id** | **int**| Id of the itemSerial to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_serial_tag**
> delete_item_serial_tag(item_serial_id, item_serial_tag)

Delete a tag for an itemSerial.

Deletes an existing itemSerial tag using the specified data.

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
api_instance = Infoplus.ItemSerialApi(Infoplus.ApiClient(configuration))
item_serial_id = 56 # int | Id of the itemSerial to remove tag from
item_serial_tag = 'item_serial_tag_example' # str | The tag to delete

try:
    # Delete a tag for an itemSerial.
    api_instance.delete_item_serial_tag(item_serial_id, item_serial_tag)
except ApiException as e:
    print("Exception when calling ItemSerialApi->delete_item_serial_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_id** | **int**| Id of the itemSerial to remove tag from | 
 **item_serial_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_item_serial_by_id**
> ItemSerial get_duplicate_item_serial_by_id(item_serial_id)

Get a duplicated an itemSerial by id

Returns a duplicated itemSerial identified by the specified id.

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
api_instance = Infoplus.ItemSerialApi(Infoplus.ApiClient(configuration))
item_serial_id = 56 # int | Id of the itemSerial to be duplicated.

try:
    # Get a duplicated an itemSerial by id
    api_response = api_instance.get_duplicate_item_serial_by_id(item_serial_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSerialApi->get_duplicate_item_serial_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_id** | **int**| Id of the itemSerial to be duplicated. | 

### Return type

[**ItemSerial**](ItemSerial.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_serial_by_filter**
> list[ItemSerial] get_item_serial_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search itemSerials by filter

Returns the list of itemSerials that match the given filter.

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
api_instance = Infoplus.ItemSerialApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search itemSerials by filter
    api_response = api_instance.get_item_serial_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSerialApi->get_item_serial_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ItemSerial]**](ItemSerial.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_serial_by_id**
> ItemSerial get_item_serial_by_id(item_serial_id)

Get an itemSerial by id

Returns the itemSerial identified by the specified id.

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
api_instance = Infoplus.ItemSerialApi(Infoplus.ApiClient(configuration))
item_serial_id = 56 # int | Id of the itemSerial to be returned.

try:
    # Get an itemSerial by id
    api_response = api_instance.get_item_serial_by_id(item_serial_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSerialApi->get_item_serial_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_id** | **int**| Id of the itemSerial to be returned. | 

### Return type

[**ItemSerial**](ItemSerial.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_serial_files**
> get_item_serial_files(item_serial_id)

Get the files for an itemSerial.

Get all existing itemSerial files.

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
api_instance = Infoplus.ItemSerialApi(Infoplus.ApiClient(configuration))
item_serial_id = 56 # int | Id of the itemSerial to get files for

try:
    # Get the files for an itemSerial.
    api_instance.get_item_serial_files(item_serial_id)
except ApiException as e:
    print("Exception when calling ItemSerialApi->get_item_serial_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_id** | **int**| Id of the itemSerial to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_serial_tags**
> get_item_serial_tags(item_serial_id)

Get the tags for an itemSerial.

Get all existing itemSerial tags.

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
api_instance = Infoplus.ItemSerialApi(Infoplus.ApiClient(configuration))
item_serial_id = 56 # int | Id of the itemSerial to get tags for

try:
    # Get the tags for an itemSerial.
    api_instance.get_item_serial_tags(item_serial_id)
except ApiException as e:
    print("Exception when calling ItemSerialApi->get_item_serial_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_id** | **int**| Id of the itemSerial to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_serial**
> update_item_serial(body)

Update an itemSerial

Updates an existing itemSerial using the specified data.

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
api_instance = Infoplus.ItemSerialApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemSerial() # ItemSerial | ItemSerial to be updated.

try:
    # Update an itemSerial
    api_instance.update_item_serial(body)
except ApiException as e:
    print("Exception when calling ItemSerialApi->update_item_serial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemSerial**](ItemSerial.md)| ItemSerial to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

