# Infoplus.LocationFootprintApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_location_footprint**](LocationFootprintApi.md#add_location_footprint) | **POST** /beta/locationFootprint | Create a locationFootprint
[**add_location_footprint_audit**](LocationFootprintApi.md#add_location_footprint_audit) | **PUT** /beta/locationFootprint/{locationFootprintId}/audit/{locationFootprintAudit} | Add new audit for a locationFootprint
[**add_location_footprint_file**](LocationFootprintApi.md#add_location_footprint_file) | **POST** /beta/locationFootprint/{locationFootprintId}/file/{fileName} | Attach a file to a locationFootprint
[**add_location_footprint_tag**](LocationFootprintApi.md#add_location_footprint_tag) | **PUT** /beta/locationFootprint/{locationFootprintId}/tag/{locationFootprintTag} | Add new tags for a locationFootprint.
[**delete_location_footprint**](LocationFootprintApi.md#delete_location_footprint) | **DELETE** /beta/locationFootprint/{locationFootprintId} | Delete a locationFootprint
[**delete_location_footprint_tag**](LocationFootprintApi.md#delete_location_footprint_tag) | **DELETE** /beta/locationFootprint/{locationFootprintId}/tag/{locationFootprintTag} | Delete a tag for a locationFootprint.
[**get_duplicate_location_footprint_by_id**](LocationFootprintApi.md#get_duplicate_location_footprint_by_id) | **GET** /beta/locationFootprint/duplicate/{locationFootprintId} | Get a duplicated a locationFootprint by id
[**get_location_footprint_by_filter**](LocationFootprintApi.md#get_location_footprint_by_filter) | **GET** /beta/locationFootprint/search | Search locationFootprints by filter
[**get_location_footprint_by_id**](LocationFootprintApi.md#get_location_footprint_by_id) | **GET** /beta/locationFootprint/{locationFootprintId} | Get a locationFootprint by id
[**get_location_footprint_tags**](LocationFootprintApi.md#get_location_footprint_tags) | **GET** /beta/locationFootprint/{locationFootprintId}/tag | Get the tags for a locationFootprint.
[**update_location_footprint**](LocationFootprintApi.md#update_location_footprint) | **PUT** /beta/locationFootprint | Update a locationFootprint
[**update_location_footprint_custom_fields**](LocationFootprintApi.md#update_location_footprint_custom_fields) | **PUT** /beta/locationFootprint/customFields | Update a locationFootprint custom fields


# **add_location_footprint**
> LocationFootprint add_location_footprint(body)

Create a locationFootprint

Inserts a new locationFootprint using the specified data.

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
api_instance = Infoplus.LocationFootprintApi(Infoplus.ApiClient(configuration))
body = Infoplus.LocationFootprint() # LocationFootprint | LocationFootprint to be inserted.

try:
    # Create a locationFootprint
    api_response = api_instance.add_location_footprint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationFootprintApi->add_location_footprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationFootprint**](LocationFootprint.md)| LocationFootprint to be inserted. | 

### Return type

[**LocationFootprint**](LocationFootprint.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_location_footprint_audit**
> add_location_footprint_audit(location_footprint_id, location_footprint_audit)

Add new audit for a locationFootprint

Adds an audit to an existing locationFootprint.

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
api_instance = Infoplus.LocationFootprintApi(Infoplus.ApiClient(configuration))
location_footprint_id = 56 # int | Id of the locationFootprint to add an audit to
location_footprint_audit = 'location_footprint_audit_example' # str | The audit to add

try:
    # Add new audit for a locationFootprint
    api_instance.add_location_footprint_audit(location_footprint_id, location_footprint_audit)
except ApiException as e:
    print("Exception when calling LocationFootprintApi->add_location_footprint_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_footprint_id** | **int**| Id of the locationFootprint to add an audit to | 
 **location_footprint_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_location_footprint_file**
> add_location_footprint_file(location_footprint_id, file_name)

Attach a file to a locationFootprint

Adds a file to an existing locationFootprint.

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
api_instance = Infoplus.LocationFootprintApi(Infoplus.ApiClient(configuration))
location_footprint_id = 56 # int | Id of the locationFootprint to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a locationFootprint
    api_instance.add_location_footprint_file(location_footprint_id, file_name)
except ApiException as e:
    print("Exception when calling LocationFootprintApi->add_location_footprint_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_footprint_id** | **int**| Id of the locationFootprint to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_location_footprint_tag**
> add_location_footprint_tag(location_footprint_id, location_footprint_tag)

Add new tags for a locationFootprint.

Adds a tag to an existing locationFootprint.

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
api_instance = Infoplus.LocationFootprintApi(Infoplus.ApiClient(configuration))
location_footprint_id = 56 # int | Id of the locationFootprint to add a tag to
location_footprint_tag = 'location_footprint_tag_example' # str | The tag to add

try:
    # Add new tags for a locationFootprint.
    api_instance.add_location_footprint_tag(location_footprint_id, location_footprint_tag)
except ApiException as e:
    print("Exception when calling LocationFootprintApi->add_location_footprint_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_footprint_id** | **int**| Id of the locationFootprint to add a tag to | 
 **location_footprint_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_location_footprint**
> delete_location_footprint(location_footprint_id)

Delete a locationFootprint

Deletes the locationFootprint identified by the specified id.

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
api_instance = Infoplus.LocationFootprintApi(Infoplus.ApiClient(configuration))
location_footprint_id = 56 # int | Id of the locationFootprint to be deleted.

try:
    # Delete a locationFootprint
    api_instance.delete_location_footprint(location_footprint_id)
except ApiException as e:
    print("Exception when calling LocationFootprintApi->delete_location_footprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_footprint_id** | **int**| Id of the locationFootprint to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_location_footprint_tag**
> delete_location_footprint_tag(location_footprint_id, location_footprint_tag)

Delete a tag for a locationFootprint.

Deletes an existing locationFootprint tag using the specified data.

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
api_instance = Infoplus.LocationFootprintApi(Infoplus.ApiClient(configuration))
location_footprint_id = 56 # int | Id of the locationFootprint to remove tag from
location_footprint_tag = 'location_footprint_tag_example' # str | The tag to delete

try:
    # Delete a tag for a locationFootprint.
    api_instance.delete_location_footprint_tag(location_footprint_id, location_footprint_tag)
except ApiException as e:
    print("Exception when calling LocationFootprintApi->delete_location_footprint_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_footprint_id** | **int**| Id of the locationFootprint to remove tag from | 
 **location_footprint_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_location_footprint_by_id**
> LocationFootprint get_duplicate_location_footprint_by_id(location_footprint_id)

Get a duplicated a locationFootprint by id

Returns a duplicated locationFootprint identified by the specified id.

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
api_instance = Infoplus.LocationFootprintApi(Infoplus.ApiClient(configuration))
location_footprint_id = 56 # int | Id of the locationFootprint to be duplicated.

try:
    # Get a duplicated a locationFootprint by id
    api_response = api_instance.get_duplicate_location_footprint_by_id(location_footprint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationFootprintApi->get_duplicate_location_footprint_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_footprint_id** | **int**| Id of the locationFootprint to be duplicated. | 

### Return type

[**LocationFootprint**](LocationFootprint.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_footprint_by_filter**
> list[LocationFootprint] get_location_footprint_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search locationFootprints by filter

Returns the list of locationFootprints that match the given filter.

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
api_instance = Infoplus.LocationFootprintApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search locationFootprints by filter
    api_response = api_instance.get_location_footprint_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationFootprintApi->get_location_footprint_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[LocationFootprint]**](LocationFootprint.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_footprint_by_id**
> LocationFootprint get_location_footprint_by_id(location_footprint_id)

Get a locationFootprint by id

Returns the locationFootprint identified by the specified id.

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
api_instance = Infoplus.LocationFootprintApi(Infoplus.ApiClient(configuration))
location_footprint_id = 56 # int | Id of the locationFootprint to be returned.

try:
    # Get a locationFootprint by id
    api_response = api_instance.get_location_footprint_by_id(location_footprint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationFootprintApi->get_location_footprint_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_footprint_id** | **int**| Id of the locationFootprint to be returned. | 

### Return type

[**LocationFootprint**](LocationFootprint.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_footprint_tags**
> get_location_footprint_tags(location_footprint_id)

Get the tags for a locationFootprint.

Get all existing locationFootprint tags.

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
api_instance = Infoplus.LocationFootprintApi(Infoplus.ApiClient(configuration))
location_footprint_id = 56 # int | Id of the locationFootprint to get tags for

try:
    # Get the tags for a locationFootprint.
    api_instance.get_location_footprint_tags(location_footprint_id)
except ApiException as e:
    print("Exception when calling LocationFootprintApi->get_location_footprint_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_footprint_id** | **int**| Id of the locationFootprint to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_location_footprint**
> update_location_footprint(body)

Update a locationFootprint

Updates an existing locationFootprint using the specified data.

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
api_instance = Infoplus.LocationFootprintApi(Infoplus.ApiClient(configuration))
body = Infoplus.LocationFootprint() # LocationFootprint | LocationFootprint to be updated.

try:
    # Update a locationFootprint
    api_instance.update_location_footprint(body)
except ApiException as e:
    print("Exception when calling LocationFootprintApi->update_location_footprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationFootprint**](LocationFootprint.md)| LocationFootprint to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_location_footprint_custom_fields**
> update_location_footprint_custom_fields(body)

Update a locationFootprint custom fields

Updates an existing locationFootprint custom fields using the specified data.

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
api_instance = Infoplus.LocationFootprintApi(Infoplus.ApiClient(configuration))
body = Infoplus.LocationFootprint() # LocationFootprint | LocationFootprint to be updated.

try:
    # Update a locationFootprint custom fields
    api_instance.update_location_footprint_custom_fields(body)
except ApiException as e:
    print("Exception when calling LocationFootprintApi->update_location_footprint_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationFootprint**](LocationFootprint.md)| LocationFootprint to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

