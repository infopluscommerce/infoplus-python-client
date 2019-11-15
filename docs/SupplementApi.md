# Infoplus.SupplementApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_supplement**](SupplementApi.md#add_supplement) | **POST** /beta/supplement | Create a supplement
[**add_supplement_audit**](SupplementApi.md#add_supplement_audit) | **PUT** /beta/supplement/{supplementId}/audit/{supplementAudit} | Add new audit for a supplement
[**add_supplement_file**](SupplementApi.md#add_supplement_file) | **POST** /beta/supplement/{supplementId}/file/{fileName} | Attach a file to a supplement
[**add_supplement_tag**](SupplementApi.md#add_supplement_tag) | **PUT** /beta/supplement/{supplementId}/tag/{supplementTag} | Add new tags for a supplement.
[**delete_supplement**](SupplementApi.md#delete_supplement) | **DELETE** /beta/supplement/{supplementId} | Delete a supplement
[**delete_supplement_tag**](SupplementApi.md#delete_supplement_tag) | **DELETE** /beta/supplement/{supplementId}/tag/{supplementTag} | Delete a tag for a supplement.
[**get_duplicate_supplement_by_id**](SupplementApi.md#get_duplicate_supplement_by_id) | **GET** /beta/supplement/duplicate/{supplementId} | Get a duplicated a supplement by id
[**get_supplement_by_filter**](SupplementApi.md#get_supplement_by_filter) | **GET** /beta/supplement/search | Search supplements by filter
[**get_supplement_by_id**](SupplementApi.md#get_supplement_by_id) | **GET** /beta/supplement/{supplementId} | Get a supplement by id
[**get_supplement_tags**](SupplementApi.md#get_supplement_tags) | **GET** /beta/supplement/{supplementId}/tag | Get the tags for a supplement.
[**update_supplement**](SupplementApi.md#update_supplement) | **PUT** /beta/supplement | Update a supplement
[**update_supplement_custom_fields**](SupplementApi.md#update_supplement_custom_fields) | **PUT** /beta/supplement/customFields | Update a supplement custom fields


# **add_supplement**
> Supplement add_supplement(body)

Create a supplement

Inserts a new supplement using the specified data.

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
api_instance = Infoplus.SupplementApi(Infoplus.ApiClient(configuration))
body = Infoplus.Supplement() # Supplement | Supplement to be inserted.

try:
    # Create a supplement
    api_response = api_instance.add_supplement(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplementApi->add_supplement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Supplement**](Supplement.md)| Supplement to be inserted. | 

### Return type

[**Supplement**](Supplement.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_supplement_audit**
> add_supplement_audit(supplement_id, supplement_audit)

Add new audit for a supplement

Adds an audit to an existing supplement.

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
api_instance = Infoplus.SupplementApi(Infoplus.ApiClient(configuration))
supplement_id = 56 # int | Id of the supplement to add an audit to
supplement_audit = 'supplement_audit_example' # str | The audit to add

try:
    # Add new audit for a supplement
    api_instance.add_supplement_audit(supplement_id, supplement_audit)
except ApiException as e:
    print("Exception when calling SupplementApi->add_supplement_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplement_id** | **int**| Id of the supplement to add an audit to | 
 **supplement_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_supplement_file**
> add_supplement_file(supplement_id, file_name)

Attach a file to a supplement

Adds a file to an existing supplement.

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
api_instance = Infoplus.SupplementApi(Infoplus.ApiClient(configuration))
supplement_id = 56 # int | Id of the supplement to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a supplement
    api_instance.add_supplement_file(supplement_id, file_name)
except ApiException as e:
    print("Exception when calling SupplementApi->add_supplement_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplement_id** | **int**| Id of the supplement to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_supplement_tag**
> add_supplement_tag(supplement_id, supplement_tag)

Add new tags for a supplement.

Adds a tag to an existing supplement.

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
api_instance = Infoplus.SupplementApi(Infoplus.ApiClient(configuration))
supplement_id = 56 # int | Id of the supplement to add a tag to
supplement_tag = 'supplement_tag_example' # str | The tag to add

try:
    # Add new tags for a supplement.
    api_instance.add_supplement_tag(supplement_id, supplement_tag)
except ApiException as e:
    print("Exception when calling SupplementApi->add_supplement_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplement_id** | **int**| Id of the supplement to add a tag to | 
 **supplement_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_supplement**
> delete_supplement(supplement_id)

Delete a supplement

Deletes the supplement identified by the specified id.

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
api_instance = Infoplus.SupplementApi(Infoplus.ApiClient(configuration))
supplement_id = 56 # int | Id of the supplement to be deleted.

try:
    # Delete a supplement
    api_instance.delete_supplement(supplement_id)
except ApiException as e:
    print("Exception when calling SupplementApi->delete_supplement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplement_id** | **int**| Id of the supplement to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_supplement_tag**
> delete_supplement_tag(supplement_id, supplement_tag)

Delete a tag for a supplement.

Deletes an existing supplement tag using the specified data.

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
api_instance = Infoplus.SupplementApi(Infoplus.ApiClient(configuration))
supplement_id = 56 # int | Id of the supplement to remove tag from
supplement_tag = 'supplement_tag_example' # str | The tag to delete

try:
    # Delete a tag for a supplement.
    api_instance.delete_supplement_tag(supplement_id, supplement_tag)
except ApiException as e:
    print("Exception when calling SupplementApi->delete_supplement_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplement_id** | **int**| Id of the supplement to remove tag from | 
 **supplement_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_supplement_by_id**
> Supplement get_duplicate_supplement_by_id(supplement_id)

Get a duplicated a supplement by id

Returns a duplicated supplement identified by the specified id.

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
api_instance = Infoplus.SupplementApi(Infoplus.ApiClient(configuration))
supplement_id = 56 # int | Id of the supplement to be duplicated.

try:
    # Get a duplicated a supplement by id
    api_response = api_instance.get_duplicate_supplement_by_id(supplement_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplementApi->get_duplicate_supplement_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplement_id** | **int**| Id of the supplement to be duplicated. | 

### Return type

[**Supplement**](Supplement.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supplement_by_filter**
> list[Supplement] get_supplement_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search supplements by filter

Returns the list of supplements that match the given filter.

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
api_instance = Infoplus.SupplementApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search supplements by filter
    api_response = api_instance.get_supplement_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplementApi->get_supplement_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Supplement]**](Supplement.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supplement_by_id**
> Supplement get_supplement_by_id(supplement_id)

Get a supplement by id

Returns the supplement identified by the specified id.

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
api_instance = Infoplus.SupplementApi(Infoplus.ApiClient(configuration))
supplement_id = 56 # int | Id of the supplement to be returned.

try:
    # Get a supplement by id
    api_response = api_instance.get_supplement_by_id(supplement_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplementApi->get_supplement_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplement_id** | **int**| Id of the supplement to be returned. | 

### Return type

[**Supplement**](Supplement.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supplement_tags**
> get_supplement_tags(supplement_id)

Get the tags for a supplement.

Get all existing supplement tags.

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
api_instance = Infoplus.SupplementApi(Infoplus.ApiClient(configuration))
supplement_id = 56 # int | Id of the supplement to get tags for

try:
    # Get the tags for a supplement.
    api_instance.get_supplement_tags(supplement_id)
except ApiException as e:
    print("Exception when calling SupplementApi->get_supplement_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplement_id** | **int**| Id of the supplement to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_supplement**
> update_supplement(body)

Update a supplement

Updates an existing supplement using the specified data.

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
api_instance = Infoplus.SupplementApi(Infoplus.ApiClient(configuration))
body = Infoplus.Supplement() # Supplement | Supplement to be updated.

try:
    # Update a supplement
    api_instance.update_supplement(body)
except ApiException as e:
    print("Exception when calling SupplementApi->update_supplement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Supplement**](Supplement.md)| Supplement to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_supplement_custom_fields**
> update_supplement_custom_fields(body)

Update a supplement custom fields

Updates an existing supplement custom fields using the specified data.

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
api_instance = Infoplus.SupplementApi(Infoplus.ApiClient(configuration))
body = Infoplus.Supplement() # Supplement | Supplement to be updated.

try:
    # Update a supplement custom fields
    api_instance.update_supplement_custom_fields(body)
except ApiException as e:
    print("Exception when calling SupplementApi->update_supplement_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Supplement**](Supplement.md)| Supplement to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

