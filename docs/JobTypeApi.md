# Infoplus.JobTypeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_job_type**](JobTypeApi.md#add_job_type) | **POST** /beta/jobType | Create a jobType
[**add_job_type_audit**](JobTypeApi.md#add_job_type_audit) | **PUT** /beta/jobType/{jobTypeId}/audit/{jobTypeAudit} | Add new audit for a jobType
[**add_job_type_file**](JobTypeApi.md#add_job_type_file) | **POST** /beta/jobType/{jobTypeId}/file/{fileName} | Attach a file to a jobType
[**add_job_type_file_by_url**](JobTypeApi.md#add_job_type_file_by_url) | **POST** /beta/jobType/{jobTypeId}/file | Attach a file to a jobType by URL.
[**add_job_type_tag**](JobTypeApi.md#add_job_type_tag) | **PUT** /beta/jobType/{jobTypeId}/tag/{jobTypeTag} | Add new tags for a jobType.
[**delete_job_type**](JobTypeApi.md#delete_job_type) | **DELETE** /beta/jobType/{jobTypeId} | Delete a jobType
[**delete_job_type_file**](JobTypeApi.md#delete_job_type_file) | **DELETE** /beta/jobType/{jobTypeId}/file/{fileId} | Delete a file for a jobType.
[**delete_job_type_tag**](JobTypeApi.md#delete_job_type_tag) | **DELETE** /beta/jobType/{jobTypeId}/tag/{jobTypeTag} | Delete a tag for a jobType.
[**get_duplicate_job_type_by_id**](JobTypeApi.md#get_duplicate_job_type_by_id) | **GET** /beta/jobType/duplicate/{jobTypeId} | Get a duplicated a jobType by id
[**get_job_type_by_filter**](JobTypeApi.md#get_job_type_by_filter) | **GET** /beta/jobType/search | Search jobTypes by filter
[**get_job_type_by_id**](JobTypeApi.md#get_job_type_by_id) | **GET** /beta/jobType/{jobTypeId} | Get a jobType by id
[**get_job_type_files**](JobTypeApi.md#get_job_type_files) | **GET** /beta/jobType/{jobTypeId}/file | Get the files for a jobType.
[**get_job_type_tags**](JobTypeApi.md#get_job_type_tags) | **GET** /beta/jobType/{jobTypeId}/tag | Get the tags for a jobType.
[**update_job_type**](JobTypeApi.md#update_job_type) | **PUT** /beta/jobType | Update a jobType
[**update_job_type_custom_fields**](JobTypeApi.md#update_job_type_custom_fields) | **PUT** /beta/jobType/customFields | Update a jobType custom fields


# **add_job_type**
> JobType add_job_type(body)

Create a jobType

Inserts a new jobType using the specified data.

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
api_instance = Infoplus.JobTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.JobType() # JobType | JobType to be inserted.

try:
    # Create a jobType
    api_response = api_instance.add_job_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobTypeApi->add_job_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobType**](JobType.md)| JobType to be inserted. | 

### Return type

[**JobType**](JobType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_type_audit**
> add_job_type_audit(job_type_id, job_type_audit)

Add new audit for a jobType

Adds an audit to an existing jobType.

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
api_instance = Infoplus.JobTypeApi(Infoplus.ApiClient(configuration))
job_type_id = 56 # int | Id of the jobType to add an audit to
job_type_audit = 'job_type_audit_example' # str | The audit to add

try:
    # Add new audit for a jobType
    api_instance.add_job_type_audit(job_type_id, job_type_audit)
except ApiException as e:
    print("Exception when calling JobTypeApi->add_job_type_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type_id** | **int**| Id of the jobType to add an audit to | 
 **job_type_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_type_file**
> add_job_type_file(job_type_id, file_name)

Attach a file to a jobType

Adds a file to an existing jobType.

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
api_instance = Infoplus.JobTypeApi(Infoplus.ApiClient(configuration))
job_type_id = 56 # int | Id of the jobType to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a jobType
    api_instance.add_job_type_file(job_type_id, file_name)
except ApiException as e:
    print("Exception when calling JobTypeApi->add_job_type_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type_id** | **int**| Id of the jobType to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_type_file_by_url**
> add_job_type_file_by_url(body, job_type_id)

Attach a file to a jobType by URL.

Adds a file to an existing jobType by URL.

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
api_instance = Infoplus.JobTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
job_type_id = 56 # int | Id of the jobType to add an file to

try:
    # Attach a file to a jobType by URL.
    api_instance.add_job_type_file_by_url(body, job_type_id)
except ApiException as e:
    print("Exception when calling JobTypeApi->add_job_type_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **job_type_id** | **int**| Id of the jobType to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_type_tag**
> add_job_type_tag(job_type_id, job_type_tag)

Add new tags for a jobType.

Adds a tag to an existing jobType.

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
api_instance = Infoplus.JobTypeApi(Infoplus.ApiClient(configuration))
job_type_id = 56 # int | Id of the jobType to add a tag to
job_type_tag = 'job_type_tag_example' # str | The tag to add

try:
    # Add new tags for a jobType.
    api_instance.add_job_type_tag(job_type_id, job_type_tag)
except ApiException as e:
    print("Exception when calling JobTypeApi->add_job_type_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type_id** | **int**| Id of the jobType to add a tag to | 
 **job_type_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_type**
> delete_job_type(job_type_id)

Delete a jobType

Deletes the jobType identified by the specified id.

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
api_instance = Infoplus.JobTypeApi(Infoplus.ApiClient(configuration))
job_type_id = 56 # int | Id of the jobType to be deleted.

try:
    # Delete a jobType
    api_instance.delete_job_type(job_type_id)
except ApiException as e:
    print("Exception when calling JobTypeApi->delete_job_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type_id** | **int**| Id of the jobType to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_type_file**
> delete_job_type_file(job_type_id, file_id)

Delete a file for a jobType.

Deletes an existing jobType file using the specified data.

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
api_instance = Infoplus.JobTypeApi(Infoplus.ApiClient(configuration))
job_type_id = 56 # int | Id of the jobType to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a jobType.
    api_instance.delete_job_type_file(job_type_id, file_id)
except ApiException as e:
    print("Exception when calling JobTypeApi->delete_job_type_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type_id** | **int**| Id of the jobType to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_type_tag**
> delete_job_type_tag(job_type_id, job_type_tag)

Delete a tag for a jobType.

Deletes an existing jobType tag using the specified data.

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
api_instance = Infoplus.JobTypeApi(Infoplus.ApiClient(configuration))
job_type_id = 56 # int | Id of the jobType to remove tag from
job_type_tag = 'job_type_tag_example' # str | The tag to delete

try:
    # Delete a tag for a jobType.
    api_instance.delete_job_type_tag(job_type_id, job_type_tag)
except ApiException as e:
    print("Exception when calling JobTypeApi->delete_job_type_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type_id** | **int**| Id of the jobType to remove tag from | 
 **job_type_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_job_type_by_id**
> JobType get_duplicate_job_type_by_id(job_type_id)

Get a duplicated a jobType by id

Returns a duplicated jobType identified by the specified id.

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
api_instance = Infoplus.JobTypeApi(Infoplus.ApiClient(configuration))
job_type_id = 56 # int | Id of the jobType to be duplicated.

try:
    # Get a duplicated a jobType by id
    api_response = api_instance.get_duplicate_job_type_by_id(job_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobTypeApi->get_duplicate_job_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type_id** | **int**| Id of the jobType to be duplicated. | 

### Return type

[**JobType**](JobType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_type_by_filter**
> list[JobType] get_job_type_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search jobTypes by filter

Returns the list of jobTypes that match the given filter.

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
api_instance = Infoplus.JobTypeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search jobTypes by filter
    api_response = api_instance.get_job_type_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobTypeApi->get_job_type_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[JobType]**](JobType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_type_by_id**
> JobType get_job_type_by_id(job_type_id)

Get a jobType by id

Returns the jobType identified by the specified id.

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
api_instance = Infoplus.JobTypeApi(Infoplus.ApiClient(configuration))
job_type_id = 56 # int | Id of the jobType to be returned.

try:
    # Get a jobType by id
    api_response = api_instance.get_job_type_by_id(job_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobTypeApi->get_job_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type_id** | **int**| Id of the jobType to be returned. | 

### Return type

[**JobType**](JobType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_type_files**
> get_job_type_files(job_type_id)

Get the files for a jobType.

Get all existing jobType files.

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
api_instance = Infoplus.JobTypeApi(Infoplus.ApiClient(configuration))
job_type_id = 56 # int | Id of the jobType to get files for

try:
    # Get the files for a jobType.
    api_instance.get_job_type_files(job_type_id)
except ApiException as e:
    print("Exception when calling JobTypeApi->get_job_type_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type_id** | **int**| Id of the jobType to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_type_tags**
> get_job_type_tags(job_type_id)

Get the tags for a jobType.

Get all existing jobType tags.

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
api_instance = Infoplus.JobTypeApi(Infoplus.ApiClient(configuration))
job_type_id = 56 # int | Id of the jobType to get tags for

try:
    # Get the tags for a jobType.
    api_instance.get_job_type_tags(job_type_id)
except ApiException as e:
    print("Exception when calling JobTypeApi->get_job_type_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type_id** | **int**| Id of the jobType to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_type**
> update_job_type(body)

Update a jobType

Updates an existing jobType using the specified data.

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
api_instance = Infoplus.JobTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.JobType() # JobType | JobType to be updated.

try:
    # Update a jobType
    api_instance.update_job_type(body)
except ApiException as e:
    print("Exception when calling JobTypeApi->update_job_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobType**](JobType.md)| JobType to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_type_custom_fields**
> update_job_type_custom_fields(body)

Update a jobType custom fields

Updates an existing jobType custom fields using the specified data.

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
api_instance = Infoplus.JobTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.JobType() # JobType | JobType to be updated.

try:
    # Update a jobType custom fields
    api_instance.update_job_type_custom_fields(body)
except ApiException as e:
    print("Exception when calling JobTypeApi->update_job_type_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobType**](JobType.md)| JobType to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

