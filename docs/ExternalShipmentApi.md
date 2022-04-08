# Infoplus.ExternalShipmentApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_external_shipment**](ExternalShipmentApi.md#add_external_shipment) | **POST** /beta/externalShipment | Create an externalShipment
[**add_external_shipment_audit**](ExternalShipmentApi.md#add_external_shipment_audit) | **PUT** /beta/externalShipment/{externalShipmentId}/audit/{externalShipmentAudit} | Add new audit for an externalShipment
[**add_external_shipment_file**](ExternalShipmentApi.md#add_external_shipment_file) | **POST** /beta/externalShipment/{externalShipmentId}/file/{fileName} | Attach a file to an externalShipment
[**add_external_shipment_file_by_url**](ExternalShipmentApi.md#add_external_shipment_file_by_url) | **POST** /beta/externalShipment/{externalShipmentId}/file | Attach a file to an externalShipment by URL.
[**add_external_shipment_tag**](ExternalShipmentApi.md#add_external_shipment_tag) | **PUT** /beta/externalShipment/{externalShipmentId}/tag/{externalShipmentTag} | Add new tags for an externalShipment.
[**delete_external_shipment**](ExternalShipmentApi.md#delete_external_shipment) | **DELETE** /beta/externalShipment/{externalShipmentId} | Delete an externalShipment
[**delete_external_shipment_file**](ExternalShipmentApi.md#delete_external_shipment_file) | **DELETE** /beta/externalShipment/{externalShipmentId}/file/{fileId} | Delete a file for an externalShipment.
[**delete_external_shipment_tag**](ExternalShipmentApi.md#delete_external_shipment_tag) | **DELETE** /beta/externalShipment/{externalShipmentId}/tag/{externalShipmentTag} | Delete a tag for an externalShipment.
[**get_duplicate_external_shipment_by_id**](ExternalShipmentApi.md#get_duplicate_external_shipment_by_id) | **GET** /beta/externalShipment/duplicate/{externalShipmentId} | Get a duplicated an externalShipment by id
[**get_external_shipment_by_filter**](ExternalShipmentApi.md#get_external_shipment_by_filter) | **GET** /beta/externalShipment/search | Search externalShipments by filter
[**get_external_shipment_by_id**](ExternalShipmentApi.md#get_external_shipment_by_id) | **GET** /beta/externalShipment/{externalShipmentId} | Get an externalShipment by id
[**get_external_shipment_files**](ExternalShipmentApi.md#get_external_shipment_files) | **GET** /beta/externalShipment/{externalShipmentId}/file | Get the files for an externalShipment.
[**get_external_shipment_tags**](ExternalShipmentApi.md#get_external_shipment_tags) | **GET** /beta/externalShipment/{externalShipmentId}/tag | Get the tags for an externalShipment.
[**update_external_shipment**](ExternalShipmentApi.md#update_external_shipment) | **PUT** /beta/externalShipment | Update an externalShipment
[**update_external_shipment_custom_fields**](ExternalShipmentApi.md#update_external_shipment_custom_fields) | **PUT** /beta/externalShipment/customFields | Update an externalShipment custom fields


# **add_external_shipment**
> ExternalShipment add_external_shipment(body)

Create an externalShipment

Inserts a new externalShipment using the specified data.

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
api_instance = Infoplus.ExternalShipmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.ExternalShipment() # ExternalShipment | ExternalShipment to be inserted.

try:
    # Create an externalShipment
    api_response = api_instance.add_external_shipment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalShipmentApi->add_external_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalShipment**](ExternalShipment.md)| ExternalShipment to be inserted. | 

### Return type

[**ExternalShipment**](ExternalShipment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_external_shipment_audit**
> add_external_shipment_audit(external_shipment_id, external_shipment_audit)

Add new audit for an externalShipment

Adds an audit to an existing externalShipment.

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
api_instance = Infoplus.ExternalShipmentApi(Infoplus.ApiClient(configuration))
external_shipment_id = 56 # int | Id of the externalShipment to add an audit to
external_shipment_audit = 'external_shipment_audit_example' # str | The audit to add

try:
    # Add new audit for an externalShipment
    api_instance.add_external_shipment_audit(external_shipment_id, external_shipment_audit)
except ApiException as e:
    print("Exception when calling ExternalShipmentApi->add_external_shipment_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipment_id** | **int**| Id of the externalShipment to add an audit to | 
 **external_shipment_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_external_shipment_file**
> add_external_shipment_file(external_shipment_id, file_name)

Attach a file to an externalShipment

Adds a file to an existing externalShipment.

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
api_instance = Infoplus.ExternalShipmentApi(Infoplus.ApiClient(configuration))
external_shipment_id = 56 # int | Id of the externalShipment to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an externalShipment
    api_instance.add_external_shipment_file(external_shipment_id, file_name)
except ApiException as e:
    print("Exception when calling ExternalShipmentApi->add_external_shipment_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipment_id** | **int**| Id of the externalShipment to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_external_shipment_file_by_url**
> add_external_shipment_file_by_url(body, external_shipment_id)

Attach a file to an externalShipment by URL.

Adds a file to an existing externalShipment by URL.

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
api_instance = Infoplus.ExternalShipmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
external_shipment_id = 56 # int | Id of the externalShipment to add an file to

try:
    # Attach a file to an externalShipment by URL.
    api_instance.add_external_shipment_file_by_url(body, external_shipment_id)
except ApiException as e:
    print("Exception when calling ExternalShipmentApi->add_external_shipment_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **external_shipment_id** | **int**| Id of the externalShipment to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_external_shipment_tag**
> add_external_shipment_tag(external_shipment_id, external_shipment_tag)

Add new tags for an externalShipment.

Adds a tag to an existing externalShipment.

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
api_instance = Infoplus.ExternalShipmentApi(Infoplus.ApiClient(configuration))
external_shipment_id = 56 # int | Id of the externalShipment to add a tag to
external_shipment_tag = 'external_shipment_tag_example' # str | The tag to add

try:
    # Add new tags for an externalShipment.
    api_instance.add_external_shipment_tag(external_shipment_id, external_shipment_tag)
except ApiException as e:
    print("Exception when calling ExternalShipmentApi->add_external_shipment_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipment_id** | **int**| Id of the externalShipment to add a tag to | 
 **external_shipment_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_shipment**
> delete_external_shipment(external_shipment_id)

Delete an externalShipment

Deletes the externalShipment identified by the specified id.

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
api_instance = Infoplus.ExternalShipmentApi(Infoplus.ApiClient(configuration))
external_shipment_id = 56 # int | Id of the externalShipment to be deleted.

try:
    # Delete an externalShipment
    api_instance.delete_external_shipment(external_shipment_id)
except ApiException as e:
    print("Exception when calling ExternalShipmentApi->delete_external_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipment_id** | **int**| Id of the externalShipment to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_shipment_file**
> delete_external_shipment_file(external_shipment_id, file_id)

Delete a file for an externalShipment.

Deletes an existing externalShipment file using the specified data.

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
api_instance = Infoplus.ExternalShipmentApi(Infoplus.ApiClient(configuration))
external_shipment_id = 56 # int | Id of the externalShipment to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an externalShipment.
    api_instance.delete_external_shipment_file(external_shipment_id, file_id)
except ApiException as e:
    print("Exception when calling ExternalShipmentApi->delete_external_shipment_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipment_id** | **int**| Id of the externalShipment to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_shipment_tag**
> delete_external_shipment_tag(external_shipment_id, external_shipment_tag)

Delete a tag for an externalShipment.

Deletes an existing externalShipment tag using the specified data.

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
api_instance = Infoplus.ExternalShipmentApi(Infoplus.ApiClient(configuration))
external_shipment_id = 56 # int | Id of the externalShipment to remove tag from
external_shipment_tag = 'external_shipment_tag_example' # str | The tag to delete

try:
    # Delete a tag for an externalShipment.
    api_instance.delete_external_shipment_tag(external_shipment_id, external_shipment_tag)
except ApiException as e:
    print("Exception when calling ExternalShipmentApi->delete_external_shipment_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipment_id** | **int**| Id of the externalShipment to remove tag from | 
 **external_shipment_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_external_shipment_by_id**
> ExternalShipment get_duplicate_external_shipment_by_id(external_shipment_id)

Get a duplicated an externalShipment by id

Returns a duplicated externalShipment identified by the specified id.

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
api_instance = Infoplus.ExternalShipmentApi(Infoplus.ApiClient(configuration))
external_shipment_id = 56 # int | Id of the externalShipment to be duplicated.

try:
    # Get a duplicated an externalShipment by id
    api_response = api_instance.get_duplicate_external_shipment_by_id(external_shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalShipmentApi->get_duplicate_external_shipment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipment_id** | **int**| Id of the externalShipment to be duplicated. | 

### Return type

[**ExternalShipment**](ExternalShipment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_shipment_by_filter**
> list[ExternalShipment] get_external_shipment_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search externalShipments by filter

Returns the list of externalShipments that match the given filter.

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
api_instance = Infoplus.ExternalShipmentApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search externalShipments by filter
    api_response = api_instance.get_external_shipment_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalShipmentApi->get_external_shipment_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ExternalShipment]**](ExternalShipment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_shipment_by_id**
> ExternalShipment get_external_shipment_by_id(external_shipment_id)

Get an externalShipment by id

Returns the externalShipment identified by the specified id.

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
api_instance = Infoplus.ExternalShipmentApi(Infoplus.ApiClient(configuration))
external_shipment_id = 56 # int | Id of the externalShipment to be returned.

try:
    # Get an externalShipment by id
    api_response = api_instance.get_external_shipment_by_id(external_shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalShipmentApi->get_external_shipment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipment_id** | **int**| Id of the externalShipment to be returned. | 

### Return type

[**ExternalShipment**](ExternalShipment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_shipment_files**
> get_external_shipment_files(external_shipment_id)

Get the files for an externalShipment.

Get all existing externalShipment files.

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
api_instance = Infoplus.ExternalShipmentApi(Infoplus.ApiClient(configuration))
external_shipment_id = 56 # int | Id of the externalShipment to get files for

try:
    # Get the files for an externalShipment.
    api_instance.get_external_shipment_files(external_shipment_id)
except ApiException as e:
    print("Exception when calling ExternalShipmentApi->get_external_shipment_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipment_id** | **int**| Id of the externalShipment to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_shipment_tags**
> get_external_shipment_tags(external_shipment_id)

Get the tags for an externalShipment.

Get all existing externalShipment tags.

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
api_instance = Infoplus.ExternalShipmentApi(Infoplus.ApiClient(configuration))
external_shipment_id = 56 # int | Id of the externalShipment to get tags for

try:
    # Get the tags for an externalShipment.
    api_instance.get_external_shipment_tags(external_shipment_id)
except ApiException as e:
    print("Exception when calling ExternalShipmentApi->get_external_shipment_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_shipment_id** | **int**| Id of the externalShipment to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_shipment**
> update_external_shipment(body)

Update an externalShipment

Updates an existing externalShipment using the specified data.

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
api_instance = Infoplus.ExternalShipmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.ExternalShipment() # ExternalShipment | ExternalShipment to be updated.

try:
    # Update an externalShipment
    api_instance.update_external_shipment(body)
except ApiException as e:
    print("Exception when calling ExternalShipmentApi->update_external_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalShipment**](ExternalShipment.md)| ExternalShipment to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_shipment_custom_fields**
> update_external_shipment_custom_fields(body)

Update an externalShipment custom fields

Updates an existing externalShipment custom fields using the specified data.

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
api_instance = Infoplus.ExternalShipmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.ExternalShipment() # ExternalShipment | ExternalShipment to be updated.

try:
    # Update an externalShipment custom fields
    api_instance.update_external_shipment_custom_fields(body)
except ApiException as e:
    print("Exception when calling ExternalShipmentApi->update_external_shipment_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalShipment**](ExternalShipment.md)| ExternalShipment to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

