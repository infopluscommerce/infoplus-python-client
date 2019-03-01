# Infoplus.ManageScheduledPlansApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_manage_scheduled_plans**](ManageScheduledPlansApi.md#add_manage_scheduled_plans) | **POST** /beta/manageScheduledPlans | Create a manageScheduledPlans
[**add_manage_scheduled_plans_audit**](ManageScheduledPlansApi.md#add_manage_scheduled_plans_audit) | **PUT** /beta/manageScheduledPlans/{manageScheduledPlansId}/audit/{manageScheduledPlansAudit} | Add new audit for a manageScheduledPlans
[**add_manage_scheduled_plans_file**](ManageScheduledPlansApi.md#add_manage_scheduled_plans_file) | **POST** /beta/manageScheduledPlans/{manageScheduledPlansId}/file/{fileName} | Attach a file to a manageScheduledPlans
[**add_manage_scheduled_plans_tag**](ManageScheduledPlansApi.md#add_manage_scheduled_plans_tag) | **PUT** /beta/manageScheduledPlans/{manageScheduledPlansId}/tag/{manageScheduledPlansTag} | Add new tags for a manageScheduledPlans.
[**delete_manage_scheduled_plans**](ManageScheduledPlansApi.md#delete_manage_scheduled_plans) | **DELETE** /beta/manageScheduledPlans/{manageScheduledPlansId} | Delete a manageScheduledPlans
[**delete_manage_scheduled_plans_tag**](ManageScheduledPlansApi.md#delete_manage_scheduled_plans_tag) | **DELETE** /beta/manageScheduledPlans/{manageScheduledPlansId}/tag/{manageScheduledPlansTag} | Delete a tag for a manageScheduledPlans.
[**get_duplicate_manage_scheduled_plans_by_id**](ManageScheduledPlansApi.md#get_duplicate_manage_scheduled_plans_by_id) | **GET** /beta/manageScheduledPlans/duplicate/{manageScheduledPlansId} | Get a duplicated a manageScheduledPlans by id
[**get_manage_scheduled_plans_by_filter**](ManageScheduledPlansApi.md#get_manage_scheduled_plans_by_filter) | **GET** /beta/manageScheduledPlans/search | Search manageScheduledPlanses by filter
[**get_manage_scheduled_plans_by_id**](ManageScheduledPlansApi.md#get_manage_scheduled_plans_by_id) | **GET** /beta/manageScheduledPlans/{manageScheduledPlansId} | Get a manageScheduledPlans by id
[**get_manage_scheduled_plans_tags**](ManageScheduledPlansApi.md#get_manage_scheduled_plans_tags) | **GET** /beta/manageScheduledPlans/{manageScheduledPlansId}/tag | Get the tags for a manageScheduledPlans.
[**update_manage_scheduled_plans**](ManageScheduledPlansApi.md#update_manage_scheduled_plans) | **PUT** /beta/manageScheduledPlans | Update a manageScheduledPlans


# **add_manage_scheduled_plans**
> ManageScheduledPlans add_manage_scheduled_plans(body)

Create a manageScheduledPlans

Inserts a new manageScheduledPlans using the specified data.

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
api_instance = Infoplus.ManageScheduledPlansApi(Infoplus.ApiClient(configuration))
body = Infoplus.ManageScheduledPlans() # ManageScheduledPlans | ManageScheduledPlans to be inserted.

try:
    # Create a manageScheduledPlans
    api_response = api_instance.add_manage_scheduled_plans(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManageScheduledPlansApi->add_manage_scheduled_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManageScheduledPlans**](ManageScheduledPlans.md)| ManageScheduledPlans to be inserted. | 

### Return type

[**ManageScheduledPlans**](ManageScheduledPlans.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_manage_scheduled_plans_audit**
> add_manage_scheduled_plans_audit(manage_scheduled_plans_id, manage_scheduled_plans_audit)

Add new audit for a manageScheduledPlans

Adds an audit to an existing manageScheduledPlans.

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
api_instance = Infoplus.ManageScheduledPlansApi(Infoplus.ApiClient(configuration))
manage_scheduled_plans_id = 56 # int | Id of the manageScheduledPlans to add an audit to
manage_scheduled_plans_audit = 'manage_scheduled_plans_audit_example' # str | The audit to add

try:
    # Add new audit for a manageScheduledPlans
    api_instance.add_manage_scheduled_plans_audit(manage_scheduled_plans_id, manage_scheduled_plans_audit)
except ApiException as e:
    print("Exception when calling ManageScheduledPlansApi->add_manage_scheduled_plans_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manage_scheduled_plans_id** | **int**| Id of the manageScheduledPlans to add an audit to | 
 **manage_scheduled_plans_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_manage_scheduled_plans_file**
> add_manage_scheduled_plans_file(manage_scheduled_plans_id, file_name)

Attach a file to a manageScheduledPlans

Adds a file to an existing manageScheduledPlans.

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
api_instance = Infoplus.ManageScheduledPlansApi(Infoplus.ApiClient(configuration))
manage_scheduled_plans_id = 56 # int | Id of the manageScheduledPlans to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a manageScheduledPlans
    api_instance.add_manage_scheduled_plans_file(manage_scheduled_plans_id, file_name)
except ApiException as e:
    print("Exception when calling ManageScheduledPlansApi->add_manage_scheduled_plans_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manage_scheduled_plans_id** | **int**| Id of the manageScheduledPlans to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_manage_scheduled_plans_tag**
> add_manage_scheduled_plans_tag(manage_scheduled_plans_id, manage_scheduled_plans_tag)

Add new tags for a manageScheduledPlans.

Adds a tag to an existing manageScheduledPlans.

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
api_instance = Infoplus.ManageScheduledPlansApi(Infoplus.ApiClient(configuration))
manage_scheduled_plans_id = 56 # int | Id of the manageScheduledPlans to add a tag to
manage_scheduled_plans_tag = 'manage_scheduled_plans_tag_example' # str | The tag to add

try:
    # Add new tags for a manageScheduledPlans.
    api_instance.add_manage_scheduled_plans_tag(manage_scheduled_plans_id, manage_scheduled_plans_tag)
except ApiException as e:
    print("Exception when calling ManageScheduledPlansApi->add_manage_scheduled_plans_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manage_scheduled_plans_id** | **int**| Id of the manageScheduledPlans to add a tag to | 
 **manage_scheduled_plans_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_manage_scheduled_plans**
> delete_manage_scheduled_plans(manage_scheduled_plans_id)

Delete a manageScheduledPlans

Deletes the manageScheduledPlans identified by the specified id.

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
api_instance = Infoplus.ManageScheduledPlansApi(Infoplus.ApiClient(configuration))
manage_scheduled_plans_id = 56 # int | Id of the manageScheduledPlans to be deleted.

try:
    # Delete a manageScheduledPlans
    api_instance.delete_manage_scheduled_plans(manage_scheduled_plans_id)
except ApiException as e:
    print("Exception when calling ManageScheduledPlansApi->delete_manage_scheduled_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manage_scheduled_plans_id** | **int**| Id of the manageScheduledPlans to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_manage_scheduled_plans_tag**
> delete_manage_scheduled_plans_tag(manage_scheduled_plans_id, manage_scheduled_plans_tag)

Delete a tag for a manageScheduledPlans.

Deletes an existing manageScheduledPlans tag using the specified data.

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
api_instance = Infoplus.ManageScheduledPlansApi(Infoplus.ApiClient(configuration))
manage_scheduled_plans_id = 56 # int | Id of the manageScheduledPlans to remove tag from
manage_scheduled_plans_tag = 'manage_scheduled_plans_tag_example' # str | The tag to delete

try:
    # Delete a tag for a manageScheduledPlans.
    api_instance.delete_manage_scheduled_plans_tag(manage_scheduled_plans_id, manage_scheduled_plans_tag)
except ApiException as e:
    print("Exception when calling ManageScheduledPlansApi->delete_manage_scheduled_plans_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manage_scheduled_plans_id** | **int**| Id of the manageScheduledPlans to remove tag from | 
 **manage_scheduled_plans_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_manage_scheduled_plans_by_id**
> ManageScheduledPlans get_duplicate_manage_scheduled_plans_by_id(manage_scheduled_plans_id)

Get a duplicated a manageScheduledPlans by id

Returns a duplicated manageScheduledPlans identified by the specified id.

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
api_instance = Infoplus.ManageScheduledPlansApi(Infoplus.ApiClient(configuration))
manage_scheduled_plans_id = 56 # int | Id of the manageScheduledPlans to be duplicated.

try:
    # Get a duplicated a manageScheduledPlans by id
    api_response = api_instance.get_duplicate_manage_scheduled_plans_by_id(manage_scheduled_plans_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManageScheduledPlansApi->get_duplicate_manage_scheduled_plans_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manage_scheduled_plans_id** | **int**| Id of the manageScheduledPlans to be duplicated. | 

### Return type

[**ManageScheduledPlans**](ManageScheduledPlans.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manage_scheduled_plans_by_filter**
> list[ManageScheduledPlans] get_manage_scheduled_plans_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search manageScheduledPlanses by filter

Returns the list of manageScheduledPlanses that match the given filter.

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
api_instance = Infoplus.ManageScheduledPlansApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search manageScheduledPlanses by filter
    api_response = api_instance.get_manage_scheduled_plans_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManageScheduledPlansApi->get_manage_scheduled_plans_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[ManageScheduledPlans]**](ManageScheduledPlans.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manage_scheduled_plans_by_id**
> ManageScheduledPlans get_manage_scheduled_plans_by_id(manage_scheduled_plans_id)

Get a manageScheduledPlans by id

Returns the manageScheduledPlans identified by the specified id.

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
api_instance = Infoplus.ManageScheduledPlansApi(Infoplus.ApiClient(configuration))
manage_scheduled_plans_id = 56 # int | Id of the manageScheduledPlans to be returned.

try:
    # Get a manageScheduledPlans by id
    api_response = api_instance.get_manage_scheduled_plans_by_id(manage_scheduled_plans_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManageScheduledPlansApi->get_manage_scheduled_plans_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manage_scheduled_plans_id** | **int**| Id of the manageScheduledPlans to be returned. | 

### Return type

[**ManageScheduledPlans**](ManageScheduledPlans.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manage_scheduled_plans_tags**
> get_manage_scheduled_plans_tags(manage_scheduled_plans_id)

Get the tags for a manageScheduledPlans.

Get all existing manageScheduledPlans tags.

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
api_instance = Infoplus.ManageScheduledPlansApi(Infoplus.ApiClient(configuration))
manage_scheduled_plans_id = 56 # int | Id of the manageScheduledPlans to get tags for

try:
    # Get the tags for a manageScheduledPlans.
    api_instance.get_manage_scheduled_plans_tags(manage_scheduled_plans_id)
except ApiException as e:
    print("Exception when calling ManageScheduledPlansApi->get_manage_scheduled_plans_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manage_scheduled_plans_id** | **int**| Id of the manageScheduledPlans to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_manage_scheduled_plans**
> update_manage_scheduled_plans(body)

Update a manageScheduledPlans

Updates an existing manageScheduledPlans using the specified data.

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
api_instance = Infoplus.ManageScheduledPlansApi(Infoplus.ApiClient(configuration))
body = Infoplus.ManageScheduledPlans() # ManageScheduledPlans | ManageScheduledPlans to be updated.

try:
    # Update a manageScheduledPlans
    api_instance.update_manage_scheduled_plans(body)
except ApiException as e:
    print("Exception when calling ManageScheduledPlansApi->update_manage_scheduled_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManageScheduledPlans**](ManageScheduledPlans.md)| ManageScheduledPlans to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

