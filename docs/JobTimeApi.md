# Infoplus.JobTimeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_job_time**](JobTimeApi.md#add_job_time) | **POST** /beta/jobTime | Create a jobTime
[**add_job_time_audit**](JobTimeApi.md#add_job_time_audit) | **PUT** /beta/jobTime/{jobTimeId}/audit/{jobTimeAudit} | Add new audit for a jobTime
[**add_job_time_tag**](JobTimeApi.md#add_job_time_tag) | **PUT** /beta/jobTime/{jobTimeId}/tag/{jobTimeTag} | Add new tags for a jobTime.
[**delete_job_time**](JobTimeApi.md#delete_job_time) | **DELETE** /beta/jobTime/{jobTimeId} | Delete a jobTime
[**delete_job_time_tag**](JobTimeApi.md#delete_job_time_tag) | **DELETE** /beta/jobTime/{jobTimeId}/tag/{jobTimeTag} | Delete a tag for a jobTime.
[**get_duplicate_job_time_by_id**](JobTimeApi.md#get_duplicate_job_time_by_id) | **GET** /beta/jobTime/duplicate/{jobTimeId} | Get a duplicated a jobTime by id
[**get_job_time_by_filter**](JobTimeApi.md#get_job_time_by_filter) | **GET** /beta/jobTime/search | Search jobTimes by filter
[**get_job_time_by_id**](JobTimeApi.md#get_job_time_by_id) | **GET** /beta/jobTime/{jobTimeId} | Get a jobTime by id
[**get_job_time_tags**](JobTimeApi.md#get_job_time_tags) | **GET** /beta/jobTime/{jobTimeId}/tag | Get the tags for a jobTime.
[**update_job_time**](JobTimeApi.md#update_job_time) | **PUT** /beta/jobTime | Update a jobTime
[**update_job_time_custom_fields**](JobTimeApi.md#update_job_time_custom_fields) | **PUT** /beta/jobTime/customFields | Update a jobTime custom fields


# **add_job_time**
> JobTime add_job_time(body)

Create a jobTime

Inserts a new jobTime using the specified data.

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
api_instance = Infoplus.JobTimeApi(Infoplus.ApiClient(configuration))
body = Infoplus.JobTime() # JobTime | JobTime to be inserted.

try:
    # Create a jobTime
    api_response = api_instance.add_job_time(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobTimeApi->add_job_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobTime**](JobTime.md)| JobTime to be inserted. | 

### Return type

[**JobTime**](JobTime.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_time_audit**
> add_job_time_audit(job_time_id, job_time_audit)

Add new audit for a jobTime

Adds an audit to an existing jobTime.

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
api_instance = Infoplus.JobTimeApi(Infoplus.ApiClient(configuration))
job_time_id = 56 # int | Id of the jobTime to add an audit to
job_time_audit = 'job_time_audit_example' # str | The audit to add

try:
    # Add new audit for a jobTime
    api_instance.add_job_time_audit(job_time_id, job_time_audit)
except ApiException as e:
    print("Exception when calling JobTimeApi->add_job_time_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_id** | **int**| Id of the jobTime to add an audit to | 
 **job_time_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_time_tag**
> add_job_time_tag(job_time_id, job_time_tag)

Add new tags for a jobTime.

Adds a tag to an existing jobTime.

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
api_instance = Infoplus.JobTimeApi(Infoplus.ApiClient(configuration))
job_time_id = 56 # int | Id of the jobTime to add a tag to
job_time_tag = 'job_time_tag_example' # str | The tag to add

try:
    # Add new tags for a jobTime.
    api_instance.add_job_time_tag(job_time_id, job_time_tag)
except ApiException as e:
    print("Exception when calling JobTimeApi->add_job_time_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_id** | **int**| Id of the jobTime to add a tag to | 
 **job_time_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_time**
> delete_job_time(job_time_id)

Delete a jobTime

Deletes the jobTime identified by the specified id.

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
api_instance = Infoplus.JobTimeApi(Infoplus.ApiClient(configuration))
job_time_id = 56 # int | Id of the jobTime to be deleted.

try:
    # Delete a jobTime
    api_instance.delete_job_time(job_time_id)
except ApiException as e:
    print("Exception when calling JobTimeApi->delete_job_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_id** | **int**| Id of the jobTime to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_time_tag**
> delete_job_time_tag(job_time_id, job_time_tag)

Delete a tag for a jobTime.

Deletes an existing jobTime tag using the specified data.

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
api_instance = Infoplus.JobTimeApi(Infoplus.ApiClient(configuration))
job_time_id = 56 # int | Id of the jobTime to remove tag from
job_time_tag = 'job_time_tag_example' # str | The tag to delete

try:
    # Delete a tag for a jobTime.
    api_instance.delete_job_time_tag(job_time_id, job_time_tag)
except ApiException as e:
    print("Exception when calling JobTimeApi->delete_job_time_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_id** | **int**| Id of the jobTime to remove tag from | 
 **job_time_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_job_time_by_id**
> JobTime get_duplicate_job_time_by_id(job_time_id)

Get a duplicated a jobTime by id

Returns a duplicated jobTime identified by the specified id.

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
api_instance = Infoplus.JobTimeApi(Infoplus.ApiClient(configuration))
job_time_id = 56 # int | Id of the jobTime to be duplicated.

try:
    # Get a duplicated a jobTime by id
    api_response = api_instance.get_duplicate_job_time_by_id(job_time_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobTimeApi->get_duplicate_job_time_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_id** | **int**| Id of the jobTime to be duplicated. | 

### Return type

[**JobTime**](JobTime.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_time_by_filter**
> list[JobTime] get_job_time_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search jobTimes by filter

Returns the list of jobTimes that match the given filter.

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
api_instance = Infoplus.JobTimeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search jobTimes by filter
    api_response = api_instance.get_job_time_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobTimeApi->get_job_time_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[JobTime]**](JobTime.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_time_by_id**
> JobTime get_job_time_by_id(job_time_id)

Get a jobTime by id

Returns the jobTime identified by the specified id.

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
api_instance = Infoplus.JobTimeApi(Infoplus.ApiClient(configuration))
job_time_id = 56 # int | Id of the jobTime to be returned.

try:
    # Get a jobTime by id
    api_response = api_instance.get_job_time_by_id(job_time_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobTimeApi->get_job_time_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_id** | **int**| Id of the jobTime to be returned. | 

### Return type

[**JobTime**](JobTime.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_time_tags**
> get_job_time_tags(job_time_id)

Get the tags for a jobTime.

Get all existing jobTime tags.

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
api_instance = Infoplus.JobTimeApi(Infoplus.ApiClient(configuration))
job_time_id = 56 # int | Id of the jobTime to get tags for

try:
    # Get the tags for a jobTime.
    api_instance.get_job_time_tags(job_time_id)
except ApiException as e:
    print("Exception when calling JobTimeApi->get_job_time_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_time_id** | **int**| Id of the jobTime to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_time**
> update_job_time(body)

Update a jobTime

Updates an existing jobTime using the specified data.

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
api_instance = Infoplus.JobTimeApi(Infoplus.ApiClient(configuration))
body = Infoplus.JobTime() # JobTime | JobTime to be updated.

try:
    # Update a jobTime
    api_instance.update_job_time(body)
except ApiException as e:
    print("Exception when calling JobTimeApi->update_job_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobTime**](JobTime.md)| JobTime to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_time_custom_fields**
> update_job_time_custom_fields(body)

Update a jobTime custom fields

Updates an existing jobTime custom fields using the specified data.

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
api_instance = Infoplus.JobTimeApi(Infoplus.ApiClient(configuration))
body = Infoplus.JobTime() # JobTime | JobTime to be updated.

try:
    # Update a jobTime custom fields
    api_instance.update_job_time_custom_fields(body)
except ApiException as e:
    print("Exception when calling JobTimeApi->update_job_time_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobTime**](JobTime.md)| JobTime to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

