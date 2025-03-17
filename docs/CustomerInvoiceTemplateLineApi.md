# Infoplus.CustomerInvoiceTemplateLineApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_customer_invoice_template_line_audit**](CustomerInvoiceTemplateLineApi.md#add_customer_invoice_template_line_audit) | **PUT** /beta/customerInvoiceTemplateLine/{customerInvoiceTemplateLineId}/audit/{customerInvoiceTemplateLineAudit} | Add new audit for a customerInvoiceTemplateLine
[**add_customer_invoice_template_line_file**](CustomerInvoiceTemplateLineApi.md#add_customer_invoice_template_line_file) | **POST** /beta/customerInvoiceTemplateLine/{customerInvoiceTemplateLineId}/file/{fileName} | Attach a file to a customerInvoiceTemplateLine
[**add_customer_invoice_template_line_file_by_url**](CustomerInvoiceTemplateLineApi.md#add_customer_invoice_template_line_file_by_url) | **POST** /beta/customerInvoiceTemplateLine/{customerInvoiceTemplateLineId}/file | Attach a file to a customerInvoiceTemplateLine by URL.
[**add_customer_invoice_template_line_tag**](CustomerInvoiceTemplateLineApi.md#add_customer_invoice_template_line_tag) | **PUT** /beta/customerInvoiceTemplateLine/{customerInvoiceTemplateLineId}/tag/{customerInvoiceTemplateLineTag} | Add new tags for a customerInvoiceTemplateLine.
[**delete_customer_invoice_template_line**](CustomerInvoiceTemplateLineApi.md#delete_customer_invoice_template_line) | **DELETE** /beta/customerInvoiceTemplateLine/{customerInvoiceTemplateLineId} | Delete a customerInvoiceTemplateLine
[**delete_customer_invoice_template_line_file**](CustomerInvoiceTemplateLineApi.md#delete_customer_invoice_template_line_file) | **DELETE** /beta/customerInvoiceTemplateLine/{customerInvoiceTemplateLineId}/file/{fileId} | Delete a file for a customerInvoiceTemplateLine.
[**delete_customer_invoice_template_line_tag**](CustomerInvoiceTemplateLineApi.md#delete_customer_invoice_template_line_tag) | **DELETE** /beta/customerInvoiceTemplateLine/{customerInvoiceTemplateLineId}/tag/{customerInvoiceTemplateLineTag} | Delete a tag for a customerInvoiceTemplateLine.
[**get_customer_invoice_template_line_by_filter**](CustomerInvoiceTemplateLineApi.md#get_customer_invoice_template_line_by_filter) | **GET** /beta/customerInvoiceTemplateLine/search | Search customerInvoiceTemplateLines by filter
[**get_customer_invoice_template_line_by_id**](CustomerInvoiceTemplateLineApi.md#get_customer_invoice_template_line_by_id) | **GET** /beta/customerInvoiceTemplateLine/{customerInvoiceTemplateLineId} | Get a customerInvoiceTemplateLine by id
[**get_customer_invoice_template_line_files**](CustomerInvoiceTemplateLineApi.md#get_customer_invoice_template_line_files) | **GET** /beta/customerInvoiceTemplateLine/{customerInvoiceTemplateLineId}/file | Get the files for a customerInvoiceTemplateLine.
[**get_customer_invoice_template_line_tags**](CustomerInvoiceTemplateLineApi.md#get_customer_invoice_template_line_tags) | **GET** /beta/customerInvoiceTemplateLine/{customerInvoiceTemplateLineId}/tag | Get the tags for a customerInvoiceTemplateLine.
[**get_duplicate_customer_invoice_template_line_by_id**](CustomerInvoiceTemplateLineApi.md#get_duplicate_customer_invoice_template_line_by_id) | **GET** /beta/customerInvoiceTemplateLine/duplicate/{customerInvoiceTemplateLineId} | Get a duplicated a customerInvoiceTemplateLine by id
[**update_customer_invoice_template_line**](CustomerInvoiceTemplateLineApi.md#update_customer_invoice_template_line) | **PUT** /beta/customerInvoiceTemplateLine | Update a customerInvoiceTemplateLine


# **add_customer_invoice_template_line_audit**
> add_customer_invoice_template_line_audit(customer_invoice_template_line_id, customer_invoice_template_line_audit)

Add new audit for a customerInvoiceTemplateLine

Adds an audit to an existing customerInvoiceTemplateLine.

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
api_instance = Infoplus.CustomerInvoiceTemplateLineApi(Infoplus.ApiClient(configuration))
customer_invoice_template_line_id = 56 # int | Id of the customerInvoiceTemplateLine to add an audit to
customer_invoice_template_line_audit = 'customer_invoice_template_line_audit_example' # str | The audit to add

try:
    # Add new audit for a customerInvoiceTemplateLine
    api_instance.add_customer_invoice_template_line_audit(customer_invoice_template_line_id, customer_invoice_template_line_audit)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateLineApi->add_customer_invoice_template_line_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_line_id** | **int**| Id of the customerInvoiceTemplateLine to add an audit to | 
 **customer_invoice_template_line_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_customer_invoice_template_line_file**
> add_customer_invoice_template_line_file(customer_invoice_template_line_id, file_name)

Attach a file to a customerInvoiceTemplateLine

Adds a file to an existing customerInvoiceTemplateLine.

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
api_instance = Infoplus.CustomerInvoiceTemplateLineApi(Infoplus.ApiClient(configuration))
customer_invoice_template_line_id = 56 # int | Id of the customerInvoiceTemplateLine to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a customerInvoiceTemplateLine
    api_instance.add_customer_invoice_template_line_file(customer_invoice_template_line_id, file_name)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateLineApi->add_customer_invoice_template_line_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_line_id** | **int**| Id of the customerInvoiceTemplateLine to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_customer_invoice_template_line_file_by_url**
> add_customer_invoice_template_line_file_by_url(body, customer_invoice_template_line_id)

Attach a file to a customerInvoiceTemplateLine by URL.

Adds a file to an existing customerInvoiceTemplateLine by URL.

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
api_instance = Infoplus.CustomerInvoiceTemplateLineApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
customer_invoice_template_line_id = 56 # int | Id of the customerInvoiceTemplateLine to add an file to

try:
    # Attach a file to a customerInvoiceTemplateLine by URL.
    api_instance.add_customer_invoice_template_line_file_by_url(body, customer_invoice_template_line_id)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateLineApi->add_customer_invoice_template_line_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **customer_invoice_template_line_id** | **int**| Id of the customerInvoiceTemplateLine to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_customer_invoice_template_line_tag**
> add_customer_invoice_template_line_tag(customer_invoice_template_line_id, customer_invoice_template_line_tag)

Add new tags for a customerInvoiceTemplateLine.

Adds a tag to an existing customerInvoiceTemplateLine.

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
api_instance = Infoplus.CustomerInvoiceTemplateLineApi(Infoplus.ApiClient(configuration))
customer_invoice_template_line_id = 56 # int | Id of the customerInvoiceTemplateLine to add a tag to
customer_invoice_template_line_tag = 'customer_invoice_template_line_tag_example' # str | The tag to add

try:
    # Add new tags for a customerInvoiceTemplateLine.
    api_instance.add_customer_invoice_template_line_tag(customer_invoice_template_line_id, customer_invoice_template_line_tag)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateLineApi->add_customer_invoice_template_line_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_line_id** | **int**| Id of the customerInvoiceTemplateLine to add a tag to | 
 **customer_invoice_template_line_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_invoice_template_line**
> delete_customer_invoice_template_line(customer_invoice_template_line_id)

Delete a customerInvoiceTemplateLine

Deletes the customerInvoiceTemplateLine identified by the specified id.

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
api_instance = Infoplus.CustomerInvoiceTemplateLineApi(Infoplus.ApiClient(configuration))
customer_invoice_template_line_id = 56 # int | Id of the customerInvoiceTemplateLine to be deleted.

try:
    # Delete a customerInvoiceTemplateLine
    api_instance.delete_customer_invoice_template_line(customer_invoice_template_line_id)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateLineApi->delete_customer_invoice_template_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_line_id** | **int**| Id of the customerInvoiceTemplateLine to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_invoice_template_line_file**
> delete_customer_invoice_template_line_file(customer_invoice_template_line_id, file_id)

Delete a file for a customerInvoiceTemplateLine.

Deletes an existing customerInvoiceTemplateLine file using the specified data.

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
api_instance = Infoplus.CustomerInvoiceTemplateLineApi(Infoplus.ApiClient(configuration))
customer_invoice_template_line_id = 56 # int | Id of the customerInvoiceTemplateLine to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a customerInvoiceTemplateLine.
    api_instance.delete_customer_invoice_template_line_file(customer_invoice_template_line_id, file_id)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateLineApi->delete_customer_invoice_template_line_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_line_id** | **int**| Id of the customerInvoiceTemplateLine to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_invoice_template_line_tag**
> delete_customer_invoice_template_line_tag(customer_invoice_template_line_id, customer_invoice_template_line_tag)

Delete a tag for a customerInvoiceTemplateLine.

Deletes an existing customerInvoiceTemplateLine tag using the specified data.

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
api_instance = Infoplus.CustomerInvoiceTemplateLineApi(Infoplus.ApiClient(configuration))
customer_invoice_template_line_id = 56 # int | Id of the customerInvoiceTemplateLine to remove tag from
customer_invoice_template_line_tag = 'customer_invoice_template_line_tag_example' # str | The tag to delete

try:
    # Delete a tag for a customerInvoiceTemplateLine.
    api_instance.delete_customer_invoice_template_line_tag(customer_invoice_template_line_id, customer_invoice_template_line_tag)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateLineApi->delete_customer_invoice_template_line_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_line_id** | **int**| Id of the customerInvoiceTemplateLine to remove tag from | 
 **customer_invoice_template_line_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_invoice_template_line_by_filter**
> list[CustomerInvoiceTemplateLine] get_customer_invoice_template_line_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search customerInvoiceTemplateLines by filter

Returns the list of customerInvoiceTemplateLines that match the given filter.

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
api_instance = Infoplus.CustomerInvoiceTemplateLineApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search customerInvoiceTemplateLines by filter
    api_response = api_instance.get_customer_invoice_template_line_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateLineApi->get_customer_invoice_template_line_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[CustomerInvoiceTemplateLine]**](CustomerInvoiceTemplateLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_invoice_template_line_by_id**
> CustomerInvoiceTemplateLine get_customer_invoice_template_line_by_id(customer_invoice_template_line_id)

Get a customerInvoiceTemplateLine by id

Returns the customerInvoiceTemplateLine identified by the specified id.

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
api_instance = Infoplus.CustomerInvoiceTemplateLineApi(Infoplus.ApiClient(configuration))
customer_invoice_template_line_id = 56 # int | Id of the customerInvoiceTemplateLine to be returned.

try:
    # Get a customerInvoiceTemplateLine by id
    api_response = api_instance.get_customer_invoice_template_line_by_id(customer_invoice_template_line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateLineApi->get_customer_invoice_template_line_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_line_id** | **int**| Id of the customerInvoiceTemplateLine to be returned. | 

### Return type

[**CustomerInvoiceTemplateLine**](CustomerInvoiceTemplateLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_invoice_template_line_files**
> get_customer_invoice_template_line_files(customer_invoice_template_line_id)

Get the files for a customerInvoiceTemplateLine.

Get all existing customerInvoiceTemplateLine files.

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
api_instance = Infoplus.CustomerInvoiceTemplateLineApi(Infoplus.ApiClient(configuration))
customer_invoice_template_line_id = 56 # int | Id of the customerInvoiceTemplateLine to get files for

try:
    # Get the files for a customerInvoiceTemplateLine.
    api_instance.get_customer_invoice_template_line_files(customer_invoice_template_line_id)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateLineApi->get_customer_invoice_template_line_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_line_id** | **int**| Id of the customerInvoiceTemplateLine to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_invoice_template_line_tags**
> get_customer_invoice_template_line_tags(customer_invoice_template_line_id)

Get the tags for a customerInvoiceTemplateLine.

Get all existing customerInvoiceTemplateLine tags.

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
api_instance = Infoplus.CustomerInvoiceTemplateLineApi(Infoplus.ApiClient(configuration))
customer_invoice_template_line_id = 56 # int | Id of the customerInvoiceTemplateLine to get tags for

try:
    # Get the tags for a customerInvoiceTemplateLine.
    api_instance.get_customer_invoice_template_line_tags(customer_invoice_template_line_id)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateLineApi->get_customer_invoice_template_line_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_line_id** | **int**| Id of the customerInvoiceTemplateLine to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_customer_invoice_template_line_by_id**
> CustomerInvoiceTemplateLine get_duplicate_customer_invoice_template_line_by_id(customer_invoice_template_line_id)

Get a duplicated a customerInvoiceTemplateLine by id

Returns a duplicated customerInvoiceTemplateLine identified by the specified id.

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
api_instance = Infoplus.CustomerInvoiceTemplateLineApi(Infoplus.ApiClient(configuration))
customer_invoice_template_line_id = 56 # int | Id of the customerInvoiceTemplateLine to be duplicated.

try:
    # Get a duplicated a customerInvoiceTemplateLine by id
    api_response = api_instance.get_duplicate_customer_invoice_template_line_by_id(customer_invoice_template_line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateLineApi->get_duplicate_customer_invoice_template_line_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_line_id** | **int**| Id of the customerInvoiceTemplateLine to be duplicated. | 

### Return type

[**CustomerInvoiceTemplateLine**](CustomerInvoiceTemplateLine.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_invoice_template_line**
> update_customer_invoice_template_line(body)

Update a customerInvoiceTemplateLine

Updates an existing customerInvoiceTemplateLine using the specified data.

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
api_instance = Infoplus.CustomerInvoiceTemplateLineApi(Infoplus.ApiClient(configuration))
body = Infoplus.CustomerInvoiceTemplateLine() # CustomerInvoiceTemplateLine | CustomerInvoiceTemplateLine to be updated.

try:
    # Update a customerInvoiceTemplateLine
    api_instance.update_customer_invoice_template_line(body)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateLineApi->update_customer_invoice_template_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerInvoiceTemplateLine**](CustomerInvoiceTemplateLine.md)| CustomerInvoiceTemplateLine to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

