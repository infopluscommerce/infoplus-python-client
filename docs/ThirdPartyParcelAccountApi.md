# Infoplus.ThirdPartyParcelAccountApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_third_party_parcel_account**](ThirdPartyParcelAccountApi.md#add_third_party_parcel_account) | **POST** /v3.0/thirdPartyParcelAccount | Create a thirdPartyParcelAccount
[**add_third_party_parcel_account_audit**](ThirdPartyParcelAccountApi.md#add_third_party_parcel_account_audit) | **PUT** /v3.0/thirdPartyParcelAccount/{thirdPartyParcelAccountId}/audit/{thirdPartyParcelAccountAudit} | Add new audit for a thirdPartyParcelAccount
[**add_third_party_parcel_account_file**](ThirdPartyParcelAccountApi.md#add_third_party_parcel_account_file) | **POST** /v3.0/thirdPartyParcelAccount/{thirdPartyParcelAccountId}/file/{fileName} | Attach a file to a thirdPartyParcelAccount
[**add_third_party_parcel_account_file_by_url**](ThirdPartyParcelAccountApi.md#add_third_party_parcel_account_file_by_url) | **POST** /v3.0/thirdPartyParcelAccount/{thirdPartyParcelAccountId}/file | Attach a file to a thirdPartyParcelAccount by URL.
[**add_third_party_parcel_account_tag**](ThirdPartyParcelAccountApi.md#add_third_party_parcel_account_tag) | **PUT** /v3.0/thirdPartyParcelAccount/{thirdPartyParcelAccountId}/tag/{thirdPartyParcelAccountTag} | Add new tags for a thirdPartyParcelAccount.
[**delete_third_party_parcel_account**](ThirdPartyParcelAccountApi.md#delete_third_party_parcel_account) | **DELETE** /v3.0/thirdPartyParcelAccount/{thirdPartyParcelAccountId} | Delete a thirdPartyParcelAccount
[**delete_third_party_parcel_account_file**](ThirdPartyParcelAccountApi.md#delete_third_party_parcel_account_file) | **DELETE** /v3.0/thirdPartyParcelAccount/{thirdPartyParcelAccountId}/file/{fileId} | Delete a file for a thirdPartyParcelAccount.
[**delete_third_party_parcel_account_tag**](ThirdPartyParcelAccountApi.md#delete_third_party_parcel_account_tag) | **DELETE** /v3.0/thirdPartyParcelAccount/{thirdPartyParcelAccountId}/tag/{thirdPartyParcelAccountTag} | Delete a tag for a thirdPartyParcelAccount.
[**get_duplicate_third_party_parcel_account_by_id**](ThirdPartyParcelAccountApi.md#get_duplicate_third_party_parcel_account_by_id) | **GET** /v3.0/thirdPartyParcelAccount/duplicate/{thirdPartyParcelAccountId} | Get a duplicated a thirdPartyParcelAccount by id
[**get_third_party_parcel_account_by_filter**](ThirdPartyParcelAccountApi.md#get_third_party_parcel_account_by_filter) | **GET** /v3.0/thirdPartyParcelAccount/search | Search thirdPartyParcelAccounts by filter
[**get_third_party_parcel_account_by_id**](ThirdPartyParcelAccountApi.md#get_third_party_parcel_account_by_id) | **GET** /v3.0/thirdPartyParcelAccount/{thirdPartyParcelAccountId} | Get a thirdPartyParcelAccount by id
[**get_third_party_parcel_account_files**](ThirdPartyParcelAccountApi.md#get_third_party_parcel_account_files) | **GET** /v3.0/thirdPartyParcelAccount/{thirdPartyParcelAccountId}/file | Get the files for a thirdPartyParcelAccount.
[**get_third_party_parcel_account_tags**](ThirdPartyParcelAccountApi.md#get_third_party_parcel_account_tags) | **GET** /v3.0/thirdPartyParcelAccount/{thirdPartyParcelAccountId}/tag | Get the tags for a thirdPartyParcelAccount.
[**update_third_party_parcel_account**](ThirdPartyParcelAccountApi.md#update_third_party_parcel_account) | **PUT** /v3.0/thirdPartyParcelAccount | Update a thirdPartyParcelAccount
[**update_third_party_parcel_account_custom_fields**](ThirdPartyParcelAccountApi.md#update_third_party_parcel_account_custom_fields) | **PUT** /v3.0/thirdPartyParcelAccount/customFields | Update a thirdPartyParcelAccount custom fields


# **add_third_party_parcel_account**
> ThirdPartyParcelAccount add_third_party_parcel_account(body)

Create a thirdPartyParcelAccount

Inserts a new thirdPartyParcelAccount using the specified data.

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
api_instance = Infoplus.ThirdPartyParcelAccountApi(Infoplus.ApiClient(configuration))
body = Infoplus.ThirdPartyParcelAccount() # ThirdPartyParcelAccount | ThirdPartyParcelAccount to be inserted.

try:
    # Create a thirdPartyParcelAccount
    api_response = api_instance.add_third_party_parcel_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdPartyParcelAccountApi->add_third_party_parcel_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThirdPartyParcelAccount**](ThirdPartyParcelAccount.md)| ThirdPartyParcelAccount to be inserted. | 

### Return type

[**ThirdPartyParcelAccount**](ThirdPartyParcelAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_third_party_parcel_account_audit**
> add_third_party_parcel_account_audit(third_party_parcel_account_id, third_party_parcel_account_audit)

Add new audit for a thirdPartyParcelAccount

Adds an audit to an existing thirdPartyParcelAccount.

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
api_instance = Infoplus.ThirdPartyParcelAccountApi(Infoplus.ApiClient(configuration))
third_party_parcel_account_id = 56 # int | Id of the thirdPartyParcelAccount to add an audit to
third_party_parcel_account_audit = 'third_party_parcel_account_audit_example' # str | The audit to add

try:
    # Add new audit for a thirdPartyParcelAccount
    api_instance.add_third_party_parcel_account_audit(third_party_parcel_account_id, third_party_parcel_account_audit)
except ApiException as e:
    print("Exception when calling ThirdPartyParcelAccountApi->add_third_party_parcel_account_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **third_party_parcel_account_id** | **int**| Id of the thirdPartyParcelAccount to add an audit to | 
 **third_party_parcel_account_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_third_party_parcel_account_file**
> add_third_party_parcel_account_file(third_party_parcel_account_id, file_name)

Attach a file to a thirdPartyParcelAccount

Adds a file to an existing thirdPartyParcelAccount.

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
api_instance = Infoplus.ThirdPartyParcelAccountApi(Infoplus.ApiClient(configuration))
third_party_parcel_account_id = 56 # int | Id of the thirdPartyParcelAccount to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a thirdPartyParcelAccount
    api_instance.add_third_party_parcel_account_file(third_party_parcel_account_id, file_name)
except ApiException as e:
    print("Exception when calling ThirdPartyParcelAccountApi->add_third_party_parcel_account_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **third_party_parcel_account_id** | **int**| Id of the thirdPartyParcelAccount to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_third_party_parcel_account_file_by_url**
> add_third_party_parcel_account_file_by_url(body, third_party_parcel_account_id)

Attach a file to a thirdPartyParcelAccount by URL.

Adds a file to an existing thirdPartyParcelAccount by URL.

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
api_instance = Infoplus.ThirdPartyParcelAccountApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
third_party_parcel_account_id = 56 # int | Id of the thirdPartyParcelAccount to add an file to

try:
    # Attach a file to a thirdPartyParcelAccount by URL.
    api_instance.add_third_party_parcel_account_file_by_url(body, third_party_parcel_account_id)
except ApiException as e:
    print("Exception when calling ThirdPartyParcelAccountApi->add_third_party_parcel_account_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **third_party_parcel_account_id** | **int**| Id of the thirdPartyParcelAccount to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_third_party_parcel_account_tag**
> add_third_party_parcel_account_tag(third_party_parcel_account_id, third_party_parcel_account_tag)

Add new tags for a thirdPartyParcelAccount.

Adds a tag to an existing thirdPartyParcelAccount.

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
api_instance = Infoplus.ThirdPartyParcelAccountApi(Infoplus.ApiClient(configuration))
third_party_parcel_account_id = 56 # int | Id of the thirdPartyParcelAccount to add a tag to
third_party_parcel_account_tag = 'third_party_parcel_account_tag_example' # str | The tag to add

try:
    # Add new tags for a thirdPartyParcelAccount.
    api_instance.add_third_party_parcel_account_tag(third_party_parcel_account_id, third_party_parcel_account_tag)
except ApiException as e:
    print("Exception when calling ThirdPartyParcelAccountApi->add_third_party_parcel_account_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **third_party_parcel_account_id** | **int**| Id of the thirdPartyParcelAccount to add a tag to | 
 **third_party_parcel_account_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_third_party_parcel_account**
> delete_third_party_parcel_account(third_party_parcel_account_id)

Delete a thirdPartyParcelAccount

Deletes the thirdPartyParcelAccount identified by the specified id.

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
api_instance = Infoplus.ThirdPartyParcelAccountApi(Infoplus.ApiClient(configuration))
third_party_parcel_account_id = 56 # int | Id of the thirdPartyParcelAccount to be deleted.

try:
    # Delete a thirdPartyParcelAccount
    api_instance.delete_third_party_parcel_account(third_party_parcel_account_id)
except ApiException as e:
    print("Exception when calling ThirdPartyParcelAccountApi->delete_third_party_parcel_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **third_party_parcel_account_id** | **int**| Id of the thirdPartyParcelAccount to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_third_party_parcel_account_file**
> delete_third_party_parcel_account_file(third_party_parcel_account_id, file_id)

Delete a file for a thirdPartyParcelAccount.

Deletes an existing thirdPartyParcelAccount file using the specified data.

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
api_instance = Infoplus.ThirdPartyParcelAccountApi(Infoplus.ApiClient(configuration))
third_party_parcel_account_id = 56 # int | Id of the thirdPartyParcelAccount to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a thirdPartyParcelAccount.
    api_instance.delete_third_party_parcel_account_file(third_party_parcel_account_id, file_id)
except ApiException as e:
    print("Exception when calling ThirdPartyParcelAccountApi->delete_third_party_parcel_account_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **third_party_parcel_account_id** | **int**| Id of the thirdPartyParcelAccount to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_third_party_parcel_account_tag**
> delete_third_party_parcel_account_tag(third_party_parcel_account_id, third_party_parcel_account_tag)

Delete a tag for a thirdPartyParcelAccount.

Deletes an existing thirdPartyParcelAccount tag using the specified data.

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
api_instance = Infoplus.ThirdPartyParcelAccountApi(Infoplus.ApiClient(configuration))
third_party_parcel_account_id = 56 # int | Id of the thirdPartyParcelAccount to remove tag from
third_party_parcel_account_tag = 'third_party_parcel_account_tag_example' # str | The tag to delete

try:
    # Delete a tag for a thirdPartyParcelAccount.
    api_instance.delete_third_party_parcel_account_tag(third_party_parcel_account_id, third_party_parcel_account_tag)
except ApiException as e:
    print("Exception when calling ThirdPartyParcelAccountApi->delete_third_party_parcel_account_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **third_party_parcel_account_id** | **int**| Id of the thirdPartyParcelAccount to remove tag from | 
 **third_party_parcel_account_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_third_party_parcel_account_by_id**
> ThirdPartyParcelAccount get_duplicate_third_party_parcel_account_by_id(third_party_parcel_account_id)

Get a duplicated a thirdPartyParcelAccount by id

Returns a duplicated thirdPartyParcelAccount identified by the specified id.

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
api_instance = Infoplus.ThirdPartyParcelAccountApi(Infoplus.ApiClient(configuration))
third_party_parcel_account_id = 56 # int | Id of the thirdPartyParcelAccount to be duplicated.

try:
    # Get a duplicated a thirdPartyParcelAccount by id
    api_response = api_instance.get_duplicate_third_party_parcel_account_by_id(third_party_parcel_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdPartyParcelAccountApi->get_duplicate_third_party_parcel_account_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **third_party_parcel_account_id** | **int**| Id of the thirdPartyParcelAccount to be duplicated. | 

### Return type

[**ThirdPartyParcelAccount**](ThirdPartyParcelAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_third_party_parcel_account_by_filter**
> list[ThirdPartyParcelAccount] get_third_party_parcel_account_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search thirdPartyParcelAccounts by filter

Returns the list of thirdPartyParcelAccounts that match the given filter.

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
api_instance = Infoplus.ThirdPartyParcelAccountApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search thirdPartyParcelAccounts by filter
    api_response = api_instance.get_third_party_parcel_account_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdPartyParcelAccountApi->get_third_party_parcel_account_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ThirdPartyParcelAccount]**](ThirdPartyParcelAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_third_party_parcel_account_by_id**
> ThirdPartyParcelAccount get_third_party_parcel_account_by_id(third_party_parcel_account_id)

Get a thirdPartyParcelAccount by id

Returns the thirdPartyParcelAccount identified by the specified id.

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
api_instance = Infoplus.ThirdPartyParcelAccountApi(Infoplus.ApiClient(configuration))
third_party_parcel_account_id = 56 # int | Id of the thirdPartyParcelAccount to be returned.

try:
    # Get a thirdPartyParcelAccount by id
    api_response = api_instance.get_third_party_parcel_account_by_id(third_party_parcel_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdPartyParcelAccountApi->get_third_party_parcel_account_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **third_party_parcel_account_id** | **int**| Id of the thirdPartyParcelAccount to be returned. | 

### Return type

[**ThirdPartyParcelAccount**](ThirdPartyParcelAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_third_party_parcel_account_files**
> get_third_party_parcel_account_files(third_party_parcel_account_id)

Get the files for a thirdPartyParcelAccount.

Get all existing thirdPartyParcelAccount files.

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
api_instance = Infoplus.ThirdPartyParcelAccountApi(Infoplus.ApiClient(configuration))
third_party_parcel_account_id = 56 # int | Id of the thirdPartyParcelAccount to get files for

try:
    # Get the files for a thirdPartyParcelAccount.
    api_instance.get_third_party_parcel_account_files(third_party_parcel_account_id)
except ApiException as e:
    print("Exception when calling ThirdPartyParcelAccountApi->get_third_party_parcel_account_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **third_party_parcel_account_id** | **int**| Id of the thirdPartyParcelAccount to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_third_party_parcel_account_tags**
> get_third_party_parcel_account_tags(third_party_parcel_account_id)

Get the tags for a thirdPartyParcelAccount.

Get all existing thirdPartyParcelAccount tags.

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
api_instance = Infoplus.ThirdPartyParcelAccountApi(Infoplus.ApiClient(configuration))
third_party_parcel_account_id = 56 # int | Id of the thirdPartyParcelAccount to get tags for

try:
    # Get the tags for a thirdPartyParcelAccount.
    api_instance.get_third_party_parcel_account_tags(third_party_parcel_account_id)
except ApiException as e:
    print("Exception when calling ThirdPartyParcelAccountApi->get_third_party_parcel_account_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **third_party_parcel_account_id** | **int**| Id of the thirdPartyParcelAccount to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_third_party_parcel_account**
> update_third_party_parcel_account(body)

Update a thirdPartyParcelAccount

Updates an existing thirdPartyParcelAccount using the specified data.

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
api_instance = Infoplus.ThirdPartyParcelAccountApi(Infoplus.ApiClient(configuration))
body = Infoplus.ThirdPartyParcelAccount() # ThirdPartyParcelAccount | ThirdPartyParcelAccount to be updated.

try:
    # Update a thirdPartyParcelAccount
    api_instance.update_third_party_parcel_account(body)
except ApiException as e:
    print("Exception when calling ThirdPartyParcelAccountApi->update_third_party_parcel_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThirdPartyParcelAccount**](ThirdPartyParcelAccount.md)| ThirdPartyParcelAccount to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_third_party_parcel_account_custom_fields**
> update_third_party_parcel_account_custom_fields(body)

Update a thirdPartyParcelAccount custom fields

Updates an existing thirdPartyParcelAccount custom fields using the specified data.

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
api_instance = Infoplus.ThirdPartyParcelAccountApi(Infoplus.ApiClient(configuration))
body = Infoplus.ThirdPartyParcelAccount() # ThirdPartyParcelAccount | ThirdPartyParcelAccount to be updated.

try:
    # Update a thirdPartyParcelAccount custom fields
    api_instance.update_third_party_parcel_account_custom_fields(body)
except ApiException as e:
    print("Exception when calling ThirdPartyParcelAccountApi->update_third_party_parcel_account_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThirdPartyParcelAccount**](ThirdPartyParcelAccount.md)| ThirdPartyParcelAccount to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

