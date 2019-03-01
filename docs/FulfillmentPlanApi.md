# Infoplus.FulfillmentPlanApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fulfillment_plan**](FulfillmentPlanApi.md#add_fulfillment_plan) | **POST** /beta/fulfillmentPlan | Create a fulfillmentPlan
[**add_fulfillment_plan_audit**](FulfillmentPlanApi.md#add_fulfillment_plan_audit) | **PUT** /beta/fulfillmentPlan/{fulfillmentPlanId}/audit/{fulfillmentPlanAudit} | Add new audit for a fulfillmentPlan
[**add_fulfillment_plan_file**](FulfillmentPlanApi.md#add_fulfillment_plan_file) | **POST** /beta/fulfillmentPlan/{fulfillmentPlanId}/file/{fileName} | Attach a file to a fulfillmentPlan
[**add_fulfillment_plan_tag**](FulfillmentPlanApi.md#add_fulfillment_plan_tag) | **PUT** /beta/fulfillmentPlan/{fulfillmentPlanId}/tag/{fulfillmentPlanTag} | Add new tags for a fulfillmentPlan.
[**delete_fulfillment_plan**](FulfillmentPlanApi.md#delete_fulfillment_plan) | **DELETE** /beta/fulfillmentPlan/{fulfillmentPlanId} | Delete a fulfillmentPlan
[**delete_fulfillment_plan_tag**](FulfillmentPlanApi.md#delete_fulfillment_plan_tag) | **DELETE** /beta/fulfillmentPlan/{fulfillmentPlanId}/tag/{fulfillmentPlanTag} | Delete a tag for a fulfillmentPlan.
[**get_duplicate_fulfillment_plan_by_id**](FulfillmentPlanApi.md#get_duplicate_fulfillment_plan_by_id) | **GET** /beta/fulfillmentPlan/duplicate/{fulfillmentPlanId} | Get a duplicated a fulfillmentPlan by id
[**get_fulfillment_plan_by_filter**](FulfillmentPlanApi.md#get_fulfillment_plan_by_filter) | **GET** /beta/fulfillmentPlan/search | Search fulfillmentPlans by filter
[**get_fulfillment_plan_by_id**](FulfillmentPlanApi.md#get_fulfillment_plan_by_id) | **GET** /beta/fulfillmentPlan/{fulfillmentPlanId} | Get a fulfillmentPlan by id
[**get_fulfillment_plan_tags**](FulfillmentPlanApi.md#get_fulfillment_plan_tags) | **GET** /beta/fulfillmentPlan/{fulfillmentPlanId}/tag | Get the tags for a fulfillmentPlan.
[**update_fulfillment_plan**](FulfillmentPlanApi.md#update_fulfillment_plan) | **PUT** /beta/fulfillmentPlan | Update a fulfillmentPlan
[**update_fulfillment_plan_custom_fields**](FulfillmentPlanApi.md#update_fulfillment_plan_custom_fields) | **PUT** /beta/fulfillmentPlan/customFields | Update a fulfillmentPlan custom fields


# **add_fulfillment_plan**
> FulfillmentPlan add_fulfillment_plan(body)

Create a fulfillmentPlan

Inserts a new fulfillmentPlan using the specified data.

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
api_instance = Infoplus.FulfillmentPlanApi(Infoplus.ApiClient(configuration))
body = Infoplus.FulfillmentPlan() # FulfillmentPlan | FulfillmentPlan to be inserted.

try:
    # Create a fulfillmentPlan
    api_response = api_instance.add_fulfillment_plan(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentPlanApi->add_fulfillment_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FulfillmentPlan**](FulfillmentPlan.md)| FulfillmentPlan to be inserted. | 

### Return type

[**FulfillmentPlan**](FulfillmentPlan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_fulfillment_plan_audit**
> add_fulfillment_plan_audit(fulfillment_plan_id, fulfillment_plan_audit)

Add new audit for a fulfillmentPlan

Adds an audit to an existing fulfillmentPlan.

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
api_instance = Infoplus.FulfillmentPlanApi(Infoplus.ApiClient(configuration))
fulfillment_plan_id = 56 # int | Id of the fulfillmentPlan to add an audit to
fulfillment_plan_audit = 'fulfillment_plan_audit_example' # str | The audit to add

try:
    # Add new audit for a fulfillmentPlan
    api_instance.add_fulfillment_plan_audit(fulfillment_plan_id, fulfillment_plan_audit)
except ApiException as e:
    print("Exception when calling FulfillmentPlanApi->add_fulfillment_plan_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_plan_id** | **int**| Id of the fulfillmentPlan to add an audit to | 
 **fulfillment_plan_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_fulfillment_plan_file**
> add_fulfillment_plan_file(fulfillment_plan_id, file_name)

Attach a file to a fulfillmentPlan

Adds a file to an existing fulfillmentPlan.

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
api_instance = Infoplus.FulfillmentPlanApi(Infoplus.ApiClient(configuration))
fulfillment_plan_id = 56 # int | Id of the fulfillmentPlan to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a fulfillmentPlan
    api_instance.add_fulfillment_plan_file(fulfillment_plan_id, file_name)
except ApiException as e:
    print("Exception when calling FulfillmentPlanApi->add_fulfillment_plan_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_plan_id** | **int**| Id of the fulfillmentPlan to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_fulfillment_plan_tag**
> add_fulfillment_plan_tag(fulfillment_plan_id, fulfillment_plan_tag)

Add new tags for a fulfillmentPlan.

Adds a tag to an existing fulfillmentPlan.

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
api_instance = Infoplus.FulfillmentPlanApi(Infoplus.ApiClient(configuration))
fulfillment_plan_id = 56 # int | Id of the fulfillmentPlan to add a tag to
fulfillment_plan_tag = 'fulfillment_plan_tag_example' # str | The tag to add

try:
    # Add new tags for a fulfillmentPlan.
    api_instance.add_fulfillment_plan_tag(fulfillment_plan_id, fulfillment_plan_tag)
except ApiException as e:
    print("Exception when calling FulfillmentPlanApi->add_fulfillment_plan_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_plan_id** | **int**| Id of the fulfillmentPlan to add a tag to | 
 **fulfillment_plan_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fulfillment_plan**
> delete_fulfillment_plan(fulfillment_plan_id)

Delete a fulfillmentPlan

Deletes the fulfillmentPlan identified by the specified id.

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
api_instance = Infoplus.FulfillmentPlanApi(Infoplus.ApiClient(configuration))
fulfillment_plan_id = 56 # int | Id of the fulfillmentPlan to be deleted.

try:
    # Delete a fulfillmentPlan
    api_instance.delete_fulfillment_plan(fulfillment_plan_id)
except ApiException as e:
    print("Exception when calling FulfillmentPlanApi->delete_fulfillment_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_plan_id** | **int**| Id of the fulfillmentPlan to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fulfillment_plan_tag**
> delete_fulfillment_plan_tag(fulfillment_plan_id, fulfillment_plan_tag)

Delete a tag for a fulfillmentPlan.

Deletes an existing fulfillmentPlan tag using the specified data.

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
api_instance = Infoplus.FulfillmentPlanApi(Infoplus.ApiClient(configuration))
fulfillment_plan_id = 56 # int | Id of the fulfillmentPlan to remove tag from
fulfillment_plan_tag = 'fulfillment_plan_tag_example' # str | The tag to delete

try:
    # Delete a tag for a fulfillmentPlan.
    api_instance.delete_fulfillment_plan_tag(fulfillment_plan_id, fulfillment_plan_tag)
except ApiException as e:
    print("Exception when calling FulfillmentPlanApi->delete_fulfillment_plan_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_plan_id** | **int**| Id of the fulfillmentPlan to remove tag from | 
 **fulfillment_plan_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_fulfillment_plan_by_id**
> FulfillmentPlan get_duplicate_fulfillment_plan_by_id(fulfillment_plan_id)

Get a duplicated a fulfillmentPlan by id

Returns a duplicated fulfillmentPlan identified by the specified id.

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
api_instance = Infoplus.FulfillmentPlanApi(Infoplus.ApiClient(configuration))
fulfillment_plan_id = 56 # int | Id of the fulfillmentPlan to be duplicated.

try:
    # Get a duplicated a fulfillmentPlan by id
    api_response = api_instance.get_duplicate_fulfillment_plan_by_id(fulfillment_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentPlanApi->get_duplicate_fulfillment_plan_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_plan_id** | **int**| Id of the fulfillmentPlan to be duplicated. | 

### Return type

[**FulfillmentPlan**](FulfillmentPlan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_plan_by_filter**
> list[FulfillmentPlan] get_fulfillment_plan_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search fulfillmentPlans by filter

Returns the list of fulfillmentPlans that match the given filter.

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
api_instance = Infoplus.FulfillmentPlanApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search fulfillmentPlans by filter
    api_response = api_instance.get_fulfillment_plan_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentPlanApi->get_fulfillment_plan_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[FulfillmentPlan]**](FulfillmentPlan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_plan_by_id**
> FulfillmentPlan get_fulfillment_plan_by_id(fulfillment_plan_id)

Get a fulfillmentPlan by id

Returns the fulfillmentPlan identified by the specified id.

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
api_instance = Infoplus.FulfillmentPlanApi(Infoplus.ApiClient(configuration))
fulfillment_plan_id = 56 # int | Id of the fulfillmentPlan to be returned.

try:
    # Get a fulfillmentPlan by id
    api_response = api_instance.get_fulfillment_plan_by_id(fulfillment_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentPlanApi->get_fulfillment_plan_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_plan_id** | **int**| Id of the fulfillmentPlan to be returned. | 

### Return type

[**FulfillmentPlan**](FulfillmentPlan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_plan_tags**
> get_fulfillment_plan_tags(fulfillment_plan_id)

Get the tags for a fulfillmentPlan.

Get all existing fulfillmentPlan tags.

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
api_instance = Infoplus.FulfillmentPlanApi(Infoplus.ApiClient(configuration))
fulfillment_plan_id = 56 # int | Id of the fulfillmentPlan to get tags for

try:
    # Get the tags for a fulfillmentPlan.
    api_instance.get_fulfillment_plan_tags(fulfillment_plan_id)
except ApiException as e:
    print("Exception when calling FulfillmentPlanApi->get_fulfillment_plan_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_plan_id** | **int**| Id of the fulfillmentPlan to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fulfillment_plan**
> update_fulfillment_plan(body)

Update a fulfillmentPlan

Updates an existing fulfillmentPlan using the specified data.

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
api_instance = Infoplus.FulfillmentPlanApi(Infoplus.ApiClient(configuration))
body = Infoplus.FulfillmentPlan() # FulfillmentPlan | FulfillmentPlan to be updated.

try:
    # Update a fulfillmentPlan
    api_instance.update_fulfillment_plan(body)
except ApiException as e:
    print("Exception when calling FulfillmentPlanApi->update_fulfillment_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FulfillmentPlan**](FulfillmentPlan.md)| FulfillmentPlan to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fulfillment_plan_custom_fields**
> update_fulfillment_plan_custom_fields(body)

Update a fulfillmentPlan custom fields

Updates an existing fulfillmentPlan custom fields using the specified data.

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
api_instance = Infoplus.FulfillmentPlanApi(Infoplus.ApiClient(configuration))
body = Infoplus.FulfillmentPlan() # FulfillmentPlan | FulfillmentPlan to be updated.

try:
    # Update a fulfillmentPlan custom fields
    api_instance.update_fulfillment_plan_custom_fields(body)
except ApiException as e:
    print("Exception when calling FulfillmentPlanApi->update_fulfillment_plan_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FulfillmentPlan**](FulfillmentPlan.md)| FulfillmentPlan to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

