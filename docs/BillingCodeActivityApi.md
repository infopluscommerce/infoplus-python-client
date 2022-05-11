# Infoplus.BillingCodeActivityApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_billing_code_activity**](BillingCodeActivityApi.md#add_billing_code_activity) | **POST** /v3.0/billingCodeActivity | Create a billingCodeActivity
[**add_billing_code_activity_audit**](BillingCodeActivityApi.md#add_billing_code_activity_audit) | **PUT** /v3.0/billingCodeActivity/{billingCodeActivityId}/audit/{billingCodeActivityAudit} | Add new audit for a billingCodeActivity
[**add_billing_code_activity_file**](BillingCodeActivityApi.md#add_billing_code_activity_file) | **POST** /v3.0/billingCodeActivity/{billingCodeActivityId}/file/{fileName} | Attach a file to a billingCodeActivity
[**add_billing_code_activity_file_by_url**](BillingCodeActivityApi.md#add_billing_code_activity_file_by_url) | **POST** /v3.0/billingCodeActivity/{billingCodeActivityId}/file | Attach a file to a billingCodeActivity by URL.
[**add_billing_code_activity_tag**](BillingCodeActivityApi.md#add_billing_code_activity_tag) | **PUT** /v3.0/billingCodeActivity/{billingCodeActivityId}/tag/{billingCodeActivityTag} | Add new tags for a billingCodeActivity.
[**delete_billing_code_activity**](BillingCodeActivityApi.md#delete_billing_code_activity) | **DELETE** /v3.0/billingCodeActivity/{billingCodeActivityId} | Delete a billingCodeActivity
[**delete_billing_code_activity_file**](BillingCodeActivityApi.md#delete_billing_code_activity_file) | **DELETE** /v3.0/billingCodeActivity/{billingCodeActivityId}/file/{fileId} | Delete a file for a billingCodeActivity.
[**delete_billing_code_activity_tag**](BillingCodeActivityApi.md#delete_billing_code_activity_tag) | **DELETE** /v3.0/billingCodeActivity/{billingCodeActivityId}/tag/{billingCodeActivityTag} | Delete a tag for a billingCodeActivity.
[**get_billing_code_activity_by_filter**](BillingCodeActivityApi.md#get_billing_code_activity_by_filter) | **GET** /v3.0/billingCodeActivity/search | Search billingCodeActivitys by filter
[**get_billing_code_activity_by_id**](BillingCodeActivityApi.md#get_billing_code_activity_by_id) | **GET** /v3.0/billingCodeActivity/{billingCodeActivityId} | Get a billingCodeActivity by id
[**get_billing_code_activity_files**](BillingCodeActivityApi.md#get_billing_code_activity_files) | **GET** /v3.0/billingCodeActivity/{billingCodeActivityId}/file | Get the files for a billingCodeActivity.
[**get_billing_code_activity_tags**](BillingCodeActivityApi.md#get_billing_code_activity_tags) | **GET** /v3.0/billingCodeActivity/{billingCodeActivityId}/tag | Get the tags for a billingCodeActivity.
[**get_duplicate_billing_code_activity_by_id**](BillingCodeActivityApi.md#get_duplicate_billing_code_activity_by_id) | **GET** /v3.0/billingCodeActivity/duplicate/{billingCodeActivityId} | Get a duplicated a billingCodeActivity by id
[**update_billing_code_activity**](BillingCodeActivityApi.md#update_billing_code_activity) | **PUT** /v3.0/billingCodeActivity | Update a billingCodeActivity


# **add_billing_code_activity**
> BillingCodeActivity add_billing_code_activity(body)

Create a billingCodeActivity

Inserts a new billingCodeActivity using the specified data.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.BillingCodeActivity() # BillingCodeActivity | BillingCodeActivity to be inserted.

try:
    # Create a billingCodeActivity
    api_response = api_instance.add_billing_code_activity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->add_billing_code_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingCodeActivity**](BillingCodeActivity.md)| BillingCodeActivity to be inserted. | 

### Return type

[**BillingCodeActivity**](BillingCodeActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_billing_code_activity_audit**
> add_billing_code_activity_audit(billing_code_activity_id, billing_code_activity_audit)

Add new audit for a billingCodeActivity

Adds an audit to an existing billingCodeActivity.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to add an audit to
billing_code_activity_audit = 'billing_code_activity_audit_example' # str | The audit to add

try:
    # Add new audit for a billingCodeActivity
    api_instance.add_billing_code_activity_audit(billing_code_activity_id, billing_code_activity_audit)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->add_billing_code_activity_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to add an audit to | 
 **billing_code_activity_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_billing_code_activity_file**
> add_billing_code_activity_file(billing_code_activity_id, file_name)

Attach a file to a billingCodeActivity

Adds a file to an existing billingCodeActivity.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a billingCodeActivity
    api_instance.add_billing_code_activity_file(billing_code_activity_id, file_name)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->add_billing_code_activity_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_billing_code_activity_file_by_url**
> add_billing_code_activity_file_by_url(body, billing_code_activity_id)

Attach a file to a billingCodeActivity by URL.

Adds a file to an existing billingCodeActivity by URL.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to add an file to

try:
    # Attach a file to a billingCodeActivity by URL.
    api_instance.add_billing_code_activity_file_by_url(body, billing_code_activity_id)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->add_billing_code_activity_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_billing_code_activity_tag**
> add_billing_code_activity_tag(billing_code_activity_id, billing_code_activity_tag)

Add new tags for a billingCodeActivity.

Adds a tag to an existing billingCodeActivity.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to add a tag to
billing_code_activity_tag = 'billing_code_activity_tag_example' # str | The tag to add

try:
    # Add new tags for a billingCodeActivity.
    api_instance.add_billing_code_activity_tag(billing_code_activity_id, billing_code_activity_tag)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->add_billing_code_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to add a tag to | 
 **billing_code_activity_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_code_activity**
> delete_billing_code_activity(billing_code_activity_id)

Delete a billingCodeActivity

Deletes the billingCodeActivity identified by the specified id.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to be deleted.

try:
    # Delete a billingCodeActivity
    api_instance.delete_billing_code_activity(billing_code_activity_id)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->delete_billing_code_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_code_activity_file**
> delete_billing_code_activity_file(billing_code_activity_id, file_id)

Delete a file for a billingCodeActivity.

Deletes an existing billingCodeActivity file using the specified data.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a billingCodeActivity.
    api_instance.delete_billing_code_activity_file(billing_code_activity_id, file_id)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->delete_billing_code_activity_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_code_activity_tag**
> delete_billing_code_activity_tag(billing_code_activity_id, billing_code_activity_tag)

Delete a tag for a billingCodeActivity.

Deletes an existing billingCodeActivity tag using the specified data.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to remove tag from
billing_code_activity_tag = 'billing_code_activity_tag_example' # str | The tag to delete

try:
    # Delete a tag for a billingCodeActivity.
    api_instance.delete_billing_code_activity_tag(billing_code_activity_id, billing_code_activity_tag)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->delete_billing_code_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to remove tag from | 
 **billing_code_activity_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_code_activity_by_filter**
> list[BillingCodeActivity] get_billing_code_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search billingCodeActivitys by filter

Returns the list of billingCodeActivitys that match the given filter.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search billingCodeActivitys by filter
    api_response = api_instance.get_billing_code_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->get_billing_code_activity_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[BillingCodeActivity]**](BillingCodeActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_code_activity_by_id**
> BillingCodeActivity get_billing_code_activity_by_id(billing_code_activity_id)

Get a billingCodeActivity by id

Returns the billingCodeActivity identified by the specified id.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to be returned.

try:
    # Get a billingCodeActivity by id
    api_response = api_instance.get_billing_code_activity_by_id(billing_code_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->get_billing_code_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to be returned. | 

### Return type

[**BillingCodeActivity**](BillingCodeActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_code_activity_files**
> get_billing_code_activity_files(billing_code_activity_id)

Get the files for a billingCodeActivity.

Get all existing billingCodeActivity files.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to get files for

try:
    # Get the files for a billingCodeActivity.
    api_instance.get_billing_code_activity_files(billing_code_activity_id)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->get_billing_code_activity_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_code_activity_tags**
> get_billing_code_activity_tags(billing_code_activity_id)

Get the tags for a billingCodeActivity.

Get all existing billingCodeActivity tags.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to get tags for

try:
    # Get the tags for a billingCodeActivity.
    api_instance.get_billing_code_activity_tags(billing_code_activity_id)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->get_billing_code_activity_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_billing_code_activity_by_id**
> BillingCodeActivity get_duplicate_billing_code_activity_by_id(billing_code_activity_id)

Get a duplicated a billingCodeActivity by id

Returns a duplicated billingCodeActivity identified by the specified id.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to be duplicated.

try:
    # Get a duplicated a billingCodeActivity by id
    api_response = api_instance.get_duplicate_billing_code_activity_by_id(billing_code_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->get_duplicate_billing_code_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to be duplicated. | 

### Return type

[**BillingCodeActivity**](BillingCodeActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_code_activity**
> update_billing_code_activity(body)

Update a billingCodeActivity

Updates an existing billingCodeActivity using the specified data.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.BillingCodeActivity() # BillingCodeActivity | BillingCodeActivity to be updated.

try:
    # Update a billingCodeActivity
    api_instance.update_billing_code_activity(body)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->update_billing_code_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingCodeActivity**](BillingCodeActivity.md)| BillingCodeActivity to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

