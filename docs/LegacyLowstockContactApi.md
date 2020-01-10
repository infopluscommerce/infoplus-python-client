# Infoplus.LegacyLowstockContactApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_legacy_lowstock_contact**](LegacyLowstockContactApi.md#add_legacy_lowstock_contact) | **POST** /beta/legacyLowstockContact | Create a legacyLowstockContact
[**add_legacy_lowstock_contact_audit**](LegacyLowstockContactApi.md#add_legacy_lowstock_contact_audit) | **PUT** /beta/legacyLowstockContact/{legacyLowstockContactId}/audit/{legacyLowstockContactAudit} | Add new audit for a legacyLowstockContact
[**add_legacy_lowstock_contact_file**](LegacyLowstockContactApi.md#add_legacy_lowstock_contact_file) | **POST** /beta/legacyLowstockContact/{legacyLowstockContactId}/file/{fileName} | Attach a file to a legacyLowstockContact
[**add_legacy_lowstock_contact_tag**](LegacyLowstockContactApi.md#add_legacy_lowstock_contact_tag) | **PUT** /beta/legacyLowstockContact/{legacyLowstockContactId}/tag/{legacyLowstockContactTag} | Add new tags for a legacyLowstockContact.
[**delete_legacy_lowstock_contact**](LegacyLowstockContactApi.md#delete_legacy_lowstock_contact) | **DELETE** /beta/legacyLowstockContact/{legacyLowstockContactId} | Delete a legacyLowstockContact
[**delete_legacy_lowstock_contact_tag**](LegacyLowstockContactApi.md#delete_legacy_lowstock_contact_tag) | **DELETE** /beta/legacyLowstockContact/{legacyLowstockContactId}/tag/{legacyLowstockContactTag} | Delete a tag for a legacyLowstockContact.
[**get_duplicate_legacy_lowstock_contact_by_id**](LegacyLowstockContactApi.md#get_duplicate_legacy_lowstock_contact_by_id) | **GET** /beta/legacyLowstockContact/duplicate/{legacyLowstockContactId} | Get a duplicated a legacyLowstockContact by id
[**get_legacy_lowstock_contact_by_filter**](LegacyLowstockContactApi.md#get_legacy_lowstock_contact_by_filter) | **GET** /beta/legacyLowstockContact/search | Search legacyLowstockContacts by filter
[**get_legacy_lowstock_contact_by_id**](LegacyLowstockContactApi.md#get_legacy_lowstock_contact_by_id) | **GET** /beta/legacyLowstockContact/{legacyLowstockContactId} | Get a legacyLowstockContact by id
[**get_legacy_lowstock_contact_tags**](LegacyLowstockContactApi.md#get_legacy_lowstock_contact_tags) | **GET** /beta/legacyLowstockContact/{legacyLowstockContactId}/tag | Get the tags for a legacyLowstockContact.
[**update_legacy_lowstock_contact**](LegacyLowstockContactApi.md#update_legacy_lowstock_contact) | **PUT** /beta/legacyLowstockContact | Update a legacyLowstockContact


# **add_legacy_lowstock_contact**
> LegacyLowstockContact add_legacy_lowstock_contact(body)

Create a legacyLowstockContact

Inserts a new legacyLowstockContact using the specified data.

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
api_instance = Infoplus.LegacyLowstockContactApi(Infoplus.ApiClient(configuration))
body = Infoplus.LegacyLowstockContact() # LegacyLowstockContact | LegacyLowstockContact to be inserted.

try:
    # Create a legacyLowstockContact
    api_response = api_instance.add_legacy_lowstock_contact(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyLowstockContactApi->add_legacy_lowstock_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LegacyLowstockContact**](LegacyLowstockContact.md)| LegacyLowstockContact to be inserted. | 

### Return type

[**LegacyLowstockContact**](LegacyLowstockContact.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_legacy_lowstock_contact_audit**
> add_legacy_lowstock_contact_audit(legacy_lowstock_contact_id, legacy_lowstock_contact_audit)

Add new audit for a legacyLowstockContact

Adds an audit to an existing legacyLowstockContact.

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
api_instance = Infoplus.LegacyLowstockContactApi(Infoplus.ApiClient(configuration))
legacy_lowstock_contact_id = 56 # int | Id of the legacyLowstockContact to add an audit to
legacy_lowstock_contact_audit = 'legacy_lowstock_contact_audit_example' # str | The audit to add

try:
    # Add new audit for a legacyLowstockContact
    api_instance.add_legacy_lowstock_contact_audit(legacy_lowstock_contact_id, legacy_lowstock_contact_audit)
except ApiException as e:
    print("Exception when calling LegacyLowstockContactApi->add_legacy_lowstock_contact_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legacy_lowstock_contact_id** | **int**| Id of the legacyLowstockContact to add an audit to | 
 **legacy_lowstock_contact_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_legacy_lowstock_contact_file**
> add_legacy_lowstock_contact_file(legacy_lowstock_contact_id, file_name)

Attach a file to a legacyLowstockContact

Adds a file to an existing legacyLowstockContact.

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
api_instance = Infoplus.LegacyLowstockContactApi(Infoplus.ApiClient(configuration))
legacy_lowstock_contact_id = 56 # int | Id of the legacyLowstockContact to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a legacyLowstockContact
    api_instance.add_legacy_lowstock_contact_file(legacy_lowstock_contact_id, file_name)
except ApiException as e:
    print("Exception when calling LegacyLowstockContactApi->add_legacy_lowstock_contact_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legacy_lowstock_contact_id** | **int**| Id of the legacyLowstockContact to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_legacy_lowstock_contact_tag**
> add_legacy_lowstock_contact_tag(legacy_lowstock_contact_id, legacy_lowstock_contact_tag)

Add new tags for a legacyLowstockContact.

Adds a tag to an existing legacyLowstockContact.

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
api_instance = Infoplus.LegacyLowstockContactApi(Infoplus.ApiClient(configuration))
legacy_lowstock_contact_id = 56 # int | Id of the legacyLowstockContact to add a tag to
legacy_lowstock_contact_tag = 'legacy_lowstock_contact_tag_example' # str | The tag to add

try:
    # Add new tags for a legacyLowstockContact.
    api_instance.add_legacy_lowstock_contact_tag(legacy_lowstock_contact_id, legacy_lowstock_contact_tag)
except ApiException as e:
    print("Exception when calling LegacyLowstockContactApi->add_legacy_lowstock_contact_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legacy_lowstock_contact_id** | **int**| Id of the legacyLowstockContact to add a tag to | 
 **legacy_lowstock_contact_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_legacy_lowstock_contact**
> delete_legacy_lowstock_contact(legacy_lowstock_contact_id)

Delete a legacyLowstockContact

Deletes the legacyLowstockContact identified by the specified id.

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
api_instance = Infoplus.LegacyLowstockContactApi(Infoplus.ApiClient(configuration))
legacy_lowstock_contact_id = 56 # int | Id of the legacyLowstockContact to be deleted.

try:
    # Delete a legacyLowstockContact
    api_instance.delete_legacy_lowstock_contact(legacy_lowstock_contact_id)
except ApiException as e:
    print("Exception when calling LegacyLowstockContactApi->delete_legacy_lowstock_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legacy_lowstock_contact_id** | **int**| Id of the legacyLowstockContact to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_legacy_lowstock_contact_tag**
> delete_legacy_lowstock_contact_tag(legacy_lowstock_contact_id, legacy_lowstock_contact_tag)

Delete a tag for a legacyLowstockContact.

Deletes an existing legacyLowstockContact tag using the specified data.

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
api_instance = Infoplus.LegacyLowstockContactApi(Infoplus.ApiClient(configuration))
legacy_lowstock_contact_id = 56 # int | Id of the legacyLowstockContact to remove tag from
legacy_lowstock_contact_tag = 'legacy_lowstock_contact_tag_example' # str | The tag to delete

try:
    # Delete a tag for a legacyLowstockContact.
    api_instance.delete_legacy_lowstock_contact_tag(legacy_lowstock_contact_id, legacy_lowstock_contact_tag)
except ApiException as e:
    print("Exception when calling LegacyLowstockContactApi->delete_legacy_lowstock_contact_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legacy_lowstock_contact_id** | **int**| Id of the legacyLowstockContact to remove tag from | 
 **legacy_lowstock_contact_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_legacy_lowstock_contact_by_id**
> LegacyLowstockContact get_duplicate_legacy_lowstock_contact_by_id(legacy_lowstock_contact_id)

Get a duplicated a legacyLowstockContact by id

Returns a duplicated legacyLowstockContact identified by the specified id.

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
api_instance = Infoplus.LegacyLowstockContactApi(Infoplus.ApiClient(configuration))
legacy_lowstock_contact_id = 56 # int | Id of the legacyLowstockContact to be duplicated.

try:
    # Get a duplicated a legacyLowstockContact by id
    api_response = api_instance.get_duplicate_legacy_lowstock_contact_by_id(legacy_lowstock_contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyLowstockContactApi->get_duplicate_legacy_lowstock_contact_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legacy_lowstock_contact_id** | **int**| Id of the legacyLowstockContact to be duplicated. | 

### Return type

[**LegacyLowstockContact**](LegacyLowstockContact.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legacy_lowstock_contact_by_filter**
> list[LegacyLowstockContact] get_legacy_lowstock_contact_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search legacyLowstockContacts by filter

Returns the list of legacyLowstockContacts that match the given filter.

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
api_instance = Infoplus.LegacyLowstockContactApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search legacyLowstockContacts by filter
    api_response = api_instance.get_legacy_lowstock_contact_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyLowstockContactApi->get_legacy_lowstock_contact_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[LegacyLowstockContact]**](LegacyLowstockContact.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legacy_lowstock_contact_by_id**
> LegacyLowstockContact get_legacy_lowstock_contact_by_id(legacy_lowstock_contact_id)

Get a legacyLowstockContact by id

Returns the legacyLowstockContact identified by the specified id.

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
api_instance = Infoplus.LegacyLowstockContactApi(Infoplus.ApiClient(configuration))
legacy_lowstock_contact_id = 56 # int | Id of the legacyLowstockContact to be returned.

try:
    # Get a legacyLowstockContact by id
    api_response = api_instance.get_legacy_lowstock_contact_by_id(legacy_lowstock_contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyLowstockContactApi->get_legacy_lowstock_contact_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legacy_lowstock_contact_id** | **int**| Id of the legacyLowstockContact to be returned. | 

### Return type

[**LegacyLowstockContact**](LegacyLowstockContact.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legacy_lowstock_contact_tags**
> get_legacy_lowstock_contact_tags(legacy_lowstock_contact_id)

Get the tags for a legacyLowstockContact.

Get all existing legacyLowstockContact tags.

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
api_instance = Infoplus.LegacyLowstockContactApi(Infoplus.ApiClient(configuration))
legacy_lowstock_contact_id = 56 # int | Id of the legacyLowstockContact to get tags for

try:
    # Get the tags for a legacyLowstockContact.
    api_instance.get_legacy_lowstock_contact_tags(legacy_lowstock_contact_id)
except ApiException as e:
    print("Exception when calling LegacyLowstockContactApi->get_legacy_lowstock_contact_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legacy_lowstock_contact_id** | **int**| Id of the legacyLowstockContact to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_legacy_lowstock_contact**
> update_legacy_lowstock_contact(body)

Update a legacyLowstockContact

Updates an existing legacyLowstockContact using the specified data.

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
api_instance = Infoplus.LegacyLowstockContactApi(Infoplus.ApiClient(configuration))
body = Infoplus.LegacyLowstockContact() # LegacyLowstockContact | LegacyLowstockContact to be updated.

try:
    # Update a legacyLowstockContact
    api_instance.update_legacy_lowstock_contact(body)
except ApiException as e:
    print("Exception when calling LegacyLowstockContactApi->update_legacy_lowstock_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LegacyLowstockContact**](LegacyLowstockContact.md)| LegacyLowstockContact to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

