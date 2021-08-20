# Infoplus.ShoppingCartConnectionApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_shopping_cart_connection**](ShoppingCartConnectionApi.md#add_shopping_cart_connection) | **POST** /beta/shoppingCartConnection | Create a shoppingCartConnection
[**add_shopping_cart_connection_audit**](ShoppingCartConnectionApi.md#add_shopping_cart_connection_audit) | **PUT** /beta/shoppingCartConnection/{shoppingCartConnectionId}/audit/{shoppingCartConnectionAudit} | Add new audit for a shoppingCartConnection
[**add_shopping_cart_connection_file**](ShoppingCartConnectionApi.md#add_shopping_cart_connection_file) | **POST** /beta/shoppingCartConnection/{shoppingCartConnectionId}/file/{fileName} | Attach a file to a shoppingCartConnection
[**add_shopping_cart_connection_file_by_url**](ShoppingCartConnectionApi.md#add_shopping_cart_connection_file_by_url) | **POST** /beta/shoppingCartConnection/{shoppingCartConnectionId}/file | Attach a file to a shoppingCartConnection by URL.
[**add_shopping_cart_connection_tag**](ShoppingCartConnectionApi.md#add_shopping_cart_connection_tag) | **PUT** /beta/shoppingCartConnection/{shoppingCartConnectionId}/tag/{shoppingCartConnectionTag} | Add new tags for a shoppingCartConnection.
[**delete_shopping_cart_connection**](ShoppingCartConnectionApi.md#delete_shopping_cart_connection) | **DELETE** /beta/shoppingCartConnection/{shoppingCartConnectionId} | Delete a shoppingCartConnection
[**delete_shopping_cart_connection_file**](ShoppingCartConnectionApi.md#delete_shopping_cart_connection_file) | **DELETE** /beta/shoppingCartConnection/{shoppingCartConnectionId}/file/{fileId} | Delete a file for a shoppingCartConnection.
[**delete_shopping_cart_connection_tag**](ShoppingCartConnectionApi.md#delete_shopping_cart_connection_tag) | **DELETE** /beta/shoppingCartConnection/{shoppingCartConnectionId}/tag/{shoppingCartConnectionTag} | Delete a tag for a shoppingCartConnection.
[**get_duplicate_shopping_cart_connection_by_id**](ShoppingCartConnectionApi.md#get_duplicate_shopping_cart_connection_by_id) | **GET** /beta/shoppingCartConnection/duplicate/{shoppingCartConnectionId} | Get a duplicated a shoppingCartConnection by id
[**get_shopping_cart_connection_by_filter**](ShoppingCartConnectionApi.md#get_shopping_cart_connection_by_filter) | **GET** /beta/shoppingCartConnection/search | Search shoppingCartConnections by filter
[**get_shopping_cart_connection_by_id**](ShoppingCartConnectionApi.md#get_shopping_cart_connection_by_id) | **GET** /beta/shoppingCartConnection/{shoppingCartConnectionId} | Get a shoppingCartConnection by id
[**get_shopping_cart_connection_files**](ShoppingCartConnectionApi.md#get_shopping_cart_connection_files) | **GET** /beta/shoppingCartConnection/{shoppingCartConnectionId}/file | Get the files for a shoppingCartConnection.
[**get_shopping_cart_connection_tags**](ShoppingCartConnectionApi.md#get_shopping_cart_connection_tags) | **GET** /beta/shoppingCartConnection/{shoppingCartConnectionId}/tag | Get the tags for a shoppingCartConnection.
[**update_shopping_cart_connection**](ShoppingCartConnectionApi.md#update_shopping_cart_connection) | **PUT** /beta/shoppingCartConnection | Update a shoppingCartConnection
[**update_shopping_cart_connection_custom_fields**](ShoppingCartConnectionApi.md#update_shopping_cart_connection_custom_fields) | **PUT** /beta/shoppingCartConnection/customFields | Update a shoppingCartConnection custom fields


# **add_shopping_cart_connection**
> ShoppingCartConnection add_shopping_cart_connection(body)

Create a shoppingCartConnection

Inserts a new shoppingCartConnection using the specified data.

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
api_instance = Infoplus.ShoppingCartConnectionApi(Infoplus.ApiClient(configuration))
body = Infoplus.ShoppingCartConnection() # ShoppingCartConnection | ShoppingCartConnection to be inserted.

try:
    # Create a shoppingCartConnection
    api_response = api_instance.add_shopping_cart_connection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShoppingCartConnectionApi->add_shopping_cart_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShoppingCartConnection**](ShoppingCartConnection.md)| ShoppingCartConnection to be inserted. | 

### Return type

[**ShoppingCartConnection**](ShoppingCartConnection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_shopping_cart_connection_audit**
> add_shopping_cart_connection_audit(shopping_cart_connection_id, shopping_cart_connection_audit)

Add new audit for a shoppingCartConnection

Adds an audit to an existing shoppingCartConnection.

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
api_instance = Infoplus.ShoppingCartConnectionApi(Infoplus.ApiClient(configuration))
shopping_cart_connection_id = 56 # int | Id of the shoppingCartConnection to add an audit to
shopping_cart_connection_audit = 'shopping_cart_connection_audit_example' # str | The audit to add

try:
    # Add new audit for a shoppingCartConnection
    api_instance.add_shopping_cart_connection_audit(shopping_cart_connection_id, shopping_cart_connection_audit)
except ApiException as e:
    print("Exception when calling ShoppingCartConnectionApi->add_shopping_cart_connection_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_connection_id** | **int**| Id of the shoppingCartConnection to add an audit to | 
 **shopping_cart_connection_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_shopping_cart_connection_file**
> add_shopping_cart_connection_file(shopping_cart_connection_id, file_name)

Attach a file to a shoppingCartConnection

Adds a file to an existing shoppingCartConnection.

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
api_instance = Infoplus.ShoppingCartConnectionApi(Infoplus.ApiClient(configuration))
shopping_cart_connection_id = 56 # int | Id of the shoppingCartConnection to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a shoppingCartConnection
    api_instance.add_shopping_cart_connection_file(shopping_cart_connection_id, file_name)
except ApiException as e:
    print("Exception when calling ShoppingCartConnectionApi->add_shopping_cart_connection_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_connection_id** | **int**| Id of the shoppingCartConnection to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_shopping_cart_connection_file_by_url**
> add_shopping_cart_connection_file_by_url(body, shopping_cart_connection_id)

Attach a file to a shoppingCartConnection by URL.

Adds a file to an existing shoppingCartConnection by URL.

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
api_instance = Infoplus.ShoppingCartConnectionApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
shopping_cart_connection_id = 56 # int | Id of the shoppingCartConnection to add an file to

try:
    # Attach a file to a shoppingCartConnection by URL.
    api_instance.add_shopping_cart_connection_file_by_url(body, shopping_cart_connection_id)
except ApiException as e:
    print("Exception when calling ShoppingCartConnectionApi->add_shopping_cart_connection_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **shopping_cart_connection_id** | **int**| Id of the shoppingCartConnection to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_shopping_cart_connection_tag**
> add_shopping_cart_connection_tag(shopping_cart_connection_id, shopping_cart_connection_tag)

Add new tags for a shoppingCartConnection.

Adds a tag to an existing shoppingCartConnection.

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
api_instance = Infoplus.ShoppingCartConnectionApi(Infoplus.ApiClient(configuration))
shopping_cart_connection_id = 56 # int | Id of the shoppingCartConnection to add a tag to
shopping_cart_connection_tag = 'shopping_cart_connection_tag_example' # str | The tag to add

try:
    # Add new tags for a shoppingCartConnection.
    api_instance.add_shopping_cart_connection_tag(shopping_cart_connection_id, shopping_cart_connection_tag)
except ApiException as e:
    print("Exception when calling ShoppingCartConnectionApi->add_shopping_cart_connection_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_connection_id** | **int**| Id of the shoppingCartConnection to add a tag to | 
 **shopping_cart_connection_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shopping_cart_connection**
> delete_shopping_cart_connection(shopping_cart_connection_id)

Delete a shoppingCartConnection

Deletes the shoppingCartConnection identified by the specified id.

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
api_instance = Infoplus.ShoppingCartConnectionApi(Infoplus.ApiClient(configuration))
shopping_cart_connection_id = 56 # int | Id of the shoppingCartConnection to be deleted.

try:
    # Delete a shoppingCartConnection
    api_instance.delete_shopping_cart_connection(shopping_cart_connection_id)
except ApiException as e:
    print("Exception when calling ShoppingCartConnectionApi->delete_shopping_cart_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_connection_id** | **int**| Id of the shoppingCartConnection to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shopping_cart_connection_file**
> delete_shopping_cart_connection_file(shopping_cart_connection_id, file_id)

Delete a file for a shoppingCartConnection.

Deletes an existing shoppingCartConnection file using the specified data.

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
api_instance = Infoplus.ShoppingCartConnectionApi(Infoplus.ApiClient(configuration))
shopping_cart_connection_id = 56 # int | Id of the shoppingCartConnection to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a shoppingCartConnection.
    api_instance.delete_shopping_cart_connection_file(shopping_cart_connection_id, file_id)
except ApiException as e:
    print("Exception when calling ShoppingCartConnectionApi->delete_shopping_cart_connection_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_connection_id** | **int**| Id of the shoppingCartConnection to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shopping_cart_connection_tag**
> delete_shopping_cart_connection_tag(shopping_cart_connection_id, shopping_cart_connection_tag)

Delete a tag for a shoppingCartConnection.

Deletes an existing shoppingCartConnection tag using the specified data.

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
api_instance = Infoplus.ShoppingCartConnectionApi(Infoplus.ApiClient(configuration))
shopping_cart_connection_id = 56 # int | Id of the shoppingCartConnection to remove tag from
shopping_cart_connection_tag = 'shopping_cart_connection_tag_example' # str | The tag to delete

try:
    # Delete a tag for a shoppingCartConnection.
    api_instance.delete_shopping_cart_connection_tag(shopping_cart_connection_id, shopping_cart_connection_tag)
except ApiException as e:
    print("Exception when calling ShoppingCartConnectionApi->delete_shopping_cart_connection_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_connection_id** | **int**| Id of the shoppingCartConnection to remove tag from | 
 **shopping_cart_connection_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_shopping_cart_connection_by_id**
> ShoppingCartConnection get_duplicate_shopping_cart_connection_by_id(shopping_cart_connection_id)

Get a duplicated a shoppingCartConnection by id

Returns a duplicated shoppingCartConnection identified by the specified id.

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
api_instance = Infoplus.ShoppingCartConnectionApi(Infoplus.ApiClient(configuration))
shopping_cart_connection_id = 56 # int | Id of the shoppingCartConnection to be duplicated.

try:
    # Get a duplicated a shoppingCartConnection by id
    api_response = api_instance.get_duplicate_shopping_cart_connection_by_id(shopping_cart_connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShoppingCartConnectionApi->get_duplicate_shopping_cart_connection_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_connection_id** | **int**| Id of the shoppingCartConnection to be duplicated. | 

### Return type

[**ShoppingCartConnection**](ShoppingCartConnection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shopping_cart_connection_by_filter**
> list[ShoppingCartConnection] get_shopping_cart_connection_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search shoppingCartConnections by filter

Returns the list of shoppingCartConnections that match the given filter.

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
api_instance = Infoplus.ShoppingCartConnectionApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search shoppingCartConnections by filter
    api_response = api_instance.get_shopping_cart_connection_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShoppingCartConnectionApi->get_shopping_cart_connection_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ShoppingCartConnection]**](ShoppingCartConnection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shopping_cart_connection_by_id**
> ShoppingCartConnection get_shopping_cart_connection_by_id(shopping_cart_connection_id)

Get a shoppingCartConnection by id

Returns the shoppingCartConnection identified by the specified id.

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
api_instance = Infoplus.ShoppingCartConnectionApi(Infoplus.ApiClient(configuration))
shopping_cart_connection_id = 56 # int | Id of the shoppingCartConnection to be returned.

try:
    # Get a shoppingCartConnection by id
    api_response = api_instance.get_shopping_cart_connection_by_id(shopping_cart_connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShoppingCartConnectionApi->get_shopping_cart_connection_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_connection_id** | **int**| Id of the shoppingCartConnection to be returned. | 

### Return type

[**ShoppingCartConnection**](ShoppingCartConnection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shopping_cart_connection_files**
> get_shopping_cart_connection_files(shopping_cart_connection_id)

Get the files for a shoppingCartConnection.

Get all existing shoppingCartConnection files.

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
api_instance = Infoplus.ShoppingCartConnectionApi(Infoplus.ApiClient(configuration))
shopping_cart_connection_id = 56 # int | Id of the shoppingCartConnection to get files for

try:
    # Get the files for a shoppingCartConnection.
    api_instance.get_shopping_cart_connection_files(shopping_cart_connection_id)
except ApiException as e:
    print("Exception when calling ShoppingCartConnectionApi->get_shopping_cart_connection_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_connection_id** | **int**| Id of the shoppingCartConnection to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shopping_cart_connection_tags**
> get_shopping_cart_connection_tags(shopping_cart_connection_id)

Get the tags for a shoppingCartConnection.

Get all existing shoppingCartConnection tags.

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
api_instance = Infoplus.ShoppingCartConnectionApi(Infoplus.ApiClient(configuration))
shopping_cart_connection_id = 56 # int | Id of the shoppingCartConnection to get tags for

try:
    # Get the tags for a shoppingCartConnection.
    api_instance.get_shopping_cart_connection_tags(shopping_cart_connection_id)
except ApiException as e:
    print("Exception when calling ShoppingCartConnectionApi->get_shopping_cart_connection_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopping_cart_connection_id** | **int**| Id of the shoppingCartConnection to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shopping_cart_connection**
> update_shopping_cart_connection(body)

Update a shoppingCartConnection

Updates an existing shoppingCartConnection using the specified data.

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
api_instance = Infoplus.ShoppingCartConnectionApi(Infoplus.ApiClient(configuration))
body = Infoplus.ShoppingCartConnection() # ShoppingCartConnection | ShoppingCartConnection to be updated.

try:
    # Update a shoppingCartConnection
    api_instance.update_shopping_cart_connection(body)
except ApiException as e:
    print("Exception when calling ShoppingCartConnectionApi->update_shopping_cart_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShoppingCartConnection**](ShoppingCartConnection.md)| ShoppingCartConnection to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shopping_cart_connection_custom_fields**
> update_shopping_cart_connection_custom_fields(body)

Update a shoppingCartConnection custom fields

Updates an existing shoppingCartConnection custom fields using the specified data.

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
api_instance = Infoplus.ShoppingCartConnectionApi(Infoplus.ApiClient(configuration))
body = Infoplus.ShoppingCartConnection() # ShoppingCartConnection | ShoppingCartConnection to be updated.

try:
    # Update a shoppingCartConnection custom fields
    api_instance.update_shopping_cart_connection_custom_fields(body)
except ApiException as e:
    print("Exception when calling ShoppingCartConnectionApi->update_shopping_cart_connection_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShoppingCartConnection**](ShoppingCartConnection.md)| ShoppingCartConnection to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

