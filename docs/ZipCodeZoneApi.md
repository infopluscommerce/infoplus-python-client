# Infoplus.ZipCodeZoneApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_zip_code_zone**](ZipCodeZoneApi.md#add_zip_code_zone) | **POST** /beta/zipCodeZone | Create a zipCodeZone
[**add_zip_code_zone_audit**](ZipCodeZoneApi.md#add_zip_code_zone_audit) | **PUT** /beta/zipCodeZone/{zipCodeZoneId}/audit/{zipCodeZoneAudit} | Add new audit for a zipCodeZone
[**add_zip_code_zone_file**](ZipCodeZoneApi.md#add_zip_code_zone_file) | **POST** /beta/zipCodeZone/{zipCodeZoneId}/file/{fileName} | Attach a file to a zipCodeZone
[**add_zip_code_zone_file_by_url**](ZipCodeZoneApi.md#add_zip_code_zone_file_by_url) | **POST** /beta/zipCodeZone/{zipCodeZoneId}/file | Attach a file to a zipCodeZone by URL.
[**add_zip_code_zone_tag**](ZipCodeZoneApi.md#add_zip_code_zone_tag) | **PUT** /beta/zipCodeZone/{zipCodeZoneId}/tag/{zipCodeZoneTag} | Add new tags for a zipCodeZone.
[**delete_zip_code_zone**](ZipCodeZoneApi.md#delete_zip_code_zone) | **DELETE** /beta/zipCodeZone/{zipCodeZoneId} | Delete a zipCodeZone
[**delete_zip_code_zone_file**](ZipCodeZoneApi.md#delete_zip_code_zone_file) | **DELETE** /beta/zipCodeZone/{zipCodeZoneId}/file/{fileId} | Delete a file for a zipCodeZone.
[**delete_zip_code_zone_tag**](ZipCodeZoneApi.md#delete_zip_code_zone_tag) | **DELETE** /beta/zipCodeZone/{zipCodeZoneId}/tag/{zipCodeZoneTag} | Delete a tag for a zipCodeZone.
[**get_duplicate_zip_code_zone_by_id**](ZipCodeZoneApi.md#get_duplicate_zip_code_zone_by_id) | **GET** /beta/zipCodeZone/duplicate/{zipCodeZoneId} | Get a duplicated a zipCodeZone by id
[**get_zip_code_zone_by_filter**](ZipCodeZoneApi.md#get_zip_code_zone_by_filter) | **GET** /beta/zipCodeZone/search | Search zipCodeZones by filter
[**get_zip_code_zone_by_id**](ZipCodeZoneApi.md#get_zip_code_zone_by_id) | **GET** /beta/zipCodeZone/{zipCodeZoneId} | Get a zipCodeZone by id
[**get_zip_code_zone_files**](ZipCodeZoneApi.md#get_zip_code_zone_files) | **GET** /beta/zipCodeZone/{zipCodeZoneId}/file | Get the files for a zipCodeZone.
[**get_zip_code_zone_tags**](ZipCodeZoneApi.md#get_zip_code_zone_tags) | **GET** /beta/zipCodeZone/{zipCodeZoneId}/tag | Get the tags for a zipCodeZone.
[**update_zip_code_zone**](ZipCodeZoneApi.md#update_zip_code_zone) | **PUT** /beta/zipCodeZone | Update a zipCodeZone


# **add_zip_code_zone**
> ZipCodeZone add_zip_code_zone(body)

Create a zipCodeZone

Inserts a new zipCodeZone using the specified data.

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
api_instance = Infoplus.ZipCodeZoneApi(Infoplus.ApiClient(configuration))
body = Infoplus.ZipCodeZone() # ZipCodeZone | ZipCodeZone to be inserted.

try:
    # Create a zipCodeZone
    api_response = api_instance.add_zip_code_zone(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZipCodeZoneApi->add_zip_code_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ZipCodeZone**](ZipCodeZone.md)| ZipCodeZone to be inserted. | 

### Return type

[**ZipCodeZone**](ZipCodeZone.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_zip_code_zone_audit**
> add_zip_code_zone_audit(zip_code_zone_id, zip_code_zone_audit)

Add new audit for a zipCodeZone

Adds an audit to an existing zipCodeZone.

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
api_instance = Infoplus.ZipCodeZoneApi(Infoplus.ApiClient(configuration))
zip_code_zone_id = 56 # int | Id of the zipCodeZone to add an audit to
zip_code_zone_audit = 'zip_code_zone_audit_example' # str | The audit to add

try:
    # Add new audit for a zipCodeZone
    api_instance.add_zip_code_zone_audit(zip_code_zone_id, zip_code_zone_audit)
except ApiException as e:
    print("Exception when calling ZipCodeZoneApi->add_zip_code_zone_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip_code_zone_id** | **int**| Id of the zipCodeZone to add an audit to | 
 **zip_code_zone_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_zip_code_zone_file**
> add_zip_code_zone_file(zip_code_zone_id, file_name)

Attach a file to a zipCodeZone

Adds a file to an existing zipCodeZone.

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
api_instance = Infoplus.ZipCodeZoneApi(Infoplus.ApiClient(configuration))
zip_code_zone_id = 56 # int | Id of the zipCodeZone to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a zipCodeZone
    api_instance.add_zip_code_zone_file(zip_code_zone_id, file_name)
except ApiException as e:
    print("Exception when calling ZipCodeZoneApi->add_zip_code_zone_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip_code_zone_id** | **int**| Id of the zipCodeZone to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_zip_code_zone_file_by_url**
> add_zip_code_zone_file_by_url(body, zip_code_zone_id)

Attach a file to a zipCodeZone by URL.

Adds a file to an existing zipCodeZone by URL.

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
api_instance = Infoplus.ZipCodeZoneApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
zip_code_zone_id = 56 # int | Id of the zipCodeZone to add an file to

try:
    # Attach a file to a zipCodeZone by URL.
    api_instance.add_zip_code_zone_file_by_url(body, zip_code_zone_id)
except ApiException as e:
    print("Exception when calling ZipCodeZoneApi->add_zip_code_zone_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **zip_code_zone_id** | **int**| Id of the zipCodeZone to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_zip_code_zone_tag**
> add_zip_code_zone_tag(zip_code_zone_id, zip_code_zone_tag)

Add new tags for a zipCodeZone.

Adds a tag to an existing zipCodeZone.

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
api_instance = Infoplus.ZipCodeZoneApi(Infoplus.ApiClient(configuration))
zip_code_zone_id = 56 # int | Id of the zipCodeZone to add a tag to
zip_code_zone_tag = 'zip_code_zone_tag_example' # str | The tag to add

try:
    # Add new tags for a zipCodeZone.
    api_instance.add_zip_code_zone_tag(zip_code_zone_id, zip_code_zone_tag)
except ApiException as e:
    print("Exception when calling ZipCodeZoneApi->add_zip_code_zone_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip_code_zone_id** | **int**| Id of the zipCodeZone to add a tag to | 
 **zip_code_zone_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zip_code_zone**
> delete_zip_code_zone(zip_code_zone_id)

Delete a zipCodeZone

Deletes the zipCodeZone identified by the specified id.

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
api_instance = Infoplus.ZipCodeZoneApi(Infoplus.ApiClient(configuration))
zip_code_zone_id = 56 # int | Id of the zipCodeZone to be deleted.

try:
    # Delete a zipCodeZone
    api_instance.delete_zip_code_zone(zip_code_zone_id)
except ApiException as e:
    print("Exception when calling ZipCodeZoneApi->delete_zip_code_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip_code_zone_id** | **int**| Id of the zipCodeZone to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zip_code_zone_file**
> delete_zip_code_zone_file(zip_code_zone_id, file_id)

Delete a file for a zipCodeZone.

Deletes an existing zipCodeZone file using the specified data.

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
api_instance = Infoplus.ZipCodeZoneApi(Infoplus.ApiClient(configuration))
zip_code_zone_id = 56 # int | Id of the zipCodeZone to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a zipCodeZone.
    api_instance.delete_zip_code_zone_file(zip_code_zone_id, file_id)
except ApiException as e:
    print("Exception when calling ZipCodeZoneApi->delete_zip_code_zone_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip_code_zone_id** | **int**| Id of the zipCodeZone to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zip_code_zone_tag**
> delete_zip_code_zone_tag(zip_code_zone_id, zip_code_zone_tag)

Delete a tag for a zipCodeZone.

Deletes an existing zipCodeZone tag using the specified data.

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
api_instance = Infoplus.ZipCodeZoneApi(Infoplus.ApiClient(configuration))
zip_code_zone_id = 56 # int | Id of the zipCodeZone to remove tag from
zip_code_zone_tag = 'zip_code_zone_tag_example' # str | The tag to delete

try:
    # Delete a tag for a zipCodeZone.
    api_instance.delete_zip_code_zone_tag(zip_code_zone_id, zip_code_zone_tag)
except ApiException as e:
    print("Exception when calling ZipCodeZoneApi->delete_zip_code_zone_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip_code_zone_id** | **int**| Id of the zipCodeZone to remove tag from | 
 **zip_code_zone_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_zip_code_zone_by_id**
> ZipCodeZone get_duplicate_zip_code_zone_by_id(zip_code_zone_id)

Get a duplicated a zipCodeZone by id

Returns a duplicated zipCodeZone identified by the specified id.

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
api_instance = Infoplus.ZipCodeZoneApi(Infoplus.ApiClient(configuration))
zip_code_zone_id = 56 # int | Id of the zipCodeZone to be duplicated.

try:
    # Get a duplicated a zipCodeZone by id
    api_response = api_instance.get_duplicate_zip_code_zone_by_id(zip_code_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZipCodeZoneApi->get_duplicate_zip_code_zone_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip_code_zone_id** | **int**| Id of the zipCodeZone to be duplicated. | 

### Return type

[**ZipCodeZone**](ZipCodeZone.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zip_code_zone_by_filter**
> list[ZipCodeZone] get_zip_code_zone_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search zipCodeZones by filter

Returns the list of zipCodeZones that match the given filter.

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
api_instance = Infoplus.ZipCodeZoneApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search zipCodeZones by filter
    api_response = api_instance.get_zip_code_zone_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZipCodeZoneApi->get_zip_code_zone_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ZipCodeZone]**](ZipCodeZone.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zip_code_zone_by_id**
> ZipCodeZone get_zip_code_zone_by_id(zip_code_zone_id)

Get a zipCodeZone by id

Returns the zipCodeZone identified by the specified id.

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
api_instance = Infoplus.ZipCodeZoneApi(Infoplus.ApiClient(configuration))
zip_code_zone_id = 56 # int | Id of the zipCodeZone to be returned.

try:
    # Get a zipCodeZone by id
    api_response = api_instance.get_zip_code_zone_by_id(zip_code_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZipCodeZoneApi->get_zip_code_zone_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip_code_zone_id** | **int**| Id of the zipCodeZone to be returned. | 

### Return type

[**ZipCodeZone**](ZipCodeZone.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zip_code_zone_files**
> get_zip_code_zone_files(zip_code_zone_id)

Get the files for a zipCodeZone.

Get all existing zipCodeZone files.

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
api_instance = Infoplus.ZipCodeZoneApi(Infoplus.ApiClient(configuration))
zip_code_zone_id = 56 # int | Id of the zipCodeZone to get files for

try:
    # Get the files for a zipCodeZone.
    api_instance.get_zip_code_zone_files(zip_code_zone_id)
except ApiException as e:
    print("Exception when calling ZipCodeZoneApi->get_zip_code_zone_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip_code_zone_id** | **int**| Id of the zipCodeZone to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zip_code_zone_tags**
> get_zip_code_zone_tags(zip_code_zone_id)

Get the tags for a zipCodeZone.

Get all existing zipCodeZone tags.

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
api_instance = Infoplus.ZipCodeZoneApi(Infoplus.ApiClient(configuration))
zip_code_zone_id = 56 # int | Id of the zipCodeZone to get tags for

try:
    # Get the tags for a zipCodeZone.
    api_instance.get_zip_code_zone_tags(zip_code_zone_id)
except ApiException as e:
    print("Exception when calling ZipCodeZoneApi->get_zip_code_zone_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip_code_zone_id** | **int**| Id of the zipCodeZone to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_zip_code_zone**
> update_zip_code_zone(body)

Update a zipCodeZone

Updates an existing zipCodeZone using the specified data.

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
api_instance = Infoplus.ZipCodeZoneApi(Infoplus.ApiClient(configuration))
body = Infoplus.ZipCodeZone() # ZipCodeZone | ZipCodeZone to be updated.

try:
    # Update a zipCodeZone
    api_instance.update_zip_code_zone(body)
except ApiException as e:
    print("Exception when calling ZipCodeZoneApi->update_zip_code_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ZipCodeZone**](ZipCodeZone.md)| ZipCodeZone to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

