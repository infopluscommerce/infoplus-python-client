# Infoplus.PackingDetailApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_packing_detail_audit**](PackingDetailApi.md#add_packing_detail_audit) | **PUT** /beta/packingDetail/{packingDetailId}/audit/{packingDetailAudit} | Add new audit for a packingDetail
[**add_packing_detail_file**](PackingDetailApi.md#add_packing_detail_file) | **POST** /beta/packingDetail/{packingDetailId}/file/{fileName} | Attach a file to a packingDetail
[**add_packing_detail_file_by_url**](PackingDetailApi.md#add_packing_detail_file_by_url) | **POST** /beta/packingDetail/{packingDetailId}/file | Attach a file to a packingDetail by URL.
[**add_packing_detail_tag**](PackingDetailApi.md#add_packing_detail_tag) | **PUT** /beta/packingDetail/{packingDetailId}/tag/{packingDetailTag} | Add new tags for a packingDetail.
[**delete_packing_detail_file**](PackingDetailApi.md#delete_packing_detail_file) | **DELETE** /beta/packingDetail/{packingDetailId}/file/{fileId} | Delete a file for a packingDetail.
[**delete_packing_detail_tag**](PackingDetailApi.md#delete_packing_detail_tag) | **DELETE** /beta/packingDetail/{packingDetailId}/tag/{packingDetailTag} | Delete a tag for a packingDetail.
[**get_duplicate_packing_detail_by_id**](PackingDetailApi.md#get_duplicate_packing_detail_by_id) | **GET** /beta/packingDetail/duplicate/{packingDetailId} | Get a duplicated a packingDetail by id
[**get_packing_detail_by_filter**](PackingDetailApi.md#get_packing_detail_by_filter) | **GET** /beta/packingDetail/search | Search packingDetails by filter
[**get_packing_detail_by_id**](PackingDetailApi.md#get_packing_detail_by_id) | **GET** /beta/packingDetail/{packingDetailId} | Get a packingDetail by id
[**get_packing_detail_files**](PackingDetailApi.md#get_packing_detail_files) | **GET** /beta/packingDetail/{packingDetailId}/file | Get the files for a packingDetail.
[**get_packing_detail_tags**](PackingDetailApi.md#get_packing_detail_tags) | **GET** /beta/packingDetail/{packingDetailId}/tag | Get the tags for a packingDetail.
[**update_packing_detail_custom_fields**](PackingDetailApi.md#update_packing_detail_custom_fields) | **PUT** /beta/packingDetail/customFields | Update a packingDetail custom fields


# **add_packing_detail_audit**
> add_packing_detail_audit(packing_detail_id, packing_detail_audit)

Add new audit for a packingDetail

Adds an audit to an existing packingDetail.

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
api_instance = Infoplus.PackingDetailApi(Infoplus.ApiClient(configuration))
packing_detail_id = 56 # int | Id of the packingDetail to add an audit to
packing_detail_audit = 'packing_detail_audit_example' # str | The audit to add

try:
    # Add new audit for a packingDetail
    api_instance.add_packing_detail_audit(packing_detail_id, packing_detail_audit)
except ApiException as e:
    print("Exception when calling PackingDetailApi->add_packing_detail_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_detail_id** | **int**| Id of the packingDetail to add an audit to | 
 **packing_detail_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_packing_detail_file**
> add_packing_detail_file(packing_detail_id, file_name)

Attach a file to a packingDetail

Adds a file to an existing packingDetail.

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
api_instance = Infoplus.PackingDetailApi(Infoplus.ApiClient(configuration))
packing_detail_id = 56 # int | Id of the packingDetail to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a packingDetail
    api_instance.add_packing_detail_file(packing_detail_id, file_name)
except ApiException as e:
    print("Exception when calling PackingDetailApi->add_packing_detail_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_detail_id** | **int**| Id of the packingDetail to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_packing_detail_file_by_url**
> add_packing_detail_file_by_url(body, packing_detail_id)

Attach a file to a packingDetail by URL.

Adds a file to an existing packingDetail by URL.

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
api_instance = Infoplus.PackingDetailApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
packing_detail_id = 56 # int | Id of the packingDetail to add an file to

try:
    # Attach a file to a packingDetail by URL.
    api_instance.add_packing_detail_file_by_url(body, packing_detail_id)
except ApiException as e:
    print("Exception when calling PackingDetailApi->add_packing_detail_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **packing_detail_id** | **int**| Id of the packingDetail to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_packing_detail_tag**
> add_packing_detail_tag(packing_detail_id, packing_detail_tag)

Add new tags for a packingDetail.

Adds a tag to an existing packingDetail.

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
api_instance = Infoplus.PackingDetailApi(Infoplus.ApiClient(configuration))
packing_detail_id = 56 # int | Id of the packingDetail to add a tag to
packing_detail_tag = 'packing_detail_tag_example' # str | The tag to add

try:
    # Add new tags for a packingDetail.
    api_instance.add_packing_detail_tag(packing_detail_id, packing_detail_tag)
except ApiException as e:
    print("Exception when calling PackingDetailApi->add_packing_detail_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_detail_id** | **int**| Id of the packingDetail to add a tag to | 
 **packing_detail_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_packing_detail_file**
> delete_packing_detail_file(packing_detail_id, file_id)

Delete a file for a packingDetail.

Deletes an existing packingDetail file using the specified data.

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
api_instance = Infoplus.PackingDetailApi(Infoplus.ApiClient(configuration))
packing_detail_id = 56 # int | Id of the packingDetail to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a packingDetail.
    api_instance.delete_packing_detail_file(packing_detail_id, file_id)
except ApiException as e:
    print("Exception when calling PackingDetailApi->delete_packing_detail_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_detail_id** | **int**| Id of the packingDetail to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_packing_detail_tag**
> delete_packing_detail_tag(packing_detail_id, packing_detail_tag)

Delete a tag for a packingDetail.

Deletes an existing packingDetail tag using the specified data.

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
api_instance = Infoplus.PackingDetailApi(Infoplus.ApiClient(configuration))
packing_detail_id = 56 # int | Id of the packingDetail to remove tag from
packing_detail_tag = 'packing_detail_tag_example' # str | The tag to delete

try:
    # Delete a tag for a packingDetail.
    api_instance.delete_packing_detail_tag(packing_detail_id, packing_detail_tag)
except ApiException as e:
    print("Exception when calling PackingDetailApi->delete_packing_detail_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_detail_id** | **int**| Id of the packingDetail to remove tag from | 
 **packing_detail_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_packing_detail_by_id**
> PackingDetail get_duplicate_packing_detail_by_id(packing_detail_id)

Get a duplicated a packingDetail by id

Returns a duplicated packingDetail identified by the specified id.

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
api_instance = Infoplus.PackingDetailApi(Infoplus.ApiClient(configuration))
packing_detail_id = 56 # int | Id of the packingDetail to be duplicated.

try:
    # Get a duplicated a packingDetail by id
    api_response = api_instance.get_duplicate_packing_detail_by_id(packing_detail_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackingDetailApi->get_duplicate_packing_detail_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_detail_id** | **int**| Id of the packingDetail to be duplicated. | 

### Return type

[**PackingDetail**](PackingDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packing_detail_by_filter**
> list[PackingDetail] get_packing_detail_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search packingDetails by filter

Returns the list of packingDetails that match the given filter.

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
api_instance = Infoplus.PackingDetailApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search packingDetails by filter
    api_response = api_instance.get_packing_detail_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackingDetailApi->get_packing_detail_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[PackingDetail]**](PackingDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packing_detail_by_id**
> PackingDetail get_packing_detail_by_id(packing_detail_id)

Get a packingDetail by id

Returns the packingDetail identified by the specified id.

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
api_instance = Infoplus.PackingDetailApi(Infoplus.ApiClient(configuration))
packing_detail_id = 56 # int | Id of the packingDetail to be returned.

try:
    # Get a packingDetail by id
    api_response = api_instance.get_packing_detail_by_id(packing_detail_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackingDetailApi->get_packing_detail_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_detail_id** | **int**| Id of the packingDetail to be returned. | 

### Return type

[**PackingDetail**](PackingDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packing_detail_files**
> get_packing_detail_files(packing_detail_id)

Get the files for a packingDetail.

Get all existing packingDetail files.

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
api_instance = Infoplus.PackingDetailApi(Infoplus.ApiClient(configuration))
packing_detail_id = 56 # int | Id of the packingDetail to get files for

try:
    # Get the files for a packingDetail.
    api_instance.get_packing_detail_files(packing_detail_id)
except ApiException as e:
    print("Exception when calling PackingDetailApi->get_packing_detail_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_detail_id** | **int**| Id of the packingDetail to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packing_detail_tags**
> get_packing_detail_tags(packing_detail_id)

Get the tags for a packingDetail.

Get all existing packingDetail tags.

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
api_instance = Infoplus.PackingDetailApi(Infoplus.ApiClient(configuration))
packing_detail_id = 56 # int | Id of the packingDetail to get tags for

try:
    # Get the tags for a packingDetail.
    api_instance.get_packing_detail_tags(packing_detail_id)
except ApiException as e:
    print("Exception when calling PackingDetailApi->get_packing_detail_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_detail_id** | **int**| Id of the packingDetail to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_packing_detail_custom_fields**
> update_packing_detail_custom_fields(body)

Update a packingDetail custom fields

Updates an existing packingDetail custom fields using the specified data.

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
api_instance = Infoplus.PackingDetailApi(Infoplus.ApiClient(configuration))
body = Infoplus.PackingDetail() # PackingDetail | PackingDetail to be updated.

try:
    # Update a packingDetail custom fields
    api_instance.update_packing_detail_custom_fields(body)
except ApiException as e:
    print("Exception when calling PackingDetailApi->update_packing_detail_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PackingDetail**](PackingDetail.md)| PackingDetail to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

