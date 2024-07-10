# Infoplus.ZoneApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_zone**](ZoneApi.md#add_zone) | **POST** /beta/zone | Create a zone
[**add_zone_audit**](ZoneApi.md#add_zone_audit) | **PUT** /beta/zone/{zoneId}/audit/{zoneAudit} | Add new audit for a zone
[**add_zone_file**](ZoneApi.md#add_zone_file) | **POST** /beta/zone/{zoneId}/file/{fileName} | Attach a file to a zone
[**add_zone_file_by_url**](ZoneApi.md#add_zone_file_by_url) | **POST** /beta/zone/{zoneId}/file | Attach a file to a zone by URL.
[**add_zone_tag**](ZoneApi.md#add_zone_tag) | **PUT** /beta/zone/{zoneId}/tag/{zoneTag} | Add new tags for a zone.
[**delete_zone**](ZoneApi.md#delete_zone) | **DELETE** /beta/zone/{zoneId} | Delete a zone
[**delete_zone_file**](ZoneApi.md#delete_zone_file) | **DELETE** /beta/zone/{zoneId}/file/{fileId} | Delete a file for a zone.
[**delete_zone_tag**](ZoneApi.md#delete_zone_tag) | **DELETE** /beta/zone/{zoneId}/tag/{zoneTag} | Delete a tag for a zone.
[**get_duplicate_zone_by_id**](ZoneApi.md#get_duplicate_zone_by_id) | **GET** /beta/zone/duplicate/{zoneId} | Get a duplicated a zone by id
[**get_zone_by_filter**](ZoneApi.md#get_zone_by_filter) | **GET** /beta/zone/search | Search zones by filter
[**get_zone_by_id**](ZoneApi.md#get_zone_by_id) | **GET** /beta/zone/{zoneId} | Get a zone by id
[**get_zone_files**](ZoneApi.md#get_zone_files) | **GET** /beta/zone/{zoneId}/file | Get the files for a zone.
[**get_zone_tags**](ZoneApi.md#get_zone_tags) | **GET** /beta/zone/{zoneId}/tag | Get the tags for a zone.
[**update_zone**](ZoneApi.md#update_zone) | **PUT** /beta/zone | Update a zone
[**update_zone_custom_fields**](ZoneApi.md#update_zone_custom_fields) | **PUT** /beta/zone/customFields | Update a zone custom fields


# **add_zone**
> Zone add_zone(body)

Create a zone

Inserts a new zone using the specified data.

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
api_instance = Infoplus.ZoneApi(Infoplus.ApiClient(configuration))
body = Infoplus.Zone() # Zone | Zone to be inserted.

try:
    # Create a zone
    api_response = api_instance.add_zone(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneApi->add_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Zone**](Zone.md)| Zone to be inserted. | 

### Return type

[**Zone**](Zone.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_zone_audit**
> add_zone_audit(zone_id, zone_audit)

Add new audit for a zone

Adds an audit to an existing zone.

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
api_instance = Infoplus.ZoneApi(Infoplus.ApiClient(configuration))
zone_id = 56 # int | Id of the zone to add an audit to
zone_audit = 'zone_audit_example' # str | The audit to add

try:
    # Add new audit for a zone
    api_instance.add_zone_audit(zone_id, zone_audit)
except ApiException as e:
    print("Exception when calling ZoneApi->add_zone_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| Id of the zone to add an audit to | 
 **zone_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_zone_file**
> add_zone_file(zone_id, file_name)

Attach a file to a zone

Adds a file to an existing zone.

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
api_instance = Infoplus.ZoneApi(Infoplus.ApiClient(configuration))
zone_id = 56 # int | Id of the zone to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a zone
    api_instance.add_zone_file(zone_id, file_name)
except ApiException as e:
    print("Exception when calling ZoneApi->add_zone_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| Id of the zone to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_zone_file_by_url**
> add_zone_file_by_url(body, zone_id)

Attach a file to a zone by URL.

Adds a file to an existing zone by URL.

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
api_instance = Infoplus.ZoneApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
zone_id = 56 # int | Id of the zone to add an file to

try:
    # Attach a file to a zone by URL.
    api_instance.add_zone_file_by_url(body, zone_id)
except ApiException as e:
    print("Exception when calling ZoneApi->add_zone_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **zone_id** | **int**| Id of the zone to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_zone_tag**
> add_zone_tag(zone_id, zone_tag)

Add new tags for a zone.

Adds a tag to an existing zone.

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
api_instance = Infoplus.ZoneApi(Infoplus.ApiClient(configuration))
zone_id = 56 # int | Id of the zone to add a tag to
zone_tag = 'zone_tag_example' # str | The tag to add

try:
    # Add new tags for a zone.
    api_instance.add_zone_tag(zone_id, zone_tag)
except ApiException as e:
    print("Exception when calling ZoneApi->add_zone_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| Id of the zone to add a tag to | 
 **zone_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zone**
> delete_zone(zone_id)

Delete a zone

Deletes the zone identified by the specified id.

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
api_instance = Infoplus.ZoneApi(Infoplus.ApiClient(configuration))
zone_id = 56 # int | Id of the zone to be deleted.

try:
    # Delete a zone
    api_instance.delete_zone(zone_id)
except ApiException as e:
    print("Exception when calling ZoneApi->delete_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| Id of the zone to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zone_file**
> delete_zone_file(zone_id, file_id)

Delete a file for a zone.

Deletes an existing zone file using the specified data.

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
api_instance = Infoplus.ZoneApi(Infoplus.ApiClient(configuration))
zone_id = 56 # int | Id of the zone to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a zone.
    api_instance.delete_zone_file(zone_id, file_id)
except ApiException as e:
    print("Exception when calling ZoneApi->delete_zone_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| Id of the zone to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zone_tag**
> delete_zone_tag(zone_id, zone_tag)

Delete a tag for a zone.

Deletes an existing zone tag using the specified data.

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
api_instance = Infoplus.ZoneApi(Infoplus.ApiClient(configuration))
zone_id = 56 # int | Id of the zone to remove tag from
zone_tag = 'zone_tag_example' # str | The tag to delete

try:
    # Delete a tag for a zone.
    api_instance.delete_zone_tag(zone_id, zone_tag)
except ApiException as e:
    print("Exception when calling ZoneApi->delete_zone_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| Id of the zone to remove tag from | 
 **zone_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_zone_by_id**
> Zone get_duplicate_zone_by_id(zone_id)

Get a duplicated a zone by id

Returns a duplicated zone identified by the specified id.

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
api_instance = Infoplus.ZoneApi(Infoplus.ApiClient(configuration))
zone_id = 56 # int | Id of the zone to be duplicated.

try:
    # Get a duplicated a zone by id
    api_response = api_instance.get_duplicate_zone_by_id(zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneApi->get_duplicate_zone_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| Id of the zone to be duplicated. | 

### Return type

[**Zone**](Zone.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_by_filter**
> list[Zone] get_zone_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search zones by filter

Returns the list of zones that match the given filter.

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
api_instance = Infoplus.ZoneApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search zones by filter
    api_response = api_instance.get_zone_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneApi->get_zone_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Zone]**](Zone.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_by_id**
> Zone get_zone_by_id(zone_id)

Get a zone by id

Returns the zone identified by the specified id.

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
api_instance = Infoplus.ZoneApi(Infoplus.ApiClient(configuration))
zone_id = 56 # int | Id of the zone to be returned.

try:
    # Get a zone by id
    api_response = api_instance.get_zone_by_id(zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneApi->get_zone_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| Id of the zone to be returned. | 

### Return type

[**Zone**](Zone.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_files**
> get_zone_files(zone_id)

Get the files for a zone.

Get all existing zone files.

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
api_instance = Infoplus.ZoneApi(Infoplus.ApiClient(configuration))
zone_id = 56 # int | Id of the zone to get files for

try:
    # Get the files for a zone.
    api_instance.get_zone_files(zone_id)
except ApiException as e:
    print("Exception when calling ZoneApi->get_zone_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| Id of the zone to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_tags**
> get_zone_tags(zone_id)

Get the tags for a zone.

Get all existing zone tags.

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
api_instance = Infoplus.ZoneApi(Infoplus.ApiClient(configuration))
zone_id = 56 # int | Id of the zone to get tags for

try:
    # Get the tags for a zone.
    api_instance.get_zone_tags(zone_id)
except ApiException as e:
    print("Exception when calling ZoneApi->get_zone_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| Id of the zone to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_zone**
> update_zone(body)

Update a zone

Updates an existing zone using the specified data.

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
api_instance = Infoplus.ZoneApi(Infoplus.ApiClient(configuration))
body = Infoplus.Zone() # Zone | Zone to be updated.

try:
    # Update a zone
    api_instance.update_zone(body)
except ApiException as e:
    print("Exception when calling ZoneApi->update_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Zone**](Zone.md)| Zone to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_zone_custom_fields**
> update_zone_custom_fields(body)

Update a zone custom fields

Updates an existing zone custom fields using the specified data.

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
api_instance = Infoplus.ZoneApi(Infoplus.ApiClient(configuration))
body = Infoplus.Zone() # Zone | Zone to be updated.

try:
    # Update a zone custom fields
    api_instance.update_zone_custom_fields(body)
except ApiException as e:
    print("Exception when calling ZoneApi->update_zone_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Zone**](Zone.md)| Zone to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

