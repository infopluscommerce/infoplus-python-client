# Infoplus.CartLocationApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cart_location_audit**](CartLocationApi.md#add_cart_location_audit) | **PUT** /beta/cartLocation/{cartLocationId}/audit/{cartLocationAudit} | Add new audit for a cartLocation
[**add_cart_location_file**](CartLocationApi.md#add_cart_location_file) | **POST** /beta/cartLocation/{cartLocationId}/file/{fileName} | Attach a file to a cartLocation
[**add_cart_location_tag**](CartLocationApi.md#add_cart_location_tag) | **PUT** /beta/cartLocation/{cartLocationId}/tag/{cartLocationTag} | Add new tags for a cartLocation.
[**delete_cart_location_tag**](CartLocationApi.md#delete_cart_location_tag) | **DELETE** /beta/cartLocation/{cartLocationId}/tag/{cartLocationTag} | Delete a tag for a cartLocation.
[**get_cart_location_by_filter**](CartLocationApi.md#get_cart_location_by_filter) | **GET** /beta/cartLocation/search | Search cartLocations by filter
[**get_cart_location_by_id**](CartLocationApi.md#get_cart_location_by_id) | **GET** /beta/cartLocation/{cartLocationId} | Get a cartLocation by id
[**get_cart_location_tags**](CartLocationApi.md#get_cart_location_tags) | **GET** /beta/cartLocation/{cartLocationId}/tag | Get the tags for a cartLocation.
[**get_duplicate_cart_location_by_id**](CartLocationApi.md#get_duplicate_cart_location_by_id) | **GET** /beta/cartLocation/duplicate/{cartLocationId} | Get a duplicated a cartLocation by id


# **add_cart_location_audit**
> add_cart_location_audit(cart_location_id, cart_location_audit)

Add new audit for a cartLocation

Adds an audit to an existing cartLocation.

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
api_instance = Infoplus.CartLocationApi(Infoplus.ApiClient(configuration))
cart_location_id = 56 # int | Id of the cartLocation to add an audit to
cart_location_audit = 'cart_location_audit_example' # str | The audit to add

try:
    # Add new audit for a cartLocation
    api_instance.add_cart_location_audit(cart_location_id, cart_location_audit)
except ApiException as e:
    print("Exception when calling CartLocationApi->add_cart_location_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_location_id** | **int**| Id of the cartLocation to add an audit to | 
 **cart_location_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_cart_location_file**
> add_cart_location_file(cart_location_id, file_name)

Attach a file to a cartLocation

Adds a file to an existing cartLocation.

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
api_instance = Infoplus.CartLocationApi(Infoplus.ApiClient(configuration))
cart_location_id = 56 # int | Id of the cartLocation to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a cartLocation
    api_instance.add_cart_location_file(cart_location_id, file_name)
except ApiException as e:
    print("Exception when calling CartLocationApi->add_cart_location_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_location_id** | **int**| Id of the cartLocation to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_cart_location_tag**
> add_cart_location_tag(cart_location_id, cart_location_tag)

Add new tags for a cartLocation.

Adds a tag to an existing cartLocation.

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
api_instance = Infoplus.CartLocationApi(Infoplus.ApiClient(configuration))
cart_location_id = 56 # int | Id of the cartLocation to add a tag to
cart_location_tag = 'cart_location_tag_example' # str | The tag to add

try:
    # Add new tags for a cartLocation.
    api_instance.add_cart_location_tag(cart_location_id, cart_location_tag)
except ApiException as e:
    print("Exception when calling CartLocationApi->add_cart_location_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_location_id** | **int**| Id of the cartLocation to add a tag to | 
 **cart_location_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cart_location_tag**
> delete_cart_location_tag(cart_location_id, cart_location_tag)

Delete a tag for a cartLocation.

Deletes an existing cartLocation tag using the specified data.

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
api_instance = Infoplus.CartLocationApi(Infoplus.ApiClient(configuration))
cart_location_id = 56 # int | Id of the cartLocation to remove tag from
cart_location_tag = 'cart_location_tag_example' # str | The tag to delete

try:
    # Delete a tag for a cartLocation.
    api_instance.delete_cart_location_tag(cart_location_id, cart_location_tag)
except ApiException as e:
    print("Exception when calling CartLocationApi->delete_cart_location_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_location_id** | **int**| Id of the cartLocation to remove tag from | 
 **cart_location_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_location_by_filter**
> list[CartLocation] get_cart_location_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search cartLocations by filter

Returns the list of cartLocations that match the given filter.

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
api_instance = Infoplus.CartLocationApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search cartLocations by filter
    api_response = api_instance.get_cart_location_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartLocationApi->get_cart_location_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[CartLocation]**](CartLocation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_location_by_id**
> CartLocation get_cart_location_by_id(cart_location_id)

Get a cartLocation by id

Returns the cartLocation identified by the specified id.

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
api_instance = Infoplus.CartLocationApi(Infoplus.ApiClient(configuration))
cart_location_id = 56 # int | Id of the cartLocation to be returned.

try:
    # Get a cartLocation by id
    api_response = api_instance.get_cart_location_by_id(cart_location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartLocationApi->get_cart_location_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_location_id** | **int**| Id of the cartLocation to be returned. | 

### Return type

[**CartLocation**](CartLocation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_location_tags**
> get_cart_location_tags(cart_location_id)

Get the tags for a cartLocation.

Get all existing cartLocation tags.

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
api_instance = Infoplus.CartLocationApi(Infoplus.ApiClient(configuration))
cart_location_id = 56 # int | Id of the cartLocation to get tags for

try:
    # Get the tags for a cartLocation.
    api_instance.get_cart_location_tags(cart_location_id)
except ApiException as e:
    print("Exception when calling CartLocationApi->get_cart_location_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_location_id** | **int**| Id of the cartLocation to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_cart_location_by_id**
> CartLocation get_duplicate_cart_location_by_id(cart_location_id)

Get a duplicated a cartLocation by id

Returns a duplicated cartLocation identified by the specified id.

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
api_instance = Infoplus.CartLocationApi(Infoplus.ApiClient(configuration))
cart_location_id = 56 # int | Id of the cartLocation to be duplicated.

try:
    # Get a duplicated a cartLocation by id
    api_response = api_instance.get_duplicate_cart_location_by_id(cart_location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartLocationApi->get_duplicate_cart_location_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_location_id** | **int**| Id of the cartLocation to be duplicated. | 

### Return type

[**CartLocation**](CartLocation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

