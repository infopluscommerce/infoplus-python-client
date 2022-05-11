# Infoplus.CartonContentApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_carton_content**](CartonContentApi.md#add_carton_content) | **POST** /v3.0/cartonContent | Create a cartonContent
[**add_carton_content_audit**](CartonContentApi.md#add_carton_content_audit) | **PUT** /v3.0/cartonContent/{cartonContentId}/audit/{cartonContentAudit} | Add new audit for a cartonContent
[**add_carton_content_file**](CartonContentApi.md#add_carton_content_file) | **POST** /v3.0/cartonContent/{cartonContentId}/file/{fileName} | Attach a file to a cartonContent
[**add_carton_content_file_by_url**](CartonContentApi.md#add_carton_content_file_by_url) | **POST** /v3.0/cartonContent/{cartonContentId}/file | Attach a file to a cartonContent by URL.
[**add_carton_content_tag**](CartonContentApi.md#add_carton_content_tag) | **PUT** /v3.0/cartonContent/{cartonContentId}/tag/{cartonContentTag} | Add new tags for a cartonContent.
[**delete_carton_content**](CartonContentApi.md#delete_carton_content) | **DELETE** /v3.0/cartonContent/{cartonContentId} | Delete a cartonContent
[**delete_carton_content_file**](CartonContentApi.md#delete_carton_content_file) | **DELETE** /v3.0/cartonContent/{cartonContentId}/file/{fileId} | Delete a file for a cartonContent.
[**delete_carton_content_tag**](CartonContentApi.md#delete_carton_content_tag) | **DELETE** /v3.0/cartonContent/{cartonContentId}/tag/{cartonContentTag} | Delete a tag for a cartonContent.
[**get_carton_content_by_filter**](CartonContentApi.md#get_carton_content_by_filter) | **GET** /v3.0/cartonContent/search | Search cartonContents by filter
[**get_carton_content_by_id**](CartonContentApi.md#get_carton_content_by_id) | **GET** /v3.0/cartonContent/{cartonContentId} | Get a cartonContent by id
[**get_carton_content_files**](CartonContentApi.md#get_carton_content_files) | **GET** /v3.0/cartonContent/{cartonContentId}/file | Get the files for a cartonContent.
[**get_carton_content_tags**](CartonContentApi.md#get_carton_content_tags) | **GET** /v3.0/cartonContent/{cartonContentId}/tag | Get the tags for a cartonContent.
[**get_duplicate_carton_content_by_id**](CartonContentApi.md#get_duplicate_carton_content_by_id) | **GET** /v3.0/cartonContent/duplicate/{cartonContentId} | Get a duplicated a cartonContent by id
[**update_carton_content**](CartonContentApi.md#update_carton_content) | **PUT** /v3.0/cartonContent | Update a cartonContent
[**update_carton_content_custom_fields**](CartonContentApi.md#update_carton_content_custom_fields) | **PUT** /v3.0/cartonContent/customFields | Update a cartonContent custom fields


# **add_carton_content**
> CartonContent add_carton_content(body)

Create a cartonContent

Inserts a new cartonContent using the specified data.

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
api_instance = Infoplus.CartonContentApi(Infoplus.ApiClient(configuration))
body = Infoplus.CartonContent() # CartonContent | CartonContent to be inserted.

try:
    # Create a cartonContent
    api_response = api_instance.add_carton_content(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonContentApi->add_carton_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartonContent**](CartonContent.md)| CartonContent to be inserted. | 

### Return type

[**CartonContent**](CartonContent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_carton_content_audit**
> add_carton_content_audit(carton_content_id, carton_content_audit)

Add new audit for a cartonContent

Adds an audit to an existing cartonContent.

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
api_instance = Infoplus.CartonContentApi(Infoplus.ApiClient(configuration))
carton_content_id = 56 # int | Id of the cartonContent to add an audit to
carton_content_audit = 'carton_content_audit_example' # str | The audit to add

try:
    # Add new audit for a cartonContent
    api_instance.add_carton_content_audit(carton_content_id, carton_content_audit)
except ApiException as e:
    print("Exception when calling CartonContentApi->add_carton_content_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_content_id** | **int**| Id of the cartonContent to add an audit to | 
 **carton_content_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_carton_content_file**
> add_carton_content_file(carton_content_id, file_name)

Attach a file to a cartonContent

Adds a file to an existing cartonContent.

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
api_instance = Infoplus.CartonContentApi(Infoplus.ApiClient(configuration))
carton_content_id = 56 # int | Id of the cartonContent to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a cartonContent
    api_instance.add_carton_content_file(carton_content_id, file_name)
except ApiException as e:
    print("Exception when calling CartonContentApi->add_carton_content_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_content_id** | **int**| Id of the cartonContent to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_carton_content_file_by_url**
> add_carton_content_file_by_url(body, carton_content_id)

Attach a file to a cartonContent by URL.

Adds a file to an existing cartonContent by URL.

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
api_instance = Infoplus.CartonContentApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
carton_content_id = 56 # int | Id of the cartonContent to add an file to

try:
    # Attach a file to a cartonContent by URL.
    api_instance.add_carton_content_file_by_url(body, carton_content_id)
except ApiException as e:
    print("Exception when calling CartonContentApi->add_carton_content_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **carton_content_id** | **int**| Id of the cartonContent to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_carton_content_tag**
> add_carton_content_tag(carton_content_id, carton_content_tag)

Add new tags for a cartonContent.

Adds a tag to an existing cartonContent.

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
api_instance = Infoplus.CartonContentApi(Infoplus.ApiClient(configuration))
carton_content_id = 56 # int | Id of the cartonContent to add a tag to
carton_content_tag = 'carton_content_tag_example' # str | The tag to add

try:
    # Add new tags for a cartonContent.
    api_instance.add_carton_content_tag(carton_content_id, carton_content_tag)
except ApiException as e:
    print("Exception when calling CartonContentApi->add_carton_content_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_content_id** | **int**| Id of the cartonContent to add a tag to | 
 **carton_content_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_carton_content**
> delete_carton_content(carton_content_id)

Delete a cartonContent

Deletes the cartonContent identified by the specified id.

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
api_instance = Infoplus.CartonContentApi(Infoplus.ApiClient(configuration))
carton_content_id = 56 # int | Id of the cartonContent to be deleted.

try:
    # Delete a cartonContent
    api_instance.delete_carton_content(carton_content_id)
except ApiException as e:
    print("Exception when calling CartonContentApi->delete_carton_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_content_id** | **int**| Id of the cartonContent to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_carton_content_file**
> delete_carton_content_file(carton_content_id, file_id)

Delete a file for a cartonContent.

Deletes an existing cartonContent file using the specified data.

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
api_instance = Infoplus.CartonContentApi(Infoplus.ApiClient(configuration))
carton_content_id = 56 # int | Id of the cartonContent to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a cartonContent.
    api_instance.delete_carton_content_file(carton_content_id, file_id)
except ApiException as e:
    print("Exception when calling CartonContentApi->delete_carton_content_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_content_id** | **int**| Id of the cartonContent to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_carton_content_tag**
> delete_carton_content_tag(carton_content_id, carton_content_tag)

Delete a tag for a cartonContent.

Deletes an existing cartonContent tag using the specified data.

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
api_instance = Infoplus.CartonContentApi(Infoplus.ApiClient(configuration))
carton_content_id = 56 # int | Id of the cartonContent to remove tag from
carton_content_tag = 'carton_content_tag_example' # str | The tag to delete

try:
    # Delete a tag for a cartonContent.
    api_instance.delete_carton_content_tag(carton_content_id, carton_content_tag)
except ApiException as e:
    print("Exception when calling CartonContentApi->delete_carton_content_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_content_id** | **int**| Id of the cartonContent to remove tag from | 
 **carton_content_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carton_content_by_filter**
> list[CartonContent] get_carton_content_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search cartonContents by filter

Returns the list of cartonContents that match the given filter.

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
api_instance = Infoplus.CartonContentApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search cartonContents by filter
    api_response = api_instance.get_carton_content_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonContentApi->get_carton_content_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[CartonContent]**](CartonContent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carton_content_by_id**
> CartonContent get_carton_content_by_id(carton_content_id)

Get a cartonContent by id

Returns the cartonContent identified by the specified id.

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
api_instance = Infoplus.CartonContentApi(Infoplus.ApiClient(configuration))
carton_content_id = 56 # int | Id of the cartonContent to be returned.

try:
    # Get a cartonContent by id
    api_response = api_instance.get_carton_content_by_id(carton_content_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonContentApi->get_carton_content_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_content_id** | **int**| Id of the cartonContent to be returned. | 

### Return type

[**CartonContent**](CartonContent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carton_content_files**
> get_carton_content_files(carton_content_id)

Get the files for a cartonContent.

Get all existing cartonContent files.

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
api_instance = Infoplus.CartonContentApi(Infoplus.ApiClient(configuration))
carton_content_id = 56 # int | Id of the cartonContent to get files for

try:
    # Get the files for a cartonContent.
    api_instance.get_carton_content_files(carton_content_id)
except ApiException as e:
    print("Exception when calling CartonContentApi->get_carton_content_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_content_id** | **int**| Id of the cartonContent to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carton_content_tags**
> get_carton_content_tags(carton_content_id)

Get the tags for a cartonContent.

Get all existing cartonContent tags.

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
api_instance = Infoplus.CartonContentApi(Infoplus.ApiClient(configuration))
carton_content_id = 56 # int | Id of the cartonContent to get tags for

try:
    # Get the tags for a cartonContent.
    api_instance.get_carton_content_tags(carton_content_id)
except ApiException as e:
    print("Exception when calling CartonContentApi->get_carton_content_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_content_id** | **int**| Id of the cartonContent to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_carton_content_by_id**
> CartonContent get_duplicate_carton_content_by_id(carton_content_id)

Get a duplicated a cartonContent by id

Returns a duplicated cartonContent identified by the specified id.

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
api_instance = Infoplus.CartonContentApi(Infoplus.ApiClient(configuration))
carton_content_id = 56 # int | Id of the cartonContent to be duplicated.

try:
    # Get a duplicated a cartonContent by id
    api_response = api_instance.get_duplicate_carton_content_by_id(carton_content_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartonContentApi->get_duplicate_carton_content_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carton_content_id** | **int**| Id of the cartonContent to be duplicated. | 

### Return type

[**CartonContent**](CartonContent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_carton_content**
> update_carton_content(body)

Update a cartonContent

Updates an existing cartonContent using the specified data.

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
api_instance = Infoplus.CartonContentApi(Infoplus.ApiClient(configuration))
body = Infoplus.CartonContent() # CartonContent | CartonContent to be updated.

try:
    # Update a cartonContent
    api_instance.update_carton_content(body)
except ApiException as e:
    print("Exception when calling CartonContentApi->update_carton_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartonContent**](CartonContent.md)| CartonContent to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_carton_content_custom_fields**
> update_carton_content_custom_fields(body)

Update a cartonContent custom fields

Updates an existing cartonContent custom fields using the specified data.

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
api_instance = Infoplus.CartonContentApi(Infoplus.ApiClient(configuration))
body = Infoplus.CartonContent() # CartonContent | CartonContent to be updated.

try:
    # Update a cartonContent custom fields
    api_instance.update_carton_content_custom_fields(body)
except ApiException as e:
    print("Exception when calling CartonContentApi->update_carton_content_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartonContent**](CartonContent.md)| CartonContent to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

