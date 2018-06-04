# Infoplus.WorkApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_work_audit**](WorkApi.md#add_work_audit) | **PUT** /beta/work/{workId}/audit/{workAudit} | Add new audit for a work
[**add_work_tag**](WorkApi.md#add_work_tag) | **PUT** /beta/work/{workId}/tag/{workTag} | Add new tags for a work.
[**delete_work_tag**](WorkApi.md#delete_work_tag) | **DELETE** /beta/work/{workId}/tag/{workTag} | Delete a tag for a work.
[**get_duplicate_work_by_id**](WorkApi.md#get_duplicate_work_by_id) | **GET** /beta/work/duplicate/{workId} | Get a duplicated a work by id
[**get_work_by_filter**](WorkApi.md#get_work_by_filter) | **GET** /beta/work/search | Search works by filter
[**get_work_by_id**](WorkApi.md#get_work_by_id) | **GET** /beta/work/{workId} | Get a work by id
[**get_work_tags**](WorkApi.md#get_work_tags) | **GET** /beta/work/{workId}/tag | Get the tags for a work.
[**update_work_custom_fields**](WorkApi.md#update_work_custom_fields) | **PUT** /beta/work/customFields | Update a work custom fields


# **add_work_audit**
> add_work_audit(work_id, work_audit)

Add new audit for a work

Adds an audit to an existing work.

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
api_instance = Infoplus.WorkApi(Infoplus.ApiClient(configuration))
work_id = 56 # int | Id of the work to add an audit to
work_audit = 'work_audit_example' # str | The audit to add

try:
    # Add new audit for a work
    api_instance.add_work_audit(work_id, work_audit)
except ApiException as e:
    print("Exception when calling WorkApi->add_work_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_id** | **int**| Id of the work to add an audit to | 
 **work_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_work_tag**
> add_work_tag(work_id, work_tag)

Add new tags for a work.

Adds a tag to an existing work.

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
api_instance = Infoplus.WorkApi(Infoplus.ApiClient(configuration))
work_id = 56 # int | Id of the work to add a tag to
work_tag = 'work_tag_example' # str | The tag to add

try:
    # Add new tags for a work.
    api_instance.add_work_tag(work_id, work_tag)
except ApiException as e:
    print("Exception when calling WorkApi->add_work_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_id** | **int**| Id of the work to add a tag to | 
 **work_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_work_tag**
> delete_work_tag(work_id, work_tag)

Delete a tag for a work.

Deletes an existing work tag using the specified data.

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
api_instance = Infoplus.WorkApi(Infoplus.ApiClient(configuration))
work_id = 56 # int | Id of the work to remove tag from
work_tag = 'work_tag_example' # str | The tag to delete

try:
    # Delete a tag for a work.
    api_instance.delete_work_tag(work_id, work_tag)
except ApiException as e:
    print("Exception when calling WorkApi->delete_work_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_id** | **int**| Id of the work to remove tag from | 
 **work_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_work_by_id**
> Work get_duplicate_work_by_id(work_id)

Get a duplicated a work by id

Returns a duplicated work identified by the specified id.

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
api_instance = Infoplus.WorkApi(Infoplus.ApiClient(configuration))
work_id = 56 # int | Id of the work to be duplicated.

try:
    # Get a duplicated a work by id
    api_response = api_instance.get_duplicate_work_by_id(work_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkApi->get_duplicate_work_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_id** | **int**| Id of the work to be duplicated. | 

### Return type

[**Work**](Work.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_by_filter**
> list[Work] get_work_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search works by filter

Returns the list of works that match the given filter.

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
api_instance = Infoplus.WorkApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search works by filter
    api_response = api_instance.get_work_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkApi->get_work_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Work]**](Work.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_by_id**
> Work get_work_by_id(work_id)

Get a work by id

Returns the work identified by the specified id.

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
api_instance = Infoplus.WorkApi(Infoplus.ApiClient(configuration))
work_id = 56 # int | Id of the work to be returned.

try:
    # Get a work by id
    api_response = api_instance.get_work_by_id(work_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkApi->get_work_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_id** | **int**| Id of the work to be returned. | 

### Return type

[**Work**](Work.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_tags**
> get_work_tags(work_id)

Get the tags for a work.

Get all existing work tags.

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
api_instance = Infoplus.WorkApi(Infoplus.ApiClient(configuration))
work_id = 56 # int | Id of the work to get tags for

try:
    # Get the tags for a work.
    api_instance.get_work_tags(work_id)
except ApiException as e:
    print("Exception when calling WorkApi->get_work_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_id** | **int**| Id of the work to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_work_custom_fields**
> update_work_custom_fields(body)

Update a work custom fields

Updates an existing work custom fields using the specified data.

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
api_instance = Infoplus.WorkApi(Infoplus.ApiClient(configuration))
body = Infoplus.Work() # Work | Work to be updated.

try:
    # Update a work custom fields
    api_instance.update_work_custom_fields(body)
except ApiException as e:
    print("Exception when calling WorkApi->update_work_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Work**](Work.md)| Work to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

