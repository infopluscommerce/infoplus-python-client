# Infoplus.ReplenishmentApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_replenishment_audit**](ReplenishmentApi.md#add_replenishment_audit) | **PUT** /v3.0/replenishment/{replenishmentId}/audit/{replenishmentAudit} | Add new audit for a replenishment
[**add_replenishment_file**](ReplenishmentApi.md#add_replenishment_file) | **POST** /v3.0/replenishment/{replenishmentId}/file/{fileName} | Attach a file to a replenishment
[**add_replenishment_file_by_url**](ReplenishmentApi.md#add_replenishment_file_by_url) | **POST** /v3.0/replenishment/{replenishmentId}/file | Attach a file to a replenishment by URL.
[**add_replenishment_tag**](ReplenishmentApi.md#add_replenishment_tag) | **PUT** /v3.0/replenishment/{replenishmentId}/tag/{replenishmentTag} | Add new tags for a replenishment.
[**delete_replenishment_file**](ReplenishmentApi.md#delete_replenishment_file) | **DELETE** /v3.0/replenishment/{replenishmentId}/file/{fileId} | Delete a file for a replenishment.
[**delete_replenishment_tag**](ReplenishmentApi.md#delete_replenishment_tag) | **DELETE** /v3.0/replenishment/{replenishmentId}/tag/{replenishmentTag} | Delete a tag for a replenishment.
[**get_duplicate_replenishment_by_id**](ReplenishmentApi.md#get_duplicate_replenishment_by_id) | **GET** /v3.0/replenishment/duplicate/{replenishmentId} | Get a duplicated a replenishment by id
[**get_replenishment_by_filter**](ReplenishmentApi.md#get_replenishment_by_filter) | **GET** /v3.0/replenishment/search | Search replenishments by filter
[**get_replenishment_by_id**](ReplenishmentApi.md#get_replenishment_by_id) | **GET** /v3.0/replenishment/{replenishmentId} | Get a replenishment by id
[**get_replenishment_files**](ReplenishmentApi.md#get_replenishment_files) | **GET** /v3.0/replenishment/{replenishmentId}/file | Get the files for a replenishment.
[**get_replenishment_tags**](ReplenishmentApi.md#get_replenishment_tags) | **GET** /v3.0/replenishment/{replenishmentId}/tag | Get the tags for a replenishment.
[**update_replenishment_custom_fields**](ReplenishmentApi.md#update_replenishment_custom_fields) | **PUT** /v3.0/replenishment/customFields | Update a replenishment custom fields


# **add_replenishment_audit**
> add_replenishment_audit(replenishment_id, replenishment_audit)

Add new audit for a replenishment

Adds an audit to an existing replenishment.

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
api_instance = Infoplus.ReplenishmentApi(Infoplus.ApiClient(configuration))
replenishment_id = 56 # int | Id of the replenishment to add an audit to
replenishment_audit = 'replenishment_audit_example' # str | The audit to add

try:
    # Add new audit for a replenishment
    api_instance.add_replenishment_audit(replenishment_id, replenishment_audit)
except ApiException as e:
    print("Exception when calling ReplenishmentApi->add_replenishment_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_id** | **int**| Id of the replenishment to add an audit to | 
 **replenishment_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_replenishment_file**
> add_replenishment_file(replenishment_id, file_name)

Attach a file to a replenishment

Adds a file to an existing replenishment.

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
api_instance = Infoplus.ReplenishmentApi(Infoplus.ApiClient(configuration))
replenishment_id = 56 # int | Id of the replenishment to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a replenishment
    api_instance.add_replenishment_file(replenishment_id, file_name)
except ApiException as e:
    print("Exception when calling ReplenishmentApi->add_replenishment_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_id** | **int**| Id of the replenishment to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_replenishment_file_by_url**
> add_replenishment_file_by_url(body, replenishment_id)

Attach a file to a replenishment by URL.

Adds a file to an existing replenishment by URL.

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
api_instance = Infoplus.ReplenishmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
replenishment_id = 56 # int | Id of the replenishment to add an file to

try:
    # Attach a file to a replenishment by URL.
    api_instance.add_replenishment_file_by_url(body, replenishment_id)
except ApiException as e:
    print("Exception when calling ReplenishmentApi->add_replenishment_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **replenishment_id** | **int**| Id of the replenishment to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_replenishment_tag**
> add_replenishment_tag(replenishment_id, replenishment_tag)

Add new tags for a replenishment.

Adds a tag to an existing replenishment.

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
api_instance = Infoplus.ReplenishmentApi(Infoplus.ApiClient(configuration))
replenishment_id = 56 # int | Id of the replenishment to add a tag to
replenishment_tag = 'replenishment_tag_example' # str | The tag to add

try:
    # Add new tags for a replenishment.
    api_instance.add_replenishment_tag(replenishment_id, replenishment_tag)
except ApiException as e:
    print("Exception when calling ReplenishmentApi->add_replenishment_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_id** | **int**| Id of the replenishment to add a tag to | 
 **replenishment_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_replenishment_file**
> delete_replenishment_file(replenishment_id, file_id)

Delete a file for a replenishment.

Deletes an existing replenishment file using the specified data.

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
api_instance = Infoplus.ReplenishmentApi(Infoplus.ApiClient(configuration))
replenishment_id = 56 # int | Id of the replenishment to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a replenishment.
    api_instance.delete_replenishment_file(replenishment_id, file_id)
except ApiException as e:
    print("Exception when calling ReplenishmentApi->delete_replenishment_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_id** | **int**| Id of the replenishment to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_replenishment_tag**
> delete_replenishment_tag(replenishment_id, replenishment_tag)

Delete a tag for a replenishment.

Deletes an existing replenishment tag using the specified data.

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
api_instance = Infoplus.ReplenishmentApi(Infoplus.ApiClient(configuration))
replenishment_id = 56 # int | Id of the replenishment to remove tag from
replenishment_tag = 'replenishment_tag_example' # str | The tag to delete

try:
    # Delete a tag for a replenishment.
    api_instance.delete_replenishment_tag(replenishment_id, replenishment_tag)
except ApiException as e:
    print("Exception when calling ReplenishmentApi->delete_replenishment_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_id** | **int**| Id of the replenishment to remove tag from | 
 **replenishment_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_replenishment_by_id**
> Replenishment get_duplicate_replenishment_by_id(replenishment_id)

Get a duplicated a replenishment by id

Returns a duplicated replenishment identified by the specified id.

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
api_instance = Infoplus.ReplenishmentApi(Infoplus.ApiClient(configuration))
replenishment_id = 56 # int | Id of the replenishment to be duplicated.

try:
    # Get a duplicated a replenishment by id
    api_response = api_instance.get_duplicate_replenishment_by_id(replenishment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplenishmentApi->get_duplicate_replenishment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_id** | **int**| Id of the replenishment to be duplicated. | 

### Return type

[**Replenishment**](Replenishment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replenishment_by_filter**
> list[Replenishment] get_replenishment_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search replenishments by filter

Returns the list of replenishments that match the given filter.

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
api_instance = Infoplus.ReplenishmentApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search replenishments by filter
    api_response = api_instance.get_replenishment_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplenishmentApi->get_replenishment_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Replenishment]**](Replenishment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replenishment_by_id**
> Replenishment get_replenishment_by_id(replenishment_id)

Get a replenishment by id

Returns the replenishment identified by the specified id.

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
api_instance = Infoplus.ReplenishmentApi(Infoplus.ApiClient(configuration))
replenishment_id = 56 # int | Id of the replenishment to be returned.

try:
    # Get a replenishment by id
    api_response = api_instance.get_replenishment_by_id(replenishment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplenishmentApi->get_replenishment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_id** | **int**| Id of the replenishment to be returned. | 

### Return type

[**Replenishment**](Replenishment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replenishment_files**
> get_replenishment_files(replenishment_id)

Get the files for a replenishment.

Get all existing replenishment files.

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
api_instance = Infoplus.ReplenishmentApi(Infoplus.ApiClient(configuration))
replenishment_id = 56 # int | Id of the replenishment to get files for

try:
    # Get the files for a replenishment.
    api_instance.get_replenishment_files(replenishment_id)
except ApiException as e:
    print("Exception when calling ReplenishmentApi->get_replenishment_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_id** | **int**| Id of the replenishment to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replenishment_tags**
> get_replenishment_tags(replenishment_id)

Get the tags for a replenishment.

Get all existing replenishment tags.

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
api_instance = Infoplus.ReplenishmentApi(Infoplus.ApiClient(configuration))
replenishment_id = 56 # int | Id of the replenishment to get tags for

try:
    # Get the tags for a replenishment.
    api_instance.get_replenishment_tags(replenishment_id)
except ApiException as e:
    print("Exception when calling ReplenishmentApi->get_replenishment_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_id** | **int**| Id of the replenishment to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_replenishment_custom_fields**
> update_replenishment_custom_fields(body)

Update a replenishment custom fields

Updates an existing replenishment custom fields using the specified data.

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
api_instance = Infoplus.ReplenishmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.Replenishment() # Replenishment | Replenishment to be updated.

try:
    # Update a replenishment custom fields
    api_instance.update_replenishment_custom_fields(body)
except ApiException as e:
    print("Exception when calling ReplenishmentApi->update_replenishment_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Replenishment**](Replenishment.md)| Replenishment to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

