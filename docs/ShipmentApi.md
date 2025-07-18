# Infoplus.ShipmentApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_shipment_audit**](ShipmentApi.md#add_shipment_audit) | **PUT** /beta/shipment/{shipmentId}/audit/{shipmentAudit} | Add new audit for a shipment
[**add_shipment_file**](ShipmentApi.md#add_shipment_file) | **POST** /beta/shipment/{shipmentId}/file/{fileName} | Attach a file to a shipment
[**add_shipment_file_by_url**](ShipmentApi.md#add_shipment_file_by_url) | **POST** /beta/shipment/{shipmentId}/file | Attach a file to a shipment by URL.
[**add_shipment_tag**](ShipmentApi.md#add_shipment_tag) | **PUT** /beta/shipment/{shipmentId}/tag/{shipmentTag} | Add new tags for a shipment.
[**delete_shipment_file**](ShipmentApi.md#delete_shipment_file) | **DELETE** /beta/shipment/{shipmentId}/file/{fileId} | Delete a file for a shipment.
[**delete_shipment_tag**](ShipmentApi.md#delete_shipment_tag) | **DELETE** /beta/shipment/{shipmentId}/tag/{shipmentTag} | Delete a tag for a shipment.
[**get_duplicate_shipment_by_id**](ShipmentApi.md#get_duplicate_shipment_by_id) | **GET** /beta/shipment/duplicate/{shipmentId} | Get a duplicated a shipment by id
[**get_shipment_by_filter**](ShipmentApi.md#get_shipment_by_filter) | **GET** /beta/shipment/search | Search shipments by filter
[**get_shipment_by_id**](ShipmentApi.md#get_shipment_by_id) | **GET** /beta/shipment/{shipmentId} | Get a shipment by id
[**get_shipment_files**](ShipmentApi.md#get_shipment_files) | **GET** /beta/shipment/{shipmentId}/file | Get the files for a shipment.
[**get_shipment_tags**](ShipmentApi.md#get_shipment_tags) | **GET** /beta/shipment/{shipmentId}/tag | Get the tags for a shipment.
[**update_shipment_custom_fields**](ShipmentApi.md#update_shipment_custom_fields) | **PUT** /beta/shipment/customFields | Update a shipment custom fields


# **add_shipment_audit**
> add_shipment_audit(shipment_id, shipment_audit)

Add new audit for a shipment

Adds an audit to an existing shipment.

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
api_instance = Infoplus.ShipmentApi(Infoplus.ApiClient(configuration))
shipment_id = 56 # int | Id of the shipment to add an audit to
shipment_audit = 'shipment_audit_example' # str | The audit to add

try:
    # Add new audit for a shipment
    api_instance.add_shipment_audit(shipment_id, shipment_audit)
except ApiException as e:
    print("Exception when calling ShipmentApi->add_shipment_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**| Id of the shipment to add an audit to | 
 **shipment_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_shipment_file**
> add_shipment_file(shipment_id, file_name)

Attach a file to a shipment

Adds a file to an existing shipment.

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
api_instance = Infoplus.ShipmentApi(Infoplus.ApiClient(configuration))
shipment_id = 56 # int | Id of the shipment to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a shipment
    api_instance.add_shipment_file(shipment_id, file_name)
except ApiException as e:
    print("Exception when calling ShipmentApi->add_shipment_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**| Id of the shipment to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_shipment_file_by_url**
> add_shipment_file_by_url(body, shipment_id)

Attach a file to a shipment by URL.

Adds a file to an existing shipment by URL.

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
api_instance = Infoplus.ShipmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
shipment_id = 56 # int | Id of the shipment to add an file to

try:
    # Attach a file to a shipment by URL.
    api_instance.add_shipment_file_by_url(body, shipment_id)
except ApiException as e:
    print("Exception when calling ShipmentApi->add_shipment_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **shipment_id** | **int**| Id of the shipment to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_shipment_tag**
> add_shipment_tag(shipment_id, shipment_tag)

Add new tags for a shipment.

Adds a tag to an existing shipment.

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
api_instance = Infoplus.ShipmentApi(Infoplus.ApiClient(configuration))
shipment_id = 56 # int | Id of the shipment to add a tag to
shipment_tag = 'shipment_tag_example' # str | The tag to add

try:
    # Add new tags for a shipment.
    api_instance.add_shipment_tag(shipment_id, shipment_tag)
except ApiException as e:
    print("Exception when calling ShipmentApi->add_shipment_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**| Id of the shipment to add a tag to | 
 **shipment_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shipment_file**
> delete_shipment_file(shipment_id, file_id)

Delete a file for a shipment.

Deletes an existing shipment file using the specified data.

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
api_instance = Infoplus.ShipmentApi(Infoplus.ApiClient(configuration))
shipment_id = 56 # int | Id of the shipment to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a shipment.
    api_instance.delete_shipment_file(shipment_id, file_id)
except ApiException as e:
    print("Exception when calling ShipmentApi->delete_shipment_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**| Id of the shipment to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shipment_tag**
> delete_shipment_tag(shipment_id, shipment_tag)

Delete a tag for a shipment.

Deletes an existing shipment tag using the specified data.

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
api_instance = Infoplus.ShipmentApi(Infoplus.ApiClient(configuration))
shipment_id = 56 # int | Id of the shipment to remove tag from
shipment_tag = 'shipment_tag_example' # str | The tag to delete

try:
    # Delete a tag for a shipment.
    api_instance.delete_shipment_tag(shipment_id, shipment_tag)
except ApiException as e:
    print("Exception when calling ShipmentApi->delete_shipment_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**| Id of the shipment to remove tag from | 
 **shipment_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_shipment_by_id**
> Shipment get_duplicate_shipment_by_id(shipment_id)

Get a duplicated a shipment by id

Returns a duplicated shipment identified by the specified id.

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
api_instance = Infoplus.ShipmentApi(Infoplus.ApiClient(configuration))
shipment_id = 56 # int | Id of the shipment to be duplicated.

try:
    # Get a duplicated a shipment by id
    api_response = api_instance.get_duplicate_shipment_by_id(shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentApi->get_duplicate_shipment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**| Id of the shipment to be duplicated. | 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment_by_filter**
> list[Shipment] get_shipment_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search shipments by filter

Returns the list of shipments that match the given filter.

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
api_instance = Infoplus.ShipmentApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search shipments by filter
    api_response = api_instance.get_shipment_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentApi->get_shipment_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Shipment]**](Shipment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment_by_id**
> Shipment get_shipment_by_id(shipment_id)

Get a shipment by id

Returns the shipment identified by the specified id.

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
api_instance = Infoplus.ShipmentApi(Infoplus.ApiClient(configuration))
shipment_id = 56 # int | Id of the shipment to be returned.

try:
    # Get a shipment by id
    api_response = api_instance.get_shipment_by_id(shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentApi->get_shipment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**| Id of the shipment to be returned. | 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment_files**
> get_shipment_files(shipment_id)

Get the files for a shipment.

Get all existing shipment files.

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
api_instance = Infoplus.ShipmentApi(Infoplus.ApiClient(configuration))
shipment_id = 56 # int | Id of the shipment to get files for

try:
    # Get the files for a shipment.
    api_instance.get_shipment_files(shipment_id)
except ApiException as e:
    print("Exception when calling ShipmentApi->get_shipment_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**| Id of the shipment to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment_tags**
> get_shipment_tags(shipment_id)

Get the tags for a shipment.

Get all existing shipment tags.

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
api_instance = Infoplus.ShipmentApi(Infoplus.ApiClient(configuration))
shipment_id = 56 # int | Id of the shipment to get tags for

try:
    # Get the tags for a shipment.
    api_instance.get_shipment_tags(shipment_id)
except ApiException as e:
    print("Exception when calling ShipmentApi->get_shipment_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**| Id of the shipment to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipment_custom_fields**
> update_shipment_custom_fields(body)

Update a shipment custom fields

Updates an existing shipment custom fields using the specified data.

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
api_instance = Infoplus.ShipmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.Shipment() # Shipment | Shipment to be updated.

try:
    # Update a shipment custom fields
    api_instance.update_shipment_custom_fields(body)
except ApiException as e:
    print("Exception when calling ShipmentApi->update_shipment_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Shipment**](Shipment.md)| Shipment to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

