# Infoplus.CartonApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_carton**](CartonApi.md#add_carton) | **POST** /beta/carton | Create a carton
[**add_carton_audit**](CartonApi.md#add_carton_audit) | **PUT** /beta/carton/{cartonId}/audit/{cartonAudit} | Add new audit for a carton
[**add_carton_file**](CartonApi.md#add_carton_file) | **POST** /beta/carton/{cartonId}/file/{fileName} | Attach a file to a carton
[**add_carton_file_by_url**](CartonApi.md#add_carton_file_by_url) | **POST** /beta/carton/{cartonId}/file | Attach a file to a carton by URL.
[**add_carton_tag**](CartonApi.md#add_carton_tag) | **PUT** /beta/carton/{cartonId}/tag/{cartonTag} | Add new tags for a carton.
[**delete_carton**](CartonApi.md#delete_carton) | **DELETE** /beta/carton/{cartonId} | Delete a carton
[**delete_carton_file**](CartonApi.md#delete_carton_file) | **DELETE** /beta/carton/{cartonId}/file/{fileId} | Delete a file for a carton.
[**delete_carton_tag**](CartonApi.md#delete_carton_tag) | **DELETE** /beta/carton/{cartonId}/tag/{cartonTag} | Delete a tag for a carton.
[**get_carton_by_filter**](CartonApi.md#get_carton_by_filter) | **GET** /beta/carton/search | Search cartons by filter
[**get_carton_by_id**](CartonApi.md#get_carton_by_id) | **GET** /beta/carton/{cartonId} | Get a carton by id
[**get_carton_files**](CartonApi.md#get_carton_files) | **GET** /beta/carton/{cartonId}/file | Get the files for a carton.
[**get_carton_tags**](CartonApi.md#get_carton_tags) | **GET** /beta/carton/{cartonId}/tag | Get the tags for a carton.
[**get_duplicate_carton_by_id**](CartonApi.md#get_duplicate_carton_by_id) | **GET** /beta/carton/duplicate/{cartonId} | Get a duplicated a carton by id
[**update_carton**](CartonApi.md#update_carton) | **PUT** /beta/carton | Update a carton
[**update_carton_custom_fields**](CartonApi.md#update_carton_custom_fields) | **PUT** /beta/carton/customFields | Update a carton custom fields


# **add_carton**
> Carton add_carton(body)

Create a carton

Inserts a new carton using the specified data.

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
api_instance = Infoplus.CartonApi(Infoplus.ApiClient(configuration))
body = Infoplus.Carton() # Carton | Carton to be inserted.

try:
    # Create a carton
    api_response = api_instance.add_carton(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonApi->add_carton: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Carton**](Carton.md)| Carton to be inserted. | 

### Return type

[**Carton**](Carton.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_carton_audit**
> add_carton_audit(carton_id, carton_audit)

Add new audit for a carton

Adds an audit to an existing carton.

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
api_instance = Infoplus.CartonApi(Infoplus.ApiClient(configuration))
carton_id = 56 # int | Id of the carton to add an audit to
carton_audit = 'carton_audit_example' # str | The audit to add

try:
    # Add new audit for a carton
    api_instance.add_carton_audit(carton_id, carton_audit)
except ApiException as e:
    print("Exception when calling CartonApi->add_carton_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_id** | **int**| Id of the carton to add an audit to | 
 **carton_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_carton_file**
> add_carton_file(carton_id, file_name)

Attach a file to a carton

Adds a file to an existing carton.

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
api_instance = Infoplus.CartonApi(Infoplus.ApiClient(configuration))
carton_id = 56 # int | Id of the carton to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a carton
    api_instance.add_carton_file(carton_id, file_name)
except ApiException as e:
    print("Exception when calling CartonApi->add_carton_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_id** | **int**| Id of the carton to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_carton_file_by_url**
> add_carton_file_by_url(body, carton_id)

Attach a file to a carton by URL.

Adds a file to an existing carton by URL.

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
api_instance = Infoplus.CartonApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
carton_id = 56 # int | Id of the carton to add an file to

try:
    # Attach a file to a carton by URL.
    api_instance.add_carton_file_by_url(body, carton_id)
except ApiException as e:
    print("Exception when calling CartonApi->add_carton_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **carton_id** | **int**| Id of the carton to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_carton_tag**
> add_carton_tag(carton_id, carton_tag)

Add new tags for a carton.

Adds a tag to an existing carton.

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
api_instance = Infoplus.CartonApi(Infoplus.ApiClient(configuration))
carton_id = 56 # int | Id of the carton to add a tag to
carton_tag = 'carton_tag_example' # str | The tag to add

try:
    # Add new tags for a carton.
    api_instance.add_carton_tag(carton_id, carton_tag)
except ApiException as e:
    print("Exception when calling CartonApi->add_carton_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_id** | **int**| Id of the carton to add a tag to | 
 **carton_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_carton**
> delete_carton(carton_id)

Delete a carton

Deletes the carton identified by the specified id.

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
api_instance = Infoplus.CartonApi(Infoplus.ApiClient(configuration))
carton_id = 56 # int | Id of the carton to be deleted.

try:
    # Delete a carton
    api_instance.delete_carton(carton_id)
except ApiException as e:
    print("Exception when calling CartonApi->delete_carton: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_id** | **int**| Id of the carton to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_carton_file**
> delete_carton_file(carton_id, file_id)

Delete a file for a carton.

Deletes an existing carton file using the specified data.

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
api_instance = Infoplus.CartonApi(Infoplus.ApiClient(configuration))
carton_id = 56 # int | Id of the carton to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a carton.
    api_instance.delete_carton_file(carton_id, file_id)
except ApiException as e:
    print("Exception when calling CartonApi->delete_carton_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_id** | **int**| Id of the carton to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_carton_tag**
> delete_carton_tag(carton_id, carton_tag)

Delete a tag for a carton.

Deletes an existing carton tag using the specified data.

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
api_instance = Infoplus.CartonApi(Infoplus.ApiClient(configuration))
carton_id = 56 # int | Id of the carton to remove tag from
carton_tag = 'carton_tag_example' # str | The tag to delete

try:
    # Delete a tag for a carton.
    api_instance.delete_carton_tag(carton_id, carton_tag)
except ApiException as e:
    print("Exception when calling CartonApi->delete_carton_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_id** | **int**| Id of the carton to remove tag from | 
 **carton_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carton_by_filter**
> list[Carton] get_carton_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search cartons by filter

Returns the list of cartons that match the given filter.

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
api_instance = Infoplus.CartonApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search cartons by filter
    api_response = api_instance.get_carton_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonApi->get_carton_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Carton]**](Carton.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carton_by_id**
> Carton get_carton_by_id(carton_id)

Get a carton by id

Returns the carton identified by the specified id.

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
api_instance = Infoplus.CartonApi(Infoplus.ApiClient(configuration))
carton_id = 56 # int | Id of the carton to be returned.

try:
    # Get a carton by id
    api_response = api_instance.get_carton_by_id(carton_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonApi->get_carton_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_id** | **int**| Id of the carton to be returned. | 

### Return type

[**Carton**](Carton.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carton_files**
> get_carton_files(carton_id)

Get the files for a carton.

Get all existing carton files.

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
api_instance = Infoplus.CartonApi(Infoplus.ApiClient(configuration))
carton_id = 56 # int | Id of the carton to get files for

try:
    # Get the files for a carton.
    api_instance.get_carton_files(carton_id)
except ApiException as e:
    print("Exception when calling CartonApi->get_carton_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_id** | **int**| Id of the carton to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carton_tags**
> get_carton_tags(carton_id)

Get the tags for a carton.

Get all existing carton tags.

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
api_instance = Infoplus.CartonApi(Infoplus.ApiClient(configuration))
carton_id = 56 # int | Id of the carton to get tags for

try:
    # Get the tags for a carton.
    api_instance.get_carton_tags(carton_id)
except ApiException as e:
    print("Exception when calling CartonApi->get_carton_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_id** | **int**| Id of the carton to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_carton_by_id**
> Carton get_duplicate_carton_by_id(carton_id)

Get a duplicated a carton by id

Returns a duplicated carton identified by the specified id.

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
api_instance = Infoplus.CartonApi(Infoplus.ApiClient(configuration))
carton_id = 56 # int | Id of the carton to be duplicated.

try:
    # Get a duplicated a carton by id
    api_response = api_instance.get_duplicate_carton_by_id(carton_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonApi->get_duplicate_carton_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_id** | **int**| Id of the carton to be duplicated. | 

### Return type

[**Carton**](Carton.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_carton**
> update_carton(body)

Update a carton

Updates an existing carton using the specified data.

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
api_instance = Infoplus.CartonApi(Infoplus.ApiClient(configuration))
body = Infoplus.Carton() # Carton | Carton to be updated.

try:
    # Update a carton
    api_instance.update_carton(body)
except ApiException as e:
    print("Exception when calling CartonApi->update_carton: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Carton**](Carton.md)| Carton to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_carton_custom_fields**
> update_carton_custom_fields(body)

Update a carton custom fields

Updates an existing carton custom fields using the specified data.

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
api_instance = Infoplus.CartonApi(Infoplus.ApiClient(configuration))
body = Infoplus.Carton() # Carton | Carton to be updated.

try:
    # Update a carton custom fields
    api_instance.update_carton_custom_fields(body)
except ApiException as e:
    print("Exception when calling CartonApi->update_carton_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Carton**](Carton.md)| Carton to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

