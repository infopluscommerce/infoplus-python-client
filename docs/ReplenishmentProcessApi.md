# Infoplus.ReplenishmentProcessApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_replenishment_process_audit**](ReplenishmentProcessApi.md#add_replenishment_process_audit) | **PUT** /v3.0/replenishmentProcess/{replenishmentProcessId}/audit/{replenishmentProcessAudit} | Add new audit for a replenishmentProcess
[**add_replenishment_process_file**](ReplenishmentProcessApi.md#add_replenishment_process_file) | **POST** /v3.0/replenishmentProcess/{replenishmentProcessId}/file/{fileName} | Attach a file to a replenishmentProcess
[**add_replenishment_process_file_by_url**](ReplenishmentProcessApi.md#add_replenishment_process_file_by_url) | **POST** /v3.0/replenishmentProcess/{replenishmentProcessId}/file | Attach a file to a replenishmentProcess by URL.
[**add_replenishment_process_tag**](ReplenishmentProcessApi.md#add_replenishment_process_tag) | **PUT** /v3.0/replenishmentProcess/{replenishmentProcessId}/tag/{replenishmentProcessTag} | Add new tags for a replenishmentProcess.
[**delete_replenishment_process_file**](ReplenishmentProcessApi.md#delete_replenishment_process_file) | **DELETE** /v3.0/replenishmentProcess/{replenishmentProcessId}/file/{fileId} | Delete a file for a replenishmentProcess.
[**delete_replenishment_process_tag**](ReplenishmentProcessApi.md#delete_replenishment_process_tag) | **DELETE** /v3.0/replenishmentProcess/{replenishmentProcessId}/tag/{replenishmentProcessTag} | Delete a tag for a replenishmentProcess.
[**get_duplicate_replenishment_process_by_id**](ReplenishmentProcessApi.md#get_duplicate_replenishment_process_by_id) | **GET** /v3.0/replenishmentProcess/duplicate/{replenishmentProcessId} | Get a duplicated a replenishmentProcess by id
[**get_replenishment_process_by_filter**](ReplenishmentProcessApi.md#get_replenishment_process_by_filter) | **GET** /v3.0/replenishmentProcess/search | Search replenishmentProcesses by filter
[**get_replenishment_process_by_id**](ReplenishmentProcessApi.md#get_replenishment_process_by_id) | **GET** /v3.0/replenishmentProcess/{replenishmentProcessId} | Get a replenishmentProcess by id
[**get_replenishment_process_files**](ReplenishmentProcessApi.md#get_replenishment_process_files) | **GET** /v3.0/replenishmentProcess/{replenishmentProcessId}/file | Get the files for a replenishmentProcess.
[**get_replenishment_process_tags**](ReplenishmentProcessApi.md#get_replenishment_process_tags) | **GET** /v3.0/replenishmentProcess/{replenishmentProcessId}/tag | Get the tags for a replenishmentProcess.
[**update_replenishment_process_custom_fields**](ReplenishmentProcessApi.md#update_replenishment_process_custom_fields) | **PUT** /v3.0/replenishmentProcess/customFields | Update a replenishmentProcess custom fields


# **add_replenishment_process_audit**
> add_replenishment_process_audit(replenishment_process_id, replenishment_process_audit)

Add new audit for a replenishmentProcess

Adds an audit to an existing replenishmentProcess.

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
api_instance = Infoplus.ReplenishmentProcessApi(Infoplus.ApiClient(configuration))
replenishment_process_id = 56 # int | Id of the replenishmentProcess to add an audit to
replenishment_process_audit = 'replenishment_process_audit_example' # str | The audit to add

try:
    # Add new audit for a replenishmentProcess
    api_instance.add_replenishment_process_audit(replenishment_process_id, replenishment_process_audit)
except ApiException as e:
    print("Exception when calling ReplenishmentProcessApi->add_replenishment_process_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_process_id** | **int**| Id of the replenishmentProcess to add an audit to | 
 **replenishment_process_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_replenishment_process_file**
> add_replenishment_process_file(replenishment_process_id, file_name)

Attach a file to a replenishmentProcess

Adds a file to an existing replenishmentProcess.

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
api_instance = Infoplus.ReplenishmentProcessApi(Infoplus.ApiClient(configuration))
replenishment_process_id = 56 # int | Id of the replenishmentProcess to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a replenishmentProcess
    api_instance.add_replenishment_process_file(replenishment_process_id, file_name)
except ApiException as e:
    print("Exception when calling ReplenishmentProcessApi->add_replenishment_process_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_process_id** | **int**| Id of the replenishmentProcess to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_replenishment_process_file_by_url**
> add_replenishment_process_file_by_url(body, replenishment_process_id)

Attach a file to a replenishmentProcess by URL.

Adds a file to an existing replenishmentProcess by URL.

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
api_instance = Infoplus.ReplenishmentProcessApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
replenishment_process_id = 56 # int | Id of the replenishmentProcess to add an file to

try:
    # Attach a file to a replenishmentProcess by URL.
    api_instance.add_replenishment_process_file_by_url(body, replenishment_process_id)
except ApiException as e:
    print("Exception when calling ReplenishmentProcessApi->add_replenishment_process_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **replenishment_process_id** | **int**| Id of the replenishmentProcess to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_replenishment_process_tag**
> add_replenishment_process_tag(replenishment_process_id, replenishment_process_tag)

Add new tags for a replenishmentProcess.

Adds a tag to an existing replenishmentProcess.

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
api_instance = Infoplus.ReplenishmentProcessApi(Infoplus.ApiClient(configuration))
replenishment_process_id = 56 # int | Id of the replenishmentProcess to add a tag to
replenishment_process_tag = 'replenishment_process_tag_example' # str | The tag to add

try:
    # Add new tags for a replenishmentProcess.
    api_instance.add_replenishment_process_tag(replenishment_process_id, replenishment_process_tag)
except ApiException as e:
    print("Exception when calling ReplenishmentProcessApi->add_replenishment_process_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_process_id** | **int**| Id of the replenishmentProcess to add a tag to | 
 **replenishment_process_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_replenishment_process_file**
> delete_replenishment_process_file(replenishment_process_id, file_id)

Delete a file for a replenishmentProcess.

Deletes an existing replenishmentProcess file using the specified data.

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
api_instance = Infoplus.ReplenishmentProcessApi(Infoplus.ApiClient(configuration))
replenishment_process_id = 56 # int | Id of the replenishmentProcess to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a replenishmentProcess.
    api_instance.delete_replenishment_process_file(replenishment_process_id, file_id)
except ApiException as e:
    print("Exception when calling ReplenishmentProcessApi->delete_replenishment_process_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_process_id** | **int**| Id of the replenishmentProcess to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_replenishment_process_tag**
> delete_replenishment_process_tag(replenishment_process_id, replenishment_process_tag)

Delete a tag for a replenishmentProcess.

Deletes an existing replenishmentProcess tag using the specified data.

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
api_instance = Infoplus.ReplenishmentProcessApi(Infoplus.ApiClient(configuration))
replenishment_process_id = 56 # int | Id of the replenishmentProcess to remove tag from
replenishment_process_tag = 'replenishment_process_tag_example' # str | The tag to delete

try:
    # Delete a tag for a replenishmentProcess.
    api_instance.delete_replenishment_process_tag(replenishment_process_id, replenishment_process_tag)
except ApiException as e:
    print("Exception when calling ReplenishmentProcessApi->delete_replenishment_process_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_process_id** | **int**| Id of the replenishmentProcess to remove tag from | 
 **replenishment_process_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_replenishment_process_by_id**
> ReplenishmentProcess get_duplicate_replenishment_process_by_id(replenishment_process_id)

Get a duplicated a replenishmentProcess by id

Returns a duplicated replenishmentProcess identified by the specified id.

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
api_instance = Infoplus.ReplenishmentProcessApi(Infoplus.ApiClient(configuration))
replenishment_process_id = 56 # int | Id of the replenishmentProcess to be duplicated.

try:
    # Get a duplicated a replenishmentProcess by id
    api_response = api_instance.get_duplicate_replenishment_process_by_id(replenishment_process_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplenishmentProcessApi->get_duplicate_replenishment_process_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_process_id** | **int**| Id of the replenishmentProcess to be duplicated. | 

### Return type

[**ReplenishmentProcess**](ReplenishmentProcess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replenishment_process_by_filter**
> list[ReplenishmentProcess] get_replenishment_process_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search replenishmentProcesses by filter

Returns the list of replenishmentProcesses that match the given filter.

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
api_instance = Infoplus.ReplenishmentProcessApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search replenishmentProcesses by filter
    api_response = api_instance.get_replenishment_process_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplenishmentProcessApi->get_replenishment_process_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ReplenishmentProcess]**](ReplenishmentProcess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replenishment_process_by_id**
> ReplenishmentProcess get_replenishment_process_by_id(replenishment_process_id)

Get a replenishmentProcess by id

Returns the replenishmentProcess identified by the specified id.

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
api_instance = Infoplus.ReplenishmentProcessApi(Infoplus.ApiClient(configuration))
replenishment_process_id = 56 # int | Id of the replenishmentProcess to be returned.

try:
    # Get a replenishmentProcess by id
    api_response = api_instance.get_replenishment_process_by_id(replenishment_process_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplenishmentProcessApi->get_replenishment_process_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_process_id** | **int**| Id of the replenishmentProcess to be returned. | 

### Return type

[**ReplenishmentProcess**](ReplenishmentProcess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replenishment_process_files**
> get_replenishment_process_files(replenishment_process_id)

Get the files for a replenishmentProcess.

Get all existing replenishmentProcess files.

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
api_instance = Infoplus.ReplenishmentProcessApi(Infoplus.ApiClient(configuration))
replenishment_process_id = 56 # int | Id of the replenishmentProcess to get files for

try:
    # Get the files for a replenishmentProcess.
    api_instance.get_replenishment_process_files(replenishment_process_id)
except ApiException as e:
    print("Exception when calling ReplenishmentProcessApi->get_replenishment_process_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_process_id** | **int**| Id of the replenishmentProcess to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replenishment_process_tags**
> get_replenishment_process_tags(replenishment_process_id)

Get the tags for a replenishmentProcess.

Get all existing replenishmentProcess tags.

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
api_instance = Infoplus.ReplenishmentProcessApi(Infoplus.ApiClient(configuration))
replenishment_process_id = 56 # int | Id of the replenishmentProcess to get tags for

try:
    # Get the tags for a replenishmentProcess.
    api_instance.get_replenishment_process_tags(replenishment_process_id)
except ApiException as e:
    print("Exception when calling ReplenishmentProcessApi->get_replenishment_process_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_process_id** | **int**| Id of the replenishmentProcess to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_replenishment_process_custom_fields**
> update_replenishment_process_custom_fields(body)

Update a replenishmentProcess custom fields

Updates an existing replenishmentProcess custom fields using the specified data.

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
api_instance = Infoplus.ReplenishmentProcessApi(Infoplus.ApiClient(configuration))
body = Infoplus.ReplenishmentProcess() # ReplenishmentProcess | ReplenishmentProcess to be updated.

try:
    # Update a replenishmentProcess custom fields
    api_instance.update_replenishment_process_custom_fields(body)
except ApiException as e:
    print("Exception when calling ReplenishmentProcessApi->update_replenishment_process_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplenishmentProcess**](ReplenishmentProcess.md)| ReplenishmentProcess to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

