# Infoplus.ReplenishmentPlanApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_replenishment_plan**](ReplenishmentPlanApi.md#add_replenishment_plan) | **POST** /beta/replenishmentPlan | Create a replenishmentPlan
[**add_replenishment_plan_audit**](ReplenishmentPlanApi.md#add_replenishment_plan_audit) | **PUT** /beta/replenishmentPlan/{replenishmentPlanId}/audit/{replenishmentPlanAudit} | Add new audit for a replenishmentPlan
[**add_replenishment_plan_file**](ReplenishmentPlanApi.md#add_replenishment_plan_file) | **POST** /beta/replenishmentPlan/{replenishmentPlanId}/file/{fileName} | Attach a file to a replenishmentPlan
[**add_replenishment_plan_file_by_url**](ReplenishmentPlanApi.md#add_replenishment_plan_file_by_url) | **POST** /beta/replenishmentPlan/{replenishmentPlanId}/file | Attach a file to a replenishmentPlan by URL.
[**add_replenishment_plan_tag**](ReplenishmentPlanApi.md#add_replenishment_plan_tag) | **PUT** /beta/replenishmentPlan/{replenishmentPlanId}/tag/{replenishmentPlanTag} | Add new tags for a replenishmentPlan.
[**delete_replenishment_plan**](ReplenishmentPlanApi.md#delete_replenishment_plan) | **DELETE** /beta/replenishmentPlan/{replenishmentPlanId} | Delete a replenishmentPlan
[**delete_replenishment_plan_file**](ReplenishmentPlanApi.md#delete_replenishment_plan_file) | **DELETE** /beta/replenishmentPlan/{replenishmentPlanId}/file/{fileId} | Delete a file for a replenishmentPlan.
[**delete_replenishment_plan_tag**](ReplenishmentPlanApi.md#delete_replenishment_plan_tag) | **DELETE** /beta/replenishmentPlan/{replenishmentPlanId}/tag/{replenishmentPlanTag} | Delete a tag for a replenishmentPlan.
[**get_duplicate_replenishment_plan_by_id**](ReplenishmentPlanApi.md#get_duplicate_replenishment_plan_by_id) | **GET** /beta/replenishmentPlan/duplicate/{replenishmentPlanId} | Get a duplicated a replenishmentPlan by id
[**get_replenishment_plan_by_filter**](ReplenishmentPlanApi.md#get_replenishment_plan_by_filter) | **GET** /beta/replenishmentPlan/search | Search replenishmentPlans by filter
[**get_replenishment_plan_by_id**](ReplenishmentPlanApi.md#get_replenishment_plan_by_id) | **GET** /beta/replenishmentPlan/{replenishmentPlanId} | Get a replenishmentPlan by id
[**get_replenishment_plan_files**](ReplenishmentPlanApi.md#get_replenishment_plan_files) | **GET** /beta/replenishmentPlan/{replenishmentPlanId}/file | Get the files for a replenishmentPlan.
[**get_replenishment_plan_tags**](ReplenishmentPlanApi.md#get_replenishment_plan_tags) | **GET** /beta/replenishmentPlan/{replenishmentPlanId}/tag | Get the tags for a replenishmentPlan.
[**update_replenishment_plan**](ReplenishmentPlanApi.md#update_replenishment_plan) | **PUT** /beta/replenishmentPlan | Update a replenishmentPlan
[**update_replenishment_plan_custom_fields**](ReplenishmentPlanApi.md#update_replenishment_plan_custom_fields) | **PUT** /beta/replenishmentPlan/customFields | Update a replenishmentPlan custom fields


# **add_replenishment_plan**
> ReplenishmentPlan add_replenishment_plan(body)

Create a replenishmentPlan

Inserts a new replenishmentPlan using the specified data.

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
api_instance = Infoplus.ReplenishmentPlanApi(Infoplus.ApiClient(configuration))
body = Infoplus.ReplenishmentPlan() # ReplenishmentPlan | ReplenishmentPlan to be inserted.

try:
    # Create a replenishmentPlan
    api_response = api_instance.add_replenishment_plan(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplenishmentPlanApi->add_replenishment_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplenishmentPlan**](ReplenishmentPlan.md)| ReplenishmentPlan to be inserted. | 

### Return type

[**ReplenishmentPlan**](ReplenishmentPlan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_replenishment_plan_audit**
> add_replenishment_plan_audit(replenishment_plan_id, replenishment_plan_audit)

Add new audit for a replenishmentPlan

Adds an audit to an existing replenishmentPlan.

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
api_instance = Infoplus.ReplenishmentPlanApi(Infoplus.ApiClient(configuration))
replenishment_plan_id = 56 # int | Id of the replenishmentPlan to add an audit to
replenishment_plan_audit = 'replenishment_plan_audit_example' # str | The audit to add

try:
    # Add new audit for a replenishmentPlan
    api_instance.add_replenishment_plan_audit(replenishment_plan_id, replenishment_plan_audit)
except ApiException as e:
    print("Exception when calling ReplenishmentPlanApi->add_replenishment_plan_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_plan_id** | **int**| Id of the replenishmentPlan to add an audit to | 
 **replenishment_plan_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_replenishment_plan_file**
> add_replenishment_plan_file(replenishment_plan_id, file_name)

Attach a file to a replenishmentPlan

Adds a file to an existing replenishmentPlan.

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
api_instance = Infoplus.ReplenishmentPlanApi(Infoplus.ApiClient(configuration))
replenishment_plan_id = 56 # int | Id of the replenishmentPlan to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a replenishmentPlan
    api_instance.add_replenishment_plan_file(replenishment_plan_id, file_name)
except ApiException as e:
    print("Exception when calling ReplenishmentPlanApi->add_replenishment_plan_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_plan_id** | **int**| Id of the replenishmentPlan to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_replenishment_plan_file_by_url**
> add_replenishment_plan_file_by_url(body, replenishment_plan_id)

Attach a file to a replenishmentPlan by URL.

Adds a file to an existing replenishmentPlan by URL.

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
api_instance = Infoplus.ReplenishmentPlanApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
replenishment_plan_id = 56 # int | Id of the replenishmentPlan to add an file to

try:
    # Attach a file to a replenishmentPlan by URL.
    api_instance.add_replenishment_plan_file_by_url(body, replenishment_plan_id)
except ApiException as e:
    print("Exception when calling ReplenishmentPlanApi->add_replenishment_plan_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **replenishment_plan_id** | **int**| Id of the replenishmentPlan to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_replenishment_plan_tag**
> add_replenishment_plan_tag(replenishment_plan_id, replenishment_plan_tag)

Add new tags for a replenishmentPlan.

Adds a tag to an existing replenishmentPlan.

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
api_instance = Infoplus.ReplenishmentPlanApi(Infoplus.ApiClient(configuration))
replenishment_plan_id = 56 # int | Id of the replenishmentPlan to add a tag to
replenishment_plan_tag = 'replenishment_plan_tag_example' # str | The tag to add

try:
    # Add new tags for a replenishmentPlan.
    api_instance.add_replenishment_plan_tag(replenishment_plan_id, replenishment_plan_tag)
except ApiException as e:
    print("Exception when calling ReplenishmentPlanApi->add_replenishment_plan_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_plan_id** | **int**| Id of the replenishmentPlan to add a tag to | 
 **replenishment_plan_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_replenishment_plan**
> delete_replenishment_plan(replenishment_plan_id)

Delete a replenishmentPlan

Deletes the replenishmentPlan identified by the specified id.

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
api_instance = Infoplus.ReplenishmentPlanApi(Infoplus.ApiClient(configuration))
replenishment_plan_id = 56 # int | Id of the replenishmentPlan to be deleted.

try:
    # Delete a replenishmentPlan
    api_instance.delete_replenishment_plan(replenishment_plan_id)
except ApiException as e:
    print("Exception when calling ReplenishmentPlanApi->delete_replenishment_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_plan_id** | **int**| Id of the replenishmentPlan to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_replenishment_plan_file**
> delete_replenishment_plan_file(replenishment_plan_id, file_id)

Delete a file for a replenishmentPlan.

Deletes an existing replenishmentPlan file using the specified data.

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
api_instance = Infoplus.ReplenishmentPlanApi(Infoplus.ApiClient(configuration))
replenishment_plan_id = 56 # int | Id of the replenishmentPlan to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a replenishmentPlan.
    api_instance.delete_replenishment_plan_file(replenishment_plan_id, file_id)
except ApiException as e:
    print("Exception when calling ReplenishmentPlanApi->delete_replenishment_plan_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_plan_id** | **int**| Id of the replenishmentPlan to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_replenishment_plan_tag**
> delete_replenishment_plan_tag(replenishment_plan_id, replenishment_plan_tag)

Delete a tag for a replenishmentPlan.

Deletes an existing replenishmentPlan tag using the specified data.

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
api_instance = Infoplus.ReplenishmentPlanApi(Infoplus.ApiClient(configuration))
replenishment_plan_id = 56 # int | Id of the replenishmentPlan to remove tag from
replenishment_plan_tag = 'replenishment_plan_tag_example' # str | The tag to delete

try:
    # Delete a tag for a replenishmentPlan.
    api_instance.delete_replenishment_plan_tag(replenishment_plan_id, replenishment_plan_tag)
except ApiException as e:
    print("Exception when calling ReplenishmentPlanApi->delete_replenishment_plan_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_plan_id** | **int**| Id of the replenishmentPlan to remove tag from | 
 **replenishment_plan_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_replenishment_plan_by_id**
> ReplenishmentPlan get_duplicate_replenishment_plan_by_id(replenishment_plan_id)

Get a duplicated a replenishmentPlan by id

Returns a duplicated replenishmentPlan identified by the specified id.

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
api_instance = Infoplus.ReplenishmentPlanApi(Infoplus.ApiClient(configuration))
replenishment_plan_id = 56 # int | Id of the replenishmentPlan to be duplicated.

try:
    # Get a duplicated a replenishmentPlan by id
    api_response = api_instance.get_duplicate_replenishment_plan_by_id(replenishment_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplenishmentPlanApi->get_duplicate_replenishment_plan_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_plan_id** | **int**| Id of the replenishmentPlan to be duplicated. | 

### Return type

[**ReplenishmentPlan**](ReplenishmentPlan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replenishment_plan_by_filter**
> list[ReplenishmentPlan] get_replenishment_plan_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search replenishmentPlans by filter

Returns the list of replenishmentPlans that match the given filter.

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
api_instance = Infoplus.ReplenishmentPlanApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search replenishmentPlans by filter
    api_response = api_instance.get_replenishment_plan_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplenishmentPlanApi->get_replenishment_plan_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ReplenishmentPlan]**](ReplenishmentPlan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replenishment_plan_by_id**
> ReplenishmentPlan get_replenishment_plan_by_id(replenishment_plan_id)

Get a replenishmentPlan by id

Returns the replenishmentPlan identified by the specified id.

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
api_instance = Infoplus.ReplenishmentPlanApi(Infoplus.ApiClient(configuration))
replenishment_plan_id = 56 # int | Id of the replenishmentPlan to be returned.

try:
    # Get a replenishmentPlan by id
    api_response = api_instance.get_replenishment_plan_by_id(replenishment_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplenishmentPlanApi->get_replenishment_plan_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_plan_id** | **int**| Id of the replenishmentPlan to be returned. | 

### Return type

[**ReplenishmentPlan**](ReplenishmentPlan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replenishment_plan_files**
> get_replenishment_plan_files(replenishment_plan_id)

Get the files for a replenishmentPlan.

Get all existing replenishmentPlan files.

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
api_instance = Infoplus.ReplenishmentPlanApi(Infoplus.ApiClient(configuration))
replenishment_plan_id = 56 # int | Id of the replenishmentPlan to get files for

try:
    # Get the files for a replenishmentPlan.
    api_instance.get_replenishment_plan_files(replenishment_plan_id)
except ApiException as e:
    print("Exception when calling ReplenishmentPlanApi->get_replenishment_plan_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_plan_id** | **int**| Id of the replenishmentPlan to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replenishment_plan_tags**
> get_replenishment_plan_tags(replenishment_plan_id)

Get the tags for a replenishmentPlan.

Get all existing replenishmentPlan tags.

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
api_instance = Infoplus.ReplenishmentPlanApi(Infoplus.ApiClient(configuration))
replenishment_plan_id = 56 # int | Id of the replenishmentPlan to get tags for

try:
    # Get the tags for a replenishmentPlan.
    api_instance.get_replenishment_plan_tags(replenishment_plan_id)
except ApiException as e:
    print("Exception when calling ReplenishmentPlanApi->get_replenishment_plan_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_plan_id** | **int**| Id of the replenishmentPlan to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_replenishment_plan**
> update_replenishment_plan(body)

Update a replenishmentPlan

Updates an existing replenishmentPlan using the specified data.

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
api_instance = Infoplus.ReplenishmentPlanApi(Infoplus.ApiClient(configuration))
body = Infoplus.ReplenishmentPlan() # ReplenishmentPlan | ReplenishmentPlan to be updated.

try:
    # Update a replenishmentPlan
    api_instance.update_replenishment_plan(body)
except ApiException as e:
    print("Exception when calling ReplenishmentPlanApi->update_replenishment_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplenishmentPlan**](ReplenishmentPlan.md)| ReplenishmentPlan to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_replenishment_plan_custom_fields**
> update_replenishment_plan_custom_fields(body)

Update a replenishmentPlan custom fields

Updates an existing replenishmentPlan custom fields using the specified data.

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
api_instance = Infoplus.ReplenishmentPlanApi(Infoplus.ApiClient(configuration))
body = Infoplus.ReplenishmentPlan() # ReplenishmentPlan | ReplenishmentPlan to be updated.

try:
    # Update a replenishmentPlan custom fields
    api_instance.update_replenishment_plan_custom_fields(body)
except ApiException as e:
    print("Exception when calling ReplenishmentPlanApi->update_replenishment_plan_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplenishmentPlan**](ReplenishmentPlan.md)| ReplenishmentPlan to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

