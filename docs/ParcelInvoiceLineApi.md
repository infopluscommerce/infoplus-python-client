# Infoplus.ParcelInvoiceLineApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_parcel_invoice_line_audit**](ParcelInvoiceLineApi.md#add_parcel_invoice_line_audit) | **PUT** /beta/parcelInvoiceLine/{parcelInvoiceLineId}/audit/{parcelInvoiceLineAudit} | Add new audit for a parcelInvoiceLine
[**add_parcel_invoice_line_file**](ParcelInvoiceLineApi.md#add_parcel_invoice_line_file) | **POST** /beta/parcelInvoiceLine/{parcelInvoiceLineId}/file/{fileName} | Attach a file to a parcelInvoiceLine
[**add_parcel_invoice_line_file_by_url**](ParcelInvoiceLineApi.md#add_parcel_invoice_line_file_by_url) | **POST** /beta/parcelInvoiceLine/{parcelInvoiceLineId}/file | Attach a file to a parcelInvoiceLine by URL.
[**add_parcel_invoice_line_tag**](ParcelInvoiceLineApi.md#add_parcel_invoice_line_tag) | **PUT** /beta/parcelInvoiceLine/{parcelInvoiceLineId}/tag/{parcelInvoiceLineTag} | Add new tags for a parcelInvoiceLine.
[**delete_parcel_invoice_line_file**](ParcelInvoiceLineApi.md#delete_parcel_invoice_line_file) | **DELETE** /beta/parcelInvoiceLine/{parcelInvoiceLineId}/file/{fileId} | Delete a file for a parcelInvoiceLine.
[**delete_parcel_invoice_line_tag**](ParcelInvoiceLineApi.md#delete_parcel_invoice_line_tag) | **DELETE** /beta/parcelInvoiceLine/{parcelInvoiceLineId}/tag/{parcelInvoiceLineTag} | Delete a tag for a parcelInvoiceLine.
[**get_duplicate_parcel_invoice_line_by_id**](ParcelInvoiceLineApi.md#get_duplicate_parcel_invoice_line_by_id) | **GET** /beta/parcelInvoiceLine/duplicate/{parcelInvoiceLineId} | Get a duplicated a parcelInvoiceLine by id
[**get_parcel_invoice_line_by_filter**](ParcelInvoiceLineApi.md#get_parcel_invoice_line_by_filter) | **GET** /beta/parcelInvoiceLine/search | Search parcelInvoiceLines by filter
[**get_parcel_invoice_line_by_id**](ParcelInvoiceLineApi.md#get_parcel_invoice_line_by_id) | **GET** /beta/parcelInvoiceLine/{parcelInvoiceLineId} | Get a parcelInvoiceLine by id
[**get_parcel_invoice_line_files**](ParcelInvoiceLineApi.md#get_parcel_invoice_line_files) | **GET** /beta/parcelInvoiceLine/{parcelInvoiceLineId}/file | Get the files for a parcelInvoiceLine.
[**get_parcel_invoice_line_tags**](ParcelInvoiceLineApi.md#get_parcel_invoice_line_tags) | **GET** /beta/parcelInvoiceLine/{parcelInvoiceLineId}/tag | Get the tags for a parcelInvoiceLine.
[**update_parcel_invoice_line**](ParcelInvoiceLineApi.md#update_parcel_invoice_line) | **PUT** /beta/parcelInvoiceLine | Update a parcelInvoiceLine


# **add_parcel_invoice_line_audit**
> add_parcel_invoice_line_audit(parcel_invoice_line_id, parcel_invoice_line_audit)

Add new audit for a parcelInvoiceLine

Adds an audit to an existing parcelInvoiceLine.

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
api_instance = Infoplus.ParcelInvoiceLineApi(Infoplus.ApiClient(configuration))
parcel_invoice_line_id = 56 # int | Id of the parcelInvoiceLine to add an audit to
parcel_invoice_line_audit = 'parcel_invoice_line_audit_example' # str | The audit to add

try:
    # Add new audit for a parcelInvoiceLine
    api_instance.add_parcel_invoice_line_audit(parcel_invoice_line_id, parcel_invoice_line_audit)
except ApiException as e:
    print("Exception when calling ParcelInvoiceLineApi->add_parcel_invoice_line_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_line_id** | **int**| Id of the parcelInvoiceLine to add an audit to | 
 **parcel_invoice_line_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_parcel_invoice_line_file**
> add_parcel_invoice_line_file(parcel_invoice_line_id, file_name)

Attach a file to a parcelInvoiceLine

Adds a file to an existing parcelInvoiceLine.

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
api_instance = Infoplus.ParcelInvoiceLineApi(Infoplus.ApiClient(configuration))
parcel_invoice_line_id = 56 # int | Id of the parcelInvoiceLine to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a parcelInvoiceLine
    api_instance.add_parcel_invoice_line_file(parcel_invoice_line_id, file_name)
except ApiException as e:
    print("Exception when calling ParcelInvoiceLineApi->add_parcel_invoice_line_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_line_id** | **int**| Id of the parcelInvoiceLine to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_parcel_invoice_line_file_by_url**
> add_parcel_invoice_line_file_by_url(body, parcel_invoice_line_id)

Attach a file to a parcelInvoiceLine by URL.

Adds a file to an existing parcelInvoiceLine by URL.

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
api_instance = Infoplus.ParcelInvoiceLineApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
parcel_invoice_line_id = 56 # int | Id of the parcelInvoiceLine to add an file to

try:
    # Attach a file to a parcelInvoiceLine by URL.
    api_instance.add_parcel_invoice_line_file_by_url(body, parcel_invoice_line_id)
except ApiException as e:
    print("Exception when calling ParcelInvoiceLineApi->add_parcel_invoice_line_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **parcel_invoice_line_id** | **int**| Id of the parcelInvoiceLine to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_parcel_invoice_line_tag**
> add_parcel_invoice_line_tag(parcel_invoice_line_id, parcel_invoice_line_tag)

Add new tags for a parcelInvoiceLine.

Adds a tag to an existing parcelInvoiceLine.

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
api_instance = Infoplus.ParcelInvoiceLineApi(Infoplus.ApiClient(configuration))
parcel_invoice_line_id = 56 # int | Id of the parcelInvoiceLine to add a tag to
parcel_invoice_line_tag = 'parcel_invoice_line_tag_example' # str | The tag to add

try:
    # Add new tags for a parcelInvoiceLine.
    api_instance.add_parcel_invoice_line_tag(parcel_invoice_line_id, parcel_invoice_line_tag)
except ApiException as e:
    print("Exception when calling ParcelInvoiceLineApi->add_parcel_invoice_line_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_line_id** | **int**| Id of the parcelInvoiceLine to add a tag to | 
 **parcel_invoice_line_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_parcel_invoice_line_file**
> delete_parcel_invoice_line_file(parcel_invoice_line_id, file_id)

Delete a file for a parcelInvoiceLine.

Deletes an existing parcelInvoiceLine file using the specified data.

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
api_instance = Infoplus.ParcelInvoiceLineApi(Infoplus.ApiClient(configuration))
parcel_invoice_line_id = 56 # int | Id of the parcelInvoiceLine to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a parcelInvoiceLine.
    api_instance.delete_parcel_invoice_line_file(parcel_invoice_line_id, file_id)
except ApiException as e:
    print("Exception when calling ParcelInvoiceLineApi->delete_parcel_invoice_line_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_line_id** | **int**| Id of the parcelInvoiceLine to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_parcel_invoice_line_tag**
> delete_parcel_invoice_line_tag(parcel_invoice_line_id, parcel_invoice_line_tag)

Delete a tag for a parcelInvoiceLine.

Deletes an existing parcelInvoiceLine tag using the specified data.

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
api_instance = Infoplus.ParcelInvoiceLineApi(Infoplus.ApiClient(configuration))
parcel_invoice_line_id = 56 # int | Id of the parcelInvoiceLine to remove tag from
parcel_invoice_line_tag = 'parcel_invoice_line_tag_example' # str | The tag to delete

try:
    # Delete a tag for a parcelInvoiceLine.
    api_instance.delete_parcel_invoice_line_tag(parcel_invoice_line_id, parcel_invoice_line_tag)
except ApiException as e:
    print("Exception when calling ParcelInvoiceLineApi->delete_parcel_invoice_line_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_line_id** | **int**| Id of the parcelInvoiceLine to remove tag from | 
 **parcel_invoice_line_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_parcel_invoice_line_by_id**
> ParcelInvoiceLine get_duplicate_parcel_invoice_line_by_id(parcel_invoice_line_id)

Get a duplicated a parcelInvoiceLine by id

Returns a duplicated parcelInvoiceLine identified by the specified id.

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
api_instance = Infoplus.ParcelInvoiceLineApi(Infoplus.ApiClient(configuration))
parcel_invoice_line_id = 56 # int | Id of the parcelInvoiceLine to be duplicated.

try:
    # Get a duplicated a parcelInvoiceLine by id
    api_response = api_instance.get_duplicate_parcel_invoice_line_by_id(parcel_invoice_line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParcelInvoiceLineApi->get_duplicate_parcel_invoice_line_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_line_id** | **int**| Id of the parcelInvoiceLine to be duplicated. | 

### Return type

[**ParcelInvoiceLine**](ParcelInvoiceLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parcel_invoice_line_by_filter**
> list[ParcelInvoiceLine] get_parcel_invoice_line_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search parcelInvoiceLines by filter

Returns the list of parcelInvoiceLines that match the given filter.

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
api_instance = Infoplus.ParcelInvoiceLineApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search parcelInvoiceLines by filter
    api_response = api_instance.get_parcel_invoice_line_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParcelInvoiceLineApi->get_parcel_invoice_line_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ParcelInvoiceLine]**](ParcelInvoiceLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parcel_invoice_line_by_id**
> ParcelInvoiceLine get_parcel_invoice_line_by_id(parcel_invoice_line_id)

Get a parcelInvoiceLine by id

Returns the parcelInvoiceLine identified by the specified id.

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
api_instance = Infoplus.ParcelInvoiceLineApi(Infoplus.ApiClient(configuration))
parcel_invoice_line_id = 56 # int | Id of the parcelInvoiceLine to be returned.

try:
    # Get a parcelInvoiceLine by id
    api_response = api_instance.get_parcel_invoice_line_by_id(parcel_invoice_line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParcelInvoiceLineApi->get_parcel_invoice_line_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_line_id** | **int**| Id of the parcelInvoiceLine to be returned. | 

### Return type

[**ParcelInvoiceLine**](ParcelInvoiceLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parcel_invoice_line_files**
> get_parcel_invoice_line_files(parcel_invoice_line_id)

Get the files for a parcelInvoiceLine.

Get all existing parcelInvoiceLine files.

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
api_instance = Infoplus.ParcelInvoiceLineApi(Infoplus.ApiClient(configuration))
parcel_invoice_line_id = 56 # int | Id of the parcelInvoiceLine to get files for

try:
    # Get the files for a parcelInvoiceLine.
    api_instance.get_parcel_invoice_line_files(parcel_invoice_line_id)
except ApiException as e:
    print("Exception when calling ParcelInvoiceLineApi->get_parcel_invoice_line_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_line_id** | **int**| Id of the parcelInvoiceLine to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parcel_invoice_line_tags**
> get_parcel_invoice_line_tags(parcel_invoice_line_id)

Get the tags for a parcelInvoiceLine.

Get all existing parcelInvoiceLine tags.

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
api_instance = Infoplus.ParcelInvoiceLineApi(Infoplus.ApiClient(configuration))
parcel_invoice_line_id = 56 # int | Id of the parcelInvoiceLine to get tags for

try:
    # Get the tags for a parcelInvoiceLine.
    api_instance.get_parcel_invoice_line_tags(parcel_invoice_line_id)
except ApiException as e:
    print("Exception when calling ParcelInvoiceLineApi->get_parcel_invoice_line_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_invoice_line_id** | **int**| Id of the parcelInvoiceLine to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_parcel_invoice_line**
> update_parcel_invoice_line(body)

Update a parcelInvoiceLine

Updates an existing parcelInvoiceLine using the specified data.

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
api_instance = Infoplus.ParcelInvoiceLineApi(Infoplus.ApiClient(configuration))
body = Infoplus.ParcelInvoiceLine() # ParcelInvoiceLine | ParcelInvoiceLine to be updated.

try:
    # Update a parcelInvoiceLine
    api_instance.update_parcel_invoice_line(body)
except ApiException as e:
    print("Exception when calling ParcelInvoiceLineApi->update_parcel_invoice_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParcelInvoiceLine**](ParcelInvoiceLine.md)| ParcelInvoiceLine to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

