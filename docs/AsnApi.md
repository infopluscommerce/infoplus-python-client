# Infoplus.AsnApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asn**](AsnApi.md#add_asn) | **POST** /beta/asn | Create an asn
[**add_asn_audit**](AsnApi.md#add_asn_audit) | **PUT** /beta/asn/{asnId}/audit/{asnAudit} | Add new audit for an asn
[**add_asn_file**](AsnApi.md#add_asn_file) | **POST** /beta/asn/{asnId}/file/{fileName} | Attach a file to an asn
[**add_asn_file_by_url**](AsnApi.md#add_asn_file_by_url) | **POST** /beta/asn/{asnId}/file | Attach a file to an asn by URL.
[**add_asn_tag**](AsnApi.md#add_asn_tag) | **PUT** /beta/asn/{asnId}/tag/{asnTag} | Add new tags for an asn.
[**delete_asn**](AsnApi.md#delete_asn) | **DELETE** /beta/asn/{asnId} | Delete an asn
[**delete_asn_file**](AsnApi.md#delete_asn_file) | **DELETE** /beta/asn/{asnId}/file/{fileId} | Delete a file for an asn.
[**delete_asn_tag**](AsnApi.md#delete_asn_tag) | **DELETE** /beta/asn/{asnId}/tag/{asnTag} | Delete a tag for an asn.
[**get_asn_by_filter**](AsnApi.md#get_asn_by_filter) | **GET** /beta/asn/search | Search asns by filter
[**get_asn_by_id**](AsnApi.md#get_asn_by_id) | **GET** /beta/asn/{asnId} | Get an asn by id
[**get_asn_files**](AsnApi.md#get_asn_files) | **GET** /beta/asn/{asnId}/file | Get the files for an asn.
[**get_asn_tags**](AsnApi.md#get_asn_tags) | **GET** /beta/asn/{asnId}/tag | Get the tags for an asn.
[**get_duplicate_asn_by_id**](AsnApi.md#get_duplicate_asn_by_id) | **GET** /beta/asn/duplicate/{asnId} | Get a duplicated an asn by id
[**update_asn**](AsnApi.md#update_asn) | **PUT** /beta/asn | Update an asn
[**update_asn_custom_fields**](AsnApi.md#update_asn_custom_fields) | **PUT** /beta/asn/customFields | Update an asn custom fields


# **add_asn**
> Asn add_asn(body)

Create an asn

Inserts a new asn using the specified data.

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
api_instance = Infoplus.AsnApi(Infoplus.ApiClient(configuration))
body = Infoplus.Asn() # Asn | Asn to be inserted.

try:
    # Create an asn
    api_response = api_instance.add_asn(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsnApi->add_asn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Asn**](Asn.md)| Asn to be inserted. | 

### Return type

[**Asn**](Asn.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_asn_audit**
> add_asn_audit(asn_id, asn_audit)

Add new audit for an asn

Adds an audit to an existing asn.

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
api_instance = Infoplus.AsnApi(Infoplus.ApiClient(configuration))
asn_id = 56 # int | Id of the asn to add an audit to
asn_audit = 'asn_audit_example' # str | The audit to add

try:
    # Add new audit for an asn
    api_instance.add_asn_audit(asn_id, asn_audit)
except ApiException as e:
    print("Exception when calling AsnApi->add_asn_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn_id** | **int**| Id of the asn to add an audit to | 
 **asn_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_asn_file**
> add_asn_file(asn_id, file_name)

Attach a file to an asn

Adds a file to an existing asn.

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
api_instance = Infoplus.AsnApi(Infoplus.ApiClient(configuration))
asn_id = 56 # int | Id of the asn to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an asn
    api_instance.add_asn_file(asn_id, file_name)
except ApiException as e:
    print("Exception when calling AsnApi->add_asn_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn_id** | **int**| Id of the asn to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_asn_file_by_url**
> add_asn_file_by_url(body, asn_id)

Attach a file to an asn by URL.

Adds a file to an existing asn by URL.

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
api_instance = Infoplus.AsnApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
asn_id = 56 # int | Id of the asn to add an file to

try:
    # Attach a file to an asn by URL.
    api_instance.add_asn_file_by_url(body, asn_id)
except ApiException as e:
    print("Exception when calling AsnApi->add_asn_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **asn_id** | **int**| Id of the asn to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_asn_tag**
> add_asn_tag(asn_id, asn_tag)

Add new tags for an asn.

Adds a tag to an existing asn.

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
api_instance = Infoplus.AsnApi(Infoplus.ApiClient(configuration))
asn_id = 56 # int | Id of the asn to add a tag to
asn_tag = 'asn_tag_example' # str | The tag to add

try:
    # Add new tags for an asn.
    api_instance.add_asn_tag(asn_id, asn_tag)
except ApiException as e:
    print("Exception when calling AsnApi->add_asn_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn_id** | **int**| Id of the asn to add a tag to | 
 **asn_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asn**
> delete_asn(asn_id)

Delete an asn

Deletes the asn identified by the specified id.

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
api_instance = Infoplus.AsnApi(Infoplus.ApiClient(configuration))
asn_id = 56 # int | Id of the asn to be deleted.

try:
    # Delete an asn
    api_instance.delete_asn(asn_id)
except ApiException as e:
    print("Exception when calling AsnApi->delete_asn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn_id** | **int**| Id of the asn to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asn_file**
> delete_asn_file(asn_id, file_id)

Delete a file for an asn.

Deletes an existing asn file using the specified data.

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
api_instance = Infoplus.AsnApi(Infoplus.ApiClient(configuration))
asn_id = 56 # int | Id of the asn to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an asn.
    api_instance.delete_asn_file(asn_id, file_id)
except ApiException as e:
    print("Exception when calling AsnApi->delete_asn_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn_id** | **int**| Id of the asn to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asn_tag**
> delete_asn_tag(asn_id, asn_tag)

Delete a tag for an asn.

Deletes an existing asn tag using the specified data.

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
api_instance = Infoplus.AsnApi(Infoplus.ApiClient(configuration))
asn_id = 56 # int | Id of the asn to remove tag from
asn_tag = 'asn_tag_example' # str | The tag to delete

try:
    # Delete a tag for an asn.
    api_instance.delete_asn_tag(asn_id, asn_tag)
except ApiException as e:
    print("Exception when calling AsnApi->delete_asn_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn_id** | **int**| Id of the asn to remove tag from | 
 **asn_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asn_by_filter**
> list[Asn] get_asn_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search asns by filter

Returns the list of asns that match the given filter.

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
api_instance = Infoplus.AsnApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search asns by filter
    api_response = api_instance.get_asn_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsnApi->get_asn_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Asn]**](Asn.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asn_by_id**
> Asn get_asn_by_id(asn_id)

Get an asn by id

Returns the asn identified by the specified id.

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
api_instance = Infoplus.AsnApi(Infoplus.ApiClient(configuration))
asn_id = 56 # int | Id of the asn to be returned.

try:
    # Get an asn by id
    api_response = api_instance.get_asn_by_id(asn_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsnApi->get_asn_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn_id** | **int**| Id of the asn to be returned. | 

### Return type

[**Asn**](Asn.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asn_files**
> get_asn_files(asn_id)

Get the files for an asn.

Get all existing asn files.

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
api_instance = Infoplus.AsnApi(Infoplus.ApiClient(configuration))
asn_id = 56 # int | Id of the asn to get files for

try:
    # Get the files for an asn.
    api_instance.get_asn_files(asn_id)
except ApiException as e:
    print("Exception when calling AsnApi->get_asn_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn_id** | **int**| Id of the asn to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asn_tags**
> get_asn_tags(asn_id)

Get the tags for an asn.

Get all existing asn tags.

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
api_instance = Infoplus.AsnApi(Infoplus.ApiClient(configuration))
asn_id = 56 # int | Id of the asn to get tags for

try:
    # Get the tags for an asn.
    api_instance.get_asn_tags(asn_id)
except ApiException as e:
    print("Exception when calling AsnApi->get_asn_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn_id** | **int**| Id of the asn to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_asn_by_id**
> Asn get_duplicate_asn_by_id(asn_id)

Get a duplicated an asn by id

Returns a duplicated asn identified by the specified id.

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
api_instance = Infoplus.AsnApi(Infoplus.ApiClient(configuration))
asn_id = 56 # int | Id of the asn to be duplicated.

try:
    # Get a duplicated an asn by id
    api_response = api_instance.get_duplicate_asn_by_id(asn_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsnApi->get_duplicate_asn_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn_id** | **int**| Id of the asn to be duplicated. | 

### Return type

[**Asn**](Asn.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asn**
> update_asn(body)

Update an asn

Updates an existing asn using the specified data.

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
api_instance = Infoplus.AsnApi(Infoplus.ApiClient(configuration))
body = Infoplus.Asn() # Asn | Asn to be updated.

try:
    # Update an asn
    api_instance.update_asn(body)
except ApiException as e:
    print("Exception when calling AsnApi->update_asn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Asn**](Asn.md)| Asn to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asn_custom_fields**
> update_asn_custom_fields(body)

Update an asn custom fields

Updates an existing asn custom fields using the specified data.

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
api_instance = Infoplus.AsnApi(Infoplus.ApiClient(configuration))
body = Infoplus.Asn() # Asn | Asn to be updated.

try:
    # Update an asn custom fields
    api_instance.update_asn_custom_fields(body)
except ApiException as e:
    print("Exception when calling AsnApi->update_asn_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Asn**](Asn.md)| Asn to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

