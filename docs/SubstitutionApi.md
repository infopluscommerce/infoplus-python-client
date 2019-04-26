# Infoplus.SubstitutionApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_substitution**](SubstitutionApi.md#add_substitution) | **POST** /beta/substitution | Create a substitution
[**add_substitution_audit**](SubstitutionApi.md#add_substitution_audit) | **PUT** /beta/substitution/{substitutionId}/audit/{substitutionAudit} | Add new audit for a substitution
[**add_substitution_file**](SubstitutionApi.md#add_substitution_file) | **POST** /beta/substitution/{substitutionId}/file/{fileName} | Attach a file to a substitution
[**add_substitution_tag**](SubstitutionApi.md#add_substitution_tag) | **PUT** /beta/substitution/{substitutionId}/tag/{substitutionTag} | Add new tags for a substitution.
[**delete_substitution**](SubstitutionApi.md#delete_substitution) | **DELETE** /beta/substitution/{substitutionId} | Delete a substitution
[**delete_substitution_tag**](SubstitutionApi.md#delete_substitution_tag) | **DELETE** /beta/substitution/{substitutionId}/tag/{substitutionTag} | Delete a tag for a substitution.
[**get_duplicate_substitution_by_id**](SubstitutionApi.md#get_duplicate_substitution_by_id) | **GET** /beta/substitution/duplicate/{substitutionId} | Get a duplicated a substitution by id
[**get_substitution_by_filter**](SubstitutionApi.md#get_substitution_by_filter) | **GET** /beta/substitution/search | Search substitutions by filter
[**get_substitution_by_id**](SubstitutionApi.md#get_substitution_by_id) | **GET** /beta/substitution/{substitutionId} | Get a substitution by id
[**get_substitution_tags**](SubstitutionApi.md#get_substitution_tags) | **GET** /beta/substitution/{substitutionId}/tag | Get the tags for a substitution.
[**update_substitution**](SubstitutionApi.md#update_substitution) | **PUT** /beta/substitution | Update a substitution
[**update_substitution_custom_fields**](SubstitutionApi.md#update_substitution_custom_fields) | **PUT** /beta/substitution/customFields | Update a substitution custom fields


# **add_substitution**
> Substitution add_substitution(body)

Create a substitution

Inserts a new substitution using the specified data.

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
api_instance = Infoplus.SubstitutionApi(Infoplus.ApiClient(configuration))
body = Infoplus.Substitution() # Substitution | Substitution to be inserted.

try:
    # Create a substitution
    api_response = api_instance.add_substitution(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubstitutionApi->add_substitution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Substitution**](Substitution.md)| Substitution to be inserted. | 

### Return type

[**Substitution**](Substitution.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_substitution_audit**
> add_substitution_audit(substitution_id, substitution_audit)

Add new audit for a substitution

Adds an audit to an existing substitution.

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
api_instance = Infoplus.SubstitutionApi(Infoplus.ApiClient(configuration))
substitution_id = 56 # int | Id of the substitution to add an audit to
substitution_audit = 'substitution_audit_example' # str | The audit to add

try:
    # Add new audit for a substitution
    api_instance.add_substitution_audit(substitution_id, substitution_audit)
except ApiException as e:
    print("Exception when calling SubstitutionApi->add_substitution_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **substitution_id** | **int**| Id of the substitution to add an audit to | 
 **substitution_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_substitution_file**
> add_substitution_file(substitution_id, file_name)

Attach a file to a substitution

Adds a file to an existing substitution.

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
api_instance = Infoplus.SubstitutionApi(Infoplus.ApiClient(configuration))
substitution_id = 56 # int | Id of the substitution to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a substitution
    api_instance.add_substitution_file(substitution_id, file_name)
except ApiException as e:
    print("Exception when calling SubstitutionApi->add_substitution_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **substitution_id** | **int**| Id of the substitution to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_substitution_tag**
> add_substitution_tag(substitution_id, substitution_tag)

Add new tags for a substitution.

Adds a tag to an existing substitution.

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
api_instance = Infoplus.SubstitutionApi(Infoplus.ApiClient(configuration))
substitution_id = 56 # int | Id of the substitution to add a tag to
substitution_tag = 'substitution_tag_example' # str | The tag to add

try:
    # Add new tags for a substitution.
    api_instance.add_substitution_tag(substitution_id, substitution_tag)
except ApiException as e:
    print("Exception when calling SubstitutionApi->add_substitution_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **substitution_id** | **int**| Id of the substitution to add a tag to | 
 **substitution_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_substitution**
> delete_substitution(substitution_id)

Delete a substitution

Deletes the substitution identified by the specified id.

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
api_instance = Infoplus.SubstitutionApi(Infoplus.ApiClient(configuration))
substitution_id = 56 # int | Id of the substitution to be deleted.

try:
    # Delete a substitution
    api_instance.delete_substitution(substitution_id)
except ApiException as e:
    print("Exception when calling SubstitutionApi->delete_substitution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **substitution_id** | **int**| Id of the substitution to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_substitution_tag**
> delete_substitution_tag(substitution_id, substitution_tag)

Delete a tag for a substitution.

Deletes an existing substitution tag using the specified data.

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
api_instance = Infoplus.SubstitutionApi(Infoplus.ApiClient(configuration))
substitution_id = 56 # int | Id of the substitution to remove tag from
substitution_tag = 'substitution_tag_example' # str | The tag to delete

try:
    # Delete a tag for a substitution.
    api_instance.delete_substitution_tag(substitution_id, substitution_tag)
except ApiException as e:
    print("Exception when calling SubstitutionApi->delete_substitution_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **substitution_id** | **int**| Id of the substitution to remove tag from | 
 **substitution_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_substitution_by_id**
> Substitution get_duplicate_substitution_by_id(substitution_id)

Get a duplicated a substitution by id

Returns a duplicated substitution identified by the specified id.

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
api_instance = Infoplus.SubstitutionApi(Infoplus.ApiClient(configuration))
substitution_id = 56 # int | Id of the substitution to be duplicated.

try:
    # Get a duplicated a substitution by id
    api_response = api_instance.get_duplicate_substitution_by_id(substitution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubstitutionApi->get_duplicate_substitution_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **substitution_id** | **int**| Id of the substitution to be duplicated. | 

### Return type

[**Substitution**](Substitution.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_substitution_by_filter**
> list[Substitution] get_substitution_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search substitutions by filter

Returns the list of substitutions that match the given filter.

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
api_instance = Infoplus.SubstitutionApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search substitutions by filter
    api_response = api_instance.get_substitution_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubstitutionApi->get_substitution_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Substitution]**](Substitution.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_substitution_by_id**
> Substitution get_substitution_by_id(substitution_id)

Get a substitution by id

Returns the substitution identified by the specified id.

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
api_instance = Infoplus.SubstitutionApi(Infoplus.ApiClient(configuration))
substitution_id = 56 # int | Id of the substitution to be returned.

try:
    # Get a substitution by id
    api_response = api_instance.get_substitution_by_id(substitution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubstitutionApi->get_substitution_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **substitution_id** | **int**| Id of the substitution to be returned. | 

### Return type

[**Substitution**](Substitution.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_substitution_tags**
> get_substitution_tags(substitution_id)

Get the tags for a substitution.

Get all existing substitution tags.

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
api_instance = Infoplus.SubstitutionApi(Infoplus.ApiClient(configuration))
substitution_id = 56 # int | Id of the substitution to get tags for

try:
    # Get the tags for a substitution.
    api_instance.get_substitution_tags(substitution_id)
except ApiException as e:
    print("Exception when calling SubstitutionApi->get_substitution_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **substitution_id** | **int**| Id of the substitution to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_substitution**
> update_substitution(body)

Update a substitution

Updates an existing substitution using the specified data.

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
api_instance = Infoplus.SubstitutionApi(Infoplus.ApiClient(configuration))
body = Infoplus.Substitution() # Substitution | Substitution to be updated.

try:
    # Update a substitution
    api_instance.update_substitution(body)
except ApiException as e:
    print("Exception when calling SubstitutionApi->update_substitution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Substitution**](Substitution.md)| Substitution to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_substitution_custom_fields**
> update_substitution_custom_fields(body)

Update a substitution custom fields

Updates an existing substitution custom fields using the specified data.

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
api_instance = Infoplus.SubstitutionApi(Infoplus.ApiClient(configuration))
body = Infoplus.Substitution() # Substitution | Substitution to be updated.

try:
    # Update a substitution custom fields
    api_instance.update_substitution_custom_fields(body)
except ApiException as e:
    print("Exception when calling SubstitutionApi->update_substitution_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Substitution**](Substitution.md)| Substitution to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

