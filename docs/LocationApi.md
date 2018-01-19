# Infoplus.LocationApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_location**](LocationApi.md#add_location) | **POST** /beta/location | Create a location
[**add_location_audit**](LocationApi.md#add_location_audit) | **PUT** /beta/location/{locationId}/audit/{locationAudit} | Add new audit for a location
[**add_location_tag**](LocationApi.md#add_location_tag) | **PUT** /beta/location/{locationId}/tag/{locationTag} | Add new tags for a location.
[**delete_location**](LocationApi.md#delete_location) | **DELETE** /beta/location/{locationId} | Delete a location
[**delete_location_tag**](LocationApi.md#delete_location_tag) | **DELETE** /beta/location/{locationId}/tag/{locationTag} | Delete a tag for a location.
[**get_duplicate_location_by_id**](LocationApi.md#get_duplicate_location_by_id) | **GET** /beta/location/duplicate/{locationId} | Get a duplicated a location by id
[**get_location_by_filter**](LocationApi.md#get_location_by_filter) | **GET** /beta/location/search | Search locations by filter
[**get_location_by_id**](LocationApi.md#get_location_by_id) | **GET** /beta/location/{locationId} | Get a location by id
[**get_location_tags**](LocationApi.md#get_location_tags) | **GET** /beta/location/{locationId}/tag | Get the tags for a location.
[**update_location**](LocationApi.md#update_location) | **PUT** /beta/location | Update a location
[**update_location_custom_fields**](LocationApi.md#update_location_custom_fields) | **PUT** /beta/location/customFields | Update a location custom fields


# **add_location**
> Location add_location(body)

Create a location

Inserts a new location using the specified data.

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
api_instance = Infoplus.LocationApi(Infoplus.ApiClient(configuration))
body = Infoplus.Location() # Location | Location to be inserted.

try:
    # Create a location
    api_response = api_instance.add_location(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->add_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Location**](Location.md)| Location to be inserted. | 

### Return type

[**Location**](Location.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_location_audit**
> add_location_audit(location_id, location_audit)

Add new audit for a location

Adds an audit to an existing location.

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
api_instance = Infoplus.LocationApi(Infoplus.ApiClient(configuration))
location_id = 56 # int | Id of the location to add an audit to
location_audit = 'location_audit_example' # str | The audit to add

try:
    # Add new audit for a location
    api_instance.add_location_audit(location_id, location_audit)
except ApiException as e:
    print("Exception when calling LocationApi->add_location_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| Id of the location to add an audit to | 
 **location_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_location_tag**
> add_location_tag(location_id, location_tag)

Add new tags for a location.

Adds a tag to an existing location.

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
api_instance = Infoplus.LocationApi(Infoplus.ApiClient(configuration))
location_id = 56 # int | Id of the location to add a tag to
location_tag = 'location_tag_example' # str | The tag to add

try:
    # Add new tags for a location.
    api_instance.add_location_tag(location_id, location_tag)
except ApiException as e:
    print("Exception when calling LocationApi->add_location_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| Id of the location to add a tag to | 
 **location_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_location**
> delete_location(location_id)

Delete a location

Deletes the location identified by the specified id.

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
api_instance = Infoplus.LocationApi(Infoplus.ApiClient(configuration))
location_id = 56 # int | Id of the location to be deleted.

try:
    # Delete a location
    api_instance.delete_location(location_id)
except ApiException as e:
    print("Exception when calling LocationApi->delete_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| Id of the location to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_location_tag**
> delete_location_tag(location_id, location_tag)

Delete a tag for a location.

Deletes an existing location tag using the specified data.

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
api_instance = Infoplus.LocationApi(Infoplus.ApiClient(configuration))
location_id = 56 # int | Id of the location to remove tag from
location_tag = 'location_tag_example' # str | The tag to delete

try:
    # Delete a tag for a location.
    api_instance.delete_location_tag(location_id, location_tag)
except ApiException as e:
    print("Exception when calling LocationApi->delete_location_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| Id of the location to remove tag from | 
 **location_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_location_by_id**
> Location get_duplicate_location_by_id(location_id)

Get a duplicated a location by id

Returns a duplicated location identified by the specified id.

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
api_instance = Infoplus.LocationApi(Infoplus.ApiClient(configuration))
location_id = 56 # int | Id of the location to be duplicated.

try:
    # Get a duplicated a location by id
    api_response = api_instance.get_duplicate_location_by_id(location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->get_duplicate_location_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| Id of the location to be duplicated. | 

### Return type

[**Location**](Location.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_by_filter**
> list[Location] get_location_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search locations by filter

Returns the list of locations that match the given filter.

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
api_instance = Infoplus.LocationApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search locations by filter
    api_response = api_instance.get_location_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->get_location_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Location]**](Location.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_by_id**
> Location get_location_by_id(location_id)

Get a location by id

Returns the location identified by the specified id.

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
api_instance = Infoplus.LocationApi(Infoplus.ApiClient(configuration))
location_id = 56 # int | Id of the location to be returned.

try:
    # Get a location by id
    api_response = api_instance.get_location_by_id(location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->get_location_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| Id of the location to be returned. | 

### Return type

[**Location**](Location.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_tags**
> get_location_tags(location_id)

Get the tags for a location.

Get all existing location tags.

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
api_instance = Infoplus.LocationApi(Infoplus.ApiClient(configuration))
location_id = 56 # int | Id of the location to get tags for

try:
    # Get the tags for a location.
    api_instance.get_location_tags(location_id)
except ApiException as e:
    print("Exception when calling LocationApi->get_location_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| Id of the location to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_location**
> update_location(body)

Update a location

Updates an existing location using the specified data.

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
api_instance = Infoplus.LocationApi(Infoplus.ApiClient(configuration))
body = Infoplus.Location() # Location | Location to be updated.

try:
    # Update a location
    api_instance.update_location(body)
except ApiException as e:
    print("Exception when calling LocationApi->update_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Location**](Location.md)| Location to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_location_custom_fields**
> update_location_custom_fields(body)

Update a location custom fields

Updates an existing location custom fields using the specified data.

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
api_instance = Infoplus.LocationApi(Infoplus.ApiClient(configuration))
body = Infoplus.Location() # Location | Location to be updated.

try:
    # Update a location custom fields
    api_instance.update_location_custom_fields(body)
except ApiException as e:
    print("Exception when calling LocationApi->update_location_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Location**](Location.md)| Location to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

