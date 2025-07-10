# Infoplus.ReturnOrderLineApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_return_order_line_audit**](ReturnOrderLineApi.md#add_return_order_line_audit) | **PUT** /beta/returnOrderLine/{returnOrderLineId}/audit/{returnOrderLineAudit} | Add new audit for a returnOrderLine
[**add_return_order_line_file**](ReturnOrderLineApi.md#add_return_order_line_file) | **POST** /beta/returnOrderLine/{returnOrderLineId}/file/{fileName} | Attach a file to a returnOrderLine
[**add_return_order_line_file_by_url**](ReturnOrderLineApi.md#add_return_order_line_file_by_url) | **POST** /beta/returnOrderLine/{returnOrderLineId}/file | Attach a file to a returnOrderLine by URL.
[**add_return_order_line_tag**](ReturnOrderLineApi.md#add_return_order_line_tag) | **PUT** /beta/returnOrderLine/{returnOrderLineId}/tag/{returnOrderLineTag} | Add new tags for a returnOrderLine.
[**delete_return_order_line_file**](ReturnOrderLineApi.md#delete_return_order_line_file) | **DELETE** /beta/returnOrderLine/{returnOrderLineId}/file/{fileId} | Delete a file for a returnOrderLine.
[**delete_return_order_line_tag**](ReturnOrderLineApi.md#delete_return_order_line_tag) | **DELETE** /beta/returnOrderLine/{returnOrderLineId}/tag/{returnOrderLineTag} | Delete a tag for a returnOrderLine.
[**get_duplicate_return_order_line_by_id**](ReturnOrderLineApi.md#get_duplicate_return_order_line_by_id) | **GET** /beta/returnOrderLine/duplicate/{returnOrderLineId} | Get a duplicated a returnOrderLine by id
[**get_return_order_line_by_filter**](ReturnOrderLineApi.md#get_return_order_line_by_filter) | **GET** /beta/returnOrderLine/search | Search returnOrderLines by filter
[**get_return_order_line_by_id**](ReturnOrderLineApi.md#get_return_order_line_by_id) | **GET** /beta/returnOrderLine/{returnOrderLineId} | Get a returnOrderLine by id
[**get_return_order_line_files**](ReturnOrderLineApi.md#get_return_order_line_files) | **GET** /beta/returnOrderLine/{returnOrderLineId}/file | Get the files for a returnOrderLine.
[**get_return_order_line_tags**](ReturnOrderLineApi.md#get_return_order_line_tags) | **GET** /beta/returnOrderLine/{returnOrderLineId}/tag | Get the tags for a returnOrderLine.
[**update_return_order_line_custom_fields**](ReturnOrderLineApi.md#update_return_order_line_custom_fields) | **PUT** /beta/returnOrderLine/customFields | Update a returnOrderLine custom fields


# **add_return_order_line_audit**
> add_return_order_line_audit(return_order_line_id, return_order_line_audit)

Add new audit for a returnOrderLine

Adds an audit to an existing returnOrderLine.

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
api_instance = Infoplus.ReturnOrderLineApi(Infoplus.ApiClient(configuration))
return_order_line_id = 56 # int | Id of the returnOrderLine to add an audit to
return_order_line_audit = 'return_order_line_audit_example' # str | The audit to add

try:
    # Add new audit for a returnOrderLine
    api_instance.add_return_order_line_audit(return_order_line_id, return_order_line_audit)
except ApiException as e:
    print("Exception when calling ReturnOrderLineApi->add_return_order_line_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_id** | **int**| Id of the returnOrderLine to add an audit to | 
 **return_order_line_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_return_order_line_file**
> add_return_order_line_file(return_order_line_id, file_name)

Attach a file to a returnOrderLine

Adds a file to an existing returnOrderLine.

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
api_instance = Infoplus.ReturnOrderLineApi(Infoplus.ApiClient(configuration))
return_order_line_id = 56 # int | Id of the returnOrderLine to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a returnOrderLine
    api_instance.add_return_order_line_file(return_order_line_id, file_name)
except ApiException as e:
    print("Exception when calling ReturnOrderLineApi->add_return_order_line_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_id** | **int**| Id of the returnOrderLine to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_return_order_line_file_by_url**
> add_return_order_line_file_by_url(body, return_order_line_id)

Attach a file to a returnOrderLine by URL.

Adds a file to an existing returnOrderLine by URL.

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
api_instance = Infoplus.ReturnOrderLineApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
return_order_line_id = 56 # int | Id of the returnOrderLine to add an file to

try:
    # Attach a file to a returnOrderLine by URL.
    api_instance.add_return_order_line_file_by_url(body, return_order_line_id)
except ApiException as e:
    print("Exception when calling ReturnOrderLineApi->add_return_order_line_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **return_order_line_id** | **int**| Id of the returnOrderLine to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_return_order_line_tag**
> add_return_order_line_tag(return_order_line_id, return_order_line_tag)

Add new tags for a returnOrderLine.

Adds a tag to an existing returnOrderLine.

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
api_instance = Infoplus.ReturnOrderLineApi(Infoplus.ApiClient(configuration))
return_order_line_id = 56 # int | Id of the returnOrderLine to add a tag to
return_order_line_tag = 'return_order_line_tag_example' # str | The tag to add

try:
    # Add new tags for a returnOrderLine.
    api_instance.add_return_order_line_tag(return_order_line_id, return_order_line_tag)
except ApiException as e:
    print("Exception when calling ReturnOrderLineApi->add_return_order_line_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_id** | **int**| Id of the returnOrderLine to add a tag to | 
 **return_order_line_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_return_order_line_file**
> delete_return_order_line_file(return_order_line_id, file_id)

Delete a file for a returnOrderLine.

Deletes an existing returnOrderLine file using the specified data.

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
api_instance = Infoplus.ReturnOrderLineApi(Infoplus.ApiClient(configuration))
return_order_line_id = 56 # int | Id of the returnOrderLine to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a returnOrderLine.
    api_instance.delete_return_order_line_file(return_order_line_id, file_id)
except ApiException as e:
    print("Exception when calling ReturnOrderLineApi->delete_return_order_line_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_id** | **int**| Id of the returnOrderLine to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_return_order_line_tag**
> delete_return_order_line_tag(return_order_line_id, return_order_line_tag)

Delete a tag for a returnOrderLine.

Deletes an existing returnOrderLine tag using the specified data.

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
api_instance = Infoplus.ReturnOrderLineApi(Infoplus.ApiClient(configuration))
return_order_line_id = 56 # int | Id of the returnOrderLine to remove tag from
return_order_line_tag = 'return_order_line_tag_example' # str | The tag to delete

try:
    # Delete a tag for a returnOrderLine.
    api_instance.delete_return_order_line_tag(return_order_line_id, return_order_line_tag)
except ApiException as e:
    print("Exception when calling ReturnOrderLineApi->delete_return_order_line_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_id** | **int**| Id of the returnOrderLine to remove tag from | 
 **return_order_line_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_return_order_line_by_id**
> ReturnOrderLine get_duplicate_return_order_line_by_id(return_order_line_id)

Get a duplicated a returnOrderLine by id

Returns a duplicated returnOrderLine identified by the specified id.

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
api_instance = Infoplus.ReturnOrderLineApi(Infoplus.ApiClient(configuration))
return_order_line_id = 56 # int | Id of the returnOrderLine to be duplicated.

try:
    # Get a duplicated a returnOrderLine by id
    api_response = api_instance.get_duplicate_return_order_line_by_id(return_order_line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnOrderLineApi->get_duplicate_return_order_line_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_id** | **int**| Id of the returnOrderLine to be duplicated. | 

### Return type

[**ReturnOrderLine**](ReturnOrderLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_order_line_by_filter**
> list[ReturnOrderLine] get_return_order_line_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search returnOrderLines by filter

Returns the list of returnOrderLines that match the given filter.

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
api_instance = Infoplus.ReturnOrderLineApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search returnOrderLines by filter
    api_response = api_instance.get_return_order_line_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnOrderLineApi->get_return_order_line_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ReturnOrderLine]**](ReturnOrderLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_order_line_by_id**
> ReturnOrderLine get_return_order_line_by_id(return_order_line_id)

Get a returnOrderLine by id

Returns the returnOrderLine identified by the specified id.

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
api_instance = Infoplus.ReturnOrderLineApi(Infoplus.ApiClient(configuration))
return_order_line_id = 56 # int | Id of the returnOrderLine to be returned.

try:
    # Get a returnOrderLine by id
    api_response = api_instance.get_return_order_line_by_id(return_order_line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnOrderLineApi->get_return_order_line_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_id** | **int**| Id of the returnOrderLine to be returned. | 

### Return type

[**ReturnOrderLine**](ReturnOrderLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_order_line_files**
> get_return_order_line_files(return_order_line_id)

Get the files for a returnOrderLine.

Get all existing returnOrderLine files.

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
api_instance = Infoplus.ReturnOrderLineApi(Infoplus.ApiClient(configuration))
return_order_line_id = 56 # int | Id of the returnOrderLine to get files for

try:
    # Get the files for a returnOrderLine.
    api_instance.get_return_order_line_files(return_order_line_id)
except ApiException as e:
    print("Exception when calling ReturnOrderLineApi->get_return_order_line_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_id** | **int**| Id of the returnOrderLine to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_order_line_tags**
> get_return_order_line_tags(return_order_line_id)

Get the tags for a returnOrderLine.

Get all existing returnOrderLine tags.

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
api_instance = Infoplus.ReturnOrderLineApi(Infoplus.ApiClient(configuration))
return_order_line_id = 56 # int | Id of the returnOrderLine to get tags for

try:
    # Get the tags for a returnOrderLine.
    api_instance.get_return_order_line_tags(return_order_line_id)
except ApiException as e:
    print("Exception when calling ReturnOrderLineApi->get_return_order_line_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_id** | **int**| Id of the returnOrderLine to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_return_order_line_custom_fields**
> update_return_order_line_custom_fields(body)

Update a returnOrderLine custom fields

Updates an existing returnOrderLine custom fields using the specified data.

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
api_instance = Infoplus.ReturnOrderLineApi(Infoplus.ApiClient(configuration))
body = Infoplus.ReturnOrderLine() # ReturnOrderLine | ReturnOrderLine to be updated.

try:
    # Update a returnOrderLine custom fields
    api_instance.update_return_order_line_custom_fields(body)
except ApiException as e:
    print("Exception when calling ReturnOrderLineApi->update_return_order_line_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReturnOrderLine**](ReturnOrderLine.md)| ReturnOrderLine to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

