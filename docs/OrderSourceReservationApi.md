# Infoplus.OrderSourceReservationApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_order_source_reservation**](OrderSourceReservationApi.md#add_order_source_reservation) | **POST** /beta/orderSourceReservation | Create an orderSourceReservation
[**add_order_source_reservation_audit**](OrderSourceReservationApi.md#add_order_source_reservation_audit) | **PUT** /beta/orderSourceReservation/{orderSourceReservationId}/audit/{orderSourceReservationAudit} | Add new audit for an orderSourceReservation
[**add_order_source_reservation_file**](OrderSourceReservationApi.md#add_order_source_reservation_file) | **POST** /beta/orderSourceReservation/{orderSourceReservationId}/file/{fileName} | Attach a file to an orderSourceReservation
[**add_order_source_reservation_tag**](OrderSourceReservationApi.md#add_order_source_reservation_tag) | **PUT** /beta/orderSourceReservation/{orderSourceReservationId}/tag/{orderSourceReservationTag} | Add new tags for an orderSourceReservation.
[**delete_order_source_reservation**](OrderSourceReservationApi.md#delete_order_source_reservation) | **DELETE** /beta/orderSourceReservation/{orderSourceReservationId} | Delete an orderSourceReservation
[**delete_order_source_reservation_tag**](OrderSourceReservationApi.md#delete_order_source_reservation_tag) | **DELETE** /beta/orderSourceReservation/{orderSourceReservationId}/tag/{orderSourceReservationTag} | Delete a tag for an orderSourceReservation.
[**get_duplicate_order_source_reservation_by_id**](OrderSourceReservationApi.md#get_duplicate_order_source_reservation_by_id) | **GET** /beta/orderSourceReservation/duplicate/{orderSourceReservationId} | Get a duplicated an orderSourceReservation by id
[**get_order_source_reservation_by_filter**](OrderSourceReservationApi.md#get_order_source_reservation_by_filter) | **GET** /beta/orderSourceReservation/search | Search orderSourceReservations by filter
[**get_order_source_reservation_by_id**](OrderSourceReservationApi.md#get_order_source_reservation_by_id) | **GET** /beta/orderSourceReservation/{orderSourceReservationId} | Get an orderSourceReservation by id
[**get_order_source_reservation_tags**](OrderSourceReservationApi.md#get_order_source_reservation_tags) | **GET** /beta/orderSourceReservation/{orderSourceReservationId}/tag | Get the tags for an orderSourceReservation.
[**update_order_source_reservation**](OrderSourceReservationApi.md#update_order_source_reservation) | **PUT** /beta/orderSourceReservation | Update an orderSourceReservation
[**update_order_source_reservation_custom_fields**](OrderSourceReservationApi.md#update_order_source_reservation_custom_fields) | **PUT** /beta/orderSourceReservation/customFields | Update an orderSourceReservation custom fields


# **add_order_source_reservation**
> OrderSourceReservation add_order_source_reservation(body)

Create an orderSourceReservation

Inserts a new orderSourceReservation using the specified data.

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
api_instance = Infoplus.OrderSourceReservationApi(Infoplus.ApiClient(configuration))
body = Infoplus.OrderSourceReservation() # OrderSourceReservation | OrderSourceReservation to be inserted.

try:
    # Create an orderSourceReservation
    api_response = api_instance.add_order_source_reservation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderSourceReservationApi->add_order_source_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderSourceReservation**](OrderSourceReservation.md)| OrderSourceReservation to be inserted. | 

### Return type

[**OrderSourceReservation**](OrderSourceReservation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_source_reservation_audit**
> add_order_source_reservation_audit(order_source_reservation_id, order_source_reservation_audit)

Add new audit for an orderSourceReservation

Adds an audit to an existing orderSourceReservation.

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
api_instance = Infoplus.OrderSourceReservationApi(Infoplus.ApiClient(configuration))
order_source_reservation_id = 56 # int | Id of the orderSourceReservation to add an audit to
order_source_reservation_audit = 'order_source_reservation_audit_example' # str | The audit to add

try:
    # Add new audit for an orderSourceReservation
    api_instance.add_order_source_reservation_audit(order_source_reservation_id, order_source_reservation_audit)
except ApiException as e:
    print("Exception when calling OrderSourceReservationApi->add_order_source_reservation_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_reservation_id** | **int**| Id of the orderSourceReservation to add an audit to | 
 **order_source_reservation_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_source_reservation_file**
> add_order_source_reservation_file(order_source_reservation_id, file_name)

Attach a file to an orderSourceReservation

Adds a file to an existing orderSourceReservation.

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
api_instance = Infoplus.OrderSourceReservationApi(Infoplus.ApiClient(configuration))
order_source_reservation_id = 56 # int | Id of the orderSourceReservation to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an orderSourceReservation
    api_instance.add_order_source_reservation_file(order_source_reservation_id, file_name)
except ApiException as e:
    print("Exception when calling OrderSourceReservationApi->add_order_source_reservation_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_reservation_id** | **int**| Id of the orderSourceReservation to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_source_reservation_tag**
> add_order_source_reservation_tag(order_source_reservation_id, order_source_reservation_tag)

Add new tags for an orderSourceReservation.

Adds a tag to an existing orderSourceReservation.

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
api_instance = Infoplus.OrderSourceReservationApi(Infoplus.ApiClient(configuration))
order_source_reservation_id = 56 # int | Id of the orderSourceReservation to add a tag to
order_source_reservation_tag = 'order_source_reservation_tag_example' # str | The tag to add

try:
    # Add new tags for an orderSourceReservation.
    api_instance.add_order_source_reservation_tag(order_source_reservation_id, order_source_reservation_tag)
except ApiException as e:
    print("Exception when calling OrderSourceReservationApi->add_order_source_reservation_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_reservation_id** | **int**| Id of the orderSourceReservation to add a tag to | 
 **order_source_reservation_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_source_reservation**
> delete_order_source_reservation(order_source_reservation_id)

Delete an orderSourceReservation

Deletes the orderSourceReservation identified by the specified id.

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
api_instance = Infoplus.OrderSourceReservationApi(Infoplus.ApiClient(configuration))
order_source_reservation_id = 56 # int | Id of the orderSourceReservation to be deleted.

try:
    # Delete an orderSourceReservation
    api_instance.delete_order_source_reservation(order_source_reservation_id)
except ApiException as e:
    print("Exception when calling OrderSourceReservationApi->delete_order_source_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_reservation_id** | **int**| Id of the orderSourceReservation to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_source_reservation_tag**
> delete_order_source_reservation_tag(order_source_reservation_id, order_source_reservation_tag)

Delete a tag for an orderSourceReservation.

Deletes an existing orderSourceReservation tag using the specified data.

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
api_instance = Infoplus.OrderSourceReservationApi(Infoplus.ApiClient(configuration))
order_source_reservation_id = 56 # int | Id of the orderSourceReservation to remove tag from
order_source_reservation_tag = 'order_source_reservation_tag_example' # str | The tag to delete

try:
    # Delete a tag for an orderSourceReservation.
    api_instance.delete_order_source_reservation_tag(order_source_reservation_id, order_source_reservation_tag)
except ApiException as e:
    print("Exception when calling OrderSourceReservationApi->delete_order_source_reservation_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_reservation_id** | **int**| Id of the orderSourceReservation to remove tag from | 
 **order_source_reservation_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_order_source_reservation_by_id**
> OrderSourceReservation get_duplicate_order_source_reservation_by_id(order_source_reservation_id)

Get a duplicated an orderSourceReservation by id

Returns a duplicated orderSourceReservation identified by the specified id.

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
api_instance = Infoplus.OrderSourceReservationApi(Infoplus.ApiClient(configuration))
order_source_reservation_id = 56 # int | Id of the orderSourceReservation to be duplicated.

try:
    # Get a duplicated an orderSourceReservation by id
    api_response = api_instance.get_duplicate_order_source_reservation_by_id(order_source_reservation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderSourceReservationApi->get_duplicate_order_source_reservation_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_reservation_id** | **int**| Id of the orderSourceReservation to be duplicated. | 

### Return type

[**OrderSourceReservation**](OrderSourceReservation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_source_reservation_by_filter**
> list[OrderSourceReservation] get_order_source_reservation_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search orderSourceReservations by filter

Returns the list of orderSourceReservations that match the given filter.

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
api_instance = Infoplus.OrderSourceReservationApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search orderSourceReservations by filter
    api_response = api_instance.get_order_source_reservation_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderSourceReservationApi->get_order_source_reservation_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[OrderSourceReservation]**](OrderSourceReservation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_source_reservation_by_id**
> OrderSourceReservation get_order_source_reservation_by_id(order_source_reservation_id)

Get an orderSourceReservation by id

Returns the orderSourceReservation identified by the specified id.

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
api_instance = Infoplus.OrderSourceReservationApi(Infoplus.ApiClient(configuration))
order_source_reservation_id = 56 # int | Id of the orderSourceReservation to be returned.

try:
    # Get an orderSourceReservation by id
    api_response = api_instance.get_order_source_reservation_by_id(order_source_reservation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderSourceReservationApi->get_order_source_reservation_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_reservation_id** | **int**| Id of the orderSourceReservation to be returned. | 

### Return type

[**OrderSourceReservation**](OrderSourceReservation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_source_reservation_tags**
> get_order_source_reservation_tags(order_source_reservation_id)

Get the tags for an orderSourceReservation.

Get all existing orderSourceReservation tags.

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
api_instance = Infoplus.OrderSourceReservationApi(Infoplus.ApiClient(configuration))
order_source_reservation_id = 56 # int | Id of the orderSourceReservation to get tags for

try:
    # Get the tags for an orderSourceReservation.
    api_instance.get_order_source_reservation_tags(order_source_reservation_id)
except ApiException as e:
    print("Exception when calling OrderSourceReservationApi->get_order_source_reservation_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_source_reservation_id** | **int**| Id of the orderSourceReservation to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_source_reservation**
> update_order_source_reservation(body)

Update an orderSourceReservation

Updates an existing orderSourceReservation using the specified data.

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
api_instance = Infoplus.OrderSourceReservationApi(Infoplus.ApiClient(configuration))
body = Infoplus.OrderSourceReservation() # OrderSourceReservation | OrderSourceReservation to be updated.

try:
    # Update an orderSourceReservation
    api_instance.update_order_source_reservation(body)
except ApiException as e:
    print("Exception when calling OrderSourceReservationApi->update_order_source_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderSourceReservation**](OrderSourceReservation.md)| OrderSourceReservation to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_source_reservation_custom_fields**
> update_order_source_reservation_custom_fields(body)

Update an orderSourceReservation custom fields

Updates an existing orderSourceReservation custom fields using the specified data.

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
api_instance = Infoplus.OrderSourceReservationApi(Infoplus.ApiClient(configuration))
body = Infoplus.OrderSourceReservation() # OrderSourceReservation | OrderSourceReservation to be updated.

try:
    # Update an orderSourceReservation custom fields
    api_instance.update_order_source_reservation_custom_fields(body)
except ApiException as e:
    print("Exception when calling OrderSourceReservationApi->update_order_source_reservation_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderSourceReservation**](OrderSourceReservation.md)| OrderSourceReservation to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

