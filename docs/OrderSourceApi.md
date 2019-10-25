# Infoplus.OrderSourceApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_order_source**](OrderSourceApi.md#add_order_source) | **POST** /beta/orderSource | Create an orderSource
[**add_order_source_audit**](OrderSourceApi.md#add_order_source_audit) | **PUT** /beta/orderSource/{orderSourceId}/audit/{orderSourceAudit} | Add new audit for an orderSource
[**add_order_source_file**](OrderSourceApi.md#add_order_source_file) | **POST** /beta/orderSource/{orderSourceId}/file/{fileName} | Attach a file to an orderSource
[**add_order_source_tag**](OrderSourceApi.md#add_order_source_tag) | **PUT** /beta/orderSource/{orderSourceId}/tag/{orderSourceTag} | Add new tags for an orderSource.
[**delete_order_source**](OrderSourceApi.md#delete_order_source) | **DELETE** /beta/orderSource/{orderSourceId} | Delete an orderSource
[**delete_order_source_tag**](OrderSourceApi.md#delete_order_source_tag) | **DELETE** /beta/orderSource/{orderSourceId}/tag/{orderSourceTag} | Delete a tag for an orderSource.
[**get_duplicate_order_source_by_id**](OrderSourceApi.md#get_duplicate_order_source_by_id) | **GET** /beta/orderSource/duplicate/{orderSourceId} | Get a duplicated an orderSource by id
[**get_order_source_by_filter**](OrderSourceApi.md#get_order_source_by_filter) | **GET** /beta/orderSource/search | Search orderSources by filter
[**get_order_source_by_id**](OrderSourceApi.md#get_order_source_by_id) | **GET** /beta/orderSource/{orderSourceId} | Get an orderSource by id
[**get_order_source_tags**](OrderSourceApi.md#get_order_source_tags) | **GET** /beta/orderSource/{orderSourceId}/tag | Get the tags for an orderSource.
[**update_order_source**](OrderSourceApi.md#update_order_source) | **PUT** /beta/orderSource | Update an orderSource
[**update_order_source_custom_fields**](OrderSourceApi.md#update_order_source_custom_fields) | **PUT** /beta/orderSource/customFields | Update an orderSource custom fields


# **add_order_source**
> OrderSource add_order_source(body)

Create an orderSource

Inserts a new orderSource using the specified data.

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
api_instance = Infoplus.OrderSourceApi(Infoplus.ApiClient(configuration))
body = Infoplus.OrderSource() # OrderSource | OrderSource to be inserted.

try:
    # Create an orderSource
    api_response = api_instance.add_order_source(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderSourceApi->add_order_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderSource**](OrderSource.md)| OrderSource to be inserted. | 

### Return type

[**OrderSource**](OrderSource.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_source_audit**
> add_order_source_audit(order_source_id, order_source_audit)

Add new audit for an orderSource

Adds an audit to an existing orderSource.

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
api_instance = Infoplus.OrderSourceApi(Infoplus.ApiClient(configuration))
order_source_id = 56 # int | Id of the orderSource to add an audit to
order_source_audit = 'order_source_audit_example' # str | The audit to add

try:
    # Add new audit for an orderSource
    api_instance.add_order_source_audit(order_source_id, order_source_audit)
except ApiException as e:
    print("Exception when calling OrderSourceApi->add_order_source_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_id** | **int**| Id of the orderSource to add an audit to | 
 **order_source_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_source_file**
> add_order_source_file(order_source_id, file_name)

Attach a file to an orderSource

Adds a file to an existing orderSource.

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
api_instance = Infoplus.OrderSourceApi(Infoplus.ApiClient(configuration))
order_source_id = 56 # int | Id of the orderSource to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an orderSource
    api_instance.add_order_source_file(order_source_id, file_name)
except ApiException as e:
    print("Exception when calling OrderSourceApi->add_order_source_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_id** | **int**| Id of the orderSource to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_source_tag**
> add_order_source_tag(order_source_id, order_source_tag)

Add new tags for an orderSource.

Adds a tag to an existing orderSource.

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
api_instance = Infoplus.OrderSourceApi(Infoplus.ApiClient(configuration))
order_source_id = 56 # int | Id of the orderSource to add a tag to
order_source_tag = 'order_source_tag_example' # str | The tag to add

try:
    # Add new tags for an orderSource.
    api_instance.add_order_source_tag(order_source_id, order_source_tag)
except ApiException as e:
    print("Exception when calling OrderSourceApi->add_order_source_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_id** | **int**| Id of the orderSource to add a tag to | 
 **order_source_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_source**
> delete_order_source(order_source_id)

Delete an orderSource

Deletes the orderSource identified by the specified id.

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
api_instance = Infoplus.OrderSourceApi(Infoplus.ApiClient(configuration))
order_source_id = 56 # int | Id of the orderSource to be deleted.

try:
    # Delete an orderSource
    api_instance.delete_order_source(order_source_id)
except ApiException as e:
    print("Exception when calling OrderSourceApi->delete_order_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_id** | **int**| Id of the orderSource to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_source_tag**
> delete_order_source_tag(order_source_id, order_source_tag)

Delete a tag for an orderSource.

Deletes an existing orderSource tag using the specified data.

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
api_instance = Infoplus.OrderSourceApi(Infoplus.ApiClient(configuration))
order_source_id = 56 # int | Id of the orderSource to remove tag from
order_source_tag = 'order_source_tag_example' # str | The tag to delete

try:
    # Delete a tag for an orderSource.
    api_instance.delete_order_source_tag(order_source_id, order_source_tag)
except ApiException as e:
    print("Exception when calling OrderSourceApi->delete_order_source_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_id** | **int**| Id of the orderSource to remove tag from | 
 **order_source_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_order_source_by_id**
> OrderSource get_duplicate_order_source_by_id(order_source_id)

Get a duplicated an orderSource by id

Returns a duplicated orderSource identified by the specified id.

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
api_instance = Infoplus.OrderSourceApi(Infoplus.ApiClient(configuration))
order_source_id = 56 # int | Id of the orderSource to be duplicated.

try:
    # Get a duplicated an orderSource by id
    api_response = api_instance.get_duplicate_order_source_by_id(order_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderSourceApi->get_duplicate_order_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_id** | **int**| Id of the orderSource to be duplicated. | 

### Return type

[**OrderSource**](OrderSource.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_source_by_filter**
> list[OrderSource] get_order_source_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search orderSources by filter

Returns the list of orderSources that match the given filter.

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
api_instance = Infoplus.OrderSourceApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search orderSources by filter
    api_response = api_instance.get_order_source_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderSourceApi->get_order_source_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[OrderSource]**](OrderSource.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_source_by_id**
> OrderSource get_order_source_by_id(order_source_id)

Get an orderSource by id

Returns the orderSource identified by the specified id.

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
api_instance = Infoplus.OrderSourceApi(Infoplus.ApiClient(configuration))
order_source_id = 56 # int | Id of the orderSource to be returned.

try:
    # Get an orderSource by id
    api_response = api_instance.get_order_source_by_id(order_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderSourceApi->get_order_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_id** | **int**| Id of the orderSource to be returned. | 

### Return type

[**OrderSource**](OrderSource.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_source_tags**
> get_order_source_tags(order_source_id)

Get the tags for an orderSource.

Get all existing orderSource tags.

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
api_instance = Infoplus.OrderSourceApi(Infoplus.ApiClient(configuration))
order_source_id = 56 # int | Id of the orderSource to get tags for

try:
    # Get the tags for an orderSource.
    api_instance.get_order_source_tags(order_source_id)
except ApiException as e:
    print("Exception when calling OrderSourceApi->get_order_source_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_id** | **int**| Id of the orderSource to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_source**
> update_order_source(body)

Update an orderSource

Updates an existing orderSource using the specified data.

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
api_instance = Infoplus.OrderSourceApi(Infoplus.ApiClient(configuration))
body = Infoplus.OrderSource() # OrderSource | OrderSource to be updated.

try:
    # Update an orderSource
    api_instance.update_order_source(body)
except ApiException as e:
    print("Exception when calling OrderSourceApi->update_order_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderSource**](OrderSource.md)| OrderSource to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_source_custom_fields**
> update_order_source_custom_fields(body)

Update an orderSource custom fields

Updates an existing orderSource custom fields using the specified data.

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
api_instance = Infoplus.OrderSourceApi(Infoplus.ApiClient(configuration))
body = Infoplus.OrderSource() # OrderSource | OrderSource to be updated.

try:
    # Update an orderSource custom fields
    api_instance.update_order_source_custom_fields(body)
except ApiException as e:
    print("Exception when calling OrderSourceApi->update_order_source_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderSource**](OrderSource.md)| OrderSource to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

