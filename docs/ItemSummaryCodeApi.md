# Infoplus.ItemSummaryCodeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_summary_code**](ItemSummaryCodeApi.md#add_item_summary_code) | **POST** /beta/itemSummaryCode | Create an itemSummaryCode
[**add_item_summary_code_audit**](ItemSummaryCodeApi.md#add_item_summary_code_audit) | **PUT** /beta/itemSummaryCode/{itemSummaryCodeId}/audit/{itemSummaryCodeAudit} | Add new audit for an itemSummaryCode
[**add_item_summary_code_tag**](ItemSummaryCodeApi.md#add_item_summary_code_tag) | **PUT** /beta/itemSummaryCode/{itemSummaryCodeId}/tag/{itemSummaryCodeTag} | Add new tags for an itemSummaryCode.
[**delete_item_summary_code**](ItemSummaryCodeApi.md#delete_item_summary_code) | **DELETE** /beta/itemSummaryCode/{itemSummaryCodeId} | Delete an itemSummaryCode
[**delete_item_summary_code_tag**](ItemSummaryCodeApi.md#delete_item_summary_code_tag) | **DELETE** /beta/itemSummaryCode/{itemSummaryCodeId}/tag/{itemSummaryCodeTag} | Delete a tag for an itemSummaryCode.
[**get_duplicate_item_summary_code_by_id**](ItemSummaryCodeApi.md#get_duplicate_item_summary_code_by_id) | **GET** /beta/itemSummaryCode/duplicate/{itemSummaryCodeId} | Get a duplicated an itemSummaryCode by id
[**get_item_summary_code_by_filter**](ItemSummaryCodeApi.md#get_item_summary_code_by_filter) | **GET** /beta/itemSummaryCode/search | Search itemSummaryCodes by filter
[**get_item_summary_code_by_id**](ItemSummaryCodeApi.md#get_item_summary_code_by_id) | **GET** /beta/itemSummaryCode/{itemSummaryCodeId} | Get an itemSummaryCode by id
[**get_item_summary_code_tags**](ItemSummaryCodeApi.md#get_item_summary_code_tags) | **GET** /beta/itemSummaryCode/{itemSummaryCodeId}/tag | Get the tags for an itemSummaryCode.
[**update_item_summary_code**](ItemSummaryCodeApi.md#update_item_summary_code) | **PUT** /beta/itemSummaryCode | Update an itemSummaryCode


# **add_item_summary_code**
> ItemSummaryCode add_item_summary_code(body)

Create an itemSummaryCode

Inserts a new itemSummaryCode using the specified data.

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
api_instance = Infoplus.ItemSummaryCodeApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemSummaryCode() # ItemSummaryCode | ItemSummaryCode to be inserted.

try:
    # Create an itemSummaryCode
    api_response = api_instance.add_item_summary_code(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSummaryCodeApi->add_item_summary_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemSummaryCode**](ItemSummaryCode.md)| ItemSummaryCode to be inserted. | 

### Return type

[**ItemSummaryCode**](ItemSummaryCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_summary_code_audit**
> add_item_summary_code_audit(item_summary_code_id, item_summary_code_audit)

Add new audit for an itemSummaryCode

Adds an audit to an existing itemSummaryCode.

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
api_instance = Infoplus.ItemSummaryCodeApi(Infoplus.ApiClient(configuration))
item_summary_code_id = 56 # int | Id of the itemSummaryCode to add an audit to
item_summary_code_audit = 'item_summary_code_audit_example' # str | The audit to add

try:
    # Add new audit for an itemSummaryCode
    api_instance.add_item_summary_code_audit(item_summary_code_id, item_summary_code_audit)
except ApiException as e:
    print("Exception when calling ItemSummaryCodeApi->add_item_summary_code_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_summary_code_id** | **int**| Id of the itemSummaryCode to add an audit to | 
 **item_summary_code_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_summary_code_tag**
> add_item_summary_code_tag(item_summary_code_id, item_summary_code_tag)

Add new tags for an itemSummaryCode.

Adds a tag to an existing itemSummaryCode.

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
api_instance = Infoplus.ItemSummaryCodeApi(Infoplus.ApiClient(configuration))
item_summary_code_id = 56 # int | Id of the itemSummaryCode to add a tag to
item_summary_code_tag = 'item_summary_code_tag_example' # str | The tag to add

try:
    # Add new tags for an itemSummaryCode.
    api_instance.add_item_summary_code_tag(item_summary_code_id, item_summary_code_tag)
except ApiException as e:
    print("Exception when calling ItemSummaryCodeApi->add_item_summary_code_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_summary_code_id** | **int**| Id of the itemSummaryCode to add a tag to | 
 **item_summary_code_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_summary_code**
> delete_item_summary_code(item_summary_code_id)

Delete an itemSummaryCode

Deletes the itemSummaryCode identified by the specified id.

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
api_instance = Infoplus.ItemSummaryCodeApi(Infoplus.ApiClient(configuration))
item_summary_code_id = 56 # int | Id of the itemSummaryCode to be deleted.

try:
    # Delete an itemSummaryCode
    api_instance.delete_item_summary_code(item_summary_code_id)
except ApiException as e:
    print("Exception when calling ItemSummaryCodeApi->delete_item_summary_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_summary_code_id** | **int**| Id of the itemSummaryCode to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_summary_code_tag**
> delete_item_summary_code_tag(item_summary_code_id, item_summary_code_tag)

Delete a tag for an itemSummaryCode.

Deletes an existing itemSummaryCode tag using the specified data.

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
api_instance = Infoplus.ItemSummaryCodeApi(Infoplus.ApiClient(configuration))
item_summary_code_id = 56 # int | Id of the itemSummaryCode to remove tag from
item_summary_code_tag = 'item_summary_code_tag_example' # str | The tag to delete

try:
    # Delete a tag for an itemSummaryCode.
    api_instance.delete_item_summary_code_tag(item_summary_code_id, item_summary_code_tag)
except ApiException as e:
    print("Exception when calling ItemSummaryCodeApi->delete_item_summary_code_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_summary_code_id** | **int**| Id of the itemSummaryCode to remove tag from | 
 **item_summary_code_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_item_summary_code_by_id**
> ItemSummaryCode get_duplicate_item_summary_code_by_id(item_summary_code_id)

Get a duplicated an itemSummaryCode by id

Returns a duplicated itemSummaryCode identified by the specified id.

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
api_instance = Infoplus.ItemSummaryCodeApi(Infoplus.ApiClient(configuration))
item_summary_code_id = 56 # int | Id of the itemSummaryCode to be duplicated.

try:
    # Get a duplicated an itemSummaryCode by id
    api_response = api_instance.get_duplicate_item_summary_code_by_id(item_summary_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSummaryCodeApi->get_duplicate_item_summary_code_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_summary_code_id** | **int**| Id of the itemSummaryCode to be duplicated. | 

### Return type

[**ItemSummaryCode**](ItemSummaryCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_summary_code_by_filter**
> list[ItemSummaryCode] get_item_summary_code_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search itemSummaryCodes by filter

Returns the list of itemSummaryCodes that match the given filter.

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
api_instance = Infoplus.ItemSummaryCodeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search itemSummaryCodes by filter
    api_response = api_instance.get_item_summary_code_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSummaryCodeApi->get_item_summary_code_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ItemSummaryCode]**](ItemSummaryCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_summary_code_by_id**
> ItemSummaryCode get_item_summary_code_by_id(item_summary_code_id)

Get an itemSummaryCode by id

Returns the itemSummaryCode identified by the specified id.

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
api_instance = Infoplus.ItemSummaryCodeApi(Infoplus.ApiClient(configuration))
item_summary_code_id = 56 # int | Id of the itemSummaryCode to be returned.

try:
    # Get an itemSummaryCode by id
    api_response = api_instance.get_item_summary_code_by_id(item_summary_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSummaryCodeApi->get_item_summary_code_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_summary_code_id** | **int**| Id of the itemSummaryCode to be returned. | 

### Return type

[**ItemSummaryCode**](ItemSummaryCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_summary_code_tags**
> get_item_summary_code_tags(item_summary_code_id)

Get the tags for an itemSummaryCode.

Get all existing itemSummaryCode tags.

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
api_instance = Infoplus.ItemSummaryCodeApi(Infoplus.ApiClient(configuration))
item_summary_code_id = 56 # int | Id of the itemSummaryCode to get tags for

try:
    # Get the tags for an itemSummaryCode.
    api_instance.get_item_summary_code_tags(item_summary_code_id)
except ApiException as e:
    print("Exception when calling ItemSummaryCodeApi->get_item_summary_code_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_summary_code_id** | **int**| Id of the itemSummaryCode to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_summary_code**
> update_item_summary_code(body)

Update an itemSummaryCode

Updates an existing itemSummaryCode using the specified data.

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
api_instance = Infoplus.ItemSummaryCodeApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemSummaryCode() # ItemSummaryCode | ItemSummaryCode to be updated.

try:
    # Update an itemSummaryCode
    api_instance.update_item_summary_code(body)
except ApiException as e:
    print("Exception when calling ItemSummaryCodeApi->update_item_summary_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemSummaryCode**](ItemSummaryCode.md)| ItemSummaryCode to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

