# Infoplus.BillingCodeActivityApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_billing_code_activity**](BillingCodeActivityApi.md#add_billing_code_activity) | **POST** /beta/billingCodeActivity | Create a billingCodeActivity
[**add_billing_code_activity_audit**](BillingCodeActivityApi.md#add_billing_code_activity_audit) | **PUT** /beta/billingCodeActivity/{billingCodeActivityId}/audit/{billingCodeActivityAudit} | Add new audit for a billingCodeActivity
[**add_billing_code_activity_tag**](BillingCodeActivityApi.md#add_billing_code_activity_tag) | **PUT** /beta/billingCodeActivity/{billingCodeActivityId}/tag/{billingCodeActivityTag} | Add new tags for a billingCodeActivity.
[**delete_billing_code_activity**](BillingCodeActivityApi.md#delete_billing_code_activity) | **DELETE** /beta/billingCodeActivity/{billingCodeActivityId} | Delete a billingCodeActivity
[**delete_billing_code_activity_tag**](BillingCodeActivityApi.md#delete_billing_code_activity_tag) | **DELETE** /beta/billingCodeActivity/{billingCodeActivityId}/tag/{billingCodeActivityTag} | Delete a tag for a billingCodeActivity.
[**get_billing_code_activity_by_filter**](BillingCodeActivityApi.md#get_billing_code_activity_by_filter) | **GET** /beta/billingCodeActivity/search | Search billingCodeActivitys by filter
[**get_billing_code_activity_by_id**](BillingCodeActivityApi.md#get_billing_code_activity_by_id) | **GET** /beta/billingCodeActivity/{billingCodeActivityId} | Get a billingCodeActivity by id
[**get_billing_code_activity_tags**](BillingCodeActivityApi.md#get_billing_code_activity_tags) | **GET** /beta/billingCodeActivity/{billingCodeActivityId}/tag | Get the tags for a billingCodeActivity.
[**get_duplicate_billing_code_activity_by_id**](BillingCodeActivityApi.md#get_duplicate_billing_code_activity_by_id) | **GET** /beta/billingCodeActivity/duplicate/{billingCodeActivityId} | Get a duplicated a billingCodeActivity by id
[**update_billing_code_activity**](BillingCodeActivityApi.md#update_billing_code_activity) | **PUT** /beta/billingCodeActivity | Update a billingCodeActivity


# **add_billing_code_activity**
> BillingCodeActivity add_billing_code_activity(body)

Create a billingCodeActivity

Inserts a new billingCodeActivity using the specified data.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.BillingCodeActivity() # BillingCodeActivity | BillingCodeActivity to be inserted.

try:
    # Create a billingCodeActivity
    api_response = api_instance.add_billing_code_activity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->add_billing_code_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingCodeActivity**](BillingCodeActivity.md)| BillingCodeActivity to be inserted. | 

### Return type

[**BillingCodeActivity**](BillingCodeActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_billing_code_activity_audit**
> add_billing_code_activity_audit(billing_code_activity_id, billing_code_activity_audit)

Add new audit for a billingCodeActivity

Adds an audit to an existing billingCodeActivity.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to add an audit to
billing_code_activity_audit = 'billing_code_activity_audit_example' # str | The audit to add

try:
    # Add new audit for a billingCodeActivity
    api_instance.add_billing_code_activity_audit(billing_code_activity_id, billing_code_activity_audit)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->add_billing_code_activity_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to add an audit to | 
 **billing_code_activity_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_billing_code_activity_tag**
> add_billing_code_activity_tag(billing_code_activity_id, billing_code_activity_tag)

Add new tags for a billingCodeActivity.

Adds a tag to an existing billingCodeActivity.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to add a tag to
billing_code_activity_tag = 'billing_code_activity_tag_example' # str | The tag to add

try:
    # Add new tags for a billingCodeActivity.
    api_instance.add_billing_code_activity_tag(billing_code_activity_id, billing_code_activity_tag)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->add_billing_code_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to add a tag to | 
 **billing_code_activity_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_code_activity**
> delete_billing_code_activity(billing_code_activity_id)

Delete a billingCodeActivity

Deletes the billingCodeActivity identified by the specified id.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to be deleted.

try:
    # Delete a billingCodeActivity
    api_instance.delete_billing_code_activity(billing_code_activity_id)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->delete_billing_code_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_code_activity_tag**
> delete_billing_code_activity_tag(billing_code_activity_id, billing_code_activity_tag)

Delete a tag for a billingCodeActivity.

Deletes an existing billingCodeActivity tag using the specified data.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to remove tag from
billing_code_activity_tag = 'billing_code_activity_tag_example' # str | The tag to delete

try:
    # Delete a tag for a billingCodeActivity.
    api_instance.delete_billing_code_activity_tag(billing_code_activity_id, billing_code_activity_tag)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->delete_billing_code_activity_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to remove tag from | 
 **billing_code_activity_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_code_activity_by_filter**
> list[BillingCodeActivity] get_billing_code_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search billingCodeActivitys by filter

Returns the list of billingCodeActivitys that match the given filter.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search billingCodeActivitys by filter
    api_response = api_instance.get_billing_code_activity_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->get_billing_code_activity_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[BillingCodeActivity]**](BillingCodeActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_code_activity_by_id**
> BillingCodeActivity get_billing_code_activity_by_id(billing_code_activity_id)

Get a billingCodeActivity by id

Returns the billingCodeActivity identified by the specified id.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to be returned.

try:
    # Get a billingCodeActivity by id
    api_response = api_instance.get_billing_code_activity_by_id(billing_code_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->get_billing_code_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to be returned. | 

### Return type

[**BillingCodeActivity**](BillingCodeActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_code_activity_tags**
> get_billing_code_activity_tags(billing_code_activity_id)

Get the tags for a billingCodeActivity.

Get all existing billingCodeActivity tags.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to get tags for

try:
    # Get the tags for a billingCodeActivity.
    api_instance.get_billing_code_activity_tags(billing_code_activity_id)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->get_billing_code_activity_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_billing_code_activity_by_id**
> BillingCodeActivity get_duplicate_billing_code_activity_by_id(billing_code_activity_id)

Get a duplicated a billingCodeActivity by id

Returns a duplicated billingCodeActivity identified by the specified id.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
billing_code_activity_id = 56 # int | Id of the billingCodeActivity to be duplicated.

try:
    # Get a duplicated a billingCodeActivity by id
    api_response = api_instance.get_duplicate_billing_code_activity_by_id(billing_code_activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->get_duplicate_billing_code_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_code_activity_id** | **int**| Id of the billingCodeActivity to be duplicated. | 

### Return type

[**BillingCodeActivity**](BillingCodeActivity.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_code_activity**
> update_billing_code_activity(body)

Update a billingCodeActivity

Updates an existing billingCodeActivity using the specified data.

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
api_instance = Infoplus.BillingCodeActivityApi(Infoplus.ApiClient(configuration))
body = Infoplus.BillingCodeActivity() # BillingCodeActivity | BillingCodeActivity to be updated.

try:
    # Update a billingCodeActivity
    api_instance.update_billing_code_activity(body)
except ApiException as e:
    print("Exception when calling BillingCodeActivityApi->update_billing_code_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingCodeActivity**](BillingCodeActivity.md)| BillingCodeActivity to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

