# Infoplus.InvoiceWorksheetLineApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_invoice_worksheet_line**](InvoiceWorksheetLineApi.md#add_invoice_worksheet_line) | **POST** /v3.0/invoiceWorksheetLine | Create an invoiceWorksheetLine
[**add_invoice_worksheet_line_audit**](InvoiceWorksheetLineApi.md#add_invoice_worksheet_line_audit) | **PUT** /v3.0/invoiceWorksheetLine/{invoiceWorksheetLineId}/audit/{invoiceWorksheetLineAudit} | Add new audit for an invoiceWorksheetLine
[**add_invoice_worksheet_line_file**](InvoiceWorksheetLineApi.md#add_invoice_worksheet_line_file) | **POST** /v3.0/invoiceWorksheetLine/{invoiceWorksheetLineId}/file/{fileName} | Attach a file to an invoiceWorksheetLine
[**add_invoice_worksheet_line_file_by_url**](InvoiceWorksheetLineApi.md#add_invoice_worksheet_line_file_by_url) | **POST** /v3.0/invoiceWorksheetLine/{invoiceWorksheetLineId}/file | Attach a file to an invoiceWorksheetLine by URL.
[**add_invoice_worksheet_line_tag**](InvoiceWorksheetLineApi.md#add_invoice_worksheet_line_tag) | **PUT** /v3.0/invoiceWorksheetLine/{invoiceWorksheetLineId}/tag/{invoiceWorksheetLineTag} | Add new tags for an invoiceWorksheetLine.
[**delete_invoice_worksheet_line**](InvoiceWorksheetLineApi.md#delete_invoice_worksheet_line) | **DELETE** /v3.0/invoiceWorksheetLine/{invoiceWorksheetLineId} | Delete an invoiceWorksheetLine
[**delete_invoice_worksheet_line_file**](InvoiceWorksheetLineApi.md#delete_invoice_worksheet_line_file) | **DELETE** /v3.0/invoiceWorksheetLine/{invoiceWorksheetLineId}/file/{fileId} | Delete a file for an invoiceWorksheetLine.
[**delete_invoice_worksheet_line_tag**](InvoiceWorksheetLineApi.md#delete_invoice_worksheet_line_tag) | **DELETE** /v3.0/invoiceWorksheetLine/{invoiceWorksheetLineId}/tag/{invoiceWorksheetLineTag} | Delete a tag for an invoiceWorksheetLine.
[**get_duplicate_invoice_worksheet_line_by_id**](InvoiceWorksheetLineApi.md#get_duplicate_invoice_worksheet_line_by_id) | **GET** /v3.0/invoiceWorksheetLine/duplicate/{invoiceWorksheetLineId} | Get a duplicated an invoiceWorksheetLine by id
[**get_invoice_worksheet_line_by_filter**](InvoiceWorksheetLineApi.md#get_invoice_worksheet_line_by_filter) | **GET** /v3.0/invoiceWorksheetLine/search | Search invoiceWorksheetLines by filter
[**get_invoice_worksheet_line_by_id**](InvoiceWorksheetLineApi.md#get_invoice_worksheet_line_by_id) | **GET** /v3.0/invoiceWorksheetLine/{invoiceWorksheetLineId} | Get an invoiceWorksheetLine by id
[**get_invoice_worksheet_line_files**](InvoiceWorksheetLineApi.md#get_invoice_worksheet_line_files) | **GET** /v3.0/invoiceWorksheetLine/{invoiceWorksheetLineId}/file | Get the files for an invoiceWorksheetLine.
[**get_invoice_worksheet_line_tags**](InvoiceWorksheetLineApi.md#get_invoice_worksheet_line_tags) | **GET** /v3.0/invoiceWorksheetLine/{invoiceWorksheetLineId}/tag | Get the tags for an invoiceWorksheetLine.
[**update_invoice_worksheet_line**](InvoiceWorksheetLineApi.md#update_invoice_worksheet_line) | **PUT** /v3.0/invoiceWorksheetLine | Update an invoiceWorksheetLine


# **add_invoice_worksheet_line**
> InvoiceWorksheetLine add_invoice_worksheet_line(body)

Create an invoiceWorksheetLine

Inserts a new invoiceWorksheetLine using the specified data.

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
api_instance = Infoplus.InvoiceWorksheetLineApi(Infoplus.ApiClient(configuration))
body = Infoplus.InvoiceWorksheetLine() # InvoiceWorksheetLine | InvoiceWorksheetLine to be inserted.

try:
    # Create an invoiceWorksheetLine
    api_response = api_instance.add_invoice_worksheet_line(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineApi->add_invoice_worksheet_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoiceWorksheetLine**](InvoiceWorksheetLine.md)| InvoiceWorksheetLine to be inserted. | 

### Return type

[**InvoiceWorksheetLine**](InvoiceWorksheetLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_invoice_worksheet_line_audit**
> add_invoice_worksheet_line_audit(invoice_worksheet_line_id, invoice_worksheet_line_audit)

Add new audit for an invoiceWorksheetLine

Adds an audit to an existing invoiceWorksheetLine.

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
api_instance = Infoplus.InvoiceWorksheetLineApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_id = 56 # int | Id of the invoiceWorksheetLine to add an audit to
invoice_worksheet_line_audit = 'invoice_worksheet_line_audit_example' # str | The audit to add

try:
    # Add new audit for an invoiceWorksheetLine
    api_instance.add_invoice_worksheet_line_audit(invoice_worksheet_line_id, invoice_worksheet_line_audit)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineApi->add_invoice_worksheet_line_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_id** | **int**| Id of the invoiceWorksheetLine to add an audit to | 
 **invoice_worksheet_line_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_invoice_worksheet_line_file**
> add_invoice_worksheet_line_file(invoice_worksheet_line_id, file_name)

Attach a file to an invoiceWorksheetLine

Adds a file to an existing invoiceWorksheetLine.

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
api_instance = Infoplus.InvoiceWorksheetLineApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_id = 56 # int | Id of the invoiceWorksheetLine to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an invoiceWorksheetLine
    api_instance.add_invoice_worksheet_line_file(invoice_worksheet_line_id, file_name)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineApi->add_invoice_worksheet_line_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_id** | **int**| Id of the invoiceWorksheetLine to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_invoice_worksheet_line_file_by_url**
> add_invoice_worksheet_line_file_by_url(body, invoice_worksheet_line_id)

Attach a file to an invoiceWorksheetLine by URL.

Adds a file to an existing invoiceWorksheetLine by URL.

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
api_instance = Infoplus.InvoiceWorksheetLineApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
invoice_worksheet_line_id = 56 # int | Id of the invoiceWorksheetLine to add an file to

try:
    # Attach a file to an invoiceWorksheetLine by URL.
    api_instance.add_invoice_worksheet_line_file_by_url(body, invoice_worksheet_line_id)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineApi->add_invoice_worksheet_line_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **invoice_worksheet_line_id** | **int**| Id of the invoiceWorksheetLine to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_invoice_worksheet_line_tag**
> add_invoice_worksheet_line_tag(invoice_worksheet_line_id, invoice_worksheet_line_tag)

Add new tags for an invoiceWorksheetLine.

Adds a tag to an existing invoiceWorksheetLine.

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
api_instance = Infoplus.InvoiceWorksheetLineApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_id = 56 # int | Id of the invoiceWorksheetLine to add a tag to
invoice_worksheet_line_tag = 'invoice_worksheet_line_tag_example' # str | The tag to add

try:
    # Add new tags for an invoiceWorksheetLine.
    api_instance.add_invoice_worksheet_line_tag(invoice_worksheet_line_id, invoice_worksheet_line_tag)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineApi->add_invoice_worksheet_line_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_id** | **int**| Id of the invoiceWorksheetLine to add a tag to | 
 **invoice_worksheet_line_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice_worksheet_line**
> delete_invoice_worksheet_line(invoice_worksheet_line_id)

Delete an invoiceWorksheetLine

Deletes the invoiceWorksheetLine identified by the specified id.

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
api_instance = Infoplus.InvoiceWorksheetLineApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_id = 56 # int | Id of the invoiceWorksheetLine to be deleted.

try:
    # Delete an invoiceWorksheetLine
    api_instance.delete_invoice_worksheet_line(invoice_worksheet_line_id)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineApi->delete_invoice_worksheet_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_id** | **int**| Id of the invoiceWorksheetLine to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice_worksheet_line_file**
> delete_invoice_worksheet_line_file(invoice_worksheet_line_id, file_id)

Delete a file for an invoiceWorksheetLine.

Deletes an existing invoiceWorksheetLine file using the specified data.

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
api_instance = Infoplus.InvoiceWorksheetLineApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_id = 56 # int | Id of the invoiceWorksheetLine to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an invoiceWorksheetLine.
    api_instance.delete_invoice_worksheet_line_file(invoice_worksheet_line_id, file_id)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineApi->delete_invoice_worksheet_line_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_id** | **int**| Id of the invoiceWorksheetLine to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice_worksheet_line_tag**
> delete_invoice_worksheet_line_tag(invoice_worksheet_line_id, invoice_worksheet_line_tag)

Delete a tag for an invoiceWorksheetLine.

Deletes an existing invoiceWorksheetLine tag using the specified data.

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
api_instance = Infoplus.InvoiceWorksheetLineApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_id = 56 # int | Id of the invoiceWorksheetLine to remove tag from
invoice_worksheet_line_tag = 'invoice_worksheet_line_tag_example' # str | The tag to delete

try:
    # Delete a tag for an invoiceWorksheetLine.
    api_instance.delete_invoice_worksheet_line_tag(invoice_worksheet_line_id, invoice_worksheet_line_tag)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineApi->delete_invoice_worksheet_line_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_id** | **int**| Id of the invoiceWorksheetLine to remove tag from | 
 **invoice_worksheet_line_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_invoice_worksheet_line_by_id**
> InvoiceWorksheetLine get_duplicate_invoice_worksheet_line_by_id(invoice_worksheet_line_id)

Get a duplicated an invoiceWorksheetLine by id

Returns a duplicated invoiceWorksheetLine identified by the specified id.

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
api_instance = Infoplus.InvoiceWorksheetLineApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_id = 56 # int | Id of the invoiceWorksheetLine to be duplicated.

try:
    # Get a duplicated an invoiceWorksheetLine by id
    api_response = api_instance.get_duplicate_invoice_worksheet_line_by_id(invoice_worksheet_line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineApi->get_duplicate_invoice_worksheet_line_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_id** | **int**| Id of the invoiceWorksheetLine to be duplicated. | 

### Return type

[**InvoiceWorksheetLine**](InvoiceWorksheetLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_worksheet_line_by_filter**
> list[InvoiceWorksheetLine] get_invoice_worksheet_line_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search invoiceWorksheetLines by filter

Returns the list of invoiceWorksheetLines that match the given filter.

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
api_instance = Infoplus.InvoiceWorksheetLineApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search invoiceWorksheetLines by filter
    api_response = api_instance.get_invoice_worksheet_line_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineApi->get_invoice_worksheet_line_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[InvoiceWorksheetLine]**](InvoiceWorksheetLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_worksheet_line_by_id**
> InvoiceWorksheetLine get_invoice_worksheet_line_by_id(invoice_worksheet_line_id)

Get an invoiceWorksheetLine by id

Returns the invoiceWorksheetLine identified by the specified id.

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
api_instance = Infoplus.InvoiceWorksheetLineApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_id = 56 # int | Id of the invoiceWorksheetLine to be returned.

try:
    # Get an invoiceWorksheetLine by id
    api_response = api_instance.get_invoice_worksheet_line_by_id(invoice_worksheet_line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineApi->get_invoice_worksheet_line_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_id** | **int**| Id of the invoiceWorksheetLine to be returned. | 

### Return type

[**InvoiceWorksheetLine**](InvoiceWorksheetLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_worksheet_line_files**
> get_invoice_worksheet_line_files(invoice_worksheet_line_id)

Get the files for an invoiceWorksheetLine.

Get all existing invoiceWorksheetLine files.

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
api_instance = Infoplus.InvoiceWorksheetLineApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_id = 56 # int | Id of the invoiceWorksheetLine to get files for

try:
    # Get the files for an invoiceWorksheetLine.
    api_instance.get_invoice_worksheet_line_files(invoice_worksheet_line_id)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineApi->get_invoice_worksheet_line_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_id** | **int**| Id of the invoiceWorksheetLine to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_worksheet_line_tags**
> get_invoice_worksheet_line_tags(invoice_worksheet_line_id)

Get the tags for an invoiceWorksheetLine.

Get all existing invoiceWorksheetLine tags.

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
api_instance = Infoplus.InvoiceWorksheetLineApi(Infoplus.ApiClient(configuration))
invoice_worksheet_line_id = 56 # int | Id of the invoiceWorksheetLine to get tags for

try:
    # Get the tags for an invoiceWorksheetLine.
    api_instance.get_invoice_worksheet_line_tags(invoice_worksheet_line_id)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineApi->get_invoice_worksheet_line_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_worksheet_line_id** | **int**| Id of the invoiceWorksheetLine to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_worksheet_line**
> update_invoice_worksheet_line(body)

Update an invoiceWorksheetLine

Updates an existing invoiceWorksheetLine using the specified data.

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
api_instance = Infoplus.InvoiceWorksheetLineApi(Infoplus.ApiClient(configuration))
body = Infoplus.InvoiceWorksheetLine() # InvoiceWorksheetLine | InvoiceWorksheetLine to be updated.

try:
    # Update an invoiceWorksheetLine
    api_instance.update_invoice_worksheet_line(body)
except ApiException as e:
    print("Exception when calling InvoiceWorksheetLineApi->update_invoice_worksheet_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoiceWorksheetLine**](InvoiceWorksheetLine.md)| InvoiceWorksheetLine to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

