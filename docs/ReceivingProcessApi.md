# Infoplus.ReceivingProcessApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_receiving_process_audit**](ReceivingProcessApi.md#add_receiving_process_audit) | **PUT** /v3.0/receivingProcess/{receivingProcessId}/audit/{receivingProcessAudit} | Add new audit for a receivingProcess
[**add_receiving_process_file**](ReceivingProcessApi.md#add_receiving_process_file) | **POST** /v3.0/receivingProcess/{receivingProcessId}/file/{fileName} | Attach a file to a receivingProcess
[**add_receiving_process_file_by_url**](ReceivingProcessApi.md#add_receiving_process_file_by_url) | **POST** /v3.0/receivingProcess/{receivingProcessId}/file | Attach a file to a receivingProcess by URL.
[**add_receiving_process_tag**](ReceivingProcessApi.md#add_receiving_process_tag) | **PUT** /v3.0/receivingProcess/{receivingProcessId}/tag/{receivingProcessTag} | Add new tags for a receivingProcess.
[**delete_receiving_process_file**](ReceivingProcessApi.md#delete_receiving_process_file) | **DELETE** /v3.0/receivingProcess/{receivingProcessId}/file/{fileId} | Delete a file for a receivingProcess.
[**delete_receiving_process_tag**](ReceivingProcessApi.md#delete_receiving_process_tag) | **DELETE** /v3.0/receivingProcess/{receivingProcessId}/tag/{receivingProcessTag} | Delete a tag for a receivingProcess.
[**get_duplicate_receiving_process_by_id**](ReceivingProcessApi.md#get_duplicate_receiving_process_by_id) | **GET** /v3.0/receivingProcess/duplicate/{receivingProcessId} | Get a duplicated a receivingProcess by id
[**get_receiving_process_by_filter**](ReceivingProcessApi.md#get_receiving_process_by_filter) | **GET** /v3.0/receivingProcess/search | Search receivingProcesses by filter
[**get_receiving_process_by_id**](ReceivingProcessApi.md#get_receiving_process_by_id) | **GET** /v3.0/receivingProcess/{receivingProcessId} | Get a receivingProcess by id
[**get_receiving_process_files**](ReceivingProcessApi.md#get_receiving_process_files) | **GET** /v3.0/receivingProcess/{receivingProcessId}/file | Get the files for a receivingProcess.
[**get_receiving_process_tags**](ReceivingProcessApi.md#get_receiving_process_tags) | **GET** /v3.0/receivingProcess/{receivingProcessId}/tag | Get the tags for a receivingProcess.
[**update_receiving_process_custom_fields**](ReceivingProcessApi.md#update_receiving_process_custom_fields) | **PUT** /v3.0/receivingProcess/customFields | Update a receivingProcess custom fields


# **add_receiving_process_audit**
> add_receiving_process_audit(receiving_process_id, receiving_process_audit)

Add new audit for a receivingProcess

Adds an audit to an existing receivingProcess.

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
api_instance = Infoplus.ReceivingProcessApi(Infoplus.ApiClient(configuration))
receiving_process_id = 56 # int | Id of the receivingProcess to add an audit to
receiving_process_audit = 'receiving_process_audit_example' # str | The audit to add

try:
    # Add new audit for a receivingProcess
    api_instance.add_receiving_process_audit(receiving_process_id, receiving_process_audit)
except ApiException as e:
    print("Exception when calling ReceivingProcessApi->add_receiving_process_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_process_id** | **int**| Id of the receivingProcess to add an audit to | 
 **receiving_process_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_receiving_process_file**
> add_receiving_process_file(receiving_process_id, file_name)

Attach a file to a receivingProcess

Adds a file to an existing receivingProcess.

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
api_instance = Infoplus.ReceivingProcessApi(Infoplus.ApiClient(configuration))
receiving_process_id = 56 # int | Id of the receivingProcess to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a receivingProcess
    api_instance.add_receiving_process_file(receiving_process_id, file_name)
except ApiException as e:
    print("Exception when calling ReceivingProcessApi->add_receiving_process_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_process_id** | **int**| Id of the receivingProcess to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_receiving_process_file_by_url**
> add_receiving_process_file_by_url(body, receiving_process_id)

Attach a file to a receivingProcess by URL.

Adds a file to an existing receivingProcess by URL.

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
api_instance = Infoplus.ReceivingProcessApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
receiving_process_id = 56 # int | Id of the receivingProcess to add an file to

try:
    # Attach a file to a receivingProcess by URL.
    api_instance.add_receiving_process_file_by_url(body, receiving_process_id)
except ApiException as e:
    print("Exception when calling ReceivingProcessApi->add_receiving_process_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **receiving_process_id** | **int**| Id of the receivingProcess to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_receiving_process_tag**
> add_receiving_process_tag(receiving_process_id, receiving_process_tag)

Add new tags for a receivingProcess.

Adds a tag to an existing receivingProcess.

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
api_instance = Infoplus.ReceivingProcessApi(Infoplus.ApiClient(configuration))
receiving_process_id = 56 # int | Id of the receivingProcess to add a tag to
receiving_process_tag = 'receiving_process_tag_example' # str | The tag to add

try:
    # Add new tags for a receivingProcess.
    api_instance.add_receiving_process_tag(receiving_process_id, receiving_process_tag)
except ApiException as e:
    print("Exception when calling ReceivingProcessApi->add_receiving_process_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_process_id** | **int**| Id of the receivingProcess to add a tag to | 
 **receiving_process_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_receiving_process_file**
> delete_receiving_process_file(receiving_process_id, file_id)

Delete a file for a receivingProcess.

Deletes an existing receivingProcess file using the specified data.

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
api_instance = Infoplus.ReceivingProcessApi(Infoplus.ApiClient(configuration))
receiving_process_id = 56 # int | Id of the receivingProcess to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a receivingProcess.
    api_instance.delete_receiving_process_file(receiving_process_id, file_id)
except ApiException as e:
    print("Exception when calling ReceivingProcessApi->delete_receiving_process_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_process_id** | **int**| Id of the receivingProcess to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_receiving_process_tag**
> delete_receiving_process_tag(receiving_process_id, receiving_process_tag)

Delete a tag for a receivingProcess.

Deletes an existing receivingProcess tag using the specified data.

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
api_instance = Infoplus.ReceivingProcessApi(Infoplus.ApiClient(configuration))
receiving_process_id = 56 # int | Id of the receivingProcess to remove tag from
receiving_process_tag = 'receiving_process_tag_example' # str | The tag to delete

try:
    # Delete a tag for a receivingProcess.
    api_instance.delete_receiving_process_tag(receiving_process_id, receiving_process_tag)
except ApiException as e:
    print("Exception when calling ReceivingProcessApi->delete_receiving_process_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_process_id** | **int**| Id of the receivingProcess to remove tag from | 
 **receiving_process_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_receiving_process_by_id**
> ReceivingProcess get_duplicate_receiving_process_by_id(receiving_process_id)

Get a duplicated a receivingProcess by id

Returns a duplicated receivingProcess identified by the specified id.

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
api_instance = Infoplus.ReceivingProcessApi(Infoplus.ApiClient(configuration))
receiving_process_id = 56 # int | Id of the receivingProcess to be duplicated.

try:
    # Get a duplicated a receivingProcess by id
    api_response = api_instance.get_duplicate_receiving_process_by_id(receiving_process_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceivingProcessApi->get_duplicate_receiving_process_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_process_id** | **int**| Id of the receivingProcess to be duplicated. | 

### Return type

[**ReceivingProcess**](ReceivingProcess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receiving_process_by_filter**
> list[ReceivingProcess] get_receiving_process_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search receivingProcesses by filter

Returns the list of receivingProcesses that match the given filter.

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
api_instance = Infoplus.ReceivingProcessApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search receivingProcesses by filter
    api_response = api_instance.get_receiving_process_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceivingProcessApi->get_receiving_process_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ReceivingProcess]**](ReceivingProcess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receiving_process_by_id**
> ReceivingProcess get_receiving_process_by_id(receiving_process_id)

Get a receivingProcess by id

Returns the receivingProcess identified by the specified id.

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
api_instance = Infoplus.ReceivingProcessApi(Infoplus.ApiClient(configuration))
receiving_process_id = 56 # int | Id of the receivingProcess to be returned.

try:
    # Get a receivingProcess by id
    api_response = api_instance.get_receiving_process_by_id(receiving_process_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceivingProcessApi->get_receiving_process_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_process_id** | **int**| Id of the receivingProcess to be returned. | 

### Return type

[**ReceivingProcess**](ReceivingProcess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receiving_process_files**
> get_receiving_process_files(receiving_process_id)

Get the files for a receivingProcess.

Get all existing receivingProcess files.

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
api_instance = Infoplus.ReceivingProcessApi(Infoplus.ApiClient(configuration))
receiving_process_id = 56 # int | Id of the receivingProcess to get files for

try:
    # Get the files for a receivingProcess.
    api_instance.get_receiving_process_files(receiving_process_id)
except ApiException as e:
    print("Exception when calling ReceivingProcessApi->get_receiving_process_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_process_id** | **int**| Id of the receivingProcess to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receiving_process_tags**
> get_receiving_process_tags(receiving_process_id)

Get the tags for a receivingProcess.

Get all existing receivingProcess tags.

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
api_instance = Infoplus.ReceivingProcessApi(Infoplus.ApiClient(configuration))
receiving_process_id = 56 # int | Id of the receivingProcess to get tags for

try:
    # Get the tags for a receivingProcess.
    api_instance.get_receiving_process_tags(receiving_process_id)
except ApiException as e:
    print("Exception when calling ReceivingProcessApi->get_receiving_process_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_process_id** | **int**| Id of the receivingProcess to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_receiving_process_custom_fields**
> update_receiving_process_custom_fields(body)

Update a receivingProcess custom fields

Updates an existing receivingProcess custom fields using the specified data.

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
api_instance = Infoplus.ReceivingProcessApi(Infoplus.ApiClient(configuration))
body = Infoplus.ReceivingProcess() # ReceivingProcess | ReceivingProcess to be updated.

try:
    # Update a receivingProcess custom fields
    api_instance.update_receiving_process_custom_fields(body)
except ApiException as e:
    print("Exception when calling ReceivingProcessApi->update_receiving_process_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReceivingProcess**](ReceivingProcess.md)| ReceivingProcess to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

