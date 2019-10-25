# Infoplus.OrderActivityApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_order_activity**](OrderActivityApi.md#add_order_activity) | **POST** /beta/orderActivity | Create an orderActivity
[**add_order_activity_audit**](OrderActivityApi.md#add_order_activity_audit) | **PUT** /beta/orderActivity/{orderActivityId}/audit/{orderActivityAudit} | Add new audit for an orderActivity
[**add_order_activity_file**](OrderActivityApi.md#add_order_activity_file) | **POST** /beta/orderActivity/{orderActivityId}/file/{fileName} | Attach a file to an orderActivity
[**add_order_activity_tag**](OrderActivityApi.md#add_order_activity_tag) | **PUT** /beta/orderActivity/{orderActivityId}/tag/{orderActivityTag} | Add new tags for an orderActivity.
[**delete_order_activity**](OrderActivityApi.md#delete_order_activity) | **DELETE** /beta/orderActivity/{orderActivityId} | Delete an orderActivity
[**delete_order_activity_tag**](OrderActivityApi.md#delete_order_activity_tag) | **DELETE** /beta/orderActivity/{orderActivityId}/tag/{orderActivityTag} | Delete a tag for an orderActivity.
[**get_duplicate_order_activity_by_id**](OrderActivityApi.md#get_duplicate_order_activity_by_id) | **GET** /beta/orderActivity/duplicate/{orderActivityId} | Get a duplicated an orderActivity by id
[**get_order_activity_by_filter**](OrderActivityApi.md#get_order_activity_by_filter) | **GET** /beta/orderActivity/search | Search orderActivitys by filter
[**get_order_activity_by_id**](OrderActivityApi.md#get_order_activity_by_id) | **GET** /beta/orderActivity/{orderActivityId} | Get an orderActivity by id
[**get_order_activity_tags**](OrderActivityApi.md#get_order_activity_tags) | **GET** /beta/orderActivity/{orderActivityId}/tag | Get the tags for an orderActivity.
[**update_order_activity**](OrderActivityApi.md#update_order_activity) | **PUT** /beta/orderActivity | Update an orderActivity


# **add_order_activity**
> OrderActivity add_order_activity(body)

Create an orderActivity

Inserts a new orderActivity using the specified data.

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
api_instance = Infoplus.OrderActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.OrderActivity() # OrderActivity | OrderActivity to be inserted.

try:
    # Create an orderActivity
    api_response = api_instance.add_order_activity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderActivityApi->add_order_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderActivity**](OrderActivity.md)| OrderActivity to be inserted. | 

### Return type

[**OrderActivity**](OrderActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_activity_audit**
> add_order_activity_audit(order_activity_id, order_activity_audit)

Add new audit for an orderActivity

Adds an audit to an existing orderActivity.

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
api_instance = Infoplus.OrderActivityApi(Infoplus.ApiClient(configuration))
order_activity_id = 8.14 # float | Id of the orderActivity to add an audit to
order_activity_audit = 'order_activity_audit_example' # str | The audit to add

try:
    # Add new audit for an orderActivity
    api_instance.add_order_activity_audit(order_activity_id, order_activity_audit)
except ApiException as e:
    print("Exception when calling OrderActivityApi->add_order_activity_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_activity_id** | **float**| Id of the orderActivity to add an audit to | 
 **order_activity_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_activity_file**
> add_order_activity_file(order_activity_id, file_name)

Attach a file to an orderActivity

Adds a file to an existing orderActivity.

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
api_instance = Infoplus.OrderActivityApi(Infoplus.ApiClient(configuration))
order_activity_id = 8.14 # float | Id of the orderActivity to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an orderActivity
    api_instance.add_order_activity_file(order_activity_id, file_name)
except ApiException as e:
    print("Exception when calling OrderActivityApi->add_order_activity_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_activity_id** | **float**| Id of the orderActivity to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_activity_tag**
> add_order_activity_tag(order_activity_id, order_activity_tag)

Add new tags for an orderActivity.

Adds a tag to an existing orderActivity.

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
api_instance = Infoplus.OrderActivityApi(Infoplus.ApiClient(configuration))
order_activity_id = 8.14 # float | Id of the orderActivity to add a tag to
order_activity_tag = 'order_activity_tag_example' # str | The tag to add

try:
    # Add new tags for an orderActivity.
    api_instance.add_order_activity_tag(order_activity_id, order_activity_tag)
except ApiException as e:
    print("Exception when calling OrderActivityApi->add_order_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_activity_id** | **float**| Id of the orderActivity to add a tag to | 
 **order_activity_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_activity**
> delete_order_activity(order_activity_id)

Delete an orderActivity

Deletes the orderActivity identified by the specified id.

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
api_instance = Infoplus.OrderActivityApi(Infoplus.ApiClient(configuration))
order_activity_id = 8.14 # float | Id of the orderActivity to be deleted.

try:
    # Delete an orderActivity
    api_instance.delete_order_activity(order_activity_id)
except ApiException as e:
    print("Exception when calling OrderActivityApi->delete_order_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_activity_id** | **float**| Id of the orderActivity to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_activity_tag**
> delete_order_activity_tag(order_activity_id, order_activity_tag)

Delete a tag for an orderActivity.

Deletes an existing orderActivity tag using the specified data.

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
api_instance = Infoplus.OrderActivityApi(Infoplus.ApiClient(configuration))
order_activity_id = 8.14 # float | Id of the orderActivity to remove tag from
order_activity_tag = 'order_activity_tag_example' # str | The tag to delete

try:
    # Delete a tag for an orderActivity.
    api_instance.delete_order_activity_tag(order_activity_id, order_activity_tag)
except ApiException as e:
    print("Exception when calling OrderActivityApi->delete_order_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_activity_id** | **float**| Id of the orderActivity to remove tag from | 
 **order_activity_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_order_activity_by_id**
> OrderActivity get_duplicate_order_activity_by_id(order_activity_id)

Get a duplicated an orderActivity by id

Returns a duplicated orderActivity identified by the specified id.

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
api_instance = Infoplus.OrderActivityApi(Infoplus.ApiClient(configuration))
order_activity_id = 8.14 # float | Id of the orderActivity to be duplicated.

try:
    # Get a duplicated an orderActivity by id
    api_response = api_instance.get_duplicate_order_activity_by_id(order_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderActivityApi->get_duplicate_order_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_activity_id** | **float**| Id of the orderActivity to be duplicated. | 

### Return type

[**OrderActivity**](OrderActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_activity_by_filter**
> list[OrderActivity] get_order_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search orderActivitys by filter

Returns the list of orderActivitys that match the given filter.

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
api_instance = Infoplus.OrderActivityApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search orderActivitys by filter
    api_response = api_instance.get_order_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderActivityApi->get_order_activity_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[OrderActivity]**](OrderActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_activity_by_id**
> OrderActivity get_order_activity_by_id(order_activity_id)

Get an orderActivity by id

Returns the orderActivity identified by the specified id.

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
api_instance = Infoplus.OrderActivityApi(Infoplus.ApiClient(configuration))
order_activity_id = 8.14 # float | Id of the orderActivity to be returned.

try:
    # Get an orderActivity by id
    api_response = api_instance.get_order_activity_by_id(order_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderActivityApi->get_order_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_activity_id** | **float**| Id of the orderActivity to be returned. | 

### Return type

[**OrderActivity**](OrderActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_activity_tags**
> get_order_activity_tags(order_activity_id)

Get the tags for an orderActivity.

Get all existing orderActivity tags.

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
api_instance = Infoplus.OrderActivityApi(Infoplus.ApiClient(configuration))
order_activity_id = 8.14 # float | Id of the orderActivity to get tags for

try:
    # Get the tags for an orderActivity.
    api_instance.get_order_activity_tags(order_activity_id)
except ApiException as e:
    print("Exception when calling OrderActivityApi->get_order_activity_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_activity_id** | **float**| Id of the orderActivity to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_activity**
> update_order_activity(body)

Update an orderActivity

Updates an existing orderActivity using the specified data.

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
api_instance = Infoplus.OrderActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.OrderActivity() # OrderActivity | OrderActivity to be updated.

try:
    # Update an orderActivity
    api_instance.update_order_activity(body)
except ApiException as e:
    print("Exception when calling OrderActivityApi->update_order_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderActivity**](OrderActivity.md)| OrderActivity to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

