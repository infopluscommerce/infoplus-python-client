# Infoplus.OrderLineApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_order_line_audit**](OrderLineApi.md#add_order_line_audit) | **PUT** /v3.0/orderLine/{orderLineId}/audit/{orderLineAudit} | Add new audit for an orderLine
[**add_order_line_file**](OrderLineApi.md#add_order_line_file) | **POST** /v3.0/orderLine/{orderLineId}/file/{fileName} | Attach a file to an orderLine
[**add_order_line_file_by_url**](OrderLineApi.md#add_order_line_file_by_url) | **POST** /v3.0/orderLine/{orderLineId}/file | Attach a file to an orderLine by URL.
[**add_order_line_tag**](OrderLineApi.md#add_order_line_tag) | **PUT** /v3.0/orderLine/{orderLineId}/tag/{orderLineTag} | Add new tags for an orderLine.
[**delete_order_line_file**](OrderLineApi.md#delete_order_line_file) | **DELETE** /v3.0/orderLine/{orderLineId}/file/{fileId} | Delete a file for an orderLine.
[**delete_order_line_tag**](OrderLineApi.md#delete_order_line_tag) | **DELETE** /v3.0/orderLine/{orderLineId}/tag/{orderLineTag} | Delete a tag for an orderLine.
[**get_duplicate_order_line_by_id**](OrderLineApi.md#get_duplicate_order_line_by_id) | **GET** /v3.0/orderLine/duplicate/{orderLineId} | Get a duplicated an orderLine by id
[**get_order_line_by_filter**](OrderLineApi.md#get_order_line_by_filter) | **GET** /v3.0/orderLine/search | Search orderLines by filter
[**get_order_line_by_id**](OrderLineApi.md#get_order_line_by_id) | **GET** /v3.0/orderLine/{orderLineId} | Get an orderLine by id
[**get_order_line_files**](OrderLineApi.md#get_order_line_files) | **GET** /v3.0/orderLine/{orderLineId}/file | Get the files for an orderLine.
[**get_order_line_tags**](OrderLineApi.md#get_order_line_tags) | **GET** /v3.0/orderLine/{orderLineId}/tag | Get the tags for an orderLine.
[**update_order_line_custom_fields**](OrderLineApi.md#update_order_line_custom_fields) | **PUT** /v3.0/orderLine/customFields | Update an orderLine custom fields


# **add_order_line_audit**
> add_order_line_audit(order_line_id, order_line_audit)

Add new audit for an orderLine

Adds an audit to an existing orderLine.

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
api_instance = Infoplus.OrderLineApi(Infoplus.ApiClient(configuration))
order_line_id = 56 # int | Id of the orderLine to add an audit to
order_line_audit = 'order_line_audit_example' # str | The audit to add

try:
    # Add new audit for an orderLine
    api_instance.add_order_line_audit(order_line_id, order_line_audit)
except ApiException as e:
    print("Exception when calling OrderLineApi->add_order_line_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_id** | **int**| Id of the orderLine to add an audit to | 
 **order_line_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_line_file**
> add_order_line_file(order_line_id, file_name)

Attach a file to an orderLine

Adds a file to an existing orderLine.

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
api_instance = Infoplus.OrderLineApi(Infoplus.ApiClient(configuration))
order_line_id = 56 # int | Id of the orderLine to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an orderLine
    api_instance.add_order_line_file(order_line_id, file_name)
except ApiException as e:
    print("Exception when calling OrderLineApi->add_order_line_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_id** | **int**| Id of the orderLine to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_line_file_by_url**
> add_order_line_file_by_url(body, order_line_id)

Attach a file to an orderLine by URL.

Adds a file to an existing orderLine by URL.

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
api_instance = Infoplus.OrderLineApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
order_line_id = 56 # int | Id of the orderLine to add an file to

try:
    # Attach a file to an orderLine by URL.
    api_instance.add_order_line_file_by_url(body, order_line_id)
except ApiException as e:
    print("Exception when calling OrderLineApi->add_order_line_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **order_line_id** | **int**| Id of the orderLine to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_line_tag**
> add_order_line_tag(order_line_id, order_line_tag)

Add new tags for an orderLine.

Adds a tag to an existing orderLine.

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
api_instance = Infoplus.OrderLineApi(Infoplus.ApiClient(configuration))
order_line_id = 56 # int | Id of the orderLine to add a tag to
order_line_tag = 'order_line_tag_example' # str | The tag to add

try:
    # Add new tags for an orderLine.
    api_instance.add_order_line_tag(order_line_id, order_line_tag)
except ApiException as e:
    print("Exception when calling OrderLineApi->add_order_line_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_id** | **int**| Id of the orderLine to add a tag to | 
 **order_line_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_line_file**
> delete_order_line_file(order_line_id, file_id)

Delete a file for an orderLine.

Deletes an existing orderLine file using the specified data.

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
api_instance = Infoplus.OrderLineApi(Infoplus.ApiClient(configuration))
order_line_id = 56 # int | Id of the orderLine to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an orderLine.
    api_instance.delete_order_line_file(order_line_id, file_id)
except ApiException as e:
    print("Exception when calling OrderLineApi->delete_order_line_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_id** | **int**| Id of the orderLine to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_line_tag**
> delete_order_line_tag(order_line_id, order_line_tag)

Delete a tag for an orderLine.

Deletes an existing orderLine tag using the specified data.

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
api_instance = Infoplus.OrderLineApi(Infoplus.ApiClient(configuration))
order_line_id = 56 # int | Id of the orderLine to remove tag from
order_line_tag = 'order_line_tag_example' # str | The tag to delete

try:
    # Delete a tag for an orderLine.
    api_instance.delete_order_line_tag(order_line_id, order_line_tag)
except ApiException as e:
    print("Exception when calling OrderLineApi->delete_order_line_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_id** | **int**| Id of the orderLine to remove tag from | 
 **order_line_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_order_line_by_id**
> OrderLine get_duplicate_order_line_by_id(order_line_id)

Get a duplicated an orderLine by id

Returns a duplicated orderLine identified by the specified id.

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
api_instance = Infoplus.OrderLineApi(Infoplus.ApiClient(configuration))
order_line_id = 56 # int | Id of the orderLine to be duplicated.

try:
    # Get a duplicated an orderLine by id
    api_response = api_instance.get_duplicate_order_line_by_id(order_line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderLineApi->get_duplicate_order_line_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_id** | **int**| Id of the orderLine to be duplicated. | 

### Return type

[**OrderLine**](OrderLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_line_by_filter**
> list[OrderLine] get_order_line_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search orderLines by filter

Returns the list of orderLines that match the given filter.

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
api_instance = Infoplus.OrderLineApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search orderLines by filter
    api_response = api_instance.get_order_line_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderLineApi->get_order_line_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[OrderLine]**](OrderLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_line_by_id**
> OrderLine get_order_line_by_id(order_line_id)

Get an orderLine by id

Returns the orderLine identified by the specified id.

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
api_instance = Infoplus.OrderLineApi(Infoplus.ApiClient(configuration))
order_line_id = 56 # int | Id of the orderLine to be returned.

try:
    # Get an orderLine by id
    api_response = api_instance.get_order_line_by_id(order_line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderLineApi->get_order_line_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_id** | **int**| Id of the orderLine to be returned. | 

### Return type

[**OrderLine**](OrderLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_line_files**
> get_order_line_files(order_line_id)

Get the files for an orderLine.

Get all existing orderLine files.

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
api_instance = Infoplus.OrderLineApi(Infoplus.ApiClient(configuration))
order_line_id = 56 # int | Id of the orderLine to get files for

try:
    # Get the files for an orderLine.
    api_instance.get_order_line_files(order_line_id)
except ApiException as e:
    print("Exception when calling OrderLineApi->get_order_line_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_id** | **int**| Id of the orderLine to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_line_tags**
> get_order_line_tags(order_line_id)

Get the tags for an orderLine.

Get all existing orderLine tags.

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
api_instance = Infoplus.OrderLineApi(Infoplus.ApiClient(configuration))
order_line_id = 56 # int | Id of the orderLine to get tags for

try:
    # Get the tags for an orderLine.
    api_instance.get_order_line_tags(order_line_id)
except ApiException as e:
    print("Exception when calling OrderLineApi->get_order_line_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_id** | **int**| Id of the orderLine to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_line_custom_fields**
> update_order_line_custom_fields(body)

Update an orderLine custom fields

Updates an existing orderLine custom fields using the specified data.

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
api_instance = Infoplus.OrderLineApi(Infoplus.ApiClient(configuration))
body = Infoplus.OrderLine() # OrderLine | OrderLine to be updated.

try:
    # Update an orderLine custom fields
    api_instance.update_order_line_custom_fields(body)
except ApiException as e:
    print("Exception when calling OrderLineApi->update_order_line_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderLine**](OrderLine.md)| OrderLine to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

