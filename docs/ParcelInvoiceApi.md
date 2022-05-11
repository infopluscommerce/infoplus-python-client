# Infoplus.ParcelInvoiceApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_parcel_invoice_audit**](ParcelInvoiceApi.md#add_parcel_invoice_audit) | **PUT** /v3.0/parcelInvoice/{parcelInvoiceId}/audit/{parcelInvoiceAudit} | Add new audit for a parcelInvoice
[**add_parcel_invoice_file**](ParcelInvoiceApi.md#add_parcel_invoice_file) | **POST** /v3.0/parcelInvoice/{parcelInvoiceId}/file/{fileName} | Attach a file to a parcelInvoice
[**add_parcel_invoice_file_by_url**](ParcelInvoiceApi.md#add_parcel_invoice_file_by_url) | **POST** /v3.0/parcelInvoice/{parcelInvoiceId}/file | Attach a file to a parcelInvoice by URL.
[**add_parcel_invoice_tag**](ParcelInvoiceApi.md#add_parcel_invoice_tag) | **PUT** /v3.0/parcelInvoice/{parcelInvoiceId}/tag/{parcelInvoiceTag} | Add new tags for a parcelInvoice.
[**delete_parcel_invoice**](ParcelInvoiceApi.md#delete_parcel_invoice) | **DELETE** /v3.0/parcelInvoice/{parcelInvoiceId} | Delete a parcelInvoice
[**delete_parcel_invoice_file**](ParcelInvoiceApi.md#delete_parcel_invoice_file) | **DELETE** /v3.0/parcelInvoice/{parcelInvoiceId}/file/{fileId} | Delete a file for a parcelInvoice.
[**delete_parcel_invoice_tag**](ParcelInvoiceApi.md#delete_parcel_invoice_tag) | **DELETE** /v3.0/parcelInvoice/{parcelInvoiceId}/tag/{parcelInvoiceTag} | Delete a tag for a parcelInvoice.
[**get_duplicate_parcel_invoice_by_id**](ParcelInvoiceApi.md#get_duplicate_parcel_invoice_by_id) | **GET** /v3.0/parcelInvoice/duplicate/{parcelInvoiceId} | Get a duplicated a parcelInvoice by id
[**get_parcel_invoice_by_filter**](ParcelInvoiceApi.md#get_parcel_invoice_by_filter) | **GET** /v3.0/parcelInvoice/search | Search parcelInvoices by filter
[**get_parcel_invoice_by_id**](ParcelInvoiceApi.md#get_parcel_invoice_by_id) | **GET** /v3.0/parcelInvoice/{parcelInvoiceId} | Get a parcelInvoice by id
[**get_parcel_invoice_files**](ParcelInvoiceApi.md#get_parcel_invoice_files) | **GET** /v3.0/parcelInvoice/{parcelInvoiceId}/file | Get the files for a parcelInvoice.
[**get_parcel_invoice_tags**](ParcelInvoiceApi.md#get_parcel_invoice_tags) | **GET** /v3.0/parcelInvoice/{parcelInvoiceId}/tag | Get the tags for a parcelInvoice.


# **add_parcel_invoice_audit**
> add_parcel_invoice_audit(parcel_invoice_id, parcel_invoice_audit)

Add new audit for a parcelInvoice

Adds an audit to an existing parcelInvoice.

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
api_instance = Infoplus.ParcelInvoiceApi(Infoplus.ApiClient(configuration))
parcel_invoice_id = 56 # int | Id of the parcelInvoice to add an audit to
parcel_invoice_audit = 'parcel_invoice_audit_example' # str | The audit to add

try:
    # Add new audit for a parcelInvoice
    api_instance.add_parcel_invoice_audit(parcel_invoice_id, parcel_invoice_audit)
except ApiException as e:
    print("Exception when calling ParcelInvoiceApi->add_parcel_invoice_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_id** | **int**| Id of the parcelInvoice to add an audit to | 
 **parcel_invoice_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_parcel_invoice_file**
> add_parcel_invoice_file(parcel_invoice_id, file_name)

Attach a file to a parcelInvoice

Adds a file to an existing parcelInvoice.

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
api_instance = Infoplus.ParcelInvoiceApi(Infoplus.ApiClient(configuration))
parcel_invoice_id = 56 # int | Id of the parcelInvoice to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a parcelInvoice
    api_instance.add_parcel_invoice_file(parcel_invoice_id, file_name)
except ApiException as e:
    print("Exception when calling ParcelInvoiceApi->add_parcel_invoice_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_id** | **int**| Id of the parcelInvoice to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_parcel_invoice_file_by_url**
> add_parcel_invoice_file_by_url(body, parcel_invoice_id)

Attach a file to a parcelInvoice by URL.

Adds a file to an existing parcelInvoice by URL.

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
api_instance = Infoplus.ParcelInvoiceApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
parcel_invoice_id = 56 # int | Id of the parcelInvoice to add an file to

try:
    # Attach a file to a parcelInvoice by URL.
    api_instance.add_parcel_invoice_file_by_url(body, parcel_invoice_id)
except ApiException as e:
    print("Exception when calling ParcelInvoiceApi->add_parcel_invoice_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **parcel_invoice_id** | **int**| Id of the parcelInvoice to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_parcel_invoice_tag**
> add_parcel_invoice_tag(parcel_invoice_id, parcel_invoice_tag)

Add new tags for a parcelInvoice.

Adds a tag to an existing parcelInvoice.

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
api_instance = Infoplus.ParcelInvoiceApi(Infoplus.ApiClient(configuration))
parcel_invoice_id = 56 # int | Id of the parcelInvoice to add a tag to
parcel_invoice_tag = 'parcel_invoice_tag_example' # str | The tag to add

try:
    # Add new tags for a parcelInvoice.
    api_instance.add_parcel_invoice_tag(parcel_invoice_id, parcel_invoice_tag)
except ApiException as e:
    print("Exception when calling ParcelInvoiceApi->add_parcel_invoice_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_id** | **int**| Id of the parcelInvoice to add a tag to | 
 **parcel_invoice_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_parcel_invoice**
> delete_parcel_invoice(parcel_invoice_id)

Delete a parcelInvoice

Deletes the parcelInvoice identified by the specified id.

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
api_instance = Infoplus.ParcelInvoiceApi(Infoplus.ApiClient(configuration))
parcel_invoice_id = 56 # int | Id of the parcelInvoice to be deleted.

try:
    # Delete a parcelInvoice
    api_instance.delete_parcel_invoice(parcel_invoice_id)
except ApiException as e:
    print("Exception when calling ParcelInvoiceApi->delete_parcel_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_id** | **int**| Id of the parcelInvoice to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_parcel_invoice_file**
> delete_parcel_invoice_file(parcel_invoice_id, file_id)

Delete a file for a parcelInvoice.

Deletes an existing parcelInvoice file using the specified data.

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
api_instance = Infoplus.ParcelInvoiceApi(Infoplus.ApiClient(configuration))
parcel_invoice_id = 56 # int | Id of the parcelInvoice to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a parcelInvoice.
    api_instance.delete_parcel_invoice_file(parcel_invoice_id, file_id)
except ApiException as e:
    print("Exception when calling ParcelInvoiceApi->delete_parcel_invoice_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_id** | **int**| Id of the parcelInvoice to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_parcel_invoice_tag**
> delete_parcel_invoice_tag(parcel_invoice_id, parcel_invoice_tag)

Delete a tag for a parcelInvoice.

Deletes an existing parcelInvoice tag using the specified data.

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
api_instance = Infoplus.ParcelInvoiceApi(Infoplus.ApiClient(configuration))
parcel_invoice_id = 56 # int | Id of the parcelInvoice to remove tag from
parcel_invoice_tag = 'parcel_invoice_tag_example' # str | The tag to delete

try:
    # Delete a tag for a parcelInvoice.
    api_instance.delete_parcel_invoice_tag(parcel_invoice_id, parcel_invoice_tag)
except ApiException as e:
    print("Exception when calling ParcelInvoiceApi->delete_parcel_invoice_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_id** | **int**| Id of the parcelInvoice to remove tag from | 
 **parcel_invoice_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_parcel_invoice_by_id**
> ParcelInvoice get_duplicate_parcel_invoice_by_id(parcel_invoice_id)

Get a duplicated a parcelInvoice by id

Returns a duplicated parcelInvoice identified by the specified id.

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
api_instance = Infoplus.ParcelInvoiceApi(Infoplus.ApiClient(configuration))
parcel_invoice_id = 56 # int | Id of the parcelInvoice to be duplicated.

try:
    # Get a duplicated a parcelInvoice by id
    api_response = api_instance.get_duplicate_parcel_invoice_by_id(parcel_invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParcelInvoiceApi->get_duplicate_parcel_invoice_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_id** | **int**| Id of the parcelInvoice to be duplicated. | 

### Return type

[**ParcelInvoice**](ParcelInvoice.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parcel_invoice_by_filter**
> list[ParcelInvoice] get_parcel_invoice_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search parcelInvoices by filter

Returns the list of parcelInvoices that match the given filter.

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
api_instance = Infoplus.ParcelInvoiceApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search parcelInvoices by filter
    api_response = api_instance.get_parcel_invoice_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParcelInvoiceApi->get_parcel_invoice_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ParcelInvoice]**](ParcelInvoice.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parcel_invoice_by_id**
> ParcelInvoice get_parcel_invoice_by_id(parcel_invoice_id)

Get a parcelInvoice by id

Returns the parcelInvoice identified by the specified id.

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
api_instance = Infoplus.ParcelInvoiceApi(Infoplus.ApiClient(configuration))
parcel_invoice_id = 56 # int | Id of the parcelInvoice to be returned.

try:
    # Get a parcelInvoice by id
    api_response = api_instance.get_parcel_invoice_by_id(parcel_invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParcelInvoiceApi->get_parcel_invoice_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_id** | **int**| Id of the parcelInvoice to be returned. | 

### Return type

[**ParcelInvoice**](ParcelInvoice.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parcel_invoice_files**
> get_parcel_invoice_files(parcel_invoice_id)

Get the files for a parcelInvoice.

Get all existing parcelInvoice files.

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
api_instance = Infoplus.ParcelInvoiceApi(Infoplus.ApiClient(configuration))
parcel_invoice_id = 56 # int | Id of the parcelInvoice to get files for

try:
    # Get the files for a parcelInvoice.
    api_instance.get_parcel_invoice_files(parcel_invoice_id)
except ApiException as e:
    print("Exception when calling ParcelInvoiceApi->get_parcel_invoice_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_id** | **int**| Id of the parcelInvoice to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parcel_invoice_tags**
> get_parcel_invoice_tags(parcel_invoice_id)

Get the tags for a parcelInvoice.

Get all existing parcelInvoice tags.

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
api_instance = Infoplus.ParcelInvoiceApi(Infoplus.ApiClient(configuration))
parcel_invoice_id = 56 # int | Id of the parcelInvoice to get tags for

try:
    # Get the tags for a parcelInvoice.
    api_instance.get_parcel_invoice_tags(parcel_invoice_id)
except ApiException as e:
    print("Exception when calling ParcelInvoiceApi->get_parcel_invoice_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_id** | **int**| Id of the parcelInvoice to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

