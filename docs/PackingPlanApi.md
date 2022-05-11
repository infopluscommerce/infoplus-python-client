# Infoplus.PackingPlanApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_packing_plan**](PackingPlanApi.md#add_packing_plan) | **POST** /v3.0/packingPlan | Create a packingPlan
[**add_packing_plan_audit**](PackingPlanApi.md#add_packing_plan_audit) | **PUT** /v3.0/packingPlan/{packingPlanId}/audit/{packingPlanAudit} | Add new audit for a packingPlan
[**add_packing_plan_file**](PackingPlanApi.md#add_packing_plan_file) | **POST** /v3.0/packingPlan/{packingPlanId}/file/{fileName} | Attach a file to a packingPlan
[**add_packing_plan_file_by_url**](PackingPlanApi.md#add_packing_plan_file_by_url) | **POST** /v3.0/packingPlan/{packingPlanId}/file | Attach a file to a packingPlan by URL.
[**add_packing_plan_tag**](PackingPlanApi.md#add_packing_plan_tag) | **PUT** /v3.0/packingPlan/{packingPlanId}/tag/{packingPlanTag} | Add new tags for a packingPlan.
[**delete_packing_plan**](PackingPlanApi.md#delete_packing_plan) | **DELETE** /v3.0/packingPlan/{packingPlanId} | Delete a packingPlan
[**delete_packing_plan_file**](PackingPlanApi.md#delete_packing_plan_file) | **DELETE** /v3.0/packingPlan/{packingPlanId}/file/{fileId} | Delete a file for a packingPlan.
[**delete_packing_plan_tag**](PackingPlanApi.md#delete_packing_plan_tag) | **DELETE** /v3.0/packingPlan/{packingPlanId}/tag/{packingPlanTag} | Delete a tag for a packingPlan.
[**get_duplicate_packing_plan_by_id**](PackingPlanApi.md#get_duplicate_packing_plan_by_id) | **GET** /v3.0/packingPlan/duplicate/{packingPlanId} | Get a duplicated a packingPlan by id
[**get_packing_plan_by_filter**](PackingPlanApi.md#get_packing_plan_by_filter) | **GET** /v3.0/packingPlan/search | Search packingPlans by filter
[**get_packing_plan_by_id**](PackingPlanApi.md#get_packing_plan_by_id) | **GET** /v3.0/packingPlan/{packingPlanId} | Get a packingPlan by id
[**get_packing_plan_files**](PackingPlanApi.md#get_packing_plan_files) | **GET** /v3.0/packingPlan/{packingPlanId}/file | Get the files for a packingPlan.
[**get_packing_plan_tags**](PackingPlanApi.md#get_packing_plan_tags) | **GET** /v3.0/packingPlan/{packingPlanId}/tag | Get the tags for a packingPlan.
[**update_packing_plan**](PackingPlanApi.md#update_packing_plan) | **PUT** /v3.0/packingPlan | Update a packingPlan
[**update_packing_plan_custom_fields**](PackingPlanApi.md#update_packing_plan_custom_fields) | **PUT** /v3.0/packingPlan/customFields | Update a packingPlan custom fields


# **add_packing_plan**
> PackingPlan add_packing_plan(body)

Create a packingPlan

Inserts a new packingPlan using the specified data.

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
api_instance = Infoplus.PackingPlanApi(Infoplus.ApiClient(configuration))
body = Infoplus.PackingPlan() # PackingPlan | PackingPlan to be inserted.

try:
    # Create a packingPlan
    api_response = api_instance.add_packing_plan(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackingPlanApi->add_packing_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PackingPlan**](PackingPlan.md)| PackingPlan to be inserted. | 

### Return type

[**PackingPlan**](PackingPlan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_packing_plan_audit**
> add_packing_plan_audit(packing_plan_id, packing_plan_audit)

Add new audit for a packingPlan

Adds an audit to an existing packingPlan.

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
api_instance = Infoplus.PackingPlanApi(Infoplus.ApiClient(configuration))
packing_plan_id = 56 # int | Id of the packingPlan to add an audit to
packing_plan_audit = 'packing_plan_audit_example' # str | The audit to add

try:
    # Add new audit for a packingPlan
    api_instance.add_packing_plan_audit(packing_plan_id, packing_plan_audit)
except ApiException as e:
    print("Exception when calling PackingPlanApi->add_packing_plan_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_id** | **int**| Id of the packingPlan to add an audit to | 
 **packing_plan_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_packing_plan_file**
> add_packing_plan_file(packing_plan_id, file_name)

Attach a file to a packingPlan

Adds a file to an existing packingPlan.

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
api_instance = Infoplus.PackingPlanApi(Infoplus.ApiClient(configuration))
packing_plan_id = 56 # int | Id of the packingPlan to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a packingPlan
    api_instance.add_packing_plan_file(packing_plan_id, file_name)
except ApiException as e:
    print("Exception when calling PackingPlanApi->add_packing_plan_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_id** | **int**| Id of the packingPlan to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_packing_plan_file_by_url**
> add_packing_plan_file_by_url(body, packing_plan_id)

Attach a file to a packingPlan by URL.

Adds a file to an existing packingPlan by URL.

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
api_instance = Infoplus.PackingPlanApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
packing_plan_id = 56 # int | Id of the packingPlan to add an file to

try:
    # Attach a file to a packingPlan by URL.
    api_instance.add_packing_plan_file_by_url(body, packing_plan_id)
except ApiException as e:
    print("Exception when calling PackingPlanApi->add_packing_plan_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **packing_plan_id** | **int**| Id of the packingPlan to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_packing_plan_tag**
> add_packing_plan_tag(packing_plan_id, packing_plan_tag)

Add new tags for a packingPlan.

Adds a tag to an existing packingPlan.

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
api_instance = Infoplus.PackingPlanApi(Infoplus.ApiClient(configuration))
packing_plan_id = 56 # int | Id of the packingPlan to add a tag to
packing_plan_tag = 'packing_plan_tag_example' # str | The tag to add

try:
    # Add new tags for a packingPlan.
    api_instance.add_packing_plan_tag(packing_plan_id, packing_plan_tag)
except ApiException as e:
    print("Exception when calling PackingPlanApi->add_packing_plan_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_id** | **int**| Id of the packingPlan to add a tag to | 
 **packing_plan_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_packing_plan**
> delete_packing_plan(packing_plan_id)

Delete a packingPlan

Deletes the packingPlan identified by the specified id.

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
api_instance = Infoplus.PackingPlanApi(Infoplus.ApiClient(configuration))
packing_plan_id = 56 # int | Id of the packingPlan to be deleted.

try:
    # Delete a packingPlan
    api_instance.delete_packing_plan(packing_plan_id)
except ApiException as e:
    print("Exception when calling PackingPlanApi->delete_packing_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_id** | **int**| Id of the packingPlan to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_packing_plan_file**
> delete_packing_plan_file(packing_plan_id, file_id)

Delete a file for a packingPlan.

Deletes an existing packingPlan file using the specified data.

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
api_instance = Infoplus.PackingPlanApi(Infoplus.ApiClient(configuration))
packing_plan_id = 56 # int | Id of the packingPlan to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a packingPlan.
    api_instance.delete_packing_plan_file(packing_plan_id, file_id)
except ApiException as e:
    print("Exception when calling PackingPlanApi->delete_packing_plan_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_id** | **int**| Id of the packingPlan to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_packing_plan_tag**
> delete_packing_plan_tag(packing_plan_id, packing_plan_tag)

Delete a tag for a packingPlan.

Deletes an existing packingPlan tag using the specified data.

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
api_instance = Infoplus.PackingPlanApi(Infoplus.ApiClient(configuration))
packing_plan_id = 56 # int | Id of the packingPlan to remove tag from
packing_plan_tag = 'packing_plan_tag_example' # str | The tag to delete

try:
    # Delete a tag for a packingPlan.
    api_instance.delete_packing_plan_tag(packing_plan_id, packing_plan_tag)
except ApiException as e:
    print("Exception when calling PackingPlanApi->delete_packing_plan_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_id** | **int**| Id of the packingPlan to remove tag from | 
 **packing_plan_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_packing_plan_by_id**
> PackingPlan get_duplicate_packing_plan_by_id(packing_plan_id)

Get a duplicated a packingPlan by id

Returns a duplicated packingPlan identified by the specified id.

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
api_instance = Infoplus.PackingPlanApi(Infoplus.ApiClient(configuration))
packing_plan_id = 56 # int | Id of the packingPlan to be duplicated.

try:
    # Get a duplicated a packingPlan by id
    api_response = api_instance.get_duplicate_packing_plan_by_id(packing_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackingPlanApi->get_duplicate_packing_plan_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_id** | **int**| Id of the packingPlan to be duplicated. | 

### Return type

[**PackingPlan**](PackingPlan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packing_plan_by_filter**
> list[PackingPlan] get_packing_plan_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search packingPlans by filter

Returns the list of packingPlans that match the given filter.

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
api_instance = Infoplus.PackingPlanApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search packingPlans by filter
    api_response = api_instance.get_packing_plan_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackingPlanApi->get_packing_plan_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[PackingPlan]**](PackingPlan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packing_plan_by_id**
> PackingPlan get_packing_plan_by_id(packing_plan_id)

Get a packingPlan by id

Returns the packingPlan identified by the specified id.

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
api_instance = Infoplus.PackingPlanApi(Infoplus.ApiClient(configuration))
packing_plan_id = 56 # int | Id of the packingPlan to be returned.

try:
    # Get a packingPlan by id
    api_response = api_instance.get_packing_plan_by_id(packing_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackingPlanApi->get_packing_plan_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_id** | **int**| Id of the packingPlan to be returned. | 

### Return type

[**PackingPlan**](PackingPlan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packing_plan_files**
> get_packing_plan_files(packing_plan_id)

Get the files for a packingPlan.

Get all existing packingPlan files.

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
api_instance = Infoplus.PackingPlanApi(Infoplus.ApiClient(configuration))
packing_plan_id = 56 # int | Id of the packingPlan to get files for

try:
    # Get the files for a packingPlan.
    api_instance.get_packing_plan_files(packing_plan_id)
except ApiException as e:
    print("Exception when calling PackingPlanApi->get_packing_plan_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_id** | **int**| Id of the packingPlan to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packing_plan_tags**
> get_packing_plan_tags(packing_plan_id)

Get the tags for a packingPlan.

Get all existing packingPlan tags.

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
api_instance = Infoplus.PackingPlanApi(Infoplus.ApiClient(configuration))
packing_plan_id = 56 # int | Id of the packingPlan to get tags for

try:
    # Get the tags for a packingPlan.
    api_instance.get_packing_plan_tags(packing_plan_id)
except ApiException as e:
    print("Exception when calling PackingPlanApi->get_packing_plan_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packing_plan_id** | **int**| Id of the packingPlan to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_packing_plan**
> update_packing_plan(body)

Update a packingPlan

Updates an existing packingPlan using the specified data.

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
api_instance = Infoplus.PackingPlanApi(Infoplus.ApiClient(configuration))
body = Infoplus.PackingPlan() # PackingPlan | PackingPlan to be updated.

try:
    # Update a packingPlan
    api_instance.update_packing_plan(body)
except ApiException as e:
    print("Exception when calling PackingPlanApi->update_packing_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PackingPlan**](PackingPlan.md)| PackingPlan to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_packing_plan_custom_fields**
> update_packing_plan_custom_fields(body)

Update a packingPlan custom fields

Updates an existing packingPlan custom fields using the specified data.

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
api_instance = Infoplus.PackingPlanApi(Infoplus.ApiClient(configuration))
body = Infoplus.PackingPlan() # PackingPlan | PackingPlan to be updated.

try:
    # Update a packingPlan custom fields
    api_instance.update_packing_plan_custom_fields(body)
except ApiException as e:
    print("Exception when calling PackingPlanApi->update_packing_plan_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PackingPlan**](PackingPlan.md)| PackingPlan to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

