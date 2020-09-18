# Infoplus.FulfillmentProcessLogApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fulfillment_process_log_audit**](FulfillmentProcessLogApi.md#add_fulfillment_process_log_audit) | **PUT** /beta/fulfillmentProcessLog/{fulfillmentProcessLogId}/audit/{fulfillmentProcessLogAudit} | Add new audit for a fulfillmentProcessLog
[**add_fulfillment_process_log_file**](FulfillmentProcessLogApi.md#add_fulfillment_process_log_file) | **POST** /beta/fulfillmentProcessLog/{fulfillmentProcessLogId}/file/{fileName} | Attach a file to a fulfillmentProcessLog
[**add_fulfillment_process_log_file_by_url**](FulfillmentProcessLogApi.md#add_fulfillment_process_log_file_by_url) | **POST** /beta/fulfillmentProcessLog/{fulfillmentProcessLogId}/file | Attach a file to a fulfillmentProcessLog by URL.
[**add_fulfillment_process_log_tag**](FulfillmentProcessLogApi.md#add_fulfillment_process_log_tag) | **PUT** /beta/fulfillmentProcessLog/{fulfillmentProcessLogId}/tag/{fulfillmentProcessLogTag} | Add new tags for a fulfillmentProcessLog.
[**delete_fulfillment_process_log_file**](FulfillmentProcessLogApi.md#delete_fulfillment_process_log_file) | **DELETE** /beta/fulfillmentProcessLog/{fulfillmentProcessLogId}/file/{fileId} | Delete a file for a fulfillmentProcessLog.
[**delete_fulfillment_process_log_tag**](FulfillmentProcessLogApi.md#delete_fulfillment_process_log_tag) | **DELETE** /beta/fulfillmentProcessLog/{fulfillmentProcessLogId}/tag/{fulfillmentProcessLogTag} | Delete a tag for a fulfillmentProcessLog.
[**get_duplicate_fulfillment_process_log_by_id**](FulfillmentProcessLogApi.md#get_duplicate_fulfillment_process_log_by_id) | **GET** /beta/fulfillmentProcessLog/duplicate/{fulfillmentProcessLogId} | Get a duplicated a fulfillmentProcessLog by id
[**get_fulfillment_process_log_by_filter**](FulfillmentProcessLogApi.md#get_fulfillment_process_log_by_filter) | **GET** /beta/fulfillmentProcessLog/search | Search fulfillmentProcessLogs by filter
[**get_fulfillment_process_log_by_id**](FulfillmentProcessLogApi.md#get_fulfillment_process_log_by_id) | **GET** /beta/fulfillmentProcessLog/{fulfillmentProcessLogId} | Get a fulfillmentProcessLog by id
[**get_fulfillment_process_log_files**](FulfillmentProcessLogApi.md#get_fulfillment_process_log_files) | **GET** /beta/fulfillmentProcessLog/{fulfillmentProcessLogId}/file | Get the files for a fulfillmentProcessLog.
[**get_fulfillment_process_log_tags**](FulfillmentProcessLogApi.md#get_fulfillment_process_log_tags) | **GET** /beta/fulfillmentProcessLog/{fulfillmentProcessLogId}/tag | Get the tags for a fulfillmentProcessLog.


# **add_fulfillment_process_log_audit**
> add_fulfillment_process_log_audit(fulfillment_process_log_id, fulfillment_process_log_audit)

Add new audit for a fulfillmentProcessLog

Adds an audit to an existing fulfillmentProcessLog.

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
api_instance = Infoplus.FulfillmentProcessLogApi(Infoplus.ApiClient(configuration))
fulfillment_process_log_id = 56 # int | Id of the fulfillmentProcessLog to add an audit to
fulfillment_process_log_audit = 'fulfillment_process_log_audit_example' # str | The audit to add

try:
    # Add new audit for a fulfillmentProcessLog
    api_instance.add_fulfillment_process_log_audit(fulfillment_process_log_id, fulfillment_process_log_audit)
except ApiException as e:
    print("Exception when calling FulfillmentProcessLogApi->add_fulfillment_process_log_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_log_id** | **int**| Id of the fulfillmentProcessLog to add an audit to | 
 **fulfillment_process_log_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_fulfillment_process_log_file**
> add_fulfillment_process_log_file(fulfillment_process_log_id, file_name)

Attach a file to a fulfillmentProcessLog

Adds a file to an existing fulfillmentProcessLog.

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
api_instance = Infoplus.FulfillmentProcessLogApi(Infoplus.ApiClient(configuration))
fulfillment_process_log_id = 56 # int | Id of the fulfillmentProcessLog to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a fulfillmentProcessLog
    api_instance.add_fulfillment_process_log_file(fulfillment_process_log_id, file_name)
except ApiException as e:
    print("Exception when calling FulfillmentProcessLogApi->add_fulfillment_process_log_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_log_id** | **int**| Id of the fulfillmentProcessLog to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_fulfillment_process_log_file_by_url**
> add_fulfillment_process_log_file_by_url(body, fulfillment_process_log_id)

Attach a file to a fulfillmentProcessLog by URL.

Adds a file to an existing fulfillmentProcessLog by URL.

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
api_instance = Infoplus.FulfillmentProcessLogApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
fulfillment_process_log_id = 56 # int | Id of the fulfillmentProcessLog to add an file to

try:
    # Attach a file to a fulfillmentProcessLog by URL.
    api_instance.add_fulfillment_process_log_file_by_url(body, fulfillment_process_log_id)
except ApiException as e:
    print("Exception when calling FulfillmentProcessLogApi->add_fulfillment_process_log_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **fulfillment_process_log_id** | **int**| Id of the fulfillmentProcessLog to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_fulfillment_process_log_tag**
> add_fulfillment_process_log_tag(fulfillment_process_log_id, fulfillment_process_log_tag)

Add new tags for a fulfillmentProcessLog.

Adds a tag to an existing fulfillmentProcessLog.

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
api_instance = Infoplus.FulfillmentProcessLogApi(Infoplus.ApiClient(configuration))
fulfillment_process_log_id = 56 # int | Id of the fulfillmentProcessLog to add a tag to
fulfillment_process_log_tag = 'fulfillment_process_log_tag_example' # str | The tag to add

try:
    # Add new tags for a fulfillmentProcessLog.
    api_instance.add_fulfillment_process_log_tag(fulfillment_process_log_id, fulfillment_process_log_tag)
except ApiException as e:
    print("Exception when calling FulfillmentProcessLogApi->add_fulfillment_process_log_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_log_id** | **int**| Id of the fulfillmentProcessLog to add a tag to | 
 **fulfillment_process_log_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fulfillment_process_log_file**
> delete_fulfillment_process_log_file(fulfillment_process_log_id, file_id)

Delete a file for a fulfillmentProcessLog.

Deletes an existing fulfillmentProcessLog file using the specified data.

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
api_instance = Infoplus.FulfillmentProcessLogApi(Infoplus.ApiClient(configuration))
fulfillment_process_log_id = 56 # int | Id of the fulfillmentProcessLog to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a fulfillmentProcessLog.
    api_instance.delete_fulfillment_process_log_file(fulfillment_process_log_id, file_id)
except ApiException as e:
    print("Exception when calling FulfillmentProcessLogApi->delete_fulfillment_process_log_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_log_id** | **int**| Id of the fulfillmentProcessLog to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fulfillment_process_log_tag**
> delete_fulfillment_process_log_tag(fulfillment_process_log_id, fulfillment_process_log_tag)

Delete a tag for a fulfillmentProcessLog.

Deletes an existing fulfillmentProcessLog tag using the specified data.

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
api_instance = Infoplus.FulfillmentProcessLogApi(Infoplus.ApiClient(configuration))
fulfillment_process_log_id = 56 # int | Id of the fulfillmentProcessLog to remove tag from
fulfillment_process_log_tag = 'fulfillment_process_log_tag_example' # str | The tag to delete

try:
    # Delete a tag for a fulfillmentProcessLog.
    api_instance.delete_fulfillment_process_log_tag(fulfillment_process_log_id, fulfillment_process_log_tag)
except ApiException as e:
    print("Exception when calling FulfillmentProcessLogApi->delete_fulfillment_process_log_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_log_id** | **int**| Id of the fulfillmentProcessLog to remove tag from | 
 **fulfillment_process_log_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_fulfillment_process_log_by_id**
> FulfillmentProcessLog get_duplicate_fulfillment_process_log_by_id(fulfillment_process_log_id)

Get a duplicated a fulfillmentProcessLog by id

Returns a duplicated fulfillmentProcessLog identified by the specified id.

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
api_instance = Infoplus.FulfillmentProcessLogApi(Infoplus.ApiClient(configuration))
fulfillment_process_log_id = 56 # int | Id of the fulfillmentProcessLog to be duplicated.

try:
    # Get a duplicated a fulfillmentProcessLog by id
    api_response = api_instance.get_duplicate_fulfillment_process_log_by_id(fulfillment_process_log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentProcessLogApi->get_duplicate_fulfillment_process_log_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_log_id** | **int**| Id of the fulfillmentProcessLog to be duplicated. | 

### Return type

[**FulfillmentProcessLog**](FulfillmentProcessLog.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_process_log_by_filter**
> list[FulfillmentProcessLog] get_fulfillment_process_log_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search fulfillmentProcessLogs by filter

Returns the list of fulfillmentProcessLogs that match the given filter.

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
api_instance = Infoplus.FulfillmentProcessLogApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search fulfillmentProcessLogs by filter
    api_response = api_instance.get_fulfillment_process_log_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentProcessLogApi->get_fulfillment_process_log_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[FulfillmentProcessLog]**](FulfillmentProcessLog.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_process_log_by_id**
> FulfillmentProcessLog get_fulfillment_process_log_by_id(fulfillment_process_log_id)

Get a fulfillmentProcessLog by id

Returns the fulfillmentProcessLog identified by the specified id.

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
api_instance = Infoplus.FulfillmentProcessLogApi(Infoplus.ApiClient(configuration))
fulfillment_process_log_id = 56 # int | Id of the fulfillmentProcessLog to be returned.

try:
    # Get a fulfillmentProcessLog by id
    api_response = api_instance.get_fulfillment_process_log_by_id(fulfillment_process_log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentProcessLogApi->get_fulfillment_process_log_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_log_id** | **int**| Id of the fulfillmentProcessLog to be returned. | 

### Return type

[**FulfillmentProcessLog**](FulfillmentProcessLog.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_process_log_files**
> get_fulfillment_process_log_files(fulfillment_process_log_id)

Get the files for a fulfillmentProcessLog.

Get all existing fulfillmentProcessLog files.

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
api_instance = Infoplus.FulfillmentProcessLogApi(Infoplus.ApiClient(configuration))
fulfillment_process_log_id = 56 # int | Id of the fulfillmentProcessLog to get files for

try:
    # Get the files for a fulfillmentProcessLog.
    api_instance.get_fulfillment_process_log_files(fulfillment_process_log_id)
except ApiException as e:
    print("Exception when calling FulfillmentProcessLogApi->get_fulfillment_process_log_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_log_id** | **int**| Id of the fulfillmentProcessLog to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_process_log_tags**
> get_fulfillment_process_log_tags(fulfillment_process_log_id)

Get the tags for a fulfillmentProcessLog.

Get all existing fulfillmentProcessLog tags.

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
api_instance = Infoplus.FulfillmentProcessLogApi(Infoplus.ApiClient(configuration))
fulfillment_process_log_id = 56 # int | Id of the fulfillmentProcessLog to get tags for

try:
    # Get the tags for a fulfillmentProcessLog.
    api_instance.get_fulfillment_process_log_tags(fulfillment_process_log_id)
except ApiException as e:
    print("Exception when calling FulfillmentProcessLogApi->get_fulfillment_process_log_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_log_id** | **int**| Id of the fulfillmentProcessLog to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

