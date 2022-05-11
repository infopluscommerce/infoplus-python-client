# Infoplus.QuickReceiptApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_quick_receipt**](QuickReceiptApi.md#add_quick_receipt) | **POST** /v3.0/quickReceipt | Create a quickReceipt
[**add_quick_receipt_audit**](QuickReceiptApi.md#add_quick_receipt_audit) | **PUT** /v3.0/quickReceipt/{quickReceiptId}/audit/{quickReceiptAudit} | Add new audit for a quickReceipt
[**add_quick_receipt_file**](QuickReceiptApi.md#add_quick_receipt_file) | **POST** /v3.0/quickReceipt/{quickReceiptId}/file/{fileName} | Attach a file to a quickReceipt
[**add_quick_receipt_file_by_url**](QuickReceiptApi.md#add_quick_receipt_file_by_url) | **POST** /v3.0/quickReceipt/{quickReceiptId}/file | Attach a file to a quickReceipt by URL.
[**add_quick_receipt_tag**](QuickReceiptApi.md#add_quick_receipt_tag) | **PUT** /v3.0/quickReceipt/{quickReceiptId}/tag/{quickReceiptTag} | Add new tags for a quickReceipt.
[**delete_quick_receipt**](QuickReceiptApi.md#delete_quick_receipt) | **DELETE** /v3.0/quickReceipt/{quickReceiptId} | Delete a quickReceipt
[**delete_quick_receipt_file**](QuickReceiptApi.md#delete_quick_receipt_file) | **DELETE** /v3.0/quickReceipt/{quickReceiptId}/file/{fileId} | Delete a file for a quickReceipt.
[**delete_quick_receipt_tag**](QuickReceiptApi.md#delete_quick_receipt_tag) | **DELETE** /v3.0/quickReceipt/{quickReceiptId}/tag/{quickReceiptTag} | Delete a tag for a quickReceipt.
[**execute_quick_receipt**](QuickReceiptApi.md#execute_quick_receipt) | **POST** /v3.0/quickReceipt/executeQuickReceipt | Run the ExecuteQuickReceipt process.
[**get_duplicate_quick_receipt_by_id**](QuickReceiptApi.md#get_duplicate_quick_receipt_by_id) | **GET** /v3.0/quickReceipt/duplicate/{quickReceiptId} | Get a duplicated a quickReceipt by id
[**get_quick_receipt_by_filter**](QuickReceiptApi.md#get_quick_receipt_by_filter) | **GET** /v3.0/quickReceipt/search | Search quickReceipts by filter
[**get_quick_receipt_by_id**](QuickReceiptApi.md#get_quick_receipt_by_id) | **GET** /v3.0/quickReceipt/{quickReceiptId} | Get a quickReceipt by id
[**get_quick_receipt_files**](QuickReceiptApi.md#get_quick_receipt_files) | **GET** /v3.0/quickReceipt/{quickReceiptId}/file | Get the files for a quickReceipt.
[**get_quick_receipt_tags**](QuickReceiptApi.md#get_quick_receipt_tags) | **GET** /v3.0/quickReceipt/{quickReceiptId}/tag | Get the tags for a quickReceipt.
[**update_quick_receipt**](QuickReceiptApi.md#update_quick_receipt) | **PUT** /v3.0/quickReceipt | Update a quickReceipt
[**update_quick_receipt_custom_fields**](QuickReceiptApi.md#update_quick_receipt_custom_fields) | **PUT** /v3.0/quickReceipt/customFields | Update a quickReceipt custom fields


# **add_quick_receipt**
> QuickReceipt add_quick_receipt(body)

Create a quickReceipt

Inserts a new quickReceipt using the specified data.

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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
body = Infoplus.QuickReceipt() # QuickReceipt | QuickReceipt to be inserted.

try:
    # Create a quickReceipt
    api_response = api_instance.add_quick_receipt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->add_quick_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuickReceipt**](QuickReceipt.md)| QuickReceipt to be inserted. | 

### Return type

[**QuickReceipt**](QuickReceipt.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_quick_receipt_audit**
> add_quick_receipt_audit(quick_receipt_id, quick_receipt_audit)

Add new audit for a quickReceipt

Adds an audit to an existing quickReceipt.

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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
quick_receipt_id = 56 # int | Id of the quickReceipt to add an audit to
quick_receipt_audit = 'quick_receipt_audit_example' # str | The audit to add

try:
    # Add new audit for a quickReceipt
    api_instance.add_quick_receipt_audit(quick_receipt_id, quick_receipt_audit)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->add_quick_receipt_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_receipt_id** | **int**| Id of the quickReceipt to add an audit to | 
 **quick_receipt_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_quick_receipt_file**
> add_quick_receipt_file(quick_receipt_id, file_name)

Attach a file to a quickReceipt

Adds a file to an existing quickReceipt.

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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
quick_receipt_id = 56 # int | Id of the quickReceipt to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a quickReceipt
    api_instance.add_quick_receipt_file(quick_receipt_id, file_name)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->add_quick_receipt_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_receipt_id** | **int**| Id of the quickReceipt to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_quick_receipt_file_by_url**
> add_quick_receipt_file_by_url(body, quick_receipt_id)

Attach a file to a quickReceipt by URL.

Adds a file to an existing quickReceipt by URL.

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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
quick_receipt_id = 56 # int | Id of the quickReceipt to add an file to

try:
    # Attach a file to a quickReceipt by URL.
    api_instance.add_quick_receipt_file_by_url(body, quick_receipt_id)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->add_quick_receipt_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **quick_receipt_id** | **int**| Id of the quickReceipt to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_quick_receipt_tag**
> add_quick_receipt_tag(quick_receipt_id, quick_receipt_tag)

Add new tags for a quickReceipt.

Adds a tag to an existing quickReceipt.

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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
quick_receipt_id = 56 # int | Id of the quickReceipt to add a tag to
quick_receipt_tag = 'quick_receipt_tag_example' # str | The tag to add

try:
    # Add new tags for a quickReceipt.
    api_instance.add_quick_receipt_tag(quick_receipt_id, quick_receipt_tag)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->add_quick_receipt_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_receipt_id** | **int**| Id of the quickReceipt to add a tag to | 
 **quick_receipt_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quick_receipt**
> delete_quick_receipt(quick_receipt_id)

Delete a quickReceipt

Deletes the quickReceipt identified by the specified id.

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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
quick_receipt_id = 56 # int | Id of the quickReceipt to be deleted.

try:
    # Delete a quickReceipt
    api_instance.delete_quick_receipt(quick_receipt_id)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->delete_quick_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_receipt_id** | **int**| Id of the quickReceipt to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quick_receipt_file**
> delete_quick_receipt_file(quick_receipt_id, file_id)

Delete a file for a quickReceipt.

Deletes an existing quickReceipt file using the specified data.

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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
quick_receipt_id = 56 # int | Id of the quickReceipt to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a quickReceipt.
    api_instance.delete_quick_receipt_file(quick_receipt_id, file_id)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->delete_quick_receipt_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_receipt_id** | **int**| Id of the quickReceipt to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quick_receipt_tag**
> delete_quick_receipt_tag(quick_receipt_id, quick_receipt_tag)

Delete a tag for a quickReceipt.

Deletes an existing quickReceipt tag using the specified data.

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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
quick_receipt_id = 56 # int | Id of the quickReceipt to remove tag from
quick_receipt_tag = 'quick_receipt_tag_example' # str | The tag to delete

try:
    # Delete a tag for a quickReceipt.
    api_instance.delete_quick_receipt_tag(quick_receipt_id, quick_receipt_tag)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->delete_quick_receipt_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_receipt_id** | **int**| Id of the quickReceipt to remove tag from | 
 **quick_receipt_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_quick_receipt**
> list[ProcessOutputAPIModel] execute_quick_receipt(body)

Run the ExecuteQuickReceipt process.



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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
body = Infoplus.ExecuteQuickReceiptInputAPIModel() # ExecuteQuickReceiptInputAPIModel | Input data for ExecuteQuickReceipt process.

try:
    # Run the ExecuteQuickReceipt process.
    api_response = api_instance.execute_quick_receipt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->execute_quick_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExecuteQuickReceiptInputAPIModel**](ExecuteQuickReceiptInputAPIModel.md)| Input data for ExecuteQuickReceipt process. | 

### Return type

[**list[ProcessOutputAPIModel]**](ProcessOutputAPIModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_quick_receipt_by_id**
> QuickReceipt get_duplicate_quick_receipt_by_id(quick_receipt_id)

Get a duplicated a quickReceipt by id

Returns a duplicated quickReceipt identified by the specified id.

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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
quick_receipt_id = 56 # int | Id of the quickReceipt to be duplicated.

try:
    # Get a duplicated a quickReceipt by id
    api_response = api_instance.get_duplicate_quick_receipt_by_id(quick_receipt_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->get_duplicate_quick_receipt_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_receipt_id** | **int**| Id of the quickReceipt to be duplicated. | 

### Return type

[**QuickReceipt**](QuickReceipt.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quick_receipt_by_filter**
> list[QuickReceipt] get_quick_receipt_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search quickReceipts by filter

Returns the list of quickReceipts that match the given filter.

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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search quickReceipts by filter
    api_response = api_instance.get_quick_receipt_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->get_quick_receipt_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[QuickReceipt]**](QuickReceipt.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quick_receipt_by_id**
> QuickReceipt get_quick_receipt_by_id(quick_receipt_id)

Get a quickReceipt by id

Returns the quickReceipt identified by the specified id.

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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
quick_receipt_id = 56 # int | Id of the quickReceipt to be returned.

try:
    # Get a quickReceipt by id
    api_response = api_instance.get_quick_receipt_by_id(quick_receipt_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->get_quick_receipt_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_receipt_id** | **int**| Id of the quickReceipt to be returned. | 

### Return type

[**QuickReceipt**](QuickReceipt.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quick_receipt_files**
> get_quick_receipt_files(quick_receipt_id)

Get the files for a quickReceipt.

Get all existing quickReceipt files.

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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
quick_receipt_id = 56 # int | Id of the quickReceipt to get files for

try:
    # Get the files for a quickReceipt.
    api_instance.get_quick_receipt_files(quick_receipt_id)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->get_quick_receipt_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_receipt_id** | **int**| Id of the quickReceipt to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quick_receipt_tags**
> get_quick_receipt_tags(quick_receipt_id)

Get the tags for a quickReceipt.

Get all existing quickReceipt tags.

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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
quick_receipt_id = 56 # int | Id of the quickReceipt to get tags for

try:
    # Get the tags for a quickReceipt.
    api_instance.get_quick_receipt_tags(quick_receipt_id)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->get_quick_receipt_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_receipt_id** | **int**| Id of the quickReceipt to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quick_receipt**
> update_quick_receipt(body)

Update a quickReceipt

Updates an existing quickReceipt using the specified data.

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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
body = Infoplus.QuickReceipt() # QuickReceipt | QuickReceipt to be updated.

try:
    # Update a quickReceipt
    api_instance.update_quick_receipt(body)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->update_quick_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuickReceipt**](QuickReceipt.md)| QuickReceipt to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quick_receipt_custom_fields**
> update_quick_receipt_custom_fields(body)

Update a quickReceipt custom fields

Updates an existing quickReceipt custom fields using the specified data.

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
api_instance = Infoplus.QuickReceiptApi(Infoplus.ApiClient(configuration))
body = Infoplus.QuickReceipt() # QuickReceipt | QuickReceipt to be updated.

try:
    # Update a quickReceipt custom fields
    api_instance.update_quick_receipt_custom_fields(body)
except ApiException as e:
    print("Exception when calling QuickReceiptApi->update_quick_receipt_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuickReceipt**](QuickReceipt.md)| QuickReceipt to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

