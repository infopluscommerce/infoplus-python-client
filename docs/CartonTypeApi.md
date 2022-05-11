# Infoplus.CartonTypeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_carton_type**](CartonTypeApi.md#add_carton_type) | **POST** /v3.0/cartonType | Create a cartonType
[**add_carton_type_audit**](CartonTypeApi.md#add_carton_type_audit) | **PUT** /v3.0/cartonType/{cartonTypeId}/audit/{cartonTypeAudit} | Add new audit for a cartonType
[**add_carton_type_file**](CartonTypeApi.md#add_carton_type_file) | **POST** /v3.0/cartonType/{cartonTypeId}/file/{fileName} | Attach a file to a cartonType
[**add_carton_type_file_by_url**](CartonTypeApi.md#add_carton_type_file_by_url) | **POST** /v3.0/cartonType/{cartonTypeId}/file | Attach a file to a cartonType by URL.
[**add_carton_type_tag**](CartonTypeApi.md#add_carton_type_tag) | **PUT** /v3.0/cartonType/{cartonTypeId}/tag/{cartonTypeTag} | Add new tags for a cartonType.
[**delete_carton_type**](CartonTypeApi.md#delete_carton_type) | **DELETE** /v3.0/cartonType/{cartonTypeId} | Delete a cartonType
[**delete_carton_type_file**](CartonTypeApi.md#delete_carton_type_file) | **DELETE** /v3.0/cartonType/{cartonTypeId}/file/{fileId} | Delete a file for a cartonType.
[**delete_carton_type_tag**](CartonTypeApi.md#delete_carton_type_tag) | **DELETE** /v3.0/cartonType/{cartonTypeId}/tag/{cartonTypeTag} | Delete a tag for a cartonType.
[**get_carton_type_by_filter**](CartonTypeApi.md#get_carton_type_by_filter) | **GET** /v3.0/cartonType/search | Search cartonTypes by filter
[**get_carton_type_by_id**](CartonTypeApi.md#get_carton_type_by_id) | **GET** /v3.0/cartonType/{cartonTypeId} | Get a cartonType by id
[**get_carton_type_files**](CartonTypeApi.md#get_carton_type_files) | **GET** /v3.0/cartonType/{cartonTypeId}/file | Get the files for a cartonType.
[**get_carton_type_tags**](CartonTypeApi.md#get_carton_type_tags) | **GET** /v3.0/cartonType/{cartonTypeId}/tag | Get the tags for a cartonType.
[**get_duplicate_carton_type_by_id**](CartonTypeApi.md#get_duplicate_carton_type_by_id) | **GET** /v3.0/cartonType/duplicate/{cartonTypeId} | Get a duplicated a cartonType by id
[**update_carton_type**](CartonTypeApi.md#update_carton_type) | **PUT** /v3.0/cartonType | Update a cartonType
[**update_carton_type_custom_fields**](CartonTypeApi.md#update_carton_type_custom_fields) | **PUT** /v3.0/cartonType/customFields | Update a cartonType custom fields


# **add_carton_type**
> CartonType add_carton_type(body)

Create a cartonType

Inserts a new cartonType using the specified data.

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
api_instance = Infoplus.CartonTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.CartonType() # CartonType | CartonType to be inserted.

try:
    # Create a cartonType
    api_response = api_instance.add_carton_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonTypeApi->add_carton_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartonType**](CartonType.md)| CartonType to be inserted. | 

### Return type

[**CartonType**](CartonType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_carton_type_audit**
> add_carton_type_audit(carton_type_id, carton_type_audit)

Add new audit for a cartonType

Adds an audit to an existing cartonType.

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
api_instance = Infoplus.CartonTypeApi(Infoplus.ApiClient(configuration))
carton_type_id = 56 # int | Id of the cartonType to add an audit to
carton_type_audit = 'carton_type_audit_example' # str | The audit to add

try:
    # Add new audit for a cartonType
    api_instance.add_carton_type_audit(carton_type_id, carton_type_audit)
except ApiException as e:
    print("Exception when calling CartonTypeApi->add_carton_type_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_type_id** | **int**| Id of the cartonType to add an audit to | 
 **carton_type_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_carton_type_file**
> add_carton_type_file(carton_type_id, file_name)

Attach a file to a cartonType

Adds a file to an existing cartonType.

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
api_instance = Infoplus.CartonTypeApi(Infoplus.ApiClient(configuration))
carton_type_id = 56 # int | Id of the cartonType to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a cartonType
    api_instance.add_carton_type_file(carton_type_id, file_name)
except ApiException as e:
    print("Exception when calling CartonTypeApi->add_carton_type_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_type_id** | **int**| Id of the cartonType to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_carton_type_file_by_url**
> add_carton_type_file_by_url(body, carton_type_id)

Attach a file to a cartonType by URL.

Adds a file to an existing cartonType by URL.

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
api_instance = Infoplus.CartonTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
carton_type_id = 56 # int | Id of the cartonType to add an file to

try:
    # Attach a file to a cartonType by URL.
    api_instance.add_carton_type_file_by_url(body, carton_type_id)
except ApiException as e:
    print("Exception when calling CartonTypeApi->add_carton_type_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **carton_type_id** | **int**| Id of the cartonType to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_carton_type_tag**
> add_carton_type_tag(carton_type_id, carton_type_tag)

Add new tags for a cartonType.

Adds a tag to an existing cartonType.

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
api_instance = Infoplus.CartonTypeApi(Infoplus.ApiClient(configuration))
carton_type_id = 56 # int | Id of the cartonType to add a tag to
carton_type_tag = 'carton_type_tag_example' # str | The tag to add

try:
    # Add new tags for a cartonType.
    api_instance.add_carton_type_tag(carton_type_id, carton_type_tag)
except ApiException as e:
    print("Exception when calling CartonTypeApi->add_carton_type_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_type_id** | **int**| Id of the cartonType to add a tag to | 
 **carton_type_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_carton_type**
> delete_carton_type(carton_type_id)

Delete a cartonType

Deletes the cartonType identified by the specified id.

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
api_instance = Infoplus.CartonTypeApi(Infoplus.ApiClient(configuration))
carton_type_id = 56 # int | Id of the cartonType to be deleted.

try:
    # Delete a cartonType
    api_instance.delete_carton_type(carton_type_id)
except ApiException as e:
    print("Exception when calling CartonTypeApi->delete_carton_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_type_id** | **int**| Id of the cartonType to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_carton_type_file**
> delete_carton_type_file(carton_type_id, file_id)

Delete a file for a cartonType.

Deletes an existing cartonType file using the specified data.

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
api_instance = Infoplus.CartonTypeApi(Infoplus.ApiClient(configuration))
carton_type_id = 56 # int | Id of the cartonType to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a cartonType.
    api_instance.delete_carton_type_file(carton_type_id, file_id)
except ApiException as e:
    print("Exception when calling CartonTypeApi->delete_carton_type_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_type_id** | **int**| Id of the cartonType to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_carton_type_tag**
> delete_carton_type_tag(carton_type_id, carton_type_tag)

Delete a tag for a cartonType.

Deletes an existing cartonType tag using the specified data.

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
api_instance = Infoplus.CartonTypeApi(Infoplus.ApiClient(configuration))
carton_type_id = 56 # int | Id of the cartonType to remove tag from
carton_type_tag = 'carton_type_tag_example' # str | The tag to delete

try:
    # Delete a tag for a cartonType.
    api_instance.delete_carton_type_tag(carton_type_id, carton_type_tag)
except ApiException as e:
    print("Exception when calling CartonTypeApi->delete_carton_type_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_type_id** | **int**| Id of the cartonType to remove tag from | 
 **carton_type_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carton_type_by_filter**
> list[CartonType] get_carton_type_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search cartonTypes by filter

Returns the list of cartonTypes that match the given filter.

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
api_instance = Infoplus.CartonTypeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search cartonTypes by filter
    api_response = api_instance.get_carton_type_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonTypeApi->get_carton_type_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[CartonType]**](CartonType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carton_type_by_id**
> CartonType get_carton_type_by_id(carton_type_id)

Get a cartonType by id

Returns the cartonType identified by the specified id.

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
api_instance = Infoplus.CartonTypeApi(Infoplus.ApiClient(configuration))
carton_type_id = 56 # int | Id of the cartonType to be returned.

try:
    # Get a cartonType by id
    api_response = api_instance.get_carton_type_by_id(carton_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonTypeApi->get_carton_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_type_id** | **int**| Id of the cartonType to be returned. | 

### Return type

[**CartonType**](CartonType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carton_type_files**
> get_carton_type_files(carton_type_id)

Get the files for a cartonType.

Get all existing cartonType files.

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
api_instance = Infoplus.CartonTypeApi(Infoplus.ApiClient(configuration))
carton_type_id = 56 # int | Id of the cartonType to get files for

try:
    # Get the files for a cartonType.
    api_instance.get_carton_type_files(carton_type_id)
except ApiException as e:
    print("Exception when calling CartonTypeApi->get_carton_type_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_type_id** | **int**| Id of the cartonType to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carton_type_tags**
> get_carton_type_tags(carton_type_id)

Get the tags for a cartonType.

Get all existing cartonType tags.

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
api_instance = Infoplus.CartonTypeApi(Infoplus.ApiClient(configuration))
carton_type_id = 56 # int | Id of the cartonType to get tags for

try:
    # Get the tags for a cartonType.
    api_instance.get_carton_type_tags(carton_type_id)
except ApiException as e:
    print("Exception when calling CartonTypeApi->get_carton_type_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_type_id** | **int**| Id of the cartonType to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_carton_type_by_id**
> CartonType get_duplicate_carton_type_by_id(carton_type_id)

Get a duplicated a cartonType by id

Returns a duplicated cartonType identified by the specified id.

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
api_instance = Infoplus.CartonTypeApi(Infoplus.ApiClient(configuration))
carton_type_id = 56 # int | Id of the cartonType to be duplicated.

try:
    # Get a duplicated a cartonType by id
    api_response = api_instance.get_duplicate_carton_type_by_id(carton_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonTypeApi->get_duplicate_carton_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_type_id** | **int**| Id of the cartonType to be duplicated. | 

### Return type

[**CartonType**](CartonType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_carton_type**
> update_carton_type(body)

Update a cartonType

Updates an existing cartonType using the specified data.

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
api_instance = Infoplus.CartonTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.CartonType() # CartonType | CartonType to be updated.

try:
    # Update a cartonType
    api_instance.update_carton_type(body)
except ApiException as e:
    print("Exception when calling CartonTypeApi->update_carton_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartonType**](CartonType.md)| CartonType to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_carton_type_custom_fields**
> update_carton_type_custom_fields(body)

Update a cartonType custom fields

Updates an existing cartonType custom fields using the specified data.

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
api_instance = Infoplus.CartonTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.CartonType() # CartonType | CartonType to be updated.

try:
    # Update a cartonType custom fields
    api_instance.update_carton_type_custom_fields(body)
except ApiException as e:
    print("Exception when calling CartonTypeApi->update_carton_type_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartonType**](CartonType.md)| CartonType to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

