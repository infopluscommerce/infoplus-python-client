# Infoplus.ParcelAccountApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_parcel_account_audit**](ParcelAccountApi.md#add_parcel_account_audit) | **PUT** /beta/parcelAccount/{parcelAccountId}/audit/{parcelAccountAudit} | Add new audit for a parcelAccount
[**add_parcel_account_file**](ParcelAccountApi.md#add_parcel_account_file) | **POST** /beta/parcelAccount/{parcelAccountId}/file/{fileName} | Attach a file to a parcelAccount
[**add_parcel_account_tag**](ParcelAccountApi.md#add_parcel_account_tag) | **PUT** /beta/parcelAccount/{parcelAccountId}/tag/{parcelAccountTag} | Add new tags for a parcelAccount.
[**delete_parcel_account_tag**](ParcelAccountApi.md#delete_parcel_account_tag) | **DELETE** /beta/parcelAccount/{parcelAccountId}/tag/{parcelAccountTag} | Delete a tag for a parcelAccount.
[**get_duplicate_parcel_account_by_id**](ParcelAccountApi.md#get_duplicate_parcel_account_by_id) | **GET** /beta/parcelAccount/duplicate/{parcelAccountId} | Get a duplicated a parcelAccount by id
[**get_parcel_account_by_filter**](ParcelAccountApi.md#get_parcel_account_by_filter) | **GET** /beta/parcelAccount/search | Search parcelAccounts by filter
[**get_parcel_account_by_id**](ParcelAccountApi.md#get_parcel_account_by_id) | **GET** /beta/parcelAccount/{parcelAccountId} | Get a parcelAccount by id
[**get_parcel_account_tags**](ParcelAccountApi.md#get_parcel_account_tags) | **GET** /beta/parcelAccount/{parcelAccountId}/tag | Get the tags for a parcelAccount.
[**update_parcel_account_custom_fields**](ParcelAccountApi.md#update_parcel_account_custom_fields) | **PUT** /beta/parcelAccount/customFields | Update a parcelAccount custom fields


# **add_parcel_account_audit**
> add_parcel_account_audit(parcel_account_id, parcel_account_audit)

Add new audit for a parcelAccount

Adds an audit to an existing parcelAccount.

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
api_instance = Infoplus.ParcelAccountApi(Infoplus.ApiClient(configuration))
parcel_account_id = 56 # int | Id of the parcelAccount to add an audit to
parcel_account_audit = 'parcel_account_audit_example' # str | The audit to add

try:
    # Add new audit for a parcelAccount
    api_instance.add_parcel_account_audit(parcel_account_id, parcel_account_audit)
except ApiException as e:
    print("Exception when calling ParcelAccountApi->add_parcel_account_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_account_id** | **int**| Id of the parcelAccount to add an audit to | 
 **parcel_account_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_parcel_account_file**
> add_parcel_account_file(parcel_account_id, file_name)

Attach a file to a parcelAccount

Adds a file to an existing parcelAccount.

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
api_instance = Infoplus.ParcelAccountApi(Infoplus.ApiClient(configuration))
parcel_account_id = 56 # int | Id of the parcelAccount to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a parcelAccount
    api_instance.add_parcel_account_file(parcel_account_id, file_name)
except ApiException as e:
    print("Exception when calling ParcelAccountApi->add_parcel_account_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_account_id** | **int**| Id of the parcelAccount to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_parcel_account_tag**
> add_parcel_account_tag(parcel_account_id, parcel_account_tag)

Add new tags for a parcelAccount.

Adds a tag to an existing parcelAccount.

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
api_instance = Infoplus.ParcelAccountApi(Infoplus.ApiClient(configuration))
parcel_account_id = 56 # int | Id of the parcelAccount to add a tag to
parcel_account_tag = 'parcel_account_tag_example' # str | The tag to add

try:
    # Add new tags for a parcelAccount.
    api_instance.add_parcel_account_tag(parcel_account_id, parcel_account_tag)
except ApiException as e:
    print("Exception when calling ParcelAccountApi->add_parcel_account_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_account_id** | **int**| Id of the parcelAccount to add a tag to | 
 **parcel_account_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_parcel_account_tag**
> delete_parcel_account_tag(parcel_account_id, parcel_account_tag)

Delete a tag for a parcelAccount.

Deletes an existing parcelAccount tag using the specified data.

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
api_instance = Infoplus.ParcelAccountApi(Infoplus.ApiClient(configuration))
parcel_account_id = 56 # int | Id of the parcelAccount to remove tag from
parcel_account_tag = 'parcel_account_tag_example' # str | The tag to delete

try:
    # Delete a tag for a parcelAccount.
    api_instance.delete_parcel_account_tag(parcel_account_id, parcel_account_tag)
except ApiException as e:
    print("Exception when calling ParcelAccountApi->delete_parcel_account_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_account_id** | **int**| Id of the parcelAccount to remove tag from | 
 **parcel_account_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_parcel_account_by_id**
> ParcelAccount get_duplicate_parcel_account_by_id(parcel_account_id)

Get a duplicated a parcelAccount by id

Returns a duplicated parcelAccount identified by the specified id.

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
api_instance = Infoplus.ParcelAccountApi(Infoplus.ApiClient(configuration))
parcel_account_id = 56 # int | Id of the parcelAccount to be duplicated.

try:
    # Get a duplicated a parcelAccount by id
    api_response = api_instance.get_duplicate_parcel_account_by_id(parcel_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParcelAccountApi->get_duplicate_parcel_account_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_account_id** | **int**| Id of the parcelAccount to be duplicated. | 

### Return type

[**ParcelAccount**](ParcelAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parcel_account_by_filter**
> list[ParcelAccount] get_parcel_account_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search parcelAccounts by filter

Returns the list of parcelAccounts that match the given filter.

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
api_instance = Infoplus.ParcelAccountApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search parcelAccounts by filter
    api_response = api_instance.get_parcel_account_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParcelAccountApi->get_parcel_account_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ParcelAccount]**](ParcelAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parcel_account_by_id**
> ParcelAccount get_parcel_account_by_id(parcel_account_id)

Get a parcelAccount by id

Returns the parcelAccount identified by the specified id.

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
api_instance = Infoplus.ParcelAccountApi(Infoplus.ApiClient(configuration))
parcel_account_id = 56 # int | Id of the parcelAccount to be returned.

try:
    # Get a parcelAccount by id
    api_response = api_instance.get_parcel_account_by_id(parcel_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParcelAccountApi->get_parcel_account_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_account_id** | **int**| Id of the parcelAccount to be returned. | 

### Return type

[**ParcelAccount**](ParcelAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parcel_account_tags**
> get_parcel_account_tags(parcel_account_id)

Get the tags for a parcelAccount.

Get all existing parcelAccount tags.

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
api_instance = Infoplus.ParcelAccountApi(Infoplus.ApiClient(configuration))
parcel_account_id = 56 # int | Id of the parcelAccount to get tags for

try:
    # Get the tags for a parcelAccount.
    api_instance.get_parcel_account_tags(parcel_account_id)
except ApiException as e:
    print("Exception when calling ParcelAccountApi->get_parcel_account_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parcel_account_id** | **int**| Id of the parcelAccount to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_parcel_account_custom_fields**
> update_parcel_account_custom_fields(body)

Update a parcelAccount custom fields

Updates an existing parcelAccount custom fields using the specified data.

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
api_instance = Infoplus.ParcelAccountApi(Infoplus.ApiClient(configuration))
body = Infoplus.ParcelAccount() # ParcelAccount | ParcelAccount to be updated.

try:
    # Update a parcelAccount custom fields
    api_instance.update_parcel_account_custom_fields(body)
except ApiException as e:
    print("Exception when calling ParcelAccountApi->update_parcel_account_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParcelAccount**](ParcelAccount.md)| ParcelAccount to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

