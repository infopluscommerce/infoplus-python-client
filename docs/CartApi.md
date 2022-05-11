# Infoplus.CartApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cart**](CartApi.md#add_cart) | **POST** /v3.0/cart | Create a cart
[**add_cart_audit**](CartApi.md#add_cart_audit) | **PUT** /v3.0/cart/{cartId}/audit/{cartAudit} | Add new audit for a cart
[**add_cart_file**](CartApi.md#add_cart_file) | **POST** /v3.0/cart/{cartId}/file/{fileName} | Attach a file to a cart
[**add_cart_file_by_url**](CartApi.md#add_cart_file_by_url) | **POST** /v3.0/cart/{cartId}/file | Attach a file to a cart by URL.
[**add_cart_tag**](CartApi.md#add_cart_tag) | **PUT** /v3.0/cart/{cartId}/tag/{cartTag} | Add new tags for a cart.
[**delete_cart**](CartApi.md#delete_cart) | **DELETE** /v3.0/cart/{cartId} | Delete a cart
[**delete_cart_file**](CartApi.md#delete_cart_file) | **DELETE** /v3.0/cart/{cartId}/file/{fileId} | Delete a file for a cart.
[**delete_cart_tag**](CartApi.md#delete_cart_tag) | **DELETE** /v3.0/cart/{cartId}/tag/{cartTag} | Delete a tag for a cart.
[**get_cart_by_filter**](CartApi.md#get_cart_by_filter) | **GET** /v3.0/cart/search | Search carts by filter
[**get_cart_by_id**](CartApi.md#get_cart_by_id) | **GET** /v3.0/cart/{cartId} | Get a cart by id
[**get_cart_files**](CartApi.md#get_cart_files) | **GET** /v3.0/cart/{cartId}/file | Get the files for a cart.
[**get_cart_tags**](CartApi.md#get_cart_tags) | **GET** /v3.0/cart/{cartId}/tag | Get the tags for a cart.
[**get_duplicate_cart_by_id**](CartApi.md#get_duplicate_cart_by_id) | **GET** /v3.0/cart/duplicate/{cartId} | Get a duplicated a cart by id
[**update_cart**](CartApi.md#update_cart) | **PUT** /v3.0/cart | Update a cart


# **add_cart**
> Cart add_cart(body)

Create a cart

Inserts a new cart using the specified data.

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
api_instance = Infoplus.CartApi(Infoplus.ApiClient(configuration))
body = Infoplus.Cart() # Cart | Cart to be inserted.

try:
    # Create a cart
    api_response = api_instance.add_cart(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->add_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Cart**](Cart.md)| Cart to be inserted. | 

### Return type

[**Cart**](Cart.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_cart_audit**
> add_cart_audit(cart_id, cart_audit)

Add new audit for a cart

Adds an audit to an existing cart.

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
api_instance = Infoplus.CartApi(Infoplus.ApiClient(configuration))
cart_id = 56 # int | Id of the cart to add an audit to
cart_audit = 'cart_audit_example' # str | The audit to add

try:
    # Add new audit for a cart
    api_instance.add_cart_audit(cart_id, cart_audit)
except ApiException as e:
    print("Exception when calling CartApi->add_cart_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Id of the cart to add an audit to | 
 **cart_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_cart_file**
> add_cart_file(cart_id, file_name)

Attach a file to a cart

Adds a file to an existing cart.

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
api_instance = Infoplus.CartApi(Infoplus.ApiClient(configuration))
cart_id = 56 # int | Id of the cart to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a cart
    api_instance.add_cart_file(cart_id, file_name)
except ApiException as e:
    print("Exception when calling CartApi->add_cart_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Id of the cart to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_cart_file_by_url**
> add_cart_file_by_url(body, cart_id)

Attach a file to a cart by URL.

Adds a file to an existing cart by URL.

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
api_instance = Infoplus.CartApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
cart_id = 56 # int | Id of the cart to add an file to

try:
    # Attach a file to a cart by URL.
    api_instance.add_cart_file_by_url(body, cart_id)
except ApiException as e:
    print("Exception when calling CartApi->add_cart_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **cart_id** | **int**| Id of the cart to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_cart_tag**
> add_cart_tag(cart_id, cart_tag)

Add new tags for a cart.

Adds a tag to an existing cart.

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
api_instance = Infoplus.CartApi(Infoplus.ApiClient(configuration))
cart_id = 56 # int | Id of the cart to add a tag to
cart_tag = 'cart_tag_example' # str | The tag to add

try:
    # Add new tags for a cart.
    api_instance.add_cart_tag(cart_id, cart_tag)
except ApiException as e:
    print("Exception when calling CartApi->add_cart_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Id of the cart to add a tag to | 
 **cart_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cart**
> delete_cart(cart_id)

Delete a cart

Deletes the cart identified by the specified id.

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
api_instance = Infoplus.CartApi(Infoplus.ApiClient(configuration))
cart_id = 56 # int | Id of the cart to be deleted.

try:
    # Delete a cart
    api_instance.delete_cart(cart_id)
except ApiException as e:
    print("Exception when calling CartApi->delete_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Id of the cart to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cart_file**
> delete_cart_file(cart_id, file_id)

Delete a file for a cart.

Deletes an existing cart file using the specified data.

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
api_instance = Infoplus.CartApi(Infoplus.ApiClient(configuration))
cart_id = 56 # int | Id of the cart to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a cart.
    api_instance.delete_cart_file(cart_id, file_id)
except ApiException as e:
    print("Exception when calling CartApi->delete_cart_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Id of the cart to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cart_tag**
> delete_cart_tag(cart_id, cart_tag)

Delete a tag for a cart.

Deletes an existing cart tag using the specified data.

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
api_instance = Infoplus.CartApi(Infoplus.ApiClient(configuration))
cart_id = 56 # int | Id of the cart to remove tag from
cart_tag = 'cart_tag_example' # str | The tag to delete

try:
    # Delete a tag for a cart.
    api_instance.delete_cart_tag(cart_id, cart_tag)
except ApiException as e:
    print("Exception when calling CartApi->delete_cart_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Id of the cart to remove tag from | 
 **cart_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_by_filter**
> list[Cart] get_cart_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search carts by filter

Returns the list of carts that match the given filter.

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
api_instance = Infoplus.CartApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search carts by filter
    api_response = api_instance.get_cart_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->get_cart_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Cart]**](Cart.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_by_id**
> Cart get_cart_by_id(cart_id)

Get a cart by id

Returns the cart identified by the specified id.

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
api_instance = Infoplus.CartApi(Infoplus.ApiClient(configuration))
cart_id = 56 # int | Id of the cart to be returned.

try:
    # Get a cart by id
    api_response = api_instance.get_cart_by_id(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->get_cart_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Id of the cart to be returned. | 

### Return type

[**Cart**](Cart.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_files**
> get_cart_files(cart_id)

Get the files for a cart.

Get all existing cart files.

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
api_instance = Infoplus.CartApi(Infoplus.ApiClient(configuration))
cart_id = 56 # int | Id of the cart to get files for

try:
    # Get the files for a cart.
    api_instance.get_cart_files(cart_id)
except ApiException as e:
    print("Exception when calling CartApi->get_cart_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Id of the cart to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_tags**
> get_cart_tags(cart_id)

Get the tags for a cart.

Get all existing cart tags.

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
api_instance = Infoplus.CartApi(Infoplus.ApiClient(configuration))
cart_id = 56 # int | Id of the cart to get tags for

try:
    # Get the tags for a cart.
    api_instance.get_cart_tags(cart_id)
except ApiException as e:
    print("Exception when calling CartApi->get_cart_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Id of the cart to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_cart_by_id**
> Cart get_duplicate_cart_by_id(cart_id)

Get a duplicated a cart by id

Returns a duplicated cart identified by the specified id.

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
api_instance = Infoplus.CartApi(Infoplus.ApiClient(configuration))
cart_id = 56 # int | Id of the cart to be duplicated.

try:
    # Get a duplicated a cart by id
    api_response = api_instance.get_duplicate_cart_by_id(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->get_duplicate_cart_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Id of the cart to be duplicated. | 

### Return type

[**Cart**](Cart.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cart**
> update_cart(body)

Update a cart

Updates an existing cart using the specified data.

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
api_instance = Infoplus.CartApi(Infoplus.ApiClient(configuration))
body = Infoplus.Cart() # Cart | Cart to be updated.

try:
    # Update a cart
    api_instance.update_cart(body)
except ApiException as e:
    print("Exception when calling CartApi->update_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Cart**](Cart.md)| Cart to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

