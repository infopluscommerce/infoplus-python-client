# Infoplus.LoggedTimeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_logged_time_audit**](LoggedTimeApi.md#add_logged_time_audit) | **PUT** /v3.0/loggedTime/{loggedTimeId}/audit/{loggedTimeAudit} | Add new audit for a loggedTime
[**add_logged_time_file**](LoggedTimeApi.md#add_logged_time_file) | **POST** /v3.0/loggedTime/{loggedTimeId}/file/{fileName} | Attach a file to a loggedTime
[**add_logged_time_file_by_url**](LoggedTimeApi.md#add_logged_time_file_by_url) | **POST** /v3.0/loggedTime/{loggedTimeId}/file | Attach a file to a loggedTime by URL.
[**add_logged_time_tag**](LoggedTimeApi.md#add_logged_time_tag) | **PUT** /v3.0/loggedTime/{loggedTimeId}/tag/{loggedTimeTag} | Add new tags for a loggedTime.
[**delete_logged_time_file**](LoggedTimeApi.md#delete_logged_time_file) | **DELETE** /v3.0/loggedTime/{loggedTimeId}/file/{fileId} | Delete a file for a loggedTime.
[**delete_logged_time_tag**](LoggedTimeApi.md#delete_logged_time_tag) | **DELETE** /v3.0/loggedTime/{loggedTimeId}/tag/{loggedTimeTag} | Delete a tag for a loggedTime.
[**get_duplicate_logged_time_by_id**](LoggedTimeApi.md#get_duplicate_logged_time_by_id) | **GET** /v3.0/loggedTime/duplicate/{loggedTimeId} | Get a duplicated a loggedTime by id
[**get_logged_time_by_filter**](LoggedTimeApi.md#get_logged_time_by_filter) | **GET** /v3.0/loggedTime/search | Search loggedTimes by filter
[**get_logged_time_by_id**](LoggedTimeApi.md#get_logged_time_by_id) | **GET** /v3.0/loggedTime/{loggedTimeId} | Get a loggedTime by id
[**get_logged_time_files**](LoggedTimeApi.md#get_logged_time_files) | **GET** /v3.0/loggedTime/{loggedTimeId}/file | Get the files for a loggedTime.
[**get_logged_time_tags**](LoggedTimeApi.md#get_logged_time_tags) | **GET** /v3.0/loggedTime/{loggedTimeId}/tag | Get the tags for a loggedTime.
[**update_logged_time_custom_fields**](LoggedTimeApi.md#update_logged_time_custom_fields) | **PUT** /v3.0/loggedTime/customFields | Update a loggedTime custom fields


# **add_logged_time_audit**
> add_logged_time_audit(logged_time_id, logged_time_audit)

Add new audit for a loggedTime

Adds an audit to an existing loggedTime.

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
api_instance = Infoplus.LoggedTimeApi(Infoplus.ApiClient(configuration))
logged_time_id = 56 # int | Id of the loggedTime to add an audit to
logged_time_audit = 'logged_time_audit_example' # str | The audit to add

try:
    # Add new audit for a loggedTime
    api_instance.add_logged_time_audit(logged_time_id, logged_time_audit)
except ApiException as e:
    print("Exception when calling LoggedTimeApi->add_logged_time_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logged_time_id** | **int**| Id of the loggedTime to add an audit to | 
 **logged_time_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_logged_time_file**
> add_logged_time_file(logged_time_id, file_name)

Attach a file to a loggedTime

Adds a file to an existing loggedTime.

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
api_instance = Infoplus.LoggedTimeApi(Infoplus.ApiClient(configuration))
logged_time_id = 56 # int | Id of the loggedTime to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a loggedTime
    api_instance.add_logged_time_file(logged_time_id, file_name)
except ApiException as e:
    print("Exception when calling LoggedTimeApi->add_logged_time_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logged_time_id** | **int**| Id of the loggedTime to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_logged_time_file_by_url**
> add_logged_time_file_by_url(body, logged_time_id)

Attach a file to a loggedTime by URL.

Adds a file to an existing loggedTime by URL.

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
api_instance = Infoplus.LoggedTimeApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
logged_time_id = 56 # int | Id of the loggedTime to add an file to

try:
    # Attach a file to a loggedTime by URL.
    api_instance.add_logged_time_file_by_url(body, logged_time_id)
except ApiException as e:
    print("Exception when calling LoggedTimeApi->add_logged_time_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **logged_time_id** | **int**| Id of the loggedTime to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_logged_time_tag**
> add_logged_time_tag(logged_time_id, logged_time_tag)

Add new tags for a loggedTime.

Adds a tag to an existing loggedTime.

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
api_instance = Infoplus.LoggedTimeApi(Infoplus.ApiClient(configuration))
logged_time_id = 56 # int | Id of the loggedTime to add a tag to
logged_time_tag = 'logged_time_tag_example' # str | The tag to add

try:
    # Add new tags for a loggedTime.
    api_instance.add_logged_time_tag(logged_time_id, logged_time_tag)
except ApiException as e:
    print("Exception when calling LoggedTimeApi->add_logged_time_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logged_time_id** | **int**| Id of the loggedTime to add a tag to | 
 **logged_time_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_logged_time_file**
> delete_logged_time_file(logged_time_id, file_id)

Delete a file for a loggedTime.

Deletes an existing loggedTime file using the specified data.

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
api_instance = Infoplus.LoggedTimeApi(Infoplus.ApiClient(configuration))
logged_time_id = 56 # int | Id of the loggedTime to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a loggedTime.
    api_instance.delete_logged_time_file(logged_time_id, file_id)
except ApiException as e:
    print("Exception when calling LoggedTimeApi->delete_logged_time_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logged_time_id** | **int**| Id of the loggedTime to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_logged_time_tag**
> delete_logged_time_tag(logged_time_id, logged_time_tag)

Delete a tag for a loggedTime.

Deletes an existing loggedTime tag using the specified data.

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
api_instance = Infoplus.LoggedTimeApi(Infoplus.ApiClient(configuration))
logged_time_id = 56 # int | Id of the loggedTime to remove tag from
logged_time_tag = 'logged_time_tag_example' # str | The tag to delete

try:
    # Delete a tag for a loggedTime.
    api_instance.delete_logged_time_tag(logged_time_id, logged_time_tag)
except ApiException as e:
    print("Exception when calling LoggedTimeApi->delete_logged_time_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logged_time_id** | **int**| Id of the loggedTime to remove tag from | 
 **logged_time_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_logged_time_by_id**
> LoggedTime get_duplicate_logged_time_by_id(logged_time_id)

Get a duplicated a loggedTime by id

Returns a duplicated loggedTime identified by the specified id.

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
api_instance = Infoplus.LoggedTimeApi(Infoplus.ApiClient(configuration))
logged_time_id = 56 # int | Id of the loggedTime to be duplicated.

try:
    # Get a duplicated a loggedTime by id
    api_response = api_instance.get_duplicate_logged_time_by_id(logged_time_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggedTimeApi->get_duplicate_logged_time_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logged_time_id** | **int**| Id of the loggedTime to be duplicated. | 

### Return type

[**LoggedTime**](LoggedTime.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logged_time_by_filter**
> list[LoggedTime] get_logged_time_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search loggedTimes by filter

Returns the list of loggedTimes that match the given filter.

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
api_instance = Infoplus.LoggedTimeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search loggedTimes by filter
    api_response = api_instance.get_logged_time_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggedTimeApi->get_logged_time_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[LoggedTime]**](LoggedTime.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logged_time_by_id**
> LoggedTime get_logged_time_by_id(logged_time_id)

Get a loggedTime by id

Returns the loggedTime identified by the specified id.

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
api_instance = Infoplus.LoggedTimeApi(Infoplus.ApiClient(configuration))
logged_time_id = 56 # int | Id of the loggedTime to be returned.

try:
    # Get a loggedTime by id
    api_response = api_instance.get_logged_time_by_id(logged_time_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggedTimeApi->get_logged_time_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logged_time_id** | **int**| Id of the loggedTime to be returned. | 

### Return type

[**LoggedTime**](LoggedTime.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logged_time_files**
> get_logged_time_files(logged_time_id)

Get the files for a loggedTime.

Get all existing loggedTime files.

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
api_instance = Infoplus.LoggedTimeApi(Infoplus.ApiClient(configuration))
logged_time_id = 56 # int | Id of the loggedTime to get files for

try:
    # Get the files for a loggedTime.
    api_instance.get_logged_time_files(logged_time_id)
except ApiException as e:
    print("Exception when calling LoggedTimeApi->get_logged_time_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logged_time_id** | **int**| Id of the loggedTime to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logged_time_tags**
> get_logged_time_tags(logged_time_id)

Get the tags for a loggedTime.

Get all existing loggedTime tags.

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
api_instance = Infoplus.LoggedTimeApi(Infoplus.ApiClient(configuration))
logged_time_id = 56 # int | Id of the loggedTime to get tags for

try:
    # Get the tags for a loggedTime.
    api_instance.get_logged_time_tags(logged_time_id)
except ApiException as e:
    print("Exception when calling LoggedTimeApi->get_logged_time_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logged_time_id** | **int**| Id of the loggedTime to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_logged_time_custom_fields**
> update_logged_time_custom_fields(body)

Update a loggedTime custom fields

Updates an existing loggedTime custom fields using the specified data.

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
api_instance = Infoplus.LoggedTimeApi(Infoplus.ApiClient(configuration))
body = Infoplus.LoggedTime() # LoggedTime | LoggedTime to be updated.

try:
    # Update a loggedTime custom fields
    api_instance.update_logged_time_custom_fields(body)
except ApiException as e:
    print("Exception when calling LoggedTimeApi->update_logged_time_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoggedTime**](LoggedTime.md)| LoggedTime to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

