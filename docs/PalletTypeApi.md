# Infoplus.PalletTypeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_pallet_type**](PalletTypeApi.md#add_pallet_type) | **POST** /beta/palletType | Create a palletType
[**add_pallet_type_audit**](PalletTypeApi.md#add_pallet_type_audit) | **PUT** /beta/palletType/{palletTypeId}/audit/{palletTypeAudit} | Add new audit for a palletType
[**add_pallet_type_file**](PalletTypeApi.md#add_pallet_type_file) | **POST** /beta/palletType/{palletTypeId}/file/{fileName} | Attach a file to a palletType
[**add_pallet_type_file_by_url**](PalletTypeApi.md#add_pallet_type_file_by_url) | **POST** /beta/palletType/{palletTypeId}/file | Attach a file to a palletType by URL.
[**add_pallet_type_tag**](PalletTypeApi.md#add_pallet_type_tag) | **PUT** /beta/palletType/{palletTypeId}/tag/{palletTypeTag} | Add new tags for a palletType.
[**delete_pallet_type**](PalletTypeApi.md#delete_pallet_type) | **DELETE** /beta/palletType/{palletTypeId} | Delete a palletType
[**delete_pallet_type_file**](PalletTypeApi.md#delete_pallet_type_file) | **DELETE** /beta/palletType/{palletTypeId}/file/{fileId} | Delete a file for a palletType.
[**delete_pallet_type_tag**](PalletTypeApi.md#delete_pallet_type_tag) | **DELETE** /beta/palletType/{palletTypeId}/tag/{palletTypeTag} | Delete a tag for a palletType.
[**get_duplicate_pallet_type_by_id**](PalletTypeApi.md#get_duplicate_pallet_type_by_id) | **GET** /beta/palletType/duplicate/{palletTypeId} | Get a duplicated a palletType by id
[**get_pallet_type_by_filter**](PalletTypeApi.md#get_pallet_type_by_filter) | **GET** /beta/palletType/search | Search palletTypes by filter
[**get_pallet_type_by_id**](PalletTypeApi.md#get_pallet_type_by_id) | **GET** /beta/palletType/{palletTypeId} | Get a palletType by id
[**get_pallet_type_files**](PalletTypeApi.md#get_pallet_type_files) | **GET** /beta/palletType/{palletTypeId}/file | Get the files for a palletType.
[**get_pallet_type_tags**](PalletTypeApi.md#get_pallet_type_tags) | **GET** /beta/palletType/{palletTypeId}/tag | Get the tags for a palletType.
[**update_pallet_type**](PalletTypeApi.md#update_pallet_type) | **PUT** /beta/palletType | Update a palletType
[**update_pallet_type_custom_fields**](PalletTypeApi.md#update_pallet_type_custom_fields) | **PUT** /beta/palletType/customFields | Update a palletType custom fields


# **add_pallet_type**
> PalletType add_pallet_type(body)

Create a palletType

Inserts a new palletType using the specified data.

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
api_instance = Infoplus.PalletTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.PalletType() # PalletType | PalletType to be inserted.

try:
    # Create a palletType
    api_response = api_instance.add_pallet_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PalletTypeApi->add_pallet_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PalletType**](PalletType.md)| PalletType to be inserted. | 

### Return type

[**PalletType**](PalletType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_pallet_type_audit**
> add_pallet_type_audit(pallet_type_id, pallet_type_audit)

Add new audit for a palletType

Adds an audit to an existing palletType.

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
api_instance = Infoplus.PalletTypeApi(Infoplus.ApiClient(configuration))
pallet_type_id = 56 # int | Id of the palletType to add an audit to
pallet_type_audit = 'pallet_type_audit_example' # str | The audit to add

try:
    # Add new audit for a palletType
    api_instance.add_pallet_type_audit(pallet_type_id, pallet_type_audit)
except ApiException as e:
    print("Exception when calling PalletTypeApi->add_pallet_type_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pallet_type_id** | **int**| Id of the palletType to add an audit to | 
 **pallet_type_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_pallet_type_file**
> add_pallet_type_file(pallet_type_id, file_name)

Attach a file to a palletType

Adds a file to an existing palletType.

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
api_instance = Infoplus.PalletTypeApi(Infoplus.ApiClient(configuration))
pallet_type_id = 56 # int | Id of the palletType to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a palletType
    api_instance.add_pallet_type_file(pallet_type_id, file_name)
except ApiException as e:
    print("Exception when calling PalletTypeApi->add_pallet_type_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pallet_type_id** | **int**| Id of the palletType to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_pallet_type_file_by_url**
> add_pallet_type_file_by_url(body, pallet_type_id)

Attach a file to a palletType by URL.

Adds a file to an existing palletType by URL.

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
api_instance = Infoplus.PalletTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
pallet_type_id = 56 # int | Id of the palletType to add an file to

try:
    # Attach a file to a palletType by URL.
    api_instance.add_pallet_type_file_by_url(body, pallet_type_id)
except ApiException as e:
    print("Exception when calling PalletTypeApi->add_pallet_type_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **pallet_type_id** | **int**| Id of the palletType to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_pallet_type_tag**
> add_pallet_type_tag(pallet_type_id, pallet_type_tag)

Add new tags for a palletType.

Adds a tag to an existing palletType.

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
api_instance = Infoplus.PalletTypeApi(Infoplus.ApiClient(configuration))
pallet_type_id = 56 # int | Id of the palletType to add a tag to
pallet_type_tag = 'pallet_type_tag_example' # str | The tag to add

try:
    # Add new tags for a palletType.
    api_instance.add_pallet_type_tag(pallet_type_id, pallet_type_tag)
except ApiException as e:
    print("Exception when calling PalletTypeApi->add_pallet_type_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pallet_type_id** | **int**| Id of the palletType to add a tag to | 
 **pallet_type_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pallet_type**
> delete_pallet_type(pallet_type_id)

Delete a palletType

Deletes the palletType identified by the specified id.

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
api_instance = Infoplus.PalletTypeApi(Infoplus.ApiClient(configuration))
pallet_type_id = 56 # int | Id of the palletType to be deleted.

try:
    # Delete a palletType
    api_instance.delete_pallet_type(pallet_type_id)
except ApiException as e:
    print("Exception when calling PalletTypeApi->delete_pallet_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pallet_type_id** | **int**| Id of the palletType to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pallet_type_file**
> delete_pallet_type_file(pallet_type_id, file_id)

Delete a file for a palletType.

Deletes an existing palletType file using the specified data.

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
api_instance = Infoplus.PalletTypeApi(Infoplus.ApiClient(configuration))
pallet_type_id = 56 # int | Id of the palletType to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a palletType.
    api_instance.delete_pallet_type_file(pallet_type_id, file_id)
except ApiException as e:
    print("Exception when calling PalletTypeApi->delete_pallet_type_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pallet_type_id** | **int**| Id of the palletType to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pallet_type_tag**
> delete_pallet_type_tag(pallet_type_id, pallet_type_tag)

Delete a tag for a palletType.

Deletes an existing palletType tag using the specified data.

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
api_instance = Infoplus.PalletTypeApi(Infoplus.ApiClient(configuration))
pallet_type_id = 56 # int | Id of the palletType to remove tag from
pallet_type_tag = 'pallet_type_tag_example' # str | The tag to delete

try:
    # Delete a tag for a palletType.
    api_instance.delete_pallet_type_tag(pallet_type_id, pallet_type_tag)
except ApiException as e:
    print("Exception when calling PalletTypeApi->delete_pallet_type_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pallet_type_id** | **int**| Id of the palletType to remove tag from | 
 **pallet_type_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_pallet_type_by_id**
> PalletType get_duplicate_pallet_type_by_id(pallet_type_id)

Get a duplicated a palletType by id

Returns a duplicated palletType identified by the specified id.

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
api_instance = Infoplus.PalletTypeApi(Infoplus.ApiClient(configuration))
pallet_type_id = 56 # int | Id of the palletType to be duplicated.

try:
    # Get a duplicated a palletType by id
    api_response = api_instance.get_duplicate_pallet_type_by_id(pallet_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PalletTypeApi->get_duplicate_pallet_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pallet_type_id** | **int**| Id of the palletType to be duplicated. | 

### Return type

[**PalletType**](PalletType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pallet_type_by_filter**
> list[PalletType] get_pallet_type_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search palletTypes by filter

Returns the list of palletTypes that match the given filter.

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
api_instance = Infoplus.PalletTypeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search palletTypes by filter
    api_response = api_instance.get_pallet_type_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PalletTypeApi->get_pallet_type_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[PalletType]**](PalletType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pallet_type_by_id**
> PalletType get_pallet_type_by_id(pallet_type_id)

Get a palletType by id

Returns the palletType identified by the specified id.

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
api_instance = Infoplus.PalletTypeApi(Infoplus.ApiClient(configuration))
pallet_type_id = 56 # int | Id of the palletType to be returned.

try:
    # Get a palletType by id
    api_response = api_instance.get_pallet_type_by_id(pallet_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PalletTypeApi->get_pallet_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pallet_type_id** | **int**| Id of the palletType to be returned. | 

### Return type

[**PalletType**](PalletType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pallet_type_files**
> get_pallet_type_files(pallet_type_id)

Get the files for a palletType.

Get all existing palletType files.

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
api_instance = Infoplus.PalletTypeApi(Infoplus.ApiClient(configuration))
pallet_type_id = 56 # int | Id of the palletType to get files for

try:
    # Get the files for a palletType.
    api_instance.get_pallet_type_files(pallet_type_id)
except ApiException as e:
    print("Exception when calling PalletTypeApi->get_pallet_type_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pallet_type_id** | **int**| Id of the palletType to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pallet_type_tags**
> get_pallet_type_tags(pallet_type_id)

Get the tags for a palletType.

Get all existing palletType tags.

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
api_instance = Infoplus.PalletTypeApi(Infoplus.ApiClient(configuration))
pallet_type_id = 56 # int | Id of the palletType to get tags for

try:
    # Get the tags for a palletType.
    api_instance.get_pallet_type_tags(pallet_type_id)
except ApiException as e:
    print("Exception when calling PalletTypeApi->get_pallet_type_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pallet_type_id** | **int**| Id of the palletType to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pallet_type**
> update_pallet_type(body)

Update a palletType

Updates an existing palletType using the specified data.

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
api_instance = Infoplus.PalletTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.PalletType() # PalletType | PalletType to be updated.

try:
    # Update a palletType
    api_instance.update_pallet_type(body)
except ApiException as e:
    print("Exception when calling PalletTypeApi->update_pallet_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PalletType**](PalletType.md)| PalletType to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pallet_type_custom_fields**
> update_pallet_type_custom_fields(body)

Update a palletType custom fields

Updates an existing palletType custom fields using the specified data.

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
api_instance = Infoplus.PalletTypeApi(Infoplus.ApiClient(configuration))
body = Infoplus.PalletType() # PalletType | PalletType to be updated.

try:
    # Update a palletType custom fields
    api_instance.update_pallet_type_custom_fields(body)
except ApiException as e:
    print("Exception when calling PalletTypeApi->update_pallet_type_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PalletType**](PalletType.md)| PalletType to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

