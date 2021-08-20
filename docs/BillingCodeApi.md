# Infoplus.BillingCodeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_billing_code**](BillingCodeApi.md#add_billing_code) | **POST** /beta/billingCode | Create a billingCode
[**add_billing_code_audit**](BillingCodeApi.md#add_billing_code_audit) | **PUT** /beta/billingCode/{billingCodeId}/audit/{billingCodeAudit} | Add new audit for a billingCode
[**add_billing_code_file**](BillingCodeApi.md#add_billing_code_file) | **POST** /beta/billingCode/{billingCodeId}/file/{fileName} | Attach a file to a billingCode
[**add_billing_code_file_by_url**](BillingCodeApi.md#add_billing_code_file_by_url) | **POST** /beta/billingCode/{billingCodeId}/file | Attach a file to a billingCode by URL.
[**add_billing_code_tag**](BillingCodeApi.md#add_billing_code_tag) | **PUT** /beta/billingCode/{billingCodeId}/tag/{billingCodeTag} | Add new tags for a billingCode.
[**delete_billing_code**](BillingCodeApi.md#delete_billing_code) | **DELETE** /beta/billingCode/{billingCodeId} | Delete a billingCode
[**delete_billing_code_file**](BillingCodeApi.md#delete_billing_code_file) | **DELETE** /beta/billingCode/{billingCodeId}/file/{fileId} | Delete a file for a billingCode.
[**delete_billing_code_tag**](BillingCodeApi.md#delete_billing_code_tag) | **DELETE** /beta/billingCode/{billingCodeId}/tag/{billingCodeTag} | Delete a tag for a billingCode.
[**get_billing_code_by_filter**](BillingCodeApi.md#get_billing_code_by_filter) | **GET** /beta/billingCode/search | Search billingCodes by filter
[**get_billing_code_by_id**](BillingCodeApi.md#get_billing_code_by_id) | **GET** /beta/billingCode/{billingCodeId} | Get a billingCode by id
[**get_billing_code_files**](BillingCodeApi.md#get_billing_code_files) | **GET** /beta/billingCode/{billingCodeId}/file | Get the files for a billingCode.
[**get_billing_code_tags**](BillingCodeApi.md#get_billing_code_tags) | **GET** /beta/billingCode/{billingCodeId}/tag | Get the tags for a billingCode.
[**get_duplicate_billing_code_by_id**](BillingCodeApi.md#get_duplicate_billing_code_by_id) | **GET** /beta/billingCode/duplicate/{billingCodeId} | Get a duplicated a billingCode by id
[**update_billing_code**](BillingCodeApi.md#update_billing_code) | **PUT** /beta/billingCode | Update a billingCode
[**update_billing_code_custom_fields**](BillingCodeApi.md#update_billing_code_custom_fields) | **PUT** /beta/billingCode/customFields | Update a billingCode custom fields


# **add_billing_code**
> BillingCode add_billing_code(body)

Create a billingCode

Inserts a new billingCode using the specified data.

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
api_instance = Infoplus.BillingCodeApi(Infoplus.ApiClient(configuration))
body = Infoplus.BillingCode() # BillingCode | BillingCode to be inserted.

try:
    # Create a billingCode
    api_response = api_instance.add_billing_code(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeApi->add_billing_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingCode**](BillingCode.md)| BillingCode to be inserted. | 

### Return type

[**BillingCode**](BillingCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_billing_code_audit**
> add_billing_code_audit(billing_code_id, billing_code_audit)

Add new audit for a billingCode

Adds an audit to an existing billingCode.

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
api_instance = Infoplus.BillingCodeApi(Infoplus.ApiClient(configuration))
billing_code_id = 56 # int | Id of the billingCode to add an audit to
billing_code_audit = 'billing_code_audit_example' # str | The audit to add

try:
    # Add new audit for a billingCode
    api_instance.add_billing_code_audit(billing_code_id, billing_code_audit)
except ApiException as e:
    print("Exception when calling BillingCodeApi->add_billing_code_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_id** | **int**| Id of the billingCode to add an audit to | 
 **billing_code_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_billing_code_file**
> add_billing_code_file(billing_code_id, file_name)

Attach a file to a billingCode

Adds a file to an existing billingCode.

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
api_instance = Infoplus.BillingCodeApi(Infoplus.ApiClient(configuration))
billing_code_id = 56 # int | Id of the billingCode to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a billingCode
    api_instance.add_billing_code_file(billing_code_id, file_name)
except ApiException as e:
    print("Exception when calling BillingCodeApi->add_billing_code_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_id** | **int**| Id of the billingCode to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_billing_code_file_by_url**
> add_billing_code_file_by_url(body, billing_code_id)

Attach a file to a billingCode by URL.

Adds a file to an existing billingCode by URL.

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
api_instance = Infoplus.BillingCodeApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
billing_code_id = 56 # int | Id of the billingCode to add an file to

try:
    # Attach a file to a billingCode by URL.
    api_instance.add_billing_code_file_by_url(body, billing_code_id)
except ApiException as e:
    print("Exception when calling BillingCodeApi->add_billing_code_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **billing_code_id** | **int**| Id of the billingCode to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_billing_code_tag**
> add_billing_code_tag(billing_code_id, billing_code_tag)

Add new tags for a billingCode.

Adds a tag to an existing billingCode.

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
api_instance = Infoplus.BillingCodeApi(Infoplus.ApiClient(configuration))
billing_code_id = 56 # int | Id of the billingCode to add a tag to
billing_code_tag = 'billing_code_tag_example' # str | The tag to add

try:
    # Add new tags for a billingCode.
    api_instance.add_billing_code_tag(billing_code_id, billing_code_tag)
except ApiException as e:
    print("Exception when calling BillingCodeApi->add_billing_code_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_id** | **int**| Id of the billingCode to add a tag to | 
 **billing_code_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_code**
> delete_billing_code(billing_code_id)

Delete a billingCode

Deletes the billingCode identified by the specified id.

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
api_instance = Infoplus.BillingCodeApi(Infoplus.ApiClient(configuration))
billing_code_id = 56 # int | Id of the billingCode to be deleted.

try:
    # Delete a billingCode
    api_instance.delete_billing_code(billing_code_id)
except ApiException as e:
    print("Exception when calling BillingCodeApi->delete_billing_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_id** | **int**| Id of the billingCode to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_code_file**
> delete_billing_code_file(billing_code_id, file_id)

Delete a file for a billingCode.

Deletes an existing billingCode file using the specified data.

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
api_instance = Infoplus.BillingCodeApi(Infoplus.ApiClient(configuration))
billing_code_id = 56 # int | Id of the billingCode to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a billingCode.
    api_instance.delete_billing_code_file(billing_code_id, file_id)
except ApiException as e:
    print("Exception when calling BillingCodeApi->delete_billing_code_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_id** | **int**| Id of the billingCode to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_code_tag**
> delete_billing_code_tag(billing_code_id, billing_code_tag)

Delete a tag for a billingCode.

Deletes an existing billingCode tag using the specified data.

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
api_instance = Infoplus.BillingCodeApi(Infoplus.ApiClient(configuration))
billing_code_id = 56 # int | Id of the billingCode to remove tag from
billing_code_tag = 'billing_code_tag_example' # str | The tag to delete

try:
    # Delete a tag for a billingCode.
    api_instance.delete_billing_code_tag(billing_code_id, billing_code_tag)
except ApiException as e:
    print("Exception when calling BillingCodeApi->delete_billing_code_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_id** | **int**| Id of the billingCode to remove tag from | 
 **billing_code_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_code_by_filter**
> list[BillingCode] get_billing_code_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search billingCodes by filter

Returns the list of billingCodes that match the given filter.

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
api_instance = Infoplus.BillingCodeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search billingCodes by filter
    api_response = api_instance.get_billing_code_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeApi->get_billing_code_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[BillingCode]**](BillingCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_code_by_id**
> BillingCode get_billing_code_by_id(billing_code_id)

Get a billingCode by id

Returns the billingCode identified by the specified id.

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
api_instance = Infoplus.BillingCodeApi(Infoplus.ApiClient(configuration))
billing_code_id = 56 # int | Id of the billingCode to be returned.

try:
    # Get a billingCode by id
    api_response = api_instance.get_billing_code_by_id(billing_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeApi->get_billing_code_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_id** | **int**| Id of the billingCode to be returned. | 

### Return type

[**BillingCode**](BillingCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_code_files**
> get_billing_code_files(billing_code_id)

Get the files for a billingCode.

Get all existing billingCode files.

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
api_instance = Infoplus.BillingCodeApi(Infoplus.ApiClient(configuration))
billing_code_id = 56 # int | Id of the billingCode to get files for

try:
    # Get the files for a billingCode.
    api_instance.get_billing_code_files(billing_code_id)
except ApiException as e:
    print("Exception when calling BillingCodeApi->get_billing_code_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_id** | **int**| Id of the billingCode to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_code_tags**
> get_billing_code_tags(billing_code_id)

Get the tags for a billingCode.

Get all existing billingCode tags.

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
api_instance = Infoplus.BillingCodeApi(Infoplus.ApiClient(configuration))
billing_code_id = 56 # int | Id of the billingCode to get tags for

try:
    # Get the tags for a billingCode.
    api_instance.get_billing_code_tags(billing_code_id)
except ApiException as e:
    print("Exception when calling BillingCodeApi->get_billing_code_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_id** | **int**| Id of the billingCode to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_billing_code_by_id**
> BillingCode get_duplicate_billing_code_by_id(billing_code_id)

Get a duplicated a billingCode by id

Returns a duplicated billingCode identified by the specified id.

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
api_instance = Infoplus.BillingCodeApi(Infoplus.ApiClient(configuration))
billing_code_id = 56 # int | Id of the billingCode to be duplicated.

try:
    # Get a duplicated a billingCode by id
    api_response = api_instance.get_duplicate_billing_code_by_id(billing_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeApi->get_duplicate_billing_code_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_id** | **int**| Id of the billingCode to be duplicated. | 

### Return type

[**BillingCode**](BillingCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_code**
> update_billing_code(body)

Update a billingCode

Updates an existing billingCode using the specified data.

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
api_instance = Infoplus.BillingCodeApi(Infoplus.ApiClient(configuration))
body = Infoplus.BillingCode() # BillingCode | BillingCode to be updated.

try:
    # Update a billingCode
    api_instance.update_billing_code(body)
except ApiException as e:
    print("Exception when calling BillingCodeApi->update_billing_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingCode**](BillingCode.md)| BillingCode to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_code_custom_fields**
> update_billing_code_custom_fields(body)

Update a billingCode custom fields

Updates an existing billingCode custom fields using the specified data.

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
api_instance = Infoplus.BillingCodeApi(Infoplus.ApiClient(configuration))
body = Infoplus.BillingCode() # BillingCode | BillingCode to be updated.

try:
    # Update a billingCode custom fields
    api_instance.update_billing_code_custom_fields(body)
except ApiException as e:
    print("Exception when calling BillingCodeApi->update_billing_code_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingCode**](BillingCode.md)| BillingCode to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

