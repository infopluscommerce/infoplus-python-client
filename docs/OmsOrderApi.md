# Infoplus.OmsOrderApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_oms_order**](OmsOrderApi.md#add_oms_order) | **POST** /beta/omsOrder | Create an omsOrder
[**add_oms_order_audit**](OmsOrderApi.md#add_oms_order_audit) | **PUT** /beta/omsOrder/{omsOrderId}/audit/{omsOrderAudit} | Add new audit for an omsOrder
[**add_oms_order_file**](OmsOrderApi.md#add_oms_order_file) | **POST** /beta/omsOrder/{omsOrderId}/file/{fileName} | Attach a file to an omsOrder
[**add_oms_order_file_by_url**](OmsOrderApi.md#add_oms_order_file_by_url) | **POST** /beta/omsOrder/{omsOrderId}/file | Attach a file to an omsOrder by URL.
[**add_oms_order_tag**](OmsOrderApi.md#add_oms_order_tag) | **PUT** /beta/omsOrder/{omsOrderId}/tag/{omsOrderTag} | Add new tags for an omsOrder.
[**delete_oms_order_file**](OmsOrderApi.md#delete_oms_order_file) | **DELETE** /beta/omsOrder/{omsOrderId}/file/{fileId} | Delete a file for an omsOrder.
[**delete_oms_order_tag**](OmsOrderApi.md#delete_oms_order_tag) | **DELETE** /beta/omsOrder/{omsOrderId}/tag/{omsOrderTag} | Delete a tag for an omsOrder.
[**get_duplicate_oms_order_by_id**](OmsOrderApi.md#get_duplicate_oms_order_by_id) | **GET** /beta/omsOrder/duplicate/{omsOrderId} | Get a duplicated an omsOrder by id
[**get_oms_order_by_filter**](OmsOrderApi.md#get_oms_order_by_filter) | **GET** /beta/omsOrder/search | Search omsOrders by filter
[**get_oms_order_by_id**](OmsOrderApi.md#get_oms_order_by_id) | **GET** /beta/omsOrder/{omsOrderId} | Get an omsOrder by id
[**get_oms_order_files**](OmsOrderApi.md#get_oms_order_files) | **GET** /beta/omsOrder/{omsOrderId}/file | Get the files for an omsOrder.
[**get_oms_order_tags**](OmsOrderApi.md#get_oms_order_tags) | **GET** /beta/omsOrder/{omsOrderId}/tag | Get the tags for an omsOrder.
[**update_oms_order**](OmsOrderApi.md#update_oms_order) | **PUT** /beta/omsOrder | Update an omsOrder
[**update_oms_order_custom_fields**](OmsOrderApi.md#update_oms_order_custom_fields) | **PUT** /beta/omsOrder/customFields | Update an omsOrder custom fields


# **add_oms_order**
> OmsOrder add_oms_order(body)

Create an omsOrder

Inserts a new omsOrder using the specified data.

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
api_instance = Infoplus.OmsOrderApi(Infoplus.ApiClient(configuration))
body = Infoplus.OmsOrder() # OmsOrder | OmsOrder to be inserted.

try:
    # Create an omsOrder
    api_response = api_instance.add_oms_order(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OmsOrderApi->add_oms_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OmsOrder**](OmsOrder.md)| OmsOrder to be inserted. | 

### Return type

[**OmsOrder**](OmsOrder.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_oms_order_audit**
> add_oms_order_audit(oms_order_id, oms_order_audit)

Add new audit for an omsOrder

Adds an audit to an existing omsOrder.

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
api_instance = Infoplus.OmsOrderApi(Infoplus.ApiClient(configuration))
oms_order_id = 56 # int | Id of the omsOrder to add an audit to
oms_order_audit = 'oms_order_audit_example' # str | The audit to add

try:
    # Add new audit for an omsOrder
    api_instance.add_oms_order_audit(oms_order_id, oms_order_audit)
except ApiException as e:
    print("Exception when calling OmsOrderApi->add_oms_order_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oms_order_id** | **int**| Id of the omsOrder to add an audit to | 
 **oms_order_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_oms_order_file**
> add_oms_order_file(oms_order_id, file_name)

Attach a file to an omsOrder

Adds a file to an existing omsOrder.

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
api_instance = Infoplus.OmsOrderApi(Infoplus.ApiClient(configuration))
oms_order_id = 56 # int | Id of the omsOrder to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an omsOrder
    api_instance.add_oms_order_file(oms_order_id, file_name)
except ApiException as e:
    print("Exception when calling OmsOrderApi->add_oms_order_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oms_order_id** | **int**| Id of the omsOrder to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_oms_order_file_by_url**
> add_oms_order_file_by_url(body, oms_order_id)

Attach a file to an omsOrder by URL.

Adds a file to an existing omsOrder by URL.

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
api_instance = Infoplus.OmsOrderApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
oms_order_id = 56 # int | Id of the omsOrder to add an file to

try:
    # Attach a file to an omsOrder by URL.
    api_instance.add_oms_order_file_by_url(body, oms_order_id)
except ApiException as e:
    print("Exception when calling OmsOrderApi->add_oms_order_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **oms_order_id** | **int**| Id of the omsOrder to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_oms_order_tag**
> add_oms_order_tag(oms_order_id, oms_order_tag)

Add new tags for an omsOrder.

Adds a tag to an existing omsOrder.

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
api_instance = Infoplus.OmsOrderApi(Infoplus.ApiClient(configuration))
oms_order_id = 56 # int | Id of the omsOrder to add a tag to
oms_order_tag = 'oms_order_tag_example' # str | The tag to add

try:
    # Add new tags for an omsOrder.
    api_instance.add_oms_order_tag(oms_order_id, oms_order_tag)
except ApiException as e:
    print("Exception when calling OmsOrderApi->add_oms_order_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oms_order_id** | **int**| Id of the omsOrder to add a tag to | 
 **oms_order_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oms_order_file**
> delete_oms_order_file(oms_order_id, file_id)

Delete a file for an omsOrder.

Deletes an existing omsOrder file using the specified data.

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
api_instance = Infoplus.OmsOrderApi(Infoplus.ApiClient(configuration))
oms_order_id = 56 # int | Id of the omsOrder to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an omsOrder.
    api_instance.delete_oms_order_file(oms_order_id, file_id)
except ApiException as e:
    print("Exception when calling OmsOrderApi->delete_oms_order_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oms_order_id** | **int**| Id of the omsOrder to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oms_order_tag**
> delete_oms_order_tag(oms_order_id, oms_order_tag)

Delete a tag for an omsOrder.

Deletes an existing omsOrder tag using the specified data.

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
api_instance = Infoplus.OmsOrderApi(Infoplus.ApiClient(configuration))
oms_order_id = 56 # int | Id of the omsOrder to remove tag from
oms_order_tag = 'oms_order_tag_example' # str | The tag to delete

try:
    # Delete a tag for an omsOrder.
    api_instance.delete_oms_order_tag(oms_order_id, oms_order_tag)
except ApiException as e:
    print("Exception when calling OmsOrderApi->delete_oms_order_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oms_order_id** | **int**| Id of the omsOrder to remove tag from | 
 **oms_order_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_oms_order_by_id**
> OmsOrder get_duplicate_oms_order_by_id(oms_order_id)

Get a duplicated an omsOrder by id

Returns a duplicated omsOrder identified by the specified id.

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
api_instance = Infoplus.OmsOrderApi(Infoplus.ApiClient(configuration))
oms_order_id = 56 # int | Id of the omsOrder to be duplicated.

try:
    # Get a duplicated an omsOrder by id
    api_response = api_instance.get_duplicate_oms_order_by_id(oms_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OmsOrderApi->get_duplicate_oms_order_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oms_order_id** | **int**| Id of the omsOrder to be duplicated. | 

### Return type

[**OmsOrder**](OmsOrder.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oms_order_by_filter**
> list[OmsOrder] get_oms_order_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search omsOrders by filter

Returns the list of omsOrders that match the given filter.

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
api_instance = Infoplus.OmsOrderApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search omsOrders by filter
    api_response = api_instance.get_oms_order_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OmsOrderApi->get_oms_order_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[OmsOrder]**](OmsOrder.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oms_order_by_id**
> OmsOrder get_oms_order_by_id(oms_order_id)

Get an omsOrder by id

Returns the omsOrder identified by the specified id.

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
api_instance = Infoplus.OmsOrderApi(Infoplus.ApiClient(configuration))
oms_order_id = 56 # int | Id of the omsOrder to be returned.

try:
    # Get an omsOrder by id
    api_response = api_instance.get_oms_order_by_id(oms_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OmsOrderApi->get_oms_order_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oms_order_id** | **int**| Id of the omsOrder to be returned. | 

### Return type

[**OmsOrder**](OmsOrder.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oms_order_files**
> get_oms_order_files(oms_order_id)

Get the files for an omsOrder.

Get all existing omsOrder files.

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
api_instance = Infoplus.OmsOrderApi(Infoplus.ApiClient(configuration))
oms_order_id = 56 # int | Id of the omsOrder to get files for

try:
    # Get the files for an omsOrder.
    api_instance.get_oms_order_files(oms_order_id)
except ApiException as e:
    print("Exception when calling OmsOrderApi->get_oms_order_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oms_order_id** | **int**| Id of the omsOrder to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oms_order_tags**
> get_oms_order_tags(oms_order_id)

Get the tags for an omsOrder.

Get all existing omsOrder tags.

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
api_instance = Infoplus.OmsOrderApi(Infoplus.ApiClient(configuration))
oms_order_id = 56 # int | Id of the omsOrder to get tags for

try:
    # Get the tags for an omsOrder.
    api_instance.get_oms_order_tags(oms_order_id)
except ApiException as e:
    print("Exception when calling OmsOrderApi->get_oms_order_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oms_order_id** | **int**| Id of the omsOrder to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_oms_order**
> update_oms_order(body)

Update an omsOrder

Updates an existing omsOrder using the specified data.

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
api_instance = Infoplus.OmsOrderApi(Infoplus.ApiClient(configuration))
body = Infoplus.OmsOrder() # OmsOrder | OmsOrder to be updated.

try:
    # Update an omsOrder
    api_instance.update_oms_order(body)
except ApiException as e:
    print("Exception when calling OmsOrderApi->update_oms_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OmsOrder**](OmsOrder.md)| OmsOrder to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_oms_order_custom_fields**
> update_oms_order_custom_fields(body)

Update an omsOrder custom fields

Updates an existing omsOrder custom fields using the specified data.

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
api_instance = Infoplus.OmsOrderApi(Infoplus.ApiClient(configuration))
body = Infoplus.OmsOrder() # OmsOrder | OmsOrder to be updated.

try:
    # Update an omsOrder custom fields
    api_instance.update_oms_order_custom_fields(body)
except ApiException as e:
    print("Exception when calling OmsOrderApi->update_oms_order_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OmsOrder**](OmsOrder.md)| OmsOrder to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

