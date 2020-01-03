# Infoplus.LocationAddressSchemeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_location_address_scheme**](LocationAddressSchemeApi.md#add_location_address_scheme) | **POST** /beta/locationAddressScheme | Create a locationAddressScheme
[**add_location_address_scheme_audit**](LocationAddressSchemeApi.md#add_location_address_scheme_audit) | **PUT** /beta/locationAddressScheme/{locationAddressSchemeId}/audit/{locationAddressSchemeAudit} | Add new audit for a locationAddressScheme
[**add_location_address_scheme_file**](LocationAddressSchemeApi.md#add_location_address_scheme_file) | **POST** /beta/locationAddressScheme/{locationAddressSchemeId}/file/{fileName} | Attach a file to a locationAddressScheme
[**add_location_address_scheme_tag**](LocationAddressSchemeApi.md#add_location_address_scheme_tag) | **PUT** /beta/locationAddressScheme/{locationAddressSchemeId}/tag/{locationAddressSchemeTag} | Add new tags for a locationAddressScheme.
[**delete_location_address_scheme**](LocationAddressSchemeApi.md#delete_location_address_scheme) | **DELETE** /beta/locationAddressScheme/{locationAddressSchemeId} | Delete a locationAddressScheme
[**delete_location_address_scheme_tag**](LocationAddressSchemeApi.md#delete_location_address_scheme_tag) | **DELETE** /beta/locationAddressScheme/{locationAddressSchemeId}/tag/{locationAddressSchemeTag} | Delete a tag for a locationAddressScheme.
[**get_duplicate_location_address_scheme_by_id**](LocationAddressSchemeApi.md#get_duplicate_location_address_scheme_by_id) | **GET** /beta/locationAddressScheme/duplicate/{locationAddressSchemeId} | Get a duplicated a locationAddressScheme by id
[**get_location_address_scheme_by_filter**](LocationAddressSchemeApi.md#get_location_address_scheme_by_filter) | **GET** /beta/locationAddressScheme/search | Search locationAddressSchemes by filter
[**get_location_address_scheme_by_id**](LocationAddressSchemeApi.md#get_location_address_scheme_by_id) | **GET** /beta/locationAddressScheme/{locationAddressSchemeId} | Get a locationAddressScheme by id
[**get_location_address_scheme_tags**](LocationAddressSchemeApi.md#get_location_address_scheme_tags) | **GET** /beta/locationAddressScheme/{locationAddressSchemeId}/tag | Get the tags for a locationAddressScheme.
[**update_location_address_scheme**](LocationAddressSchemeApi.md#update_location_address_scheme) | **PUT** /beta/locationAddressScheme | Update a locationAddressScheme
[**update_location_address_scheme_custom_fields**](LocationAddressSchemeApi.md#update_location_address_scheme_custom_fields) | **PUT** /beta/locationAddressScheme/customFields | Update a locationAddressScheme custom fields


# **add_location_address_scheme**
> LocationAddressScheme add_location_address_scheme(body)

Create a locationAddressScheme

Inserts a new locationAddressScheme using the specified data.

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
api_instance = Infoplus.LocationAddressSchemeApi(Infoplus.ApiClient(configuration))
body = Infoplus.LocationAddressScheme() # LocationAddressScheme | LocationAddressScheme to be inserted.

try:
    # Create a locationAddressScheme
    api_response = api_instance.add_location_address_scheme(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationAddressSchemeApi->add_location_address_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationAddressScheme**](LocationAddressScheme.md)| LocationAddressScheme to be inserted. | 

### Return type

[**LocationAddressScheme**](LocationAddressScheme.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_location_address_scheme_audit**
> add_location_address_scheme_audit(location_address_scheme_id, location_address_scheme_audit)

Add new audit for a locationAddressScheme

Adds an audit to an existing locationAddressScheme.

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
api_instance = Infoplus.LocationAddressSchemeApi(Infoplus.ApiClient(configuration))
location_address_scheme_id = 56 # int | Id of the locationAddressScheme to add an audit to
location_address_scheme_audit = 'location_address_scheme_audit_example' # str | The audit to add

try:
    # Add new audit for a locationAddressScheme
    api_instance.add_location_address_scheme_audit(location_address_scheme_id, location_address_scheme_audit)
except ApiException as e:
    print("Exception when calling LocationAddressSchemeApi->add_location_address_scheme_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_address_scheme_id** | **int**| Id of the locationAddressScheme to add an audit to | 
 **location_address_scheme_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_location_address_scheme_file**
> add_location_address_scheme_file(location_address_scheme_id, file_name)

Attach a file to a locationAddressScheme

Adds a file to an existing locationAddressScheme.

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
api_instance = Infoplus.LocationAddressSchemeApi(Infoplus.ApiClient(configuration))
location_address_scheme_id = 56 # int | Id of the locationAddressScheme to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a locationAddressScheme
    api_instance.add_location_address_scheme_file(location_address_scheme_id, file_name)
except ApiException as e:
    print("Exception when calling LocationAddressSchemeApi->add_location_address_scheme_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_address_scheme_id** | **int**| Id of the locationAddressScheme to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_location_address_scheme_tag**
> add_location_address_scheme_tag(location_address_scheme_id, location_address_scheme_tag)

Add new tags for a locationAddressScheme.

Adds a tag to an existing locationAddressScheme.

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
api_instance = Infoplus.LocationAddressSchemeApi(Infoplus.ApiClient(configuration))
location_address_scheme_id = 56 # int | Id of the locationAddressScheme to add a tag to
location_address_scheme_tag = 'location_address_scheme_tag_example' # str | The tag to add

try:
    # Add new tags for a locationAddressScheme.
    api_instance.add_location_address_scheme_tag(location_address_scheme_id, location_address_scheme_tag)
except ApiException as e:
    print("Exception when calling LocationAddressSchemeApi->add_location_address_scheme_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_address_scheme_id** | **int**| Id of the locationAddressScheme to add a tag to | 
 **location_address_scheme_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_location_address_scheme**
> delete_location_address_scheme(location_address_scheme_id)

Delete a locationAddressScheme

Deletes the locationAddressScheme identified by the specified id.

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
api_instance = Infoplus.LocationAddressSchemeApi(Infoplus.ApiClient(configuration))
location_address_scheme_id = 56 # int | Id of the locationAddressScheme to be deleted.

try:
    # Delete a locationAddressScheme
    api_instance.delete_location_address_scheme(location_address_scheme_id)
except ApiException as e:
    print("Exception when calling LocationAddressSchemeApi->delete_location_address_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_address_scheme_id** | **int**| Id of the locationAddressScheme to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_location_address_scheme_tag**
> delete_location_address_scheme_tag(location_address_scheme_id, location_address_scheme_tag)

Delete a tag for a locationAddressScheme.

Deletes an existing locationAddressScheme tag using the specified data.

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
api_instance = Infoplus.LocationAddressSchemeApi(Infoplus.ApiClient(configuration))
location_address_scheme_id = 56 # int | Id of the locationAddressScheme to remove tag from
location_address_scheme_tag = 'location_address_scheme_tag_example' # str | The tag to delete

try:
    # Delete a tag for a locationAddressScheme.
    api_instance.delete_location_address_scheme_tag(location_address_scheme_id, location_address_scheme_tag)
except ApiException as e:
    print("Exception when calling LocationAddressSchemeApi->delete_location_address_scheme_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_address_scheme_id** | **int**| Id of the locationAddressScheme to remove tag from | 
 **location_address_scheme_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_location_address_scheme_by_id**
> LocationAddressScheme get_duplicate_location_address_scheme_by_id(location_address_scheme_id)

Get a duplicated a locationAddressScheme by id

Returns a duplicated locationAddressScheme identified by the specified id.

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
api_instance = Infoplus.LocationAddressSchemeApi(Infoplus.ApiClient(configuration))
location_address_scheme_id = 56 # int | Id of the locationAddressScheme to be duplicated.

try:
    # Get a duplicated a locationAddressScheme by id
    api_response = api_instance.get_duplicate_location_address_scheme_by_id(location_address_scheme_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationAddressSchemeApi->get_duplicate_location_address_scheme_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_address_scheme_id** | **int**| Id of the locationAddressScheme to be duplicated. | 

### Return type

[**LocationAddressScheme**](LocationAddressScheme.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_address_scheme_by_filter**
> list[LocationAddressScheme] get_location_address_scheme_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search locationAddressSchemes by filter

Returns the list of locationAddressSchemes that match the given filter.

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
api_instance = Infoplus.LocationAddressSchemeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search locationAddressSchemes by filter
    api_response = api_instance.get_location_address_scheme_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationAddressSchemeApi->get_location_address_scheme_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[LocationAddressScheme]**](LocationAddressScheme.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_address_scheme_by_id**
> LocationAddressScheme get_location_address_scheme_by_id(location_address_scheme_id)

Get a locationAddressScheme by id

Returns the locationAddressScheme identified by the specified id.

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
api_instance = Infoplus.LocationAddressSchemeApi(Infoplus.ApiClient(configuration))
location_address_scheme_id = 56 # int | Id of the locationAddressScheme to be returned.

try:
    # Get a locationAddressScheme by id
    api_response = api_instance.get_location_address_scheme_by_id(location_address_scheme_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationAddressSchemeApi->get_location_address_scheme_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_address_scheme_id** | **int**| Id of the locationAddressScheme to be returned. | 

### Return type

[**LocationAddressScheme**](LocationAddressScheme.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_address_scheme_tags**
> get_location_address_scheme_tags(location_address_scheme_id)

Get the tags for a locationAddressScheme.

Get all existing locationAddressScheme tags.

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
api_instance = Infoplus.LocationAddressSchemeApi(Infoplus.ApiClient(configuration))
location_address_scheme_id = 56 # int | Id of the locationAddressScheme to get tags for

try:
    # Get the tags for a locationAddressScheme.
    api_instance.get_location_address_scheme_tags(location_address_scheme_id)
except ApiException as e:
    print("Exception when calling LocationAddressSchemeApi->get_location_address_scheme_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_address_scheme_id** | **int**| Id of the locationAddressScheme to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_location_address_scheme**
> update_location_address_scheme(body)

Update a locationAddressScheme

Updates an existing locationAddressScheme using the specified data.

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
api_instance = Infoplus.LocationAddressSchemeApi(Infoplus.ApiClient(configuration))
body = Infoplus.LocationAddressScheme() # LocationAddressScheme | LocationAddressScheme to be updated.

try:
    # Update a locationAddressScheme
    api_instance.update_location_address_scheme(body)
except ApiException as e:
    print("Exception when calling LocationAddressSchemeApi->update_location_address_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationAddressScheme**](LocationAddressScheme.md)| LocationAddressScheme to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_location_address_scheme_custom_fields**
> update_location_address_scheme_custom_fields(body)

Update a locationAddressScheme custom fields

Updates an existing locationAddressScheme custom fields using the specified data.

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
api_instance = Infoplus.LocationAddressSchemeApi(Infoplus.ApiClient(configuration))
body = Infoplus.LocationAddressScheme() # LocationAddressScheme | LocationAddressScheme to be updated.

try:
    # Update a locationAddressScheme custom fields
    api_instance.update_location_address_scheme_custom_fields(body)
except ApiException as e:
    print("Exception when calling LocationAddressSchemeApi->update_location_address_scheme_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationAddressScheme**](LocationAddressScheme.md)| LocationAddressScheme to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

