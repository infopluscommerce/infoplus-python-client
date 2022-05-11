# Infoplus.NonBusinessDayApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_non_business_day**](NonBusinessDayApi.md#add_non_business_day) | **POST** /v3.0/nonBusinessDay | Create a nonBusinessDay
[**add_non_business_day_audit**](NonBusinessDayApi.md#add_non_business_day_audit) | **PUT** /v3.0/nonBusinessDay/{nonBusinessDayId}/audit/{nonBusinessDayAudit} | Add new audit for a nonBusinessDay
[**add_non_business_day_file**](NonBusinessDayApi.md#add_non_business_day_file) | **POST** /v3.0/nonBusinessDay/{nonBusinessDayId}/file/{fileName} | Attach a file to a nonBusinessDay
[**add_non_business_day_file_by_url**](NonBusinessDayApi.md#add_non_business_day_file_by_url) | **POST** /v3.0/nonBusinessDay/{nonBusinessDayId}/file | Attach a file to a nonBusinessDay by URL.
[**add_non_business_day_tag**](NonBusinessDayApi.md#add_non_business_day_tag) | **PUT** /v3.0/nonBusinessDay/{nonBusinessDayId}/tag/{nonBusinessDayTag} | Add new tags for a nonBusinessDay.
[**delete_non_business_day**](NonBusinessDayApi.md#delete_non_business_day) | **DELETE** /v3.0/nonBusinessDay/{nonBusinessDayId} | Delete a nonBusinessDay
[**delete_non_business_day_file**](NonBusinessDayApi.md#delete_non_business_day_file) | **DELETE** /v3.0/nonBusinessDay/{nonBusinessDayId}/file/{fileId} | Delete a file for a nonBusinessDay.
[**delete_non_business_day_tag**](NonBusinessDayApi.md#delete_non_business_day_tag) | **DELETE** /v3.0/nonBusinessDay/{nonBusinessDayId}/tag/{nonBusinessDayTag} | Delete a tag for a nonBusinessDay.
[**get_duplicate_non_business_day_by_id**](NonBusinessDayApi.md#get_duplicate_non_business_day_by_id) | **GET** /v3.0/nonBusinessDay/duplicate/{nonBusinessDayId} | Get a duplicated a nonBusinessDay by id
[**get_non_business_day_by_filter**](NonBusinessDayApi.md#get_non_business_day_by_filter) | **GET** /v3.0/nonBusinessDay/search | Search nonBusinessDays by filter
[**get_non_business_day_by_id**](NonBusinessDayApi.md#get_non_business_day_by_id) | **GET** /v3.0/nonBusinessDay/{nonBusinessDayId} | Get a nonBusinessDay by id
[**get_non_business_day_files**](NonBusinessDayApi.md#get_non_business_day_files) | **GET** /v3.0/nonBusinessDay/{nonBusinessDayId}/file | Get the files for a nonBusinessDay.
[**get_non_business_day_tags**](NonBusinessDayApi.md#get_non_business_day_tags) | **GET** /v3.0/nonBusinessDay/{nonBusinessDayId}/tag | Get the tags for a nonBusinessDay.
[**update_non_business_day**](NonBusinessDayApi.md#update_non_business_day) | **PUT** /v3.0/nonBusinessDay | Update a nonBusinessDay


# **add_non_business_day**
> NonBusinessDay add_non_business_day(body)

Create a nonBusinessDay

Inserts a new nonBusinessDay using the specified data.

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
api_instance = Infoplus.NonBusinessDayApi(Infoplus.ApiClient(configuration))
body = Infoplus.NonBusinessDay() # NonBusinessDay | NonBusinessDay to be inserted.

try:
    # Create a nonBusinessDay
    api_response = api_instance.add_non_business_day(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NonBusinessDayApi->add_non_business_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NonBusinessDay**](NonBusinessDay.md)| NonBusinessDay to be inserted. | 

### Return type

[**NonBusinessDay**](NonBusinessDay.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_non_business_day_audit**
> add_non_business_day_audit(non_business_day_id, non_business_day_audit)

Add new audit for a nonBusinessDay

Adds an audit to an existing nonBusinessDay.

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
api_instance = Infoplus.NonBusinessDayApi(Infoplus.ApiClient(configuration))
non_business_day_id = 56 # int | Id of the nonBusinessDay to add an audit to
non_business_day_audit = 'non_business_day_audit_example' # str | The audit to add

try:
    # Add new audit for a nonBusinessDay
    api_instance.add_non_business_day_audit(non_business_day_id, non_business_day_audit)
except ApiException as e:
    print("Exception when calling NonBusinessDayApi->add_non_business_day_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **non_business_day_id** | **int**| Id of the nonBusinessDay to add an audit to | 
 **non_business_day_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_non_business_day_file**
> add_non_business_day_file(non_business_day_id, file_name)

Attach a file to a nonBusinessDay

Adds a file to an existing nonBusinessDay.

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
api_instance = Infoplus.NonBusinessDayApi(Infoplus.ApiClient(configuration))
non_business_day_id = 56 # int | Id of the nonBusinessDay to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a nonBusinessDay
    api_instance.add_non_business_day_file(non_business_day_id, file_name)
except ApiException as e:
    print("Exception when calling NonBusinessDayApi->add_non_business_day_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **non_business_day_id** | **int**| Id of the nonBusinessDay to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_non_business_day_file_by_url**
> add_non_business_day_file_by_url(body, non_business_day_id)

Attach a file to a nonBusinessDay by URL.

Adds a file to an existing nonBusinessDay by URL.

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
api_instance = Infoplus.NonBusinessDayApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
non_business_day_id = 56 # int | Id of the nonBusinessDay to add an file to

try:
    # Attach a file to a nonBusinessDay by URL.
    api_instance.add_non_business_day_file_by_url(body, non_business_day_id)
except ApiException as e:
    print("Exception when calling NonBusinessDayApi->add_non_business_day_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **non_business_day_id** | **int**| Id of the nonBusinessDay to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_non_business_day_tag**
> add_non_business_day_tag(non_business_day_id, non_business_day_tag)

Add new tags for a nonBusinessDay.

Adds a tag to an existing nonBusinessDay.

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
api_instance = Infoplus.NonBusinessDayApi(Infoplus.ApiClient(configuration))
non_business_day_id = 56 # int | Id of the nonBusinessDay to add a tag to
non_business_day_tag = 'non_business_day_tag_example' # str | The tag to add

try:
    # Add new tags for a nonBusinessDay.
    api_instance.add_non_business_day_tag(non_business_day_id, non_business_day_tag)
except ApiException as e:
    print("Exception when calling NonBusinessDayApi->add_non_business_day_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **non_business_day_id** | **int**| Id of the nonBusinessDay to add a tag to | 
 **non_business_day_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_non_business_day**
> delete_non_business_day(non_business_day_id)

Delete a nonBusinessDay

Deletes the nonBusinessDay identified by the specified id.

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
api_instance = Infoplus.NonBusinessDayApi(Infoplus.ApiClient(configuration))
non_business_day_id = 56 # int | Id of the nonBusinessDay to be deleted.

try:
    # Delete a nonBusinessDay
    api_instance.delete_non_business_day(non_business_day_id)
except ApiException as e:
    print("Exception when calling NonBusinessDayApi->delete_non_business_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **non_business_day_id** | **int**| Id of the nonBusinessDay to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_non_business_day_file**
> delete_non_business_day_file(non_business_day_id, file_id)

Delete a file for a nonBusinessDay.

Deletes an existing nonBusinessDay file using the specified data.

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
api_instance = Infoplus.NonBusinessDayApi(Infoplus.ApiClient(configuration))
non_business_day_id = 56 # int | Id of the nonBusinessDay to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a nonBusinessDay.
    api_instance.delete_non_business_day_file(non_business_day_id, file_id)
except ApiException as e:
    print("Exception when calling NonBusinessDayApi->delete_non_business_day_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **non_business_day_id** | **int**| Id of the nonBusinessDay to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_non_business_day_tag**
> delete_non_business_day_tag(non_business_day_id, non_business_day_tag)

Delete a tag for a nonBusinessDay.

Deletes an existing nonBusinessDay tag using the specified data.

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
api_instance = Infoplus.NonBusinessDayApi(Infoplus.ApiClient(configuration))
non_business_day_id = 56 # int | Id of the nonBusinessDay to remove tag from
non_business_day_tag = 'non_business_day_tag_example' # str | The tag to delete

try:
    # Delete a tag for a nonBusinessDay.
    api_instance.delete_non_business_day_tag(non_business_day_id, non_business_day_tag)
except ApiException as e:
    print("Exception when calling NonBusinessDayApi->delete_non_business_day_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **non_business_day_id** | **int**| Id of the nonBusinessDay to remove tag from | 
 **non_business_day_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_non_business_day_by_id**
> NonBusinessDay get_duplicate_non_business_day_by_id(non_business_day_id)

Get a duplicated a nonBusinessDay by id

Returns a duplicated nonBusinessDay identified by the specified id.

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
api_instance = Infoplus.NonBusinessDayApi(Infoplus.ApiClient(configuration))
non_business_day_id = 56 # int | Id of the nonBusinessDay to be duplicated.

try:
    # Get a duplicated a nonBusinessDay by id
    api_response = api_instance.get_duplicate_non_business_day_by_id(non_business_day_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NonBusinessDayApi->get_duplicate_non_business_day_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **non_business_day_id** | **int**| Id of the nonBusinessDay to be duplicated. | 

### Return type

[**NonBusinessDay**](NonBusinessDay.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_business_day_by_filter**
> list[NonBusinessDay] get_non_business_day_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search nonBusinessDays by filter

Returns the list of nonBusinessDays that match the given filter.

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
api_instance = Infoplus.NonBusinessDayApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search nonBusinessDays by filter
    api_response = api_instance.get_non_business_day_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NonBusinessDayApi->get_non_business_day_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[NonBusinessDay]**](NonBusinessDay.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_business_day_by_id**
> NonBusinessDay get_non_business_day_by_id(non_business_day_id)

Get a nonBusinessDay by id

Returns the nonBusinessDay identified by the specified id.

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
api_instance = Infoplus.NonBusinessDayApi(Infoplus.ApiClient(configuration))
non_business_day_id = 56 # int | Id of the nonBusinessDay to be returned.

try:
    # Get a nonBusinessDay by id
    api_response = api_instance.get_non_business_day_by_id(non_business_day_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NonBusinessDayApi->get_non_business_day_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **non_business_day_id** | **int**| Id of the nonBusinessDay to be returned. | 

### Return type

[**NonBusinessDay**](NonBusinessDay.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_business_day_files**
> get_non_business_day_files(non_business_day_id)

Get the files for a nonBusinessDay.

Get all existing nonBusinessDay files.

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
api_instance = Infoplus.NonBusinessDayApi(Infoplus.ApiClient(configuration))
non_business_day_id = 56 # int | Id of the nonBusinessDay to get files for

try:
    # Get the files for a nonBusinessDay.
    api_instance.get_non_business_day_files(non_business_day_id)
except ApiException as e:
    print("Exception when calling NonBusinessDayApi->get_non_business_day_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **non_business_day_id** | **int**| Id of the nonBusinessDay to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_business_day_tags**
> get_non_business_day_tags(non_business_day_id)

Get the tags for a nonBusinessDay.

Get all existing nonBusinessDay tags.

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
api_instance = Infoplus.NonBusinessDayApi(Infoplus.ApiClient(configuration))
non_business_day_id = 56 # int | Id of the nonBusinessDay to get tags for

try:
    # Get the tags for a nonBusinessDay.
    api_instance.get_non_business_day_tags(non_business_day_id)
except ApiException as e:
    print("Exception when calling NonBusinessDayApi->get_non_business_day_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **non_business_day_id** | **int**| Id of the nonBusinessDay to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_non_business_day**
> update_non_business_day(body)

Update a nonBusinessDay

Updates an existing nonBusinessDay using the specified data.

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
api_instance = Infoplus.NonBusinessDayApi(Infoplus.ApiClient(configuration))
body = Infoplus.NonBusinessDay() # NonBusinessDay | NonBusinessDay to be updated.

try:
    # Update a nonBusinessDay
    api_instance.update_non_business_day(body)
except ApiException as e:
    print("Exception when calling NonBusinessDayApi->update_non_business_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NonBusinessDay**](NonBusinessDay.md)| NonBusinessDay to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

