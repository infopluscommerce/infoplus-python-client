# Infoplus.VendorApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_vendor**](VendorApi.md#add_vendor) | **POST** /v3.0/vendor | Create a vendor
[**add_vendor_audit**](VendorApi.md#add_vendor_audit) | **PUT** /v3.0/vendor/{vendorId}/audit/{vendorAudit} | Add new audit for a vendor
[**add_vendor_file**](VendorApi.md#add_vendor_file) | **POST** /v3.0/vendor/{vendorId}/file/{fileName} | Attach a file to a vendor
[**add_vendor_file_by_url**](VendorApi.md#add_vendor_file_by_url) | **POST** /v3.0/vendor/{vendorId}/file | Attach a file to a vendor by URL.
[**add_vendor_tag**](VendorApi.md#add_vendor_tag) | **PUT** /v3.0/vendor/{vendorId}/tag/{vendorTag} | Add new tags for a vendor.
[**delete_vendor**](VendorApi.md#delete_vendor) | **DELETE** /v3.0/vendor/{vendorId} | Delete a vendor
[**delete_vendor_file**](VendorApi.md#delete_vendor_file) | **DELETE** /v3.0/vendor/{vendorId}/file/{fileId} | Delete a file for a vendor.
[**delete_vendor_tag**](VendorApi.md#delete_vendor_tag) | **DELETE** /v3.0/vendor/{vendorId}/tag/{vendorTag} | Delete a tag for a vendor.
[**get_duplicate_vendor_by_id**](VendorApi.md#get_duplicate_vendor_by_id) | **GET** /v3.0/vendor/duplicate/{vendorId} | Get a duplicated a vendor by id
[**get_vendor_by_filter**](VendorApi.md#get_vendor_by_filter) | **GET** /v3.0/vendor/search | Search vendors by filter
[**get_vendor_by_id**](VendorApi.md#get_vendor_by_id) | **GET** /v3.0/vendor/{vendorId} | Get a vendor by id
[**get_vendor_files**](VendorApi.md#get_vendor_files) | **GET** /v3.0/vendor/{vendorId}/file | Get the files for a vendor.
[**get_vendor_tags**](VendorApi.md#get_vendor_tags) | **GET** /v3.0/vendor/{vendorId}/tag | Get the tags for a vendor.
[**update_vendor**](VendorApi.md#update_vendor) | **PUT** /v3.0/vendor | Update a vendor
[**update_vendor_custom_fields**](VendorApi.md#update_vendor_custom_fields) | **PUT** /v3.0/vendor/customFields | Update a vendor custom fields


# **add_vendor**
> Vendor add_vendor(body)

Create a vendor

Inserts a new vendor using the specified data.

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
api_instance = Infoplus.VendorApi(Infoplus.ApiClient(configuration))
body = Infoplus.Vendor() # Vendor | Vendor to be inserted.

try:
    # Create a vendor
    api_response = api_instance.add_vendor(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorApi->add_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Vendor**](Vendor.md)| Vendor to be inserted. | 

### Return type

[**Vendor**](Vendor.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_vendor_audit**
> add_vendor_audit(vendor_id, vendor_audit)

Add new audit for a vendor

Adds an audit to an existing vendor.

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
api_instance = Infoplus.VendorApi(Infoplus.ApiClient(configuration))
vendor_id = 56 # int | Id of the vendor to add an audit to
vendor_audit = 'vendor_audit_example' # str | The audit to add

try:
    # Add new audit for a vendor
    api_instance.add_vendor_audit(vendor_id, vendor_audit)
except ApiException as e:
    print("Exception when calling VendorApi->add_vendor_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| Id of the vendor to add an audit to | 
 **vendor_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_vendor_file**
> add_vendor_file(vendor_id, file_name)

Attach a file to a vendor

Adds a file to an existing vendor.

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
api_instance = Infoplus.VendorApi(Infoplus.ApiClient(configuration))
vendor_id = 56 # int | Id of the vendor to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a vendor
    api_instance.add_vendor_file(vendor_id, file_name)
except ApiException as e:
    print("Exception when calling VendorApi->add_vendor_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| Id of the vendor to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_vendor_file_by_url**
> add_vendor_file_by_url(body, vendor_id)

Attach a file to a vendor by URL.

Adds a file to an existing vendor by URL.

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
api_instance = Infoplus.VendorApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
vendor_id = 56 # int | Id of the vendor to add an file to

try:
    # Attach a file to a vendor by URL.
    api_instance.add_vendor_file_by_url(body, vendor_id)
except ApiException as e:
    print("Exception when calling VendorApi->add_vendor_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **vendor_id** | **int**| Id of the vendor to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_vendor_tag**
> add_vendor_tag(vendor_id, vendor_tag)

Add new tags for a vendor.

Adds a tag to an existing vendor.

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
api_instance = Infoplus.VendorApi(Infoplus.ApiClient(configuration))
vendor_id = 56 # int | Id of the vendor to add a tag to
vendor_tag = 'vendor_tag_example' # str | The tag to add

try:
    # Add new tags for a vendor.
    api_instance.add_vendor_tag(vendor_id, vendor_tag)
except ApiException as e:
    print("Exception when calling VendorApi->add_vendor_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| Id of the vendor to add a tag to | 
 **vendor_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vendor**
> delete_vendor(vendor_id)

Delete a vendor

Deletes the vendor identified by the specified id.

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
api_instance = Infoplus.VendorApi(Infoplus.ApiClient(configuration))
vendor_id = 56 # int | Id of the vendor to be deleted.

try:
    # Delete a vendor
    api_instance.delete_vendor(vendor_id)
except ApiException as e:
    print("Exception when calling VendorApi->delete_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| Id of the vendor to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vendor_file**
> delete_vendor_file(vendor_id, file_id)

Delete a file for a vendor.

Deletes an existing vendor file using the specified data.

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
api_instance = Infoplus.VendorApi(Infoplus.ApiClient(configuration))
vendor_id = 56 # int | Id of the vendor to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a vendor.
    api_instance.delete_vendor_file(vendor_id, file_id)
except ApiException as e:
    print("Exception when calling VendorApi->delete_vendor_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| Id of the vendor to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vendor_tag**
> delete_vendor_tag(vendor_id, vendor_tag)

Delete a tag for a vendor.

Deletes an existing vendor tag using the specified data.

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
api_instance = Infoplus.VendorApi(Infoplus.ApiClient(configuration))
vendor_id = 56 # int | Id of the vendor to remove tag from
vendor_tag = 'vendor_tag_example' # str | The tag to delete

try:
    # Delete a tag for a vendor.
    api_instance.delete_vendor_tag(vendor_id, vendor_tag)
except ApiException as e:
    print("Exception when calling VendorApi->delete_vendor_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| Id of the vendor to remove tag from | 
 **vendor_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_vendor_by_id**
> Vendor get_duplicate_vendor_by_id(vendor_id)

Get a duplicated a vendor by id

Returns a duplicated vendor identified by the specified id.

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
api_instance = Infoplus.VendorApi(Infoplus.ApiClient(configuration))
vendor_id = 56 # int | Id of the vendor to be duplicated.

try:
    # Get a duplicated a vendor by id
    api_response = api_instance.get_duplicate_vendor_by_id(vendor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorApi->get_duplicate_vendor_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| Id of the vendor to be duplicated. | 

### Return type

[**Vendor**](Vendor.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_by_filter**
> list[Vendor] get_vendor_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search vendors by filter

Returns the list of vendors that match the given filter.

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
api_instance = Infoplus.VendorApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search vendors by filter
    api_response = api_instance.get_vendor_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorApi->get_vendor_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Vendor]**](Vendor.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_by_id**
> Vendor get_vendor_by_id(vendor_id)

Get a vendor by id

Returns the vendor identified by the specified id.

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
api_instance = Infoplus.VendorApi(Infoplus.ApiClient(configuration))
vendor_id = 56 # int | Id of the vendor to be returned.

try:
    # Get a vendor by id
    api_response = api_instance.get_vendor_by_id(vendor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorApi->get_vendor_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| Id of the vendor to be returned. | 

### Return type

[**Vendor**](Vendor.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_files**
> get_vendor_files(vendor_id)

Get the files for a vendor.

Get all existing vendor files.

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
api_instance = Infoplus.VendorApi(Infoplus.ApiClient(configuration))
vendor_id = 56 # int | Id of the vendor to get files for

try:
    # Get the files for a vendor.
    api_instance.get_vendor_files(vendor_id)
except ApiException as e:
    print("Exception when calling VendorApi->get_vendor_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| Id of the vendor to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_tags**
> get_vendor_tags(vendor_id)

Get the tags for a vendor.

Get all existing vendor tags.

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
api_instance = Infoplus.VendorApi(Infoplus.ApiClient(configuration))
vendor_id = 56 # int | Id of the vendor to get tags for

try:
    # Get the tags for a vendor.
    api_instance.get_vendor_tags(vendor_id)
except ApiException as e:
    print("Exception when calling VendorApi->get_vendor_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| Id of the vendor to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vendor**
> update_vendor(body)

Update a vendor

Updates an existing vendor using the specified data.

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
api_instance = Infoplus.VendorApi(Infoplus.ApiClient(configuration))
body = Infoplus.Vendor() # Vendor | Vendor to be updated.

try:
    # Update a vendor
    api_instance.update_vendor(body)
except ApiException as e:
    print("Exception when calling VendorApi->update_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Vendor**](Vendor.md)| Vendor to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vendor_custom_fields**
> update_vendor_custom_fields(body)

Update a vendor custom fields

Updates an existing vendor custom fields using the specified data.

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
api_instance = Infoplus.VendorApi(Infoplus.ApiClient(configuration))
body = Infoplus.Vendor() # Vendor | Vendor to be updated.

try:
    # Update a vendor custom fields
    api_instance.update_vendor_custom_fields(body)
except ApiException as e:
    print("Exception when calling VendorApi->update_vendor_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Vendor**](Vendor.md)| Vendor to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

