# Infoplus.JobTimeActivityApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_job_time_activity**](JobTimeActivityApi.md#add_job_time_activity) | **POST** /v3.0/jobTimeActivity | Create a jobTimeActivity
[**add_job_time_activity_audit**](JobTimeActivityApi.md#add_job_time_activity_audit) | **PUT** /v3.0/jobTimeActivity/{jobTimeActivityId}/audit/{jobTimeActivityAudit} | Add new audit for a jobTimeActivity
[**add_job_time_activity_file**](JobTimeActivityApi.md#add_job_time_activity_file) | **POST** /v3.0/jobTimeActivity/{jobTimeActivityId}/file/{fileName} | Attach a file to a jobTimeActivity
[**add_job_time_activity_file_by_url**](JobTimeActivityApi.md#add_job_time_activity_file_by_url) | **POST** /v3.0/jobTimeActivity/{jobTimeActivityId}/file | Attach a file to a jobTimeActivity by URL.
[**add_job_time_activity_tag**](JobTimeActivityApi.md#add_job_time_activity_tag) | **PUT** /v3.0/jobTimeActivity/{jobTimeActivityId}/tag/{jobTimeActivityTag} | Add new tags for a jobTimeActivity.
[**delete_job_time_activity**](JobTimeActivityApi.md#delete_job_time_activity) | **DELETE** /v3.0/jobTimeActivity/{jobTimeActivityId} | Delete a jobTimeActivity
[**delete_job_time_activity_file**](JobTimeActivityApi.md#delete_job_time_activity_file) | **DELETE** /v3.0/jobTimeActivity/{jobTimeActivityId}/file/{fileId} | Delete a file for a jobTimeActivity.
[**delete_job_time_activity_tag**](JobTimeActivityApi.md#delete_job_time_activity_tag) | **DELETE** /v3.0/jobTimeActivity/{jobTimeActivityId}/tag/{jobTimeActivityTag} | Delete a tag for a jobTimeActivity.
[**get_duplicate_job_time_activity_by_id**](JobTimeActivityApi.md#get_duplicate_job_time_activity_by_id) | **GET** /v3.0/jobTimeActivity/duplicate/{jobTimeActivityId} | Get a duplicated a jobTimeActivity by id
[**get_job_time_activity_by_filter**](JobTimeActivityApi.md#get_job_time_activity_by_filter) | **GET** /v3.0/jobTimeActivity/search | Search jobTimeActivitys by filter
[**get_job_time_activity_by_id**](JobTimeActivityApi.md#get_job_time_activity_by_id) | **GET** /v3.0/jobTimeActivity/{jobTimeActivityId} | Get a jobTimeActivity by id
[**get_job_time_activity_files**](JobTimeActivityApi.md#get_job_time_activity_files) | **GET** /v3.0/jobTimeActivity/{jobTimeActivityId}/file | Get the files for a jobTimeActivity.
[**get_job_time_activity_tags**](JobTimeActivityApi.md#get_job_time_activity_tags) | **GET** /v3.0/jobTimeActivity/{jobTimeActivityId}/tag | Get the tags for a jobTimeActivity.
[**update_job_time_activity**](JobTimeActivityApi.md#update_job_time_activity) | **PUT** /v3.0/jobTimeActivity | Update a jobTimeActivity


# **add_job_time_activity**
> JobTimeActivity add_job_time_activity(body)

Create a jobTimeActivity

Inserts a new jobTimeActivity using the specified data.

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
api_instance = Infoplus.JobTimeActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.JobTimeActivity() # JobTimeActivity | JobTimeActivity to be inserted.

try:
    # Create a jobTimeActivity
    api_response = api_instance.add_job_time_activity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobTimeActivityApi->add_job_time_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobTimeActivity**](JobTimeActivity.md)| JobTimeActivity to be inserted. | 

### Return type

[**JobTimeActivity**](JobTimeActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_time_activity_audit**
> add_job_time_activity_audit(job_time_activity_id, job_time_activity_audit)

Add new audit for a jobTimeActivity

Adds an audit to an existing jobTimeActivity.

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
api_instance = Infoplus.JobTimeActivityApi(Infoplus.ApiClient(configuration))
job_time_activity_id = 56 # int | Id of the jobTimeActivity to add an audit to
job_time_activity_audit = 'job_time_activity_audit_example' # str | The audit to add

try:
    # Add new audit for a jobTimeActivity
    api_instance.add_job_time_activity_audit(job_time_activity_id, job_time_activity_audit)
except ApiException as e:
    print("Exception when calling JobTimeActivityApi->add_job_time_activity_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_activity_id** | **int**| Id of the jobTimeActivity to add an audit to | 
 **job_time_activity_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_time_activity_file**
> add_job_time_activity_file(job_time_activity_id, file_name)

Attach a file to a jobTimeActivity

Adds a file to an existing jobTimeActivity.

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
api_instance = Infoplus.JobTimeActivityApi(Infoplus.ApiClient(configuration))
job_time_activity_id = 56 # int | Id of the jobTimeActivity to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a jobTimeActivity
    api_instance.add_job_time_activity_file(job_time_activity_id, file_name)
except ApiException as e:
    print("Exception when calling JobTimeActivityApi->add_job_time_activity_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_activity_id** | **int**| Id of the jobTimeActivity to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_time_activity_file_by_url**
> add_job_time_activity_file_by_url(body, job_time_activity_id)

Attach a file to a jobTimeActivity by URL.

Adds a file to an existing jobTimeActivity by URL.

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
api_instance = Infoplus.JobTimeActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
job_time_activity_id = 56 # int | Id of the jobTimeActivity to add an file to

try:
    # Attach a file to a jobTimeActivity by URL.
    api_instance.add_job_time_activity_file_by_url(body, job_time_activity_id)
except ApiException as e:
    print("Exception when calling JobTimeActivityApi->add_job_time_activity_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **job_time_activity_id** | **int**| Id of the jobTimeActivity to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_time_activity_tag**
> add_job_time_activity_tag(job_time_activity_id, job_time_activity_tag)

Add new tags for a jobTimeActivity.

Adds a tag to an existing jobTimeActivity.

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
api_instance = Infoplus.JobTimeActivityApi(Infoplus.ApiClient(configuration))
job_time_activity_id = 56 # int | Id of the jobTimeActivity to add a tag to
job_time_activity_tag = 'job_time_activity_tag_example' # str | The tag to add

try:
    # Add new tags for a jobTimeActivity.
    api_instance.add_job_time_activity_tag(job_time_activity_id, job_time_activity_tag)
except ApiException as e:
    print("Exception when calling JobTimeActivityApi->add_job_time_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_activity_id** | **int**| Id of the jobTimeActivity to add a tag to | 
 **job_time_activity_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_time_activity**
> delete_job_time_activity(job_time_activity_id)

Delete a jobTimeActivity

Deletes the jobTimeActivity identified by the specified id.

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
api_instance = Infoplus.JobTimeActivityApi(Infoplus.ApiClient(configuration))
job_time_activity_id = 56 # int | Id of the jobTimeActivity to be deleted.

try:
    # Delete a jobTimeActivity
    api_instance.delete_job_time_activity(job_time_activity_id)
except ApiException as e:
    print("Exception when calling JobTimeActivityApi->delete_job_time_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_activity_id** | **int**| Id of the jobTimeActivity to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_time_activity_file**
> delete_job_time_activity_file(job_time_activity_id, file_id)

Delete a file for a jobTimeActivity.

Deletes an existing jobTimeActivity file using the specified data.

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
api_instance = Infoplus.JobTimeActivityApi(Infoplus.ApiClient(configuration))
job_time_activity_id = 56 # int | Id of the jobTimeActivity to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a jobTimeActivity.
    api_instance.delete_job_time_activity_file(job_time_activity_id, file_id)
except ApiException as e:
    print("Exception when calling JobTimeActivityApi->delete_job_time_activity_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_activity_id** | **int**| Id of the jobTimeActivity to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_time_activity_tag**
> delete_job_time_activity_tag(job_time_activity_id, job_time_activity_tag)

Delete a tag for a jobTimeActivity.

Deletes an existing jobTimeActivity tag using the specified data.

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
api_instance = Infoplus.JobTimeActivityApi(Infoplus.ApiClient(configuration))
job_time_activity_id = 56 # int | Id of the jobTimeActivity to remove tag from
job_time_activity_tag = 'job_time_activity_tag_example' # str | The tag to delete

try:
    # Delete a tag for a jobTimeActivity.
    api_instance.delete_job_time_activity_tag(job_time_activity_id, job_time_activity_tag)
except ApiException as e:
    print("Exception when calling JobTimeActivityApi->delete_job_time_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_activity_id** | **int**| Id of the jobTimeActivity to remove tag from | 
 **job_time_activity_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_job_time_activity_by_id**
> JobTimeActivity get_duplicate_job_time_activity_by_id(job_time_activity_id)

Get a duplicated a jobTimeActivity by id

Returns a duplicated jobTimeActivity identified by the specified id.

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
api_instance = Infoplus.JobTimeActivityApi(Infoplus.ApiClient(configuration))
job_time_activity_id = 56 # int | Id of the jobTimeActivity to be duplicated.

try:
    # Get a duplicated a jobTimeActivity by id
    api_response = api_instance.get_duplicate_job_time_activity_by_id(job_time_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobTimeActivityApi->get_duplicate_job_time_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_activity_id** | **int**| Id of the jobTimeActivity to be duplicated. | 

### Return type

[**JobTimeActivity**](JobTimeActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_time_activity_by_filter**
> list[JobTimeActivity] get_job_time_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search jobTimeActivitys by filter

Returns the list of jobTimeActivitys that match the given filter.

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
api_instance = Infoplus.JobTimeActivityApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search jobTimeActivitys by filter
    api_response = api_instance.get_job_time_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobTimeActivityApi->get_job_time_activity_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[JobTimeActivity]**](JobTimeActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_time_activity_by_id**
> JobTimeActivity get_job_time_activity_by_id(job_time_activity_id)

Get a jobTimeActivity by id

Returns the jobTimeActivity identified by the specified id.

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
api_instance = Infoplus.JobTimeActivityApi(Infoplus.ApiClient(configuration))
job_time_activity_id = 56 # int | Id of the jobTimeActivity to be returned.

try:
    # Get a jobTimeActivity by id
    api_response = api_instance.get_job_time_activity_by_id(job_time_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobTimeActivityApi->get_job_time_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_activity_id** | **int**| Id of the jobTimeActivity to be returned. | 

### Return type

[**JobTimeActivity**](JobTimeActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_time_activity_files**
> get_job_time_activity_files(job_time_activity_id)

Get the files for a jobTimeActivity.

Get all existing jobTimeActivity files.

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
api_instance = Infoplus.JobTimeActivityApi(Infoplus.ApiClient(configuration))
job_time_activity_id = 56 # int | Id of the jobTimeActivity to get files for

try:
    # Get the files for a jobTimeActivity.
    api_instance.get_job_time_activity_files(job_time_activity_id)
except ApiException as e:
    print("Exception when calling JobTimeActivityApi->get_job_time_activity_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_activity_id** | **int**| Id of the jobTimeActivity to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_time_activity_tags**
> get_job_time_activity_tags(job_time_activity_id)

Get the tags for a jobTimeActivity.

Get all existing jobTimeActivity tags.

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
api_instance = Infoplus.JobTimeActivityApi(Infoplus.ApiClient(configuration))
job_time_activity_id = 56 # int | Id of the jobTimeActivity to get tags for

try:
    # Get the tags for a jobTimeActivity.
    api_instance.get_job_time_activity_tags(job_time_activity_id)
except ApiException as e:
    print("Exception when calling JobTimeActivityApi->get_job_time_activity_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_activity_id** | **int**| Id of the jobTimeActivity to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_time_activity**
> update_job_time_activity(body)

Update a jobTimeActivity

Updates an existing jobTimeActivity using the specified data.

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
api_instance = Infoplus.JobTimeActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.JobTimeActivity() # JobTimeActivity | JobTimeActivity to be updated.

try:
    # Update a jobTimeActivity
    api_instance.update_job_time_activity(body)
except ApiException as e:
    print("Exception when calling JobTimeActivityApi->update_job_time_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobTimeActivity**](JobTimeActivity.md)| JobTimeActivity to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

