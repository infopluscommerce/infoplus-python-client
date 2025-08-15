# Infoplus.DasFeesApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_das_fees**](DasFeesApi.md#add_das_fees) | **POST** /beta/dasFees | Create a dasFees
[**add_das_fees_audit**](DasFeesApi.md#add_das_fees_audit) | **PUT** /beta/dasFees/{dasFeesId}/audit/{dasFeesAudit} | Add new audit for a dasFees
[**add_das_fees_file**](DasFeesApi.md#add_das_fees_file) | **POST** /beta/dasFees/{dasFeesId}/file/{fileName} | Attach a file to a dasFees
[**add_das_fees_file_by_url**](DasFeesApi.md#add_das_fees_file_by_url) | **POST** /beta/dasFees/{dasFeesId}/file | Attach a file to a dasFees by URL.
[**add_das_fees_tag**](DasFeesApi.md#add_das_fees_tag) | **PUT** /beta/dasFees/{dasFeesId}/tag/{dasFeesTag} | Add new tags for a dasFees.
[**delete_das_fees**](DasFeesApi.md#delete_das_fees) | **DELETE** /beta/dasFees/{dasFeesId} | Delete a dasFees
[**delete_das_fees_file**](DasFeesApi.md#delete_das_fees_file) | **DELETE** /beta/dasFees/{dasFeesId}/file/{fileId} | Delete a file for a dasFees.
[**delete_das_fees_tag**](DasFeesApi.md#delete_das_fees_tag) | **DELETE** /beta/dasFees/{dasFeesId}/tag/{dasFeesTag} | Delete a tag for a dasFees.
[**get_das_fees_by_filter**](DasFeesApi.md#get_das_fees_by_filter) | **GET** /beta/dasFees/search | Search dasFeeses by filter
[**get_das_fees_by_id**](DasFeesApi.md#get_das_fees_by_id) | **GET** /beta/dasFees/{dasFeesId} | Get a dasFees by id
[**get_das_fees_files**](DasFeesApi.md#get_das_fees_files) | **GET** /beta/dasFees/{dasFeesId}/file | Get the files for a dasFees.
[**get_das_fees_tags**](DasFeesApi.md#get_das_fees_tags) | **GET** /beta/dasFees/{dasFeesId}/tag | Get the tags for a dasFees.
[**get_duplicate_das_fees_by_id**](DasFeesApi.md#get_duplicate_das_fees_by_id) | **GET** /beta/dasFees/duplicate/{dasFeesId} | Get a duplicated a dasFees by id
[**update_das_fees**](DasFeesApi.md#update_das_fees) | **PUT** /beta/dasFees | Update a dasFees


# **add_das_fees**
> DasFees add_das_fees(body)

Create a dasFees

Inserts a new dasFees using the specified data.

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
api_instance = Infoplus.DasFeesApi(Infoplus.ApiClient(configuration))
body = Infoplus.DasFees() # DasFees | DasFees to be inserted.

try:
    # Create a dasFees
    api_response = api_instance.add_das_fees(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DasFeesApi->add_das_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DasFees**](DasFees.md)| DasFees to be inserted. | 

### Return type

[**DasFees**](DasFees.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_das_fees_audit**
> add_das_fees_audit(das_fees_id, das_fees_audit)

Add new audit for a dasFees

Adds an audit to an existing dasFees.

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
api_instance = Infoplus.DasFeesApi(Infoplus.ApiClient(configuration))
das_fees_id = 56 # int | Id of the dasFees to add an audit to
das_fees_audit = 'das_fees_audit_example' # str | The audit to add

try:
    # Add new audit for a dasFees
    api_instance.add_das_fees_audit(das_fees_id, das_fees_audit)
except ApiException as e:
    print("Exception when calling DasFeesApi->add_das_fees_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **das_fees_id** | **int**| Id of the dasFees to add an audit to | 
 **das_fees_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_das_fees_file**
> add_das_fees_file(das_fees_id, file_name)

Attach a file to a dasFees

Adds a file to an existing dasFees.

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
api_instance = Infoplus.DasFeesApi(Infoplus.ApiClient(configuration))
das_fees_id = 56 # int | Id of the dasFees to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a dasFees
    api_instance.add_das_fees_file(das_fees_id, file_name)
except ApiException as e:
    print("Exception when calling DasFeesApi->add_das_fees_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **das_fees_id** | **int**| Id of the dasFees to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_das_fees_file_by_url**
> add_das_fees_file_by_url(body, das_fees_id)

Attach a file to a dasFees by URL.

Adds a file to an existing dasFees by URL.

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
api_instance = Infoplus.DasFeesApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
das_fees_id = 56 # int | Id of the dasFees to add an file to

try:
    # Attach a file to a dasFees by URL.
    api_instance.add_das_fees_file_by_url(body, das_fees_id)
except ApiException as e:
    print("Exception when calling DasFeesApi->add_das_fees_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **das_fees_id** | **int**| Id of the dasFees to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_das_fees_tag**
> add_das_fees_tag(das_fees_id, das_fees_tag)

Add new tags for a dasFees.

Adds a tag to an existing dasFees.

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
api_instance = Infoplus.DasFeesApi(Infoplus.ApiClient(configuration))
das_fees_id = 56 # int | Id of the dasFees to add a tag to
das_fees_tag = 'das_fees_tag_example' # str | The tag to add

try:
    # Add new tags for a dasFees.
    api_instance.add_das_fees_tag(das_fees_id, das_fees_tag)
except ApiException as e:
    print("Exception when calling DasFeesApi->add_das_fees_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **das_fees_id** | **int**| Id of the dasFees to add a tag to | 
 **das_fees_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_das_fees**
> delete_das_fees(das_fees_id)

Delete a dasFees

Deletes the dasFees identified by the specified id.

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
api_instance = Infoplus.DasFeesApi(Infoplus.ApiClient(configuration))
das_fees_id = 56 # int | Id of the dasFees to be deleted.

try:
    # Delete a dasFees
    api_instance.delete_das_fees(das_fees_id)
except ApiException as e:
    print("Exception when calling DasFeesApi->delete_das_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **das_fees_id** | **int**| Id of the dasFees to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_das_fees_file**
> delete_das_fees_file(das_fees_id, file_id)

Delete a file for a dasFees.

Deletes an existing dasFees file using the specified data.

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
api_instance = Infoplus.DasFeesApi(Infoplus.ApiClient(configuration))
das_fees_id = 56 # int | Id of the dasFees to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a dasFees.
    api_instance.delete_das_fees_file(das_fees_id, file_id)
except ApiException as e:
    print("Exception when calling DasFeesApi->delete_das_fees_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **das_fees_id** | **int**| Id of the dasFees to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_das_fees_tag**
> delete_das_fees_tag(das_fees_id, das_fees_tag)

Delete a tag for a dasFees.

Deletes an existing dasFees tag using the specified data.

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
api_instance = Infoplus.DasFeesApi(Infoplus.ApiClient(configuration))
das_fees_id = 56 # int | Id of the dasFees to remove tag from
das_fees_tag = 'das_fees_tag_example' # str | The tag to delete

try:
    # Delete a tag for a dasFees.
    api_instance.delete_das_fees_tag(das_fees_id, das_fees_tag)
except ApiException as e:
    print("Exception when calling DasFeesApi->delete_das_fees_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **das_fees_id** | **int**| Id of the dasFees to remove tag from | 
 **das_fees_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_das_fees_by_filter**
> list[DasFees] get_das_fees_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search dasFeeses by filter

Returns the list of dasFeeses that match the given filter.

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
api_instance = Infoplus.DasFeesApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search dasFeeses by filter
    api_response = api_instance.get_das_fees_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DasFeesApi->get_das_fees_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[DasFees]**](DasFees.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_das_fees_by_id**
> DasFees get_das_fees_by_id(das_fees_id)

Get a dasFees by id

Returns the dasFees identified by the specified id.

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
api_instance = Infoplus.DasFeesApi(Infoplus.ApiClient(configuration))
das_fees_id = 56 # int | Id of the dasFees to be returned.

try:
    # Get a dasFees by id
    api_response = api_instance.get_das_fees_by_id(das_fees_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DasFeesApi->get_das_fees_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **das_fees_id** | **int**| Id of the dasFees to be returned. | 

### Return type

[**DasFees**](DasFees.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_das_fees_files**
> get_das_fees_files(das_fees_id)

Get the files for a dasFees.

Get all existing dasFees files.

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
api_instance = Infoplus.DasFeesApi(Infoplus.ApiClient(configuration))
das_fees_id = 56 # int | Id of the dasFees to get files for

try:
    # Get the files for a dasFees.
    api_instance.get_das_fees_files(das_fees_id)
except ApiException as e:
    print("Exception when calling DasFeesApi->get_das_fees_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **das_fees_id** | **int**| Id of the dasFees to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_das_fees_tags**
> get_das_fees_tags(das_fees_id)

Get the tags for a dasFees.

Get all existing dasFees tags.

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
api_instance = Infoplus.DasFeesApi(Infoplus.ApiClient(configuration))
das_fees_id = 56 # int | Id of the dasFees to get tags for

try:
    # Get the tags for a dasFees.
    api_instance.get_das_fees_tags(das_fees_id)
except ApiException as e:
    print("Exception when calling DasFeesApi->get_das_fees_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **das_fees_id** | **int**| Id of the dasFees to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_das_fees_by_id**
> DasFees get_duplicate_das_fees_by_id(das_fees_id)

Get a duplicated a dasFees by id

Returns a duplicated dasFees identified by the specified id.

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
api_instance = Infoplus.DasFeesApi(Infoplus.ApiClient(configuration))
das_fees_id = 56 # int | Id of the dasFees to be duplicated.

try:
    # Get a duplicated a dasFees by id
    api_response = api_instance.get_duplicate_das_fees_by_id(das_fees_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DasFeesApi->get_duplicate_das_fees_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **das_fees_id** | **int**| Id of the dasFees to be duplicated. | 

### Return type

[**DasFees**](DasFees.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_das_fees**
> update_das_fees(body)

Update a dasFees

Updates an existing dasFees using the specified data.

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
api_instance = Infoplus.DasFeesApi(Infoplus.ApiClient(configuration))
body = Infoplus.DasFees() # DasFees | DasFees to be updated.

try:
    # Update a dasFees
    api_instance.update_das_fees(body)
except ApiException as e:
    print("Exception when calling DasFeesApi->update_das_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DasFees**](DasFees.md)| DasFees to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

