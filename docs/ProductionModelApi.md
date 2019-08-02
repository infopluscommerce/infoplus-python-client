# Infoplus.ProductionModelApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_production_model**](ProductionModelApi.md#add_production_model) | **POST** /beta/productionModel | Create a productionModel
[**add_production_model_audit**](ProductionModelApi.md#add_production_model_audit) | **PUT** /beta/productionModel/{productionModelId}/audit/{productionModelAudit} | Add new audit for a productionModel
[**add_production_model_file**](ProductionModelApi.md#add_production_model_file) | **POST** /beta/productionModel/{productionModelId}/file/{fileName} | Attach a file to a productionModel
[**add_production_model_tag**](ProductionModelApi.md#add_production_model_tag) | **PUT** /beta/productionModel/{productionModelId}/tag/{productionModelTag} | Add new tags for a productionModel.
[**delete_production_model**](ProductionModelApi.md#delete_production_model) | **DELETE** /beta/productionModel/{productionModelId} | Delete a productionModel
[**delete_production_model_tag**](ProductionModelApi.md#delete_production_model_tag) | **DELETE** /beta/productionModel/{productionModelId}/tag/{productionModelTag} | Delete a tag for a productionModel.
[**get_duplicate_production_model_by_id**](ProductionModelApi.md#get_duplicate_production_model_by_id) | **GET** /beta/productionModel/duplicate/{productionModelId} | Get a duplicated a productionModel by id
[**get_production_model_by_filter**](ProductionModelApi.md#get_production_model_by_filter) | **GET** /beta/productionModel/search | Search productionModels by filter
[**get_production_model_by_id**](ProductionModelApi.md#get_production_model_by_id) | **GET** /beta/productionModel/{productionModelId} | Get a productionModel by id
[**get_production_model_tags**](ProductionModelApi.md#get_production_model_tags) | **GET** /beta/productionModel/{productionModelId}/tag | Get the tags for a productionModel.
[**update_production_model**](ProductionModelApi.md#update_production_model) | **PUT** /beta/productionModel | Update a productionModel
[**update_production_model_custom_fields**](ProductionModelApi.md#update_production_model_custom_fields) | **PUT** /beta/productionModel/customFields | Update a productionModel custom fields


# **add_production_model**
> ProductionModel add_production_model(body)

Create a productionModel

Inserts a new productionModel using the specified data.

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
api_instance = Infoplus.ProductionModelApi(Infoplus.ApiClient(configuration))
body = Infoplus.ProductionModel() # ProductionModel | ProductionModel to be inserted.

try:
    # Create a productionModel
    api_response = api_instance.add_production_model(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductionModelApi->add_production_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductionModel**](ProductionModel.md)| ProductionModel to be inserted. | 

### Return type

[**ProductionModel**](ProductionModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_production_model_audit**
> add_production_model_audit(production_model_id, production_model_audit)

Add new audit for a productionModel

Adds an audit to an existing productionModel.

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
api_instance = Infoplus.ProductionModelApi(Infoplus.ApiClient(configuration))
production_model_id = 56 # int | Id of the productionModel to add an audit to
production_model_audit = 'production_model_audit_example' # str | The audit to add

try:
    # Add new audit for a productionModel
    api_instance.add_production_model_audit(production_model_id, production_model_audit)
except ApiException as e:
    print("Exception when calling ProductionModelApi->add_production_model_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_model_id** | **int**| Id of the productionModel to add an audit to | 
 **production_model_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_production_model_file**
> add_production_model_file(production_model_id, file_name)

Attach a file to a productionModel

Adds a file to an existing productionModel.

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
api_instance = Infoplus.ProductionModelApi(Infoplus.ApiClient(configuration))
production_model_id = 56 # int | Id of the productionModel to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a productionModel
    api_instance.add_production_model_file(production_model_id, file_name)
except ApiException as e:
    print("Exception when calling ProductionModelApi->add_production_model_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_model_id** | **int**| Id of the productionModel to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_production_model_tag**
> add_production_model_tag(production_model_id, production_model_tag)

Add new tags for a productionModel.

Adds a tag to an existing productionModel.

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
api_instance = Infoplus.ProductionModelApi(Infoplus.ApiClient(configuration))
production_model_id = 56 # int | Id of the productionModel to add a tag to
production_model_tag = 'production_model_tag_example' # str | The tag to add

try:
    # Add new tags for a productionModel.
    api_instance.add_production_model_tag(production_model_id, production_model_tag)
except ApiException as e:
    print("Exception when calling ProductionModelApi->add_production_model_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_model_id** | **int**| Id of the productionModel to add a tag to | 
 **production_model_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_production_model**
> delete_production_model(production_model_id)

Delete a productionModel

Deletes the productionModel identified by the specified id.

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
api_instance = Infoplus.ProductionModelApi(Infoplus.ApiClient(configuration))
production_model_id = 56 # int | Id of the productionModel to be deleted.

try:
    # Delete a productionModel
    api_instance.delete_production_model(production_model_id)
except ApiException as e:
    print("Exception when calling ProductionModelApi->delete_production_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_model_id** | **int**| Id of the productionModel to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_production_model_tag**
> delete_production_model_tag(production_model_id, production_model_tag)

Delete a tag for a productionModel.

Deletes an existing productionModel tag using the specified data.

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
api_instance = Infoplus.ProductionModelApi(Infoplus.ApiClient(configuration))
production_model_id = 56 # int | Id of the productionModel to remove tag from
production_model_tag = 'production_model_tag_example' # str | The tag to delete

try:
    # Delete a tag for a productionModel.
    api_instance.delete_production_model_tag(production_model_id, production_model_tag)
except ApiException as e:
    print("Exception when calling ProductionModelApi->delete_production_model_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_model_id** | **int**| Id of the productionModel to remove tag from | 
 **production_model_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_production_model_by_id**
> ProductionModel get_duplicate_production_model_by_id(production_model_id)

Get a duplicated a productionModel by id

Returns a duplicated productionModel identified by the specified id.

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
api_instance = Infoplus.ProductionModelApi(Infoplus.ApiClient(configuration))
production_model_id = 56 # int | Id of the productionModel to be duplicated.

try:
    # Get a duplicated a productionModel by id
    api_response = api_instance.get_duplicate_production_model_by_id(production_model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductionModelApi->get_duplicate_production_model_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_model_id** | **int**| Id of the productionModel to be duplicated. | 

### Return type

[**ProductionModel**](ProductionModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_model_by_filter**
> list[ProductionModel] get_production_model_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search productionModels by filter

Returns the list of productionModels that match the given filter.

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
api_instance = Infoplus.ProductionModelApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search productionModels by filter
    api_response = api_instance.get_production_model_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductionModelApi->get_production_model_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ProductionModel]**](ProductionModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_model_by_id**
> ProductionModel get_production_model_by_id(production_model_id)

Get a productionModel by id

Returns the productionModel identified by the specified id.

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
api_instance = Infoplus.ProductionModelApi(Infoplus.ApiClient(configuration))
production_model_id = 56 # int | Id of the productionModel to be returned.

try:
    # Get a productionModel by id
    api_response = api_instance.get_production_model_by_id(production_model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductionModelApi->get_production_model_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_model_id** | **int**| Id of the productionModel to be returned. | 

### Return type

[**ProductionModel**](ProductionModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_model_tags**
> get_production_model_tags(production_model_id)

Get the tags for a productionModel.

Get all existing productionModel tags.

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
api_instance = Infoplus.ProductionModelApi(Infoplus.ApiClient(configuration))
production_model_id = 56 # int | Id of the productionModel to get tags for

try:
    # Get the tags for a productionModel.
    api_instance.get_production_model_tags(production_model_id)
except ApiException as e:
    print("Exception when calling ProductionModelApi->get_production_model_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_model_id** | **int**| Id of the productionModel to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_production_model**
> update_production_model(body)

Update a productionModel

Updates an existing productionModel using the specified data.

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
api_instance = Infoplus.ProductionModelApi(Infoplus.ApiClient(configuration))
body = Infoplus.ProductionModel() # ProductionModel | ProductionModel to be updated.

try:
    # Update a productionModel
    api_instance.update_production_model(body)
except ApiException as e:
    print("Exception when calling ProductionModelApi->update_production_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductionModel**](ProductionModel.md)| ProductionModel to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_production_model_custom_fields**
> update_production_model_custom_fields(body)

Update a productionModel custom fields

Updates an existing productionModel custom fields using the specified data.

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
api_instance = Infoplus.ProductionModelApi(Infoplus.ApiClient(configuration))
body = Infoplus.ProductionModel() # ProductionModel | ProductionModel to be updated.

try:
    # Update a productionModel custom fields
    api_instance.update_production_model_custom_fields(body)
except ApiException as e:
    print("Exception when calling ProductionModelApi->update_production_model_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductionModel**](ProductionModel.md)| ProductionModel to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

