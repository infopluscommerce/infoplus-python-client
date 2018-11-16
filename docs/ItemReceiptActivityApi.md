# Infoplus.ItemReceiptActivityApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_receipt_activity**](ItemReceiptActivityApi.md#add_item_receipt_activity) | **POST** /beta/itemReceiptActivity | Create an itemReceiptActivity
[**add_item_receipt_activity_audit**](ItemReceiptActivityApi.md#add_item_receipt_activity_audit) | **PUT** /beta/itemReceiptActivity/{itemReceiptActivityId}/audit/{itemReceiptActivityAudit} | Add new audit for an itemReceiptActivity
[**add_item_receipt_activity_tag**](ItemReceiptActivityApi.md#add_item_receipt_activity_tag) | **PUT** /beta/itemReceiptActivity/{itemReceiptActivityId}/tag/{itemReceiptActivityTag} | Add new tags for an itemReceiptActivity.
[**delete_item_receipt_activity**](ItemReceiptActivityApi.md#delete_item_receipt_activity) | **DELETE** /beta/itemReceiptActivity/{itemReceiptActivityId} | Delete an itemReceiptActivity
[**delete_item_receipt_activity_tag**](ItemReceiptActivityApi.md#delete_item_receipt_activity_tag) | **DELETE** /beta/itemReceiptActivity/{itemReceiptActivityId}/tag/{itemReceiptActivityTag} | Delete a tag for an itemReceiptActivity.
[**get_duplicate_item_receipt_activity_by_id**](ItemReceiptActivityApi.md#get_duplicate_item_receipt_activity_by_id) | **GET** /beta/itemReceiptActivity/duplicate/{itemReceiptActivityId} | Get a duplicated an itemReceiptActivity by id
[**get_item_receipt_activity_by_filter**](ItemReceiptActivityApi.md#get_item_receipt_activity_by_filter) | **GET** /beta/itemReceiptActivity/search | Search itemReceiptActivitys by filter
[**get_item_receipt_activity_by_id**](ItemReceiptActivityApi.md#get_item_receipt_activity_by_id) | **GET** /beta/itemReceiptActivity/{itemReceiptActivityId} | Get an itemReceiptActivity by id
[**get_item_receipt_activity_tags**](ItemReceiptActivityApi.md#get_item_receipt_activity_tags) | **GET** /beta/itemReceiptActivity/{itemReceiptActivityId}/tag | Get the tags for an itemReceiptActivity.
[**update_item_receipt_activity**](ItemReceiptActivityApi.md#update_item_receipt_activity) | **PUT** /beta/itemReceiptActivity | Update an itemReceiptActivity


# **add_item_receipt_activity**
> ItemReceiptActivity add_item_receipt_activity(body)

Create an itemReceiptActivity

Inserts a new itemReceiptActivity using the specified data.

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
api_instance = Infoplus.ItemReceiptActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemReceiptActivity() # ItemReceiptActivity | ItemReceiptActivity to be inserted.

try:
    # Create an itemReceiptActivity
    api_response = api_instance.add_item_receipt_activity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemReceiptActivityApi->add_item_receipt_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemReceiptActivity**](ItemReceiptActivity.md)| ItemReceiptActivity to be inserted. | 

### Return type

[**ItemReceiptActivity**](ItemReceiptActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_receipt_activity_audit**
> add_item_receipt_activity_audit(item_receipt_activity_id, item_receipt_activity_audit)

Add new audit for an itemReceiptActivity

Adds an audit to an existing itemReceiptActivity.

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
api_instance = Infoplus.ItemReceiptActivityApi(Infoplus.ApiClient(configuration))
item_receipt_activity_id = 56 # int | Id of the itemReceiptActivity to add an audit to
item_receipt_activity_audit = 'item_receipt_activity_audit_example' # str | The audit to add

try:
    # Add new audit for an itemReceiptActivity
    api_instance.add_item_receipt_activity_audit(item_receipt_activity_id, item_receipt_activity_audit)
except ApiException as e:
    print("Exception when calling ItemReceiptActivityApi->add_item_receipt_activity_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_activity_id** | **int**| Id of the itemReceiptActivity to add an audit to | 
 **item_receipt_activity_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_receipt_activity_tag**
> add_item_receipt_activity_tag(item_receipt_activity_id, item_receipt_activity_tag)

Add new tags for an itemReceiptActivity.

Adds a tag to an existing itemReceiptActivity.

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
api_instance = Infoplus.ItemReceiptActivityApi(Infoplus.ApiClient(configuration))
item_receipt_activity_id = 56 # int | Id of the itemReceiptActivity to add a tag to
item_receipt_activity_tag = 'item_receipt_activity_tag_example' # str | The tag to add

try:
    # Add new tags for an itemReceiptActivity.
    api_instance.add_item_receipt_activity_tag(item_receipt_activity_id, item_receipt_activity_tag)
except ApiException as e:
    print("Exception when calling ItemReceiptActivityApi->add_item_receipt_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_activity_id** | **int**| Id of the itemReceiptActivity to add a tag to | 
 **item_receipt_activity_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_receipt_activity**
> delete_item_receipt_activity(item_receipt_activity_id)

Delete an itemReceiptActivity

Deletes the itemReceiptActivity identified by the specified id.

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
api_instance = Infoplus.ItemReceiptActivityApi(Infoplus.ApiClient(configuration))
item_receipt_activity_id = 56 # int | Id of the itemReceiptActivity to be deleted.

try:
    # Delete an itemReceiptActivity
    api_instance.delete_item_receipt_activity(item_receipt_activity_id)
except ApiException as e:
    print("Exception when calling ItemReceiptActivityApi->delete_item_receipt_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_activity_id** | **int**| Id of the itemReceiptActivity to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_receipt_activity_tag**
> delete_item_receipt_activity_tag(item_receipt_activity_id, item_receipt_activity_tag)

Delete a tag for an itemReceiptActivity.

Deletes an existing itemReceiptActivity tag using the specified data.

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
api_instance = Infoplus.ItemReceiptActivityApi(Infoplus.ApiClient(configuration))
item_receipt_activity_id = 56 # int | Id of the itemReceiptActivity to remove tag from
item_receipt_activity_tag = 'item_receipt_activity_tag_example' # str | The tag to delete

try:
    # Delete a tag for an itemReceiptActivity.
    api_instance.delete_item_receipt_activity_tag(item_receipt_activity_id, item_receipt_activity_tag)
except ApiException as e:
    print("Exception when calling ItemReceiptActivityApi->delete_item_receipt_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_activity_id** | **int**| Id of the itemReceiptActivity to remove tag from | 
 **item_receipt_activity_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_item_receipt_activity_by_id**
> ItemReceiptActivity get_duplicate_item_receipt_activity_by_id(item_receipt_activity_id)

Get a duplicated an itemReceiptActivity by id

Returns a duplicated itemReceiptActivity identified by the specified id.

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
api_instance = Infoplus.ItemReceiptActivityApi(Infoplus.ApiClient(configuration))
item_receipt_activity_id = 56 # int | Id of the itemReceiptActivity to be duplicated.

try:
    # Get a duplicated an itemReceiptActivity by id
    api_response = api_instance.get_duplicate_item_receipt_activity_by_id(item_receipt_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemReceiptActivityApi->get_duplicate_item_receipt_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_activity_id** | **int**| Id of the itemReceiptActivity to be duplicated. | 

### Return type

[**ItemReceiptActivity**](ItemReceiptActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_receipt_activity_by_filter**
> list[ItemReceiptActivity] get_item_receipt_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search itemReceiptActivitys by filter

Returns the list of itemReceiptActivitys that match the given filter.

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
api_instance = Infoplus.ItemReceiptActivityApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search itemReceiptActivitys by filter
    api_response = api_instance.get_item_receipt_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemReceiptActivityApi->get_item_receipt_activity_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ItemReceiptActivity]**](ItemReceiptActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_receipt_activity_by_id**
> ItemReceiptActivity get_item_receipt_activity_by_id(item_receipt_activity_id)

Get an itemReceiptActivity by id

Returns the itemReceiptActivity identified by the specified id.

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
api_instance = Infoplus.ItemReceiptActivityApi(Infoplus.ApiClient(configuration))
item_receipt_activity_id = 56 # int | Id of the itemReceiptActivity to be returned.

try:
    # Get an itemReceiptActivity by id
    api_response = api_instance.get_item_receipt_activity_by_id(item_receipt_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemReceiptActivityApi->get_item_receipt_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_activity_id** | **int**| Id of the itemReceiptActivity to be returned. | 

### Return type

[**ItemReceiptActivity**](ItemReceiptActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_receipt_activity_tags**
> get_item_receipt_activity_tags(item_receipt_activity_id)

Get the tags for an itemReceiptActivity.

Get all existing itemReceiptActivity tags.

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
api_instance = Infoplus.ItemReceiptActivityApi(Infoplus.ApiClient(configuration))
item_receipt_activity_id = 56 # int | Id of the itemReceiptActivity to get tags for

try:
    # Get the tags for an itemReceiptActivity.
    api_instance.get_item_receipt_activity_tags(item_receipt_activity_id)
except ApiException as e:
    print("Exception when calling ItemReceiptActivityApi->get_item_receipt_activity_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_receipt_activity_id** | **int**| Id of the itemReceiptActivity to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_receipt_activity**
> update_item_receipt_activity(body)

Update an itemReceiptActivity

Updates an existing itemReceiptActivity using the specified data.

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
api_instance = Infoplus.ItemReceiptActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemReceiptActivity() # ItemReceiptActivity | ItemReceiptActivity to be updated.

try:
    # Update an itemReceiptActivity
    api_instance.update_item_receipt_activity(body)
except ApiException as e:
    print("Exception when calling ItemReceiptActivityApi->update_item_receipt_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemReceiptActivity**](ItemReceiptActivity.md)| ItemReceiptActivity to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

