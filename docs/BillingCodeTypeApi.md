# Infoplus.BillingCodeTypeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_billing_code_type**](BillingCodeTypeApi.md#add_billing_code_type) | **POST** /beta/billingCodeType | Create a billingCodeType
[**add_billing_code_type_audit**](BillingCodeTypeApi.md#add_billing_code_type_audit) | **PUT** /beta/billingCodeType/{billingCodeTypeId}/audit/{billingCodeTypeAudit} | Add new audit for a billingCodeType
[**add_billing_code_type_file**](BillingCodeTypeApi.md#add_billing_code_type_file) | **POST** /beta/billingCodeType/{billingCodeTypeId}/file/{fileName} | Attach a file to a billingCodeType
[**add_billing_code_type_file_by_url**](BillingCodeTypeApi.md#add_billing_code_type_file_by_url) | **POST** /beta/billingCodeType/{billingCodeTypeId}/file | Attach a file to a billingCodeType by URL.
[**add_billing_code_type_tag**](BillingCodeTypeApi.md#add_billing_code_type_tag) | **PUT** /beta/billingCodeType/{billingCodeTypeId}/tag/{billingCodeTypeTag} | Add new tags for a billingCodeType.
[**delete_billing_code_type**](BillingCodeTypeApi.md#delete_billing_code_type) | **DELETE** /beta/billingCodeType/{billingCodeTypeId} | Delete a billingCodeType
[**delete_billing_code_type_file**](BillingCodeTypeApi.md#delete_billing_code_type_file) | **DELETE** /beta/billingCodeType/{billingCodeTypeId}/file/{fileId} | Delete a file for a billingCodeType.
[**delete_billing_code_type_tag**](BillingCodeTypeApi.md#delete_billing_code_type_tag) | **DELETE** /beta/billingCodeType/{billingCodeTypeId}/tag/{billingCodeTypeTag} | Delete a tag for a billingCodeType.
[**get_billing_code_type_by_filter**](BillingCodeTypeApi.md#get_billing_code_type_by_filter) | **GET** /beta/billingCodeType/search | Search billingCodeTypes by filter
[**get_billing_code_type_by_id**](BillingCodeTypeApi.md#get_billing_code_type_by_id) | **GET** /beta/billingCodeType/{billingCodeTypeId} | Get a billingCodeType by id
[**get_billing_code_type_files**](BillingCodeTypeApi.md#get_billing_code_type_files) | **GET** /beta/billingCodeType/{billingCodeTypeId}/file | Get the files for a billingCodeType.
[**get_billing_code_type_tags**](BillingCodeTypeApi.md#get_billing_code_type_tags) | **GET** /beta/billingCodeType/{billingCodeTypeId}/tag | Get the tags for a billingCodeType.
[**get_duplicate_billing_code_type_by_id**](BillingCodeTypeApi.md#get_duplicate_billing_code_type_by_id) | **GET** /beta/billingCodeType/duplicate/{billingCodeTypeId} | Get a duplicated a billingCodeType by id
[**update_billing_code_type**](BillingCodeTypeApi.md#update_billing_code_type) | **PUT** /beta/billingCodeType | Update a billingCodeType
[**update_billing_code_type_custom_fields**](BillingCodeTypeApi.md#update_billing_code_type_custom_fields) | **PUT** /beta/billingCodeType/customFields | Update a billingCodeType custom fields


# **add_billing_code_type**
> BillingCodeType add_billing_code_type(body)

Create a billingCodeType

Inserts a new billingCodeType using the specified data.

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
api_instance = Infoplus.BillingCodeTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.BillingCodeType() # BillingCodeType | BillingCodeType to be inserted.

try:
    # Create a billingCodeType
    api_response = api_instance.add_billing_code_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeTypeApi->add_billing_code_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingCodeType**](BillingCodeType.md)| BillingCodeType to be inserted. | 

### Return type

[**BillingCodeType**](BillingCodeType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_billing_code_type_audit**
> add_billing_code_type_audit(billing_code_type_id, billing_code_type_audit)

Add new audit for a billingCodeType

Adds an audit to an existing billingCodeType.

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
api_instance = Infoplus.BillingCodeTypeApi(Infoplus.ApiClient(configuration))
billing_code_type_id = 56 # int | Id of the billingCodeType to add an audit to
billing_code_type_audit = 'billing_code_type_audit_example' # str | The audit to add

try:
    # Add new audit for a billingCodeType
    api_instance.add_billing_code_type_audit(billing_code_type_id, billing_code_type_audit)
except ApiException as e:
    print("Exception when calling BillingCodeTypeApi->add_billing_code_type_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_type_id** | **int**| Id of the billingCodeType to add an audit to | 
 **billing_code_type_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_billing_code_type_file**
> add_billing_code_type_file(billing_code_type_id, file_name)

Attach a file to a billingCodeType

Adds a file to an existing billingCodeType.

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
api_instance = Infoplus.BillingCodeTypeApi(Infoplus.ApiClient(configuration))
billing_code_type_id = 56 # int | Id of the billingCodeType to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a billingCodeType
    api_instance.add_billing_code_type_file(billing_code_type_id, file_name)
except ApiException as e:
    print("Exception when calling BillingCodeTypeApi->add_billing_code_type_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_type_id** | **int**| Id of the billingCodeType to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_billing_code_type_file_by_url**
> add_billing_code_type_file_by_url(body, billing_code_type_id)

Attach a file to a billingCodeType by URL.

Adds a file to an existing billingCodeType by URL.

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
api_instance = Infoplus.BillingCodeTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
billing_code_type_id = 56 # int | Id of the billingCodeType to add an file to

try:
    # Attach a file to a billingCodeType by URL.
    api_instance.add_billing_code_type_file_by_url(body, billing_code_type_id)
except ApiException as e:
    print("Exception when calling BillingCodeTypeApi->add_billing_code_type_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **billing_code_type_id** | **int**| Id of the billingCodeType to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_billing_code_type_tag**
> add_billing_code_type_tag(billing_code_type_id, billing_code_type_tag)

Add new tags for a billingCodeType.

Adds a tag to an existing billingCodeType.

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
api_instance = Infoplus.BillingCodeTypeApi(Infoplus.ApiClient(configuration))
billing_code_type_id = 56 # int | Id of the billingCodeType to add a tag to
billing_code_type_tag = 'billing_code_type_tag_example' # str | The tag to add

try:
    # Add new tags for a billingCodeType.
    api_instance.add_billing_code_type_tag(billing_code_type_id, billing_code_type_tag)
except ApiException as e:
    print("Exception when calling BillingCodeTypeApi->add_billing_code_type_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_type_id** | **int**| Id of the billingCodeType to add a tag to | 
 **billing_code_type_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_code_type**
> delete_billing_code_type(billing_code_type_id)

Delete a billingCodeType

Deletes the billingCodeType identified by the specified id.

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
api_instance = Infoplus.BillingCodeTypeApi(Infoplus.ApiClient(configuration))
billing_code_type_id = 56 # int | Id of the billingCodeType to be deleted.

try:
    # Delete a billingCodeType
    api_instance.delete_billing_code_type(billing_code_type_id)
except ApiException as e:
    print("Exception when calling BillingCodeTypeApi->delete_billing_code_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_type_id** | **int**| Id of the billingCodeType to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_code_type_file**
> delete_billing_code_type_file(billing_code_type_id, file_id)

Delete a file for a billingCodeType.

Deletes an existing billingCodeType file using the specified data.

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
api_instance = Infoplus.BillingCodeTypeApi(Infoplus.ApiClient(configuration))
billing_code_type_id = 56 # int | Id of the billingCodeType to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a billingCodeType.
    api_instance.delete_billing_code_type_file(billing_code_type_id, file_id)
except ApiException as e:
    print("Exception when calling BillingCodeTypeApi->delete_billing_code_type_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_type_id** | **int**| Id of the billingCodeType to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_code_type_tag**
> delete_billing_code_type_tag(billing_code_type_id, billing_code_type_tag)

Delete a tag for a billingCodeType.

Deletes an existing billingCodeType tag using the specified data.

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
api_instance = Infoplus.BillingCodeTypeApi(Infoplus.ApiClient(configuration))
billing_code_type_id = 56 # int | Id of the billingCodeType to remove tag from
billing_code_type_tag = 'billing_code_type_tag_example' # str | The tag to delete

try:
    # Delete a tag for a billingCodeType.
    api_instance.delete_billing_code_type_tag(billing_code_type_id, billing_code_type_tag)
except ApiException as e:
    print("Exception when calling BillingCodeTypeApi->delete_billing_code_type_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_type_id** | **int**| Id of the billingCodeType to remove tag from | 
 **billing_code_type_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_code_type_by_filter**
> list[BillingCodeType] get_billing_code_type_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search billingCodeTypes by filter

Returns the list of billingCodeTypes that match the given filter.

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
api_instance = Infoplus.BillingCodeTypeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search billingCodeTypes by filter
    api_response = api_instance.get_billing_code_type_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeTypeApi->get_billing_code_type_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[BillingCodeType]**](BillingCodeType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_code_type_by_id**
> BillingCodeType get_billing_code_type_by_id(billing_code_type_id)

Get a billingCodeType by id

Returns the billingCodeType identified by the specified id.

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
api_instance = Infoplus.BillingCodeTypeApi(Infoplus.ApiClient(configuration))
billing_code_type_id = 56 # int | Id of the billingCodeType to be returned.

try:
    # Get a billingCodeType by id
    api_response = api_instance.get_billing_code_type_by_id(billing_code_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeTypeApi->get_billing_code_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_type_id** | **int**| Id of the billingCodeType to be returned. | 

### Return type

[**BillingCodeType**](BillingCodeType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_code_type_files**
> get_billing_code_type_files(billing_code_type_id)

Get the files for a billingCodeType.

Get all existing billingCodeType files.

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
api_instance = Infoplus.BillingCodeTypeApi(Infoplus.ApiClient(configuration))
billing_code_type_id = 56 # int | Id of the billingCodeType to get files for

try:
    # Get the files for a billingCodeType.
    api_instance.get_billing_code_type_files(billing_code_type_id)
except ApiException as e:
    print("Exception when calling BillingCodeTypeApi->get_billing_code_type_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_type_id** | **int**| Id of the billingCodeType to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_code_type_tags**
> get_billing_code_type_tags(billing_code_type_id)

Get the tags for a billingCodeType.

Get all existing billingCodeType tags.

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
api_instance = Infoplus.BillingCodeTypeApi(Infoplus.ApiClient(configuration))
billing_code_type_id = 56 # int | Id of the billingCodeType to get tags for

try:
    # Get the tags for a billingCodeType.
    api_instance.get_billing_code_type_tags(billing_code_type_id)
except ApiException as e:
    print("Exception when calling BillingCodeTypeApi->get_billing_code_type_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_type_id** | **int**| Id of the billingCodeType to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_billing_code_type_by_id**
> BillingCodeType get_duplicate_billing_code_type_by_id(billing_code_type_id)

Get a duplicated a billingCodeType by id

Returns a duplicated billingCodeType identified by the specified id.

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
api_instance = Infoplus.BillingCodeTypeApi(Infoplus.ApiClient(configuration))
billing_code_type_id = 56 # int | Id of the billingCodeType to be duplicated.

try:
    # Get a duplicated a billingCodeType by id
    api_response = api_instance.get_duplicate_billing_code_type_by_id(billing_code_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeTypeApi->get_duplicate_billing_code_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_type_id** | **int**| Id of the billingCodeType to be duplicated. | 

### Return type

[**BillingCodeType**](BillingCodeType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_code_type**
> update_billing_code_type(body)

Update a billingCodeType

Updates an existing billingCodeType using the specified data.

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
api_instance = Infoplus.BillingCodeTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.BillingCodeType() # BillingCodeType | BillingCodeType to be updated.

try:
    # Update a billingCodeType
    api_instance.update_billing_code_type(body)
except ApiException as e:
    print("Exception when calling BillingCodeTypeApi->update_billing_code_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingCodeType**](BillingCodeType.md)| BillingCodeType to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_code_type_custom_fields**
> update_billing_code_type_custom_fields(body)

Update a billingCodeType custom fields

Updates an existing billingCodeType custom fields using the specified data.

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
api_instance = Infoplus.BillingCodeTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.BillingCodeType() # BillingCodeType | BillingCodeType to be updated.

try:
    # Update a billingCodeType custom fields
    api_instance.update_billing_code_type_custom_fields(body)
except ApiException as e:
    print("Exception when calling BillingCodeTypeApi->update_billing_code_type_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingCodeType**](BillingCodeType.md)| BillingCodeType to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

