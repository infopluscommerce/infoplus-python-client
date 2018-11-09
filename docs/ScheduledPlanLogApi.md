# Infoplus.ScheduledPlanLogApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_scheduled_plan_log_audit**](ScheduledPlanLogApi.md#add_scheduled_plan_log_audit) | **PUT** /beta/scheduledPlanLog/{scheduledPlanLogId}/audit/{scheduledPlanLogAudit} | Add new audit for a scheduledPlanLog
[**add_scheduled_plan_log_tag**](ScheduledPlanLogApi.md#add_scheduled_plan_log_tag) | **PUT** /beta/scheduledPlanLog/{scheduledPlanLogId}/tag/{scheduledPlanLogTag} | Add new tags for a scheduledPlanLog.
[**delete_scheduled_plan_log_tag**](ScheduledPlanLogApi.md#delete_scheduled_plan_log_tag) | **DELETE** /beta/scheduledPlanLog/{scheduledPlanLogId}/tag/{scheduledPlanLogTag} | Delete a tag for a scheduledPlanLog.
[**get_duplicate_scheduled_plan_log_by_id**](ScheduledPlanLogApi.md#get_duplicate_scheduled_plan_log_by_id) | **GET** /beta/scheduledPlanLog/duplicate/{scheduledPlanLogId} | Get a duplicated a scheduledPlanLog by id
[**get_scheduled_plan_log_by_filter**](ScheduledPlanLogApi.md#get_scheduled_plan_log_by_filter) | **GET** /beta/scheduledPlanLog/search | Search scheduledPlanLogs by filter
[**get_scheduled_plan_log_by_id**](ScheduledPlanLogApi.md#get_scheduled_plan_log_by_id) | **GET** /beta/scheduledPlanLog/{scheduledPlanLogId} | Get a scheduledPlanLog by id
[**get_scheduled_plan_log_tags**](ScheduledPlanLogApi.md#get_scheduled_plan_log_tags) | **GET** /beta/scheduledPlanLog/{scheduledPlanLogId}/tag | Get the tags for a scheduledPlanLog.


# **add_scheduled_plan_log_audit**
> add_scheduled_plan_log_audit(scheduled_plan_log_id, scheduled_plan_log_audit)

Add new audit for a scheduledPlanLog

Adds an audit to an existing scheduledPlanLog.

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
api_instance = Infoplus.ScheduledPlanLogApi(Infoplus.ApiClient(configuration))
scheduled_plan_log_id = 56 # int | Id of the scheduledPlanLog to add an audit to
scheduled_plan_log_audit = 'scheduled_plan_log_audit_example' # str | The audit to add

try:
    # Add new audit for a scheduledPlanLog
    api_instance.add_scheduled_plan_log_audit(scheduled_plan_log_id, scheduled_plan_log_audit)
except ApiException as e:
    print("Exception when calling ScheduledPlanLogApi->add_scheduled_plan_log_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_log_id** | **int**| Id of the scheduledPlanLog to add an audit to | 
 **scheduled_plan_log_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_scheduled_plan_log_tag**
> add_scheduled_plan_log_tag(scheduled_plan_log_id, scheduled_plan_log_tag)

Add new tags for a scheduledPlanLog.

Adds a tag to an existing scheduledPlanLog.

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
api_instance = Infoplus.ScheduledPlanLogApi(Infoplus.ApiClient(configuration))
scheduled_plan_log_id = 56 # int | Id of the scheduledPlanLog to add a tag to
scheduled_plan_log_tag = 'scheduled_plan_log_tag_example' # str | The tag to add

try:
    # Add new tags for a scheduledPlanLog.
    api_instance.add_scheduled_plan_log_tag(scheduled_plan_log_id, scheduled_plan_log_tag)
except ApiException as e:
    print("Exception when calling ScheduledPlanLogApi->add_scheduled_plan_log_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_log_id** | **int**| Id of the scheduledPlanLog to add a tag to | 
 **scheduled_plan_log_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_plan_log_tag**
> delete_scheduled_plan_log_tag(scheduled_plan_log_id, scheduled_plan_log_tag)

Delete a tag for a scheduledPlanLog.

Deletes an existing scheduledPlanLog tag using the specified data.

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
api_instance = Infoplus.ScheduledPlanLogApi(Infoplus.ApiClient(configuration))
scheduled_plan_log_id = 56 # int | Id of the scheduledPlanLog to remove tag from
scheduled_plan_log_tag = 'scheduled_plan_log_tag_example' # str | The tag to delete

try:
    # Delete a tag for a scheduledPlanLog.
    api_instance.delete_scheduled_plan_log_tag(scheduled_plan_log_id, scheduled_plan_log_tag)
except ApiException as e:
    print("Exception when calling ScheduledPlanLogApi->delete_scheduled_plan_log_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_log_id** | **int**| Id of the scheduledPlanLog to remove tag from | 
 **scheduled_plan_log_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_scheduled_plan_log_by_id**
> ScheduledPlanLog get_duplicate_scheduled_plan_log_by_id(scheduled_plan_log_id)

Get a duplicated a scheduledPlanLog by id

Returns a duplicated scheduledPlanLog identified by the specified id.

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
api_instance = Infoplus.ScheduledPlanLogApi(Infoplus.ApiClient(configuration))
scheduled_plan_log_id = 56 # int | Id of the scheduledPlanLog to be duplicated.

try:
    # Get a duplicated a scheduledPlanLog by id
    api_response = api_instance.get_duplicate_scheduled_plan_log_by_id(scheduled_plan_log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanLogApi->get_duplicate_scheduled_plan_log_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_log_id** | **int**| Id of the scheduledPlanLog to be duplicated. | 

### Return type

[**ScheduledPlanLog**](ScheduledPlanLog.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_plan_log_by_filter**
> list[ScheduledPlanLog] get_scheduled_plan_log_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search scheduledPlanLogs by filter

Returns the list of scheduledPlanLogs that match the given filter.

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
api_instance = Infoplus.ScheduledPlanLogApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search scheduledPlanLogs by filter
    api_response = api_instance.get_scheduled_plan_log_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanLogApi->get_scheduled_plan_log_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ScheduledPlanLog]**](ScheduledPlanLog.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_plan_log_by_id**
> ScheduledPlanLog get_scheduled_plan_log_by_id(scheduled_plan_log_id)

Get a scheduledPlanLog by id

Returns the scheduledPlanLog identified by the specified id.

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
api_instance = Infoplus.ScheduledPlanLogApi(Infoplus.ApiClient(configuration))
scheduled_plan_log_id = 56 # int | Id of the scheduledPlanLog to be returned.

try:
    # Get a scheduledPlanLog by id
    api_response = api_instance.get_scheduled_plan_log_by_id(scheduled_plan_log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledPlanLogApi->get_scheduled_plan_log_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_log_id** | **int**| Id of the scheduledPlanLog to be returned. | 

### Return type

[**ScheduledPlanLog**](ScheduledPlanLog.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_plan_log_tags**
> get_scheduled_plan_log_tags(scheduled_plan_log_id)

Get the tags for a scheduledPlanLog.

Get all existing scheduledPlanLog tags.

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
api_instance = Infoplus.ScheduledPlanLogApi(Infoplus.ApiClient(configuration))
scheduled_plan_log_id = 56 # int | Id of the scheduledPlanLog to get tags for

try:
    # Get the tags for a scheduledPlanLog.
    api_instance.get_scheduled_plan_log_tags(scheduled_plan_log_id)
except ApiException as e:
    print("Exception when calling ScheduledPlanLogApi->get_scheduled_plan_log_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_log_id** | **int**| Id of the scheduledPlanLog to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

