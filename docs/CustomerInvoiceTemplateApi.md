# Infoplus.CustomerInvoiceTemplateApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_customer_invoice_template**](CustomerInvoiceTemplateApi.md#add_customer_invoice_template) | **POST** /beta/customerInvoiceTemplate | Create a customerInvoiceTemplate
[**add_customer_invoice_template_audit**](CustomerInvoiceTemplateApi.md#add_customer_invoice_template_audit) | **PUT** /beta/customerInvoiceTemplate/{customerInvoiceTemplateId}/audit/{customerInvoiceTemplateAudit} | Add new audit for a customerInvoiceTemplate
[**add_customer_invoice_template_file**](CustomerInvoiceTemplateApi.md#add_customer_invoice_template_file) | **POST** /beta/customerInvoiceTemplate/{customerInvoiceTemplateId}/file/{fileName} | Attach a file to a customerInvoiceTemplate
[**add_customer_invoice_template_file_by_url**](CustomerInvoiceTemplateApi.md#add_customer_invoice_template_file_by_url) | **POST** /beta/customerInvoiceTemplate/{customerInvoiceTemplateId}/file | Attach a file to a customerInvoiceTemplate by URL.
[**add_customer_invoice_template_tag**](CustomerInvoiceTemplateApi.md#add_customer_invoice_template_tag) | **PUT** /beta/customerInvoiceTemplate/{customerInvoiceTemplateId}/tag/{customerInvoiceTemplateTag} | Add new tags for a customerInvoiceTemplate.
[**delete_customer_invoice_template**](CustomerInvoiceTemplateApi.md#delete_customer_invoice_template) | **DELETE** /beta/customerInvoiceTemplate/{customerInvoiceTemplateId} | Delete a customerInvoiceTemplate
[**delete_customer_invoice_template_file**](CustomerInvoiceTemplateApi.md#delete_customer_invoice_template_file) | **DELETE** /beta/customerInvoiceTemplate/{customerInvoiceTemplateId}/file/{fileId} | Delete a file for a customerInvoiceTemplate.
[**delete_customer_invoice_template_tag**](CustomerInvoiceTemplateApi.md#delete_customer_invoice_template_tag) | **DELETE** /beta/customerInvoiceTemplate/{customerInvoiceTemplateId}/tag/{customerInvoiceTemplateTag} | Delete a tag for a customerInvoiceTemplate.
[**get_customer_invoice_template_by_filter**](CustomerInvoiceTemplateApi.md#get_customer_invoice_template_by_filter) | **GET** /beta/customerInvoiceTemplate/search | Search customerInvoiceTemplates by filter
[**get_customer_invoice_template_by_id**](CustomerInvoiceTemplateApi.md#get_customer_invoice_template_by_id) | **GET** /beta/customerInvoiceTemplate/{customerInvoiceTemplateId} | Get a customerInvoiceTemplate by id
[**get_customer_invoice_template_files**](CustomerInvoiceTemplateApi.md#get_customer_invoice_template_files) | **GET** /beta/customerInvoiceTemplate/{customerInvoiceTemplateId}/file | Get the files for a customerInvoiceTemplate.
[**get_customer_invoice_template_tags**](CustomerInvoiceTemplateApi.md#get_customer_invoice_template_tags) | **GET** /beta/customerInvoiceTemplate/{customerInvoiceTemplateId}/tag | Get the tags for a customerInvoiceTemplate.
[**get_duplicate_customer_invoice_template_by_id**](CustomerInvoiceTemplateApi.md#get_duplicate_customer_invoice_template_by_id) | **GET** /beta/customerInvoiceTemplate/duplicate/{customerInvoiceTemplateId} | Get a duplicated a customerInvoiceTemplate by id
[**update_customer_invoice_template**](CustomerInvoiceTemplateApi.md#update_customer_invoice_template) | **PUT** /beta/customerInvoiceTemplate | Update a customerInvoiceTemplate


# **add_customer_invoice_template**
> CustomerInvoiceTemplate add_customer_invoice_template(body)

Create a customerInvoiceTemplate

Inserts a new customerInvoiceTemplate using the specified data.

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
api_instance = Infoplus.CustomerInvoiceTemplateApi(Infoplus.ApiClient(configuration))
body = Infoplus.CustomerInvoiceTemplate() # CustomerInvoiceTemplate | CustomerInvoiceTemplate to be inserted.

try:
    # Create a customerInvoiceTemplate
    api_response = api_instance.add_customer_invoice_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateApi->add_customer_invoice_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerInvoiceTemplate**](CustomerInvoiceTemplate.md)| CustomerInvoiceTemplate to be inserted. | 

### Return type

[**CustomerInvoiceTemplate**](CustomerInvoiceTemplate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_customer_invoice_template_audit**
> add_customer_invoice_template_audit(customer_invoice_template_id, customer_invoice_template_audit)

Add new audit for a customerInvoiceTemplate

Adds an audit to an existing customerInvoiceTemplate.

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
api_instance = Infoplus.CustomerInvoiceTemplateApi(Infoplus.ApiClient(configuration))
customer_invoice_template_id = 56 # int | Id of the customerInvoiceTemplate to add an audit to
customer_invoice_template_audit = 'customer_invoice_template_audit_example' # str | The audit to add

try:
    # Add new audit for a customerInvoiceTemplate
    api_instance.add_customer_invoice_template_audit(customer_invoice_template_id, customer_invoice_template_audit)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateApi->add_customer_invoice_template_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_id** | **int**| Id of the customerInvoiceTemplate to add an audit to | 
 **customer_invoice_template_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_customer_invoice_template_file**
> add_customer_invoice_template_file(customer_invoice_template_id, file_name)

Attach a file to a customerInvoiceTemplate

Adds a file to an existing customerInvoiceTemplate.

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
api_instance = Infoplus.CustomerInvoiceTemplateApi(Infoplus.ApiClient(configuration))
customer_invoice_template_id = 56 # int | Id of the customerInvoiceTemplate to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a customerInvoiceTemplate
    api_instance.add_customer_invoice_template_file(customer_invoice_template_id, file_name)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateApi->add_customer_invoice_template_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_id** | **int**| Id of the customerInvoiceTemplate to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_customer_invoice_template_file_by_url**
> add_customer_invoice_template_file_by_url(body, customer_invoice_template_id)

Attach a file to a customerInvoiceTemplate by URL.

Adds a file to an existing customerInvoiceTemplate by URL.

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
api_instance = Infoplus.CustomerInvoiceTemplateApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
customer_invoice_template_id = 56 # int | Id of the customerInvoiceTemplate to add an file to

try:
    # Attach a file to a customerInvoiceTemplate by URL.
    api_instance.add_customer_invoice_template_file_by_url(body, customer_invoice_template_id)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateApi->add_customer_invoice_template_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **customer_invoice_template_id** | **int**| Id of the customerInvoiceTemplate to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_customer_invoice_template_tag**
> add_customer_invoice_template_tag(customer_invoice_template_id, customer_invoice_template_tag)

Add new tags for a customerInvoiceTemplate.

Adds a tag to an existing customerInvoiceTemplate.

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
api_instance = Infoplus.CustomerInvoiceTemplateApi(Infoplus.ApiClient(configuration))
customer_invoice_template_id = 56 # int | Id of the customerInvoiceTemplate to add a tag to
customer_invoice_template_tag = 'customer_invoice_template_tag_example' # str | The tag to add

try:
    # Add new tags for a customerInvoiceTemplate.
    api_instance.add_customer_invoice_template_tag(customer_invoice_template_id, customer_invoice_template_tag)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateApi->add_customer_invoice_template_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_id** | **int**| Id of the customerInvoiceTemplate to add a tag to | 
 **customer_invoice_template_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_invoice_template**
> delete_customer_invoice_template(customer_invoice_template_id)

Delete a customerInvoiceTemplate

Deletes the customerInvoiceTemplate identified by the specified id.

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
api_instance = Infoplus.CustomerInvoiceTemplateApi(Infoplus.ApiClient(configuration))
customer_invoice_template_id = 56 # int | Id of the customerInvoiceTemplate to be deleted.

try:
    # Delete a customerInvoiceTemplate
    api_instance.delete_customer_invoice_template(customer_invoice_template_id)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateApi->delete_customer_invoice_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_id** | **int**| Id of the customerInvoiceTemplate to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_invoice_template_file**
> delete_customer_invoice_template_file(customer_invoice_template_id, file_id)

Delete a file for a customerInvoiceTemplate.

Deletes an existing customerInvoiceTemplate file using the specified data.

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
api_instance = Infoplus.CustomerInvoiceTemplateApi(Infoplus.ApiClient(configuration))
customer_invoice_template_id = 56 # int | Id of the customerInvoiceTemplate to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a customerInvoiceTemplate.
    api_instance.delete_customer_invoice_template_file(customer_invoice_template_id, file_id)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateApi->delete_customer_invoice_template_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_id** | **int**| Id of the customerInvoiceTemplate to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_invoice_template_tag**
> delete_customer_invoice_template_tag(customer_invoice_template_id, customer_invoice_template_tag)

Delete a tag for a customerInvoiceTemplate.

Deletes an existing customerInvoiceTemplate tag using the specified data.

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
api_instance = Infoplus.CustomerInvoiceTemplateApi(Infoplus.ApiClient(configuration))
customer_invoice_template_id = 56 # int | Id of the customerInvoiceTemplate to remove tag from
customer_invoice_template_tag = 'customer_invoice_template_tag_example' # str | The tag to delete

try:
    # Delete a tag for a customerInvoiceTemplate.
    api_instance.delete_customer_invoice_template_tag(customer_invoice_template_id, customer_invoice_template_tag)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateApi->delete_customer_invoice_template_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_id** | **int**| Id of the customerInvoiceTemplate to remove tag from | 
 **customer_invoice_template_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_invoice_template_by_filter**
> list[CustomerInvoiceTemplate] get_customer_invoice_template_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search customerInvoiceTemplates by filter

Returns the list of customerInvoiceTemplates that match the given filter.

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
api_instance = Infoplus.CustomerInvoiceTemplateApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search customerInvoiceTemplates by filter
    api_response = api_instance.get_customer_invoice_template_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateApi->get_customer_invoice_template_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[CustomerInvoiceTemplate]**](CustomerInvoiceTemplate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_invoice_template_by_id**
> CustomerInvoiceTemplate get_customer_invoice_template_by_id(customer_invoice_template_id)

Get a customerInvoiceTemplate by id

Returns the customerInvoiceTemplate identified by the specified id.

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
api_instance = Infoplus.CustomerInvoiceTemplateApi(Infoplus.ApiClient(configuration))
customer_invoice_template_id = 56 # int | Id of the customerInvoiceTemplate to be returned.

try:
    # Get a customerInvoiceTemplate by id
    api_response = api_instance.get_customer_invoice_template_by_id(customer_invoice_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateApi->get_customer_invoice_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_id** | **int**| Id of the customerInvoiceTemplate to be returned. | 

### Return type

[**CustomerInvoiceTemplate**](CustomerInvoiceTemplate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_invoice_template_files**
> get_customer_invoice_template_files(customer_invoice_template_id)

Get the files for a customerInvoiceTemplate.

Get all existing customerInvoiceTemplate files.

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
api_instance = Infoplus.CustomerInvoiceTemplateApi(Infoplus.ApiClient(configuration))
customer_invoice_template_id = 56 # int | Id of the customerInvoiceTemplate to get files for

try:
    # Get the files for a customerInvoiceTemplate.
    api_instance.get_customer_invoice_template_files(customer_invoice_template_id)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateApi->get_customer_invoice_template_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_id** | **int**| Id of the customerInvoiceTemplate to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_invoice_template_tags**
> get_customer_invoice_template_tags(customer_invoice_template_id)

Get the tags for a customerInvoiceTemplate.

Get all existing customerInvoiceTemplate tags.

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
api_instance = Infoplus.CustomerInvoiceTemplateApi(Infoplus.ApiClient(configuration))
customer_invoice_template_id = 56 # int | Id of the customerInvoiceTemplate to get tags for

try:
    # Get the tags for a customerInvoiceTemplate.
    api_instance.get_customer_invoice_template_tags(customer_invoice_template_id)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateApi->get_customer_invoice_template_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_id** | **int**| Id of the customerInvoiceTemplate to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_customer_invoice_template_by_id**
> CustomerInvoiceTemplate get_duplicate_customer_invoice_template_by_id(customer_invoice_template_id)

Get a duplicated a customerInvoiceTemplate by id

Returns a duplicated customerInvoiceTemplate identified by the specified id.

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
api_instance = Infoplus.CustomerInvoiceTemplateApi(Infoplus.ApiClient(configuration))
customer_invoice_template_id = 56 # int | Id of the customerInvoiceTemplate to be duplicated.

try:
    # Get a duplicated a customerInvoiceTemplate by id
    api_response = api_instance.get_duplicate_customer_invoice_template_by_id(customer_invoice_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateApi->get_duplicate_customer_invoice_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_invoice_template_id** | **int**| Id of the customerInvoiceTemplate to be duplicated. | 

### Return type

[**CustomerInvoiceTemplate**](CustomerInvoiceTemplate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_invoice_template**
> update_customer_invoice_template(body)

Update a customerInvoiceTemplate

Updates an existing customerInvoiceTemplate using the specified data.

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
api_instance = Infoplus.CustomerInvoiceTemplateApi(Infoplus.ApiClient(configuration))
body = Infoplus.CustomerInvoiceTemplate() # CustomerInvoiceTemplate | CustomerInvoiceTemplate to be updated.

try:
    # Update a customerInvoiceTemplate
    api_instance.update_customer_invoice_template(body)
except ApiException as e:
    print("Exception when calling CustomerInvoiceTemplateApi->update_customer_invoice_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerInvoiceTemplate**](CustomerInvoiceTemplate.md)| CustomerInvoiceTemplate to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

