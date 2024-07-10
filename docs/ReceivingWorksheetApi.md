# Infoplus.ReceivingWorksheetApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_receiving_worksheet**](ReceivingWorksheetApi.md#add_receiving_worksheet) | **POST** /beta/receivingWorksheet | Create a receivingWorksheet
[**add_receiving_worksheet_audit**](ReceivingWorksheetApi.md#add_receiving_worksheet_audit) | **PUT** /beta/receivingWorksheet/{receivingWorksheetId}/audit/{receivingWorksheetAudit} | Add new audit for a receivingWorksheet
[**add_receiving_worksheet_file**](ReceivingWorksheetApi.md#add_receiving_worksheet_file) | **POST** /beta/receivingWorksheet/{receivingWorksheetId}/file/{fileName} | Attach a file to a receivingWorksheet
[**add_receiving_worksheet_file_by_url**](ReceivingWorksheetApi.md#add_receiving_worksheet_file_by_url) | **POST** /beta/receivingWorksheet/{receivingWorksheetId}/file | Attach a file to a receivingWorksheet by URL.
[**add_receiving_worksheet_tag**](ReceivingWorksheetApi.md#add_receiving_worksheet_tag) | **PUT** /beta/receivingWorksheet/{receivingWorksheetId}/tag/{receivingWorksheetTag} | Add new tags for a receivingWorksheet.
[**delete_receiving_worksheet**](ReceivingWorksheetApi.md#delete_receiving_worksheet) | **DELETE** /beta/receivingWorksheet/{receivingWorksheetId} | Delete a receivingWorksheet
[**delete_receiving_worksheet_file**](ReceivingWorksheetApi.md#delete_receiving_worksheet_file) | **DELETE** /beta/receivingWorksheet/{receivingWorksheetId}/file/{fileId} | Delete a file for a receivingWorksheet.
[**delete_receiving_worksheet_tag**](ReceivingWorksheetApi.md#delete_receiving_worksheet_tag) | **DELETE** /beta/receivingWorksheet/{receivingWorksheetId}/tag/{receivingWorksheetTag} | Delete a tag for a receivingWorksheet.
[**get_duplicate_receiving_worksheet_by_id**](ReceivingWorksheetApi.md#get_duplicate_receiving_worksheet_by_id) | **GET** /beta/receivingWorksheet/duplicate/{receivingWorksheetId} | Get a duplicated a receivingWorksheet by id
[**get_receiving_worksheet_by_filter**](ReceivingWorksheetApi.md#get_receiving_worksheet_by_filter) | **GET** /beta/receivingWorksheet/search | Search receivingWorksheets by filter
[**get_receiving_worksheet_by_id**](ReceivingWorksheetApi.md#get_receiving_worksheet_by_id) | **GET** /beta/receivingWorksheet/{receivingWorksheetId} | Get a receivingWorksheet by id
[**get_receiving_worksheet_files**](ReceivingWorksheetApi.md#get_receiving_worksheet_files) | **GET** /beta/receivingWorksheet/{receivingWorksheetId}/file | Get the files for a receivingWorksheet.
[**get_receiving_worksheet_tags**](ReceivingWorksheetApi.md#get_receiving_worksheet_tags) | **GET** /beta/receivingWorksheet/{receivingWorksheetId}/tag | Get the tags for a receivingWorksheet.
[**update_receiving_worksheet**](ReceivingWorksheetApi.md#update_receiving_worksheet) | **PUT** /beta/receivingWorksheet | Update a receivingWorksheet
[**update_receiving_worksheet_custom_fields**](ReceivingWorksheetApi.md#update_receiving_worksheet_custom_fields) | **PUT** /beta/receivingWorksheet/customFields | Update a receivingWorksheet custom fields


# **add_receiving_worksheet**
> ReceivingWorksheet add_receiving_worksheet(body)

Create a receivingWorksheet

Inserts a new receivingWorksheet using the specified data.

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
api_instance = Infoplus.ReceivingWorksheetApi(Infoplus.ApiClient(configuration))
body = Infoplus.ReceivingWorksheet() # ReceivingWorksheet | ReceivingWorksheet to be inserted.

try:
    # Create a receivingWorksheet
    api_response = api_instance.add_receiving_worksheet(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceivingWorksheetApi->add_receiving_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReceivingWorksheet**](ReceivingWorksheet.md)| ReceivingWorksheet to be inserted. | 

### Return type

[**ReceivingWorksheet**](ReceivingWorksheet.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_receiving_worksheet_audit**
> add_receiving_worksheet_audit(receiving_worksheet_id, receiving_worksheet_audit)

Add new audit for a receivingWorksheet

Adds an audit to an existing receivingWorksheet.

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
api_instance = Infoplus.ReceivingWorksheetApi(Infoplus.ApiClient(configuration))
receiving_worksheet_id = 56 # int | Id of the receivingWorksheet to add an audit to
receiving_worksheet_audit = 'receiving_worksheet_audit_example' # str | The audit to add

try:
    # Add new audit for a receivingWorksheet
    api_instance.add_receiving_worksheet_audit(receiving_worksheet_id, receiving_worksheet_audit)
except ApiException as e:
    print("Exception when calling ReceivingWorksheetApi->add_receiving_worksheet_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_worksheet_id** | **int**| Id of the receivingWorksheet to add an audit to | 
 **receiving_worksheet_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_receiving_worksheet_file**
> add_receiving_worksheet_file(receiving_worksheet_id, file_name)

Attach a file to a receivingWorksheet

Adds a file to an existing receivingWorksheet.

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
api_instance = Infoplus.ReceivingWorksheetApi(Infoplus.ApiClient(configuration))
receiving_worksheet_id = 56 # int | Id of the receivingWorksheet to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a receivingWorksheet
    api_instance.add_receiving_worksheet_file(receiving_worksheet_id, file_name)
except ApiException as e:
    print("Exception when calling ReceivingWorksheetApi->add_receiving_worksheet_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_worksheet_id** | **int**| Id of the receivingWorksheet to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_receiving_worksheet_file_by_url**
> add_receiving_worksheet_file_by_url(body, receiving_worksheet_id)

Attach a file to a receivingWorksheet by URL.

Adds a file to an existing receivingWorksheet by URL.

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
api_instance = Infoplus.ReceivingWorksheetApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
receiving_worksheet_id = 56 # int | Id of the receivingWorksheet to add an file to

try:
    # Attach a file to a receivingWorksheet by URL.
    api_instance.add_receiving_worksheet_file_by_url(body, receiving_worksheet_id)
except ApiException as e:
    print("Exception when calling ReceivingWorksheetApi->add_receiving_worksheet_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **receiving_worksheet_id** | **int**| Id of the receivingWorksheet to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_receiving_worksheet_tag**
> add_receiving_worksheet_tag(receiving_worksheet_id, receiving_worksheet_tag)

Add new tags for a receivingWorksheet.

Adds a tag to an existing receivingWorksheet.

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
api_instance = Infoplus.ReceivingWorksheetApi(Infoplus.ApiClient(configuration))
receiving_worksheet_id = 56 # int | Id of the receivingWorksheet to add a tag to
receiving_worksheet_tag = 'receiving_worksheet_tag_example' # str | The tag to add

try:
    # Add new tags for a receivingWorksheet.
    api_instance.add_receiving_worksheet_tag(receiving_worksheet_id, receiving_worksheet_tag)
except ApiException as e:
    print("Exception when calling ReceivingWorksheetApi->add_receiving_worksheet_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_worksheet_id** | **int**| Id of the receivingWorksheet to add a tag to | 
 **receiving_worksheet_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_receiving_worksheet**
> delete_receiving_worksheet(receiving_worksheet_id)

Delete a receivingWorksheet

Deletes the receivingWorksheet identified by the specified id.

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
api_instance = Infoplus.ReceivingWorksheetApi(Infoplus.ApiClient(configuration))
receiving_worksheet_id = 56 # int | Id of the receivingWorksheet to be deleted.

try:
    # Delete a receivingWorksheet
    api_instance.delete_receiving_worksheet(receiving_worksheet_id)
except ApiException as e:
    print("Exception when calling ReceivingWorksheetApi->delete_receiving_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_worksheet_id** | **int**| Id of the receivingWorksheet to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_receiving_worksheet_file**
> delete_receiving_worksheet_file(receiving_worksheet_id, file_id)

Delete a file for a receivingWorksheet.

Deletes an existing receivingWorksheet file using the specified data.

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
api_instance = Infoplus.ReceivingWorksheetApi(Infoplus.ApiClient(configuration))
receiving_worksheet_id = 56 # int | Id of the receivingWorksheet to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a receivingWorksheet.
    api_instance.delete_receiving_worksheet_file(receiving_worksheet_id, file_id)
except ApiException as e:
    print("Exception when calling ReceivingWorksheetApi->delete_receiving_worksheet_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_worksheet_id** | **int**| Id of the receivingWorksheet to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_receiving_worksheet_tag**
> delete_receiving_worksheet_tag(receiving_worksheet_id, receiving_worksheet_tag)

Delete a tag for a receivingWorksheet.

Deletes an existing receivingWorksheet tag using the specified data.

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
api_instance = Infoplus.ReceivingWorksheetApi(Infoplus.ApiClient(configuration))
receiving_worksheet_id = 56 # int | Id of the receivingWorksheet to remove tag from
receiving_worksheet_tag = 'receiving_worksheet_tag_example' # str | The tag to delete

try:
    # Delete a tag for a receivingWorksheet.
    api_instance.delete_receiving_worksheet_tag(receiving_worksheet_id, receiving_worksheet_tag)
except ApiException as e:
    print("Exception when calling ReceivingWorksheetApi->delete_receiving_worksheet_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_worksheet_id** | **int**| Id of the receivingWorksheet to remove tag from | 
 **receiving_worksheet_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_receiving_worksheet_by_id**
> ReceivingWorksheet get_duplicate_receiving_worksheet_by_id(receiving_worksheet_id)

Get a duplicated a receivingWorksheet by id

Returns a duplicated receivingWorksheet identified by the specified id.

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
api_instance = Infoplus.ReceivingWorksheetApi(Infoplus.ApiClient(configuration))
receiving_worksheet_id = 56 # int | Id of the receivingWorksheet to be duplicated.

try:
    # Get a duplicated a receivingWorksheet by id
    api_response = api_instance.get_duplicate_receiving_worksheet_by_id(receiving_worksheet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceivingWorksheetApi->get_duplicate_receiving_worksheet_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_worksheet_id** | **int**| Id of the receivingWorksheet to be duplicated. | 

### Return type

[**ReceivingWorksheet**](ReceivingWorksheet.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receiving_worksheet_by_filter**
> list[ReceivingWorksheet] get_receiving_worksheet_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search receivingWorksheets by filter

Returns the list of receivingWorksheets that match the given filter.

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
api_instance = Infoplus.ReceivingWorksheetApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search receivingWorksheets by filter
    api_response = api_instance.get_receiving_worksheet_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceivingWorksheetApi->get_receiving_worksheet_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ReceivingWorksheet]**](ReceivingWorksheet.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receiving_worksheet_by_id**
> ReceivingWorksheet get_receiving_worksheet_by_id(receiving_worksheet_id)

Get a receivingWorksheet by id

Returns the receivingWorksheet identified by the specified id.

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
api_instance = Infoplus.ReceivingWorksheetApi(Infoplus.ApiClient(configuration))
receiving_worksheet_id = 56 # int | Id of the receivingWorksheet to be returned.

try:
    # Get a receivingWorksheet by id
    api_response = api_instance.get_receiving_worksheet_by_id(receiving_worksheet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceivingWorksheetApi->get_receiving_worksheet_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_worksheet_id** | **int**| Id of the receivingWorksheet to be returned. | 

### Return type

[**ReceivingWorksheet**](ReceivingWorksheet.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receiving_worksheet_files**
> get_receiving_worksheet_files(receiving_worksheet_id)

Get the files for a receivingWorksheet.

Get all existing receivingWorksheet files.

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
api_instance = Infoplus.ReceivingWorksheetApi(Infoplus.ApiClient(configuration))
receiving_worksheet_id = 56 # int | Id of the receivingWorksheet to get files for

try:
    # Get the files for a receivingWorksheet.
    api_instance.get_receiving_worksheet_files(receiving_worksheet_id)
except ApiException as e:
    print("Exception when calling ReceivingWorksheetApi->get_receiving_worksheet_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_worksheet_id** | **int**| Id of the receivingWorksheet to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receiving_worksheet_tags**
> get_receiving_worksheet_tags(receiving_worksheet_id)

Get the tags for a receivingWorksheet.

Get all existing receivingWorksheet tags.

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
api_instance = Infoplus.ReceivingWorksheetApi(Infoplus.ApiClient(configuration))
receiving_worksheet_id = 56 # int | Id of the receivingWorksheet to get tags for

try:
    # Get the tags for a receivingWorksheet.
    api_instance.get_receiving_worksheet_tags(receiving_worksheet_id)
except ApiException as e:
    print("Exception when calling ReceivingWorksheetApi->get_receiving_worksheet_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_worksheet_id** | **int**| Id of the receivingWorksheet to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_receiving_worksheet**
> update_receiving_worksheet(body)

Update a receivingWorksheet

Updates an existing receivingWorksheet using the specified data.

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
api_instance = Infoplus.ReceivingWorksheetApi(Infoplus.ApiClient(configuration))
body = Infoplus.ReceivingWorksheet() # ReceivingWorksheet | ReceivingWorksheet to be updated.

try:
    # Update a receivingWorksheet
    api_instance.update_receiving_worksheet(body)
except ApiException as e:
    print("Exception when calling ReceivingWorksheetApi->update_receiving_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReceivingWorksheet**](ReceivingWorksheet.md)| ReceivingWorksheet to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_receiving_worksheet_custom_fields**
> update_receiving_worksheet_custom_fields(body)

Update a receivingWorksheet custom fields

Updates an existing receivingWorksheet custom fields using the specified data.

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
api_instance = Infoplus.ReceivingWorksheetApi(Infoplus.ApiClient(configuration))
body = Infoplus.ReceivingWorksheet() # ReceivingWorksheet | ReceivingWorksheet to be updated.

try:
    # Update a receivingWorksheet custom fields
    api_instance.update_receiving_worksheet_custom_fields(body)
except ApiException as e:
    print("Exception when calling ReceivingWorksheetApi->update_receiving_worksheet_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReceivingWorksheet**](ReceivingWorksheet.md)| ReceivingWorksheet to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

