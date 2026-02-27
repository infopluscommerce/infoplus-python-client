# Infoplus.JobApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_job**](JobApi.md#add_job) | **POST** /beta/job | Create a job
[**add_job_audit**](JobApi.md#add_job_audit) | **PUT** /beta/job/{jobId}/audit/{jobAudit} | Add new audit for a job
[**add_job_file**](JobApi.md#add_job_file) | **POST** /beta/job/{jobId}/file/{fileName} | Attach a file to a job
[**add_job_file_by_url**](JobApi.md#add_job_file_by_url) | **POST** /beta/job/{jobId}/file | Attach a file to a job by URL.
[**add_job_tag**](JobApi.md#add_job_tag) | **PUT** /beta/job/{jobId}/tag/{jobTag} | Add new tags for a job.
[**delete_job**](JobApi.md#delete_job) | **DELETE** /beta/job/{jobId} | Delete a job
[**delete_job_file**](JobApi.md#delete_job_file) | **DELETE** /beta/job/{jobId}/file/{fileId} | Delete a file for a job.
[**delete_job_tag**](JobApi.md#delete_job_tag) | **DELETE** /beta/job/{jobId}/tag/{jobTag} | Delete a tag for a job.
[**execute_job**](JobApi.md#execute_job) | **POST** /beta/job/executeJob | Run the ExecuteJob process.
[**get_duplicate_job_by_id**](JobApi.md#get_duplicate_job_by_id) | **GET** /beta/job/duplicate/{jobId} | Get a duplicated a job by id
[**get_job_by_filter**](JobApi.md#get_job_by_filter) | **GET** /beta/job/search | Search jobs by filter
[**get_job_by_id**](JobApi.md#get_job_by_id) | **GET** /beta/job/{jobId} | Get a job by id
[**get_job_files**](JobApi.md#get_job_files) | **GET** /beta/job/{jobId}/file | Get the files for a job.
[**get_job_tags**](JobApi.md#get_job_tags) | **GET** /beta/job/{jobId}/tag | Get the tags for a job.
[**update_job**](JobApi.md#update_job) | **PUT** /beta/job | Update a job
[**update_job_custom_fields**](JobApi.md#update_job_custom_fields) | **PUT** /beta/job/customFields | Update a job custom fields


# **add_job**
> Job add_job(body)

Create a job

Inserts a new job using the specified data.

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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
body = Infoplus.Job() # Job | Job to be inserted.

try:
    # Create a job
    api_response = api_instance.add_job(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->add_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Job**](Job.md)| Job to be inserted. | 

### Return type

[**Job**](Job.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_audit**
> add_job_audit(job_id, job_audit)

Add new audit for a job

Adds an audit to an existing job.

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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
job_id = 56 # int | Id of the job to add an audit to
job_audit = 'job_audit_example' # str | The audit to add

try:
    # Add new audit for a job
    api_instance.add_job_audit(job_id, job_audit)
except ApiException as e:
    print("Exception when calling JobApi->add_job_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Id of the job to add an audit to | 
 **job_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_file**
> add_job_file(job_id, file_name)

Attach a file to a job

Adds a file to an existing job.

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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
job_id = 56 # int | Id of the job to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a job
    api_instance.add_job_file(job_id, file_name)
except ApiException as e:
    print("Exception when calling JobApi->add_job_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Id of the job to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_file_by_url**
> add_job_file_by_url(body, job_id)

Attach a file to a job by URL.

Adds a file to an existing job by URL.

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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
job_id = 56 # int | Id of the job to add an file to

try:
    # Attach a file to a job by URL.
    api_instance.add_job_file_by_url(body, job_id)
except ApiException as e:
    print("Exception when calling JobApi->add_job_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **job_id** | **int**| Id of the job to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_tag**
> add_job_tag(job_id, job_tag)

Add new tags for a job.

Adds a tag to an existing job.

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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
job_id = 56 # int | Id of the job to add a tag to
job_tag = 'job_tag_example' # str | The tag to add

try:
    # Add new tags for a job.
    api_instance.add_job_tag(job_id, job_tag)
except ApiException as e:
    print("Exception when calling JobApi->add_job_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Id of the job to add a tag to | 
 **job_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job**
> delete_job(job_id)

Delete a job

Deletes the job identified by the specified id.

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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
job_id = 56 # int | Id of the job to be deleted.

try:
    # Delete a job
    api_instance.delete_job(job_id)
except ApiException as e:
    print("Exception when calling JobApi->delete_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Id of the job to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_file**
> delete_job_file(job_id, file_id)

Delete a file for a job.

Deletes an existing job file using the specified data.

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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
job_id = 56 # int | Id of the job to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a job.
    api_instance.delete_job_file(job_id, file_id)
except ApiException as e:
    print("Exception when calling JobApi->delete_job_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Id of the job to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_tag**
> delete_job_tag(job_id, job_tag)

Delete a tag for a job.

Deletes an existing job tag using the specified data.

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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
job_id = 56 # int | Id of the job to remove tag from
job_tag = 'job_tag_example' # str | The tag to delete

try:
    # Delete a tag for a job.
    api_instance.delete_job_tag(job_id, job_tag)
except ApiException as e:
    print("Exception when calling JobApi->delete_job_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Id of the job to remove tag from | 
 **job_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_job**
> list[ProcessOutputAPIModel] execute_job(body)

Run the ExecuteJob process.



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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
body = Infoplus.ExecuteJobInputAPIModel() # ExecuteJobInputAPIModel | Input data for ExecuteJob process.

try:
    # Run the ExecuteJob process.
    api_response = api_instance.execute_job(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->execute_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExecuteJobInputAPIModel**](ExecuteJobInputAPIModel.md)| Input data for ExecuteJob process. | 

### Return type

[**list[ProcessOutputAPIModel]**](ProcessOutputAPIModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_job_by_id**
> Job get_duplicate_job_by_id(job_id)

Get a duplicated a job by id

Returns a duplicated job identified by the specified id.

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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
job_id = 56 # int | Id of the job to be duplicated.

try:
    # Get a duplicated a job by id
    api_response = api_instance.get_duplicate_job_by_id(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_duplicate_job_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Id of the job to be duplicated. | 

### Return type

[**Job**](Job.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_by_filter**
> list[Job] get_job_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search jobs by filter

Returns the list of jobs that match the given filter.

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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search jobs by filter
    api_response = api_instance.get_job_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_job_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Job]**](Job.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_by_id**
> Job get_job_by_id(job_id)

Get a job by id

Returns the job identified by the specified id.

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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
job_id = 56 # int | Id of the job to be returned.

try:
    # Get a job by id
    api_response = api_instance.get_job_by_id(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_job_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Id of the job to be returned. | 

### Return type

[**Job**](Job.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_files**
> get_job_files(job_id)

Get the files for a job.

Get all existing job files.

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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
job_id = 56 # int | Id of the job to get files for

try:
    # Get the files for a job.
    api_instance.get_job_files(job_id)
except ApiException as e:
    print("Exception when calling JobApi->get_job_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Id of the job to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_tags**
> get_job_tags(job_id)

Get the tags for a job.

Get all existing job tags.

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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
job_id = 56 # int | Id of the job to get tags for

try:
    # Get the tags for a job.
    api_instance.get_job_tags(job_id)
except ApiException as e:
    print("Exception when calling JobApi->get_job_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Id of the job to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job**
> update_job(body)

Update a job

Updates an existing job using the specified data.

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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
body = Infoplus.Job() # Job | Job to be updated.

try:
    # Update a job
    api_instance.update_job(body)
except ApiException as e:
    print("Exception when calling JobApi->update_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Job**](Job.md)| Job to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_custom_fields**
> update_job_custom_fields(body)

Update a job custom fields

Updates an existing job custom fields using the specified data.

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
api_instance = Infoplus.JobApi(Infoplus.ApiClient(configuration))
body = Infoplus.Job() # Job | Job to be updated.

try:
    # Update a job custom fields
    api_instance.update_job_custom_fields(body)
except ApiException as e:
    print("Exception when calling JobApi->update_job_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Job**](Job.md)| Job to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

