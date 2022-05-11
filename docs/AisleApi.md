# Infoplus.AisleApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_aisle**](AisleApi.md#add_aisle) | **POST** /v3.0/aisle | Create an aisle
[**add_aisle_audit**](AisleApi.md#add_aisle_audit) | **PUT** /v3.0/aisle/{aisleId}/audit/{aisleAudit} | Add new audit for an aisle
[**add_aisle_file**](AisleApi.md#add_aisle_file) | **POST** /v3.0/aisle/{aisleId}/file/{fileName} | Attach a file to an aisle
[**add_aisle_file_by_url**](AisleApi.md#add_aisle_file_by_url) | **POST** /v3.0/aisle/{aisleId}/file | Attach a file to an aisle by URL.
[**add_aisle_tag**](AisleApi.md#add_aisle_tag) | **PUT** /v3.0/aisle/{aisleId}/tag/{aisleTag} | Add new tags for an aisle.
[**delete_aisle**](AisleApi.md#delete_aisle) | **DELETE** /v3.0/aisle/{aisleId} | Delete an aisle
[**delete_aisle_file**](AisleApi.md#delete_aisle_file) | **DELETE** /v3.0/aisle/{aisleId}/file/{fileId} | Delete a file for an aisle.
[**delete_aisle_tag**](AisleApi.md#delete_aisle_tag) | **DELETE** /v3.0/aisle/{aisleId}/tag/{aisleTag} | Delete a tag for an aisle.
[**get_aisle_by_filter**](AisleApi.md#get_aisle_by_filter) | **GET** /v3.0/aisle/search | Search aisles by filter
[**get_aisle_by_id**](AisleApi.md#get_aisle_by_id) | **GET** /v3.0/aisle/{aisleId} | Get an aisle by id
[**get_aisle_files**](AisleApi.md#get_aisle_files) | **GET** /v3.0/aisle/{aisleId}/file | Get the files for an aisle.
[**get_aisle_tags**](AisleApi.md#get_aisle_tags) | **GET** /v3.0/aisle/{aisleId}/tag | Get the tags for an aisle.
[**get_duplicate_aisle_by_id**](AisleApi.md#get_duplicate_aisle_by_id) | **GET** /v3.0/aisle/duplicate/{aisleId} | Get a duplicated an aisle by id
[**update_aisle**](AisleApi.md#update_aisle) | **PUT** /v3.0/aisle | Update an aisle
[**update_aisle_custom_fields**](AisleApi.md#update_aisle_custom_fields) | **PUT** /v3.0/aisle/customFields | Update an aisle custom fields


# **add_aisle**
> Aisle add_aisle(body)

Create an aisle

Inserts a new aisle using the specified data.

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
api_instance = Infoplus.AisleApi(Infoplus.ApiClient(configuration))
body = Infoplus.Aisle() # Aisle | Aisle to be inserted.

try:
    # Create an aisle
    api_response = api_instance.add_aisle(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AisleApi->add_aisle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Aisle**](Aisle.md)| Aisle to be inserted. | 

### Return type

[**Aisle**](Aisle.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_aisle_audit**
> add_aisle_audit(aisle_id, aisle_audit)

Add new audit for an aisle

Adds an audit to an existing aisle.

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
api_instance = Infoplus.AisleApi(Infoplus.ApiClient(configuration))
aisle_id = 56 # int | Id of the aisle to add an audit to
aisle_audit = 'aisle_audit_example' # str | The audit to add

try:
    # Add new audit for an aisle
    api_instance.add_aisle_audit(aisle_id, aisle_audit)
except ApiException as e:
    print("Exception when calling AisleApi->add_aisle_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aisle_id** | **int**| Id of the aisle to add an audit to | 
 **aisle_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_aisle_file**
> add_aisle_file(aisle_id, file_name)

Attach a file to an aisle

Adds a file to an existing aisle.

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
api_instance = Infoplus.AisleApi(Infoplus.ApiClient(configuration))
aisle_id = 56 # int | Id of the aisle to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an aisle
    api_instance.add_aisle_file(aisle_id, file_name)
except ApiException as e:
    print("Exception when calling AisleApi->add_aisle_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aisle_id** | **int**| Id of the aisle to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_aisle_file_by_url**
> add_aisle_file_by_url(body, aisle_id)

Attach a file to an aisle by URL.

Adds a file to an existing aisle by URL.

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
api_instance = Infoplus.AisleApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
aisle_id = 56 # int | Id of the aisle to add an file to

try:
    # Attach a file to an aisle by URL.
    api_instance.add_aisle_file_by_url(body, aisle_id)
except ApiException as e:
    print("Exception when calling AisleApi->add_aisle_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **aisle_id** | **int**| Id of the aisle to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_aisle_tag**
> add_aisle_tag(aisle_id, aisle_tag)

Add new tags for an aisle.

Adds a tag to an existing aisle.

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
api_instance = Infoplus.AisleApi(Infoplus.ApiClient(configuration))
aisle_id = 56 # int | Id of the aisle to add a tag to
aisle_tag = 'aisle_tag_example' # str | The tag to add

try:
    # Add new tags for an aisle.
    api_instance.add_aisle_tag(aisle_id, aisle_tag)
except ApiException as e:
    print("Exception when calling AisleApi->add_aisle_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aisle_id** | **int**| Id of the aisle to add a tag to | 
 **aisle_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_aisle**
> delete_aisle(aisle_id)

Delete an aisle

Deletes the aisle identified by the specified id.

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
api_instance = Infoplus.AisleApi(Infoplus.ApiClient(configuration))
aisle_id = 56 # int | Id of the aisle to be deleted.

try:
    # Delete an aisle
    api_instance.delete_aisle(aisle_id)
except ApiException as e:
    print("Exception when calling AisleApi->delete_aisle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aisle_id** | **int**| Id of the aisle to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_aisle_file**
> delete_aisle_file(aisle_id, file_id)

Delete a file for an aisle.

Deletes an existing aisle file using the specified data.

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
api_instance = Infoplus.AisleApi(Infoplus.ApiClient(configuration))
aisle_id = 56 # int | Id of the aisle to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an aisle.
    api_instance.delete_aisle_file(aisle_id, file_id)
except ApiException as e:
    print("Exception when calling AisleApi->delete_aisle_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aisle_id** | **int**| Id of the aisle to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_aisle_tag**
> delete_aisle_tag(aisle_id, aisle_tag)

Delete a tag for an aisle.

Deletes an existing aisle tag using the specified data.

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
api_instance = Infoplus.AisleApi(Infoplus.ApiClient(configuration))
aisle_id = 56 # int | Id of the aisle to remove tag from
aisle_tag = 'aisle_tag_example' # str | The tag to delete

try:
    # Delete a tag for an aisle.
    api_instance.delete_aisle_tag(aisle_id, aisle_tag)
except ApiException as e:
    print("Exception when calling AisleApi->delete_aisle_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aisle_id** | **int**| Id of the aisle to remove tag from | 
 **aisle_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aisle_by_filter**
> list[Aisle] get_aisle_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search aisles by filter

Returns the list of aisles that match the given filter.

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
api_instance = Infoplus.AisleApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search aisles by filter
    api_response = api_instance.get_aisle_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AisleApi->get_aisle_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Aisle]**](Aisle.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aisle_by_id**
> Aisle get_aisle_by_id(aisle_id)

Get an aisle by id

Returns the aisle identified by the specified id.

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
api_instance = Infoplus.AisleApi(Infoplus.ApiClient(configuration))
aisle_id = 56 # int | Id of the aisle to be returned.

try:
    # Get an aisle by id
    api_response = api_instance.get_aisle_by_id(aisle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AisleApi->get_aisle_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aisle_id** | **int**| Id of the aisle to be returned. | 

### Return type

[**Aisle**](Aisle.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aisle_files**
> get_aisle_files(aisle_id)

Get the files for an aisle.

Get all existing aisle files.

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
api_instance = Infoplus.AisleApi(Infoplus.ApiClient(configuration))
aisle_id = 56 # int | Id of the aisle to get files for

try:
    # Get the files for an aisle.
    api_instance.get_aisle_files(aisle_id)
except ApiException as e:
    print("Exception when calling AisleApi->get_aisle_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aisle_id** | **int**| Id of the aisle to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aisle_tags**
> get_aisle_tags(aisle_id)

Get the tags for an aisle.

Get all existing aisle tags.

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
api_instance = Infoplus.AisleApi(Infoplus.ApiClient(configuration))
aisle_id = 56 # int | Id of the aisle to get tags for

try:
    # Get the tags for an aisle.
    api_instance.get_aisle_tags(aisle_id)
except ApiException as e:
    print("Exception when calling AisleApi->get_aisle_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aisle_id** | **int**| Id of the aisle to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_aisle_by_id**
> Aisle get_duplicate_aisle_by_id(aisle_id)

Get a duplicated an aisle by id

Returns a duplicated aisle identified by the specified id.

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
api_instance = Infoplus.AisleApi(Infoplus.ApiClient(configuration))
aisle_id = 56 # int | Id of the aisle to be duplicated.

try:
    # Get a duplicated an aisle by id
    api_response = api_instance.get_duplicate_aisle_by_id(aisle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AisleApi->get_duplicate_aisle_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aisle_id** | **int**| Id of the aisle to be duplicated. | 

### Return type

[**Aisle**](Aisle.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_aisle**
> update_aisle(body)

Update an aisle

Updates an existing aisle using the specified data.

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
api_instance = Infoplus.AisleApi(Infoplus.ApiClient(configuration))
body = Infoplus.Aisle() # Aisle | Aisle to be updated.

try:
    # Update an aisle
    api_instance.update_aisle(body)
except ApiException as e:
    print("Exception when calling AisleApi->update_aisle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Aisle**](Aisle.md)| Aisle to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_aisle_custom_fields**
> update_aisle_custom_fields(body)

Update an aisle custom fields

Updates an existing aisle custom fields using the specified data.

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
api_instance = Infoplus.AisleApi(Infoplus.ApiClient(configuration))
body = Infoplus.Aisle() # Aisle | Aisle to be updated.

try:
    # Update an aisle custom fields
    api_instance.update_aisle_custom_fields(body)
except ApiException as e:
    print("Exception when calling AisleApi->update_aisle_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Aisle**](Aisle.md)| Aisle to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

