# Infoplus.WorkBatchApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_work_batch_audit**](WorkBatchApi.md#add_work_batch_audit) | **PUT** /beta/workBatch/{workBatchId}/audit/{workBatchAudit} | Add new audit for a workBatch
[**add_work_batch_tag**](WorkBatchApi.md#add_work_batch_tag) | **PUT** /beta/workBatch/{workBatchId}/tag/{workBatchTag} | Add new tags for a workBatch.
[**delete_work_batch_tag**](WorkBatchApi.md#delete_work_batch_tag) | **DELETE** /beta/workBatch/{workBatchId}/tag/{workBatchTag} | Delete a tag for a workBatch.
[**get_duplicate_work_batch_by_id**](WorkBatchApi.md#get_duplicate_work_batch_by_id) | **GET** /beta/workBatch/duplicate/{workBatchId} | Get a duplicated a workBatch by id
[**get_work_batch_by_filter**](WorkBatchApi.md#get_work_batch_by_filter) | **GET** /beta/workBatch/search | Search workBatchs by filter
[**get_work_batch_by_id**](WorkBatchApi.md#get_work_batch_by_id) | **GET** /beta/workBatch/{workBatchId} | Get a workBatch by id
[**get_work_batch_tags**](WorkBatchApi.md#get_work_batch_tags) | **GET** /beta/workBatch/{workBatchId}/tag | Get the tags for a workBatch.
[**update_work_batch**](WorkBatchApi.md#update_work_batch) | **PUT** /beta/workBatch | Update a workBatch
[**update_work_batch_custom_fields**](WorkBatchApi.md#update_work_batch_custom_fields) | **PUT** /beta/workBatch/customFields | Update a workBatch custom fields


# **add_work_batch_audit**
> add_work_batch_audit(work_batch_id, work_batch_audit)

Add new audit for a workBatch

Adds an audit to an existing workBatch.

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
api_instance = Infoplus.WorkBatchApi(Infoplus.ApiClient(configuration))
work_batch_id = 56 # int | Id of the workBatch to add an audit to
work_batch_audit = 'work_batch_audit_example' # str | The audit to add

try:
    # Add new audit for a workBatch
    api_instance.add_work_batch_audit(work_batch_id, work_batch_audit)
except ApiException as e:
    print("Exception when calling WorkBatchApi->add_work_batch_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_batch_id** | **int**| Id of the workBatch to add an audit to | 
 **work_batch_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_work_batch_tag**
> add_work_batch_tag(work_batch_id, work_batch_tag)

Add new tags for a workBatch.

Adds a tag to an existing workBatch.

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
api_instance = Infoplus.WorkBatchApi(Infoplus.ApiClient(configuration))
work_batch_id = 56 # int | Id of the workBatch to add a tag to
work_batch_tag = 'work_batch_tag_example' # str | The tag to add

try:
    # Add new tags for a workBatch.
    api_instance.add_work_batch_tag(work_batch_id, work_batch_tag)
except ApiException as e:
    print("Exception when calling WorkBatchApi->add_work_batch_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_batch_id** | **int**| Id of the workBatch to add a tag to | 
 **work_batch_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_work_batch_tag**
> delete_work_batch_tag(work_batch_id, work_batch_tag)

Delete a tag for a workBatch.

Deletes an existing workBatch tag using the specified data.

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
api_instance = Infoplus.WorkBatchApi(Infoplus.ApiClient(configuration))
work_batch_id = 56 # int | Id of the workBatch to remove tag from
work_batch_tag = 'work_batch_tag_example' # str | The tag to delete

try:
    # Delete a tag for a workBatch.
    api_instance.delete_work_batch_tag(work_batch_id, work_batch_tag)
except ApiException as e:
    print("Exception when calling WorkBatchApi->delete_work_batch_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_batch_id** | **int**| Id of the workBatch to remove tag from | 
 **work_batch_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_work_batch_by_id**
> WorkBatch get_duplicate_work_batch_by_id(work_batch_id)

Get a duplicated a workBatch by id

Returns a duplicated workBatch identified by the specified id.

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
api_instance = Infoplus.WorkBatchApi(Infoplus.ApiClient(configuration))
work_batch_id = 56 # int | Id of the workBatch to be duplicated.

try:
    # Get a duplicated a workBatch by id
    api_response = api_instance.get_duplicate_work_batch_by_id(work_batch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkBatchApi->get_duplicate_work_batch_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_batch_id** | **int**| Id of the workBatch to be duplicated. | 

### Return type

[**WorkBatch**](WorkBatch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_batch_by_filter**
> list[WorkBatch] get_work_batch_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search workBatchs by filter

Returns the list of workBatchs that match the given filter.

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
api_instance = Infoplus.WorkBatchApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search workBatchs by filter
    api_response = api_instance.get_work_batch_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkBatchApi->get_work_batch_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[WorkBatch]**](WorkBatch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_batch_by_id**
> WorkBatch get_work_batch_by_id(work_batch_id)

Get a workBatch by id

Returns the workBatch identified by the specified id.

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
api_instance = Infoplus.WorkBatchApi(Infoplus.ApiClient(configuration))
work_batch_id = 56 # int | Id of the workBatch to be returned.

try:
    # Get a workBatch by id
    api_response = api_instance.get_work_batch_by_id(work_batch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkBatchApi->get_work_batch_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_batch_id** | **int**| Id of the workBatch to be returned. | 

### Return type

[**WorkBatch**](WorkBatch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_batch_tags**
> get_work_batch_tags(work_batch_id)

Get the tags for a workBatch.

Get all existing workBatch tags.

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
api_instance = Infoplus.WorkBatchApi(Infoplus.ApiClient(configuration))
work_batch_id = 56 # int | Id of the workBatch to get tags for

try:
    # Get the tags for a workBatch.
    api_instance.get_work_batch_tags(work_batch_id)
except ApiException as e:
    print("Exception when calling WorkBatchApi->get_work_batch_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_batch_id** | **int**| Id of the workBatch to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_work_batch**
> update_work_batch(body)

Update a workBatch

Updates an existing workBatch using the specified data.

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
api_instance = Infoplus.WorkBatchApi(Infoplus.ApiClient(configuration))
body = Infoplus.WorkBatch() # WorkBatch | WorkBatch to be updated.

try:
    # Update a workBatch
    api_instance.update_work_batch(body)
except ApiException as e:
    print("Exception when calling WorkBatchApi->update_work_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkBatch**](WorkBatch.md)| WorkBatch to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_work_batch_custom_fields**
> update_work_batch_custom_fields(body)

Update a workBatch custom fields

Updates an existing workBatch custom fields using the specified data.

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
api_instance = Infoplus.WorkBatchApi(Infoplus.ApiClient(configuration))
body = Infoplus.WorkBatch() # WorkBatch | WorkBatch to be updated.

try:
    # Update a workBatch custom fields
    api_instance.update_work_batch_custom_fields(body)
except ApiException as e:
    print("Exception when calling WorkBatchApi->update_work_batch_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkBatch**](WorkBatch.md)| WorkBatch to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

