# Infoplus.PackingPlanDetailApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_packing_plan_detail_audit**](PackingPlanDetailApi.md#add_packing_plan_detail_audit) | **PUT** /beta/packingPlanDetail/{packingPlanDetailId}/audit/{packingPlanDetailAudit} | Add new audit for a packingPlanDetail
[**add_packing_plan_detail_file**](PackingPlanDetailApi.md#add_packing_plan_detail_file) | **POST** /beta/packingPlanDetail/{packingPlanDetailId}/file/{fileName} | Attach a file to a packingPlanDetail
[**add_packing_plan_detail_file_by_url**](PackingPlanDetailApi.md#add_packing_plan_detail_file_by_url) | **POST** /beta/packingPlanDetail/{packingPlanDetailId}/file | Attach a file to a packingPlanDetail by URL.
[**add_packing_plan_detail_tag**](PackingPlanDetailApi.md#add_packing_plan_detail_tag) | **PUT** /beta/packingPlanDetail/{packingPlanDetailId}/tag/{packingPlanDetailTag} | Add new tags for a packingPlanDetail.
[**delete_packing_plan_detail_file**](PackingPlanDetailApi.md#delete_packing_plan_detail_file) | **DELETE** /beta/packingPlanDetail/{packingPlanDetailId}/file/{fileId} | Delete a file for a packingPlanDetail.
[**delete_packing_plan_detail_tag**](PackingPlanDetailApi.md#delete_packing_plan_detail_tag) | **DELETE** /beta/packingPlanDetail/{packingPlanDetailId}/tag/{packingPlanDetailTag} | Delete a tag for a packingPlanDetail.
[**get_duplicate_packing_plan_detail_by_id**](PackingPlanDetailApi.md#get_duplicate_packing_plan_detail_by_id) | **GET** /beta/packingPlanDetail/duplicate/{packingPlanDetailId} | Get a duplicated a packingPlanDetail by id
[**get_packing_plan_detail_by_filter**](PackingPlanDetailApi.md#get_packing_plan_detail_by_filter) | **GET** /beta/packingPlanDetail/search | Search packingPlanDetails by filter
[**get_packing_plan_detail_by_id**](PackingPlanDetailApi.md#get_packing_plan_detail_by_id) | **GET** /beta/packingPlanDetail/{packingPlanDetailId} | Get a packingPlanDetail by id
[**get_packing_plan_detail_files**](PackingPlanDetailApi.md#get_packing_plan_detail_files) | **GET** /beta/packingPlanDetail/{packingPlanDetailId}/file | Get the files for a packingPlanDetail.
[**get_packing_plan_detail_tags**](PackingPlanDetailApi.md#get_packing_plan_detail_tags) | **GET** /beta/packingPlanDetail/{packingPlanDetailId}/tag | Get the tags for a packingPlanDetail.
[**update_packing_plan_detail_custom_fields**](PackingPlanDetailApi.md#update_packing_plan_detail_custom_fields) | **PUT** /beta/packingPlanDetail/customFields | Update a packingPlanDetail custom fields


# **add_packing_plan_detail_audit**
> add_packing_plan_detail_audit(packing_plan_detail_id, packing_plan_detail_audit)

Add new audit for a packingPlanDetail

Adds an audit to an existing packingPlanDetail.

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
api_instance = Infoplus.PackingPlanDetailApi(Infoplus.ApiClient(configuration))
packing_plan_detail_id = 56 # int | Id of the packingPlanDetail to add an audit to
packing_plan_detail_audit = 'packing_plan_detail_audit_example' # str | The audit to add

try:
    # Add new audit for a packingPlanDetail
    api_instance.add_packing_plan_detail_audit(packing_plan_detail_id, packing_plan_detail_audit)
except ApiException as e:
    print("Exception when calling PackingPlanDetailApi->add_packing_plan_detail_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_detail_id** | **int**| Id of the packingPlanDetail to add an audit to | 
 **packing_plan_detail_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_packing_plan_detail_file**
> add_packing_plan_detail_file(packing_plan_detail_id, file_name)

Attach a file to a packingPlanDetail

Adds a file to an existing packingPlanDetail.

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
api_instance = Infoplus.PackingPlanDetailApi(Infoplus.ApiClient(configuration))
packing_plan_detail_id = 56 # int | Id of the packingPlanDetail to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a packingPlanDetail
    api_instance.add_packing_plan_detail_file(packing_plan_detail_id, file_name)
except ApiException as e:
    print("Exception when calling PackingPlanDetailApi->add_packing_plan_detail_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_detail_id** | **int**| Id of the packingPlanDetail to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_packing_plan_detail_file_by_url**
> add_packing_plan_detail_file_by_url(body, packing_plan_detail_id)

Attach a file to a packingPlanDetail by URL.

Adds a file to an existing packingPlanDetail by URL.

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
api_instance = Infoplus.PackingPlanDetailApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
packing_plan_detail_id = 56 # int | Id of the packingPlanDetail to add an file to

try:
    # Attach a file to a packingPlanDetail by URL.
    api_instance.add_packing_plan_detail_file_by_url(body, packing_plan_detail_id)
except ApiException as e:
    print("Exception when calling PackingPlanDetailApi->add_packing_plan_detail_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **packing_plan_detail_id** | **int**| Id of the packingPlanDetail to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_packing_plan_detail_tag**
> add_packing_plan_detail_tag(packing_plan_detail_id, packing_plan_detail_tag)

Add new tags for a packingPlanDetail.

Adds a tag to an existing packingPlanDetail.

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
api_instance = Infoplus.PackingPlanDetailApi(Infoplus.ApiClient(configuration))
packing_plan_detail_id = 56 # int | Id of the packingPlanDetail to add a tag to
packing_plan_detail_tag = 'packing_plan_detail_tag_example' # str | The tag to add

try:
    # Add new tags for a packingPlanDetail.
    api_instance.add_packing_plan_detail_tag(packing_plan_detail_id, packing_plan_detail_tag)
except ApiException as e:
    print("Exception when calling PackingPlanDetailApi->add_packing_plan_detail_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_detail_id** | **int**| Id of the packingPlanDetail to add a tag to | 
 **packing_plan_detail_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_packing_plan_detail_file**
> delete_packing_plan_detail_file(packing_plan_detail_id, file_id)

Delete a file for a packingPlanDetail.

Deletes an existing packingPlanDetail file using the specified data.

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
api_instance = Infoplus.PackingPlanDetailApi(Infoplus.ApiClient(configuration))
packing_plan_detail_id = 56 # int | Id of the packingPlanDetail to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a packingPlanDetail.
    api_instance.delete_packing_plan_detail_file(packing_plan_detail_id, file_id)
except ApiException as e:
    print("Exception when calling PackingPlanDetailApi->delete_packing_plan_detail_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_detail_id** | **int**| Id of the packingPlanDetail to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_packing_plan_detail_tag**
> delete_packing_plan_detail_tag(packing_plan_detail_id, packing_plan_detail_tag)

Delete a tag for a packingPlanDetail.

Deletes an existing packingPlanDetail tag using the specified data.

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
api_instance = Infoplus.PackingPlanDetailApi(Infoplus.ApiClient(configuration))
packing_plan_detail_id = 56 # int | Id of the packingPlanDetail to remove tag from
packing_plan_detail_tag = 'packing_plan_detail_tag_example' # str | The tag to delete

try:
    # Delete a tag for a packingPlanDetail.
    api_instance.delete_packing_plan_detail_tag(packing_plan_detail_id, packing_plan_detail_tag)
except ApiException as e:
    print("Exception when calling PackingPlanDetailApi->delete_packing_plan_detail_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_detail_id** | **int**| Id of the packingPlanDetail to remove tag from | 
 **packing_plan_detail_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_packing_plan_detail_by_id**
> PackingPlanDetail get_duplicate_packing_plan_detail_by_id(packing_plan_detail_id)

Get a duplicated a packingPlanDetail by id

Returns a duplicated packingPlanDetail identified by the specified id.

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
api_instance = Infoplus.PackingPlanDetailApi(Infoplus.ApiClient(configuration))
packing_plan_detail_id = 56 # int | Id of the packingPlanDetail to be duplicated.

try:
    # Get a duplicated a packingPlanDetail by id
    api_response = api_instance.get_duplicate_packing_plan_detail_by_id(packing_plan_detail_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackingPlanDetailApi->get_duplicate_packing_plan_detail_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_detail_id** | **int**| Id of the packingPlanDetail to be duplicated. | 

### Return type

[**PackingPlanDetail**](PackingPlanDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packing_plan_detail_by_filter**
> list[PackingPlanDetail] get_packing_plan_detail_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search packingPlanDetails by filter

Returns the list of packingPlanDetails that match the given filter.

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
api_instance = Infoplus.PackingPlanDetailApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search packingPlanDetails by filter
    api_response = api_instance.get_packing_plan_detail_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackingPlanDetailApi->get_packing_plan_detail_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[PackingPlanDetail]**](PackingPlanDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packing_plan_detail_by_id**
> PackingPlanDetail get_packing_plan_detail_by_id(packing_plan_detail_id)

Get a packingPlanDetail by id

Returns the packingPlanDetail identified by the specified id.

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
api_instance = Infoplus.PackingPlanDetailApi(Infoplus.ApiClient(configuration))
packing_plan_detail_id = 56 # int | Id of the packingPlanDetail to be returned.

try:
    # Get a packingPlanDetail by id
    api_response = api_instance.get_packing_plan_detail_by_id(packing_plan_detail_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackingPlanDetailApi->get_packing_plan_detail_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_detail_id** | **int**| Id of the packingPlanDetail to be returned. | 

### Return type

[**PackingPlanDetail**](PackingPlanDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packing_plan_detail_files**
> get_packing_plan_detail_files(packing_plan_detail_id)

Get the files for a packingPlanDetail.

Get all existing packingPlanDetail files.

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
api_instance = Infoplus.PackingPlanDetailApi(Infoplus.ApiClient(configuration))
packing_plan_detail_id = 56 # int | Id of the packingPlanDetail to get files for

try:
    # Get the files for a packingPlanDetail.
    api_instance.get_packing_plan_detail_files(packing_plan_detail_id)
except ApiException as e:
    print("Exception when calling PackingPlanDetailApi->get_packing_plan_detail_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_detail_id** | **int**| Id of the packingPlanDetail to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packing_plan_detail_tags**
> get_packing_plan_detail_tags(packing_plan_detail_id)

Get the tags for a packingPlanDetail.

Get all existing packingPlanDetail tags.

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
api_instance = Infoplus.PackingPlanDetailApi(Infoplus.ApiClient(configuration))
packing_plan_detail_id = 56 # int | Id of the packingPlanDetail to get tags for

try:
    # Get the tags for a packingPlanDetail.
    api_instance.get_packing_plan_detail_tags(packing_plan_detail_id)
except ApiException as e:
    print("Exception when calling PackingPlanDetailApi->get_packing_plan_detail_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_detail_id** | **int**| Id of the packingPlanDetail to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_packing_plan_detail_custom_fields**
> update_packing_plan_detail_custom_fields(body)

Update a packingPlanDetail custom fields

Updates an existing packingPlanDetail custom fields using the specified data.

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
api_instance = Infoplus.PackingPlanDetailApi(Infoplus.ApiClient(configuration))
body = Infoplus.PackingPlanDetail() # PackingPlanDetail | PackingPlanDetail to be updated.

try:
    # Update a packingPlanDetail custom fields
    api_instance.update_packing_plan_detail_custom_fields(body)
except ApiException as e:
    print("Exception when calling PackingPlanDetailApi->update_packing_plan_detail_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PackingPlanDetail**](PackingPlanDetail.md)| PackingPlanDetail to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

