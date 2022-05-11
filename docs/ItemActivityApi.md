# Infoplus.ItemActivityApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_activity_audit**](ItemActivityApi.md#add_item_activity_audit) | **PUT** /v3.0/itemActivity/{itemActivityId}/audit/{itemActivityAudit} | Add new audit for an itemActivity
[**add_item_activity_file**](ItemActivityApi.md#add_item_activity_file) | **POST** /v3.0/itemActivity/{itemActivityId}/file/{fileName} | Attach a file to an itemActivity
[**add_item_activity_file_by_url**](ItemActivityApi.md#add_item_activity_file_by_url) | **POST** /v3.0/itemActivity/{itemActivityId}/file | Attach a file to an itemActivity by URL.
[**add_item_activity_tag**](ItemActivityApi.md#add_item_activity_tag) | **PUT** /v3.0/itemActivity/{itemActivityId}/tag/{itemActivityTag} | Add new tags for an itemActivity.
[**delete_item_activity_file**](ItemActivityApi.md#delete_item_activity_file) | **DELETE** /v3.0/itemActivity/{itemActivityId}/file/{fileId} | Delete a file for an itemActivity.
[**delete_item_activity_tag**](ItemActivityApi.md#delete_item_activity_tag) | **DELETE** /v3.0/itemActivity/{itemActivityId}/tag/{itemActivityTag} | Delete a tag for an itemActivity.
[**get_duplicate_item_activity_by_id**](ItemActivityApi.md#get_duplicate_item_activity_by_id) | **GET** /v3.0/itemActivity/duplicate/{itemActivityId} | Get a duplicated an itemActivity by id
[**get_item_activity_by_filter**](ItemActivityApi.md#get_item_activity_by_filter) | **GET** /v3.0/itemActivity/search | Search itemActivitys by filter
[**get_item_activity_by_id**](ItemActivityApi.md#get_item_activity_by_id) | **GET** /v3.0/itemActivity/{itemActivityId} | Get an itemActivity by id
[**get_item_activity_files**](ItemActivityApi.md#get_item_activity_files) | **GET** /v3.0/itemActivity/{itemActivityId}/file | Get the files for an itemActivity.
[**get_item_activity_tags**](ItemActivityApi.md#get_item_activity_tags) | **GET** /v3.0/itemActivity/{itemActivityId}/tag | Get the tags for an itemActivity.


# **add_item_activity_audit**
> add_item_activity_audit(item_activity_id, item_activity_audit)

Add new audit for an itemActivity

Adds an audit to an existing itemActivity.

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
api_instance = Infoplus.ItemActivityApi(Infoplus.ApiClient(configuration))
item_activity_id = 56 # int | Id of the itemActivity to add an audit to
item_activity_audit = 'item_activity_audit_example' # str | The audit to add

try:
    # Add new audit for an itemActivity
    api_instance.add_item_activity_audit(item_activity_id, item_activity_audit)
except ApiException as e:
    print("Exception when calling ItemActivityApi->add_item_activity_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_activity_id** | **int**| Id of the itemActivity to add an audit to | 
 **item_activity_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_activity_file**
> add_item_activity_file(item_activity_id, file_name)

Attach a file to an itemActivity

Adds a file to an existing itemActivity.

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
api_instance = Infoplus.ItemActivityApi(Infoplus.ApiClient(configuration))
item_activity_id = 56 # int | Id of the itemActivity to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an itemActivity
    api_instance.add_item_activity_file(item_activity_id, file_name)
except ApiException as e:
    print("Exception when calling ItemActivityApi->add_item_activity_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_activity_id** | **int**| Id of the itemActivity to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_activity_file_by_url**
> add_item_activity_file_by_url(body, item_activity_id)

Attach a file to an itemActivity by URL.

Adds a file to an existing itemActivity by URL.

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
api_instance = Infoplus.ItemActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
item_activity_id = 56 # int | Id of the itemActivity to add an file to

try:
    # Attach a file to an itemActivity by URL.
    api_instance.add_item_activity_file_by_url(body, item_activity_id)
except ApiException as e:
    print("Exception when calling ItemActivityApi->add_item_activity_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **item_activity_id** | **int**| Id of the itemActivity to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_activity_tag**
> add_item_activity_tag(item_activity_id, item_activity_tag)

Add new tags for an itemActivity.

Adds a tag to an existing itemActivity.

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
api_instance = Infoplus.ItemActivityApi(Infoplus.ApiClient(configuration))
item_activity_id = 56 # int | Id of the itemActivity to add a tag to
item_activity_tag = 'item_activity_tag_example' # str | The tag to add

try:
    # Add new tags for an itemActivity.
    api_instance.add_item_activity_tag(item_activity_id, item_activity_tag)
except ApiException as e:
    print("Exception when calling ItemActivityApi->add_item_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_activity_id** | **int**| Id of the itemActivity to add a tag to | 
 **item_activity_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_activity_file**
> delete_item_activity_file(item_activity_id, file_id)

Delete a file for an itemActivity.

Deletes an existing itemActivity file using the specified data.

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
api_instance = Infoplus.ItemActivityApi(Infoplus.ApiClient(configuration))
item_activity_id = 56 # int | Id of the itemActivity to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an itemActivity.
    api_instance.delete_item_activity_file(item_activity_id, file_id)
except ApiException as e:
    print("Exception when calling ItemActivityApi->delete_item_activity_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_activity_id** | **int**| Id of the itemActivity to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_activity_tag**
> delete_item_activity_tag(item_activity_id, item_activity_tag)

Delete a tag for an itemActivity.

Deletes an existing itemActivity tag using the specified data.

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
api_instance = Infoplus.ItemActivityApi(Infoplus.ApiClient(configuration))
item_activity_id = 56 # int | Id of the itemActivity to remove tag from
item_activity_tag = 'item_activity_tag_example' # str | The tag to delete

try:
    # Delete a tag for an itemActivity.
    api_instance.delete_item_activity_tag(item_activity_id, item_activity_tag)
except ApiException as e:
    print("Exception when calling ItemActivityApi->delete_item_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_activity_id** | **int**| Id of the itemActivity to remove tag from | 
 **item_activity_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_item_activity_by_id**
> ItemActivity get_duplicate_item_activity_by_id(item_activity_id)

Get a duplicated an itemActivity by id

Returns a duplicated itemActivity identified by the specified id.

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
api_instance = Infoplus.ItemActivityApi(Infoplus.ApiClient(configuration))
item_activity_id = 56 # int | Id of the itemActivity to be duplicated.

try:
    # Get a duplicated an itemActivity by id
    api_response = api_instance.get_duplicate_item_activity_by_id(item_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemActivityApi->get_duplicate_item_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_activity_id** | **int**| Id of the itemActivity to be duplicated. | 

### Return type

[**ItemActivity**](ItemActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_activity_by_filter**
> list[ItemActivity] get_item_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search itemActivitys by filter

Returns the list of itemActivitys that match the given filter.

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
api_instance = Infoplus.ItemActivityApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search itemActivitys by filter
    api_response = api_instance.get_item_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemActivityApi->get_item_activity_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ItemActivity]**](ItemActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_activity_by_id**
> ItemActivity get_item_activity_by_id(item_activity_id)

Get an itemActivity by id

Returns the itemActivity identified by the specified id.

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
api_instance = Infoplus.ItemActivityApi(Infoplus.ApiClient(configuration))
item_activity_id = 56 # int | Id of the itemActivity to be returned.

try:
    # Get an itemActivity by id
    api_response = api_instance.get_item_activity_by_id(item_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemActivityApi->get_item_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_activity_id** | **int**| Id of the itemActivity to be returned. | 

### Return type

[**ItemActivity**](ItemActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_activity_files**
> get_item_activity_files(item_activity_id)

Get the files for an itemActivity.

Get all existing itemActivity files.

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
api_instance = Infoplus.ItemActivityApi(Infoplus.ApiClient(configuration))
item_activity_id = 56 # int | Id of the itemActivity to get files for

try:
    # Get the files for an itemActivity.
    api_instance.get_item_activity_files(item_activity_id)
except ApiException as e:
    print("Exception when calling ItemActivityApi->get_item_activity_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_activity_id** | **int**| Id of the itemActivity to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_activity_tags**
> get_item_activity_tags(item_activity_id)

Get the tags for an itemActivity.

Get all existing itemActivity tags.

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
api_instance = Infoplus.ItemActivityApi(Infoplus.ApiClient(configuration))
item_activity_id = 56 # int | Id of the itemActivity to get tags for

try:
    # Get the tags for an itemActivity.
    api_instance.get_item_activity_tags(item_activity_id)
except ApiException as e:
    print("Exception when calling ItemActivityApi->get_item_activity_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_activity_id** | **int**| Id of the itemActivity to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

