# Infoplus.StandardBusinessDaysApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_standard_business_days**](StandardBusinessDaysApi.md#add_standard_business_days) | **POST** /v3.0/standardBusinessDays | Create a standardBusinessDays
[**add_standard_business_days_audit**](StandardBusinessDaysApi.md#add_standard_business_days_audit) | **PUT** /v3.0/standardBusinessDays/{standardBusinessDaysId}/audit/{standardBusinessDaysAudit} | Add new audit for a standardBusinessDays
[**add_standard_business_days_file**](StandardBusinessDaysApi.md#add_standard_business_days_file) | **POST** /v3.0/standardBusinessDays/{standardBusinessDaysId}/file/{fileName} | Attach a file to a standardBusinessDays
[**add_standard_business_days_file_by_url**](StandardBusinessDaysApi.md#add_standard_business_days_file_by_url) | **POST** /v3.0/standardBusinessDays/{standardBusinessDaysId}/file | Attach a file to a standardBusinessDays by URL.
[**add_standard_business_days_tag**](StandardBusinessDaysApi.md#add_standard_business_days_tag) | **PUT** /v3.0/standardBusinessDays/{standardBusinessDaysId}/tag/{standardBusinessDaysTag} | Add new tags for a standardBusinessDays.
[**delete_standard_business_days**](StandardBusinessDaysApi.md#delete_standard_business_days) | **DELETE** /v3.0/standardBusinessDays/{standardBusinessDaysId} | Delete a standardBusinessDays
[**delete_standard_business_days_file**](StandardBusinessDaysApi.md#delete_standard_business_days_file) | **DELETE** /v3.0/standardBusinessDays/{standardBusinessDaysId}/file/{fileId} | Delete a file for a standardBusinessDays.
[**delete_standard_business_days_tag**](StandardBusinessDaysApi.md#delete_standard_business_days_tag) | **DELETE** /v3.0/standardBusinessDays/{standardBusinessDaysId}/tag/{standardBusinessDaysTag} | Delete a tag for a standardBusinessDays.
[**get_duplicate_standard_business_days_by_id**](StandardBusinessDaysApi.md#get_duplicate_standard_business_days_by_id) | **GET** /v3.0/standardBusinessDays/duplicate/{standardBusinessDaysId} | Get a duplicated a standardBusinessDays by id
[**get_standard_business_days_by_filter**](StandardBusinessDaysApi.md#get_standard_business_days_by_filter) | **GET** /v3.0/standardBusinessDays/search | Search standardBusinessDayses by filter
[**get_standard_business_days_by_id**](StandardBusinessDaysApi.md#get_standard_business_days_by_id) | **GET** /v3.0/standardBusinessDays/{standardBusinessDaysId} | Get a standardBusinessDays by id
[**get_standard_business_days_files**](StandardBusinessDaysApi.md#get_standard_business_days_files) | **GET** /v3.0/standardBusinessDays/{standardBusinessDaysId}/file | Get the files for a standardBusinessDays.
[**get_standard_business_days_tags**](StandardBusinessDaysApi.md#get_standard_business_days_tags) | **GET** /v3.0/standardBusinessDays/{standardBusinessDaysId}/tag | Get the tags for a standardBusinessDays.
[**update_standard_business_days**](StandardBusinessDaysApi.md#update_standard_business_days) | **PUT** /v3.0/standardBusinessDays | Update a standardBusinessDays


# **add_standard_business_days**
> StandardBusinessDays add_standard_business_days(body)

Create a standardBusinessDays

Inserts a new standardBusinessDays using the specified data.

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
api_instance = Infoplus.StandardBusinessDaysApi(Infoplus.ApiClient(configuration))
body = Infoplus.StandardBusinessDays() # StandardBusinessDays | StandardBusinessDays to be inserted.

try:
    # Create a standardBusinessDays
    api_response = api_instance.add_standard_business_days(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardBusinessDaysApi->add_standard_business_days: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StandardBusinessDays**](StandardBusinessDays.md)| StandardBusinessDays to be inserted. | 

### Return type

[**StandardBusinessDays**](StandardBusinessDays.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_standard_business_days_audit**
> add_standard_business_days_audit(standard_business_days_id, standard_business_days_audit)

Add new audit for a standardBusinessDays

Adds an audit to an existing standardBusinessDays.

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
api_instance = Infoplus.StandardBusinessDaysApi(Infoplus.ApiClient(configuration))
standard_business_days_id = 56 # int | Id of the standardBusinessDays to add an audit to
standard_business_days_audit = 'standard_business_days_audit_example' # str | The audit to add

try:
    # Add new audit for a standardBusinessDays
    api_instance.add_standard_business_days_audit(standard_business_days_id, standard_business_days_audit)
except ApiException as e:
    print("Exception when calling StandardBusinessDaysApi->add_standard_business_days_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_business_days_id** | **int**| Id of the standardBusinessDays to add an audit to | 
 **standard_business_days_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_standard_business_days_file**
> add_standard_business_days_file(standard_business_days_id, file_name)

Attach a file to a standardBusinessDays

Adds a file to an existing standardBusinessDays.

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
api_instance = Infoplus.StandardBusinessDaysApi(Infoplus.ApiClient(configuration))
standard_business_days_id = 56 # int | Id of the standardBusinessDays to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a standardBusinessDays
    api_instance.add_standard_business_days_file(standard_business_days_id, file_name)
except ApiException as e:
    print("Exception when calling StandardBusinessDaysApi->add_standard_business_days_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_business_days_id** | **int**| Id of the standardBusinessDays to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_standard_business_days_file_by_url**
> add_standard_business_days_file_by_url(body, standard_business_days_id)

Attach a file to a standardBusinessDays by URL.

Adds a file to an existing standardBusinessDays by URL.

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
api_instance = Infoplus.StandardBusinessDaysApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
standard_business_days_id = 56 # int | Id of the standardBusinessDays to add an file to

try:
    # Attach a file to a standardBusinessDays by URL.
    api_instance.add_standard_business_days_file_by_url(body, standard_business_days_id)
except ApiException as e:
    print("Exception when calling StandardBusinessDaysApi->add_standard_business_days_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **standard_business_days_id** | **int**| Id of the standardBusinessDays to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_standard_business_days_tag**
> add_standard_business_days_tag(standard_business_days_id, standard_business_days_tag)

Add new tags for a standardBusinessDays.

Adds a tag to an existing standardBusinessDays.

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
api_instance = Infoplus.StandardBusinessDaysApi(Infoplus.ApiClient(configuration))
standard_business_days_id = 56 # int | Id of the standardBusinessDays to add a tag to
standard_business_days_tag = 'standard_business_days_tag_example' # str | The tag to add

try:
    # Add new tags for a standardBusinessDays.
    api_instance.add_standard_business_days_tag(standard_business_days_id, standard_business_days_tag)
except ApiException as e:
    print("Exception when calling StandardBusinessDaysApi->add_standard_business_days_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_business_days_id** | **int**| Id of the standardBusinessDays to add a tag to | 
 **standard_business_days_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_standard_business_days**
> delete_standard_business_days(standard_business_days_id)

Delete a standardBusinessDays

Deletes the standardBusinessDays identified by the specified id.

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
api_instance = Infoplus.StandardBusinessDaysApi(Infoplus.ApiClient(configuration))
standard_business_days_id = 56 # int | Id of the standardBusinessDays to be deleted.

try:
    # Delete a standardBusinessDays
    api_instance.delete_standard_business_days(standard_business_days_id)
except ApiException as e:
    print("Exception when calling StandardBusinessDaysApi->delete_standard_business_days: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_business_days_id** | **int**| Id of the standardBusinessDays to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_standard_business_days_file**
> delete_standard_business_days_file(standard_business_days_id, file_id)

Delete a file for a standardBusinessDays.

Deletes an existing standardBusinessDays file using the specified data.

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
api_instance = Infoplus.StandardBusinessDaysApi(Infoplus.ApiClient(configuration))
standard_business_days_id = 56 # int | Id of the standardBusinessDays to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a standardBusinessDays.
    api_instance.delete_standard_business_days_file(standard_business_days_id, file_id)
except ApiException as e:
    print("Exception when calling StandardBusinessDaysApi->delete_standard_business_days_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_business_days_id** | **int**| Id of the standardBusinessDays to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_standard_business_days_tag**
> delete_standard_business_days_tag(standard_business_days_id, standard_business_days_tag)

Delete a tag for a standardBusinessDays.

Deletes an existing standardBusinessDays tag using the specified data.

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
api_instance = Infoplus.StandardBusinessDaysApi(Infoplus.ApiClient(configuration))
standard_business_days_id = 56 # int | Id of the standardBusinessDays to remove tag from
standard_business_days_tag = 'standard_business_days_tag_example' # str | The tag to delete

try:
    # Delete a tag for a standardBusinessDays.
    api_instance.delete_standard_business_days_tag(standard_business_days_id, standard_business_days_tag)
except ApiException as e:
    print("Exception when calling StandardBusinessDaysApi->delete_standard_business_days_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_business_days_id** | **int**| Id of the standardBusinessDays to remove tag from | 
 **standard_business_days_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_standard_business_days_by_id**
> StandardBusinessDays get_duplicate_standard_business_days_by_id(standard_business_days_id)

Get a duplicated a standardBusinessDays by id

Returns a duplicated standardBusinessDays identified by the specified id.

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
api_instance = Infoplus.StandardBusinessDaysApi(Infoplus.ApiClient(configuration))
standard_business_days_id = 56 # int | Id of the standardBusinessDays to be duplicated.

try:
    # Get a duplicated a standardBusinessDays by id
    api_response = api_instance.get_duplicate_standard_business_days_by_id(standard_business_days_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardBusinessDaysApi->get_duplicate_standard_business_days_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_business_days_id** | **int**| Id of the standardBusinessDays to be duplicated. | 

### Return type

[**StandardBusinessDays**](StandardBusinessDays.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_standard_business_days_by_filter**
> list[StandardBusinessDays] get_standard_business_days_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search standardBusinessDayses by filter

Returns the list of standardBusinessDayses that match the given filter.

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
api_instance = Infoplus.StandardBusinessDaysApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search standardBusinessDayses by filter
    api_response = api_instance.get_standard_business_days_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardBusinessDaysApi->get_standard_business_days_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[StandardBusinessDays]**](StandardBusinessDays.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_standard_business_days_by_id**
> StandardBusinessDays get_standard_business_days_by_id(standard_business_days_id)

Get a standardBusinessDays by id

Returns the standardBusinessDays identified by the specified id.

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
api_instance = Infoplus.StandardBusinessDaysApi(Infoplus.ApiClient(configuration))
standard_business_days_id = 56 # int | Id of the standardBusinessDays to be returned.

try:
    # Get a standardBusinessDays by id
    api_response = api_instance.get_standard_business_days_by_id(standard_business_days_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardBusinessDaysApi->get_standard_business_days_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_business_days_id** | **int**| Id of the standardBusinessDays to be returned. | 

### Return type

[**StandardBusinessDays**](StandardBusinessDays.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_standard_business_days_files**
> get_standard_business_days_files(standard_business_days_id)

Get the files for a standardBusinessDays.

Get all existing standardBusinessDays files.

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
api_instance = Infoplus.StandardBusinessDaysApi(Infoplus.ApiClient(configuration))
standard_business_days_id = 56 # int | Id of the standardBusinessDays to get files for

try:
    # Get the files for a standardBusinessDays.
    api_instance.get_standard_business_days_files(standard_business_days_id)
except ApiException as e:
    print("Exception when calling StandardBusinessDaysApi->get_standard_business_days_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_business_days_id** | **int**| Id of the standardBusinessDays to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_standard_business_days_tags**
> get_standard_business_days_tags(standard_business_days_id)

Get the tags for a standardBusinessDays.

Get all existing standardBusinessDays tags.

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
api_instance = Infoplus.StandardBusinessDaysApi(Infoplus.ApiClient(configuration))
standard_business_days_id = 56 # int | Id of the standardBusinessDays to get tags for

try:
    # Get the tags for a standardBusinessDays.
    api_instance.get_standard_business_days_tags(standard_business_days_id)
except ApiException as e:
    print("Exception when calling StandardBusinessDaysApi->get_standard_business_days_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_business_days_id** | **int**| Id of the standardBusinessDays to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_standard_business_days**
> update_standard_business_days(body)

Update a standardBusinessDays

Updates an existing standardBusinessDays using the specified data.

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
api_instance = Infoplus.StandardBusinessDaysApi(Infoplus.ApiClient(configuration))
body = Infoplus.StandardBusinessDays() # StandardBusinessDays | StandardBusinessDays to be updated.

try:
    # Update a standardBusinessDays
    api_instance.update_standard_business_days(body)
except ApiException as e:
    print("Exception when calling StandardBusinessDaysApi->update_standard_business_days: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StandardBusinessDays**](StandardBusinessDays.md)| StandardBusinessDays to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

