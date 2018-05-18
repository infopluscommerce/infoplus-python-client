# Infoplus.SlaSetupApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_sla_setup_audit**](SlaSetupApi.md#add_sla_setup_audit) | **PUT** /beta/slaSetup/{slaSetupId}/audit/{slaSetupAudit} | Add new audit for a slaSetup
[**add_sla_setup_tag**](SlaSetupApi.md#add_sla_setup_tag) | **PUT** /beta/slaSetup/{slaSetupId}/tag/{slaSetupTag} | Add new tags for a slaSetup.
[**delete_sla_setup_tag**](SlaSetupApi.md#delete_sla_setup_tag) | **DELETE** /beta/slaSetup/{slaSetupId}/tag/{slaSetupTag} | Delete a tag for a slaSetup.
[**get_duplicate_sla_setup_by_id**](SlaSetupApi.md#get_duplicate_sla_setup_by_id) | **GET** /beta/slaSetup/duplicate/{slaSetupId} | Get a duplicated a slaSetup by id
[**get_sla_setup_by_filter**](SlaSetupApi.md#get_sla_setup_by_filter) | **GET** /beta/slaSetup/search | Search slaSetups by filter
[**get_sla_setup_by_id**](SlaSetupApi.md#get_sla_setup_by_id) | **GET** /beta/slaSetup/{slaSetupId} | Get a slaSetup by id
[**get_sla_setup_tags**](SlaSetupApi.md#get_sla_setup_tags) | **GET** /beta/slaSetup/{slaSetupId}/tag | Get the tags for a slaSetup.


# **add_sla_setup_audit**
> add_sla_setup_audit(sla_setup_id, sla_setup_audit)

Add new audit for a slaSetup

Adds an audit to an existing slaSetup.

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
api_instance = Infoplus.SlaSetupApi(Infoplus.ApiClient(configuration))
sla_setup_id = 56 # int | Id of the slaSetup to add an audit to
sla_setup_audit = 'sla_setup_audit_example' # str | The audit to add

try:
    # Add new audit for a slaSetup
    api_instance.add_sla_setup_audit(sla_setup_id, sla_setup_audit)
except ApiException as e:
    print("Exception when calling SlaSetupApi->add_sla_setup_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_setup_id** | **int**| Id of the slaSetup to add an audit to | 
 **sla_setup_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_sla_setup_tag**
> add_sla_setup_tag(sla_setup_id, sla_setup_tag)

Add new tags for a slaSetup.

Adds a tag to an existing slaSetup.

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
api_instance = Infoplus.SlaSetupApi(Infoplus.ApiClient(configuration))
sla_setup_id = 56 # int | Id of the slaSetup to add a tag to
sla_setup_tag = 'sla_setup_tag_example' # str | The tag to add

try:
    # Add new tags for a slaSetup.
    api_instance.add_sla_setup_tag(sla_setup_id, sla_setup_tag)
except ApiException as e:
    print("Exception when calling SlaSetupApi->add_sla_setup_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_setup_id** | **int**| Id of the slaSetup to add a tag to | 
 **sla_setup_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sla_setup_tag**
> delete_sla_setup_tag(sla_setup_id, sla_setup_tag)

Delete a tag for a slaSetup.

Deletes an existing slaSetup tag using the specified data.

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
api_instance = Infoplus.SlaSetupApi(Infoplus.ApiClient(configuration))
sla_setup_id = 56 # int | Id of the slaSetup to remove tag from
sla_setup_tag = 'sla_setup_tag_example' # str | The tag to delete

try:
    # Delete a tag for a slaSetup.
    api_instance.delete_sla_setup_tag(sla_setup_id, sla_setup_tag)
except ApiException as e:
    print("Exception when calling SlaSetupApi->delete_sla_setup_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_setup_id** | **int**| Id of the slaSetup to remove tag from | 
 **sla_setup_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_sla_setup_by_id**
> SlaSetup get_duplicate_sla_setup_by_id(sla_setup_id)

Get a duplicated a slaSetup by id

Returns a duplicated slaSetup identified by the specified id.

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
api_instance = Infoplus.SlaSetupApi(Infoplus.ApiClient(configuration))
sla_setup_id = 56 # int | Id of the slaSetup to be duplicated.

try:
    # Get a duplicated a slaSetup by id
    api_response = api_instance.get_duplicate_sla_setup_by_id(sla_setup_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlaSetupApi->get_duplicate_sla_setup_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_setup_id** | **int**| Id of the slaSetup to be duplicated. | 

### Return type

[**SlaSetup**](SlaSetup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sla_setup_by_filter**
> list[SlaSetup] get_sla_setup_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search slaSetups by filter

Returns the list of slaSetups that match the given filter.

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
api_instance = Infoplus.SlaSetupApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search slaSetups by filter
    api_response = api_instance.get_sla_setup_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlaSetupApi->get_sla_setup_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[SlaSetup]**](SlaSetup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sla_setup_by_id**
> SlaSetup get_sla_setup_by_id(sla_setup_id)

Get a slaSetup by id

Returns the slaSetup identified by the specified id.

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
api_instance = Infoplus.SlaSetupApi(Infoplus.ApiClient(configuration))
sla_setup_id = 56 # int | Id of the slaSetup to be returned.

try:
    # Get a slaSetup by id
    api_response = api_instance.get_sla_setup_by_id(sla_setup_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlaSetupApi->get_sla_setup_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_setup_id** | **int**| Id of the slaSetup to be returned. | 

### Return type

[**SlaSetup**](SlaSetup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sla_setup_tags**
> get_sla_setup_tags(sla_setup_id)

Get the tags for a slaSetup.

Get all existing slaSetup tags.

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
api_instance = Infoplus.SlaSetupApi(Infoplus.ApiClient(configuration))
sla_setup_id = 56 # int | Id of the slaSetup to get tags for

try:
    # Get the tags for a slaSetup.
    api_instance.get_sla_setup_tags(sla_setup_id)
except ApiException as e:
    print("Exception when calling SlaSetupApi->get_sla_setup_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_setup_id** | **int**| Id of the slaSetup to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

