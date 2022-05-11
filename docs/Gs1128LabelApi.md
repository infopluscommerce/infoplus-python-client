# Infoplus.Gs1128LabelApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_gs1128_label_audit**](Gs1128LabelApi.md#add_gs1128_label_audit) | **PUT** /v3.0/gs1128Label/{gs1128LabelId}/audit/{gs1128LabelAudit} | Add new audit for a gs1128Label
[**add_gs1128_label_file**](Gs1128LabelApi.md#add_gs1128_label_file) | **POST** /v3.0/gs1128Label/{gs1128LabelId}/file/{fileName} | Attach a file to a gs1128Label
[**add_gs1128_label_file_by_url**](Gs1128LabelApi.md#add_gs1128_label_file_by_url) | **POST** /v3.0/gs1128Label/{gs1128LabelId}/file | Attach a file to a gs1128Label by URL.
[**add_gs1128_label_tag**](Gs1128LabelApi.md#add_gs1128_label_tag) | **PUT** /v3.0/gs1128Label/{gs1128LabelId}/tag/{gs1128LabelTag} | Add new tags for a gs1128Label.
[**delete_gs1128_label**](Gs1128LabelApi.md#delete_gs1128_label) | **DELETE** /v3.0/gs1128Label/{gs1128LabelId} | Delete a gs1128Label
[**delete_gs1128_label_file**](Gs1128LabelApi.md#delete_gs1128_label_file) | **DELETE** /v3.0/gs1128Label/{gs1128LabelId}/file/{fileId} | Delete a file for a gs1128Label.
[**delete_gs1128_label_tag**](Gs1128LabelApi.md#delete_gs1128_label_tag) | **DELETE** /v3.0/gs1128Label/{gs1128LabelId}/tag/{gs1128LabelTag} | Delete a tag for a gs1128Label.
[**get_duplicate_gs1128_label_by_id**](Gs1128LabelApi.md#get_duplicate_gs1128_label_by_id) | **GET** /v3.0/gs1128Label/duplicate/{gs1128LabelId} | Get a duplicated a gs1128Label by id
[**get_gs1128_label_by_filter**](Gs1128LabelApi.md#get_gs1128_label_by_filter) | **GET** /v3.0/gs1128Label/search | Search gs1128Labels by filter
[**get_gs1128_label_by_id**](Gs1128LabelApi.md#get_gs1128_label_by_id) | **GET** /v3.0/gs1128Label/{gs1128LabelId} | Get a gs1128Label by id
[**get_gs1128_label_files**](Gs1128LabelApi.md#get_gs1128_label_files) | **GET** /v3.0/gs1128Label/{gs1128LabelId}/file | Get the files for a gs1128Label.
[**get_gs1128_label_tags**](Gs1128LabelApi.md#get_gs1128_label_tags) | **GET** /v3.0/gs1128Label/{gs1128LabelId}/tag | Get the tags for a gs1128Label.
[**update_gs1128_label_custom_fields**](Gs1128LabelApi.md#update_gs1128_label_custom_fields) | **PUT** /v3.0/gs1128Label/customFields | Update a gs1128Label custom fields


# **add_gs1128_label_audit**
> add_gs1128_label_audit(gs1128_label_id, gs1128_label_audit)

Add new audit for a gs1128Label

Adds an audit to an existing gs1128Label.

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
api_instance = Infoplus.Gs1128LabelApi(Infoplus.ApiClient(configuration))
gs1128_label_id = 56 # int | Id of the gs1128Label to add an audit to
gs1128_label_audit = 'gs1128_label_audit_example' # str | The audit to add

try:
    # Add new audit for a gs1128Label
    api_instance.add_gs1128_label_audit(gs1128_label_id, gs1128_label_audit)
except ApiException as e:
    print("Exception when calling Gs1128LabelApi->add_gs1128_label_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_label_id** | **int**| Id of the gs1128Label to add an audit to | 
 **gs1128_label_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_gs1128_label_file**
> add_gs1128_label_file(gs1128_label_id, file_name)

Attach a file to a gs1128Label

Adds a file to an existing gs1128Label.

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
api_instance = Infoplus.Gs1128LabelApi(Infoplus.ApiClient(configuration))
gs1128_label_id = 56 # int | Id of the gs1128Label to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a gs1128Label
    api_instance.add_gs1128_label_file(gs1128_label_id, file_name)
except ApiException as e:
    print("Exception when calling Gs1128LabelApi->add_gs1128_label_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_label_id** | **int**| Id of the gs1128Label to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_gs1128_label_file_by_url**
> add_gs1128_label_file_by_url(body, gs1128_label_id)

Attach a file to a gs1128Label by URL.

Adds a file to an existing gs1128Label by URL.

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
api_instance = Infoplus.Gs1128LabelApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
gs1128_label_id = 56 # int | Id of the gs1128Label to add an file to

try:
    # Attach a file to a gs1128Label by URL.
    api_instance.add_gs1128_label_file_by_url(body, gs1128_label_id)
except ApiException as e:
    print("Exception when calling Gs1128LabelApi->add_gs1128_label_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **gs1128_label_id** | **int**| Id of the gs1128Label to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_gs1128_label_tag**
> add_gs1128_label_tag(gs1128_label_id, gs1128_label_tag)

Add new tags for a gs1128Label.

Adds a tag to an existing gs1128Label.

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
api_instance = Infoplus.Gs1128LabelApi(Infoplus.ApiClient(configuration))
gs1128_label_id = 56 # int | Id of the gs1128Label to add a tag to
gs1128_label_tag = 'gs1128_label_tag_example' # str | The tag to add

try:
    # Add new tags for a gs1128Label.
    api_instance.add_gs1128_label_tag(gs1128_label_id, gs1128_label_tag)
except ApiException as e:
    print("Exception when calling Gs1128LabelApi->add_gs1128_label_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_label_id** | **int**| Id of the gs1128Label to add a tag to | 
 **gs1128_label_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gs1128_label**
> delete_gs1128_label(gs1128_label_id)

Delete a gs1128Label

Deletes the gs1128Label identified by the specified id.

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
api_instance = Infoplus.Gs1128LabelApi(Infoplus.ApiClient(configuration))
gs1128_label_id = 56 # int | Id of the gs1128Label to be deleted.

try:
    # Delete a gs1128Label
    api_instance.delete_gs1128_label(gs1128_label_id)
except ApiException as e:
    print("Exception when calling Gs1128LabelApi->delete_gs1128_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_label_id** | **int**| Id of the gs1128Label to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gs1128_label_file**
> delete_gs1128_label_file(gs1128_label_id, file_id)

Delete a file for a gs1128Label.

Deletes an existing gs1128Label file using the specified data.

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
api_instance = Infoplus.Gs1128LabelApi(Infoplus.ApiClient(configuration))
gs1128_label_id = 56 # int | Id of the gs1128Label to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a gs1128Label.
    api_instance.delete_gs1128_label_file(gs1128_label_id, file_id)
except ApiException as e:
    print("Exception when calling Gs1128LabelApi->delete_gs1128_label_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_label_id** | **int**| Id of the gs1128Label to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gs1128_label_tag**
> delete_gs1128_label_tag(gs1128_label_id, gs1128_label_tag)

Delete a tag for a gs1128Label.

Deletes an existing gs1128Label tag using the specified data.

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
api_instance = Infoplus.Gs1128LabelApi(Infoplus.ApiClient(configuration))
gs1128_label_id = 56 # int | Id of the gs1128Label to remove tag from
gs1128_label_tag = 'gs1128_label_tag_example' # str | The tag to delete

try:
    # Delete a tag for a gs1128Label.
    api_instance.delete_gs1128_label_tag(gs1128_label_id, gs1128_label_tag)
except ApiException as e:
    print("Exception when calling Gs1128LabelApi->delete_gs1128_label_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_label_id** | **int**| Id of the gs1128Label to remove tag from | 
 **gs1128_label_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_gs1128_label_by_id**
> GS1128Label get_duplicate_gs1128_label_by_id(gs1128_label_id)

Get a duplicated a gs1128Label by id

Returns a duplicated gs1128Label identified by the specified id.

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
api_instance = Infoplus.Gs1128LabelApi(Infoplus.ApiClient(configuration))
gs1128_label_id = 56 # int | Id of the gs1128Label to be duplicated.

try:
    # Get a duplicated a gs1128Label by id
    api_response = api_instance.get_duplicate_gs1128_label_by_id(gs1128_label_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Gs1128LabelApi->get_duplicate_gs1128_label_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_label_id** | **int**| Id of the gs1128Label to be duplicated. | 

### Return type

[**GS1128Label**](GS1128Label.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gs1128_label_by_filter**
> list[GS1128Label] get_gs1128_label_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search gs1128Labels by filter

Returns the list of gs1128Labels that match the given filter.

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
api_instance = Infoplus.Gs1128LabelApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search gs1128Labels by filter
    api_response = api_instance.get_gs1128_label_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Gs1128LabelApi->get_gs1128_label_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[GS1128Label]**](GS1128Label.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gs1128_label_by_id**
> GS1128Label get_gs1128_label_by_id(gs1128_label_id)

Get a gs1128Label by id

Returns the gs1128Label identified by the specified id.

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
api_instance = Infoplus.Gs1128LabelApi(Infoplus.ApiClient(configuration))
gs1128_label_id = 56 # int | Id of the gs1128Label to be returned.

try:
    # Get a gs1128Label by id
    api_response = api_instance.get_gs1128_label_by_id(gs1128_label_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Gs1128LabelApi->get_gs1128_label_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_label_id** | **int**| Id of the gs1128Label to be returned. | 

### Return type

[**GS1128Label**](GS1128Label.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gs1128_label_files**
> get_gs1128_label_files(gs1128_label_id)

Get the files for a gs1128Label.

Get all existing gs1128Label files.

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
api_instance = Infoplus.Gs1128LabelApi(Infoplus.ApiClient(configuration))
gs1128_label_id = 56 # int | Id of the gs1128Label to get files for

try:
    # Get the files for a gs1128Label.
    api_instance.get_gs1128_label_files(gs1128_label_id)
except ApiException as e:
    print("Exception when calling Gs1128LabelApi->get_gs1128_label_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_label_id** | **int**| Id of the gs1128Label to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gs1128_label_tags**
> get_gs1128_label_tags(gs1128_label_id)

Get the tags for a gs1128Label.

Get all existing gs1128Label tags.

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
api_instance = Infoplus.Gs1128LabelApi(Infoplus.ApiClient(configuration))
gs1128_label_id = 56 # int | Id of the gs1128Label to get tags for

try:
    # Get the tags for a gs1128Label.
    api_instance.get_gs1128_label_tags(gs1128_label_id)
except ApiException as e:
    print("Exception when calling Gs1128LabelApi->get_gs1128_label_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gs1128_label_id** | **int**| Id of the gs1128Label to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gs1128_label_custom_fields**
> update_gs1128_label_custom_fields(body)

Update a gs1128Label custom fields

Updates an existing gs1128Label custom fields using the specified data.

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
api_instance = Infoplus.Gs1128LabelApi(Infoplus.ApiClient(configuration))
body = Infoplus.GS1128Label() # GS1128Label | Gs1128Label to be updated.

try:
    # Update a gs1128Label custom fields
    api_instance.update_gs1128_label_custom_fields(body)
except ApiException as e:
    print("Exception when calling Gs1128LabelApi->update_gs1128_label_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GS1128Label**](GS1128Label.md)| Gs1128Label to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

