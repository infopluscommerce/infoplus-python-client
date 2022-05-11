# Infoplus.WorkActivityApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_work_activity**](WorkActivityApi.md#add_work_activity) | **POST** /v3.0/workActivity | Create a workActivity
[**add_work_activity_audit**](WorkActivityApi.md#add_work_activity_audit) | **PUT** /v3.0/workActivity/{workActivityId}/audit/{workActivityAudit} | Add new audit for a workActivity
[**add_work_activity_file**](WorkActivityApi.md#add_work_activity_file) | **POST** /v3.0/workActivity/{workActivityId}/file/{fileName} | Attach a file to a workActivity
[**add_work_activity_file_by_url**](WorkActivityApi.md#add_work_activity_file_by_url) | **POST** /v3.0/workActivity/{workActivityId}/file | Attach a file to a workActivity by URL.
[**add_work_activity_tag**](WorkActivityApi.md#add_work_activity_tag) | **PUT** /v3.0/workActivity/{workActivityId}/tag/{workActivityTag} | Add new tags for a workActivity.
[**delete_work_activity**](WorkActivityApi.md#delete_work_activity) | **DELETE** /v3.0/workActivity/{workActivityId} | Delete a workActivity
[**delete_work_activity_file**](WorkActivityApi.md#delete_work_activity_file) | **DELETE** /v3.0/workActivity/{workActivityId}/file/{fileId} | Delete a file for a workActivity.
[**delete_work_activity_tag**](WorkActivityApi.md#delete_work_activity_tag) | **DELETE** /v3.0/workActivity/{workActivityId}/tag/{workActivityTag} | Delete a tag for a workActivity.
[**get_duplicate_work_activity_by_id**](WorkActivityApi.md#get_duplicate_work_activity_by_id) | **GET** /v3.0/workActivity/duplicate/{workActivityId} | Get a duplicated a workActivity by id
[**get_work_activity_by_filter**](WorkActivityApi.md#get_work_activity_by_filter) | **GET** /v3.0/workActivity/search | Search workActivitys by filter
[**get_work_activity_by_id**](WorkActivityApi.md#get_work_activity_by_id) | **GET** /v3.0/workActivity/{workActivityId} | Get a workActivity by id
[**get_work_activity_files**](WorkActivityApi.md#get_work_activity_files) | **GET** /v3.0/workActivity/{workActivityId}/file | Get the files for a workActivity.
[**get_work_activity_tags**](WorkActivityApi.md#get_work_activity_tags) | **GET** /v3.0/workActivity/{workActivityId}/tag | Get the tags for a workActivity.
[**update_work_activity**](WorkActivityApi.md#update_work_activity) | **PUT** /v3.0/workActivity | Update a workActivity


# **add_work_activity**
> WorkActivity add_work_activity(body)

Create a workActivity

Inserts a new workActivity using the specified data.

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
api_instance = Infoplus.WorkActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.WorkActivity() # WorkActivity | WorkActivity to be inserted.

try:
    # Create a workActivity
    api_response = api_instance.add_work_activity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkActivityApi->add_work_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkActivity**](WorkActivity.md)| WorkActivity to be inserted. | 

### Return type

[**WorkActivity**](WorkActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_work_activity_audit**
> add_work_activity_audit(work_activity_id, work_activity_audit)

Add new audit for a workActivity

Adds an audit to an existing workActivity.

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
api_instance = Infoplus.WorkActivityApi(Infoplus.ApiClient(configuration))
work_activity_id = 56 # int | Id of the workActivity to add an audit to
work_activity_audit = 'work_activity_audit_example' # str | The audit to add

try:
    # Add new audit for a workActivity
    api_instance.add_work_activity_audit(work_activity_id, work_activity_audit)
except ApiException as e:
    print("Exception when calling WorkActivityApi->add_work_activity_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_activity_id** | **int**| Id of the workActivity to add an audit to | 
 **work_activity_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_work_activity_file**
> add_work_activity_file(work_activity_id, file_name)

Attach a file to a workActivity

Adds a file to an existing workActivity.

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
api_instance = Infoplus.WorkActivityApi(Infoplus.ApiClient(configuration))
work_activity_id = 56 # int | Id of the workActivity to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a workActivity
    api_instance.add_work_activity_file(work_activity_id, file_name)
except ApiException as e:
    print("Exception when calling WorkActivityApi->add_work_activity_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_activity_id** | **int**| Id of the workActivity to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_work_activity_file_by_url**
> add_work_activity_file_by_url(body, work_activity_id)

Attach a file to a workActivity by URL.

Adds a file to an existing workActivity by URL.

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
api_instance = Infoplus.WorkActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
work_activity_id = 56 # int | Id of the workActivity to add an file to

try:
    # Attach a file to a workActivity by URL.
    api_instance.add_work_activity_file_by_url(body, work_activity_id)
except ApiException as e:
    print("Exception when calling WorkActivityApi->add_work_activity_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **work_activity_id** | **int**| Id of the workActivity to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_work_activity_tag**
> add_work_activity_tag(work_activity_id, work_activity_tag)

Add new tags for a workActivity.

Adds a tag to an existing workActivity.

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
api_instance = Infoplus.WorkActivityApi(Infoplus.ApiClient(configuration))
work_activity_id = 56 # int | Id of the workActivity to add a tag to
work_activity_tag = 'work_activity_tag_example' # str | The tag to add

try:
    # Add new tags for a workActivity.
    api_instance.add_work_activity_tag(work_activity_id, work_activity_tag)
except ApiException as e:
    print("Exception when calling WorkActivityApi->add_work_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_activity_id** | **int**| Id of the workActivity to add a tag to | 
 **work_activity_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_work_activity**
> delete_work_activity(work_activity_id)

Delete a workActivity

Deletes the workActivity identified by the specified id.

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
api_instance = Infoplus.WorkActivityApi(Infoplus.ApiClient(configuration))
work_activity_id = 56 # int | Id of the workActivity to be deleted.

try:
    # Delete a workActivity
    api_instance.delete_work_activity(work_activity_id)
except ApiException as e:
    print("Exception when calling WorkActivityApi->delete_work_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_activity_id** | **int**| Id of the workActivity to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_work_activity_file**
> delete_work_activity_file(work_activity_id, file_id)

Delete a file for a workActivity.

Deletes an existing workActivity file using the specified data.

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
api_instance = Infoplus.WorkActivityApi(Infoplus.ApiClient(configuration))
work_activity_id = 56 # int | Id of the workActivity to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a workActivity.
    api_instance.delete_work_activity_file(work_activity_id, file_id)
except ApiException as e:
    print("Exception when calling WorkActivityApi->delete_work_activity_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_activity_id** | **int**| Id of the workActivity to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_work_activity_tag**
> delete_work_activity_tag(work_activity_id, work_activity_tag)

Delete a tag for a workActivity.

Deletes an existing workActivity tag using the specified data.

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
api_instance = Infoplus.WorkActivityApi(Infoplus.ApiClient(configuration))
work_activity_id = 56 # int | Id of the workActivity to remove tag from
work_activity_tag = 'work_activity_tag_example' # str | The tag to delete

try:
    # Delete a tag for a workActivity.
    api_instance.delete_work_activity_tag(work_activity_id, work_activity_tag)
except ApiException as e:
    print("Exception when calling WorkActivityApi->delete_work_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_activity_id** | **int**| Id of the workActivity to remove tag from | 
 **work_activity_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_work_activity_by_id**
> WorkActivity get_duplicate_work_activity_by_id(work_activity_id)

Get a duplicated a workActivity by id

Returns a duplicated workActivity identified by the specified id.

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
api_instance = Infoplus.WorkActivityApi(Infoplus.ApiClient(configuration))
work_activity_id = 56 # int | Id of the workActivity to be duplicated.

try:
    # Get a duplicated a workActivity by id
    api_response = api_instance.get_duplicate_work_activity_by_id(work_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkActivityApi->get_duplicate_work_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_activity_id** | **int**| Id of the workActivity to be duplicated. | 

### Return type

[**WorkActivity**](WorkActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_activity_by_filter**
> list[WorkActivity] get_work_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search workActivitys by filter

Returns the list of workActivitys that match the given filter.

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
api_instance = Infoplus.WorkActivityApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search workActivitys by filter
    api_response = api_instance.get_work_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkActivityApi->get_work_activity_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[WorkActivity]**](WorkActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_activity_by_id**
> WorkActivity get_work_activity_by_id(work_activity_id)

Get a workActivity by id

Returns the workActivity identified by the specified id.

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
api_instance = Infoplus.WorkActivityApi(Infoplus.ApiClient(configuration))
work_activity_id = 56 # int | Id of the workActivity to be returned.

try:
    # Get a workActivity by id
    api_response = api_instance.get_work_activity_by_id(work_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkActivityApi->get_work_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_activity_id** | **int**| Id of the workActivity to be returned. | 

### Return type

[**WorkActivity**](WorkActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_activity_files**
> get_work_activity_files(work_activity_id)

Get the files for a workActivity.

Get all existing workActivity files.

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
api_instance = Infoplus.WorkActivityApi(Infoplus.ApiClient(configuration))
work_activity_id = 56 # int | Id of the workActivity to get files for

try:
    # Get the files for a workActivity.
    api_instance.get_work_activity_files(work_activity_id)
except ApiException as e:
    print("Exception when calling WorkActivityApi->get_work_activity_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_activity_id** | **int**| Id of the workActivity to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_activity_tags**
> get_work_activity_tags(work_activity_id)

Get the tags for a workActivity.

Get all existing workActivity tags.

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
api_instance = Infoplus.WorkActivityApi(Infoplus.ApiClient(configuration))
work_activity_id = 56 # int | Id of the workActivity to get tags for

try:
    # Get the tags for a workActivity.
    api_instance.get_work_activity_tags(work_activity_id)
except ApiException as e:
    print("Exception when calling WorkActivityApi->get_work_activity_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_activity_id** | **int**| Id of the workActivity to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_work_activity**
> update_work_activity(body)

Update a workActivity

Updates an existing workActivity using the specified data.

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
api_instance = Infoplus.WorkActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.WorkActivity() # WorkActivity | WorkActivity to be updated.

try:
    # Update a workActivity
    api_instance.update_work_activity(body)
except ApiException as e:
    print("Exception when calling WorkActivityApi->update_work_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkActivity**](WorkActivity.md)| WorkActivity to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

