# Infoplus.CartonActivityApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_carton_activity**](CartonActivityApi.md#add_carton_activity) | **POST** /beta/cartonActivity | Create a cartonActivity
[**add_carton_activity_audit**](CartonActivityApi.md#add_carton_activity_audit) | **PUT** /beta/cartonActivity/{cartonActivityId}/audit/{cartonActivityAudit} | Add new audit for a cartonActivity
[**add_carton_activity_file**](CartonActivityApi.md#add_carton_activity_file) | **POST** /beta/cartonActivity/{cartonActivityId}/file/{fileName} | Attach a file to a cartonActivity
[**add_carton_activity_tag**](CartonActivityApi.md#add_carton_activity_tag) | **PUT** /beta/cartonActivity/{cartonActivityId}/tag/{cartonActivityTag} | Add new tags for a cartonActivity.
[**delete_carton_activity**](CartonActivityApi.md#delete_carton_activity) | **DELETE** /beta/cartonActivity/{cartonActivityId} | Delete a cartonActivity
[**delete_carton_activity_tag**](CartonActivityApi.md#delete_carton_activity_tag) | **DELETE** /beta/cartonActivity/{cartonActivityId}/tag/{cartonActivityTag} | Delete a tag for a cartonActivity.
[**get_carton_activity_by_filter**](CartonActivityApi.md#get_carton_activity_by_filter) | **GET** /beta/cartonActivity/search | Search cartonActivitys by filter
[**get_carton_activity_by_id**](CartonActivityApi.md#get_carton_activity_by_id) | **GET** /beta/cartonActivity/{cartonActivityId} | Get a cartonActivity by id
[**get_carton_activity_tags**](CartonActivityApi.md#get_carton_activity_tags) | **GET** /beta/cartonActivity/{cartonActivityId}/tag | Get the tags for a cartonActivity.
[**get_duplicate_carton_activity_by_id**](CartonActivityApi.md#get_duplicate_carton_activity_by_id) | **GET** /beta/cartonActivity/duplicate/{cartonActivityId} | Get a duplicated a cartonActivity by id
[**update_carton_activity**](CartonActivityApi.md#update_carton_activity) | **PUT** /beta/cartonActivity | Update a cartonActivity


# **add_carton_activity**
> CartonActivity add_carton_activity(body)

Create a cartonActivity

Inserts a new cartonActivity using the specified data.

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
api_instance = Infoplus.CartonActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.CartonActivity() # CartonActivity | CartonActivity to be inserted.

try:
    # Create a cartonActivity
    api_response = api_instance.add_carton_activity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonActivityApi->add_carton_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartonActivity**](CartonActivity.md)| CartonActivity to be inserted. | 

### Return type

[**CartonActivity**](CartonActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_carton_activity_audit**
> add_carton_activity_audit(carton_activity_id, carton_activity_audit)

Add new audit for a cartonActivity

Adds an audit to an existing cartonActivity.

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
api_instance = Infoplus.CartonActivityApi(Infoplus.ApiClient(configuration))
carton_activity_id = 56 # int | Id of the cartonActivity to add an audit to
carton_activity_audit = 'carton_activity_audit_example' # str | The audit to add

try:
    # Add new audit for a cartonActivity
    api_instance.add_carton_activity_audit(carton_activity_id, carton_activity_audit)
except ApiException as e:
    print("Exception when calling CartonActivityApi->add_carton_activity_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_activity_id** | **int**| Id of the cartonActivity to add an audit to | 
 **carton_activity_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_carton_activity_file**
> add_carton_activity_file(carton_activity_id, file_name)

Attach a file to a cartonActivity

Adds a file to an existing cartonActivity.

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
api_instance = Infoplus.CartonActivityApi(Infoplus.ApiClient(configuration))
carton_activity_id = 56 # int | Id of the cartonActivity to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a cartonActivity
    api_instance.add_carton_activity_file(carton_activity_id, file_name)
except ApiException as e:
    print("Exception when calling CartonActivityApi->add_carton_activity_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_activity_id** | **int**| Id of the cartonActivity to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_carton_activity_tag**
> add_carton_activity_tag(carton_activity_id, carton_activity_tag)

Add new tags for a cartonActivity.

Adds a tag to an existing cartonActivity.

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
api_instance = Infoplus.CartonActivityApi(Infoplus.ApiClient(configuration))
carton_activity_id = 56 # int | Id of the cartonActivity to add a tag to
carton_activity_tag = 'carton_activity_tag_example' # str | The tag to add

try:
    # Add new tags for a cartonActivity.
    api_instance.add_carton_activity_tag(carton_activity_id, carton_activity_tag)
except ApiException as e:
    print("Exception when calling CartonActivityApi->add_carton_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_activity_id** | **int**| Id of the cartonActivity to add a tag to | 
 **carton_activity_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_carton_activity**
> delete_carton_activity(carton_activity_id)

Delete a cartonActivity

Deletes the cartonActivity identified by the specified id.

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
api_instance = Infoplus.CartonActivityApi(Infoplus.ApiClient(configuration))
carton_activity_id = 56 # int | Id of the cartonActivity to be deleted.

try:
    # Delete a cartonActivity
    api_instance.delete_carton_activity(carton_activity_id)
except ApiException as e:
    print("Exception when calling CartonActivityApi->delete_carton_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_activity_id** | **int**| Id of the cartonActivity to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_carton_activity_tag**
> delete_carton_activity_tag(carton_activity_id, carton_activity_tag)

Delete a tag for a cartonActivity.

Deletes an existing cartonActivity tag using the specified data.

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
api_instance = Infoplus.CartonActivityApi(Infoplus.ApiClient(configuration))
carton_activity_id = 56 # int | Id of the cartonActivity to remove tag from
carton_activity_tag = 'carton_activity_tag_example' # str | The tag to delete

try:
    # Delete a tag for a cartonActivity.
    api_instance.delete_carton_activity_tag(carton_activity_id, carton_activity_tag)
except ApiException as e:
    print("Exception when calling CartonActivityApi->delete_carton_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_activity_id** | **int**| Id of the cartonActivity to remove tag from | 
 **carton_activity_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carton_activity_by_filter**
> list[CartonActivity] get_carton_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search cartonActivitys by filter

Returns the list of cartonActivitys that match the given filter.

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
api_instance = Infoplus.CartonActivityApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search cartonActivitys by filter
    api_response = api_instance.get_carton_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonActivityApi->get_carton_activity_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[CartonActivity]**](CartonActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carton_activity_by_id**
> CartonActivity get_carton_activity_by_id(carton_activity_id)

Get a cartonActivity by id

Returns the cartonActivity identified by the specified id.

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
api_instance = Infoplus.CartonActivityApi(Infoplus.ApiClient(configuration))
carton_activity_id = 56 # int | Id of the cartonActivity to be returned.

try:
    # Get a cartonActivity by id
    api_response = api_instance.get_carton_activity_by_id(carton_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonActivityApi->get_carton_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_activity_id** | **int**| Id of the cartonActivity to be returned. | 

### Return type

[**CartonActivity**](CartonActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carton_activity_tags**
> get_carton_activity_tags(carton_activity_id)

Get the tags for a cartonActivity.

Get all existing cartonActivity tags.

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
api_instance = Infoplus.CartonActivityApi(Infoplus.ApiClient(configuration))
carton_activity_id = 56 # int | Id of the cartonActivity to get tags for

try:
    # Get the tags for a cartonActivity.
    api_instance.get_carton_activity_tags(carton_activity_id)
except ApiException as e:
    print("Exception when calling CartonActivityApi->get_carton_activity_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_activity_id** | **int**| Id of the cartonActivity to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_carton_activity_by_id**
> CartonActivity get_duplicate_carton_activity_by_id(carton_activity_id)

Get a duplicated a cartonActivity by id

Returns a duplicated cartonActivity identified by the specified id.

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
api_instance = Infoplus.CartonActivityApi(Infoplus.ApiClient(configuration))
carton_activity_id = 56 # int | Id of the cartonActivity to be duplicated.

try:
    # Get a duplicated a cartonActivity by id
    api_response = api_instance.get_duplicate_carton_activity_by_id(carton_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonActivityApi->get_duplicate_carton_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_activity_id** | **int**| Id of the cartonActivity to be duplicated. | 

### Return type

[**CartonActivity**](CartonActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_carton_activity**
> update_carton_activity(body)

Update a cartonActivity

Updates an existing cartonActivity using the specified data.

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
api_instance = Infoplus.CartonActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.CartonActivity() # CartonActivity | CartonActivity to be updated.

try:
    # Update a cartonActivity
    api_instance.update_carton_activity(body)
except ApiException as e:
    print("Exception when calling CartonActivityApi->update_carton_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartonActivity**](CartonActivity.md)| CartonActivity to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

