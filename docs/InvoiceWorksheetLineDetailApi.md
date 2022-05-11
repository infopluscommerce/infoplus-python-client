# Infoplus.InvoiceWorksheetLineDetailApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_invoice_worksheet_line_detail_audit**](InvoiceWorksheetLineDetailApi.md#add_invoice_worksheet_line_detail_audit) | **PUT** /v3.0/invoiceWorksheetLineDetail/{invoiceWorksheetLineDetailId}/audit/{invoiceWorksheetLineDetailAudit} | Add new audit for an invoiceWorksheetLineDetail
[**add_invoice_worksheet_line_detail_file**](InvoiceWorksheetLineDetailApi.md#add_invoice_worksheet_line_detail_file) | **POST** /v3.0/invoiceWorksheetLineDetail/{invoiceWorksheetLineDetailId}/file/{fileName} | Attach a file to an invoiceWorksheetLineDetail
[**add_invoice_worksheet_line_detail_file_by_url**](InvoiceWorksheetLineDetailApi.md#add_invoice_worksheet_line_detail_file_by_url) | **POST** /v3.0/invoiceWorksheetLineDetail/{invoiceWorksheetLineDetailId}/file | Attach a file to an invoiceWorksheetLineDetail by URL.
[**add_invoice_worksheet_line_detail_tag**](InvoiceWorksheetLineDetailApi.md#add_invoice_worksheet_line_detail_tag) | **PUT** /v3.0/invoiceWorksheetLineDetail/{invoiceWorksheetLineDetailId}/tag/{invoiceWorksheetLineDetailTag} | Add new tags for an invoiceWorksheetLineDetail.
[**delete_invoice_worksheet_line_detail_file**](InvoiceWorksheetLineDetailApi.md#delete_invoice_worksheet_line_detail_file) | **DELETE** /v3.0/invoiceWorksheetLineDetail/{invoiceWorksheetLineDetailId}/file/{fileId} | Delete a file for an invoiceWorksheetLineDetail.
[**delete_invoice_worksheet_line_detail_tag**](InvoiceWorksheetLineDetailApi.md#delete_invoice_worksheet_line_detail_tag) | **DELETE** /v3.0/invoiceWorksheetLineDetail/{invoiceWorksheetLineDetailId}/tag/{invoiceWorksheetLineDetailTag} | Delete a tag for an invoiceWorksheetLineDetail.
[**get_duplicate_invoice_worksheet_line_detail_by_id**](InvoiceWorksheetLineDetailApi.md#get_duplicate_invoice_worksheet_line_detail_by_id) | **GET** /v3.0/invoiceWorksheetLineDetail/duplicate/{invoiceWorksheetLineDetailId} | Get a duplicated an invoiceWorksheetLineDetail by id
[**get_invoice_worksheet_line_detail_by_filter**](InvoiceWorksheetLineDetailApi.md#get_invoice_worksheet_line_detail_by_filter) | **GET** /v3.0/invoiceWorksheetLineDetail/search | Search invoiceWorksheetLineDetails by filter
[**get_invoice_worksheet_line_detail_by_id**](InvoiceWorksheetLineDetailApi.md#get_invoice_worksheet_line_detail_by_id) | **GET** /v3.0/invoiceWorksheetLineDetail/{invoiceWorksheetLineDetailId} | Get an invoiceWorksheetLineDetail by id
[**get_invoice_worksheet_line_detail_files**](InvoiceWorksheetLineDetailApi.md#get_invoice_worksheet_line_detail_files) | **GET** /v3.0/invoiceWorksheetLineDetail/{invoiceWorksheetLineDetailId}/file | Get the files for an invoiceWorksheetLineDetail.
[**get_invoice_worksheet_line_detail_tags**](InvoiceWorksheetLineDetailApi.md#get_invoice_worksheet_line_detail_tags) | **GET** /v3.0/invoiceWorksheetLineDetail/{invoiceWorksheetLineDetailId}/tag | Get the tags for an invoiceWorksheetLineDetail.
[**update_invoice_worksheet_line_detail_custom_fields**](InvoiceWorksheetLineDetailApi.md#update_invoice_worksheet_line_detail_custom_fields) | **PUT** /v3.0/invoiceWorksheetLineDetail/customFields | Update an invoiceWorksheetLineDetail custom fields


# **add_invoice_worksheet_line_detail_audit**
> add_invoice_worksheet_line_detail_audit(invoice_worksheet_line_detail_id, invoice_worksheet_line_detail_audit)

Add new audit for an invoiceWorksheetLineDetail

Adds an audit to an existing invoiceWorksheetLineDetail.

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
api_instance = Infoplus.InvoiceWorksheetLineDetailApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_detail_id = 56 # int | Id of the invoiceWorksheetLineDetail to add an audit to
invoice_worksheet_line_detail_audit = 'invoice_worksheet_line_detail_audit_example' # str | The audit to add

try:
    # Add new audit for an invoiceWorksheetLineDetail
    api_instance.add_invoice_worksheet_line_detail_audit(invoice_worksheet_line_detail_id, invoice_worksheet_line_detail_audit)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineDetailApi->add_invoice_worksheet_line_detail_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_detail_id** | **int**| Id of the invoiceWorksheetLineDetail to add an audit to | 
 **invoice_worksheet_line_detail_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_invoice_worksheet_line_detail_file**
> add_invoice_worksheet_line_detail_file(invoice_worksheet_line_detail_id, file_name)

Attach a file to an invoiceWorksheetLineDetail

Adds a file to an existing invoiceWorksheetLineDetail.

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
api_instance = Infoplus.InvoiceWorksheetLineDetailApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_detail_id = 56 # int | Id of the invoiceWorksheetLineDetail to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an invoiceWorksheetLineDetail
    api_instance.add_invoice_worksheet_line_detail_file(invoice_worksheet_line_detail_id, file_name)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineDetailApi->add_invoice_worksheet_line_detail_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_detail_id** | **int**| Id of the invoiceWorksheetLineDetail to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_invoice_worksheet_line_detail_file_by_url**
> add_invoice_worksheet_line_detail_file_by_url(body, invoice_worksheet_line_detail_id)

Attach a file to an invoiceWorksheetLineDetail by URL.

Adds a file to an existing invoiceWorksheetLineDetail by URL.

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
api_instance = Infoplus.InvoiceWorksheetLineDetailApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
invoice_worksheet_line_detail_id = 56 # int | Id of the invoiceWorksheetLineDetail to add an file to

try:
    # Attach a file to an invoiceWorksheetLineDetail by URL.
    api_instance.add_invoice_worksheet_line_detail_file_by_url(body, invoice_worksheet_line_detail_id)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineDetailApi->add_invoice_worksheet_line_detail_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **invoice_worksheet_line_detail_id** | **int**| Id of the invoiceWorksheetLineDetail to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_invoice_worksheet_line_detail_tag**
> add_invoice_worksheet_line_detail_tag(invoice_worksheet_line_detail_id, invoice_worksheet_line_detail_tag)

Add new tags for an invoiceWorksheetLineDetail.

Adds a tag to an existing invoiceWorksheetLineDetail.

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
api_instance = Infoplus.InvoiceWorksheetLineDetailApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_detail_id = 56 # int | Id of the invoiceWorksheetLineDetail to add a tag to
invoice_worksheet_line_detail_tag = 'invoice_worksheet_line_detail_tag_example' # str | The tag to add

try:
    # Add new tags for an invoiceWorksheetLineDetail.
    api_instance.add_invoice_worksheet_line_detail_tag(invoice_worksheet_line_detail_id, invoice_worksheet_line_detail_tag)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineDetailApi->add_invoice_worksheet_line_detail_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_detail_id** | **int**| Id of the invoiceWorksheetLineDetail to add a tag to | 
 **invoice_worksheet_line_detail_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice_worksheet_line_detail_file**
> delete_invoice_worksheet_line_detail_file(invoice_worksheet_line_detail_id, file_id)

Delete a file for an invoiceWorksheetLineDetail.

Deletes an existing invoiceWorksheetLineDetail file using the specified data.

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
api_instance = Infoplus.InvoiceWorksheetLineDetailApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_detail_id = 56 # int | Id of the invoiceWorksheetLineDetail to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an invoiceWorksheetLineDetail.
    api_instance.delete_invoice_worksheet_line_detail_file(invoice_worksheet_line_detail_id, file_id)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineDetailApi->delete_invoice_worksheet_line_detail_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_detail_id** | **int**| Id of the invoiceWorksheetLineDetail to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice_worksheet_line_detail_tag**
> delete_invoice_worksheet_line_detail_tag(invoice_worksheet_line_detail_id, invoice_worksheet_line_detail_tag)

Delete a tag for an invoiceWorksheetLineDetail.

Deletes an existing invoiceWorksheetLineDetail tag using the specified data.

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
api_instance = Infoplus.InvoiceWorksheetLineDetailApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_detail_id = 56 # int | Id of the invoiceWorksheetLineDetail to remove tag from
invoice_worksheet_line_detail_tag = 'invoice_worksheet_line_detail_tag_example' # str | The tag to delete

try:
    # Delete a tag for an invoiceWorksheetLineDetail.
    api_instance.delete_invoice_worksheet_line_detail_tag(invoice_worksheet_line_detail_id, invoice_worksheet_line_detail_tag)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineDetailApi->delete_invoice_worksheet_line_detail_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_detail_id** | **int**| Id of the invoiceWorksheetLineDetail to remove tag from | 
 **invoice_worksheet_line_detail_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_invoice_worksheet_line_detail_by_id**
> InvoiceWorksheetLineDetail get_duplicate_invoice_worksheet_line_detail_by_id(invoice_worksheet_line_detail_id)

Get a duplicated an invoiceWorksheetLineDetail by id

Returns a duplicated invoiceWorksheetLineDetail identified by the specified id.

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
api_instance = Infoplus.InvoiceWorksheetLineDetailApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_detail_id = 56 # int | Id of the invoiceWorksheetLineDetail to be duplicated.

try:
    # Get a duplicated an invoiceWorksheetLineDetail by id
    api_response = api_instance.get_duplicate_invoice_worksheet_line_detail_by_id(invoice_worksheet_line_detail_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineDetailApi->get_duplicate_invoice_worksheet_line_detail_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_detail_id** | **int**| Id of the invoiceWorksheetLineDetail to be duplicated. | 

### Return type

[**InvoiceWorksheetLineDetail**](InvoiceWorksheetLineDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_worksheet_line_detail_by_filter**
> list[InvoiceWorksheetLineDetail] get_invoice_worksheet_line_detail_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search invoiceWorksheetLineDetails by filter

Returns the list of invoiceWorksheetLineDetails that match the given filter.

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
api_instance = Infoplus.InvoiceWorksheetLineDetailApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search invoiceWorksheetLineDetails by filter
    api_response = api_instance.get_invoice_worksheet_line_detail_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineDetailApi->get_invoice_worksheet_line_detail_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[InvoiceWorksheetLineDetail]**](InvoiceWorksheetLineDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_worksheet_line_detail_by_id**
> InvoiceWorksheetLineDetail get_invoice_worksheet_line_detail_by_id(invoice_worksheet_line_detail_id)

Get an invoiceWorksheetLineDetail by id

Returns the invoiceWorksheetLineDetail identified by the specified id.

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
api_instance = Infoplus.InvoiceWorksheetLineDetailApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_detail_id = 56 # int | Id of the invoiceWorksheetLineDetail to be returned.

try:
    # Get an invoiceWorksheetLineDetail by id
    api_response = api_instance.get_invoice_worksheet_line_detail_by_id(invoice_worksheet_line_detail_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineDetailApi->get_invoice_worksheet_line_detail_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_detail_id** | **int**| Id of the invoiceWorksheetLineDetail to be returned. | 

### Return type

[**InvoiceWorksheetLineDetail**](InvoiceWorksheetLineDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_worksheet_line_detail_files**
> get_invoice_worksheet_line_detail_files(invoice_worksheet_line_detail_id)

Get the files for an invoiceWorksheetLineDetail.

Get all existing invoiceWorksheetLineDetail files.

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
api_instance = Infoplus.InvoiceWorksheetLineDetailApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_detail_id = 56 # int | Id of the invoiceWorksheetLineDetail to get files for

try:
    # Get the files for an invoiceWorksheetLineDetail.
    api_instance.get_invoice_worksheet_line_detail_files(invoice_worksheet_line_detail_id)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineDetailApi->get_invoice_worksheet_line_detail_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_detail_id** | **int**| Id of the invoiceWorksheetLineDetail to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_worksheet_line_detail_tags**
> get_invoice_worksheet_line_detail_tags(invoice_worksheet_line_detail_id)

Get the tags for an invoiceWorksheetLineDetail.

Get all existing invoiceWorksheetLineDetail tags.

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
api_instance = Infoplus.InvoiceWorksheetLineDetailApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_detail_id = 56 # int | Id of the invoiceWorksheetLineDetail to get tags for

try:
    # Get the tags for an invoiceWorksheetLineDetail.
    api_instance.get_invoice_worksheet_line_detail_tags(invoice_worksheet_line_detail_id)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineDetailApi->get_invoice_worksheet_line_detail_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_detail_id** | **int**| Id of the invoiceWorksheetLineDetail to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_worksheet_line_detail_custom_fields**
> update_invoice_worksheet_line_detail_custom_fields(body)

Update an invoiceWorksheetLineDetail custom fields

Updates an existing invoiceWorksheetLineDetail custom fields using the specified data.

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
api_instance = Infoplus.InvoiceWorksheetLineDetailApi(Infoplus.ApiClient(configuration))
body = Infoplus.InvoiceWorksheetLineDetail() # InvoiceWorksheetLineDetail | InvoiceWorksheetLineDetail to be updated.

try:
    # Update an invoiceWorksheetLineDetail custom fields
    api_instance.update_invoice_worksheet_line_detail_custom_fields(body)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineDetailApi->update_invoice_worksheet_line_detail_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoiceWorksheetLineDetail**](InvoiceWorksheetLineDetail.md)| InvoiceWorksheetLineDetail to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

