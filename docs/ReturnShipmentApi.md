# Infoplus.ReturnShipmentApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_return_shipment_audit**](ReturnShipmentApi.md#add_return_shipment_audit) | **PUT** /beta/returnShipment/{returnShipmentId}/audit/{returnShipmentAudit} | Add new audit for a returnShipment
[**add_return_shipment_file**](ReturnShipmentApi.md#add_return_shipment_file) | **POST** /beta/returnShipment/{returnShipmentId}/file/{fileName} | Attach a file to a returnShipment
[**add_return_shipment_file_by_url**](ReturnShipmentApi.md#add_return_shipment_file_by_url) | **POST** /beta/returnShipment/{returnShipmentId}/file | Attach a file to a returnShipment by URL.
[**add_return_shipment_tag**](ReturnShipmentApi.md#add_return_shipment_tag) | **PUT** /beta/returnShipment/{returnShipmentId}/tag/{returnShipmentTag} | Add new tags for a returnShipment.
[**delete_return_shipment_file**](ReturnShipmentApi.md#delete_return_shipment_file) | **DELETE** /beta/returnShipment/{returnShipmentId}/file/{fileId} | Delete a file for a returnShipment.
[**delete_return_shipment_tag**](ReturnShipmentApi.md#delete_return_shipment_tag) | **DELETE** /beta/returnShipment/{returnShipmentId}/tag/{returnShipmentTag} | Delete a tag for a returnShipment.
[**get_duplicate_return_shipment_by_id**](ReturnShipmentApi.md#get_duplicate_return_shipment_by_id) | **GET** /beta/returnShipment/duplicate/{returnShipmentId} | Get a duplicated a returnShipment by id
[**get_return_shipment_by_filter**](ReturnShipmentApi.md#get_return_shipment_by_filter) | **GET** /beta/returnShipment/search | Search returnShipments by filter
[**get_return_shipment_by_id**](ReturnShipmentApi.md#get_return_shipment_by_id) | **GET** /beta/returnShipment/{returnShipmentId} | Get a returnShipment by id
[**get_return_shipment_files**](ReturnShipmentApi.md#get_return_shipment_files) | **GET** /beta/returnShipment/{returnShipmentId}/file | Get the files for a returnShipment.
[**get_return_shipment_tags**](ReturnShipmentApi.md#get_return_shipment_tags) | **GET** /beta/returnShipment/{returnShipmentId}/tag | Get the tags for a returnShipment.
[**update_return_shipment_custom_fields**](ReturnShipmentApi.md#update_return_shipment_custom_fields) | **PUT** /beta/returnShipment/customFields | Update a returnShipment custom fields


# **add_return_shipment_audit**
> add_return_shipment_audit(return_shipment_id, return_shipment_audit)

Add new audit for a returnShipment

Adds an audit to an existing returnShipment.

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
api_instance = Infoplus.ReturnShipmentApi(Infoplus.ApiClient(configuration))
return_shipment_id = 56 # int | Id of the returnShipment to add an audit to
return_shipment_audit = 'return_shipment_audit_example' # str | The audit to add

try:
    # Add new audit for a returnShipment
    api_instance.add_return_shipment_audit(return_shipment_id, return_shipment_audit)
except ApiException as e:
    print("Exception when calling ReturnShipmentApi->add_return_shipment_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_shipment_id** | **int**| Id of the returnShipment to add an audit to | 
 **return_shipment_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_return_shipment_file**
> add_return_shipment_file(return_shipment_id, file_name)

Attach a file to a returnShipment

Adds a file to an existing returnShipment.

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
api_instance = Infoplus.ReturnShipmentApi(Infoplus.ApiClient(configuration))
return_shipment_id = 56 # int | Id of the returnShipment to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a returnShipment
    api_instance.add_return_shipment_file(return_shipment_id, file_name)
except ApiException as e:
    print("Exception when calling ReturnShipmentApi->add_return_shipment_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_shipment_id** | **int**| Id of the returnShipment to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_return_shipment_file_by_url**
> add_return_shipment_file_by_url(body, return_shipment_id)

Attach a file to a returnShipment by URL.

Adds a file to an existing returnShipment by URL.

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
api_instance = Infoplus.ReturnShipmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
return_shipment_id = 56 # int | Id of the returnShipment to add an file to

try:
    # Attach a file to a returnShipment by URL.
    api_instance.add_return_shipment_file_by_url(body, return_shipment_id)
except ApiException as e:
    print("Exception when calling ReturnShipmentApi->add_return_shipment_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **return_shipment_id** | **int**| Id of the returnShipment to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_return_shipment_tag**
> add_return_shipment_tag(return_shipment_id, return_shipment_tag)

Add new tags for a returnShipment.

Adds a tag to an existing returnShipment.

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
api_instance = Infoplus.ReturnShipmentApi(Infoplus.ApiClient(configuration))
return_shipment_id = 56 # int | Id of the returnShipment to add a tag to
return_shipment_tag = 'return_shipment_tag_example' # str | The tag to add

try:
    # Add new tags for a returnShipment.
    api_instance.add_return_shipment_tag(return_shipment_id, return_shipment_tag)
except ApiException as e:
    print("Exception when calling ReturnShipmentApi->add_return_shipment_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_shipment_id** | **int**| Id of the returnShipment to add a tag to | 
 **return_shipment_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_return_shipment_file**
> delete_return_shipment_file(return_shipment_id, file_id)

Delete a file for a returnShipment.

Deletes an existing returnShipment file using the specified data.

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
api_instance = Infoplus.ReturnShipmentApi(Infoplus.ApiClient(configuration))
return_shipment_id = 56 # int | Id of the returnShipment to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a returnShipment.
    api_instance.delete_return_shipment_file(return_shipment_id, file_id)
except ApiException as e:
    print("Exception when calling ReturnShipmentApi->delete_return_shipment_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_shipment_id** | **int**| Id of the returnShipment to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_return_shipment_tag**
> delete_return_shipment_tag(return_shipment_id, return_shipment_tag)

Delete a tag for a returnShipment.

Deletes an existing returnShipment tag using the specified data.

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
api_instance = Infoplus.ReturnShipmentApi(Infoplus.ApiClient(configuration))
return_shipment_id = 56 # int | Id of the returnShipment to remove tag from
return_shipment_tag = 'return_shipment_tag_example' # str | The tag to delete

try:
    # Delete a tag for a returnShipment.
    api_instance.delete_return_shipment_tag(return_shipment_id, return_shipment_tag)
except ApiException as e:
    print("Exception when calling ReturnShipmentApi->delete_return_shipment_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_shipment_id** | **int**| Id of the returnShipment to remove tag from | 
 **return_shipment_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_return_shipment_by_id**
> ReturnShipment get_duplicate_return_shipment_by_id(return_shipment_id)

Get a duplicated a returnShipment by id

Returns a duplicated returnShipment identified by the specified id.

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
api_instance = Infoplus.ReturnShipmentApi(Infoplus.ApiClient(configuration))
return_shipment_id = 56 # int | Id of the returnShipment to be duplicated.

try:
    # Get a duplicated a returnShipment by id
    api_response = api_instance.get_duplicate_return_shipment_by_id(return_shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnShipmentApi->get_duplicate_return_shipment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_shipment_id** | **int**| Id of the returnShipment to be duplicated. | 

### Return type

[**ReturnShipment**](ReturnShipment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_shipment_by_filter**
> list[ReturnShipment] get_return_shipment_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search returnShipments by filter

Returns the list of returnShipments that match the given filter.

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
api_instance = Infoplus.ReturnShipmentApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search returnShipments by filter
    api_response = api_instance.get_return_shipment_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnShipmentApi->get_return_shipment_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ReturnShipment]**](ReturnShipment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_shipment_by_id**
> ReturnShipment get_return_shipment_by_id(return_shipment_id)

Get a returnShipment by id

Returns the returnShipment identified by the specified id.

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
api_instance = Infoplus.ReturnShipmentApi(Infoplus.ApiClient(configuration))
return_shipment_id = 56 # int | Id of the returnShipment to be returned.

try:
    # Get a returnShipment by id
    api_response = api_instance.get_return_shipment_by_id(return_shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReturnShipmentApi->get_return_shipment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_shipment_id** | **int**| Id of the returnShipment to be returned. | 

### Return type

[**ReturnShipment**](ReturnShipment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_shipment_files**
> get_return_shipment_files(return_shipment_id)

Get the files for a returnShipment.

Get all existing returnShipment files.

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
api_instance = Infoplus.ReturnShipmentApi(Infoplus.ApiClient(configuration))
return_shipment_id = 56 # int | Id of the returnShipment to get files for

try:
    # Get the files for a returnShipment.
    api_instance.get_return_shipment_files(return_shipment_id)
except ApiException as e:
    print("Exception when calling ReturnShipmentApi->get_return_shipment_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_shipment_id** | **int**| Id of the returnShipment to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_shipment_tags**
> get_return_shipment_tags(return_shipment_id)

Get the tags for a returnShipment.

Get all existing returnShipment tags.

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
api_instance = Infoplus.ReturnShipmentApi(Infoplus.ApiClient(configuration))
return_shipment_id = 56 # int | Id of the returnShipment to get tags for

try:
    # Get the tags for a returnShipment.
    api_instance.get_return_shipment_tags(return_shipment_id)
except ApiException as e:
    print("Exception when calling ReturnShipmentApi->get_return_shipment_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_shipment_id** | **int**| Id of the returnShipment to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_return_shipment_custom_fields**
> update_return_shipment_custom_fields(body)

Update a returnShipment custom fields

Updates an existing returnShipment custom fields using the specified data.

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
api_instance = Infoplus.ReturnShipmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.ReturnShipment() # ReturnShipment | ReturnShipment to be updated.

try:
    # Update a returnShipment custom fields
    api_instance.update_return_shipment_custom_fields(body)
except ApiException as e:
    print("Exception when calling ReturnShipmentApi->update_return_shipment_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReturnShipment**](ReturnShipment.md)| ReturnShipment to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

