# Infoplus.InventoryAdjustmentApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_inventory_adjustment_audit**](InventoryAdjustmentApi.md#add_inventory_adjustment_audit) | **PUT** /beta/inventoryAdjustment/{inventoryAdjustmentId}/audit/{inventoryAdjustmentAudit} | Add new audit for an inventoryAdjustment
[**add_inventory_adjustment_file**](InventoryAdjustmentApi.md#add_inventory_adjustment_file) | **POST** /beta/inventoryAdjustment/{inventoryAdjustmentId}/file/{fileName} | Attach a file to an inventoryAdjustment
[**add_inventory_adjustment_tag**](InventoryAdjustmentApi.md#add_inventory_adjustment_tag) | **PUT** /beta/inventoryAdjustment/{inventoryAdjustmentId}/tag/{inventoryAdjustmentTag} | Add new tags for an inventoryAdjustment.
[**delete_inventory_adjustment_tag**](InventoryAdjustmentApi.md#delete_inventory_adjustment_tag) | **DELETE** /beta/inventoryAdjustment/{inventoryAdjustmentId}/tag/{inventoryAdjustmentTag} | Delete a tag for an inventoryAdjustment.
[**get_duplicate_inventory_adjustment_by_id**](InventoryAdjustmentApi.md#get_duplicate_inventory_adjustment_by_id) | **GET** /beta/inventoryAdjustment/duplicate/{inventoryAdjustmentId} | Get a duplicated an inventoryAdjustment by id
[**get_inventory_adjustment_by_filter**](InventoryAdjustmentApi.md#get_inventory_adjustment_by_filter) | **GET** /beta/inventoryAdjustment/search | Search inventoryAdjustments by filter
[**get_inventory_adjustment_by_id**](InventoryAdjustmentApi.md#get_inventory_adjustment_by_id) | **GET** /beta/inventoryAdjustment/{inventoryAdjustmentId} | Get an inventoryAdjustment by id
[**get_inventory_adjustment_tags**](InventoryAdjustmentApi.md#get_inventory_adjustment_tags) | **GET** /beta/inventoryAdjustment/{inventoryAdjustmentId}/tag | Get the tags for an inventoryAdjustment.
[**update_inventory_adjustment_custom_fields**](InventoryAdjustmentApi.md#update_inventory_adjustment_custom_fields) | **PUT** /beta/inventoryAdjustment/customFields | Update an inventoryAdjustment custom fields


# **add_inventory_adjustment_audit**
> add_inventory_adjustment_audit(inventory_adjustment_id, inventory_adjustment_audit)

Add new audit for an inventoryAdjustment

Adds an audit to an existing inventoryAdjustment.

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
api_instance = Infoplus.InventoryAdjustmentApi(Infoplus.ApiClient(configuration))
inventory_adjustment_id = 56 # int | Id of the inventoryAdjustment to add an audit to
inventory_adjustment_audit = 'inventory_adjustment_audit_example' # str | The audit to add

try:
    # Add new audit for an inventoryAdjustment
    api_instance.add_inventory_adjustment_audit(inventory_adjustment_id, inventory_adjustment_audit)
except ApiException as e:
    print("Exception when calling InventoryAdjustmentApi->add_inventory_adjustment_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_adjustment_id** | **int**| Id of the inventoryAdjustment to add an audit to | 
 **inventory_adjustment_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_inventory_adjustment_file**
> add_inventory_adjustment_file(inventory_adjustment_id, file_name)

Attach a file to an inventoryAdjustment

Adds a file to an existing inventoryAdjustment.

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
api_instance = Infoplus.InventoryAdjustmentApi(Infoplus.ApiClient(configuration))
inventory_adjustment_id = 56 # int | Id of the inventoryAdjustment to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an inventoryAdjustment
    api_instance.add_inventory_adjustment_file(inventory_adjustment_id, file_name)
except ApiException as e:
    print("Exception when calling InventoryAdjustmentApi->add_inventory_adjustment_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_adjustment_id** | **int**| Id of the inventoryAdjustment to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_inventory_adjustment_tag**
> add_inventory_adjustment_tag(inventory_adjustment_id, inventory_adjustment_tag)

Add new tags for an inventoryAdjustment.

Adds a tag to an existing inventoryAdjustment.

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
api_instance = Infoplus.InventoryAdjustmentApi(Infoplus.ApiClient(configuration))
inventory_adjustment_id = 56 # int | Id of the inventoryAdjustment to add a tag to
inventory_adjustment_tag = 'inventory_adjustment_tag_example' # str | The tag to add

try:
    # Add new tags for an inventoryAdjustment.
    api_instance.add_inventory_adjustment_tag(inventory_adjustment_id, inventory_adjustment_tag)
except ApiException as e:
    print("Exception when calling InventoryAdjustmentApi->add_inventory_adjustment_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_adjustment_id** | **int**| Id of the inventoryAdjustment to add a tag to | 
 **inventory_adjustment_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inventory_adjustment_tag**
> delete_inventory_adjustment_tag(inventory_adjustment_id, inventory_adjustment_tag)

Delete a tag for an inventoryAdjustment.

Deletes an existing inventoryAdjustment tag using the specified data.

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
api_instance = Infoplus.InventoryAdjustmentApi(Infoplus.ApiClient(configuration))
inventory_adjustment_id = 56 # int | Id of the inventoryAdjustment to remove tag from
inventory_adjustment_tag = 'inventory_adjustment_tag_example' # str | The tag to delete

try:
    # Delete a tag for an inventoryAdjustment.
    api_instance.delete_inventory_adjustment_tag(inventory_adjustment_id, inventory_adjustment_tag)
except ApiException as e:
    print("Exception when calling InventoryAdjustmentApi->delete_inventory_adjustment_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_adjustment_id** | **int**| Id of the inventoryAdjustment to remove tag from | 
 **inventory_adjustment_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_inventory_adjustment_by_id**
> InventoryAdjustment get_duplicate_inventory_adjustment_by_id(inventory_adjustment_id)

Get a duplicated an inventoryAdjustment by id

Returns a duplicated inventoryAdjustment identified by the specified id.

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
api_instance = Infoplus.InventoryAdjustmentApi(Infoplus.ApiClient(configuration))
inventory_adjustment_id = 56 # int | Id of the inventoryAdjustment to be duplicated.

try:
    # Get a duplicated an inventoryAdjustment by id
    api_response = api_instance.get_duplicate_inventory_adjustment_by_id(inventory_adjustment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryAdjustmentApi->get_duplicate_inventory_adjustment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_adjustment_id** | **int**| Id of the inventoryAdjustment to be duplicated. | 

### Return type

[**InventoryAdjustment**](InventoryAdjustment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_adjustment_by_filter**
> list[InventoryAdjustment] get_inventory_adjustment_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search inventoryAdjustments by filter

Returns the list of inventoryAdjustments that match the given filter.

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
api_instance = Infoplus.InventoryAdjustmentApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search inventoryAdjustments by filter
    api_response = api_instance.get_inventory_adjustment_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryAdjustmentApi->get_inventory_adjustment_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[InventoryAdjustment]**](InventoryAdjustment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_adjustment_by_id**
> InventoryAdjustment get_inventory_adjustment_by_id(inventory_adjustment_id)

Get an inventoryAdjustment by id

Returns the inventoryAdjustment identified by the specified id.

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
api_instance = Infoplus.InventoryAdjustmentApi(Infoplus.ApiClient(configuration))
inventory_adjustment_id = 56 # int | Id of the inventoryAdjustment to be returned.

try:
    # Get an inventoryAdjustment by id
    api_response = api_instance.get_inventory_adjustment_by_id(inventory_adjustment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryAdjustmentApi->get_inventory_adjustment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_adjustment_id** | **int**| Id of the inventoryAdjustment to be returned. | 

### Return type

[**InventoryAdjustment**](InventoryAdjustment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_adjustment_tags**
> get_inventory_adjustment_tags(inventory_adjustment_id)

Get the tags for an inventoryAdjustment.

Get all existing inventoryAdjustment tags.

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
api_instance = Infoplus.InventoryAdjustmentApi(Infoplus.ApiClient(configuration))
inventory_adjustment_id = 56 # int | Id of the inventoryAdjustment to get tags for

try:
    # Get the tags for an inventoryAdjustment.
    api_instance.get_inventory_adjustment_tags(inventory_adjustment_id)
except ApiException as e:
    print("Exception when calling InventoryAdjustmentApi->get_inventory_adjustment_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_adjustment_id** | **int**| Id of the inventoryAdjustment to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inventory_adjustment_custom_fields**
> update_inventory_adjustment_custom_fields(body)

Update an inventoryAdjustment custom fields

Updates an existing inventoryAdjustment custom fields using the specified data.

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
api_instance = Infoplus.InventoryAdjustmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.InventoryAdjustment() # InventoryAdjustment | InventoryAdjustment to be updated.

try:
    # Update an inventoryAdjustment custom fields
    api_instance.update_inventory_adjustment_custom_fields(body)
except ApiException as e:
    print("Exception when calling InventoryAdjustmentApi->update_inventory_adjustment_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryAdjustment**](InventoryAdjustment.md)| InventoryAdjustment to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

