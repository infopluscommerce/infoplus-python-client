# Infoplus.FinanceSystemConnectionApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_finance_system_connection**](FinanceSystemConnectionApi.md#add_finance_system_connection) | **POST** /beta/financeSystemConnection | Create a financeSystemConnection
[**add_finance_system_connection_audit**](FinanceSystemConnectionApi.md#add_finance_system_connection_audit) | **PUT** /beta/financeSystemConnection/{financeSystemConnectionId}/audit/{financeSystemConnectionAudit} | Add new audit for a financeSystemConnection
[**add_finance_system_connection_file**](FinanceSystemConnectionApi.md#add_finance_system_connection_file) | **POST** /beta/financeSystemConnection/{financeSystemConnectionId}/file/{fileName} | Attach a file to a financeSystemConnection
[**add_finance_system_connection_file_by_url**](FinanceSystemConnectionApi.md#add_finance_system_connection_file_by_url) | **POST** /beta/financeSystemConnection/{financeSystemConnectionId}/file | Attach a file to a financeSystemConnection by URL.
[**add_finance_system_connection_tag**](FinanceSystemConnectionApi.md#add_finance_system_connection_tag) | **PUT** /beta/financeSystemConnection/{financeSystemConnectionId}/tag/{financeSystemConnectionTag} | Add new tags for a financeSystemConnection.
[**delete_finance_system_connection**](FinanceSystemConnectionApi.md#delete_finance_system_connection) | **DELETE** /beta/financeSystemConnection/{financeSystemConnectionId} | Delete a financeSystemConnection
[**delete_finance_system_connection_file**](FinanceSystemConnectionApi.md#delete_finance_system_connection_file) | **DELETE** /beta/financeSystemConnection/{financeSystemConnectionId}/file/{fileId} | Delete a file for a financeSystemConnection.
[**delete_finance_system_connection_tag**](FinanceSystemConnectionApi.md#delete_finance_system_connection_tag) | **DELETE** /beta/financeSystemConnection/{financeSystemConnectionId}/tag/{financeSystemConnectionTag} | Delete a tag for a financeSystemConnection.
[**get_duplicate_finance_system_connection_by_id**](FinanceSystemConnectionApi.md#get_duplicate_finance_system_connection_by_id) | **GET** /beta/financeSystemConnection/duplicate/{financeSystemConnectionId} | Get a duplicated a financeSystemConnection by id
[**get_finance_system_connection_by_filter**](FinanceSystemConnectionApi.md#get_finance_system_connection_by_filter) | **GET** /beta/financeSystemConnection/search | Search financeSystemConnections by filter
[**get_finance_system_connection_by_id**](FinanceSystemConnectionApi.md#get_finance_system_connection_by_id) | **GET** /beta/financeSystemConnection/{financeSystemConnectionId} | Get a financeSystemConnection by id
[**get_finance_system_connection_files**](FinanceSystemConnectionApi.md#get_finance_system_connection_files) | **GET** /beta/financeSystemConnection/{financeSystemConnectionId}/file | Get the files for a financeSystemConnection.
[**get_finance_system_connection_tags**](FinanceSystemConnectionApi.md#get_finance_system_connection_tags) | **GET** /beta/financeSystemConnection/{financeSystemConnectionId}/tag | Get the tags for a financeSystemConnection.
[**update_finance_system_connection**](FinanceSystemConnectionApi.md#update_finance_system_connection) | **PUT** /beta/financeSystemConnection | Update a financeSystemConnection
[**update_finance_system_connection_custom_fields**](FinanceSystemConnectionApi.md#update_finance_system_connection_custom_fields) | **PUT** /beta/financeSystemConnection/customFields | Update a financeSystemConnection custom fields


# **add_finance_system_connection**
> FinanceSystemConnection add_finance_system_connection(body)

Create a financeSystemConnection

Inserts a new financeSystemConnection using the specified data.

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
api_instance = Infoplus.FinanceSystemConnectionApi(Infoplus.ApiClient(configuration))
body = Infoplus.FinanceSystemConnection() # FinanceSystemConnection | FinanceSystemConnection to be inserted.

try:
    # Create a financeSystemConnection
    api_response = api_instance.add_finance_system_connection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionApi->add_finance_system_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FinanceSystemConnection**](FinanceSystemConnection.md)| FinanceSystemConnection to be inserted. | 

### Return type

[**FinanceSystemConnection**](FinanceSystemConnection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_finance_system_connection_audit**
> add_finance_system_connection_audit(finance_system_connection_id, finance_system_connection_audit)

Add new audit for a financeSystemConnection

Adds an audit to an existing financeSystemConnection.

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
api_instance = Infoplus.FinanceSystemConnectionApi(Infoplus.ApiClient(configuration))
finance_system_connection_id = 56 # int | Id of the financeSystemConnection to add an audit to
finance_system_connection_audit = 'finance_system_connection_audit_example' # str | The audit to add

try:
    # Add new audit for a financeSystemConnection
    api_instance.add_finance_system_connection_audit(finance_system_connection_id, finance_system_connection_audit)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionApi->add_finance_system_connection_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_id** | **int**| Id of the financeSystemConnection to add an audit to | 
 **finance_system_connection_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_finance_system_connection_file**
> add_finance_system_connection_file(finance_system_connection_id, file_name)

Attach a file to a financeSystemConnection

Adds a file to an existing financeSystemConnection.

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
api_instance = Infoplus.FinanceSystemConnectionApi(Infoplus.ApiClient(configuration))
finance_system_connection_id = 56 # int | Id of the financeSystemConnection to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a financeSystemConnection
    api_instance.add_finance_system_connection_file(finance_system_connection_id, file_name)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionApi->add_finance_system_connection_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_id** | **int**| Id of the financeSystemConnection to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_finance_system_connection_file_by_url**
> add_finance_system_connection_file_by_url(body, finance_system_connection_id)

Attach a file to a financeSystemConnection by URL.

Adds a file to an existing financeSystemConnection by URL.

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
api_instance = Infoplus.FinanceSystemConnectionApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
finance_system_connection_id = 56 # int | Id of the financeSystemConnection to add an file to

try:
    # Attach a file to a financeSystemConnection by URL.
    api_instance.add_finance_system_connection_file_by_url(body, finance_system_connection_id)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionApi->add_finance_system_connection_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **finance_system_connection_id** | **int**| Id of the financeSystemConnection to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_finance_system_connection_tag**
> add_finance_system_connection_tag(finance_system_connection_id, finance_system_connection_tag)

Add new tags for a financeSystemConnection.

Adds a tag to an existing financeSystemConnection.

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
api_instance = Infoplus.FinanceSystemConnectionApi(Infoplus.ApiClient(configuration))
finance_system_connection_id = 56 # int | Id of the financeSystemConnection to add a tag to
finance_system_connection_tag = 'finance_system_connection_tag_example' # str | The tag to add

try:
    # Add new tags for a financeSystemConnection.
    api_instance.add_finance_system_connection_tag(finance_system_connection_id, finance_system_connection_tag)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionApi->add_finance_system_connection_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_id** | **int**| Id of the financeSystemConnection to add a tag to | 
 **finance_system_connection_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_finance_system_connection**
> delete_finance_system_connection(finance_system_connection_id)

Delete a financeSystemConnection

Deletes the financeSystemConnection identified by the specified id.

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
api_instance = Infoplus.FinanceSystemConnectionApi(Infoplus.ApiClient(configuration))
finance_system_connection_id = 56 # int | Id of the financeSystemConnection to be deleted.

try:
    # Delete a financeSystemConnection
    api_instance.delete_finance_system_connection(finance_system_connection_id)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionApi->delete_finance_system_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_id** | **int**| Id of the financeSystemConnection to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_finance_system_connection_file**
> delete_finance_system_connection_file(finance_system_connection_id, file_id)

Delete a file for a financeSystemConnection.

Deletes an existing financeSystemConnection file using the specified data.

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
api_instance = Infoplus.FinanceSystemConnectionApi(Infoplus.ApiClient(configuration))
finance_system_connection_id = 56 # int | Id of the financeSystemConnection to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a financeSystemConnection.
    api_instance.delete_finance_system_connection_file(finance_system_connection_id, file_id)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionApi->delete_finance_system_connection_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_id** | **int**| Id of the financeSystemConnection to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_finance_system_connection_tag**
> delete_finance_system_connection_tag(finance_system_connection_id, finance_system_connection_tag)

Delete a tag for a financeSystemConnection.

Deletes an existing financeSystemConnection tag using the specified data.

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
api_instance = Infoplus.FinanceSystemConnectionApi(Infoplus.ApiClient(configuration))
finance_system_connection_id = 56 # int | Id of the financeSystemConnection to remove tag from
finance_system_connection_tag = 'finance_system_connection_tag_example' # str | The tag to delete

try:
    # Delete a tag for a financeSystemConnection.
    api_instance.delete_finance_system_connection_tag(finance_system_connection_id, finance_system_connection_tag)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionApi->delete_finance_system_connection_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_id** | **int**| Id of the financeSystemConnection to remove tag from | 
 **finance_system_connection_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_finance_system_connection_by_id**
> FinanceSystemConnection get_duplicate_finance_system_connection_by_id(finance_system_connection_id)

Get a duplicated a financeSystemConnection by id

Returns a duplicated financeSystemConnection identified by the specified id.

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
api_instance = Infoplus.FinanceSystemConnectionApi(Infoplus.ApiClient(configuration))
finance_system_connection_id = 56 # int | Id of the financeSystemConnection to be duplicated.

try:
    # Get a duplicated a financeSystemConnection by id
    api_response = api_instance.get_duplicate_finance_system_connection_by_id(finance_system_connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionApi->get_duplicate_finance_system_connection_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_id** | **int**| Id of the financeSystemConnection to be duplicated. | 

### Return type

[**FinanceSystemConnection**](FinanceSystemConnection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_system_connection_by_filter**
> list[FinanceSystemConnection] get_finance_system_connection_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search financeSystemConnections by filter

Returns the list of financeSystemConnections that match the given filter.

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
api_instance = Infoplus.FinanceSystemConnectionApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search financeSystemConnections by filter
    api_response = api_instance.get_finance_system_connection_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionApi->get_finance_system_connection_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[FinanceSystemConnection]**](FinanceSystemConnection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_system_connection_by_id**
> FinanceSystemConnection get_finance_system_connection_by_id(finance_system_connection_id)

Get a financeSystemConnection by id

Returns the financeSystemConnection identified by the specified id.

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
api_instance = Infoplus.FinanceSystemConnectionApi(Infoplus.ApiClient(configuration))
finance_system_connection_id = 56 # int | Id of the financeSystemConnection to be returned.

try:
    # Get a financeSystemConnection by id
    api_response = api_instance.get_finance_system_connection_by_id(finance_system_connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionApi->get_finance_system_connection_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_id** | **int**| Id of the financeSystemConnection to be returned. | 

### Return type

[**FinanceSystemConnection**](FinanceSystemConnection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_system_connection_files**
> get_finance_system_connection_files(finance_system_connection_id)

Get the files for a financeSystemConnection.

Get all existing financeSystemConnection files.

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
api_instance = Infoplus.FinanceSystemConnectionApi(Infoplus.ApiClient(configuration))
finance_system_connection_id = 56 # int | Id of the financeSystemConnection to get files for

try:
    # Get the files for a financeSystemConnection.
    api_instance.get_finance_system_connection_files(finance_system_connection_id)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionApi->get_finance_system_connection_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_id** | **int**| Id of the financeSystemConnection to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_system_connection_tags**
> get_finance_system_connection_tags(finance_system_connection_id)

Get the tags for a financeSystemConnection.

Get all existing financeSystemConnection tags.

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
api_instance = Infoplus.FinanceSystemConnectionApi(Infoplus.ApiClient(configuration))
finance_system_connection_id = 56 # int | Id of the financeSystemConnection to get tags for

try:
    # Get the tags for a financeSystemConnection.
    api_instance.get_finance_system_connection_tags(finance_system_connection_id)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionApi->get_finance_system_connection_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finance_system_connection_id** | **int**| Id of the financeSystemConnection to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_finance_system_connection**
> update_finance_system_connection(body)

Update a financeSystemConnection

Updates an existing financeSystemConnection using the specified data.

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
api_instance = Infoplus.FinanceSystemConnectionApi(Infoplus.ApiClient(configuration))
body = Infoplus.FinanceSystemConnection() # FinanceSystemConnection | FinanceSystemConnection to be updated.

try:
    # Update a financeSystemConnection
    api_instance.update_finance_system_connection(body)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionApi->update_finance_system_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FinanceSystemConnection**](FinanceSystemConnection.md)| FinanceSystemConnection to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_finance_system_connection_custom_fields**
> update_finance_system_connection_custom_fields(body)

Update a financeSystemConnection custom fields

Updates an existing financeSystemConnection custom fields using the specified data.

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
api_instance = Infoplus.FinanceSystemConnectionApi(Infoplus.ApiClient(configuration))
body = Infoplus.FinanceSystemConnection() # FinanceSystemConnection | FinanceSystemConnection to be updated.

try:
    # Update a financeSystemConnection custom fields
    api_instance.update_finance_system_connection_custom_fields(body)
except ApiException as e:
    print("Exception when calling FinanceSystemConnectionApi->update_finance_system_connection_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FinanceSystemConnection**](FinanceSystemConnection.md)| FinanceSystemConnection to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

