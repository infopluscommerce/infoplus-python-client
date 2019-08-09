# Infoplus.InvoiceWorksheetApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_invoice_worksheet**](InvoiceWorksheetApi.md#add_invoice_worksheet) | **POST** /beta/invoiceWorksheet | Create an invoiceWorksheet
[**add_invoice_worksheet_audit**](InvoiceWorksheetApi.md#add_invoice_worksheet_audit) | **PUT** /beta/invoiceWorksheet/{invoiceWorksheetId}/audit/{invoiceWorksheetAudit} | Add new audit for an invoiceWorksheet
[**add_invoice_worksheet_file**](InvoiceWorksheetApi.md#add_invoice_worksheet_file) | **POST** /beta/invoiceWorksheet/{invoiceWorksheetId}/file/{fileName} | Attach a file to an invoiceWorksheet
[**add_invoice_worksheet_tag**](InvoiceWorksheetApi.md#add_invoice_worksheet_tag) | **PUT** /beta/invoiceWorksheet/{invoiceWorksheetId}/tag/{invoiceWorksheetTag} | Add new tags for an invoiceWorksheet.
[**delete_invoice_worksheet**](InvoiceWorksheetApi.md#delete_invoice_worksheet) | **DELETE** /beta/invoiceWorksheet/{invoiceWorksheetId} | Delete an invoiceWorksheet
[**delete_invoice_worksheet_tag**](InvoiceWorksheetApi.md#delete_invoice_worksheet_tag) | **DELETE** /beta/invoiceWorksheet/{invoiceWorksheetId}/tag/{invoiceWorksheetTag} | Delete a tag for an invoiceWorksheet.
[**get_duplicate_invoice_worksheet_by_id**](InvoiceWorksheetApi.md#get_duplicate_invoice_worksheet_by_id) | **GET** /beta/invoiceWorksheet/duplicate/{invoiceWorksheetId} | Get a duplicated an invoiceWorksheet by id
[**get_invoice_worksheet_by_filter**](InvoiceWorksheetApi.md#get_invoice_worksheet_by_filter) | **GET** /beta/invoiceWorksheet/search | Search invoiceWorksheets by filter
[**get_invoice_worksheet_by_id**](InvoiceWorksheetApi.md#get_invoice_worksheet_by_id) | **GET** /beta/invoiceWorksheet/{invoiceWorksheetId} | Get an invoiceWorksheet by id
[**get_invoice_worksheet_tags**](InvoiceWorksheetApi.md#get_invoice_worksheet_tags) | **GET** /beta/invoiceWorksheet/{invoiceWorksheetId}/tag | Get the tags for an invoiceWorksheet.
[**update_invoice_worksheet**](InvoiceWorksheetApi.md#update_invoice_worksheet) | **PUT** /beta/invoiceWorksheet | Update an invoiceWorksheet


# **add_invoice_worksheet**
> InvoiceWorksheet add_invoice_worksheet(body)

Create an invoiceWorksheet

Inserts a new invoiceWorksheet using the specified data.

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
api_instance = Infoplus.InvoiceWorksheetApi(Infoplus.ApiClient(configuration))
body = Infoplus.InvoiceWorksheet() # InvoiceWorksheet | InvoiceWorksheet to be inserted.

try:
    # Create an invoiceWorksheet
    api_response = api_instance.add_invoice_worksheet(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetApi->add_invoice_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoiceWorksheet**](InvoiceWorksheet.md)| InvoiceWorksheet to be inserted. | 

### Return type

[**InvoiceWorksheet**](InvoiceWorksheet.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_invoice_worksheet_audit**
> add_invoice_worksheet_audit(invoice_worksheet_id, invoice_worksheet_audit)

Add new audit for an invoiceWorksheet

Adds an audit to an existing invoiceWorksheet.

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
api_instance = Infoplus.InvoiceWorksheetApi(Infoplus.ApiClient(configuration))
invoice_worksheet_id = 56 # int | Id of the invoiceWorksheet to add an audit to
invoice_worksheet_audit = 'invoice_worksheet_audit_example' # str | The audit to add

try:
    # Add new audit for an invoiceWorksheet
    api_instance.add_invoice_worksheet_audit(invoice_worksheet_id, invoice_worksheet_audit)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetApi->add_invoice_worksheet_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_id** | **int**| Id of the invoiceWorksheet to add an audit to | 
 **invoice_worksheet_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_invoice_worksheet_file**
> add_invoice_worksheet_file(invoice_worksheet_id, file_name)

Attach a file to an invoiceWorksheet

Adds a file to an existing invoiceWorksheet.

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
api_instance = Infoplus.InvoiceWorksheetApi(Infoplus.ApiClient(configuration))
invoice_worksheet_id = 56 # int | Id of the invoiceWorksheet to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an invoiceWorksheet
    api_instance.add_invoice_worksheet_file(invoice_worksheet_id, file_name)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetApi->add_invoice_worksheet_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_id** | **int**| Id of the invoiceWorksheet to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_invoice_worksheet_tag**
> add_invoice_worksheet_tag(invoice_worksheet_id, invoice_worksheet_tag)

Add new tags for an invoiceWorksheet.

Adds a tag to an existing invoiceWorksheet.

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
api_instance = Infoplus.InvoiceWorksheetApi(Infoplus.ApiClient(configuration))
invoice_worksheet_id = 56 # int | Id of the invoiceWorksheet to add a tag to
invoice_worksheet_tag = 'invoice_worksheet_tag_example' # str | The tag to add

try:
    # Add new tags for an invoiceWorksheet.
    api_instance.add_invoice_worksheet_tag(invoice_worksheet_id, invoice_worksheet_tag)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetApi->add_invoice_worksheet_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_id** | **int**| Id of the invoiceWorksheet to add a tag to | 
 **invoice_worksheet_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice_worksheet**
> delete_invoice_worksheet(invoice_worksheet_id)

Delete an invoiceWorksheet

Deletes the invoiceWorksheet identified by the specified id.

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
api_instance = Infoplus.InvoiceWorksheetApi(Infoplus.ApiClient(configuration))
invoice_worksheet_id = 56 # int | Id of the invoiceWorksheet to be deleted.

try:
    # Delete an invoiceWorksheet
    api_instance.delete_invoice_worksheet(invoice_worksheet_id)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetApi->delete_invoice_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_id** | **int**| Id of the invoiceWorksheet to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice_worksheet_tag**
> delete_invoice_worksheet_tag(invoice_worksheet_id, invoice_worksheet_tag)

Delete a tag for an invoiceWorksheet.

Deletes an existing invoiceWorksheet tag using the specified data.

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
api_instance = Infoplus.InvoiceWorksheetApi(Infoplus.ApiClient(configuration))
invoice_worksheet_id = 56 # int | Id of the invoiceWorksheet to remove tag from
invoice_worksheet_tag = 'invoice_worksheet_tag_example' # str | The tag to delete

try:
    # Delete a tag for an invoiceWorksheet.
    api_instance.delete_invoice_worksheet_tag(invoice_worksheet_id, invoice_worksheet_tag)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetApi->delete_invoice_worksheet_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_id** | **int**| Id of the invoiceWorksheet to remove tag from | 
 **invoice_worksheet_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_invoice_worksheet_by_id**
> InvoiceWorksheet get_duplicate_invoice_worksheet_by_id(invoice_worksheet_id)

Get a duplicated an invoiceWorksheet by id

Returns a duplicated invoiceWorksheet identified by the specified id.

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
api_instance = Infoplus.InvoiceWorksheetApi(Infoplus.ApiClient(configuration))
invoice_worksheet_id = 56 # int | Id of the invoiceWorksheet to be duplicated.

try:
    # Get a duplicated an invoiceWorksheet by id
    api_response = api_instance.get_duplicate_invoice_worksheet_by_id(invoice_worksheet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetApi->get_duplicate_invoice_worksheet_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_id** | **int**| Id of the invoiceWorksheet to be duplicated. | 

### Return type

[**InvoiceWorksheet**](InvoiceWorksheet.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_worksheet_by_filter**
> list[InvoiceWorksheet] get_invoice_worksheet_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search invoiceWorksheets by filter

Returns the list of invoiceWorksheets that match the given filter.

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
api_instance = Infoplus.InvoiceWorksheetApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search invoiceWorksheets by filter
    api_response = api_instance.get_invoice_worksheet_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetApi->get_invoice_worksheet_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[InvoiceWorksheet]**](InvoiceWorksheet.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_worksheet_by_id**
> InvoiceWorksheet get_invoice_worksheet_by_id(invoice_worksheet_id)

Get an invoiceWorksheet by id

Returns the invoiceWorksheet identified by the specified id.

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
api_instance = Infoplus.InvoiceWorksheetApi(Infoplus.ApiClient(configuration))
invoice_worksheet_id = 56 # int | Id of the invoiceWorksheet to be returned.

try:
    # Get an invoiceWorksheet by id
    api_response = api_instance.get_invoice_worksheet_by_id(invoice_worksheet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetApi->get_invoice_worksheet_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_id** | **int**| Id of the invoiceWorksheet to be returned. | 

### Return type

[**InvoiceWorksheet**](InvoiceWorksheet.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_worksheet_tags**
> get_invoice_worksheet_tags(invoice_worksheet_id)

Get the tags for an invoiceWorksheet.

Get all existing invoiceWorksheet tags.

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
api_instance = Infoplus.InvoiceWorksheetApi(Infoplus.ApiClient(configuration))
invoice_worksheet_id = 56 # int | Id of the invoiceWorksheet to get tags for

try:
    # Get the tags for an invoiceWorksheet.
    api_instance.get_invoice_worksheet_tags(invoice_worksheet_id)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetApi->get_invoice_worksheet_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_id** | **int**| Id of the invoiceWorksheet to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_worksheet**
> update_invoice_worksheet(body)

Update an invoiceWorksheet

Updates an existing invoiceWorksheet using the specified data.

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
api_instance = Infoplus.InvoiceWorksheetApi(Infoplus.ApiClient(configuration))
body = Infoplus.InvoiceWorksheet() # InvoiceWorksheet | InvoiceWorksheet to be updated.

try:
    # Update an invoiceWorksheet
    api_instance.update_invoice_worksheet(body)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetApi->update_invoice_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoiceWorksheet**](InvoiceWorksheet.md)| InvoiceWorksheet to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

