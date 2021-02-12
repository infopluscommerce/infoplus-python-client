# Infoplus.KitApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_kit**](KitApi.md#add_kit) | **POST** /beta/kit | Create a kit
[**add_kit_audit**](KitApi.md#add_kit_audit) | **PUT** /beta/kit/{kitId}/audit/{kitAudit} | Add new audit for a kit
[**add_kit_file**](KitApi.md#add_kit_file) | **POST** /beta/kit/{kitId}/file/{fileName} | Attach a file to a kit
[**add_kit_file_by_url**](KitApi.md#add_kit_file_by_url) | **POST** /beta/kit/{kitId}/file | Attach a file to a kit by URL.
[**add_kit_tag**](KitApi.md#add_kit_tag) | **PUT** /beta/kit/{kitId}/tag/{kitTag} | Add new tags for a kit.
[**delete_kit**](KitApi.md#delete_kit) | **DELETE** /beta/kit/{kitId} | Delete a kit
[**delete_kit_file**](KitApi.md#delete_kit_file) | **DELETE** /beta/kit/{kitId}/file/{fileId} | Delete a file for a kit.
[**delete_kit_tag**](KitApi.md#delete_kit_tag) | **DELETE** /beta/kit/{kitId}/tag/{kitTag} | Delete a tag for a kit.
[**get_duplicate_kit_by_id**](KitApi.md#get_duplicate_kit_by_id) | **GET** /beta/kit/duplicate/{kitId} | Get a duplicated a kit by id
[**get_kit_by_filter**](KitApi.md#get_kit_by_filter) | **GET** /beta/kit/search | Search kits by filter
[**get_kit_by_id**](KitApi.md#get_kit_by_id) | **GET** /beta/kit/{kitId} | Get a kit by id
[**get_kit_files**](KitApi.md#get_kit_files) | **GET** /beta/kit/{kitId}/file | Get the files for a kit.
[**get_kit_tags**](KitApi.md#get_kit_tags) | **GET** /beta/kit/{kitId}/tag | Get the tags for a kit.
[**update_kit**](KitApi.md#update_kit) | **PUT** /beta/kit | Update a kit
[**update_kit_custom_fields**](KitApi.md#update_kit_custom_fields) | **PUT** /beta/kit/customFields | Update a kit custom fields


# **add_kit**
> Kit add_kit(body)

Create a kit

Inserts a new kit using the specified data.

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
api_instance = Infoplus.KitApi(Infoplus.ApiClient(configuration))
body = Infoplus.Kit() # Kit | Kit to be inserted.

try:
    # Create a kit
    api_response = api_instance.add_kit(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KitApi->add_kit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Kit**](Kit.md)| Kit to be inserted. | 

### Return type

[**Kit**](Kit.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_kit_audit**
> add_kit_audit(kit_id, kit_audit)

Add new audit for a kit

Adds an audit to an existing kit.

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
api_instance = Infoplus.KitApi(Infoplus.ApiClient(configuration))
kit_id = 56 # int | Id of the kit to add an audit to
kit_audit = 'kit_audit_example' # str | The audit to add

try:
    # Add new audit for a kit
    api_instance.add_kit_audit(kit_id, kit_audit)
except ApiException as e:
    print("Exception when calling KitApi->add_kit_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kit_id** | **int**| Id of the kit to add an audit to | 
 **kit_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_kit_file**
> add_kit_file(kit_id, file_name)

Attach a file to a kit

Adds a file to an existing kit.

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
api_instance = Infoplus.KitApi(Infoplus.ApiClient(configuration))
kit_id = 56 # int | Id of the kit to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a kit
    api_instance.add_kit_file(kit_id, file_name)
except ApiException as e:
    print("Exception when calling KitApi->add_kit_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kit_id** | **int**| Id of the kit to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_kit_file_by_url**
> add_kit_file_by_url(body, kit_id)

Attach a file to a kit by URL.

Adds a file to an existing kit by URL.

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
api_instance = Infoplus.KitApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
kit_id = 56 # int | Id of the kit to add an file to

try:
    # Attach a file to a kit by URL.
    api_instance.add_kit_file_by_url(body, kit_id)
except ApiException as e:
    print("Exception when calling KitApi->add_kit_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **kit_id** | **int**| Id of the kit to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_kit_tag**
> add_kit_tag(kit_id, kit_tag)

Add new tags for a kit.

Adds a tag to an existing kit.

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
api_instance = Infoplus.KitApi(Infoplus.ApiClient(configuration))
kit_id = 56 # int | Id of the kit to add a tag to
kit_tag = 'kit_tag_example' # str | The tag to add

try:
    # Add new tags for a kit.
    api_instance.add_kit_tag(kit_id, kit_tag)
except ApiException as e:
    print("Exception when calling KitApi->add_kit_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kit_id** | **int**| Id of the kit to add a tag to | 
 **kit_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kit**
> delete_kit(kit_id)

Delete a kit

Deletes the kit identified by the specified id.

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
api_instance = Infoplus.KitApi(Infoplus.ApiClient(configuration))
kit_id = 56 # int | Id of the kit to be deleted.

try:
    # Delete a kit
    api_instance.delete_kit(kit_id)
except ApiException as e:
    print("Exception when calling KitApi->delete_kit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kit_id** | **int**| Id of the kit to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kit_file**
> delete_kit_file(kit_id, file_id)

Delete a file for a kit.

Deletes an existing kit file using the specified data.

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
api_instance = Infoplus.KitApi(Infoplus.ApiClient(configuration))
kit_id = 56 # int | Id of the kit to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a kit.
    api_instance.delete_kit_file(kit_id, file_id)
except ApiException as e:
    print("Exception when calling KitApi->delete_kit_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kit_id** | **int**| Id of the kit to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kit_tag**
> delete_kit_tag(kit_id, kit_tag)

Delete a tag for a kit.

Deletes an existing kit tag using the specified data.

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
api_instance = Infoplus.KitApi(Infoplus.ApiClient(configuration))
kit_id = 56 # int | Id of the kit to remove tag from
kit_tag = 'kit_tag_example' # str | The tag to delete

try:
    # Delete a tag for a kit.
    api_instance.delete_kit_tag(kit_id, kit_tag)
except ApiException as e:
    print("Exception when calling KitApi->delete_kit_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kit_id** | **int**| Id of the kit to remove tag from | 
 **kit_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_kit_by_id**
> Kit get_duplicate_kit_by_id(kit_id)

Get a duplicated a kit by id

Returns a duplicated kit identified by the specified id.

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
api_instance = Infoplus.KitApi(Infoplus.ApiClient(configuration))
kit_id = 56 # int | Id of the kit to be duplicated.

try:
    # Get a duplicated a kit by id
    api_response = api_instance.get_duplicate_kit_by_id(kit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KitApi->get_duplicate_kit_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kit_id** | **int**| Id of the kit to be duplicated. | 

### Return type

[**Kit**](Kit.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kit_by_filter**
> list[Kit] get_kit_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search kits by filter

Returns the list of kits that match the given filter.

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
api_instance = Infoplus.KitApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search kits by filter
    api_response = api_instance.get_kit_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KitApi->get_kit_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Kit]**](Kit.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kit_by_id**
> Kit get_kit_by_id(kit_id)

Get a kit by id

Returns the kit identified by the specified id.

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
api_instance = Infoplus.KitApi(Infoplus.ApiClient(configuration))
kit_id = 56 # int | Id of the kit to be returned.

try:
    # Get a kit by id
    api_response = api_instance.get_kit_by_id(kit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KitApi->get_kit_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kit_id** | **int**| Id of the kit to be returned. | 

### Return type

[**Kit**](Kit.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kit_files**
> get_kit_files(kit_id)

Get the files for a kit.

Get all existing kit files.

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
api_instance = Infoplus.KitApi(Infoplus.ApiClient(configuration))
kit_id = 56 # int | Id of the kit to get files for

try:
    # Get the files for a kit.
    api_instance.get_kit_files(kit_id)
except ApiException as e:
    print("Exception when calling KitApi->get_kit_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kit_id** | **int**| Id of the kit to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kit_tags**
> get_kit_tags(kit_id)

Get the tags for a kit.

Get all existing kit tags.

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
api_instance = Infoplus.KitApi(Infoplus.ApiClient(configuration))
kit_id = 56 # int | Id of the kit to get tags for

try:
    # Get the tags for a kit.
    api_instance.get_kit_tags(kit_id)
except ApiException as e:
    print("Exception when calling KitApi->get_kit_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kit_id** | **int**| Id of the kit to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kit**
> update_kit(body)

Update a kit

Updates an existing kit using the specified data.

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
api_instance = Infoplus.KitApi(Infoplus.ApiClient(configuration))
body = Infoplus.Kit() # Kit | Kit to be updated.

try:
    # Update a kit
    api_instance.update_kit(body)
except ApiException as e:
    print("Exception when calling KitApi->update_kit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Kit**](Kit.md)| Kit to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kit_custom_fields**
> update_kit_custom_fields(body)

Update a kit custom fields

Updates an existing kit custom fields using the specified data.

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
api_instance = Infoplus.KitApi(Infoplus.ApiClient(configuration))
body = Infoplus.Kit() # Kit | Kit to be updated.

try:
    # Update a kit custom fields
    api_instance.update_kit_custom_fields(body)
except ApiException as e:
    print("Exception when calling KitApi->update_kit_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Kit**](Kit.md)| Kit to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

