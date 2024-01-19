# Infoplus.LocationBillingTypeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_location_billing_type**](LocationBillingTypeApi.md#add_location_billing_type) | **POST** /beta/locationBillingType | Create a locationBillingType
[**add_location_billing_type_audit**](LocationBillingTypeApi.md#add_location_billing_type_audit) | **PUT** /beta/locationBillingType/{locationBillingTypeId}/audit/{locationBillingTypeAudit} | Add new audit for a locationBillingType
[**add_location_billing_type_file**](LocationBillingTypeApi.md#add_location_billing_type_file) | **POST** /beta/locationBillingType/{locationBillingTypeId}/file/{fileName} | Attach a file to a locationBillingType
[**add_location_billing_type_file_by_url**](LocationBillingTypeApi.md#add_location_billing_type_file_by_url) | **POST** /beta/locationBillingType/{locationBillingTypeId}/file | Attach a file to a locationBillingType by URL.
[**add_location_billing_type_tag**](LocationBillingTypeApi.md#add_location_billing_type_tag) | **PUT** /beta/locationBillingType/{locationBillingTypeId}/tag/{locationBillingTypeTag} | Add new tags for a locationBillingType.
[**delete_location_billing_type**](LocationBillingTypeApi.md#delete_location_billing_type) | **DELETE** /beta/locationBillingType/{locationBillingTypeId} | Delete a locationBillingType
[**delete_location_billing_type_file**](LocationBillingTypeApi.md#delete_location_billing_type_file) | **DELETE** /beta/locationBillingType/{locationBillingTypeId}/file/{fileId} | Delete a file for a locationBillingType.
[**delete_location_billing_type_tag**](LocationBillingTypeApi.md#delete_location_billing_type_tag) | **DELETE** /beta/locationBillingType/{locationBillingTypeId}/tag/{locationBillingTypeTag} | Delete a tag for a locationBillingType.
[**get_duplicate_location_billing_type_by_id**](LocationBillingTypeApi.md#get_duplicate_location_billing_type_by_id) | **GET** /beta/locationBillingType/duplicate/{locationBillingTypeId} | Get a duplicated a locationBillingType by id
[**get_location_billing_type_by_filter**](LocationBillingTypeApi.md#get_location_billing_type_by_filter) | **GET** /beta/locationBillingType/search | Search locationBillingTypes by filter
[**get_location_billing_type_by_id**](LocationBillingTypeApi.md#get_location_billing_type_by_id) | **GET** /beta/locationBillingType/{locationBillingTypeId} | Get a locationBillingType by id
[**get_location_billing_type_files**](LocationBillingTypeApi.md#get_location_billing_type_files) | **GET** /beta/locationBillingType/{locationBillingTypeId}/file | Get the files for a locationBillingType.
[**get_location_billing_type_tags**](LocationBillingTypeApi.md#get_location_billing_type_tags) | **GET** /beta/locationBillingType/{locationBillingTypeId}/tag | Get the tags for a locationBillingType.
[**update_location_billing_type**](LocationBillingTypeApi.md#update_location_billing_type) | **PUT** /beta/locationBillingType | Update a locationBillingType
[**update_location_billing_type_custom_fields**](LocationBillingTypeApi.md#update_location_billing_type_custom_fields) | **PUT** /beta/locationBillingType/customFields | Update a locationBillingType custom fields


# **add_location_billing_type**
> LocationBillingType add_location_billing_type(body)

Create a locationBillingType

Inserts a new locationBillingType using the specified data.

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
api_instance = Infoplus.LocationBillingTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.LocationBillingType() # LocationBillingType | LocationBillingType to be inserted.

try:
    # Create a locationBillingType
    api_response = api_instance.add_location_billing_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationBillingTypeApi->add_location_billing_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationBillingType**](LocationBillingType.md)| LocationBillingType to be inserted. | 

### Return type

[**LocationBillingType**](LocationBillingType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_location_billing_type_audit**
> add_location_billing_type_audit(location_billing_type_id, location_billing_type_audit)

Add new audit for a locationBillingType

Adds an audit to an existing locationBillingType.

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
api_instance = Infoplus.LocationBillingTypeApi(Infoplus.ApiClient(configuration))
location_billing_type_id = 56 # int | Id of the locationBillingType to add an audit to
location_billing_type_audit = 'location_billing_type_audit_example' # str | The audit to add

try:
    # Add new audit for a locationBillingType
    api_instance.add_location_billing_type_audit(location_billing_type_id, location_billing_type_audit)
except ApiException as e:
    print("Exception when calling LocationBillingTypeApi->add_location_billing_type_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_billing_type_id** | **int**| Id of the locationBillingType to add an audit to | 
 **location_billing_type_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_location_billing_type_file**
> add_location_billing_type_file(location_billing_type_id, file_name)

Attach a file to a locationBillingType

Adds a file to an existing locationBillingType.

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
api_instance = Infoplus.LocationBillingTypeApi(Infoplus.ApiClient(configuration))
location_billing_type_id = 56 # int | Id of the locationBillingType to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a locationBillingType
    api_instance.add_location_billing_type_file(location_billing_type_id, file_name)
except ApiException as e:
    print("Exception when calling LocationBillingTypeApi->add_location_billing_type_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_billing_type_id** | **int**| Id of the locationBillingType to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_location_billing_type_file_by_url**
> add_location_billing_type_file_by_url(body, location_billing_type_id)

Attach a file to a locationBillingType by URL.

Adds a file to an existing locationBillingType by URL.

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
api_instance = Infoplus.LocationBillingTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
location_billing_type_id = 56 # int | Id of the locationBillingType to add an file to

try:
    # Attach a file to a locationBillingType by URL.
    api_instance.add_location_billing_type_file_by_url(body, location_billing_type_id)
except ApiException as e:
    print("Exception when calling LocationBillingTypeApi->add_location_billing_type_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **location_billing_type_id** | **int**| Id of the locationBillingType to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_location_billing_type_tag**
> add_location_billing_type_tag(location_billing_type_id, location_billing_type_tag)

Add new tags for a locationBillingType.

Adds a tag to an existing locationBillingType.

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
api_instance = Infoplus.LocationBillingTypeApi(Infoplus.ApiClient(configuration))
location_billing_type_id = 56 # int | Id of the locationBillingType to add a tag to
location_billing_type_tag = 'location_billing_type_tag_example' # str | The tag to add

try:
    # Add new tags for a locationBillingType.
    api_instance.add_location_billing_type_tag(location_billing_type_id, location_billing_type_tag)
except ApiException as e:
    print("Exception when calling LocationBillingTypeApi->add_location_billing_type_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_billing_type_id** | **int**| Id of the locationBillingType to add a tag to | 
 **location_billing_type_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_location_billing_type**
> delete_location_billing_type(location_billing_type_id)

Delete a locationBillingType

Deletes the locationBillingType identified by the specified id.

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
api_instance = Infoplus.LocationBillingTypeApi(Infoplus.ApiClient(configuration))
location_billing_type_id = 56 # int | Id of the locationBillingType to be deleted.

try:
    # Delete a locationBillingType
    api_instance.delete_location_billing_type(location_billing_type_id)
except ApiException as e:
    print("Exception when calling LocationBillingTypeApi->delete_location_billing_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_billing_type_id** | **int**| Id of the locationBillingType to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_location_billing_type_file**
> delete_location_billing_type_file(location_billing_type_id, file_id)

Delete a file for a locationBillingType.

Deletes an existing locationBillingType file using the specified data.

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
api_instance = Infoplus.LocationBillingTypeApi(Infoplus.ApiClient(configuration))
location_billing_type_id = 56 # int | Id of the locationBillingType to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a locationBillingType.
    api_instance.delete_location_billing_type_file(location_billing_type_id, file_id)
except ApiException as e:
    print("Exception when calling LocationBillingTypeApi->delete_location_billing_type_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_billing_type_id** | **int**| Id of the locationBillingType to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_location_billing_type_tag**
> delete_location_billing_type_tag(location_billing_type_id, location_billing_type_tag)

Delete a tag for a locationBillingType.

Deletes an existing locationBillingType tag using the specified data.

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
api_instance = Infoplus.LocationBillingTypeApi(Infoplus.ApiClient(configuration))
location_billing_type_id = 56 # int | Id of the locationBillingType to remove tag from
location_billing_type_tag = 'location_billing_type_tag_example' # str | The tag to delete

try:
    # Delete a tag for a locationBillingType.
    api_instance.delete_location_billing_type_tag(location_billing_type_id, location_billing_type_tag)
except ApiException as e:
    print("Exception when calling LocationBillingTypeApi->delete_location_billing_type_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_billing_type_id** | **int**| Id of the locationBillingType to remove tag from | 
 **location_billing_type_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_location_billing_type_by_id**
> LocationBillingType get_duplicate_location_billing_type_by_id(location_billing_type_id)

Get a duplicated a locationBillingType by id

Returns a duplicated locationBillingType identified by the specified id.

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
api_instance = Infoplus.LocationBillingTypeApi(Infoplus.ApiClient(configuration))
location_billing_type_id = 56 # int | Id of the locationBillingType to be duplicated.

try:
    # Get a duplicated a locationBillingType by id
    api_response = api_instance.get_duplicate_location_billing_type_by_id(location_billing_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationBillingTypeApi->get_duplicate_location_billing_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_billing_type_id** | **int**| Id of the locationBillingType to be duplicated. | 

### Return type

[**LocationBillingType**](LocationBillingType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_billing_type_by_filter**
> list[LocationBillingType] get_location_billing_type_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search locationBillingTypes by filter

Returns the list of locationBillingTypes that match the given filter.

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
api_instance = Infoplus.LocationBillingTypeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search locationBillingTypes by filter
    api_response = api_instance.get_location_billing_type_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationBillingTypeApi->get_location_billing_type_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[LocationBillingType]**](LocationBillingType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_billing_type_by_id**
> LocationBillingType get_location_billing_type_by_id(location_billing_type_id)

Get a locationBillingType by id

Returns the locationBillingType identified by the specified id.

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
api_instance = Infoplus.LocationBillingTypeApi(Infoplus.ApiClient(configuration))
location_billing_type_id = 56 # int | Id of the locationBillingType to be returned.

try:
    # Get a locationBillingType by id
    api_response = api_instance.get_location_billing_type_by_id(location_billing_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationBillingTypeApi->get_location_billing_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_billing_type_id** | **int**| Id of the locationBillingType to be returned. | 

### Return type

[**LocationBillingType**](LocationBillingType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_billing_type_files**
> get_location_billing_type_files(location_billing_type_id)

Get the files for a locationBillingType.

Get all existing locationBillingType files.

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
api_instance = Infoplus.LocationBillingTypeApi(Infoplus.ApiClient(configuration))
location_billing_type_id = 56 # int | Id of the locationBillingType to get files for

try:
    # Get the files for a locationBillingType.
    api_instance.get_location_billing_type_files(location_billing_type_id)
except ApiException as e:
    print("Exception when calling LocationBillingTypeApi->get_location_billing_type_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_billing_type_id** | **int**| Id of the locationBillingType to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_billing_type_tags**
> get_location_billing_type_tags(location_billing_type_id)

Get the tags for a locationBillingType.

Get all existing locationBillingType tags.

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
api_instance = Infoplus.LocationBillingTypeApi(Infoplus.ApiClient(configuration))
location_billing_type_id = 56 # int | Id of the locationBillingType to get tags for

try:
    # Get the tags for a locationBillingType.
    api_instance.get_location_billing_type_tags(location_billing_type_id)
except ApiException as e:
    print("Exception when calling LocationBillingTypeApi->get_location_billing_type_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_billing_type_id** | **int**| Id of the locationBillingType to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_location_billing_type**
> update_location_billing_type(body)

Update a locationBillingType

Updates an existing locationBillingType using the specified data.

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
api_instance = Infoplus.LocationBillingTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.LocationBillingType() # LocationBillingType | LocationBillingType to be updated.

try:
    # Update a locationBillingType
    api_instance.update_location_billing_type(body)
except ApiException as e:
    print("Exception when calling LocationBillingTypeApi->update_location_billing_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationBillingType**](LocationBillingType.md)| LocationBillingType to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_location_billing_type_custom_fields**
> update_location_billing_type_custom_fields(body)

Update a locationBillingType custom fields

Updates an existing locationBillingType custom fields using the specified data.

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
api_instance = Infoplus.LocationBillingTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.LocationBillingType() # LocationBillingType | LocationBillingType to be updated.

try:
    # Update a locationBillingType custom fields
    api_instance.update_location_billing_type_custom_fields(body)
except ApiException as e:
    print("Exception when calling LocationBillingTypeApi->update_location_billing_type_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationBillingType**](LocationBillingType.md)| LocationBillingType to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

