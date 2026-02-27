# Infoplus.CustomFieldApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_field**](CustomFieldApi.md#add_custom_field) | **POST** /beta/customField | Create a customField
[**add_custom_field_audit**](CustomFieldApi.md#add_custom_field_audit) | **PUT** /beta/customField/{customFieldId}/audit/{customFieldAudit} | Add new audit for a customField
[**add_custom_field_file**](CustomFieldApi.md#add_custom_field_file) | **POST** /beta/customField/{customFieldId}/file/{fileName} | Attach a file to a customField
[**add_custom_field_file_by_url**](CustomFieldApi.md#add_custom_field_file_by_url) | **POST** /beta/customField/{customFieldId}/file | Attach a file to a customField by URL.
[**add_custom_field_tag**](CustomFieldApi.md#add_custom_field_tag) | **PUT** /beta/customField/{customFieldId}/tag/{customFieldTag} | Add new tags for a customField.
[**delete_custom_field_file**](CustomFieldApi.md#delete_custom_field_file) | **DELETE** /beta/customField/{customFieldId}/file/{fileId} | Delete a file for a customField.
[**delete_custom_field_tag**](CustomFieldApi.md#delete_custom_field_tag) | **DELETE** /beta/customField/{customFieldId}/tag/{customFieldTag} | Delete a tag for a customField.
[**get_custom_field_by_filter**](CustomFieldApi.md#get_custom_field_by_filter) | **GET** /beta/customField/search | Search customFields by filter
[**get_custom_field_by_id**](CustomFieldApi.md#get_custom_field_by_id) | **GET** /beta/customField/{customFieldId} | Get a customField by id
[**get_custom_field_files**](CustomFieldApi.md#get_custom_field_files) | **GET** /beta/customField/{customFieldId}/file | Get the files for a customField.
[**get_custom_field_tags**](CustomFieldApi.md#get_custom_field_tags) | **GET** /beta/customField/{customFieldId}/tag | Get the tags for a customField.
[**get_duplicate_custom_field_by_id**](CustomFieldApi.md#get_duplicate_custom_field_by_id) | **GET** /beta/customField/duplicate/{customFieldId} | Get a duplicated a customField by id
[**update_custom_field**](CustomFieldApi.md#update_custom_field) | **PUT** /beta/customField | Update a customField


# **add_custom_field**
> CustomField add_custom_field(body)

Create a customField

Inserts a new customField using the specified data.

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
api_instance = Infoplus.CustomFieldApi(Infoplus.ApiClient(configuration))
body = Infoplus.CustomField() # CustomField | CustomField to be inserted.

try:
    # Create a customField
    api_response = api_instance.add_custom_field(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldApi->add_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomField**](CustomField.md)| CustomField to be inserted. | 

### Return type

[**CustomField**](CustomField.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_custom_field_audit**
> add_custom_field_audit(custom_field_id, custom_field_audit)

Add new audit for a customField

Adds an audit to an existing customField.

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
api_instance = Infoplus.CustomFieldApi(Infoplus.ApiClient(configuration))
custom_field_id = 56 # int | Id of the customField to add an audit to
custom_field_audit = 'custom_field_audit_example' # str | The audit to add

try:
    # Add new audit for a customField
    api_instance.add_custom_field_audit(custom_field_id, custom_field_audit)
except ApiException as e:
    print("Exception when calling CustomFieldApi->add_custom_field_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **int**| Id of the customField to add an audit to | 
 **custom_field_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_custom_field_file**
> add_custom_field_file(custom_field_id, file_name)

Attach a file to a customField

Adds a file to an existing customField.

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
api_instance = Infoplus.CustomFieldApi(Infoplus.ApiClient(configuration))
custom_field_id = 56 # int | Id of the customField to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a customField
    api_instance.add_custom_field_file(custom_field_id, file_name)
except ApiException as e:
    print("Exception when calling CustomFieldApi->add_custom_field_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **int**| Id of the customField to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_custom_field_file_by_url**
> add_custom_field_file_by_url(body, custom_field_id)

Attach a file to a customField by URL.

Adds a file to an existing customField by URL.

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
api_instance = Infoplus.CustomFieldApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
custom_field_id = 56 # int | Id of the customField to add an file to

try:
    # Attach a file to a customField by URL.
    api_instance.add_custom_field_file_by_url(body, custom_field_id)
except ApiException as e:
    print("Exception when calling CustomFieldApi->add_custom_field_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **custom_field_id** | **int**| Id of the customField to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_custom_field_tag**
> add_custom_field_tag(custom_field_id, custom_field_tag)

Add new tags for a customField.

Adds a tag to an existing customField.

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
api_instance = Infoplus.CustomFieldApi(Infoplus.ApiClient(configuration))
custom_field_id = 56 # int | Id of the customField to add a tag to
custom_field_tag = 'custom_field_tag_example' # str | The tag to add

try:
    # Add new tags for a customField.
    api_instance.add_custom_field_tag(custom_field_id, custom_field_tag)
except ApiException as e:
    print("Exception when calling CustomFieldApi->add_custom_field_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **int**| Id of the customField to add a tag to | 
 **custom_field_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field_file**
> delete_custom_field_file(custom_field_id, file_id)

Delete a file for a customField.

Deletes an existing customField file using the specified data.

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
api_instance = Infoplus.CustomFieldApi(Infoplus.ApiClient(configuration))
custom_field_id = 56 # int | Id of the customField to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a customField.
    api_instance.delete_custom_field_file(custom_field_id, file_id)
except ApiException as e:
    print("Exception when calling CustomFieldApi->delete_custom_field_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **int**| Id of the customField to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field_tag**
> delete_custom_field_tag(custom_field_id, custom_field_tag)

Delete a tag for a customField.

Deletes an existing customField tag using the specified data.

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
api_instance = Infoplus.CustomFieldApi(Infoplus.ApiClient(configuration))
custom_field_id = 56 # int | Id of the customField to remove tag from
custom_field_tag = 'custom_field_tag_example' # str | The tag to delete

try:
    # Delete a tag for a customField.
    api_instance.delete_custom_field_tag(custom_field_id, custom_field_tag)
except ApiException as e:
    print("Exception when calling CustomFieldApi->delete_custom_field_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **int**| Id of the customField to remove tag from | 
 **custom_field_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field_by_filter**
> list[CustomField] get_custom_field_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search customFields by filter

Returns the list of customFields that match the given filter.

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
api_instance = Infoplus.CustomFieldApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search customFields by filter
    api_response = api_instance.get_custom_field_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldApi->get_custom_field_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[CustomField]**](CustomField.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field_by_id**
> CustomField get_custom_field_by_id(custom_field_id)

Get a customField by id

Returns the customField identified by the specified id.

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
api_instance = Infoplus.CustomFieldApi(Infoplus.ApiClient(configuration))
custom_field_id = 56 # int | Id of the customField to be returned.

try:
    # Get a customField by id
    api_response = api_instance.get_custom_field_by_id(custom_field_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldApi->get_custom_field_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **int**| Id of the customField to be returned. | 

### Return type

[**CustomField**](CustomField.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field_files**
> get_custom_field_files(custom_field_id)

Get the files for a customField.

Get all existing customField files.

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
api_instance = Infoplus.CustomFieldApi(Infoplus.ApiClient(configuration))
custom_field_id = 56 # int | Id of the customField to get files for

try:
    # Get the files for a customField.
    api_instance.get_custom_field_files(custom_field_id)
except ApiException as e:
    print("Exception when calling CustomFieldApi->get_custom_field_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **int**| Id of the customField to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field_tags**
> get_custom_field_tags(custom_field_id)

Get the tags for a customField.

Get all existing customField tags.

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
api_instance = Infoplus.CustomFieldApi(Infoplus.ApiClient(configuration))
custom_field_id = 56 # int | Id of the customField to get tags for

try:
    # Get the tags for a customField.
    api_instance.get_custom_field_tags(custom_field_id)
except ApiException as e:
    print("Exception when calling CustomFieldApi->get_custom_field_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **int**| Id of the customField to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_custom_field_by_id**
> CustomField get_duplicate_custom_field_by_id(custom_field_id)

Get a duplicated a customField by id

Returns a duplicated customField identified by the specified id.

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
api_instance = Infoplus.CustomFieldApi(Infoplus.ApiClient(configuration))
custom_field_id = 56 # int | Id of the customField to be duplicated.

try:
    # Get a duplicated a customField by id
    api_response = api_instance.get_duplicate_custom_field_by_id(custom_field_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldApi->get_duplicate_custom_field_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **int**| Id of the customField to be duplicated. | 

### Return type

[**CustomField**](CustomField.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field**
> update_custom_field(body)

Update a customField

Updates an existing customField using the specified data.

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
api_instance = Infoplus.CustomFieldApi(Infoplus.ApiClient(configuration))
body = Infoplus.CustomField() # CustomField | CustomField to be updated.

try:
    # Update a customField
    api_instance.update_custom_field(body)
except ApiException as e:
    print("Exception when calling CustomFieldApi->update_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomField**](CustomField.md)| CustomField to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

