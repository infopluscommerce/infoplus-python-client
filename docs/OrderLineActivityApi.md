# Infoplus.OrderLineActivityApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_order_line_activity**](OrderLineActivityApi.md#add_order_line_activity) | **POST** /beta/orderLineActivity | Create an orderLineActivity
[**add_order_line_activity_audit**](OrderLineActivityApi.md#add_order_line_activity_audit) | **PUT** /beta/orderLineActivity/{orderLineActivityId}/audit/{orderLineActivityAudit} | Add new audit for an orderLineActivity
[**add_order_line_activity_file**](OrderLineActivityApi.md#add_order_line_activity_file) | **POST** /beta/orderLineActivity/{orderLineActivityId}/file/{fileName} | Attach a file to an orderLineActivity
[**add_order_line_activity_tag**](OrderLineActivityApi.md#add_order_line_activity_tag) | **PUT** /beta/orderLineActivity/{orderLineActivityId}/tag/{orderLineActivityTag} | Add new tags for an orderLineActivity.
[**delete_order_line_activity**](OrderLineActivityApi.md#delete_order_line_activity) | **DELETE** /beta/orderLineActivity/{orderLineActivityId} | Delete an orderLineActivity
[**delete_order_line_activity_tag**](OrderLineActivityApi.md#delete_order_line_activity_tag) | **DELETE** /beta/orderLineActivity/{orderLineActivityId}/tag/{orderLineActivityTag} | Delete a tag for an orderLineActivity.
[**get_duplicate_order_line_activity_by_id**](OrderLineActivityApi.md#get_duplicate_order_line_activity_by_id) | **GET** /beta/orderLineActivity/duplicate/{orderLineActivityId} | Get a duplicated an orderLineActivity by id
[**get_order_line_activity_by_filter**](OrderLineActivityApi.md#get_order_line_activity_by_filter) | **GET** /beta/orderLineActivity/search | Search orderLineActivitys by filter
[**get_order_line_activity_by_id**](OrderLineActivityApi.md#get_order_line_activity_by_id) | **GET** /beta/orderLineActivity/{orderLineActivityId} | Get an orderLineActivity by id
[**get_order_line_activity_tags**](OrderLineActivityApi.md#get_order_line_activity_tags) | **GET** /beta/orderLineActivity/{orderLineActivityId}/tag | Get the tags for an orderLineActivity.
[**update_order_line_activity**](OrderLineActivityApi.md#update_order_line_activity) | **PUT** /beta/orderLineActivity | Update an orderLineActivity


# **add_order_line_activity**
> OrderLineActivity add_order_line_activity(body)

Create an orderLineActivity

Inserts a new orderLineActivity using the specified data.

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
api_instance = Infoplus.OrderLineActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.OrderLineActivity() # OrderLineActivity | OrderLineActivity to be inserted.

try:
    # Create an orderLineActivity
    api_response = api_instance.add_order_line_activity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderLineActivityApi->add_order_line_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderLineActivity**](OrderLineActivity.md)| OrderLineActivity to be inserted. | 

### Return type

[**OrderLineActivity**](OrderLineActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_line_activity_audit**
> add_order_line_activity_audit(order_line_activity_id, order_line_activity_audit)

Add new audit for an orderLineActivity

Adds an audit to an existing orderLineActivity.

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
api_instance = Infoplus.OrderLineActivityApi(Infoplus.ApiClient(configuration))
order_line_activity_id = 56 # int | Id of the orderLineActivity to add an audit to
order_line_activity_audit = 'order_line_activity_audit_example' # str | The audit to add

try:
    # Add new audit for an orderLineActivity
    api_instance.add_order_line_activity_audit(order_line_activity_id, order_line_activity_audit)
except ApiException as e:
    print("Exception when calling OrderLineActivityApi->add_order_line_activity_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_activity_id** | **int**| Id of the orderLineActivity to add an audit to | 
 **order_line_activity_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_line_activity_file**
> add_order_line_activity_file(order_line_activity_id, file_name)

Attach a file to an orderLineActivity

Adds a file to an existing orderLineActivity.

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
api_instance = Infoplus.OrderLineActivityApi(Infoplus.ApiClient(configuration))
order_line_activity_id = 56 # int | Id of the orderLineActivity to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an orderLineActivity
    api_instance.add_order_line_activity_file(order_line_activity_id, file_name)
except ApiException as e:
    print("Exception when calling OrderLineActivityApi->add_order_line_activity_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_activity_id** | **int**| Id of the orderLineActivity to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_line_activity_tag**
> add_order_line_activity_tag(order_line_activity_id, order_line_activity_tag)

Add new tags for an orderLineActivity.

Adds a tag to an existing orderLineActivity.

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
api_instance = Infoplus.OrderLineActivityApi(Infoplus.ApiClient(configuration))
order_line_activity_id = 56 # int | Id of the orderLineActivity to add a tag to
order_line_activity_tag = 'order_line_activity_tag_example' # str | The tag to add

try:
    # Add new tags for an orderLineActivity.
    api_instance.add_order_line_activity_tag(order_line_activity_id, order_line_activity_tag)
except ApiException as e:
    print("Exception when calling OrderLineActivityApi->add_order_line_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_activity_id** | **int**| Id of the orderLineActivity to add a tag to | 
 **order_line_activity_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_line_activity**
> delete_order_line_activity(order_line_activity_id)

Delete an orderLineActivity

Deletes the orderLineActivity identified by the specified id.

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
api_instance = Infoplus.OrderLineActivityApi(Infoplus.ApiClient(configuration))
order_line_activity_id = 56 # int | Id of the orderLineActivity to be deleted.

try:
    # Delete an orderLineActivity
    api_instance.delete_order_line_activity(order_line_activity_id)
except ApiException as e:
    print("Exception when calling OrderLineActivityApi->delete_order_line_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_activity_id** | **int**| Id of the orderLineActivity to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_line_activity_tag**
> delete_order_line_activity_tag(order_line_activity_id, order_line_activity_tag)

Delete a tag for an orderLineActivity.

Deletes an existing orderLineActivity tag using the specified data.

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
api_instance = Infoplus.OrderLineActivityApi(Infoplus.ApiClient(configuration))
order_line_activity_id = 56 # int | Id of the orderLineActivity to remove tag from
order_line_activity_tag = 'order_line_activity_tag_example' # str | The tag to delete

try:
    # Delete a tag for an orderLineActivity.
    api_instance.delete_order_line_activity_tag(order_line_activity_id, order_line_activity_tag)
except ApiException as e:
    print("Exception when calling OrderLineActivityApi->delete_order_line_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_activity_id** | **int**| Id of the orderLineActivity to remove tag from | 
 **order_line_activity_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_order_line_activity_by_id**
> OrderLineActivity get_duplicate_order_line_activity_by_id(order_line_activity_id)

Get a duplicated an orderLineActivity by id

Returns a duplicated orderLineActivity identified by the specified id.

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
api_instance = Infoplus.OrderLineActivityApi(Infoplus.ApiClient(configuration))
order_line_activity_id = 56 # int | Id of the orderLineActivity to be duplicated.

try:
    # Get a duplicated an orderLineActivity by id
    api_response = api_instance.get_duplicate_order_line_activity_by_id(order_line_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderLineActivityApi->get_duplicate_order_line_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_activity_id** | **int**| Id of the orderLineActivity to be duplicated. | 

### Return type

[**OrderLineActivity**](OrderLineActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_line_activity_by_filter**
> list[OrderLineActivity] get_order_line_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search orderLineActivitys by filter

Returns the list of orderLineActivitys that match the given filter.

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
api_instance = Infoplus.OrderLineActivityApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search orderLineActivitys by filter
    api_response = api_instance.get_order_line_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderLineActivityApi->get_order_line_activity_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[OrderLineActivity]**](OrderLineActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_line_activity_by_id**
> OrderLineActivity get_order_line_activity_by_id(order_line_activity_id)

Get an orderLineActivity by id

Returns the orderLineActivity identified by the specified id.

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
api_instance = Infoplus.OrderLineActivityApi(Infoplus.ApiClient(configuration))
order_line_activity_id = 56 # int | Id of the orderLineActivity to be returned.

try:
    # Get an orderLineActivity by id
    api_response = api_instance.get_order_line_activity_by_id(order_line_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderLineActivityApi->get_order_line_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_activity_id** | **int**| Id of the orderLineActivity to be returned. | 

### Return type

[**OrderLineActivity**](OrderLineActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_line_activity_tags**
> get_order_line_activity_tags(order_line_activity_id)

Get the tags for an orderLineActivity.

Get all existing orderLineActivity tags.

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
api_instance = Infoplus.OrderLineActivityApi(Infoplus.ApiClient(configuration))
order_line_activity_id = 56 # int | Id of the orderLineActivity to get tags for

try:
    # Get the tags for an orderLineActivity.
    api_instance.get_order_line_activity_tags(order_line_activity_id)
except ApiException as e:
    print("Exception when calling OrderLineActivityApi->get_order_line_activity_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_line_activity_id** | **int**| Id of the orderLineActivity to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_line_activity**
> update_order_line_activity(body)

Update an orderLineActivity

Updates an existing orderLineActivity using the specified data.

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
api_instance = Infoplus.OrderLineActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.OrderLineActivity() # OrderLineActivity | OrderLineActivity to be updated.

try:
    # Update an orderLineActivity
    api_instance.update_order_line_activity(body)
except ApiException as e:
    print("Exception when calling OrderLineActivityApi->update_order_line_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderLineActivity**](OrderLineActivity.md)| OrderLineActivity to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

