# Infoplus.ExternalShippingSystemApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_external_shipping_system**](ExternalShippingSystemApi.md#add_external_shipping_system) | **POST** /beta/externalShippingSystem | Create an externalShippingSystem
[**add_external_shipping_system_audit**](ExternalShippingSystemApi.md#add_external_shipping_system_audit) | **PUT** /beta/externalShippingSystem/{externalShippingSystemId}/audit/{externalShippingSystemAudit} | Add new audit for an externalShippingSystem
[**add_external_shipping_system_tag**](ExternalShippingSystemApi.md#add_external_shipping_system_tag) | **PUT** /beta/externalShippingSystem/{externalShippingSystemId}/tag/{externalShippingSystemTag} | Add new tags for an externalShippingSystem.
[**delete_external_shipping_system**](ExternalShippingSystemApi.md#delete_external_shipping_system) | **DELETE** /beta/externalShippingSystem/{externalShippingSystemId} | Delete an externalShippingSystem
[**delete_external_shipping_system_tag**](ExternalShippingSystemApi.md#delete_external_shipping_system_tag) | **DELETE** /beta/externalShippingSystem/{externalShippingSystemId}/tag/{externalShippingSystemTag} | Delete a tag for an externalShippingSystem.
[**get_duplicate_external_shipping_system_by_id**](ExternalShippingSystemApi.md#get_duplicate_external_shipping_system_by_id) | **GET** /beta/externalShippingSystem/duplicate/{externalShippingSystemId} | Get a duplicated an externalShippingSystem by id
[**get_external_shipping_system_by_filter**](ExternalShippingSystemApi.md#get_external_shipping_system_by_filter) | **GET** /beta/externalShippingSystem/search | Search externalShippingSystems by filter
[**get_external_shipping_system_by_id**](ExternalShippingSystemApi.md#get_external_shipping_system_by_id) | **GET** /beta/externalShippingSystem/{externalShippingSystemId} | Get an externalShippingSystem by id
[**get_external_shipping_system_tags**](ExternalShippingSystemApi.md#get_external_shipping_system_tags) | **GET** /beta/externalShippingSystem/{externalShippingSystemId}/tag | Get the tags for an externalShippingSystem.
[**update_external_shipping_system**](ExternalShippingSystemApi.md#update_external_shipping_system) | **PUT** /beta/externalShippingSystem | Update an externalShippingSystem
[**update_external_shipping_system_custom_fields**](ExternalShippingSystemApi.md#update_external_shipping_system_custom_fields) | **PUT** /beta/externalShippingSystem/customFields | Update an externalShippingSystem custom fields


# **add_external_shipping_system**
> ExternalShippingSystem add_external_shipping_system(body)

Create an externalShippingSystem

Inserts a new externalShippingSystem using the specified data.

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
api_instance = Infoplus.ExternalShippingSystemApi(Infoplus.ApiClient(configuration))
body = Infoplus.ExternalShippingSystem() # ExternalShippingSystem | ExternalShippingSystem to be inserted.

try:
    # Create an externalShippingSystem
    api_response = api_instance.add_external_shipping_system(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalShippingSystemApi->add_external_shipping_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalShippingSystem**](ExternalShippingSystem.md)| ExternalShippingSystem to be inserted. | 

### Return type

[**ExternalShippingSystem**](ExternalShippingSystem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_external_shipping_system_audit**
> add_external_shipping_system_audit(external_shipping_system_id, external_shipping_system_audit)

Add new audit for an externalShippingSystem

Adds an audit to an existing externalShippingSystem.

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
api_instance = Infoplus.ExternalShippingSystemApi(Infoplus.ApiClient(configuration))
external_shipping_system_id = 56 # int | Id of the externalShippingSystem to add an audit to
external_shipping_system_audit = 'external_shipping_system_audit_example' # str | The audit to add

try:
    # Add new audit for an externalShippingSystem
    api_instance.add_external_shipping_system_audit(external_shipping_system_id, external_shipping_system_audit)
except ApiException as e:
    print("Exception when calling ExternalShippingSystemApi->add_external_shipping_system_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipping_system_id** | **int**| Id of the externalShippingSystem to add an audit to | 
 **external_shipping_system_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_external_shipping_system_tag**
> add_external_shipping_system_tag(external_shipping_system_id, external_shipping_system_tag)

Add new tags for an externalShippingSystem.

Adds a tag to an existing externalShippingSystem.

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
api_instance = Infoplus.ExternalShippingSystemApi(Infoplus.ApiClient(configuration))
external_shipping_system_id = 56 # int | Id of the externalShippingSystem to add a tag to
external_shipping_system_tag = 'external_shipping_system_tag_example' # str | The tag to add

try:
    # Add new tags for an externalShippingSystem.
    api_instance.add_external_shipping_system_tag(external_shipping_system_id, external_shipping_system_tag)
except ApiException as e:
    print("Exception when calling ExternalShippingSystemApi->add_external_shipping_system_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipping_system_id** | **int**| Id of the externalShippingSystem to add a tag to | 
 **external_shipping_system_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_shipping_system**
> delete_external_shipping_system(external_shipping_system_id)

Delete an externalShippingSystem

Deletes the externalShippingSystem identified by the specified id.

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
api_instance = Infoplus.ExternalShippingSystemApi(Infoplus.ApiClient(configuration))
external_shipping_system_id = 56 # int | Id of the externalShippingSystem to be deleted.

try:
    # Delete an externalShippingSystem
    api_instance.delete_external_shipping_system(external_shipping_system_id)
except ApiException as e:
    print("Exception when calling ExternalShippingSystemApi->delete_external_shipping_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipping_system_id** | **int**| Id of the externalShippingSystem to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_shipping_system_tag**
> delete_external_shipping_system_tag(external_shipping_system_id, external_shipping_system_tag)

Delete a tag for an externalShippingSystem.

Deletes an existing externalShippingSystem tag using the specified data.

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
api_instance = Infoplus.ExternalShippingSystemApi(Infoplus.ApiClient(configuration))
external_shipping_system_id = 56 # int | Id of the externalShippingSystem to remove tag from
external_shipping_system_tag = 'external_shipping_system_tag_example' # str | The tag to delete

try:
    # Delete a tag for an externalShippingSystem.
    api_instance.delete_external_shipping_system_tag(external_shipping_system_id, external_shipping_system_tag)
except ApiException as e:
    print("Exception when calling ExternalShippingSystemApi->delete_external_shipping_system_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipping_system_id** | **int**| Id of the externalShippingSystem to remove tag from | 
 **external_shipping_system_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_external_shipping_system_by_id**
> ExternalShippingSystem get_duplicate_external_shipping_system_by_id(external_shipping_system_id)

Get a duplicated an externalShippingSystem by id

Returns a duplicated externalShippingSystem identified by the specified id.

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
api_instance = Infoplus.ExternalShippingSystemApi(Infoplus.ApiClient(configuration))
external_shipping_system_id = 56 # int | Id of the externalShippingSystem to be duplicated.

try:
    # Get a duplicated an externalShippingSystem by id
    api_response = api_instance.get_duplicate_external_shipping_system_by_id(external_shipping_system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalShippingSystemApi->get_duplicate_external_shipping_system_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipping_system_id** | **int**| Id of the externalShippingSystem to be duplicated. | 

### Return type

[**ExternalShippingSystem**](ExternalShippingSystem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_shipping_system_by_filter**
> list[ExternalShippingSystem] get_external_shipping_system_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search externalShippingSystems by filter

Returns the list of externalShippingSystems that match the given filter.

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
api_instance = Infoplus.ExternalShippingSystemApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search externalShippingSystems by filter
    api_response = api_instance.get_external_shipping_system_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalShippingSystemApi->get_external_shipping_system_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ExternalShippingSystem]**](ExternalShippingSystem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_shipping_system_by_id**
> ExternalShippingSystem get_external_shipping_system_by_id(external_shipping_system_id)

Get an externalShippingSystem by id

Returns the externalShippingSystem identified by the specified id.

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
api_instance = Infoplus.ExternalShippingSystemApi(Infoplus.ApiClient(configuration))
external_shipping_system_id = 56 # int | Id of the externalShippingSystem to be returned.

try:
    # Get an externalShippingSystem by id
    api_response = api_instance.get_external_shipping_system_by_id(external_shipping_system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalShippingSystemApi->get_external_shipping_system_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipping_system_id** | **int**| Id of the externalShippingSystem to be returned. | 

### Return type

[**ExternalShippingSystem**](ExternalShippingSystem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_shipping_system_tags**
> get_external_shipping_system_tags(external_shipping_system_id)

Get the tags for an externalShippingSystem.

Get all existing externalShippingSystem tags.

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
api_instance = Infoplus.ExternalShippingSystemApi(Infoplus.ApiClient(configuration))
external_shipping_system_id = 56 # int | Id of the externalShippingSystem to get tags for

try:
    # Get the tags for an externalShippingSystem.
    api_instance.get_external_shipping_system_tags(external_shipping_system_id)
except ApiException as e:
    print("Exception when calling ExternalShippingSystemApi->get_external_shipping_system_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipping_system_id** | **int**| Id of the externalShippingSystem to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_shipping_system**
> update_external_shipping_system(body)

Update an externalShippingSystem

Updates an existing externalShippingSystem using the specified data.

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
api_instance = Infoplus.ExternalShippingSystemApi(Infoplus.ApiClient(configuration))
body = Infoplus.ExternalShippingSystem() # ExternalShippingSystem | ExternalShippingSystem to be updated.

try:
    # Update an externalShippingSystem
    api_instance.update_external_shipping_system(body)
except ApiException as e:
    print("Exception when calling ExternalShippingSystemApi->update_external_shipping_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalShippingSystem**](ExternalShippingSystem.md)| ExternalShippingSystem to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_shipping_system_custom_fields**
> update_external_shipping_system_custom_fields(body)

Update an externalShippingSystem custom fields

Updates an existing externalShippingSystem custom fields using the specified data.

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
api_instance = Infoplus.ExternalShippingSystemApi(Infoplus.ApiClient(configuration))
body = Infoplus.ExternalShippingSystem() # ExternalShippingSystem | ExternalShippingSystem to be updated.

try:
    # Update an externalShippingSystem custom fields
    api_instance.update_external_shipping_system_custom_fields(body)
except ApiException as e:
    print("Exception when calling ExternalShippingSystemApi->update_external_shipping_system_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalShippingSystem**](ExternalShippingSystem.md)| ExternalShippingSystem to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

