# Infoplus.ItemAccountCodeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_account_code**](ItemAccountCodeApi.md#add_item_account_code) | **POST** /beta/itemAccountCode | Create an itemAccountCode
[**add_item_account_code_audit**](ItemAccountCodeApi.md#add_item_account_code_audit) | **PUT** /beta/itemAccountCode/{itemAccountCodeId}/audit/{itemAccountCodeAudit} | Add new audit for an itemAccountCode
[**add_item_account_code_tag**](ItemAccountCodeApi.md#add_item_account_code_tag) | **PUT** /beta/itemAccountCode/{itemAccountCodeId}/tag/{itemAccountCodeTag} | Add new tags for an itemAccountCode.
[**delete_item_account_code**](ItemAccountCodeApi.md#delete_item_account_code) | **DELETE** /beta/itemAccountCode/{itemAccountCodeId} | Delete an itemAccountCode
[**delete_item_account_code_tag**](ItemAccountCodeApi.md#delete_item_account_code_tag) | **DELETE** /beta/itemAccountCode/{itemAccountCodeId}/tag/{itemAccountCodeTag} | Delete a tag for an itemAccountCode.
[**get_duplicate_item_account_code_by_id**](ItemAccountCodeApi.md#get_duplicate_item_account_code_by_id) | **GET** /beta/itemAccountCode/duplicate/{itemAccountCodeId} | Get a duplicated an itemAccountCode by id
[**get_item_account_code_by_filter**](ItemAccountCodeApi.md#get_item_account_code_by_filter) | **GET** /beta/itemAccountCode/search | Search itemAccountCodes by filter
[**get_item_account_code_by_id**](ItemAccountCodeApi.md#get_item_account_code_by_id) | **GET** /beta/itemAccountCode/{itemAccountCodeId} | Get an itemAccountCode by id
[**get_item_account_code_tags**](ItemAccountCodeApi.md#get_item_account_code_tags) | **GET** /beta/itemAccountCode/{itemAccountCodeId}/tag | Get the tags for an itemAccountCode.
[**update_item_account_code**](ItemAccountCodeApi.md#update_item_account_code) | **PUT** /beta/itemAccountCode | Update an itemAccountCode


# **add_item_account_code**
> ItemAccountCode add_item_account_code(body)

Create an itemAccountCode

Inserts a new itemAccountCode using the specified data.

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
api_instance = Infoplus.ItemAccountCodeApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemAccountCode() # ItemAccountCode | ItemAccountCode to be inserted.

try:
    # Create an itemAccountCode
    api_response = api_instance.add_item_account_code(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemAccountCodeApi->add_item_account_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemAccountCode**](ItemAccountCode.md)| ItemAccountCode to be inserted. | 

### Return type

[**ItemAccountCode**](ItemAccountCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_account_code_audit**
> add_item_account_code_audit(item_account_code_id, item_account_code_audit)

Add new audit for an itemAccountCode

Adds an audit to an existing itemAccountCode.

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
api_instance = Infoplus.ItemAccountCodeApi(Infoplus.ApiClient(configuration))
item_account_code_id = 56 # int | Id of the itemAccountCode to add an audit to
item_account_code_audit = 'item_account_code_audit_example' # str | The audit to add

try:
    # Add new audit for an itemAccountCode
    api_instance.add_item_account_code_audit(item_account_code_id, item_account_code_audit)
except ApiException as e:
    print("Exception when calling ItemAccountCodeApi->add_item_account_code_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_account_code_id** | **int**| Id of the itemAccountCode to add an audit to | 
 **item_account_code_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_account_code_tag**
> add_item_account_code_tag(item_account_code_id, item_account_code_tag)

Add new tags for an itemAccountCode.

Adds a tag to an existing itemAccountCode.

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
api_instance = Infoplus.ItemAccountCodeApi(Infoplus.ApiClient(configuration))
item_account_code_id = 56 # int | Id of the itemAccountCode to add a tag to
item_account_code_tag = 'item_account_code_tag_example' # str | The tag to add

try:
    # Add new tags for an itemAccountCode.
    api_instance.add_item_account_code_tag(item_account_code_id, item_account_code_tag)
except ApiException as e:
    print("Exception when calling ItemAccountCodeApi->add_item_account_code_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_account_code_id** | **int**| Id of the itemAccountCode to add a tag to | 
 **item_account_code_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_account_code**
> delete_item_account_code(item_account_code_id)

Delete an itemAccountCode

Deletes the itemAccountCode identified by the specified id.

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
api_instance = Infoplus.ItemAccountCodeApi(Infoplus.ApiClient(configuration))
item_account_code_id = 56 # int | Id of the itemAccountCode to be deleted.

try:
    # Delete an itemAccountCode
    api_instance.delete_item_account_code(item_account_code_id)
except ApiException as e:
    print("Exception when calling ItemAccountCodeApi->delete_item_account_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_account_code_id** | **int**| Id of the itemAccountCode to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_account_code_tag**
> delete_item_account_code_tag(item_account_code_id, item_account_code_tag)

Delete a tag for an itemAccountCode.

Deletes an existing itemAccountCode tag using the specified data.

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
api_instance = Infoplus.ItemAccountCodeApi(Infoplus.ApiClient(configuration))
item_account_code_id = 56 # int | Id of the itemAccountCode to remove tag from
item_account_code_tag = 'item_account_code_tag_example' # str | The tag to delete

try:
    # Delete a tag for an itemAccountCode.
    api_instance.delete_item_account_code_tag(item_account_code_id, item_account_code_tag)
except ApiException as e:
    print("Exception when calling ItemAccountCodeApi->delete_item_account_code_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_account_code_id** | **int**| Id of the itemAccountCode to remove tag from | 
 **item_account_code_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_item_account_code_by_id**
> ItemAccountCode get_duplicate_item_account_code_by_id(item_account_code_id)

Get a duplicated an itemAccountCode by id

Returns a duplicated itemAccountCode identified by the specified id.

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
api_instance = Infoplus.ItemAccountCodeApi(Infoplus.ApiClient(configuration))
item_account_code_id = 56 # int | Id of the itemAccountCode to be duplicated.

try:
    # Get a duplicated an itemAccountCode by id
    api_response = api_instance.get_duplicate_item_account_code_by_id(item_account_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemAccountCodeApi->get_duplicate_item_account_code_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_account_code_id** | **int**| Id of the itemAccountCode to be duplicated. | 

### Return type

[**ItemAccountCode**](ItemAccountCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_account_code_by_filter**
> list[ItemAccountCode] get_item_account_code_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search itemAccountCodes by filter

Returns the list of itemAccountCodes that match the given filter.

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
api_instance = Infoplus.ItemAccountCodeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search itemAccountCodes by filter
    api_response = api_instance.get_item_account_code_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemAccountCodeApi->get_item_account_code_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ItemAccountCode]**](ItemAccountCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_account_code_by_id**
> ItemAccountCode get_item_account_code_by_id(item_account_code_id)

Get an itemAccountCode by id

Returns the itemAccountCode identified by the specified id.

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
api_instance = Infoplus.ItemAccountCodeApi(Infoplus.ApiClient(configuration))
item_account_code_id = 56 # int | Id of the itemAccountCode to be returned.

try:
    # Get an itemAccountCode by id
    api_response = api_instance.get_item_account_code_by_id(item_account_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemAccountCodeApi->get_item_account_code_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_account_code_id** | **int**| Id of the itemAccountCode to be returned. | 

### Return type

[**ItemAccountCode**](ItemAccountCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_account_code_tags**
> get_item_account_code_tags(item_account_code_id)

Get the tags for an itemAccountCode.

Get all existing itemAccountCode tags.

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
api_instance = Infoplus.ItemAccountCodeApi(Infoplus.ApiClient(configuration))
item_account_code_id = 56 # int | Id of the itemAccountCode to get tags for

try:
    # Get the tags for an itemAccountCode.
    api_instance.get_item_account_code_tags(item_account_code_id)
except ApiException as e:
    print("Exception when calling ItemAccountCodeApi->get_item_account_code_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_account_code_id** | **int**| Id of the itemAccountCode to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_account_code**
> update_item_account_code(body)

Update an itemAccountCode

Updates an existing itemAccountCode using the specified data.

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
api_instance = Infoplus.ItemAccountCodeApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemAccountCode() # ItemAccountCode | ItemAccountCode to be updated.

try:
    # Update an itemAccountCode
    api_instance.update_item_account_code(body)
except ApiException as e:
    print("Exception when calling ItemAccountCodeApi->update_item_account_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemAccountCode**](ItemAccountCode.md)| ItemAccountCode to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

