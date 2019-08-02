# Infoplus.FulfillmentLayoutPositionApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fulfillment_layout_position_audit**](FulfillmentLayoutPositionApi.md#add_fulfillment_layout_position_audit) | **PUT** /beta/fulfillmentLayoutPosition/{fulfillmentLayoutPositionId}/audit/{fulfillmentLayoutPositionAudit} | Add new audit for a fulfillmentLayoutPosition
[**add_fulfillment_layout_position_file**](FulfillmentLayoutPositionApi.md#add_fulfillment_layout_position_file) | **POST** /beta/fulfillmentLayoutPosition/{fulfillmentLayoutPositionId}/file/{fileName} | Attach a file to a fulfillmentLayoutPosition
[**add_fulfillment_layout_position_tag**](FulfillmentLayoutPositionApi.md#add_fulfillment_layout_position_tag) | **PUT** /beta/fulfillmentLayoutPosition/{fulfillmentLayoutPositionId}/tag/{fulfillmentLayoutPositionTag} | Add new tags for a fulfillmentLayoutPosition.
[**delete_fulfillment_layout_position_tag**](FulfillmentLayoutPositionApi.md#delete_fulfillment_layout_position_tag) | **DELETE** /beta/fulfillmentLayoutPosition/{fulfillmentLayoutPositionId}/tag/{fulfillmentLayoutPositionTag} | Delete a tag for a fulfillmentLayoutPosition.
[**get_duplicate_fulfillment_layout_position_by_id**](FulfillmentLayoutPositionApi.md#get_duplicate_fulfillment_layout_position_by_id) | **GET** /beta/fulfillmentLayoutPosition/duplicate/{fulfillmentLayoutPositionId} | Get a duplicated a fulfillmentLayoutPosition by id
[**get_fulfillment_layout_position_by_filter**](FulfillmentLayoutPositionApi.md#get_fulfillment_layout_position_by_filter) | **GET** /beta/fulfillmentLayoutPosition/search | Search fulfillmentLayoutPositions by filter
[**get_fulfillment_layout_position_by_id**](FulfillmentLayoutPositionApi.md#get_fulfillment_layout_position_by_id) | **GET** /beta/fulfillmentLayoutPosition/{fulfillmentLayoutPositionId} | Get a fulfillmentLayoutPosition by id
[**get_fulfillment_layout_position_tags**](FulfillmentLayoutPositionApi.md#get_fulfillment_layout_position_tags) | **GET** /beta/fulfillmentLayoutPosition/{fulfillmentLayoutPositionId}/tag | Get the tags for a fulfillmentLayoutPosition.


# **add_fulfillment_layout_position_audit**
> add_fulfillment_layout_position_audit(fulfillment_layout_position_id, fulfillment_layout_position_audit)

Add new audit for a fulfillmentLayoutPosition

Adds an audit to an existing fulfillmentLayoutPosition.

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
api_instance = Infoplus.FulfillmentLayoutPositionApi(Infoplus.ApiClient(configuration))
fulfillment_layout_position_id = 56 # int | Id of the fulfillmentLayoutPosition to add an audit to
fulfillment_layout_position_audit = 'fulfillment_layout_position_audit_example' # str | The audit to add

try:
    # Add new audit for a fulfillmentLayoutPosition
    api_instance.add_fulfillment_layout_position_audit(fulfillment_layout_position_id, fulfillment_layout_position_audit)
except ApiException as e:
    print("Exception when calling FulfillmentLayoutPositionApi->add_fulfillment_layout_position_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_layout_position_id** | **int**| Id of the fulfillmentLayoutPosition to add an audit to | 
 **fulfillment_layout_position_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_fulfillment_layout_position_file**
> add_fulfillment_layout_position_file(fulfillment_layout_position_id, file_name)

Attach a file to a fulfillmentLayoutPosition

Adds a file to an existing fulfillmentLayoutPosition.

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
api_instance = Infoplus.FulfillmentLayoutPositionApi(Infoplus.ApiClient(configuration))
fulfillment_layout_position_id = 56 # int | Id of the fulfillmentLayoutPosition to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a fulfillmentLayoutPosition
    api_instance.add_fulfillment_layout_position_file(fulfillment_layout_position_id, file_name)
except ApiException as e:
    print("Exception when calling FulfillmentLayoutPositionApi->add_fulfillment_layout_position_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_layout_position_id** | **int**| Id of the fulfillmentLayoutPosition to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_fulfillment_layout_position_tag**
> add_fulfillment_layout_position_tag(fulfillment_layout_position_id, fulfillment_layout_position_tag)

Add new tags for a fulfillmentLayoutPosition.

Adds a tag to an existing fulfillmentLayoutPosition.

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
api_instance = Infoplus.FulfillmentLayoutPositionApi(Infoplus.ApiClient(configuration))
fulfillment_layout_position_id = 56 # int | Id of the fulfillmentLayoutPosition to add a tag to
fulfillment_layout_position_tag = 'fulfillment_layout_position_tag_example' # str | The tag to add

try:
    # Add new tags for a fulfillmentLayoutPosition.
    api_instance.add_fulfillment_layout_position_tag(fulfillment_layout_position_id, fulfillment_layout_position_tag)
except ApiException as e:
    print("Exception when calling FulfillmentLayoutPositionApi->add_fulfillment_layout_position_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_layout_position_id** | **int**| Id of the fulfillmentLayoutPosition to add a tag to | 
 **fulfillment_layout_position_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fulfillment_layout_position_tag**
> delete_fulfillment_layout_position_tag(fulfillment_layout_position_id, fulfillment_layout_position_tag)

Delete a tag for a fulfillmentLayoutPosition.

Deletes an existing fulfillmentLayoutPosition tag using the specified data.

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
api_instance = Infoplus.FulfillmentLayoutPositionApi(Infoplus.ApiClient(configuration))
fulfillment_layout_position_id = 56 # int | Id of the fulfillmentLayoutPosition to remove tag from
fulfillment_layout_position_tag = 'fulfillment_layout_position_tag_example' # str | The tag to delete

try:
    # Delete a tag for a fulfillmentLayoutPosition.
    api_instance.delete_fulfillment_layout_position_tag(fulfillment_layout_position_id, fulfillment_layout_position_tag)
except ApiException as e:
    print("Exception when calling FulfillmentLayoutPositionApi->delete_fulfillment_layout_position_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_layout_position_id** | **int**| Id of the fulfillmentLayoutPosition to remove tag from | 
 **fulfillment_layout_position_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_fulfillment_layout_position_by_id**
> FulfillmentLayoutPosition get_duplicate_fulfillment_layout_position_by_id(fulfillment_layout_position_id)

Get a duplicated a fulfillmentLayoutPosition by id

Returns a duplicated fulfillmentLayoutPosition identified by the specified id.

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
api_instance = Infoplus.FulfillmentLayoutPositionApi(Infoplus.ApiClient(configuration))
fulfillment_layout_position_id = 56 # int | Id of the fulfillmentLayoutPosition to be duplicated.

try:
    # Get a duplicated a fulfillmentLayoutPosition by id
    api_response = api_instance.get_duplicate_fulfillment_layout_position_by_id(fulfillment_layout_position_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentLayoutPositionApi->get_duplicate_fulfillment_layout_position_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_layout_position_id** | **int**| Id of the fulfillmentLayoutPosition to be duplicated. | 

### Return type

[**FulfillmentLayoutPosition**](FulfillmentLayoutPosition.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_layout_position_by_filter**
> list[FulfillmentLayoutPosition] get_fulfillment_layout_position_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search fulfillmentLayoutPositions by filter

Returns the list of fulfillmentLayoutPositions that match the given filter.

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
api_instance = Infoplus.FulfillmentLayoutPositionApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search fulfillmentLayoutPositions by filter
    api_response = api_instance.get_fulfillment_layout_position_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentLayoutPositionApi->get_fulfillment_layout_position_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[FulfillmentLayoutPosition]**](FulfillmentLayoutPosition.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_layout_position_by_id**
> FulfillmentLayoutPosition get_fulfillment_layout_position_by_id(fulfillment_layout_position_id)

Get a fulfillmentLayoutPosition by id

Returns the fulfillmentLayoutPosition identified by the specified id.

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
api_instance = Infoplus.FulfillmentLayoutPositionApi(Infoplus.ApiClient(configuration))
fulfillment_layout_position_id = 56 # int | Id of the fulfillmentLayoutPosition to be returned.

try:
    # Get a fulfillmentLayoutPosition by id
    api_response = api_instance.get_fulfillment_layout_position_by_id(fulfillment_layout_position_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentLayoutPositionApi->get_fulfillment_layout_position_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_layout_position_id** | **int**| Id of the fulfillmentLayoutPosition to be returned. | 

### Return type

[**FulfillmentLayoutPosition**](FulfillmentLayoutPosition.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_layout_position_tags**
> get_fulfillment_layout_position_tags(fulfillment_layout_position_id)

Get the tags for a fulfillmentLayoutPosition.

Get all existing fulfillmentLayoutPosition tags.

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
api_instance = Infoplus.FulfillmentLayoutPositionApi(Infoplus.ApiClient(configuration))
fulfillment_layout_position_id = 56 # int | Id of the fulfillmentLayoutPosition to get tags for

try:
    # Get the tags for a fulfillmentLayoutPosition.
    api_instance.get_fulfillment_layout_position_tags(fulfillment_layout_position_id)
except ApiException as e:
    print("Exception when calling FulfillmentLayoutPositionApi->get_fulfillment_layout_position_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fulfillment_layout_position_id** | **int**| Id of the fulfillmentLayoutPosition to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

