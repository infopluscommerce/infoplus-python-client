# Infoplus.ItemSerialSchemeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_serial_scheme**](ItemSerialSchemeApi.md#add_item_serial_scheme) | **POST** /beta/itemSerialScheme | Create an itemSerialScheme
[**add_item_serial_scheme_audit**](ItemSerialSchemeApi.md#add_item_serial_scheme_audit) | **PUT** /beta/itemSerialScheme/{itemSerialSchemeId}/audit/{itemSerialSchemeAudit} | Add new audit for an itemSerialScheme
[**add_item_serial_scheme_tag**](ItemSerialSchemeApi.md#add_item_serial_scheme_tag) | **PUT** /beta/itemSerialScheme/{itemSerialSchemeId}/tag/{itemSerialSchemeTag} | Add new tags for an itemSerialScheme.
[**delete_item_serial_scheme**](ItemSerialSchemeApi.md#delete_item_serial_scheme) | **DELETE** /beta/itemSerialScheme/{itemSerialSchemeId} | Delete an itemSerialScheme
[**delete_item_serial_scheme_tag**](ItemSerialSchemeApi.md#delete_item_serial_scheme_tag) | **DELETE** /beta/itemSerialScheme/{itemSerialSchemeId}/tag/{itemSerialSchemeTag} | Delete a tag for an itemSerialScheme.
[**get_duplicate_item_serial_scheme_by_id**](ItemSerialSchemeApi.md#get_duplicate_item_serial_scheme_by_id) | **GET** /beta/itemSerialScheme/duplicate/{itemSerialSchemeId} | Get a duplicated an itemSerialScheme by id
[**get_item_serial_scheme_by_filter**](ItemSerialSchemeApi.md#get_item_serial_scheme_by_filter) | **GET** /beta/itemSerialScheme/search | Search itemSerialSchemes by filter
[**get_item_serial_scheme_by_id**](ItemSerialSchemeApi.md#get_item_serial_scheme_by_id) | **GET** /beta/itemSerialScheme/{itemSerialSchemeId} | Get an itemSerialScheme by id
[**get_item_serial_scheme_tags**](ItemSerialSchemeApi.md#get_item_serial_scheme_tags) | **GET** /beta/itemSerialScheme/{itemSerialSchemeId}/tag | Get the tags for an itemSerialScheme.
[**update_item_serial_scheme**](ItemSerialSchemeApi.md#update_item_serial_scheme) | **PUT** /beta/itemSerialScheme | Update an itemSerialScheme


# **add_item_serial_scheme**
> ItemSerialScheme add_item_serial_scheme(body)

Create an itemSerialScheme

Inserts a new itemSerialScheme using the specified data.

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
api_instance = Infoplus.ItemSerialSchemeApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemSerialScheme() # ItemSerialScheme | ItemSerialScheme to be inserted.

try:
    # Create an itemSerialScheme
    api_response = api_instance.add_item_serial_scheme(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSerialSchemeApi->add_item_serial_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemSerialScheme**](ItemSerialScheme.md)| ItemSerialScheme to be inserted. | 

### Return type

[**ItemSerialScheme**](ItemSerialScheme.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_serial_scheme_audit**
> add_item_serial_scheme_audit(item_serial_scheme_id, item_serial_scheme_audit)

Add new audit for an itemSerialScheme

Adds an audit to an existing itemSerialScheme.

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
api_instance = Infoplus.ItemSerialSchemeApi(Infoplus.ApiClient(configuration))
item_serial_scheme_id = 56 # int | Id of the itemSerialScheme to add an audit to
item_serial_scheme_audit = 'item_serial_scheme_audit_example' # str | The audit to add

try:
    # Add new audit for an itemSerialScheme
    api_instance.add_item_serial_scheme_audit(item_serial_scheme_id, item_serial_scheme_audit)
except ApiException as e:
    print("Exception when calling ItemSerialSchemeApi->add_item_serial_scheme_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_scheme_id** | **int**| Id of the itemSerialScheme to add an audit to | 
 **item_serial_scheme_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_serial_scheme_tag**
> add_item_serial_scheme_tag(item_serial_scheme_id, item_serial_scheme_tag)

Add new tags for an itemSerialScheme.

Adds a tag to an existing itemSerialScheme.

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
api_instance = Infoplus.ItemSerialSchemeApi(Infoplus.ApiClient(configuration))
item_serial_scheme_id = 56 # int | Id of the itemSerialScheme to add a tag to
item_serial_scheme_tag = 'item_serial_scheme_tag_example' # str | The tag to add

try:
    # Add new tags for an itemSerialScheme.
    api_instance.add_item_serial_scheme_tag(item_serial_scheme_id, item_serial_scheme_tag)
except ApiException as e:
    print("Exception when calling ItemSerialSchemeApi->add_item_serial_scheme_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_scheme_id** | **int**| Id of the itemSerialScheme to add a tag to | 
 **item_serial_scheme_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_serial_scheme**
> delete_item_serial_scheme(item_serial_scheme_id)

Delete an itemSerialScheme

Deletes the itemSerialScheme identified by the specified id.

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
api_instance = Infoplus.ItemSerialSchemeApi(Infoplus.ApiClient(configuration))
item_serial_scheme_id = 56 # int | Id of the itemSerialScheme to be deleted.

try:
    # Delete an itemSerialScheme
    api_instance.delete_item_serial_scheme(item_serial_scheme_id)
except ApiException as e:
    print("Exception when calling ItemSerialSchemeApi->delete_item_serial_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_scheme_id** | **int**| Id of the itemSerialScheme to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_serial_scheme_tag**
> delete_item_serial_scheme_tag(item_serial_scheme_id, item_serial_scheme_tag)

Delete a tag for an itemSerialScheme.

Deletes an existing itemSerialScheme tag using the specified data.

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
api_instance = Infoplus.ItemSerialSchemeApi(Infoplus.ApiClient(configuration))
item_serial_scheme_id = 56 # int | Id of the itemSerialScheme to remove tag from
item_serial_scheme_tag = 'item_serial_scheme_tag_example' # str | The tag to delete

try:
    # Delete a tag for an itemSerialScheme.
    api_instance.delete_item_serial_scheme_tag(item_serial_scheme_id, item_serial_scheme_tag)
except ApiException as e:
    print("Exception when calling ItemSerialSchemeApi->delete_item_serial_scheme_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_scheme_id** | **int**| Id of the itemSerialScheme to remove tag from | 
 **item_serial_scheme_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_item_serial_scheme_by_id**
> ItemSerialScheme get_duplicate_item_serial_scheme_by_id(item_serial_scheme_id)

Get a duplicated an itemSerialScheme by id

Returns a duplicated itemSerialScheme identified by the specified id.

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
api_instance = Infoplus.ItemSerialSchemeApi(Infoplus.ApiClient(configuration))
item_serial_scheme_id = 56 # int | Id of the itemSerialScheme to be duplicated.

try:
    # Get a duplicated an itemSerialScheme by id
    api_response = api_instance.get_duplicate_item_serial_scheme_by_id(item_serial_scheme_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSerialSchemeApi->get_duplicate_item_serial_scheme_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_scheme_id** | **int**| Id of the itemSerialScheme to be duplicated. | 

### Return type

[**ItemSerialScheme**](ItemSerialScheme.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_serial_scheme_by_filter**
> list[ItemSerialScheme] get_item_serial_scheme_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search itemSerialSchemes by filter

Returns the list of itemSerialSchemes that match the given filter.

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
api_instance = Infoplus.ItemSerialSchemeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search itemSerialSchemes by filter
    api_response = api_instance.get_item_serial_scheme_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSerialSchemeApi->get_item_serial_scheme_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ItemSerialScheme]**](ItemSerialScheme.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_serial_scheme_by_id**
> ItemSerialScheme get_item_serial_scheme_by_id(item_serial_scheme_id)

Get an itemSerialScheme by id

Returns the itemSerialScheme identified by the specified id.

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
api_instance = Infoplus.ItemSerialSchemeApi(Infoplus.ApiClient(configuration))
item_serial_scheme_id = 56 # int | Id of the itemSerialScheme to be returned.

try:
    # Get an itemSerialScheme by id
    api_response = api_instance.get_item_serial_scheme_by_id(item_serial_scheme_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSerialSchemeApi->get_item_serial_scheme_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_scheme_id** | **int**| Id of the itemSerialScheme to be returned. | 

### Return type

[**ItemSerialScheme**](ItemSerialScheme.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_serial_scheme_tags**
> get_item_serial_scheme_tags(item_serial_scheme_id)

Get the tags for an itemSerialScheme.

Get all existing itemSerialScheme tags.

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
api_instance = Infoplus.ItemSerialSchemeApi(Infoplus.ApiClient(configuration))
item_serial_scheme_id = 56 # int | Id of the itemSerialScheme to get tags for

try:
    # Get the tags for an itemSerialScheme.
    api_instance.get_item_serial_scheme_tags(item_serial_scheme_id)
except ApiException as e:
    print("Exception when calling ItemSerialSchemeApi->get_item_serial_scheme_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_serial_scheme_id** | **int**| Id of the itemSerialScheme to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_serial_scheme**
> update_item_serial_scheme(body)

Update an itemSerialScheme

Updates an existing itemSerialScheme using the specified data.

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
api_instance = Infoplus.ItemSerialSchemeApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemSerialScheme() # ItemSerialScheme | ItemSerialScheme to be updated.

try:
    # Update an itemSerialScheme
    api_instance.update_item_serial_scheme(body)
except ApiException as e:
    print("Exception when calling ItemSerialSchemeApi->update_item_serial_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemSerialScheme**](ItemSerialScheme.md)| ItemSerialScheme to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

