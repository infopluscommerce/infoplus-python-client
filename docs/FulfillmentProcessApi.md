# Infoplus.FulfillmentProcessApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fulfillment_process_audit**](FulfillmentProcessApi.md#add_fulfillment_process_audit) | **PUT** /beta/fulfillmentProcess/{fulfillmentProcessId}/audit/{fulfillmentProcessAudit} | Add new audit for a fulfillmentProcess
[**add_fulfillment_process_file**](FulfillmentProcessApi.md#add_fulfillment_process_file) | **POST** /beta/fulfillmentProcess/{fulfillmentProcessId}/file/{fileName} | Attach a file to a fulfillmentProcess
[**add_fulfillment_process_file_by_url**](FulfillmentProcessApi.md#add_fulfillment_process_file_by_url) | **POST** /beta/fulfillmentProcess/{fulfillmentProcessId}/file | Attach a file to a fulfillmentProcess by URL.
[**add_fulfillment_process_tag**](FulfillmentProcessApi.md#add_fulfillment_process_tag) | **PUT** /beta/fulfillmentProcess/{fulfillmentProcessId}/tag/{fulfillmentProcessTag} | Add new tags for a fulfillmentProcess.
[**delete_fulfillment_process_file**](FulfillmentProcessApi.md#delete_fulfillment_process_file) | **DELETE** /beta/fulfillmentProcess/{fulfillmentProcessId}/file/{fileId} | Delete a file for a fulfillmentProcess.
[**delete_fulfillment_process_tag**](FulfillmentProcessApi.md#delete_fulfillment_process_tag) | **DELETE** /beta/fulfillmentProcess/{fulfillmentProcessId}/tag/{fulfillmentProcessTag} | Delete a tag for a fulfillmentProcess.
[**get_duplicate_fulfillment_process_by_id**](FulfillmentProcessApi.md#get_duplicate_fulfillment_process_by_id) | **GET** /beta/fulfillmentProcess/duplicate/{fulfillmentProcessId} | Get a duplicated a fulfillmentProcess by id
[**get_fulfillment_process_by_filter**](FulfillmentProcessApi.md#get_fulfillment_process_by_filter) | **GET** /beta/fulfillmentProcess/search | Search fulfillmentProcesses by filter
[**get_fulfillment_process_by_id**](FulfillmentProcessApi.md#get_fulfillment_process_by_id) | **GET** /beta/fulfillmentProcess/{fulfillmentProcessId} | Get a fulfillmentProcess by id
[**get_fulfillment_process_files**](FulfillmentProcessApi.md#get_fulfillment_process_files) | **GET** /beta/fulfillmentProcess/{fulfillmentProcessId}/file | Get the files for a fulfillmentProcess.
[**get_fulfillment_process_tags**](FulfillmentProcessApi.md#get_fulfillment_process_tags) | **GET** /beta/fulfillmentProcess/{fulfillmentProcessId}/tag | Get the tags for a fulfillmentProcess.
[**update_fulfillment_process_custom_fields**](FulfillmentProcessApi.md#update_fulfillment_process_custom_fields) | **PUT** /beta/fulfillmentProcess/customFields | Update a fulfillmentProcess custom fields


# **add_fulfillment_process_audit**
> add_fulfillment_process_audit(fulfillment_process_id, fulfillment_process_audit)

Add new audit for a fulfillmentProcess

Adds an audit to an existing fulfillmentProcess.

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
api_instance = Infoplus.FulfillmentProcessApi(Infoplus.ApiClient(configuration))
fulfillment_process_id = 56 # int | Id of the fulfillmentProcess to add an audit to
fulfillment_process_audit = 'fulfillment_process_audit_example' # str | The audit to add

try:
    # Add new audit for a fulfillmentProcess
    api_instance.add_fulfillment_process_audit(fulfillment_process_id, fulfillment_process_audit)
except ApiException as e:
    print("Exception when calling FulfillmentProcessApi->add_fulfillment_process_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_id** | **int**| Id of the fulfillmentProcess to add an audit to | 
 **fulfillment_process_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_fulfillment_process_file**
> add_fulfillment_process_file(fulfillment_process_id, file_name)

Attach a file to a fulfillmentProcess

Adds a file to an existing fulfillmentProcess.

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
api_instance = Infoplus.FulfillmentProcessApi(Infoplus.ApiClient(configuration))
fulfillment_process_id = 56 # int | Id of the fulfillmentProcess to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a fulfillmentProcess
    api_instance.add_fulfillment_process_file(fulfillment_process_id, file_name)
except ApiException as e:
    print("Exception when calling FulfillmentProcessApi->add_fulfillment_process_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_id** | **int**| Id of the fulfillmentProcess to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_fulfillment_process_file_by_url**
> add_fulfillment_process_file_by_url(body, fulfillment_process_id)

Attach a file to a fulfillmentProcess by URL.

Adds a file to an existing fulfillmentProcess by URL.

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
api_instance = Infoplus.FulfillmentProcessApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
fulfillment_process_id = 56 # int | Id of the fulfillmentProcess to add an file to

try:
    # Attach a file to a fulfillmentProcess by URL.
    api_instance.add_fulfillment_process_file_by_url(body, fulfillment_process_id)
except ApiException as e:
    print("Exception when calling FulfillmentProcessApi->add_fulfillment_process_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **fulfillment_process_id** | **int**| Id of the fulfillmentProcess to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_fulfillment_process_tag**
> add_fulfillment_process_tag(fulfillment_process_id, fulfillment_process_tag)

Add new tags for a fulfillmentProcess.

Adds a tag to an existing fulfillmentProcess.

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
api_instance = Infoplus.FulfillmentProcessApi(Infoplus.ApiClient(configuration))
fulfillment_process_id = 56 # int | Id of the fulfillmentProcess to add a tag to
fulfillment_process_tag = 'fulfillment_process_tag_example' # str | The tag to add

try:
    # Add new tags for a fulfillmentProcess.
    api_instance.add_fulfillment_process_tag(fulfillment_process_id, fulfillment_process_tag)
except ApiException as e:
    print("Exception when calling FulfillmentProcessApi->add_fulfillment_process_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_id** | **int**| Id of the fulfillmentProcess to add a tag to | 
 **fulfillment_process_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fulfillment_process_file**
> delete_fulfillment_process_file(fulfillment_process_id, file_id)

Delete a file for a fulfillmentProcess.

Deletes an existing fulfillmentProcess file using the specified data.

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
api_instance = Infoplus.FulfillmentProcessApi(Infoplus.ApiClient(configuration))
fulfillment_process_id = 56 # int | Id of the fulfillmentProcess to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a fulfillmentProcess.
    api_instance.delete_fulfillment_process_file(fulfillment_process_id, file_id)
except ApiException as e:
    print("Exception when calling FulfillmentProcessApi->delete_fulfillment_process_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_id** | **int**| Id of the fulfillmentProcess to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fulfillment_process_tag**
> delete_fulfillment_process_tag(fulfillment_process_id, fulfillment_process_tag)

Delete a tag for a fulfillmentProcess.

Deletes an existing fulfillmentProcess tag using the specified data.

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
api_instance = Infoplus.FulfillmentProcessApi(Infoplus.ApiClient(configuration))
fulfillment_process_id = 56 # int | Id of the fulfillmentProcess to remove tag from
fulfillment_process_tag = 'fulfillment_process_tag_example' # str | The tag to delete

try:
    # Delete a tag for a fulfillmentProcess.
    api_instance.delete_fulfillment_process_tag(fulfillment_process_id, fulfillment_process_tag)
except ApiException as e:
    print("Exception when calling FulfillmentProcessApi->delete_fulfillment_process_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_id** | **int**| Id of the fulfillmentProcess to remove tag from | 
 **fulfillment_process_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_fulfillment_process_by_id**
> FulfillmentProcess get_duplicate_fulfillment_process_by_id(fulfillment_process_id)

Get a duplicated a fulfillmentProcess by id

Returns a duplicated fulfillmentProcess identified by the specified id.

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
api_instance = Infoplus.FulfillmentProcessApi(Infoplus.ApiClient(configuration))
fulfillment_process_id = 56 # int | Id of the fulfillmentProcess to be duplicated.

try:
    # Get a duplicated a fulfillmentProcess by id
    api_response = api_instance.get_duplicate_fulfillment_process_by_id(fulfillment_process_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentProcessApi->get_duplicate_fulfillment_process_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_id** | **int**| Id of the fulfillmentProcess to be duplicated. | 

### Return type

[**FulfillmentProcess**](FulfillmentProcess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_process_by_filter**
> list[FulfillmentProcess] get_fulfillment_process_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search fulfillmentProcesses by filter

Returns the list of fulfillmentProcesses that match the given filter.

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
api_instance = Infoplus.FulfillmentProcessApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search fulfillmentProcesses by filter
    api_response = api_instance.get_fulfillment_process_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentProcessApi->get_fulfillment_process_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[FulfillmentProcess]**](FulfillmentProcess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_process_by_id**
> FulfillmentProcess get_fulfillment_process_by_id(fulfillment_process_id)

Get a fulfillmentProcess by id

Returns the fulfillmentProcess identified by the specified id.

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
api_instance = Infoplus.FulfillmentProcessApi(Infoplus.ApiClient(configuration))
fulfillment_process_id = 56 # int | Id of the fulfillmentProcess to be returned.

try:
    # Get a fulfillmentProcess by id
    api_response = api_instance.get_fulfillment_process_by_id(fulfillment_process_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentProcessApi->get_fulfillment_process_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_id** | **int**| Id of the fulfillmentProcess to be returned. | 

### Return type

[**FulfillmentProcess**](FulfillmentProcess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_process_files**
> get_fulfillment_process_files(fulfillment_process_id)

Get the files for a fulfillmentProcess.

Get all existing fulfillmentProcess files.

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
api_instance = Infoplus.FulfillmentProcessApi(Infoplus.ApiClient(configuration))
fulfillment_process_id = 56 # int | Id of the fulfillmentProcess to get files for

try:
    # Get the files for a fulfillmentProcess.
    api_instance.get_fulfillment_process_files(fulfillment_process_id)
except ApiException as e:
    print("Exception when calling FulfillmentProcessApi->get_fulfillment_process_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_id** | **int**| Id of the fulfillmentProcess to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_process_tags**
> get_fulfillment_process_tags(fulfillment_process_id)

Get the tags for a fulfillmentProcess.

Get all existing fulfillmentProcess tags.

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
api_instance = Infoplus.FulfillmentProcessApi(Infoplus.ApiClient(configuration))
fulfillment_process_id = 56 # int | Id of the fulfillmentProcess to get tags for

try:
    # Get the tags for a fulfillmentProcess.
    api_instance.get_fulfillment_process_tags(fulfillment_process_id)
except ApiException as e:
    print("Exception when calling FulfillmentProcessApi->get_fulfillment_process_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_process_id** | **int**| Id of the fulfillmentProcess to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fulfillment_process_custom_fields**
> update_fulfillment_process_custom_fields(body)

Update a fulfillmentProcess custom fields

Updates an existing fulfillmentProcess custom fields using the specified data.

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
api_instance = Infoplus.FulfillmentProcessApi(Infoplus.ApiClient(configuration))
body = Infoplus.FulfillmentProcess() # FulfillmentProcess | FulfillmentProcess to be updated.

try:
    # Update a fulfillmentProcess custom fields
    api_instance.update_fulfillment_process_custom_fields(body)
except ApiException as e:
    print("Exception when calling FulfillmentProcessApi->update_fulfillment_process_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FulfillmentProcess**](FulfillmentProcess.md)| FulfillmentProcess to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

