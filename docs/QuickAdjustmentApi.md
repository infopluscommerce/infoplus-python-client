# Infoplus.QuickAdjustmentApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_quick_adjustment**](QuickAdjustmentApi.md#add_quick_adjustment) | **POST** /beta/quickAdjustment | Create a quickAdjustment
[**add_quick_adjustment_audit**](QuickAdjustmentApi.md#add_quick_adjustment_audit) | **PUT** /beta/quickAdjustment/{quickAdjustmentId}/audit/{quickAdjustmentAudit} | Add new audit for a quickAdjustment
[**add_quick_adjustment_file**](QuickAdjustmentApi.md#add_quick_adjustment_file) | **POST** /beta/quickAdjustment/{quickAdjustmentId}/file/{fileName} | Attach a file to a quickAdjustment
[**add_quick_adjustment_file_by_url**](QuickAdjustmentApi.md#add_quick_adjustment_file_by_url) | **POST** /beta/quickAdjustment/{quickAdjustmentId}/file | Attach a file to a quickAdjustment by URL.
[**add_quick_adjustment_tag**](QuickAdjustmentApi.md#add_quick_adjustment_tag) | **PUT** /beta/quickAdjustment/{quickAdjustmentId}/tag/{quickAdjustmentTag} | Add new tags for a quickAdjustment.
[**delete_quick_adjustment**](QuickAdjustmentApi.md#delete_quick_adjustment) | **DELETE** /beta/quickAdjustment/{quickAdjustmentId} | Delete a quickAdjustment
[**delete_quick_adjustment_file**](QuickAdjustmentApi.md#delete_quick_adjustment_file) | **DELETE** /beta/quickAdjustment/{quickAdjustmentId}/file/{fileId} | Delete a file for a quickAdjustment.
[**delete_quick_adjustment_tag**](QuickAdjustmentApi.md#delete_quick_adjustment_tag) | **DELETE** /beta/quickAdjustment/{quickAdjustmentId}/tag/{quickAdjustmentTag} | Delete a tag for a quickAdjustment.
[**execute_quick_adjustment**](QuickAdjustmentApi.md#execute_quick_adjustment) | **POST** /beta/quickAdjustment/executeQuickAdjustment | Run the ExecuteQuickAdjustment process.
[**get_duplicate_quick_adjustment_by_id**](QuickAdjustmentApi.md#get_duplicate_quick_adjustment_by_id) | **GET** /beta/quickAdjustment/duplicate/{quickAdjustmentId} | Get a duplicated a quickAdjustment by id
[**get_quick_adjustment_by_filter**](QuickAdjustmentApi.md#get_quick_adjustment_by_filter) | **GET** /beta/quickAdjustment/search | Search quickAdjustments by filter
[**get_quick_adjustment_by_id**](QuickAdjustmentApi.md#get_quick_adjustment_by_id) | **GET** /beta/quickAdjustment/{quickAdjustmentId} | Get a quickAdjustment by id
[**get_quick_adjustment_files**](QuickAdjustmentApi.md#get_quick_adjustment_files) | **GET** /beta/quickAdjustment/{quickAdjustmentId}/file | Get the files for a quickAdjustment.
[**get_quick_adjustment_tags**](QuickAdjustmentApi.md#get_quick_adjustment_tags) | **GET** /beta/quickAdjustment/{quickAdjustmentId}/tag | Get the tags for a quickAdjustment.
[**update_quick_adjustment**](QuickAdjustmentApi.md#update_quick_adjustment) | **PUT** /beta/quickAdjustment | Update a quickAdjustment
[**update_quick_adjustment_custom_fields**](QuickAdjustmentApi.md#update_quick_adjustment_custom_fields) | **PUT** /beta/quickAdjustment/customFields | Update a quickAdjustment custom fields


# **add_quick_adjustment**
> QuickAdjustment add_quick_adjustment(body)

Create a quickAdjustment

Inserts a new quickAdjustment using the specified data.

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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.QuickAdjustment() # QuickAdjustment | QuickAdjustment to be inserted.

try:
    # Create a quickAdjustment
    api_response = api_instance.add_quick_adjustment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->add_quick_adjustment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuickAdjustment**](QuickAdjustment.md)| QuickAdjustment to be inserted. | 

### Return type

[**QuickAdjustment**](QuickAdjustment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_quick_adjustment_audit**
> add_quick_adjustment_audit(quick_adjustment_id, quick_adjustment_audit)

Add new audit for a quickAdjustment

Adds an audit to an existing quickAdjustment.

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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
quick_adjustment_id = 56 # int | Id of the quickAdjustment to add an audit to
quick_adjustment_audit = 'quick_adjustment_audit_example' # str | The audit to add

try:
    # Add new audit for a quickAdjustment
    api_instance.add_quick_adjustment_audit(quick_adjustment_id, quick_adjustment_audit)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->add_quick_adjustment_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_adjustment_id** | **int**| Id of the quickAdjustment to add an audit to | 
 **quick_adjustment_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_quick_adjustment_file**
> add_quick_adjustment_file(quick_adjustment_id, file_name)

Attach a file to a quickAdjustment

Adds a file to an existing quickAdjustment.

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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
quick_adjustment_id = 56 # int | Id of the quickAdjustment to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a quickAdjustment
    api_instance.add_quick_adjustment_file(quick_adjustment_id, file_name)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->add_quick_adjustment_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_adjustment_id** | **int**| Id of the quickAdjustment to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_quick_adjustment_file_by_url**
> add_quick_adjustment_file_by_url(body, quick_adjustment_id)

Attach a file to a quickAdjustment by URL.

Adds a file to an existing quickAdjustment by URL.

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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
quick_adjustment_id = 56 # int | Id of the quickAdjustment to add an file to

try:
    # Attach a file to a quickAdjustment by URL.
    api_instance.add_quick_adjustment_file_by_url(body, quick_adjustment_id)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->add_quick_adjustment_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **quick_adjustment_id** | **int**| Id of the quickAdjustment to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_quick_adjustment_tag**
> add_quick_adjustment_tag(quick_adjustment_id, quick_adjustment_tag)

Add new tags for a quickAdjustment.

Adds a tag to an existing quickAdjustment.

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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
quick_adjustment_id = 56 # int | Id of the quickAdjustment to add a tag to
quick_adjustment_tag = 'quick_adjustment_tag_example' # str | The tag to add

try:
    # Add new tags for a quickAdjustment.
    api_instance.add_quick_adjustment_tag(quick_adjustment_id, quick_adjustment_tag)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->add_quick_adjustment_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_adjustment_id** | **int**| Id of the quickAdjustment to add a tag to | 
 **quick_adjustment_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quick_adjustment**
> delete_quick_adjustment(quick_adjustment_id)

Delete a quickAdjustment

Deletes the quickAdjustment identified by the specified id.

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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
quick_adjustment_id = 56 # int | Id of the quickAdjustment to be deleted.

try:
    # Delete a quickAdjustment
    api_instance.delete_quick_adjustment(quick_adjustment_id)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->delete_quick_adjustment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_adjustment_id** | **int**| Id of the quickAdjustment to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quick_adjustment_file**
> delete_quick_adjustment_file(quick_adjustment_id, file_id)

Delete a file for a quickAdjustment.

Deletes an existing quickAdjustment file using the specified data.

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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
quick_adjustment_id = 56 # int | Id of the quickAdjustment to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a quickAdjustment.
    api_instance.delete_quick_adjustment_file(quick_adjustment_id, file_id)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->delete_quick_adjustment_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_adjustment_id** | **int**| Id of the quickAdjustment to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quick_adjustment_tag**
> delete_quick_adjustment_tag(quick_adjustment_id, quick_adjustment_tag)

Delete a tag for a quickAdjustment.

Deletes an existing quickAdjustment tag using the specified data.

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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
quick_adjustment_id = 56 # int | Id of the quickAdjustment to remove tag from
quick_adjustment_tag = 'quick_adjustment_tag_example' # str | The tag to delete

try:
    # Delete a tag for a quickAdjustment.
    api_instance.delete_quick_adjustment_tag(quick_adjustment_id, quick_adjustment_tag)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->delete_quick_adjustment_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_adjustment_id** | **int**| Id of the quickAdjustment to remove tag from | 
 **quick_adjustment_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_quick_adjustment**
> list[ProcessOutputAPIModel] execute_quick_adjustment(body)

Run the ExecuteQuickAdjustment process.



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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.ExecuteQuickAdjustmentInputAPIModel() # ExecuteQuickAdjustmentInputAPIModel | Input data for ExecuteQuickAdjustment process.

try:
    # Run the ExecuteQuickAdjustment process.
    api_response = api_instance.execute_quick_adjustment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->execute_quick_adjustment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExecuteQuickAdjustmentInputAPIModel**](ExecuteQuickAdjustmentInputAPIModel.md)| Input data for ExecuteQuickAdjustment process. | 

### Return type

[**list[ProcessOutputAPIModel]**](ProcessOutputAPIModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_quick_adjustment_by_id**
> QuickAdjustment get_duplicate_quick_adjustment_by_id(quick_adjustment_id)

Get a duplicated a quickAdjustment by id

Returns a duplicated quickAdjustment identified by the specified id.

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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
quick_adjustment_id = 56 # int | Id of the quickAdjustment to be duplicated.

try:
    # Get a duplicated a quickAdjustment by id
    api_response = api_instance.get_duplicate_quick_adjustment_by_id(quick_adjustment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->get_duplicate_quick_adjustment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_adjustment_id** | **int**| Id of the quickAdjustment to be duplicated. | 

### Return type

[**QuickAdjustment**](QuickAdjustment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quick_adjustment_by_filter**
> list[QuickAdjustment] get_quick_adjustment_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search quickAdjustments by filter

Returns the list of quickAdjustments that match the given filter.

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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search quickAdjustments by filter
    api_response = api_instance.get_quick_adjustment_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->get_quick_adjustment_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[QuickAdjustment]**](QuickAdjustment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quick_adjustment_by_id**
> QuickAdjustment get_quick_adjustment_by_id(quick_adjustment_id)

Get a quickAdjustment by id

Returns the quickAdjustment identified by the specified id.

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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
quick_adjustment_id = 56 # int | Id of the quickAdjustment to be returned.

try:
    # Get a quickAdjustment by id
    api_response = api_instance.get_quick_adjustment_by_id(quick_adjustment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->get_quick_adjustment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_adjustment_id** | **int**| Id of the quickAdjustment to be returned. | 

### Return type

[**QuickAdjustment**](QuickAdjustment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quick_adjustment_files**
> get_quick_adjustment_files(quick_adjustment_id)

Get the files for a quickAdjustment.

Get all existing quickAdjustment files.

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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
quick_adjustment_id = 56 # int | Id of the quickAdjustment to get files for

try:
    # Get the files for a quickAdjustment.
    api_instance.get_quick_adjustment_files(quick_adjustment_id)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->get_quick_adjustment_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_adjustment_id** | **int**| Id of the quickAdjustment to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quick_adjustment_tags**
> get_quick_adjustment_tags(quick_adjustment_id)

Get the tags for a quickAdjustment.

Get all existing quickAdjustment tags.

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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
quick_adjustment_id = 56 # int | Id of the quickAdjustment to get tags for

try:
    # Get the tags for a quickAdjustment.
    api_instance.get_quick_adjustment_tags(quick_adjustment_id)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->get_quick_adjustment_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_adjustment_id** | **int**| Id of the quickAdjustment to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quick_adjustment**
> update_quick_adjustment(body)

Update a quickAdjustment

Updates an existing quickAdjustment using the specified data.

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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.QuickAdjustment() # QuickAdjustment | QuickAdjustment to be updated.

try:
    # Update a quickAdjustment
    api_instance.update_quick_adjustment(body)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->update_quick_adjustment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuickAdjustment**](QuickAdjustment.md)| QuickAdjustment to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quick_adjustment_custom_fields**
> update_quick_adjustment_custom_fields(body)

Update a quickAdjustment custom fields

Updates an existing quickAdjustment custom fields using the specified data.

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
api_instance = Infoplus.QuickAdjustmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.QuickAdjustment() # QuickAdjustment | QuickAdjustment to be updated.

try:
    # Update a quickAdjustment custom fields
    api_instance.update_quick_adjustment_custom_fields(body)
except ApiException as e:
    print("Exception when calling QuickAdjustmentApi->update_quick_adjustment_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuickAdjustment**](QuickAdjustment.md)| QuickAdjustment to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

