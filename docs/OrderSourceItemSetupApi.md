# Infoplus.OrderSourceItemSetupApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_order_source_item_setup**](OrderSourceItemSetupApi.md#add_order_source_item_setup) | **POST** /beta/orderSourceItemSetup | Create an orderSourceItemSetup
[**add_order_source_item_setup_audit**](OrderSourceItemSetupApi.md#add_order_source_item_setup_audit) | **PUT** /beta/orderSourceItemSetup/{orderSourceItemSetupId}/audit/{orderSourceItemSetupAudit} | Add new audit for an orderSourceItemSetup
[**add_order_source_item_setup_file**](OrderSourceItemSetupApi.md#add_order_source_item_setup_file) | **POST** /beta/orderSourceItemSetup/{orderSourceItemSetupId}/file/{fileName} | Attach a file to an orderSourceItemSetup
[**add_order_source_item_setup_tag**](OrderSourceItemSetupApi.md#add_order_source_item_setup_tag) | **PUT** /beta/orderSourceItemSetup/{orderSourceItemSetupId}/tag/{orderSourceItemSetupTag} | Add new tags for an orderSourceItemSetup.
[**delete_order_source_item_setup**](OrderSourceItemSetupApi.md#delete_order_source_item_setup) | **DELETE** /beta/orderSourceItemSetup/{orderSourceItemSetupId} | Delete an orderSourceItemSetup
[**delete_order_source_item_setup_tag**](OrderSourceItemSetupApi.md#delete_order_source_item_setup_tag) | **DELETE** /beta/orderSourceItemSetup/{orderSourceItemSetupId}/tag/{orderSourceItemSetupTag} | Delete a tag for an orderSourceItemSetup.
[**get_duplicate_order_source_item_setup_by_id**](OrderSourceItemSetupApi.md#get_duplicate_order_source_item_setup_by_id) | **GET** /beta/orderSourceItemSetup/duplicate/{orderSourceItemSetupId} | Get a duplicated an orderSourceItemSetup by id
[**get_order_source_item_setup_by_filter**](OrderSourceItemSetupApi.md#get_order_source_item_setup_by_filter) | **GET** /beta/orderSourceItemSetup/search | Search orderSourceItemSetups by filter
[**get_order_source_item_setup_by_id**](OrderSourceItemSetupApi.md#get_order_source_item_setup_by_id) | **GET** /beta/orderSourceItemSetup/{orderSourceItemSetupId} | Get an orderSourceItemSetup by id
[**get_order_source_item_setup_tags**](OrderSourceItemSetupApi.md#get_order_source_item_setup_tags) | **GET** /beta/orderSourceItemSetup/{orderSourceItemSetupId}/tag | Get the tags for an orderSourceItemSetup.
[**update_order_source_item_setup**](OrderSourceItemSetupApi.md#update_order_source_item_setup) | **PUT** /beta/orderSourceItemSetup | Update an orderSourceItemSetup
[**update_order_source_item_setup_custom_fields**](OrderSourceItemSetupApi.md#update_order_source_item_setup_custom_fields) | **PUT** /beta/orderSourceItemSetup/customFields | Update an orderSourceItemSetup custom fields


# **add_order_source_item_setup**
> OrderSourceItemSetup add_order_source_item_setup(body)

Create an orderSourceItemSetup

Inserts a new orderSourceItemSetup using the specified data.

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
api_instance = Infoplus.OrderSourceItemSetupApi(Infoplus.ApiClient(configuration))
body = Infoplus.OrderSourceItemSetup() # OrderSourceItemSetup | OrderSourceItemSetup to be inserted.

try:
    # Create an orderSourceItemSetup
    api_response = api_instance.add_order_source_item_setup(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderSourceItemSetupApi->add_order_source_item_setup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderSourceItemSetup**](OrderSourceItemSetup.md)| OrderSourceItemSetup to be inserted. | 

### Return type

[**OrderSourceItemSetup**](OrderSourceItemSetup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_source_item_setup_audit**
> add_order_source_item_setup_audit(order_source_item_setup_id, order_source_item_setup_audit)

Add new audit for an orderSourceItemSetup

Adds an audit to an existing orderSourceItemSetup.

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
api_instance = Infoplus.OrderSourceItemSetupApi(Infoplus.ApiClient(configuration))
order_source_item_setup_id = 56 # int | Id of the orderSourceItemSetup to add an audit to
order_source_item_setup_audit = 'order_source_item_setup_audit_example' # str | The audit to add

try:
    # Add new audit for an orderSourceItemSetup
    api_instance.add_order_source_item_setup_audit(order_source_item_setup_id, order_source_item_setup_audit)
except ApiException as e:
    print("Exception when calling OrderSourceItemSetupApi->add_order_source_item_setup_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_item_setup_id** | **int**| Id of the orderSourceItemSetup to add an audit to | 
 **order_source_item_setup_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_source_item_setup_file**
> add_order_source_item_setup_file(order_source_item_setup_id, file_name)

Attach a file to an orderSourceItemSetup

Adds a file to an existing orderSourceItemSetup.

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
api_instance = Infoplus.OrderSourceItemSetupApi(Infoplus.ApiClient(configuration))
order_source_item_setup_id = 56 # int | Id of the orderSourceItemSetup to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an orderSourceItemSetup
    api_instance.add_order_source_item_setup_file(order_source_item_setup_id, file_name)
except ApiException as e:
    print("Exception when calling OrderSourceItemSetupApi->add_order_source_item_setup_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_item_setup_id** | **int**| Id of the orderSourceItemSetup to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_source_item_setup_tag**
> add_order_source_item_setup_tag(order_source_item_setup_id, order_source_item_setup_tag)

Add new tags for an orderSourceItemSetup.

Adds a tag to an existing orderSourceItemSetup.

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
api_instance = Infoplus.OrderSourceItemSetupApi(Infoplus.ApiClient(configuration))
order_source_item_setup_id = 56 # int | Id of the orderSourceItemSetup to add a tag to
order_source_item_setup_tag = 'order_source_item_setup_tag_example' # str | The tag to add

try:
    # Add new tags for an orderSourceItemSetup.
    api_instance.add_order_source_item_setup_tag(order_source_item_setup_id, order_source_item_setup_tag)
except ApiException as e:
    print("Exception when calling OrderSourceItemSetupApi->add_order_source_item_setup_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_item_setup_id** | **int**| Id of the orderSourceItemSetup to add a tag to | 
 **order_source_item_setup_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_source_item_setup**
> delete_order_source_item_setup(order_source_item_setup_id)

Delete an orderSourceItemSetup

Deletes the orderSourceItemSetup identified by the specified id.

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
api_instance = Infoplus.OrderSourceItemSetupApi(Infoplus.ApiClient(configuration))
order_source_item_setup_id = 56 # int | Id of the orderSourceItemSetup to be deleted.

try:
    # Delete an orderSourceItemSetup
    api_instance.delete_order_source_item_setup(order_source_item_setup_id)
except ApiException as e:
    print("Exception when calling OrderSourceItemSetupApi->delete_order_source_item_setup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_item_setup_id** | **int**| Id of the orderSourceItemSetup to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_source_item_setup_tag**
> delete_order_source_item_setup_tag(order_source_item_setup_id, order_source_item_setup_tag)

Delete a tag for an orderSourceItemSetup.

Deletes an existing orderSourceItemSetup tag using the specified data.

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
api_instance = Infoplus.OrderSourceItemSetupApi(Infoplus.ApiClient(configuration))
order_source_item_setup_id = 56 # int | Id of the orderSourceItemSetup to remove tag from
order_source_item_setup_tag = 'order_source_item_setup_tag_example' # str | The tag to delete

try:
    # Delete a tag for an orderSourceItemSetup.
    api_instance.delete_order_source_item_setup_tag(order_source_item_setup_id, order_source_item_setup_tag)
except ApiException as e:
    print("Exception when calling OrderSourceItemSetupApi->delete_order_source_item_setup_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_item_setup_id** | **int**| Id of the orderSourceItemSetup to remove tag from | 
 **order_source_item_setup_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_order_source_item_setup_by_id**
> OrderSourceItemSetup get_duplicate_order_source_item_setup_by_id(order_source_item_setup_id)

Get a duplicated an orderSourceItemSetup by id

Returns a duplicated orderSourceItemSetup identified by the specified id.

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
api_instance = Infoplus.OrderSourceItemSetupApi(Infoplus.ApiClient(configuration))
order_source_item_setup_id = 56 # int | Id of the orderSourceItemSetup to be duplicated.

try:
    # Get a duplicated an orderSourceItemSetup by id
    api_response = api_instance.get_duplicate_order_source_item_setup_by_id(order_source_item_setup_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderSourceItemSetupApi->get_duplicate_order_source_item_setup_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_item_setup_id** | **int**| Id of the orderSourceItemSetup to be duplicated. | 

### Return type

[**OrderSourceItemSetup**](OrderSourceItemSetup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_source_item_setup_by_filter**
> list[OrderSourceItemSetup] get_order_source_item_setup_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search orderSourceItemSetups by filter

Returns the list of orderSourceItemSetups that match the given filter.

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
api_instance = Infoplus.OrderSourceItemSetupApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search orderSourceItemSetups by filter
    api_response = api_instance.get_order_source_item_setup_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderSourceItemSetupApi->get_order_source_item_setup_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[OrderSourceItemSetup]**](OrderSourceItemSetup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_source_item_setup_by_id**
> OrderSourceItemSetup get_order_source_item_setup_by_id(order_source_item_setup_id)

Get an orderSourceItemSetup by id

Returns the orderSourceItemSetup identified by the specified id.

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
api_instance = Infoplus.OrderSourceItemSetupApi(Infoplus.ApiClient(configuration))
order_source_item_setup_id = 56 # int | Id of the orderSourceItemSetup to be returned.

try:
    # Get an orderSourceItemSetup by id
    api_response = api_instance.get_order_source_item_setup_by_id(order_source_item_setup_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderSourceItemSetupApi->get_order_source_item_setup_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_item_setup_id** | **int**| Id of the orderSourceItemSetup to be returned. | 

### Return type

[**OrderSourceItemSetup**](OrderSourceItemSetup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_source_item_setup_tags**
> get_order_source_item_setup_tags(order_source_item_setup_id)

Get the tags for an orderSourceItemSetup.

Get all existing orderSourceItemSetup tags.

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
api_instance = Infoplus.OrderSourceItemSetupApi(Infoplus.ApiClient(configuration))
order_source_item_setup_id = 56 # int | Id of the orderSourceItemSetup to get tags for

try:
    # Get the tags for an orderSourceItemSetup.
    api_instance.get_order_source_item_setup_tags(order_source_item_setup_id)
except ApiException as e:
    print("Exception when calling OrderSourceItemSetupApi->get_order_source_item_setup_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_item_setup_id** | **int**| Id of the orderSourceItemSetup to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_source_item_setup**
> update_order_source_item_setup(body)

Update an orderSourceItemSetup

Updates an existing orderSourceItemSetup using the specified data.

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
api_instance = Infoplus.OrderSourceItemSetupApi(Infoplus.ApiClient(configuration))
body = Infoplus.OrderSourceItemSetup() # OrderSourceItemSetup | OrderSourceItemSetup to be updated.

try:
    # Update an orderSourceItemSetup
    api_instance.update_order_source_item_setup(body)
except ApiException as e:
    print("Exception when calling OrderSourceItemSetupApi->update_order_source_item_setup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderSourceItemSetup**](OrderSourceItemSetup.md)| OrderSourceItemSetup to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_source_item_setup_custom_fields**
> update_order_source_item_setup_custom_fields(body)

Update an orderSourceItemSetup custom fields

Updates an existing orderSourceItemSetup custom fields using the specified data.

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
api_instance = Infoplus.OrderSourceItemSetupApi(Infoplus.ApiClient(configuration))
body = Infoplus.OrderSourceItemSetup() # OrderSourceItemSetup | OrderSourceItemSetup to be updated.

try:
    # Update an orderSourceItemSetup custom fields
    api_instance.update_order_source_item_setup_custom_fields(body)
except ApiException as e:
    print("Exception when calling OrderSourceItemSetupApi->update_order_source_item_setup_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderSourceItemSetup**](OrderSourceItemSetup.md)| OrderSourceItemSetup to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

