# Infoplus.FinanceSystemConnectionLogApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_finance_system_connection_log_audit**](FinanceSystemConnectionLogApi.md#add_finance_system_connection_log_audit) | **PUT** /v3.0/financeSystemConnectionLog/{financeSystemConnectionLogId}/audit/{financeSystemConnectionLogAudit} | Add new audit for a financeSystemConnectionLog
[**add_finance_system_connection_log_file**](FinanceSystemConnectionLogApi.md#add_finance_system_connection_log_file) | **POST** /v3.0/financeSystemConnectionLog/{financeSystemConnectionLogId}/file/{fileName} | Attach a file to a financeSystemConnectionLog
[**add_finance_system_connection_log_file_by_url**](FinanceSystemConnectionLogApi.md#add_finance_system_connection_log_file_by_url) | **POST** /v3.0/financeSystemConnectionLog/{financeSystemConnectionLogId}/file | Attach a file to a financeSystemConnectionLog by URL.
[**add_finance_system_connection_log_tag**](FinanceSystemConnectionLogApi.md#add_finance_system_connection_log_tag) | **PUT** /v3.0/financeSystemConnectionLog/{financeSystemConnectionLogId}/tag/{financeSystemConnectionLogTag} | Add new tags for a financeSystemConnectionLog.
[**delete_finance_system_connection_log_file**](FinanceSystemConnectionLogApi.md#delete_finance_system_connection_log_file) | **DELETE** /v3.0/financeSystemConnectionLog/{financeSystemConnectionLogId}/file/{fileId} | Delete a file for a financeSystemConnectionLog.
[**delete_finance_system_connection_log_tag**](FinanceSystemConnectionLogApi.md#delete_finance_system_connection_log_tag) | **DELETE** /v3.0/financeSystemConnectionLog/{financeSystemConnectionLogId}/tag/{financeSystemConnectionLogTag} | Delete a tag for a financeSystemConnectionLog.
[**get_duplicate_finance_system_connection_log_by_id**](FinanceSystemConnectionLogApi.md#get_duplicate_finance_system_connection_log_by_id) | **GET** /v3.0/financeSystemConnectionLog/duplicate/{financeSystemConnectionLogId} | Get a duplicated a financeSystemConnectionLog by id
[**get_finance_system_connection_log_by_filter**](FinanceSystemConnectionLogApi.md#get_finance_system_connection_log_by_filter) | **GET** /v3.0/financeSystemConnectionLog/search | Search financeSystemConnectionLogs by filter
[**get_finance_system_connection_log_by_id**](FinanceSystemConnectionLogApi.md#get_finance_system_connection_log_by_id) | **GET** /v3.0/financeSystemConnectionLog/{financeSystemConnectionLogId} | Get a financeSystemConnectionLog by id
[**get_finance_system_connection_log_files**](FinanceSystemConnectionLogApi.md#get_finance_system_connection_log_files) | **GET** /v3.0/financeSystemConnectionLog/{financeSystemConnectionLogId}/file | Get the files for a financeSystemConnectionLog.
[**get_finance_system_connection_log_tags**](FinanceSystemConnectionLogApi.md#get_finance_system_connection_log_tags) | **GET** /v3.0/financeSystemConnectionLog/{financeSystemConnectionLogId}/tag | Get the tags for a financeSystemConnectionLog.


# **add_finance_system_connection_log_audit**
> add_finance_system_connection_log_audit(finance_system_connection_log_id, finance_system_connection_log_audit)

Add new audit for a financeSystemConnectionLog

Adds an audit to an existing financeSystemConnectionLog.

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
api_instance = Infoplus.FinanceSystemConnectionLogApi(Infoplus.ApiClient(configuration))
finance_system_connection_log_id = 56 # int | Id of the financeSystemConnectionLog to add an audit to
finance_system_connection_log_audit = 'finance_system_connection_log_audit_example' # str | The audit to add

try:
    # Add new audit for a financeSystemConnectionLog
    api_instance.add_finance_system_connection_log_audit(finance_system_connection_log_id, finance_system_connection_log_audit)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionLogApi->add_finance_system_connection_log_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_log_id** | **int**| Id of the financeSystemConnectionLog to add an audit to | 
 **finance_system_connection_log_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_finance_system_connection_log_file**
> add_finance_system_connection_log_file(finance_system_connection_log_id, file_name)

Attach a file to a financeSystemConnectionLog

Adds a file to an existing financeSystemConnectionLog.

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
api_instance = Infoplus.FinanceSystemConnectionLogApi(Infoplus.ApiClient(configuration))
finance_system_connection_log_id = 56 # int | Id of the financeSystemConnectionLog to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a financeSystemConnectionLog
    api_instance.add_finance_system_connection_log_file(finance_system_connection_log_id, file_name)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionLogApi->add_finance_system_connection_log_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_log_id** | **int**| Id of the financeSystemConnectionLog to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_finance_system_connection_log_file_by_url**
> add_finance_system_connection_log_file_by_url(body, finance_system_connection_log_id)

Attach a file to a financeSystemConnectionLog by URL.

Adds a file to an existing financeSystemConnectionLog by URL.

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
api_instance = Infoplus.FinanceSystemConnectionLogApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
finance_system_connection_log_id = 56 # int | Id of the financeSystemConnectionLog to add an file to

try:
    # Attach a file to a financeSystemConnectionLog by URL.
    api_instance.add_finance_system_connection_log_file_by_url(body, finance_system_connection_log_id)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionLogApi->add_finance_system_connection_log_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **finance_system_connection_log_id** | **int**| Id of the financeSystemConnectionLog to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_finance_system_connection_log_tag**
> add_finance_system_connection_log_tag(finance_system_connection_log_id, finance_system_connection_log_tag)

Add new tags for a financeSystemConnectionLog.

Adds a tag to an existing financeSystemConnectionLog.

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
api_instance = Infoplus.FinanceSystemConnectionLogApi(Infoplus.ApiClient(configuration))
finance_system_connection_log_id = 56 # int | Id of the financeSystemConnectionLog to add a tag to
finance_system_connection_log_tag = 'finance_system_connection_log_tag_example' # str | The tag to add

try:
    # Add new tags for a financeSystemConnectionLog.
    api_instance.add_finance_system_connection_log_tag(finance_system_connection_log_id, finance_system_connection_log_tag)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionLogApi->add_finance_system_connection_log_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_log_id** | **int**| Id of the financeSystemConnectionLog to add a tag to | 
 **finance_system_connection_log_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_finance_system_connection_log_file**
> delete_finance_system_connection_log_file(finance_system_connection_log_id, file_id)

Delete a file for a financeSystemConnectionLog.

Deletes an existing financeSystemConnectionLog file using the specified data.

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
api_instance = Infoplus.FinanceSystemConnectionLogApi(Infoplus.ApiClient(configuration))
finance_system_connection_log_id = 56 # int | Id of the financeSystemConnectionLog to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a financeSystemConnectionLog.
    api_instance.delete_finance_system_connection_log_file(finance_system_connection_log_id, file_id)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionLogApi->delete_finance_system_connection_log_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_log_id** | **int**| Id of the financeSystemConnectionLog to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_finance_system_connection_log_tag**
> delete_finance_system_connection_log_tag(finance_system_connection_log_id, finance_system_connection_log_tag)

Delete a tag for a financeSystemConnectionLog.

Deletes an existing financeSystemConnectionLog tag using the specified data.

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
api_instance = Infoplus.FinanceSystemConnectionLogApi(Infoplus.ApiClient(configuration))
finance_system_connection_log_id = 56 # int | Id of the financeSystemConnectionLog to remove tag from
finance_system_connection_log_tag = 'finance_system_connection_log_tag_example' # str | The tag to delete

try:
    # Delete a tag for a financeSystemConnectionLog.
    api_instance.delete_finance_system_connection_log_tag(finance_system_connection_log_id, finance_system_connection_log_tag)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionLogApi->delete_finance_system_connection_log_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_log_id** | **int**| Id of the financeSystemConnectionLog to remove tag from | 
 **finance_system_connection_log_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_finance_system_connection_log_by_id**
> FinanceSystemConnectionLog get_duplicate_finance_system_connection_log_by_id(finance_system_connection_log_id)

Get a duplicated a financeSystemConnectionLog by id

Returns a duplicated financeSystemConnectionLog identified by the specified id.

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
api_instance = Infoplus.FinanceSystemConnectionLogApi(Infoplus.ApiClient(configuration))
finance_system_connection_log_id = 56 # int | Id of the financeSystemConnectionLog to be duplicated.

try:
    # Get a duplicated a financeSystemConnectionLog by id
    api_response = api_instance.get_duplicate_finance_system_connection_log_by_id(finance_system_connection_log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionLogApi->get_duplicate_finance_system_connection_log_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_log_id** | **int**| Id of the financeSystemConnectionLog to be duplicated. | 

### Return type

[**FinanceSystemConnectionLog**](FinanceSystemConnectionLog.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_system_connection_log_by_filter**
> list[FinanceSystemConnectionLog] get_finance_system_connection_log_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search financeSystemConnectionLogs by filter

Returns the list of financeSystemConnectionLogs that match the given filter.

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
api_instance = Infoplus.FinanceSystemConnectionLogApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search financeSystemConnectionLogs by filter
    api_response = api_instance.get_finance_system_connection_log_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionLogApi->get_finance_system_connection_log_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[FinanceSystemConnectionLog]**](FinanceSystemConnectionLog.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_system_connection_log_by_id**
> FinanceSystemConnectionLog get_finance_system_connection_log_by_id(finance_system_connection_log_id)

Get a financeSystemConnectionLog by id

Returns the financeSystemConnectionLog identified by the specified id.

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
api_instance = Infoplus.FinanceSystemConnectionLogApi(Infoplus.ApiClient(configuration))
finance_system_connection_log_id = 56 # int | Id of the financeSystemConnectionLog to be returned.

try:
    # Get a financeSystemConnectionLog by id
    api_response = api_instance.get_finance_system_connection_log_by_id(finance_system_connection_log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionLogApi->get_finance_system_connection_log_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_log_id** | **int**| Id of the financeSystemConnectionLog to be returned. | 

### Return type

[**FinanceSystemConnectionLog**](FinanceSystemConnectionLog.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_system_connection_log_files**
> get_finance_system_connection_log_files(finance_system_connection_log_id)

Get the files for a financeSystemConnectionLog.

Get all existing financeSystemConnectionLog files.

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
api_instance = Infoplus.FinanceSystemConnectionLogApi(Infoplus.ApiClient(configuration))
finance_system_connection_log_id = 56 # int | Id of the financeSystemConnectionLog to get files for

try:
    # Get the files for a financeSystemConnectionLog.
    api_instance.get_finance_system_connection_log_files(finance_system_connection_log_id)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionLogApi->get_finance_system_connection_log_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_log_id** | **int**| Id of the financeSystemConnectionLog to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_system_connection_log_tags**
> get_finance_system_connection_log_tags(finance_system_connection_log_id)

Get the tags for a financeSystemConnectionLog.

Get all existing financeSystemConnectionLog tags.

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
api_instance = Infoplus.FinanceSystemConnectionLogApi(Infoplus.ApiClient(configuration))
finance_system_connection_log_id = 56 # int | Id of the financeSystemConnectionLog to get tags for

try:
    # Get the tags for a financeSystemConnectionLog.
    api_instance.get_finance_system_connection_log_tags(finance_system_connection_log_id)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionLogApi->get_finance_system_connection_log_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_log_id** | **int**| Id of the financeSystemConnectionLog to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

