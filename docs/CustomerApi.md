# Infoplus.CustomerApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_customer**](CustomerApi.md#add_customer) | **POST** /beta/customer | Create a customer
[**add_customer_audit**](CustomerApi.md#add_customer_audit) | **PUT** /beta/customer/{customerId}/audit/{customerAudit} | Add new audit for a customer
[**add_customer_file**](CustomerApi.md#add_customer_file) | **POST** /beta/customer/{customerId}/file/{fileName} | Attach a file to a customer
[**add_customer_file_by_url**](CustomerApi.md#add_customer_file_by_url) | **POST** /beta/customer/{customerId}/file | Attach a file to a customer by URL.
[**add_customer_tag**](CustomerApi.md#add_customer_tag) | **PUT** /beta/customer/{customerId}/tag/{customerTag} | Add new tags for a customer.
[**delete_customer**](CustomerApi.md#delete_customer) | **DELETE** /beta/customer/{customerId} | Delete a customer
[**delete_customer_file**](CustomerApi.md#delete_customer_file) | **DELETE** /beta/customer/{customerId}/file/{fileId} | Delete a file for a customer.
[**delete_customer_tag**](CustomerApi.md#delete_customer_tag) | **DELETE** /beta/customer/{customerId}/tag/{customerTag} | Delete a tag for a customer.
[**get_by_customer_no**](CustomerApi.md#get_by_customer_no) | **GET** /beta/customer/getByCustomerNo | Get a customer by Customer No
[**get_customer_by_filter**](CustomerApi.md#get_customer_by_filter) | **GET** /beta/customer/search | Search customers by filter
[**get_customer_by_id**](CustomerApi.md#get_customer_by_id) | **GET** /beta/customer/{customerId} | Get a customer by id
[**get_customer_files**](CustomerApi.md#get_customer_files) | **GET** /beta/customer/{customerId}/file | Get the files for a customer.
[**get_customer_tags**](CustomerApi.md#get_customer_tags) | **GET** /beta/customer/{customerId}/tag | Get the tags for a customer.
[**get_duplicate_customer_by_id**](CustomerApi.md#get_duplicate_customer_by_id) | **GET** /beta/customer/duplicate/{customerId} | Get a duplicated a customer by id
[**update_customer**](CustomerApi.md#update_customer) | **PUT** /beta/customer | Update a customer
[**update_customer_custom_fields**](CustomerApi.md#update_customer_custom_fields) | **PUT** /beta/customer/customFields | Update a customer custom fields


# **add_customer**
> Customer add_customer(body)

Create a customer

Inserts a new customer using the specified data.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
body = Infoplus.Customer() # Customer | Customer to be inserted.

try:
    # Create a customer
    api_response = api_instance.add_customer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->add_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Customer**](Customer.md)| Customer to be inserted. | 

### Return type

[**Customer**](Customer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_customer_audit**
> add_customer_audit(customer_id, customer_audit)

Add new audit for a customer

Adds an audit to an existing customer.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
customer_id = 56 # int | Id of the customer to add an audit to
customer_audit = 'customer_audit_example' # str | The audit to add

try:
    # Add new audit for a customer
    api_instance.add_customer_audit(customer_id, customer_audit)
except ApiException as e:
    print("Exception when calling CustomerApi->add_customer_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Id of the customer to add an audit to | 
 **customer_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_customer_file**
> add_customer_file(customer_id, file_name)

Attach a file to a customer

Adds a file to an existing customer.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
customer_id = 56 # int | Id of the customer to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a customer
    api_instance.add_customer_file(customer_id, file_name)
except ApiException as e:
    print("Exception when calling CustomerApi->add_customer_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Id of the customer to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_customer_file_by_url**
> add_customer_file_by_url(body, customer_id)

Attach a file to a customer by URL.

Adds a file to an existing customer by URL.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
customer_id = 56 # int | Id of the customer to add an file to

try:
    # Attach a file to a customer by URL.
    api_instance.add_customer_file_by_url(body, customer_id)
except ApiException as e:
    print("Exception when calling CustomerApi->add_customer_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **customer_id** | **int**| Id of the customer to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_customer_tag**
> add_customer_tag(customer_id, customer_tag)

Add new tags for a customer.

Adds a tag to an existing customer.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
customer_id = 56 # int | Id of the customer to add a tag to
customer_tag = 'customer_tag_example' # str | The tag to add

try:
    # Add new tags for a customer.
    api_instance.add_customer_tag(customer_id, customer_tag)
except ApiException as e:
    print("Exception when calling CustomerApi->add_customer_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Id of the customer to add a tag to | 
 **customer_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer**
> delete_customer(customer_id)

Delete a customer

Deletes the customer identified by the specified id.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
customer_id = 56 # int | Id of the customer to be deleted.

try:
    # Delete a customer
    api_instance.delete_customer(customer_id)
except ApiException as e:
    print("Exception when calling CustomerApi->delete_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Id of the customer to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_file**
> delete_customer_file(customer_id, file_id)

Delete a file for a customer.

Deletes an existing customer file using the specified data.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
customer_id = 56 # int | Id of the customer to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a customer.
    api_instance.delete_customer_file(customer_id, file_id)
except ApiException as e:
    print("Exception when calling CustomerApi->delete_customer_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Id of the customer to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_tag**
> delete_customer_tag(customer_id, customer_tag)

Delete a tag for a customer.

Deletes an existing customer tag using the specified data.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
customer_id = 56 # int | Id of the customer to remove tag from
customer_tag = 'customer_tag_example' # str | The tag to delete

try:
    # Delete a tag for a customer.
    api_instance.delete_customer_tag(customer_id, customer_tag)
except ApiException as e:
    print("Exception when calling CustomerApi->delete_customer_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Id of the customer to remove tag from | 
 **customer_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_customer_no**
> Customer get_by_customer_no(lob_id, customer_no)

Get a customer by Customer No

Returns the customer identified by the specified parameters.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
lob_id = 56 # int | lobId of the customer to be returned.
customer_no = 'customer_no_example' # str | customerNo of the customer to be returned.

try:
    # Get a customer by Customer No
    api_response = api_instance.get_by_customer_no(lob_id, customer_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->get_by_customer_no: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lob_id** | **int**| lobId of the customer to be returned. | 
 **customer_no** | **str**| customerNo of the customer to be returned. | 

### Return type

[**Customer**](Customer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_by_filter**
> list[Customer] get_customer_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search customers by filter

Returns the list of customers that match the given filter.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search customers by filter
    api_response = api_instance.get_customer_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->get_customer_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Customer]**](Customer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_by_id**
> Customer get_customer_by_id(customer_id)

Get a customer by id

Returns the customer identified by the specified id.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
customer_id = 56 # int | Id of the customer to be returned.

try:
    # Get a customer by id
    api_response = api_instance.get_customer_by_id(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->get_customer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Id of the customer to be returned. | 

### Return type

[**Customer**](Customer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_files**
> get_customer_files(customer_id)

Get the files for a customer.

Get all existing customer files.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
customer_id = 56 # int | Id of the customer to get files for

try:
    # Get the files for a customer.
    api_instance.get_customer_files(customer_id)
except ApiException as e:
    print("Exception when calling CustomerApi->get_customer_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Id of the customer to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_tags**
> get_customer_tags(customer_id)

Get the tags for a customer.

Get all existing customer tags.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
customer_id = 56 # int | Id of the customer to get tags for

try:
    # Get the tags for a customer.
    api_instance.get_customer_tags(customer_id)
except ApiException as e:
    print("Exception when calling CustomerApi->get_customer_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Id of the customer to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_customer_by_id**
> Customer get_duplicate_customer_by_id(customer_id)

Get a duplicated a customer by id

Returns a duplicated customer identified by the specified id.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
customer_id = 56 # int | Id of the customer to be duplicated.

try:
    # Get a duplicated a customer by id
    api_response = api_instance.get_duplicate_customer_by_id(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->get_duplicate_customer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Id of the customer to be duplicated. | 

### Return type

[**Customer**](Customer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer**
> update_customer(body)

Update a customer

Updates an existing customer using the specified data.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
body = Infoplus.Customer() # Customer | Customer to be updated.

try:
    # Update a customer
    api_instance.update_customer(body)
except ApiException as e:
    print("Exception when calling CustomerApi->update_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Customer**](Customer.md)| Customer to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_custom_fields**
> update_customer_custom_fields(body)

Update a customer custom fields

Updates an existing customer custom fields using the specified data.

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
api_instance = Infoplus.CustomerApi(Infoplus.ApiClient(configuration))
body = Infoplus.Customer() # Customer | Customer to be updated.

try:
    # Update a customer custom fields
    api_instance.update_customer_custom_fields(body)
except ApiException as e:
    print("Exception when calling CustomerApi->update_customer_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Customer**](Customer.md)| Customer to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

