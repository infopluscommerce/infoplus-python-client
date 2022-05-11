# Infoplus.Gs1128TemplateApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_gs1128_template**](Gs1128TemplateApi.md#add_gs1128_template) | **POST** /v3.0/gs1128Template | Create a gs1128Template
[**add_gs1128_template_audit**](Gs1128TemplateApi.md#add_gs1128_template_audit) | **PUT** /v3.0/gs1128Template/{gs1128TemplateId}/audit/{gs1128TemplateAudit} | Add new audit for a gs1128Template
[**add_gs1128_template_file**](Gs1128TemplateApi.md#add_gs1128_template_file) | **POST** /v3.0/gs1128Template/{gs1128TemplateId}/file/{fileName} | Attach a file to a gs1128Template
[**add_gs1128_template_file_by_url**](Gs1128TemplateApi.md#add_gs1128_template_file_by_url) | **POST** /v3.0/gs1128Template/{gs1128TemplateId}/file | Attach a file to a gs1128Template by URL.
[**add_gs1128_template_tag**](Gs1128TemplateApi.md#add_gs1128_template_tag) | **PUT** /v3.0/gs1128Template/{gs1128TemplateId}/tag/{gs1128TemplateTag} | Add new tags for a gs1128Template.
[**delete_gs1128_template**](Gs1128TemplateApi.md#delete_gs1128_template) | **DELETE** /v3.0/gs1128Template/{gs1128TemplateId} | Delete a gs1128Template
[**delete_gs1128_template_file**](Gs1128TemplateApi.md#delete_gs1128_template_file) | **DELETE** /v3.0/gs1128Template/{gs1128TemplateId}/file/{fileId} | Delete a file for a gs1128Template.
[**delete_gs1128_template_tag**](Gs1128TemplateApi.md#delete_gs1128_template_tag) | **DELETE** /v3.0/gs1128Template/{gs1128TemplateId}/tag/{gs1128TemplateTag} | Delete a tag for a gs1128Template.
[**get_duplicate_gs1128_template_by_id**](Gs1128TemplateApi.md#get_duplicate_gs1128_template_by_id) | **GET** /v3.0/gs1128Template/duplicate/{gs1128TemplateId} | Get a duplicated a gs1128Template by id
[**get_gs1128_template_by_filter**](Gs1128TemplateApi.md#get_gs1128_template_by_filter) | **GET** /v3.0/gs1128Template/search | Search gs1128Templates by filter
[**get_gs1128_template_by_id**](Gs1128TemplateApi.md#get_gs1128_template_by_id) | **GET** /v3.0/gs1128Template/{gs1128TemplateId} | Get a gs1128Template by id
[**get_gs1128_template_files**](Gs1128TemplateApi.md#get_gs1128_template_files) | **GET** /v3.0/gs1128Template/{gs1128TemplateId}/file | Get the files for a gs1128Template.
[**get_gs1128_template_tags**](Gs1128TemplateApi.md#get_gs1128_template_tags) | **GET** /v3.0/gs1128Template/{gs1128TemplateId}/tag | Get the tags for a gs1128Template.
[**update_gs1128_template**](Gs1128TemplateApi.md#update_gs1128_template) | **PUT** /v3.0/gs1128Template | Update a gs1128Template


# **add_gs1128_template**
> Gs1128Template add_gs1128_template(body)

Create a gs1128Template

Inserts a new gs1128Template using the specified data.

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
api_instance = Infoplus.Gs1128TemplateApi(Infoplus.ApiClient(configuration))
body = Infoplus.Gs1128Template() # Gs1128Template | Gs1128Template to be inserted.

try:
    # Create a gs1128Template
    api_response = api_instance.add_gs1128_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Gs1128TemplateApi->add_gs1128_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Gs1128Template**](Gs1128Template.md)| Gs1128Template to be inserted. | 

### Return type

[**Gs1128Template**](Gs1128Template.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_gs1128_template_audit**
> add_gs1128_template_audit(gs1128_template_id, gs1128_template_audit)

Add new audit for a gs1128Template

Adds an audit to an existing gs1128Template.

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
api_instance = Infoplus.Gs1128TemplateApi(Infoplus.ApiClient(configuration))
gs1128_template_id = 56 # int | Id of the gs1128Template to add an audit to
gs1128_template_audit = 'gs1128_template_audit_example' # str | The audit to add

try:
    # Add new audit for a gs1128Template
    api_instance.add_gs1128_template_audit(gs1128_template_id, gs1128_template_audit)
except ApiException as e:
    print("Exception when calling Gs1128TemplateApi->add_gs1128_template_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_template_id** | **int**| Id of the gs1128Template to add an audit to | 
 **gs1128_template_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_gs1128_template_file**
> add_gs1128_template_file(gs1128_template_id, file_name)

Attach a file to a gs1128Template

Adds a file to an existing gs1128Template.

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
api_instance = Infoplus.Gs1128TemplateApi(Infoplus.ApiClient(configuration))
gs1128_template_id = 56 # int | Id of the gs1128Template to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a gs1128Template
    api_instance.add_gs1128_template_file(gs1128_template_id, file_name)
except ApiException as e:
    print("Exception when calling Gs1128TemplateApi->add_gs1128_template_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_template_id** | **int**| Id of the gs1128Template to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_gs1128_template_file_by_url**
> add_gs1128_template_file_by_url(body, gs1128_template_id)

Attach a file to a gs1128Template by URL.

Adds a file to an existing gs1128Template by URL.

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
api_instance = Infoplus.Gs1128TemplateApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
gs1128_template_id = 56 # int | Id of the gs1128Template to add an file to

try:
    # Attach a file to a gs1128Template by URL.
    api_instance.add_gs1128_template_file_by_url(body, gs1128_template_id)
except ApiException as e:
    print("Exception when calling Gs1128TemplateApi->add_gs1128_template_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **gs1128_template_id** | **int**| Id of the gs1128Template to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_gs1128_template_tag**
> add_gs1128_template_tag(gs1128_template_id, gs1128_template_tag)

Add new tags for a gs1128Template.

Adds a tag to an existing gs1128Template.

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
api_instance = Infoplus.Gs1128TemplateApi(Infoplus.ApiClient(configuration))
gs1128_template_id = 56 # int | Id of the gs1128Template to add a tag to
gs1128_template_tag = 'gs1128_template_tag_example' # str | The tag to add

try:
    # Add new tags for a gs1128Template.
    api_instance.add_gs1128_template_tag(gs1128_template_id, gs1128_template_tag)
except ApiException as e:
    print("Exception when calling Gs1128TemplateApi->add_gs1128_template_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_template_id** | **int**| Id of the gs1128Template to add a tag to | 
 **gs1128_template_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gs1128_template**
> delete_gs1128_template(gs1128_template_id)

Delete a gs1128Template

Deletes the gs1128Template identified by the specified id.

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
api_instance = Infoplus.Gs1128TemplateApi(Infoplus.ApiClient(configuration))
gs1128_template_id = 56 # int | Id of the gs1128Template to be deleted.

try:
    # Delete a gs1128Template
    api_instance.delete_gs1128_template(gs1128_template_id)
except ApiException as e:
    print("Exception when calling Gs1128TemplateApi->delete_gs1128_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_template_id** | **int**| Id of the gs1128Template to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gs1128_template_file**
> delete_gs1128_template_file(gs1128_template_id, file_id)

Delete a file for a gs1128Template.

Deletes an existing gs1128Template file using the specified data.

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
api_instance = Infoplus.Gs1128TemplateApi(Infoplus.ApiClient(configuration))
gs1128_template_id = 56 # int | Id of the gs1128Template to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a gs1128Template.
    api_instance.delete_gs1128_template_file(gs1128_template_id, file_id)
except ApiException as e:
    print("Exception when calling Gs1128TemplateApi->delete_gs1128_template_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_template_id** | **int**| Id of the gs1128Template to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gs1128_template_tag**
> delete_gs1128_template_tag(gs1128_template_id, gs1128_template_tag)

Delete a tag for a gs1128Template.

Deletes an existing gs1128Template tag using the specified data.

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
api_instance = Infoplus.Gs1128TemplateApi(Infoplus.ApiClient(configuration))
gs1128_template_id = 56 # int | Id of the gs1128Template to remove tag from
gs1128_template_tag = 'gs1128_template_tag_example' # str | The tag to delete

try:
    # Delete a tag for a gs1128Template.
    api_instance.delete_gs1128_template_tag(gs1128_template_id, gs1128_template_tag)
except ApiException as e:
    print("Exception when calling Gs1128TemplateApi->delete_gs1128_template_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_template_id** | **int**| Id of the gs1128Template to remove tag from | 
 **gs1128_template_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_gs1128_template_by_id**
> Gs1128Template get_duplicate_gs1128_template_by_id(gs1128_template_id)

Get a duplicated a gs1128Template by id

Returns a duplicated gs1128Template identified by the specified id.

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
api_instance = Infoplus.Gs1128TemplateApi(Infoplus.ApiClient(configuration))
gs1128_template_id = 56 # int | Id of the gs1128Template to be duplicated.

try:
    # Get a duplicated a gs1128Template by id
    api_response = api_instance.get_duplicate_gs1128_template_by_id(gs1128_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Gs1128TemplateApi->get_duplicate_gs1128_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_template_id** | **int**| Id of the gs1128Template to be duplicated. | 

### Return type

[**Gs1128Template**](Gs1128Template.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gs1128_template_by_filter**
> list[Gs1128Template] get_gs1128_template_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search gs1128Templates by filter

Returns the list of gs1128Templates that match the given filter.

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
api_instance = Infoplus.Gs1128TemplateApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search gs1128Templates by filter
    api_response = api_instance.get_gs1128_template_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Gs1128TemplateApi->get_gs1128_template_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Gs1128Template]**](Gs1128Template.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gs1128_template_by_id**
> Gs1128Template get_gs1128_template_by_id(gs1128_template_id)

Get a gs1128Template by id

Returns the gs1128Template identified by the specified id.

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
api_instance = Infoplus.Gs1128TemplateApi(Infoplus.ApiClient(configuration))
gs1128_template_id = 56 # int | Id of the gs1128Template to be returned.

try:
    # Get a gs1128Template by id
    api_response = api_instance.get_gs1128_template_by_id(gs1128_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Gs1128TemplateApi->get_gs1128_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_template_id** | **int**| Id of the gs1128Template to be returned. | 

### Return type

[**Gs1128Template**](Gs1128Template.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gs1128_template_files**
> get_gs1128_template_files(gs1128_template_id)

Get the files for a gs1128Template.

Get all existing gs1128Template files.

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
api_instance = Infoplus.Gs1128TemplateApi(Infoplus.ApiClient(configuration))
gs1128_template_id = 56 # int | Id of the gs1128Template to get files for

try:
    # Get the files for a gs1128Template.
    api_instance.get_gs1128_template_files(gs1128_template_id)
except ApiException as e:
    print("Exception when calling Gs1128TemplateApi->get_gs1128_template_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_template_id** | **int**| Id of the gs1128Template to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gs1128_template_tags**
> get_gs1128_template_tags(gs1128_template_id)

Get the tags for a gs1128Template.

Get all existing gs1128Template tags.

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
api_instance = Infoplus.Gs1128TemplateApi(Infoplus.ApiClient(configuration))
gs1128_template_id = 56 # int | Id of the gs1128Template to get tags for

try:
    # Get the tags for a gs1128Template.
    api_instance.get_gs1128_template_tags(gs1128_template_id)
except ApiException as e:
    print("Exception when calling Gs1128TemplateApi->get_gs1128_template_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_template_id** | **int**| Id of the gs1128Template to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gs1128_template**
> update_gs1128_template(body)

Update a gs1128Template

Updates an existing gs1128Template using the specified data.

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
api_instance = Infoplus.Gs1128TemplateApi(Infoplus.ApiClient(configuration))
body = Infoplus.Gs1128Template() # Gs1128Template | Gs1128Template to be updated.

try:
    # Update a gs1128Template
    api_instance.update_gs1128_template(body)
except ApiException as e:
    print("Exception when calling Gs1128TemplateApi->update_gs1128_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Gs1128Template**](Gs1128Template.md)| Gs1128Template to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

