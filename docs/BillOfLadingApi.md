# Infoplus.BillOfLadingApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bill_of_lading**](BillOfLadingApi.md#add_bill_of_lading) | **POST** /beta/billOfLading | Create a billOfLading
[**add_bill_of_lading_audit**](BillOfLadingApi.md#add_bill_of_lading_audit) | **PUT** /beta/billOfLading/{billOfLadingId}/audit/{billOfLadingAudit} | Add new audit for a billOfLading
[**add_bill_of_lading_file**](BillOfLadingApi.md#add_bill_of_lading_file) | **POST** /beta/billOfLading/{billOfLadingId}/file/{fileName} | Attach a file to a billOfLading
[**add_bill_of_lading_file_by_url**](BillOfLadingApi.md#add_bill_of_lading_file_by_url) | **POST** /beta/billOfLading/{billOfLadingId}/file | Attach a file to a billOfLading by URL.
[**add_bill_of_lading_tag**](BillOfLadingApi.md#add_bill_of_lading_tag) | **PUT** /beta/billOfLading/{billOfLadingId}/tag/{billOfLadingTag} | Add new tags for a billOfLading.
[**delete_bill_of_lading**](BillOfLadingApi.md#delete_bill_of_lading) | **DELETE** /beta/billOfLading/{billOfLadingId} | Delete a billOfLading
[**delete_bill_of_lading_file**](BillOfLadingApi.md#delete_bill_of_lading_file) | **DELETE** /beta/billOfLading/{billOfLadingId}/file/{fileId} | Delete a file for a billOfLading.
[**delete_bill_of_lading_tag**](BillOfLadingApi.md#delete_bill_of_lading_tag) | **DELETE** /beta/billOfLading/{billOfLadingId}/tag/{billOfLadingTag} | Delete a tag for a billOfLading.
[**get_bill_of_lading_by_filter**](BillOfLadingApi.md#get_bill_of_lading_by_filter) | **GET** /beta/billOfLading/search | Search billOfLadings by filter
[**get_bill_of_lading_by_id**](BillOfLadingApi.md#get_bill_of_lading_by_id) | **GET** /beta/billOfLading/{billOfLadingId} | Get a billOfLading by id
[**get_bill_of_lading_files**](BillOfLadingApi.md#get_bill_of_lading_files) | **GET** /beta/billOfLading/{billOfLadingId}/file | Get the files for a billOfLading.
[**get_bill_of_lading_tags**](BillOfLadingApi.md#get_bill_of_lading_tags) | **GET** /beta/billOfLading/{billOfLadingId}/tag | Get the tags for a billOfLading.
[**get_duplicate_bill_of_lading_by_id**](BillOfLadingApi.md#get_duplicate_bill_of_lading_by_id) | **GET** /beta/billOfLading/duplicate/{billOfLadingId} | Get a duplicated a billOfLading by id
[**update_bill_of_lading**](BillOfLadingApi.md#update_bill_of_lading) | **PUT** /beta/billOfLading | Update a billOfLading
[**update_bill_of_lading_custom_fields**](BillOfLadingApi.md#update_bill_of_lading_custom_fields) | **PUT** /beta/billOfLading/customFields | Update a billOfLading custom fields


# **add_bill_of_lading**
> BillOfLading add_bill_of_lading(body)

Create a billOfLading

Inserts a new billOfLading using the specified data.

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
api_instance = Infoplus.BillOfLadingApi(Infoplus.ApiClient(configuration))
body = Infoplus.BillOfLading() # BillOfLading | BillOfLading to be inserted.

try:
    # Create a billOfLading
    api_response = api_instance.add_bill_of_lading(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillOfLadingApi->add_bill_of_lading: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillOfLading**](BillOfLading.md)| BillOfLading to be inserted. | 

### Return type

[**BillOfLading**](BillOfLading.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_bill_of_lading_audit**
> add_bill_of_lading_audit(bill_of_lading_id, bill_of_lading_audit)

Add new audit for a billOfLading

Adds an audit to an existing billOfLading.

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
api_instance = Infoplus.BillOfLadingApi(Infoplus.ApiClient(configuration))
bill_of_lading_id = 56 # int | Id of the billOfLading to add an audit to
bill_of_lading_audit = 'bill_of_lading_audit_example' # str | The audit to add

try:
    # Add new audit for a billOfLading
    api_instance.add_bill_of_lading_audit(bill_of_lading_id, bill_of_lading_audit)
except ApiException as e:
    print("Exception when calling BillOfLadingApi->add_bill_of_lading_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_of_lading_id** | **int**| Id of the billOfLading to add an audit to | 
 **bill_of_lading_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_bill_of_lading_file**
> add_bill_of_lading_file(bill_of_lading_id, file_name)

Attach a file to a billOfLading

Adds a file to an existing billOfLading.

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
api_instance = Infoplus.BillOfLadingApi(Infoplus.ApiClient(configuration))
bill_of_lading_id = 56 # int | Id of the billOfLading to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a billOfLading
    api_instance.add_bill_of_lading_file(bill_of_lading_id, file_name)
except ApiException as e:
    print("Exception when calling BillOfLadingApi->add_bill_of_lading_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_of_lading_id** | **int**| Id of the billOfLading to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_bill_of_lading_file_by_url**
> add_bill_of_lading_file_by_url(body, bill_of_lading_id)

Attach a file to a billOfLading by URL.

Adds a file to an existing billOfLading by URL.

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
api_instance = Infoplus.BillOfLadingApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
bill_of_lading_id = 56 # int | Id of the billOfLading to add an file to

try:
    # Attach a file to a billOfLading by URL.
    api_instance.add_bill_of_lading_file_by_url(body, bill_of_lading_id)
except ApiException as e:
    print("Exception when calling BillOfLadingApi->add_bill_of_lading_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **bill_of_lading_id** | **int**| Id of the billOfLading to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_bill_of_lading_tag**
> add_bill_of_lading_tag(bill_of_lading_id, bill_of_lading_tag)

Add new tags for a billOfLading.

Adds a tag to an existing billOfLading.

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
api_instance = Infoplus.BillOfLadingApi(Infoplus.ApiClient(configuration))
bill_of_lading_id = 56 # int | Id of the billOfLading to add a tag to
bill_of_lading_tag = 'bill_of_lading_tag_example' # str | The tag to add

try:
    # Add new tags for a billOfLading.
    api_instance.add_bill_of_lading_tag(bill_of_lading_id, bill_of_lading_tag)
except ApiException as e:
    print("Exception when calling BillOfLadingApi->add_bill_of_lading_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_of_lading_id** | **int**| Id of the billOfLading to add a tag to | 
 **bill_of_lading_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bill_of_lading**
> delete_bill_of_lading(bill_of_lading_id)

Delete a billOfLading

Deletes the billOfLading identified by the specified id.

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
api_instance = Infoplus.BillOfLadingApi(Infoplus.ApiClient(configuration))
bill_of_lading_id = 56 # int | Id of the billOfLading to be deleted.

try:
    # Delete a billOfLading
    api_instance.delete_bill_of_lading(bill_of_lading_id)
except ApiException as e:
    print("Exception when calling BillOfLadingApi->delete_bill_of_lading: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_of_lading_id** | **int**| Id of the billOfLading to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bill_of_lading_file**
> delete_bill_of_lading_file(bill_of_lading_id, file_id)

Delete a file for a billOfLading.

Deletes an existing billOfLading file using the specified data.

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
api_instance = Infoplus.BillOfLadingApi(Infoplus.ApiClient(configuration))
bill_of_lading_id = 56 # int | Id of the billOfLading to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a billOfLading.
    api_instance.delete_bill_of_lading_file(bill_of_lading_id, file_id)
except ApiException as e:
    print("Exception when calling BillOfLadingApi->delete_bill_of_lading_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_of_lading_id** | **int**| Id of the billOfLading to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bill_of_lading_tag**
> delete_bill_of_lading_tag(bill_of_lading_id, bill_of_lading_tag)

Delete a tag for a billOfLading.

Deletes an existing billOfLading tag using the specified data.

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
api_instance = Infoplus.BillOfLadingApi(Infoplus.ApiClient(configuration))
bill_of_lading_id = 56 # int | Id of the billOfLading to remove tag from
bill_of_lading_tag = 'bill_of_lading_tag_example' # str | The tag to delete

try:
    # Delete a tag for a billOfLading.
    api_instance.delete_bill_of_lading_tag(bill_of_lading_id, bill_of_lading_tag)
except ApiException as e:
    print("Exception when calling BillOfLadingApi->delete_bill_of_lading_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_of_lading_id** | **int**| Id of the billOfLading to remove tag from | 
 **bill_of_lading_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bill_of_lading_by_filter**
> list[BillOfLading] get_bill_of_lading_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search billOfLadings by filter

Returns the list of billOfLadings that match the given filter.

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
api_instance = Infoplus.BillOfLadingApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search billOfLadings by filter
    api_response = api_instance.get_bill_of_lading_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillOfLadingApi->get_bill_of_lading_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[BillOfLading]**](BillOfLading.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bill_of_lading_by_id**
> BillOfLading get_bill_of_lading_by_id(bill_of_lading_id)

Get a billOfLading by id

Returns the billOfLading identified by the specified id.

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
api_instance = Infoplus.BillOfLadingApi(Infoplus.ApiClient(configuration))
bill_of_lading_id = 56 # int | Id of the billOfLading to be returned.

try:
    # Get a billOfLading by id
    api_response = api_instance.get_bill_of_lading_by_id(bill_of_lading_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillOfLadingApi->get_bill_of_lading_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_of_lading_id** | **int**| Id of the billOfLading to be returned. | 

### Return type

[**BillOfLading**](BillOfLading.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bill_of_lading_files**
> get_bill_of_lading_files(bill_of_lading_id)

Get the files for a billOfLading.

Get all existing billOfLading files.

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
api_instance = Infoplus.BillOfLadingApi(Infoplus.ApiClient(configuration))
bill_of_lading_id = 56 # int | Id of the billOfLading to get files for

try:
    # Get the files for a billOfLading.
    api_instance.get_bill_of_lading_files(bill_of_lading_id)
except ApiException as e:
    print("Exception when calling BillOfLadingApi->get_bill_of_lading_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_of_lading_id** | **int**| Id of the billOfLading to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bill_of_lading_tags**
> get_bill_of_lading_tags(bill_of_lading_id)

Get the tags for a billOfLading.

Get all existing billOfLading tags.

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
api_instance = Infoplus.BillOfLadingApi(Infoplus.ApiClient(configuration))
bill_of_lading_id = 56 # int | Id of the billOfLading to get tags for

try:
    # Get the tags for a billOfLading.
    api_instance.get_bill_of_lading_tags(bill_of_lading_id)
except ApiException as e:
    print("Exception when calling BillOfLadingApi->get_bill_of_lading_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_of_lading_id** | **int**| Id of the billOfLading to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_bill_of_lading_by_id**
> BillOfLading get_duplicate_bill_of_lading_by_id(bill_of_lading_id)

Get a duplicated a billOfLading by id

Returns a duplicated billOfLading identified by the specified id.

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
api_instance = Infoplus.BillOfLadingApi(Infoplus.ApiClient(configuration))
bill_of_lading_id = 56 # int | Id of the billOfLading to be duplicated.

try:
    # Get a duplicated a billOfLading by id
    api_response = api_instance.get_duplicate_bill_of_lading_by_id(bill_of_lading_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillOfLadingApi->get_duplicate_bill_of_lading_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_of_lading_id** | **int**| Id of the billOfLading to be duplicated. | 

### Return type

[**BillOfLading**](BillOfLading.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bill_of_lading**
> update_bill_of_lading(body)

Update a billOfLading

Updates an existing billOfLading using the specified data.

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
api_instance = Infoplus.BillOfLadingApi(Infoplus.ApiClient(configuration))
body = Infoplus.BillOfLading() # BillOfLading | BillOfLading to be updated.

try:
    # Update a billOfLading
    api_instance.update_bill_of_lading(body)
except ApiException as e:
    print("Exception when calling BillOfLadingApi->update_bill_of_lading: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillOfLading**](BillOfLading.md)| BillOfLading to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bill_of_lading_custom_fields**
> update_bill_of_lading_custom_fields(body)

Update a billOfLading custom fields

Updates an existing billOfLading custom fields using the specified data.

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
api_instance = Infoplus.BillOfLadingApi(Infoplus.ApiClient(configuration))
body = Infoplus.BillOfLading() # BillOfLading | BillOfLading to be updated.

try:
    # Update a billOfLading custom fields
    api_instance.update_bill_of_lading_custom_fields(body)
except ApiException as e:
    print("Exception when calling BillOfLadingApi->update_bill_of_lading_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillOfLading**](BillOfLading.md)| BillOfLading to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

