# Infoplus.ProductChargesApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_product_charges**](ProductChargesApi.md#add_product_charges) | **POST** /beta/productCharges | Create a productCharges
[**add_product_charges_audit**](ProductChargesApi.md#add_product_charges_audit) | **PUT** /beta/productCharges/{productChargesId}/audit/{productChargesAudit} | Add new audit for a productCharges
[**add_product_charges_file**](ProductChargesApi.md#add_product_charges_file) | **POST** /beta/productCharges/{productChargesId}/file/{fileName} | Attach a file to a productCharges
[**add_product_charges_file_by_url**](ProductChargesApi.md#add_product_charges_file_by_url) | **POST** /beta/productCharges/{productChargesId}/file | Attach a file to a productCharges by URL.
[**add_product_charges_tag**](ProductChargesApi.md#add_product_charges_tag) | **PUT** /beta/productCharges/{productChargesId}/tag/{productChargesTag} | Add new tags for a productCharges.
[**delete_product_charges**](ProductChargesApi.md#delete_product_charges) | **DELETE** /beta/productCharges/{productChargesId} | Delete a productCharges
[**delete_product_charges_file**](ProductChargesApi.md#delete_product_charges_file) | **DELETE** /beta/productCharges/{productChargesId}/file/{fileId} | Delete a file for a productCharges.
[**delete_product_charges_tag**](ProductChargesApi.md#delete_product_charges_tag) | **DELETE** /beta/productCharges/{productChargesId}/tag/{productChargesTag} | Delete a tag for a productCharges.
[**get_duplicate_product_charges_by_id**](ProductChargesApi.md#get_duplicate_product_charges_by_id) | **GET** /beta/productCharges/duplicate/{productChargesId} | Get a duplicated a productCharges by id
[**get_product_charges_by_filter**](ProductChargesApi.md#get_product_charges_by_filter) | **GET** /beta/productCharges/search | Search productChargeses by filter
[**get_product_charges_by_id**](ProductChargesApi.md#get_product_charges_by_id) | **GET** /beta/productCharges/{productChargesId} | Get a productCharges by id
[**get_product_charges_files**](ProductChargesApi.md#get_product_charges_files) | **GET** /beta/productCharges/{productChargesId}/file | Get the files for a productCharges.
[**get_product_charges_tags**](ProductChargesApi.md#get_product_charges_tags) | **GET** /beta/productCharges/{productChargesId}/tag | Get the tags for a productCharges.
[**update_product_charges**](ProductChargesApi.md#update_product_charges) | **PUT** /beta/productCharges | Update a productCharges


# **add_product_charges**
> ProductCharges add_product_charges(body)

Create a productCharges

Inserts a new productCharges using the specified data.

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
api_instance = Infoplus.ProductChargesApi(Infoplus.ApiClient(configuration))
body = Infoplus.ProductCharges() # ProductCharges | ProductCharges to be inserted.

try:
    # Create a productCharges
    api_response = api_instance.add_product_charges(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductChargesApi->add_product_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductCharges**](ProductCharges.md)| ProductCharges to be inserted. | 

### Return type

[**ProductCharges**](ProductCharges.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_product_charges_audit**
> add_product_charges_audit(product_charges_id, product_charges_audit)

Add new audit for a productCharges

Adds an audit to an existing productCharges.

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
api_instance = Infoplus.ProductChargesApi(Infoplus.ApiClient(configuration))
product_charges_id = 56 # int | Id of the productCharges to add an audit to
product_charges_audit = 'product_charges_audit_example' # str | The audit to add

try:
    # Add new audit for a productCharges
    api_instance.add_product_charges_audit(product_charges_id, product_charges_audit)
except ApiException as e:
    print("Exception when calling ProductChargesApi->add_product_charges_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_charges_id** | **int**| Id of the productCharges to add an audit to | 
 **product_charges_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_product_charges_file**
> add_product_charges_file(product_charges_id, file_name)

Attach a file to a productCharges

Adds a file to an existing productCharges.

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
api_instance = Infoplus.ProductChargesApi(Infoplus.ApiClient(configuration))
product_charges_id = 56 # int | Id of the productCharges to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a productCharges
    api_instance.add_product_charges_file(product_charges_id, file_name)
except ApiException as e:
    print("Exception when calling ProductChargesApi->add_product_charges_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_charges_id** | **int**| Id of the productCharges to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_product_charges_file_by_url**
> add_product_charges_file_by_url(body, product_charges_id)

Attach a file to a productCharges by URL.

Adds a file to an existing productCharges by URL.

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
api_instance = Infoplus.ProductChargesApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
product_charges_id = 56 # int | Id of the productCharges to add an file to

try:
    # Attach a file to a productCharges by URL.
    api_instance.add_product_charges_file_by_url(body, product_charges_id)
except ApiException as e:
    print("Exception when calling ProductChargesApi->add_product_charges_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **product_charges_id** | **int**| Id of the productCharges to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_product_charges_tag**
> add_product_charges_tag(product_charges_id, product_charges_tag)

Add new tags for a productCharges.

Adds a tag to an existing productCharges.

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
api_instance = Infoplus.ProductChargesApi(Infoplus.ApiClient(configuration))
product_charges_id = 56 # int | Id of the productCharges to add a tag to
product_charges_tag = 'product_charges_tag_example' # str | The tag to add

try:
    # Add new tags for a productCharges.
    api_instance.add_product_charges_tag(product_charges_id, product_charges_tag)
except ApiException as e:
    print("Exception when calling ProductChargesApi->add_product_charges_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_charges_id** | **int**| Id of the productCharges to add a tag to | 
 **product_charges_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product_charges**
> delete_product_charges(product_charges_id)

Delete a productCharges

Deletes the productCharges identified by the specified id.

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
api_instance = Infoplus.ProductChargesApi(Infoplus.ApiClient(configuration))
product_charges_id = 56 # int | Id of the productCharges to be deleted.

try:
    # Delete a productCharges
    api_instance.delete_product_charges(product_charges_id)
except ApiException as e:
    print("Exception when calling ProductChargesApi->delete_product_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_charges_id** | **int**| Id of the productCharges to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product_charges_file**
> delete_product_charges_file(product_charges_id, file_id)

Delete a file for a productCharges.

Deletes an existing productCharges file using the specified data.

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
api_instance = Infoplus.ProductChargesApi(Infoplus.ApiClient(configuration))
product_charges_id = 56 # int | Id of the productCharges to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a productCharges.
    api_instance.delete_product_charges_file(product_charges_id, file_id)
except ApiException as e:
    print("Exception when calling ProductChargesApi->delete_product_charges_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_charges_id** | **int**| Id of the productCharges to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product_charges_tag**
> delete_product_charges_tag(product_charges_id, product_charges_tag)

Delete a tag for a productCharges.

Deletes an existing productCharges tag using the specified data.

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
api_instance = Infoplus.ProductChargesApi(Infoplus.ApiClient(configuration))
product_charges_id = 56 # int | Id of the productCharges to remove tag from
product_charges_tag = 'product_charges_tag_example' # str | The tag to delete

try:
    # Delete a tag for a productCharges.
    api_instance.delete_product_charges_tag(product_charges_id, product_charges_tag)
except ApiException as e:
    print("Exception when calling ProductChargesApi->delete_product_charges_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_charges_id** | **int**| Id of the productCharges to remove tag from | 
 **product_charges_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_product_charges_by_id**
> ProductCharges get_duplicate_product_charges_by_id(product_charges_id)

Get a duplicated a productCharges by id

Returns a duplicated productCharges identified by the specified id.

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
api_instance = Infoplus.ProductChargesApi(Infoplus.ApiClient(configuration))
product_charges_id = 56 # int | Id of the productCharges to be duplicated.

try:
    # Get a duplicated a productCharges by id
    api_response = api_instance.get_duplicate_product_charges_by_id(product_charges_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductChargesApi->get_duplicate_product_charges_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_charges_id** | **int**| Id of the productCharges to be duplicated. | 

### Return type

[**ProductCharges**](ProductCharges.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_charges_by_filter**
> list[ProductCharges] get_product_charges_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search productChargeses by filter

Returns the list of productChargeses that match the given filter.

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
api_instance = Infoplus.ProductChargesApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search productChargeses by filter
    api_response = api_instance.get_product_charges_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductChargesApi->get_product_charges_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ProductCharges]**](ProductCharges.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_charges_by_id**
> ProductCharges get_product_charges_by_id(product_charges_id)

Get a productCharges by id

Returns the productCharges identified by the specified id.

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
api_instance = Infoplus.ProductChargesApi(Infoplus.ApiClient(configuration))
product_charges_id = 56 # int | Id of the productCharges to be returned.

try:
    # Get a productCharges by id
    api_response = api_instance.get_product_charges_by_id(product_charges_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductChargesApi->get_product_charges_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_charges_id** | **int**| Id of the productCharges to be returned. | 

### Return type

[**ProductCharges**](ProductCharges.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_charges_files**
> get_product_charges_files(product_charges_id)

Get the files for a productCharges.

Get all existing productCharges files.

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
api_instance = Infoplus.ProductChargesApi(Infoplus.ApiClient(configuration))
product_charges_id = 56 # int | Id of the productCharges to get files for

try:
    # Get the files for a productCharges.
    api_instance.get_product_charges_files(product_charges_id)
except ApiException as e:
    print("Exception when calling ProductChargesApi->get_product_charges_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_charges_id** | **int**| Id of the productCharges to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_charges_tags**
> get_product_charges_tags(product_charges_id)

Get the tags for a productCharges.

Get all existing productCharges tags.

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
api_instance = Infoplus.ProductChargesApi(Infoplus.ApiClient(configuration))
product_charges_id = 56 # int | Id of the productCharges to get tags for

try:
    # Get the tags for a productCharges.
    api_instance.get_product_charges_tags(product_charges_id)
except ApiException as e:
    print("Exception when calling ProductChargesApi->get_product_charges_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_charges_id** | **int**| Id of the productCharges to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product_charges**
> update_product_charges(body)

Update a productCharges

Updates an existing productCharges using the specified data.

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
api_instance = Infoplus.ProductChargesApi(Infoplus.ApiClient(configuration))
body = Infoplus.ProductCharges() # ProductCharges | ProductCharges to be updated.

try:
    # Update a productCharges
    api_instance.update_product_charges(body)
except ApiException as e:
    print("Exception when calling ProductChargesApi->update_product_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductCharges**](ProductCharges.md)| ProductCharges to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

