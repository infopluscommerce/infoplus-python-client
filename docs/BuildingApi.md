# Infoplus.BuildingApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_building**](BuildingApi.md#add_building) | **POST** /beta/building | Create a building
[**add_building_audit**](BuildingApi.md#add_building_audit) | **PUT** /beta/building/{buildingId}/audit/{buildingAudit} | Add new audit for a building
[**add_building_tag**](BuildingApi.md#add_building_tag) | **PUT** /beta/building/{buildingId}/tag/{buildingTag} | Add new tags for a building.
[**delete_building**](BuildingApi.md#delete_building) | **DELETE** /beta/building/{buildingId} | Delete a building
[**delete_building_tag**](BuildingApi.md#delete_building_tag) | **DELETE** /beta/building/{buildingId}/tag/{buildingTag} | Delete a tag for a building.
[**get_building_by_filter**](BuildingApi.md#get_building_by_filter) | **GET** /beta/building/search | Search buildings by filter
[**get_building_by_id**](BuildingApi.md#get_building_by_id) | **GET** /beta/building/{buildingId} | Get a building by id
[**get_building_tags**](BuildingApi.md#get_building_tags) | **GET** /beta/building/{buildingId}/tag | Get the tags for a building.
[**get_duplicate_building_by_id**](BuildingApi.md#get_duplicate_building_by_id) | **GET** /beta/building/duplicate/{buildingId} | Get a duplicated a building by id
[**update_building**](BuildingApi.md#update_building) | **PUT** /beta/building | Update a building
[**update_building_custom_fields**](BuildingApi.md#update_building_custom_fields) | **PUT** /beta/building/customFields | Update a building custom fields


# **add_building**
> Building add_building(body)

Create a building

Inserts a new building using the specified data.

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
api_instance = Infoplus.BuildingApi(Infoplus.ApiClient(configuration))
body = Infoplus.Building() # Building | Building to be inserted.

try:
    # Create a building
    api_response = api_instance.add_building(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildingApi->add_building: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Building**](Building.md)| Building to be inserted. | 

### Return type

[**Building**](Building.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_building_audit**
> add_building_audit(building_id, building_audit)

Add new audit for a building

Adds an audit to an existing building.

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
api_instance = Infoplus.BuildingApi(Infoplus.ApiClient(configuration))
building_id = 56 # int | Id of the building to add an audit to
building_audit = 'building_audit_example' # str | The audit to add

try:
    # Add new audit for a building
    api_instance.add_building_audit(building_id, building_audit)
except ApiException as e:
    print("Exception when calling BuildingApi->add_building_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_id** | **int**| Id of the building to add an audit to | 
 **building_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_building_tag**
> add_building_tag(building_id, building_tag)

Add new tags for a building.

Adds a tag to an existing building.

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
api_instance = Infoplus.BuildingApi(Infoplus.ApiClient(configuration))
building_id = 56 # int | Id of the building to add a tag to
building_tag = 'building_tag_example' # str | The tag to add

try:
    # Add new tags for a building.
    api_instance.add_building_tag(building_id, building_tag)
except ApiException as e:
    print("Exception when calling BuildingApi->add_building_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_id** | **int**| Id of the building to add a tag to | 
 **building_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_building**
> delete_building(building_id)

Delete a building

Deletes the building identified by the specified id.

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
api_instance = Infoplus.BuildingApi(Infoplus.ApiClient(configuration))
building_id = 56 # int | Id of the building to be deleted.

try:
    # Delete a building
    api_instance.delete_building(building_id)
except ApiException as e:
    print("Exception when calling BuildingApi->delete_building: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_id** | **int**| Id of the building to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_building_tag**
> delete_building_tag(building_id, building_tag)

Delete a tag for a building.

Deletes an existing building tag using the specified data.

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
api_instance = Infoplus.BuildingApi(Infoplus.ApiClient(configuration))
building_id = 56 # int | Id of the building to remove tag from
building_tag = 'building_tag_example' # str | The tag to delete

try:
    # Delete a tag for a building.
    api_instance.delete_building_tag(building_id, building_tag)
except ApiException as e:
    print("Exception when calling BuildingApi->delete_building_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_id** | **int**| Id of the building to remove tag from | 
 **building_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_building_by_filter**
> list[Building] get_building_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search buildings by filter

Returns the list of buildings that match the given filter.

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
api_instance = Infoplus.BuildingApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search buildings by filter
    api_response = api_instance.get_building_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildingApi->get_building_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Building]**](Building.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_building_by_id**
> Building get_building_by_id(building_id)

Get a building by id

Returns the building identified by the specified id.

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
api_instance = Infoplus.BuildingApi(Infoplus.ApiClient(configuration))
building_id = 56 # int | Id of the building to be returned.

try:
    # Get a building by id
    api_response = api_instance.get_building_by_id(building_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildingApi->get_building_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_id** | **int**| Id of the building to be returned. | 

### Return type

[**Building**](Building.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_building_tags**
> get_building_tags(building_id)

Get the tags for a building.

Get all existing building tags.

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
api_instance = Infoplus.BuildingApi(Infoplus.ApiClient(configuration))
building_id = 56 # int | Id of the building to get tags for

try:
    # Get the tags for a building.
    api_instance.get_building_tags(building_id)
except ApiException as e:
    print("Exception when calling BuildingApi->get_building_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_id** | **int**| Id of the building to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_building_by_id**
> Building get_duplicate_building_by_id(building_id)

Get a duplicated a building by id

Returns a duplicated building identified by the specified id.

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
api_instance = Infoplus.BuildingApi(Infoplus.ApiClient(configuration))
building_id = 56 # int | Id of the building to be duplicated.

try:
    # Get a duplicated a building by id
    api_response = api_instance.get_duplicate_building_by_id(building_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildingApi->get_duplicate_building_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_id** | **int**| Id of the building to be duplicated. | 

### Return type

[**Building**](Building.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_building**
> update_building(body)

Update a building

Updates an existing building using the specified data.

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
api_instance = Infoplus.BuildingApi(Infoplus.ApiClient(configuration))
body = Infoplus.Building() # Building | Building to be updated.

try:
    # Update a building
    api_instance.update_building(body)
except ApiException as e:
    print("Exception when calling BuildingApi->update_building: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Building**](Building.md)| Building to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_building_custom_fields**
> update_building_custom_fields(body)

Update a building custom fields

Updates an existing building custom fields using the specified data.

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
api_instance = Infoplus.BuildingApi(Infoplus.ApiClient(configuration))
body = Infoplus.Building() # Building | Building to be updated.

try:
    # Update a building custom fields
    api_instance.update_building_custom_fields(body)
except ApiException as e:
    print("Exception when calling BuildingApi->update_building_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Building**](Building.md)| Building to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

