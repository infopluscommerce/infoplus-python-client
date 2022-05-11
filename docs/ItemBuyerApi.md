# Infoplus.ItemBuyerApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_buyer**](ItemBuyerApi.md#add_item_buyer) | **POST** /v3.0/itemBuyer | Create an itemBuyer
[**add_item_buyer_audit**](ItemBuyerApi.md#add_item_buyer_audit) | **PUT** /v3.0/itemBuyer/{itemBuyerId}/audit/{itemBuyerAudit} | Add new audit for an itemBuyer
[**add_item_buyer_file**](ItemBuyerApi.md#add_item_buyer_file) | **POST** /v3.0/itemBuyer/{itemBuyerId}/file/{fileName} | Attach a file to an itemBuyer
[**add_item_buyer_file_by_url**](ItemBuyerApi.md#add_item_buyer_file_by_url) | **POST** /v3.0/itemBuyer/{itemBuyerId}/file | Attach a file to an itemBuyer by URL.
[**add_item_buyer_tag**](ItemBuyerApi.md#add_item_buyer_tag) | **PUT** /v3.0/itemBuyer/{itemBuyerId}/tag/{itemBuyerTag} | Add new tags for an itemBuyer.
[**delete_item_buyer**](ItemBuyerApi.md#delete_item_buyer) | **DELETE** /v3.0/itemBuyer/{itemBuyerId} | Delete an itemBuyer
[**delete_item_buyer_file**](ItemBuyerApi.md#delete_item_buyer_file) | **DELETE** /v3.0/itemBuyer/{itemBuyerId}/file/{fileId} | Delete a file for an itemBuyer.
[**delete_item_buyer_tag**](ItemBuyerApi.md#delete_item_buyer_tag) | **DELETE** /v3.0/itemBuyer/{itemBuyerId}/tag/{itemBuyerTag} | Delete a tag for an itemBuyer.
[**get_duplicate_item_buyer_by_id**](ItemBuyerApi.md#get_duplicate_item_buyer_by_id) | **GET** /v3.0/itemBuyer/duplicate/{itemBuyerId} | Get a duplicated an itemBuyer by id
[**get_item_buyer_by_filter**](ItemBuyerApi.md#get_item_buyer_by_filter) | **GET** /v3.0/itemBuyer/search | Search itemBuyers by filter
[**get_item_buyer_by_id**](ItemBuyerApi.md#get_item_buyer_by_id) | **GET** /v3.0/itemBuyer/{itemBuyerId} | Get an itemBuyer by id
[**get_item_buyer_files**](ItemBuyerApi.md#get_item_buyer_files) | **GET** /v3.0/itemBuyer/{itemBuyerId}/file | Get the files for an itemBuyer.
[**get_item_buyer_tags**](ItemBuyerApi.md#get_item_buyer_tags) | **GET** /v3.0/itemBuyer/{itemBuyerId}/tag | Get the tags for an itemBuyer.
[**update_item_buyer**](ItemBuyerApi.md#update_item_buyer) | **PUT** /v3.0/itemBuyer | Update an itemBuyer


# **add_item_buyer**
> ItemBuyer add_item_buyer(body)

Create an itemBuyer

Inserts a new itemBuyer using the specified data.

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
api_instance = Infoplus.ItemBuyerApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemBuyer() # ItemBuyer | ItemBuyer to be inserted.

try:
    # Create an itemBuyer
    api_response = api_instance.add_item_buyer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemBuyerApi->add_item_buyer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemBuyer**](ItemBuyer.md)| ItemBuyer to be inserted. | 

### Return type

[**ItemBuyer**](ItemBuyer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_buyer_audit**
> add_item_buyer_audit(item_buyer_id, item_buyer_audit)

Add new audit for an itemBuyer

Adds an audit to an existing itemBuyer.

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
api_instance = Infoplus.ItemBuyerApi(Infoplus.ApiClient(configuration))
item_buyer_id = 56 # int | Id of the itemBuyer to add an audit to
item_buyer_audit = 'item_buyer_audit_example' # str | The audit to add

try:
    # Add new audit for an itemBuyer
    api_instance.add_item_buyer_audit(item_buyer_id, item_buyer_audit)
except ApiException as e:
    print("Exception when calling ItemBuyerApi->add_item_buyer_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_buyer_id** | **int**| Id of the itemBuyer to add an audit to | 
 **item_buyer_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_buyer_file**
> add_item_buyer_file(item_buyer_id, file_name)

Attach a file to an itemBuyer

Adds a file to an existing itemBuyer.

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
api_instance = Infoplus.ItemBuyerApi(Infoplus.ApiClient(configuration))
item_buyer_id = 56 # int | Id of the itemBuyer to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an itemBuyer
    api_instance.add_item_buyer_file(item_buyer_id, file_name)
except ApiException as e:
    print("Exception when calling ItemBuyerApi->add_item_buyer_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_buyer_id** | **int**| Id of the itemBuyer to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_buyer_file_by_url**
> add_item_buyer_file_by_url(body, item_buyer_id)

Attach a file to an itemBuyer by URL.

Adds a file to an existing itemBuyer by URL.

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
api_instance = Infoplus.ItemBuyerApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
item_buyer_id = 56 # int | Id of the itemBuyer to add an file to

try:
    # Attach a file to an itemBuyer by URL.
    api_instance.add_item_buyer_file_by_url(body, item_buyer_id)
except ApiException as e:
    print("Exception when calling ItemBuyerApi->add_item_buyer_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **item_buyer_id** | **int**| Id of the itemBuyer to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_buyer_tag**
> add_item_buyer_tag(item_buyer_id, item_buyer_tag)

Add new tags for an itemBuyer.

Adds a tag to an existing itemBuyer.

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
api_instance = Infoplus.ItemBuyerApi(Infoplus.ApiClient(configuration))
item_buyer_id = 56 # int | Id of the itemBuyer to add a tag to
item_buyer_tag = 'item_buyer_tag_example' # str | The tag to add

try:
    # Add new tags for an itemBuyer.
    api_instance.add_item_buyer_tag(item_buyer_id, item_buyer_tag)
except ApiException as e:
    print("Exception when calling ItemBuyerApi->add_item_buyer_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_buyer_id** | **int**| Id of the itemBuyer to add a tag to | 
 **item_buyer_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_buyer**
> delete_item_buyer(item_buyer_id)

Delete an itemBuyer

Deletes the itemBuyer identified by the specified id.

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
api_instance = Infoplus.ItemBuyerApi(Infoplus.ApiClient(configuration))
item_buyer_id = 56 # int | Id of the itemBuyer to be deleted.

try:
    # Delete an itemBuyer
    api_instance.delete_item_buyer(item_buyer_id)
except ApiException as e:
    print("Exception when calling ItemBuyerApi->delete_item_buyer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_buyer_id** | **int**| Id of the itemBuyer to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_buyer_file**
> delete_item_buyer_file(item_buyer_id, file_id)

Delete a file for an itemBuyer.

Deletes an existing itemBuyer file using the specified data.

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
api_instance = Infoplus.ItemBuyerApi(Infoplus.ApiClient(configuration))
item_buyer_id = 56 # int | Id of the itemBuyer to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an itemBuyer.
    api_instance.delete_item_buyer_file(item_buyer_id, file_id)
except ApiException as e:
    print("Exception when calling ItemBuyerApi->delete_item_buyer_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_buyer_id** | **int**| Id of the itemBuyer to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_buyer_tag**
> delete_item_buyer_tag(item_buyer_id, item_buyer_tag)

Delete a tag for an itemBuyer.

Deletes an existing itemBuyer tag using the specified data.

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
api_instance = Infoplus.ItemBuyerApi(Infoplus.ApiClient(configuration))
item_buyer_id = 56 # int | Id of the itemBuyer to remove tag from
item_buyer_tag = 'item_buyer_tag_example' # str | The tag to delete

try:
    # Delete a tag for an itemBuyer.
    api_instance.delete_item_buyer_tag(item_buyer_id, item_buyer_tag)
except ApiException as e:
    print("Exception when calling ItemBuyerApi->delete_item_buyer_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_buyer_id** | **int**| Id of the itemBuyer to remove tag from | 
 **item_buyer_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_item_buyer_by_id**
> ItemBuyer get_duplicate_item_buyer_by_id(item_buyer_id)

Get a duplicated an itemBuyer by id

Returns a duplicated itemBuyer identified by the specified id.

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
api_instance = Infoplus.ItemBuyerApi(Infoplus.ApiClient(configuration))
item_buyer_id = 56 # int | Id of the itemBuyer to be duplicated.

try:
    # Get a duplicated an itemBuyer by id
    api_response = api_instance.get_duplicate_item_buyer_by_id(item_buyer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemBuyerApi->get_duplicate_item_buyer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_buyer_id** | **int**| Id of the itemBuyer to be duplicated. | 

### Return type

[**ItemBuyer**](ItemBuyer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_buyer_by_filter**
> list[ItemBuyer] get_item_buyer_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search itemBuyers by filter

Returns the list of itemBuyers that match the given filter.

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
api_instance = Infoplus.ItemBuyerApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search itemBuyers by filter
    api_response = api_instance.get_item_buyer_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemBuyerApi->get_item_buyer_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ItemBuyer]**](ItemBuyer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_buyer_by_id**
> ItemBuyer get_item_buyer_by_id(item_buyer_id)

Get an itemBuyer by id

Returns the itemBuyer identified by the specified id.

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
api_instance = Infoplus.ItemBuyerApi(Infoplus.ApiClient(configuration))
item_buyer_id = 56 # int | Id of the itemBuyer to be returned.

try:
    # Get an itemBuyer by id
    api_response = api_instance.get_item_buyer_by_id(item_buyer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemBuyerApi->get_item_buyer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_buyer_id** | **int**| Id of the itemBuyer to be returned. | 

### Return type

[**ItemBuyer**](ItemBuyer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_buyer_files**
> get_item_buyer_files(item_buyer_id)

Get the files for an itemBuyer.

Get all existing itemBuyer files.

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
api_instance = Infoplus.ItemBuyerApi(Infoplus.ApiClient(configuration))
item_buyer_id = 56 # int | Id of the itemBuyer to get files for

try:
    # Get the files for an itemBuyer.
    api_instance.get_item_buyer_files(item_buyer_id)
except ApiException as e:
    print("Exception when calling ItemBuyerApi->get_item_buyer_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_buyer_id** | **int**| Id of the itemBuyer to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_buyer_tags**
> get_item_buyer_tags(item_buyer_id)

Get the tags for an itemBuyer.

Get all existing itemBuyer tags.

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
api_instance = Infoplus.ItemBuyerApi(Infoplus.ApiClient(configuration))
item_buyer_id = 56 # int | Id of the itemBuyer to get tags for

try:
    # Get the tags for an itemBuyer.
    api_instance.get_item_buyer_tags(item_buyer_id)
except ApiException as e:
    print("Exception when calling ItemBuyerApi->get_item_buyer_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_buyer_id** | **int**| Id of the itemBuyer to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_buyer**
> update_item_buyer(body)

Update an itemBuyer

Updates an existing itemBuyer using the specified data.

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
api_instance = Infoplus.ItemBuyerApi(Infoplus.ApiClient(configuration))
body = Infoplus.ItemBuyer() # ItemBuyer | ItemBuyer to be updated.

try:
    # Update an itemBuyer
    api_instance.update_item_buyer(body)
except ApiException as e:
    print("Exception when calling ItemBuyerApi->update_item_buyer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemBuyer**](ItemBuyer.md)| ItemBuyer to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

