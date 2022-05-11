# Infoplus.PerpetualInventoryLogApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_perpetual_inventory_log_audit**](PerpetualInventoryLogApi.md#add_perpetual_inventory_log_audit) | **PUT** /v3.0/perpetualInventoryLog/{perpetualInventoryLogId}/audit/{perpetualInventoryLogAudit} | Add new audit for a perpetualInventoryLog
[**add_perpetual_inventory_log_file**](PerpetualInventoryLogApi.md#add_perpetual_inventory_log_file) | **POST** /v3.0/perpetualInventoryLog/{perpetualInventoryLogId}/file/{fileName} | Attach a file to a perpetualInventoryLog
[**add_perpetual_inventory_log_file_by_url**](PerpetualInventoryLogApi.md#add_perpetual_inventory_log_file_by_url) | **POST** /v3.0/perpetualInventoryLog/{perpetualInventoryLogId}/file | Attach a file to a perpetualInventoryLog by URL.
[**add_perpetual_inventory_log_tag**](PerpetualInventoryLogApi.md#add_perpetual_inventory_log_tag) | **PUT** /v3.0/perpetualInventoryLog/{perpetualInventoryLogId}/tag/{perpetualInventoryLogTag} | Add new tags for a perpetualInventoryLog.
[**delete_perpetual_inventory_log_file**](PerpetualInventoryLogApi.md#delete_perpetual_inventory_log_file) | **DELETE** /v3.0/perpetualInventoryLog/{perpetualInventoryLogId}/file/{fileId} | Delete a file for a perpetualInventoryLog.
[**delete_perpetual_inventory_log_tag**](PerpetualInventoryLogApi.md#delete_perpetual_inventory_log_tag) | **DELETE** /v3.0/perpetualInventoryLog/{perpetualInventoryLogId}/tag/{perpetualInventoryLogTag} | Delete a tag for a perpetualInventoryLog.
[**get_duplicate_perpetual_inventory_log_by_id**](PerpetualInventoryLogApi.md#get_duplicate_perpetual_inventory_log_by_id) | **GET** /v3.0/perpetualInventoryLog/duplicate/{perpetualInventoryLogId} | Get a duplicated a perpetualInventoryLog by id
[**get_perpetual_inventory_log_by_filter**](PerpetualInventoryLogApi.md#get_perpetual_inventory_log_by_filter) | **GET** /v3.0/perpetualInventoryLog/search | Search perpetualInventoryLogs by filter
[**get_perpetual_inventory_log_by_id**](PerpetualInventoryLogApi.md#get_perpetual_inventory_log_by_id) | **GET** /v3.0/perpetualInventoryLog/{perpetualInventoryLogId} | Get a perpetualInventoryLog by id
[**get_perpetual_inventory_log_files**](PerpetualInventoryLogApi.md#get_perpetual_inventory_log_files) | **GET** /v3.0/perpetualInventoryLog/{perpetualInventoryLogId}/file | Get the files for a perpetualInventoryLog.
[**get_perpetual_inventory_log_tags**](PerpetualInventoryLogApi.md#get_perpetual_inventory_log_tags) | **GET** /v3.0/perpetualInventoryLog/{perpetualInventoryLogId}/tag | Get the tags for a perpetualInventoryLog.


# **add_perpetual_inventory_log_audit**
> add_perpetual_inventory_log_audit(perpetual_inventory_log_id, perpetual_inventory_log_audit)

Add new audit for a perpetualInventoryLog

Adds an audit to an existing perpetualInventoryLog.

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
api_instance = Infoplus.PerpetualInventoryLogApi(Infoplus.ApiClient(configuration))
perpetual_inventory_log_id = 56 # int | Id of the perpetualInventoryLog to add an audit to
perpetual_inventory_log_audit = 'perpetual_inventory_log_audit_example' # str | The audit to add

try:
    # Add new audit for a perpetualInventoryLog
    api_instance.add_perpetual_inventory_log_audit(perpetual_inventory_log_id, perpetual_inventory_log_audit)
except ApiException as e:
    print("Exception when calling PerpetualInventoryLogApi->add_perpetual_inventory_log_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perpetual_inventory_log_id** | **int**| Id of the perpetualInventoryLog to add an audit to | 
 **perpetual_inventory_log_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_perpetual_inventory_log_file**
> add_perpetual_inventory_log_file(perpetual_inventory_log_id, file_name)

Attach a file to a perpetualInventoryLog

Adds a file to an existing perpetualInventoryLog.

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
api_instance = Infoplus.PerpetualInventoryLogApi(Infoplus.ApiClient(configuration))
perpetual_inventory_log_id = 56 # int | Id of the perpetualInventoryLog to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a perpetualInventoryLog
    api_instance.add_perpetual_inventory_log_file(perpetual_inventory_log_id, file_name)
except ApiException as e:
    print("Exception when calling PerpetualInventoryLogApi->add_perpetual_inventory_log_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perpetual_inventory_log_id** | **int**| Id of the perpetualInventoryLog to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_perpetual_inventory_log_file_by_url**
> add_perpetual_inventory_log_file_by_url(body, perpetual_inventory_log_id)

Attach a file to a perpetualInventoryLog by URL.

Adds a file to an existing perpetualInventoryLog by URL.

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
api_instance = Infoplus.PerpetualInventoryLogApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
perpetual_inventory_log_id = 56 # int | Id of the perpetualInventoryLog to add an file to

try:
    # Attach a file to a perpetualInventoryLog by URL.
    api_instance.add_perpetual_inventory_log_file_by_url(body, perpetual_inventory_log_id)
except ApiException as e:
    print("Exception when calling PerpetualInventoryLogApi->add_perpetual_inventory_log_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **perpetual_inventory_log_id** | **int**| Id of the perpetualInventoryLog to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_perpetual_inventory_log_tag**
> add_perpetual_inventory_log_tag(perpetual_inventory_log_id, perpetual_inventory_log_tag)

Add new tags for a perpetualInventoryLog.

Adds a tag to an existing perpetualInventoryLog.

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
api_instance = Infoplus.PerpetualInventoryLogApi(Infoplus.ApiClient(configuration))
perpetual_inventory_log_id = 56 # int | Id of the perpetualInventoryLog to add a tag to
perpetual_inventory_log_tag = 'perpetual_inventory_log_tag_example' # str | The tag to add

try:
    # Add new tags for a perpetualInventoryLog.
    api_instance.add_perpetual_inventory_log_tag(perpetual_inventory_log_id, perpetual_inventory_log_tag)
except ApiException as e:
    print("Exception when calling PerpetualInventoryLogApi->add_perpetual_inventory_log_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perpetual_inventory_log_id** | **int**| Id of the perpetualInventoryLog to add a tag to | 
 **perpetual_inventory_log_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_perpetual_inventory_log_file**
> delete_perpetual_inventory_log_file(perpetual_inventory_log_id, file_id)

Delete a file for a perpetualInventoryLog.

Deletes an existing perpetualInventoryLog file using the specified data.

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
api_instance = Infoplus.PerpetualInventoryLogApi(Infoplus.ApiClient(configuration))
perpetual_inventory_log_id = 56 # int | Id of the perpetualInventoryLog to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a perpetualInventoryLog.
    api_instance.delete_perpetual_inventory_log_file(perpetual_inventory_log_id, file_id)
except ApiException as e:
    print("Exception when calling PerpetualInventoryLogApi->delete_perpetual_inventory_log_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perpetual_inventory_log_id** | **int**| Id of the perpetualInventoryLog to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_perpetual_inventory_log_tag**
> delete_perpetual_inventory_log_tag(perpetual_inventory_log_id, perpetual_inventory_log_tag)

Delete a tag for a perpetualInventoryLog.

Deletes an existing perpetualInventoryLog tag using the specified data.

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
api_instance = Infoplus.PerpetualInventoryLogApi(Infoplus.ApiClient(configuration))
perpetual_inventory_log_id = 56 # int | Id of the perpetualInventoryLog to remove tag from
perpetual_inventory_log_tag = 'perpetual_inventory_log_tag_example' # str | The tag to delete

try:
    # Delete a tag for a perpetualInventoryLog.
    api_instance.delete_perpetual_inventory_log_tag(perpetual_inventory_log_id, perpetual_inventory_log_tag)
except ApiException as e:
    print("Exception when calling PerpetualInventoryLogApi->delete_perpetual_inventory_log_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perpetual_inventory_log_id** | **int**| Id of the perpetualInventoryLog to remove tag from | 
 **perpetual_inventory_log_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_perpetual_inventory_log_by_id**
> PerpetualInventoryLog get_duplicate_perpetual_inventory_log_by_id(perpetual_inventory_log_id)

Get a duplicated a perpetualInventoryLog by id

Returns a duplicated perpetualInventoryLog identified by the specified id.

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
api_instance = Infoplus.PerpetualInventoryLogApi(Infoplus.ApiClient(configuration))
perpetual_inventory_log_id = 56 # int | Id of the perpetualInventoryLog to be duplicated.

try:
    # Get a duplicated a perpetualInventoryLog by id
    api_response = api_instance.get_duplicate_perpetual_inventory_log_by_id(perpetual_inventory_log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerpetualInventoryLogApi->get_duplicate_perpetual_inventory_log_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perpetual_inventory_log_id** | **int**| Id of the perpetualInventoryLog to be duplicated. | 

### Return type

[**PerpetualInventoryLog**](PerpetualInventoryLog.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_perpetual_inventory_log_by_filter**
> list[PerpetualInventoryLog] get_perpetual_inventory_log_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search perpetualInventoryLogs by filter

Returns the list of perpetualInventoryLogs that match the given filter.

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
api_instance = Infoplus.PerpetualInventoryLogApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search perpetualInventoryLogs by filter
    api_response = api_instance.get_perpetual_inventory_log_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerpetualInventoryLogApi->get_perpetual_inventory_log_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[PerpetualInventoryLog]**](PerpetualInventoryLog.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_perpetual_inventory_log_by_id**
> PerpetualInventoryLog get_perpetual_inventory_log_by_id(perpetual_inventory_log_id)

Get a perpetualInventoryLog by id

Returns the perpetualInventoryLog identified by the specified id.

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
api_instance = Infoplus.PerpetualInventoryLogApi(Infoplus.ApiClient(configuration))
perpetual_inventory_log_id = 56 # int | Id of the perpetualInventoryLog to be returned.

try:
    # Get a perpetualInventoryLog by id
    api_response = api_instance.get_perpetual_inventory_log_by_id(perpetual_inventory_log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerpetualInventoryLogApi->get_perpetual_inventory_log_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perpetual_inventory_log_id** | **int**| Id of the perpetualInventoryLog to be returned. | 

### Return type

[**PerpetualInventoryLog**](PerpetualInventoryLog.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_perpetual_inventory_log_files**
> get_perpetual_inventory_log_files(perpetual_inventory_log_id)

Get the files for a perpetualInventoryLog.

Get all existing perpetualInventoryLog files.

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
api_instance = Infoplus.PerpetualInventoryLogApi(Infoplus.ApiClient(configuration))
perpetual_inventory_log_id = 56 # int | Id of the perpetualInventoryLog to get files for

try:
    # Get the files for a perpetualInventoryLog.
    api_instance.get_perpetual_inventory_log_files(perpetual_inventory_log_id)
except ApiException as e:
    print("Exception when calling PerpetualInventoryLogApi->get_perpetual_inventory_log_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perpetual_inventory_log_id** | **int**| Id of the perpetualInventoryLog to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_perpetual_inventory_log_tags**
> get_perpetual_inventory_log_tags(perpetual_inventory_log_id)

Get the tags for a perpetualInventoryLog.

Get all existing perpetualInventoryLog tags.

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
api_instance = Infoplus.PerpetualInventoryLogApi(Infoplus.ApiClient(configuration))
perpetual_inventory_log_id = 56 # int | Id of the perpetualInventoryLog to get tags for

try:
    # Get the tags for a perpetualInventoryLog.
    api_instance.get_perpetual_inventory_log_tags(perpetual_inventory_log_id)
except ApiException as e:
    print("Exception when calling PerpetualInventoryLogApi->get_perpetual_inventory_log_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perpetual_inventory_log_id** | **int**| Id of the perpetualInventoryLog to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

