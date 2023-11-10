# Infoplus.LoadContentApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_load_content_audit**](LoadContentApi.md#add_load_content_audit) | **PUT** /beta/loadContent/{loadContentId}/audit/{loadContentAudit} | Add new audit for a loadContent
[**add_load_content_file**](LoadContentApi.md#add_load_content_file) | **POST** /beta/loadContent/{loadContentId}/file/{fileName} | Attach a file to a loadContent
[**add_load_content_file_by_url**](LoadContentApi.md#add_load_content_file_by_url) | **POST** /beta/loadContent/{loadContentId}/file | Attach a file to a loadContent by URL.
[**add_load_content_tag**](LoadContentApi.md#add_load_content_tag) | **PUT** /beta/loadContent/{loadContentId}/tag/{loadContentTag} | Add new tags for a loadContent.
[**delete_load_content_file**](LoadContentApi.md#delete_load_content_file) | **DELETE** /beta/loadContent/{loadContentId}/file/{fileId} | Delete a file for a loadContent.
[**delete_load_content_tag**](LoadContentApi.md#delete_load_content_tag) | **DELETE** /beta/loadContent/{loadContentId}/tag/{loadContentTag} | Delete a tag for a loadContent.
[**get_duplicate_load_content_by_id**](LoadContentApi.md#get_duplicate_load_content_by_id) | **GET** /beta/loadContent/duplicate/{loadContentId} | Get a duplicated a loadContent by id
[**get_load_content_by_filter**](LoadContentApi.md#get_load_content_by_filter) | **GET** /beta/loadContent/search | Search loadContents by filter
[**get_load_content_by_id**](LoadContentApi.md#get_load_content_by_id) | **GET** /beta/loadContent/{loadContentId} | Get a loadContent by id
[**get_load_content_files**](LoadContentApi.md#get_load_content_files) | **GET** /beta/loadContent/{loadContentId}/file | Get the files for a loadContent.
[**get_load_content_tags**](LoadContentApi.md#get_load_content_tags) | **GET** /beta/loadContent/{loadContentId}/tag | Get the tags for a loadContent.
[**update_load_content_custom_fields**](LoadContentApi.md#update_load_content_custom_fields) | **PUT** /beta/loadContent/customFields | Update a loadContent custom fields


# **add_load_content_audit**
> add_load_content_audit(load_content_id, load_content_audit)

Add new audit for a loadContent

Adds an audit to an existing loadContent.

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
api_instance = Infoplus.LoadContentApi(Infoplus.ApiClient(configuration))
load_content_id = 56 # int | Id of the loadContent to add an audit to
load_content_audit = 'load_content_audit_example' # str | The audit to add

try:
    # Add new audit for a loadContent
    api_instance.add_load_content_audit(load_content_id, load_content_audit)
except ApiException as e:
    print("Exception when calling LoadContentApi->add_load_content_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_content_id** | **int**| Id of the loadContent to add an audit to | 
 **load_content_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_load_content_file**
> add_load_content_file(load_content_id, file_name)

Attach a file to a loadContent

Adds a file to an existing loadContent.

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
api_instance = Infoplus.LoadContentApi(Infoplus.ApiClient(configuration))
load_content_id = 56 # int | Id of the loadContent to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a loadContent
    api_instance.add_load_content_file(load_content_id, file_name)
except ApiException as e:
    print("Exception when calling LoadContentApi->add_load_content_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_content_id** | **int**| Id of the loadContent to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_load_content_file_by_url**
> add_load_content_file_by_url(body, load_content_id)

Attach a file to a loadContent by URL.

Adds a file to an existing loadContent by URL.

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
api_instance = Infoplus.LoadContentApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
load_content_id = 56 # int | Id of the loadContent to add an file to

try:
    # Attach a file to a loadContent by URL.
    api_instance.add_load_content_file_by_url(body, load_content_id)
except ApiException as e:
    print("Exception when calling LoadContentApi->add_load_content_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **load_content_id** | **int**| Id of the loadContent to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_load_content_tag**
> add_load_content_tag(load_content_id, load_content_tag)

Add new tags for a loadContent.

Adds a tag to an existing loadContent.

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
api_instance = Infoplus.LoadContentApi(Infoplus.ApiClient(configuration))
load_content_id = 56 # int | Id of the loadContent to add a tag to
load_content_tag = 'load_content_tag_example' # str | The tag to add

try:
    # Add new tags for a loadContent.
    api_instance.add_load_content_tag(load_content_id, load_content_tag)
except ApiException as e:
    print("Exception when calling LoadContentApi->add_load_content_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_content_id** | **int**| Id of the loadContent to add a tag to | 
 **load_content_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_content_file**
> delete_load_content_file(load_content_id, file_id)

Delete a file for a loadContent.

Deletes an existing loadContent file using the specified data.

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
api_instance = Infoplus.LoadContentApi(Infoplus.ApiClient(configuration))
load_content_id = 56 # int | Id of the loadContent to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a loadContent.
    api_instance.delete_load_content_file(load_content_id, file_id)
except ApiException as e:
    print("Exception when calling LoadContentApi->delete_load_content_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_content_id** | **int**| Id of the loadContent to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_content_tag**
> delete_load_content_tag(load_content_id, load_content_tag)

Delete a tag for a loadContent.

Deletes an existing loadContent tag using the specified data.

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
api_instance = Infoplus.LoadContentApi(Infoplus.ApiClient(configuration))
load_content_id = 56 # int | Id of the loadContent to remove tag from
load_content_tag = 'load_content_tag_example' # str | The tag to delete

try:
    # Delete a tag for a loadContent.
    api_instance.delete_load_content_tag(load_content_id, load_content_tag)
except ApiException as e:
    print("Exception when calling LoadContentApi->delete_load_content_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_content_id** | **int**| Id of the loadContent to remove tag from | 
 **load_content_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_load_content_by_id**
> LoadContent get_duplicate_load_content_by_id(load_content_id)

Get a duplicated a loadContent by id

Returns a duplicated loadContent identified by the specified id.

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
api_instance = Infoplus.LoadContentApi(Infoplus.ApiClient(configuration))
load_content_id = 56 # int | Id of the loadContent to be duplicated.

try:
    # Get a duplicated a loadContent by id
    api_response = api_instance.get_duplicate_load_content_by_id(load_content_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadContentApi->get_duplicate_load_content_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_content_id** | **int**| Id of the loadContent to be duplicated. | 

### Return type

[**LoadContent**](LoadContent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_content_by_filter**
> list[LoadContent] get_load_content_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search loadContents by filter

Returns the list of loadContents that match the given filter.

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
api_instance = Infoplus.LoadContentApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search loadContents by filter
    api_response = api_instance.get_load_content_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadContentApi->get_load_content_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[LoadContent]**](LoadContent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_content_by_id**
> LoadContent get_load_content_by_id(load_content_id)

Get a loadContent by id

Returns the loadContent identified by the specified id.

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
api_instance = Infoplus.LoadContentApi(Infoplus.ApiClient(configuration))
load_content_id = 56 # int | Id of the loadContent to be returned.

try:
    # Get a loadContent by id
    api_response = api_instance.get_load_content_by_id(load_content_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadContentApi->get_load_content_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_content_id** | **int**| Id of the loadContent to be returned. | 

### Return type

[**LoadContent**](LoadContent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_content_files**
> get_load_content_files(load_content_id)

Get the files for a loadContent.

Get all existing loadContent files.

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
api_instance = Infoplus.LoadContentApi(Infoplus.ApiClient(configuration))
load_content_id = 56 # int | Id of the loadContent to get files for

try:
    # Get the files for a loadContent.
    api_instance.get_load_content_files(load_content_id)
except ApiException as e:
    print("Exception when calling LoadContentApi->get_load_content_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_content_id** | **int**| Id of the loadContent to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_content_tags**
> get_load_content_tags(load_content_id)

Get the tags for a loadContent.

Get all existing loadContent tags.

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
api_instance = Infoplus.LoadContentApi(Infoplus.ApiClient(configuration))
load_content_id = 56 # int | Id of the loadContent to get tags for

try:
    # Get the tags for a loadContent.
    api_instance.get_load_content_tags(load_content_id)
except ApiException as e:
    print("Exception when calling LoadContentApi->get_load_content_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_content_id** | **int**| Id of the loadContent to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_load_content_custom_fields**
> update_load_content_custom_fields(body)

Update a loadContent custom fields

Updates an existing loadContent custom fields using the specified data.

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
api_instance = Infoplus.LoadContentApi(Infoplus.ApiClient(configuration))
body = Infoplus.LoadContent() # LoadContent | LoadContent to be updated.

try:
    # Update a loadContent custom fields
    api_instance.update_load_content_custom_fields(body)
except ApiException as e:
    print("Exception when calling LoadContentApi->update_load_content_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoadContent**](LoadContent.md)| LoadContent to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

