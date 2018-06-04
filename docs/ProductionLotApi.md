# Infoplus.ProductionLotApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_production_lot**](ProductionLotApi.md#add_production_lot) | **POST** /beta/productionLot | Create a productionLot
[**add_production_lot_audit**](ProductionLotApi.md#add_production_lot_audit) | **PUT** /beta/productionLot/{productionLotId}/audit/{productionLotAudit} | Add new audit for a productionLot
[**add_production_lot_tag**](ProductionLotApi.md#add_production_lot_tag) | **PUT** /beta/productionLot/{productionLotId}/tag/{productionLotTag} | Add new tags for a productionLot.
[**delete_production_lot**](ProductionLotApi.md#delete_production_lot) | **DELETE** /beta/productionLot/{productionLotId} | Delete a productionLot
[**delete_production_lot_tag**](ProductionLotApi.md#delete_production_lot_tag) | **DELETE** /beta/productionLot/{productionLotId}/tag/{productionLotTag} | Delete a tag for a productionLot.
[**get_duplicate_production_lot_by_id**](ProductionLotApi.md#get_duplicate_production_lot_by_id) | **GET** /beta/productionLot/duplicate/{productionLotId} | Get a duplicated a productionLot by id
[**get_production_lot_by_filter**](ProductionLotApi.md#get_production_lot_by_filter) | **GET** /beta/productionLot/search | Search productionLots by filter
[**get_production_lot_by_id**](ProductionLotApi.md#get_production_lot_by_id) | **GET** /beta/productionLot/{productionLotId} | Get a productionLot by id
[**get_production_lot_tags**](ProductionLotApi.md#get_production_lot_tags) | **GET** /beta/productionLot/{productionLotId}/tag | Get the tags for a productionLot.
[**update_production_lot**](ProductionLotApi.md#update_production_lot) | **PUT** /beta/productionLot | Update a productionLot
[**update_production_lot_custom_fields**](ProductionLotApi.md#update_production_lot_custom_fields) | **PUT** /beta/productionLot/customFields | Update a productionLot custom fields


# **add_production_lot**
> ProductionLot add_production_lot(body)

Create a productionLot

Inserts a new productionLot using the specified data.

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
api_instance = Infoplus.ProductionLotApi(Infoplus.ApiClient(configuration))
body = Infoplus.ProductionLot() # ProductionLot | ProductionLot to be inserted.

try:
    # Create a productionLot
    api_response = api_instance.add_production_lot(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductionLotApi->add_production_lot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductionLot**](ProductionLot.md)| ProductionLot to be inserted. | 

### Return type

[**ProductionLot**](ProductionLot.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_production_lot_audit**
> add_production_lot_audit(production_lot_id, production_lot_audit)

Add new audit for a productionLot

Adds an audit to an existing productionLot.

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
api_instance = Infoplus.ProductionLotApi(Infoplus.ApiClient(configuration))
production_lot_id = 56 # int | Id of the productionLot to add an audit to
production_lot_audit = 'production_lot_audit_example' # str | The audit to add

try:
    # Add new audit for a productionLot
    api_instance.add_production_lot_audit(production_lot_id, production_lot_audit)
except ApiException as e:
    print("Exception when calling ProductionLotApi->add_production_lot_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_lot_id** | **int**| Id of the productionLot to add an audit to | 
 **production_lot_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_production_lot_tag**
> add_production_lot_tag(production_lot_id, production_lot_tag)

Add new tags for a productionLot.

Adds a tag to an existing productionLot.

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
api_instance = Infoplus.ProductionLotApi(Infoplus.ApiClient(configuration))
production_lot_id = 56 # int | Id of the productionLot to add a tag to
production_lot_tag = 'production_lot_tag_example' # str | The tag to add

try:
    # Add new tags for a productionLot.
    api_instance.add_production_lot_tag(production_lot_id, production_lot_tag)
except ApiException as e:
    print("Exception when calling ProductionLotApi->add_production_lot_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_lot_id** | **int**| Id of the productionLot to add a tag to | 
 **production_lot_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_production_lot**
> delete_production_lot(production_lot_id)

Delete a productionLot

Deletes the productionLot identified by the specified id.

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
api_instance = Infoplus.ProductionLotApi(Infoplus.ApiClient(configuration))
production_lot_id = 56 # int | Id of the productionLot to be deleted.

try:
    # Delete a productionLot
    api_instance.delete_production_lot(production_lot_id)
except ApiException as e:
    print("Exception when calling ProductionLotApi->delete_production_lot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_lot_id** | **int**| Id of the productionLot to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_production_lot_tag**
> delete_production_lot_tag(production_lot_id, production_lot_tag)

Delete a tag for a productionLot.

Deletes an existing productionLot tag using the specified data.

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
api_instance = Infoplus.ProductionLotApi(Infoplus.ApiClient(configuration))
production_lot_id = 56 # int | Id of the productionLot to remove tag from
production_lot_tag = 'production_lot_tag_example' # str | The tag to delete

try:
    # Delete a tag for a productionLot.
    api_instance.delete_production_lot_tag(production_lot_id, production_lot_tag)
except ApiException as e:
    print("Exception when calling ProductionLotApi->delete_production_lot_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_lot_id** | **int**| Id of the productionLot to remove tag from | 
 **production_lot_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_production_lot_by_id**
> ProductionLot get_duplicate_production_lot_by_id(production_lot_id)

Get a duplicated a productionLot by id

Returns a duplicated productionLot identified by the specified id.

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
api_instance = Infoplus.ProductionLotApi(Infoplus.ApiClient(configuration))
production_lot_id = 56 # int | Id of the productionLot to be duplicated.

try:
    # Get a duplicated a productionLot by id
    api_response = api_instance.get_duplicate_production_lot_by_id(production_lot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductionLotApi->get_duplicate_production_lot_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_lot_id** | **int**| Id of the productionLot to be duplicated. | 

### Return type

[**ProductionLot**](ProductionLot.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_lot_by_filter**
> list[ProductionLot] get_production_lot_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search productionLots by filter

Returns the list of productionLots that match the given filter.

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
api_instance = Infoplus.ProductionLotApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search productionLots by filter
    api_response = api_instance.get_production_lot_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductionLotApi->get_production_lot_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ProductionLot]**](ProductionLot.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_lot_by_id**
> ProductionLot get_production_lot_by_id(production_lot_id)

Get a productionLot by id

Returns the productionLot identified by the specified id.

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
api_instance = Infoplus.ProductionLotApi(Infoplus.ApiClient(configuration))
production_lot_id = 56 # int | Id of the productionLot to be returned.

try:
    # Get a productionLot by id
    api_response = api_instance.get_production_lot_by_id(production_lot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductionLotApi->get_production_lot_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_lot_id** | **int**| Id of the productionLot to be returned. | 

### Return type

[**ProductionLot**](ProductionLot.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_lot_tags**
> get_production_lot_tags(production_lot_id)

Get the tags for a productionLot.

Get all existing productionLot tags.

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
api_instance = Infoplus.ProductionLotApi(Infoplus.ApiClient(configuration))
production_lot_id = 56 # int | Id of the productionLot to get tags for

try:
    # Get the tags for a productionLot.
    api_instance.get_production_lot_tags(production_lot_id)
except ApiException as e:
    print("Exception when calling ProductionLotApi->get_production_lot_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_lot_id** | **int**| Id of the productionLot to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_production_lot**
> update_production_lot(body)

Update a productionLot

Updates an existing productionLot using the specified data.

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
api_instance = Infoplus.ProductionLotApi(Infoplus.ApiClient(configuration))
body = Infoplus.ProductionLot() # ProductionLot | ProductionLot to be updated.

try:
    # Update a productionLot
    api_instance.update_production_lot(body)
except ApiException as e:
    print("Exception when calling ProductionLotApi->update_production_lot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductionLot**](ProductionLot.md)| ProductionLot to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_production_lot_custom_fields**
> update_production_lot_custom_fields(body)

Update a productionLot custom fields

Updates an existing productionLot custom fields using the specified data.

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
api_instance = Infoplus.ProductionLotApi(Infoplus.ApiClient(configuration))
body = Infoplus.ProductionLot() # ProductionLot | ProductionLot to be updated.

try:
    # Update a productionLot custom fields
    api_instance.update_production_lot_custom_fields(body)
except ApiException as e:
    print("Exception when calling ProductionLotApi->update_production_lot_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductionLot**](ProductionLot.md)| ProductionLot to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

