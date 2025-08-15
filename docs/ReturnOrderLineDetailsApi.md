# Infoplus.ReturnOrderLineDetailsApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_return_order_line_details_audit**](ReturnOrderLineDetailsApi.md#add_return_order_line_details_audit) | **PUT** /beta/returnOrderLineDetails/{returnOrderLineDetailsId}/audit/{returnOrderLineDetailsAudit} | Add new audit for a returnOrderLineDetails
[**add_return_order_line_details_file**](ReturnOrderLineDetailsApi.md#add_return_order_line_details_file) | **POST** /beta/returnOrderLineDetails/{returnOrderLineDetailsId}/file/{fileName} | Attach a file to a returnOrderLineDetails
[**add_return_order_line_details_file_by_url**](ReturnOrderLineDetailsApi.md#add_return_order_line_details_file_by_url) | **POST** /beta/returnOrderLineDetails/{returnOrderLineDetailsId}/file | Attach a file to a returnOrderLineDetails by URL.
[**add_return_order_line_details_tag**](ReturnOrderLineDetailsApi.md#add_return_order_line_details_tag) | **PUT** /beta/returnOrderLineDetails/{returnOrderLineDetailsId}/tag/{returnOrderLineDetailsTag} | Add new tags for a returnOrderLineDetails.
[**delete_return_order_line_details_file**](ReturnOrderLineDetailsApi.md#delete_return_order_line_details_file) | **DELETE** /beta/returnOrderLineDetails/{returnOrderLineDetailsId}/file/{fileId} | Delete a file for a returnOrderLineDetails.
[**delete_return_order_line_details_tag**](ReturnOrderLineDetailsApi.md#delete_return_order_line_details_tag) | **DELETE** /beta/returnOrderLineDetails/{returnOrderLineDetailsId}/tag/{returnOrderLineDetailsTag} | Delete a tag for a returnOrderLineDetails.
[**get_duplicate_return_order_line_details_by_id**](ReturnOrderLineDetailsApi.md#get_duplicate_return_order_line_details_by_id) | **GET** /beta/returnOrderLineDetails/duplicate/{returnOrderLineDetailsId} | Get a duplicated a returnOrderLineDetails by id
[**get_return_order_line_details_by_filter**](ReturnOrderLineDetailsApi.md#get_return_order_line_details_by_filter) | **GET** /beta/returnOrderLineDetails/search | Search returnOrderLineDetailses by filter
[**get_return_order_line_details_by_id**](ReturnOrderLineDetailsApi.md#get_return_order_line_details_by_id) | **GET** /beta/returnOrderLineDetails/{returnOrderLineDetailsId} | Get a returnOrderLineDetails by id
[**get_return_order_line_details_files**](ReturnOrderLineDetailsApi.md#get_return_order_line_details_files) | **GET** /beta/returnOrderLineDetails/{returnOrderLineDetailsId}/file | Get the files for a returnOrderLineDetails.
[**get_return_order_line_details_tags**](ReturnOrderLineDetailsApi.md#get_return_order_line_details_tags) | **GET** /beta/returnOrderLineDetails/{returnOrderLineDetailsId}/tag | Get the tags for a returnOrderLineDetails.
[**update_return_order_line_details_custom_fields**](ReturnOrderLineDetailsApi.md#update_return_order_line_details_custom_fields) | **PUT** /beta/returnOrderLineDetails/customFields | Update a returnOrderLineDetails custom fields


# **add_return_order_line_details_audit**
> add_return_order_line_details_audit(return_order_line_details_id, return_order_line_details_audit)

Add new audit for a returnOrderLineDetails

Adds an audit to an existing returnOrderLineDetails.

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
api_instance = Infoplus.ReturnOrderLineDetailsApi(Infoplus.ApiClient(configuration))
return_order_line_details_id = 56 # int | Id of the returnOrderLineDetails to add an audit to
return_order_line_details_audit = 'return_order_line_details_audit_example' # str | The audit to add

try:
    # Add new audit for a returnOrderLineDetails
    api_instance.add_return_order_line_details_audit(return_order_line_details_id, return_order_line_details_audit)
except ApiException as e:
    print("Exception when calling ReturnOrderLineDetailsApi->add_return_order_line_details_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_details_id** | **int**| Id of the returnOrderLineDetails to add an audit to | 
 **return_order_line_details_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_return_order_line_details_file**
> add_return_order_line_details_file(return_order_line_details_id, file_name)

Attach a file to a returnOrderLineDetails

Adds a file to an existing returnOrderLineDetails.

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
api_instance = Infoplus.ReturnOrderLineDetailsApi(Infoplus.ApiClient(configuration))
return_order_line_details_id = 56 # int | Id of the returnOrderLineDetails to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a returnOrderLineDetails
    api_instance.add_return_order_line_details_file(return_order_line_details_id, file_name)
except ApiException as e:
    print("Exception when calling ReturnOrderLineDetailsApi->add_return_order_line_details_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_details_id** | **int**| Id of the returnOrderLineDetails to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_return_order_line_details_file_by_url**
> add_return_order_line_details_file_by_url(body, return_order_line_details_id)

Attach a file to a returnOrderLineDetails by URL.

Adds a file to an existing returnOrderLineDetails by URL.

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
api_instance = Infoplus.ReturnOrderLineDetailsApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
return_order_line_details_id = 56 # int | Id of the returnOrderLineDetails to add an file to

try:
    # Attach a file to a returnOrderLineDetails by URL.
    api_instance.add_return_order_line_details_file_by_url(body, return_order_line_details_id)
except ApiException as e:
    print("Exception when calling ReturnOrderLineDetailsApi->add_return_order_line_details_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **return_order_line_details_id** | **int**| Id of the returnOrderLineDetails to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_return_order_line_details_tag**
> add_return_order_line_details_tag(return_order_line_details_id, return_order_line_details_tag)

Add new tags for a returnOrderLineDetails.

Adds a tag to an existing returnOrderLineDetails.

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
api_instance = Infoplus.ReturnOrderLineDetailsApi(Infoplus.ApiClient(configuration))
return_order_line_details_id = 56 # int | Id of the returnOrderLineDetails to add a tag to
return_order_line_details_tag = 'return_order_line_details_tag_example' # str | The tag to add

try:
    # Add new tags for a returnOrderLineDetails.
    api_instance.add_return_order_line_details_tag(return_order_line_details_id, return_order_line_details_tag)
except ApiException as e:
    print("Exception when calling ReturnOrderLineDetailsApi->add_return_order_line_details_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_details_id** | **int**| Id of the returnOrderLineDetails to add a tag to | 
 **return_order_line_details_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_return_order_line_details_file**
> delete_return_order_line_details_file(return_order_line_details_id, file_id)

Delete a file for a returnOrderLineDetails.

Deletes an existing returnOrderLineDetails file using the specified data.

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
api_instance = Infoplus.ReturnOrderLineDetailsApi(Infoplus.ApiClient(configuration))
return_order_line_details_id = 56 # int | Id of the returnOrderLineDetails to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a returnOrderLineDetails.
    api_instance.delete_return_order_line_details_file(return_order_line_details_id, file_id)
except ApiException as e:
    print("Exception when calling ReturnOrderLineDetailsApi->delete_return_order_line_details_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_details_id** | **int**| Id of the returnOrderLineDetails to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_return_order_line_details_tag**
> delete_return_order_line_details_tag(return_order_line_details_id, return_order_line_details_tag)

Delete a tag for a returnOrderLineDetails.

Deletes an existing returnOrderLineDetails tag using the specified data.

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
api_instance = Infoplus.ReturnOrderLineDetailsApi(Infoplus.ApiClient(configuration))
return_order_line_details_id = 56 # int | Id of the returnOrderLineDetails to remove tag from
return_order_line_details_tag = 'return_order_line_details_tag_example' # str | The tag to delete

try:
    # Delete a tag for a returnOrderLineDetails.
    api_instance.delete_return_order_line_details_tag(return_order_line_details_id, return_order_line_details_tag)
except ApiException as e:
    print("Exception when calling ReturnOrderLineDetailsApi->delete_return_order_line_details_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_details_id** | **int**| Id of the returnOrderLineDetails to remove tag from | 
 **return_order_line_details_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_return_order_line_details_by_id**
> ReturnOrderLineDetails get_duplicate_return_order_line_details_by_id(return_order_line_details_id)

Get a duplicated a returnOrderLineDetails by id

Returns a duplicated returnOrderLineDetails identified by the specified id.

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
api_instance = Infoplus.ReturnOrderLineDetailsApi(Infoplus.ApiClient(configuration))
return_order_line_details_id = 56 # int | Id of the returnOrderLineDetails to be duplicated.

try:
    # Get a duplicated a returnOrderLineDetails by id
    api_response = api_instance.get_duplicate_return_order_line_details_by_id(return_order_line_details_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnOrderLineDetailsApi->get_duplicate_return_order_line_details_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_details_id** | **int**| Id of the returnOrderLineDetails to be duplicated. | 

### Return type

[**ReturnOrderLineDetails**](ReturnOrderLineDetails.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_order_line_details_by_filter**
> list[ReturnOrderLineDetails] get_return_order_line_details_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search returnOrderLineDetailses by filter

Returns the list of returnOrderLineDetailses that match the given filter.

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
api_instance = Infoplus.ReturnOrderLineDetailsApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search returnOrderLineDetailses by filter
    api_response = api_instance.get_return_order_line_details_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnOrderLineDetailsApi->get_return_order_line_details_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ReturnOrderLineDetails]**](ReturnOrderLineDetails.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_order_line_details_by_id**
> ReturnOrderLineDetails get_return_order_line_details_by_id(return_order_line_details_id)

Get a returnOrderLineDetails by id

Returns the returnOrderLineDetails identified by the specified id.

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
api_instance = Infoplus.ReturnOrderLineDetailsApi(Infoplus.ApiClient(configuration))
return_order_line_details_id = 56 # int | Id of the returnOrderLineDetails to be returned.

try:
    # Get a returnOrderLineDetails by id
    api_response = api_instance.get_return_order_line_details_by_id(return_order_line_details_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnOrderLineDetailsApi->get_return_order_line_details_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_details_id** | **int**| Id of the returnOrderLineDetails to be returned. | 

### Return type

[**ReturnOrderLineDetails**](ReturnOrderLineDetails.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_order_line_details_files**
> get_return_order_line_details_files(return_order_line_details_id)

Get the files for a returnOrderLineDetails.

Get all existing returnOrderLineDetails files.

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
api_instance = Infoplus.ReturnOrderLineDetailsApi(Infoplus.ApiClient(configuration))
return_order_line_details_id = 56 # int | Id of the returnOrderLineDetails to get files for

try:
    # Get the files for a returnOrderLineDetails.
    api_instance.get_return_order_line_details_files(return_order_line_details_id)
except ApiException as e:
    print("Exception when calling ReturnOrderLineDetailsApi->get_return_order_line_details_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_details_id** | **int**| Id of the returnOrderLineDetails to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_order_line_details_tags**
> get_return_order_line_details_tags(return_order_line_details_id)

Get the tags for a returnOrderLineDetails.

Get all existing returnOrderLineDetails tags.

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
api_instance = Infoplus.ReturnOrderLineDetailsApi(Infoplus.ApiClient(configuration))
return_order_line_details_id = 56 # int | Id of the returnOrderLineDetails to get tags for

try:
    # Get the tags for a returnOrderLineDetails.
    api_instance.get_return_order_line_details_tags(return_order_line_details_id)
except ApiException as e:
    print("Exception when calling ReturnOrderLineDetailsApi->get_return_order_line_details_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_order_line_details_id** | **int**| Id of the returnOrderLineDetails to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_return_order_line_details_custom_fields**
> update_return_order_line_details_custom_fields(body)

Update a returnOrderLineDetails custom fields

Updates an existing returnOrderLineDetails custom fields using the specified data.

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
api_instance = Infoplus.ReturnOrderLineDetailsApi(Infoplus.ApiClient(configuration))
body = Infoplus.ReturnOrderLineDetails() # ReturnOrderLineDetails | ReturnOrderLineDetails to be updated.

try:
    # Update a returnOrderLineDetails custom fields
    api_instance.update_return_order_line_details_custom_fields(body)
except ApiException as e:
    print("Exception when calling ReturnOrderLineDetailsApi->update_return_order_line_details_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReturnOrderLineDetails**](ReturnOrderLineDetails.md)| ReturnOrderLineDetails to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

