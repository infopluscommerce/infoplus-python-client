# Infoplus.OrderApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_order**](OrderApi.md#add_order) | **POST** /beta/order | Create an order
[**add_order_audit**](OrderApi.md#add_order_audit) | **PUT** /beta/order/{orderId}/audit/{orderAudit} | Add new audit for an order
[**add_order_tag**](OrderApi.md#add_order_tag) | **PUT** /beta/order/{orderId}/tag/{orderTag} | Add new tags for an order.
[**apply_order_warehouse_fulfillment_plan**](OrderApi.md#apply_order_warehouse_fulfillment_plan) | **POST** /beta/order/applyOrderWarehouseFulfillmentPlan | Run the Apply Order Warehouse Fulfillment Plan method.
[**delete_order**](OrderApi.md#delete_order) | **DELETE** /beta/order/{orderId} | Delete an order
[**delete_order_tag**](OrderApi.md#delete_order_tag) | **DELETE** /beta/order/{orderId}/tag/{orderTag} | Delete a tag for an order.
[**get_duplicate_order_by_id**](OrderApi.md#get_duplicate_order_by_id) | **GET** /beta/order/duplicate/{orderId} | Get a duplicated an order by id
[**get_order_by_filter**](OrderApi.md#get_order_by_filter) | **GET** /beta/order/search | Search orders by filter
[**get_order_by_id**](OrderApi.md#get_order_by_id) | **GET** /beta/order/{orderId} | Get an order by id
[**get_order_tags**](OrderApi.md#get_order_tags) | **GET** /beta/order/{orderId}/tag | Get the tags for an order.
[**get_order_warehouse_fulfillment_data**](OrderApi.md#get_order_warehouse_fulfillment_data) | **POST** /beta/order/getOrderWarehouseFulfillmentData | Run the Get Order Warehouse Fulfillment Plan method.
[**run_fulfillment_plan**](OrderApi.md#run_fulfillment_plan) | **POST** /beta/order/runFulfillmentPlan | Run the RunFulfillmentPlan process.
[**update_order**](OrderApi.md#update_order) | **PUT** /beta/order | Update an order
[**update_order_custom_fields**](OrderApi.md#update_order_custom_fields) | **PUT** /beta/order/customFields | Update an order custom fields


# **add_order**
> Order add_order(body)

Create an order

Inserts a new order using the specified data.

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
api_instance = Infoplus.OrderApi(Infoplus.ApiClient(configuration))
body = Infoplus.Order() # Order | Order to be inserted.

try:
    # Create an order
    api_response = api_instance.add_order(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->add_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Order**](Order.md)| Order to be inserted. | 

### Return type

[**Order**](Order.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_audit**
> add_order_audit(order_id, order_audit)

Add new audit for an order

Adds an audit to an existing order.

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
api_instance = Infoplus.OrderApi(Infoplus.ApiClient(configuration))
order_id = 8.14 # float | Id of the order to add an audit to
order_audit = 'order_audit_example' # str | The audit to add

try:
    # Add new audit for an order
    api_instance.add_order_audit(order_id, order_audit)
except ApiException as e:
    print("Exception when calling OrderApi->add_order_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **float**| Id of the order to add an audit to | 
 **order_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_tag**
> add_order_tag(order_id, order_tag)

Add new tags for an order.

Adds a tag to an existing order.

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
api_instance = Infoplus.OrderApi(Infoplus.ApiClient(configuration))
order_id = 8.14 # float | Id of the order to add a tag to
order_tag = 'order_tag_example' # str | The tag to add

try:
    # Add new tags for an order.
    api_instance.add_order_tag(order_id, order_tag)
except ApiException as e:
    print("Exception when calling OrderApi->add_order_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **float**| Id of the order to add a tag to | 
 **order_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_order_warehouse_fulfillment_plan**
> ApplyOrderWarehouseFulfillmentPlanOutput apply_order_warehouse_fulfillment_plan(body)

Run the Apply Order Warehouse Fulfillment Plan method.



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
api_instance = Infoplus.OrderApi(Infoplus.ApiClient(configuration))
body = Infoplus.ApplyOrderWarehouseFulfillmentPlanInput() # ApplyOrderWarehouseFulfillmentPlanInput | Input data for Apply Order Warehouse Fulfillment Plan process.

try:
    # Run the Apply Order Warehouse Fulfillment Plan method.
    api_response = api_instance.apply_order_warehouse_fulfillment_plan(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->apply_order_warehouse_fulfillment_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyOrderWarehouseFulfillmentPlanInput**](ApplyOrderWarehouseFulfillmentPlanInput.md)| Input data for Apply Order Warehouse Fulfillment Plan process. | 

### Return type

[**ApplyOrderWarehouseFulfillmentPlanOutput**](ApplyOrderWarehouseFulfillmentPlanOutput.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order**
> delete_order(order_id)

Delete an order

Deletes the order identified by the specified id.

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
api_instance = Infoplus.OrderApi(Infoplus.ApiClient(configuration))
order_id = 8.14 # float | Id of the order to be deleted.

try:
    # Delete an order
    api_instance.delete_order(order_id)
except ApiException as e:
    print("Exception when calling OrderApi->delete_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **float**| Id of the order to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_tag**
> delete_order_tag(order_id, order_tag)

Delete a tag for an order.

Deletes an existing order tag using the specified data.

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
api_instance = Infoplus.OrderApi(Infoplus.ApiClient(configuration))
order_id = 8.14 # float | Id of the order to remove tag from
order_tag = 'order_tag_example' # str | The tag to delete

try:
    # Delete a tag for an order.
    api_instance.delete_order_tag(order_id, order_tag)
except ApiException as e:
    print("Exception when calling OrderApi->delete_order_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **float**| Id of the order to remove tag from | 
 **order_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_order_by_id**
> Order get_duplicate_order_by_id(order_id)

Get a duplicated an order by id

Returns a duplicated order identified by the specified id.

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
api_instance = Infoplus.OrderApi(Infoplus.ApiClient(configuration))
order_id = 8.14 # float | Id of the order to be duplicated.

try:
    # Get a duplicated an order by id
    api_response = api_instance.get_duplicate_order_by_id(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->get_duplicate_order_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **float**| Id of the order to be duplicated. | 

### Return type

[**Order**](Order.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_filter**
> list[Order] get_order_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search orders by filter

Returns the list of orders that match the given filter.

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
api_instance = Infoplus.OrderApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search orders by filter
    api_response = api_instance.get_order_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->get_order_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Order]**](Order.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_id**
> Order get_order_by_id(order_id)

Get an order by id

Returns the order identified by the specified id.

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
api_instance = Infoplus.OrderApi(Infoplus.ApiClient(configuration))
order_id = 8.14 # float | Id of the order to be returned.

try:
    # Get an order by id
    api_response = api_instance.get_order_by_id(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->get_order_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **float**| Id of the order to be returned. | 

### Return type

[**Order**](Order.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_tags**
> get_order_tags(order_id)

Get the tags for an order.

Get all existing order tags.

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
api_instance = Infoplus.OrderApi(Infoplus.ApiClient(configuration))
order_id = 8.14 # float | Id of the order to get tags for

try:
    # Get the tags for an order.
    api_instance.get_order_tags(order_id)
except ApiException as e:
    print("Exception when calling OrderApi->get_order_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **float**| Id of the order to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_warehouse_fulfillment_data**
> GetOrderWarehouseFulfillmentDataOutput get_order_warehouse_fulfillment_data(body)

Run the Get Order Warehouse Fulfillment Plan method.



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
api_instance = Infoplus.OrderApi(Infoplus.ApiClient(configuration))
body = Infoplus.GetOrderWarehouseFulfillmentDataInput() # GetOrderWarehouseFulfillmentDataInput | Input data for Get Order Warehouse Fulfillment Plan process.

try:
    # Run the Get Order Warehouse Fulfillment Plan method.
    api_response = api_instance.get_order_warehouse_fulfillment_data(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->get_order_warehouse_fulfillment_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetOrderWarehouseFulfillmentDataInput**](GetOrderWarehouseFulfillmentDataInput.md)| Input data for Get Order Warehouse Fulfillment Plan process. | 

### Return type

[**GetOrderWarehouseFulfillmentDataOutput**](GetOrderWarehouseFulfillmentDataOutput.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_fulfillment_plan**
> list[ProcessOutputAPIModel] run_fulfillment_plan(body)

Run the RunFulfillmentPlan process.



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
api_instance = Infoplus.OrderApi(Infoplus.ApiClient(configuration))
body = Infoplus.RunFulfillmentPlanInputAPIModel() # RunFulfillmentPlanInputAPIModel | Input data for RunFulfillmentPlan process.

try:
    # Run the RunFulfillmentPlan process.
    api_response = api_instance.run_fulfillment_plan(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->run_fulfillment_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RunFulfillmentPlanInputAPIModel**](RunFulfillmentPlanInputAPIModel.md)| Input data for RunFulfillmentPlan process. | 

### Return type

[**list[ProcessOutputAPIModel]**](ProcessOutputAPIModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order**
> update_order(body)

Update an order

Updates an existing order using the specified data.

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
api_instance = Infoplus.OrderApi(Infoplus.ApiClient(configuration))
body = Infoplus.Order() # Order | Order to be updated.

try:
    # Update an order
    api_instance.update_order(body)
except ApiException as e:
    print("Exception when calling OrderApi->update_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Order**](Order.md)| Order to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_custom_fields**
> update_order_custom_fields(body)

Update an order custom fields

Updates an existing order custom fields using the specified data.

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
api_instance = Infoplus.OrderApi(Infoplus.ApiClient(configuration))
body = Infoplus.Order() # Order | Order to be updated.

try:
    # Update an order custom fields
    api_instance.update_order_custom_fields(body)
except ApiException as e:
    print("Exception when calling OrderApi->update_order_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Order**](Order.md)| Order to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

