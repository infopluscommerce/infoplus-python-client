# Infoplus.CommodityCodeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_commodity_code_audit**](CommodityCodeApi.md#add_commodity_code_audit) | **PUT** /beta/commodityCode/{commodityCodeId}/audit/{commodityCodeAudit} | Add new audit for a commodityCode
[**add_commodity_code_file**](CommodityCodeApi.md#add_commodity_code_file) | **POST** /beta/commodityCode/{commodityCodeId}/file/{fileName} | Attach a file to a commodityCode
[**add_commodity_code_file_by_url**](CommodityCodeApi.md#add_commodity_code_file_by_url) | **POST** /beta/commodityCode/{commodityCodeId}/file | Attach a file to a commodityCode by URL.
[**add_commodity_code_tag**](CommodityCodeApi.md#add_commodity_code_tag) | **PUT** /beta/commodityCode/{commodityCodeId}/tag/{commodityCodeTag} | Add new tags for a commodityCode.
[**delete_commodity_code_file**](CommodityCodeApi.md#delete_commodity_code_file) | **DELETE** /beta/commodityCode/{commodityCodeId}/file/{fileId} | Delete a file for a commodityCode.
[**delete_commodity_code_tag**](CommodityCodeApi.md#delete_commodity_code_tag) | **DELETE** /beta/commodityCode/{commodityCodeId}/tag/{commodityCodeTag} | Delete a tag for a commodityCode.
[**get_commodity_code_by_filter**](CommodityCodeApi.md#get_commodity_code_by_filter) | **GET** /beta/commodityCode/search | Search commodityCodes by filter
[**get_commodity_code_by_id**](CommodityCodeApi.md#get_commodity_code_by_id) | **GET** /beta/commodityCode/{commodityCodeId} | Get a commodityCode by id
[**get_commodity_code_files**](CommodityCodeApi.md#get_commodity_code_files) | **GET** /beta/commodityCode/{commodityCodeId}/file | Get the files for a commodityCode.
[**get_commodity_code_tags**](CommodityCodeApi.md#get_commodity_code_tags) | **GET** /beta/commodityCode/{commodityCodeId}/tag | Get the tags for a commodityCode.
[**get_duplicate_commodity_code_by_id**](CommodityCodeApi.md#get_duplicate_commodity_code_by_id) | **GET** /beta/commodityCode/duplicate/{commodityCodeId} | Get a duplicated a commodityCode by id


# **add_commodity_code_audit**
> add_commodity_code_audit(commodity_code_id, commodity_code_audit)

Add new audit for a commodityCode

Adds an audit to an existing commodityCode.

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
api_instance = Infoplus.CommodityCodeApi(Infoplus.ApiClient(configuration))
commodity_code_id = 56 # int | Id of the commodityCode to add an audit to
commodity_code_audit = 'commodity_code_audit_example' # str | The audit to add

try:
    # Add new audit for a commodityCode
    api_instance.add_commodity_code_audit(commodity_code_id, commodity_code_audit)
except ApiException as e:
    print("Exception when calling CommodityCodeApi->add_commodity_code_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commodity_code_id** | **int**| Id of the commodityCode to add an audit to | 
 **commodity_code_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_commodity_code_file**
> add_commodity_code_file(commodity_code_id, file_name)

Attach a file to a commodityCode

Adds a file to an existing commodityCode.

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
api_instance = Infoplus.CommodityCodeApi(Infoplus.ApiClient(configuration))
commodity_code_id = 56 # int | Id of the commodityCode to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a commodityCode
    api_instance.add_commodity_code_file(commodity_code_id, file_name)
except ApiException as e:
    print("Exception when calling CommodityCodeApi->add_commodity_code_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commodity_code_id** | **int**| Id of the commodityCode to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_commodity_code_file_by_url**
> add_commodity_code_file_by_url(body, commodity_code_id)

Attach a file to a commodityCode by URL.

Adds a file to an existing commodityCode by URL.

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
api_instance = Infoplus.CommodityCodeApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
commodity_code_id = 56 # int | Id of the commodityCode to add an file to

try:
    # Attach a file to a commodityCode by URL.
    api_instance.add_commodity_code_file_by_url(body, commodity_code_id)
except ApiException as e:
    print("Exception when calling CommodityCodeApi->add_commodity_code_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **commodity_code_id** | **int**| Id of the commodityCode to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_commodity_code_tag**
> add_commodity_code_tag(commodity_code_id, commodity_code_tag)

Add new tags for a commodityCode.

Adds a tag to an existing commodityCode.

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
api_instance = Infoplus.CommodityCodeApi(Infoplus.ApiClient(configuration))
commodity_code_id = 56 # int | Id of the commodityCode to add a tag to
commodity_code_tag = 'commodity_code_tag_example' # str | The tag to add

try:
    # Add new tags for a commodityCode.
    api_instance.add_commodity_code_tag(commodity_code_id, commodity_code_tag)
except ApiException as e:
    print("Exception when calling CommodityCodeApi->add_commodity_code_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commodity_code_id** | **int**| Id of the commodityCode to add a tag to | 
 **commodity_code_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_commodity_code_file**
> delete_commodity_code_file(commodity_code_id, file_id)

Delete a file for a commodityCode.

Deletes an existing commodityCode file using the specified data.

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
api_instance = Infoplus.CommodityCodeApi(Infoplus.ApiClient(configuration))
commodity_code_id = 56 # int | Id of the commodityCode to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a commodityCode.
    api_instance.delete_commodity_code_file(commodity_code_id, file_id)
except ApiException as e:
    print("Exception when calling CommodityCodeApi->delete_commodity_code_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commodity_code_id** | **int**| Id of the commodityCode to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_commodity_code_tag**
> delete_commodity_code_tag(commodity_code_id, commodity_code_tag)

Delete a tag for a commodityCode.

Deletes an existing commodityCode tag using the specified data.

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
api_instance = Infoplus.CommodityCodeApi(Infoplus.ApiClient(configuration))
commodity_code_id = 56 # int | Id of the commodityCode to remove tag from
commodity_code_tag = 'commodity_code_tag_example' # str | The tag to delete

try:
    # Delete a tag for a commodityCode.
    api_instance.delete_commodity_code_tag(commodity_code_id, commodity_code_tag)
except ApiException as e:
    print("Exception when calling CommodityCodeApi->delete_commodity_code_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commodity_code_id** | **int**| Id of the commodityCode to remove tag from | 
 **commodity_code_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commodity_code_by_filter**
> list[CommodityCode] get_commodity_code_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search commodityCodes by filter

Returns the list of commodityCodes that match the given filter.

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
api_instance = Infoplus.CommodityCodeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search commodityCodes by filter
    api_response = api_instance.get_commodity_code_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommodityCodeApi->get_commodity_code_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[CommodityCode]**](CommodityCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commodity_code_by_id**
> CommodityCode get_commodity_code_by_id(commodity_code_id)

Get a commodityCode by id

Returns the commodityCode identified by the specified id.

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
api_instance = Infoplus.CommodityCodeApi(Infoplus.ApiClient(configuration))
commodity_code_id = 56 # int | Id of the commodityCode to be returned.

try:
    # Get a commodityCode by id
    api_response = api_instance.get_commodity_code_by_id(commodity_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommodityCodeApi->get_commodity_code_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commodity_code_id** | **int**| Id of the commodityCode to be returned. | 

### Return type

[**CommodityCode**](CommodityCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commodity_code_files**
> get_commodity_code_files(commodity_code_id)

Get the files for a commodityCode.

Get all existing commodityCode files.

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
api_instance = Infoplus.CommodityCodeApi(Infoplus.ApiClient(configuration))
commodity_code_id = 56 # int | Id of the commodityCode to get files for

try:
    # Get the files for a commodityCode.
    api_instance.get_commodity_code_files(commodity_code_id)
except ApiException as e:
    print("Exception when calling CommodityCodeApi->get_commodity_code_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commodity_code_id** | **int**| Id of the commodityCode to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commodity_code_tags**
> get_commodity_code_tags(commodity_code_id)

Get the tags for a commodityCode.

Get all existing commodityCode tags.

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
api_instance = Infoplus.CommodityCodeApi(Infoplus.ApiClient(configuration))
commodity_code_id = 56 # int | Id of the commodityCode to get tags for

try:
    # Get the tags for a commodityCode.
    api_instance.get_commodity_code_tags(commodity_code_id)
except ApiException as e:
    print("Exception when calling CommodityCodeApi->get_commodity_code_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commodity_code_id** | **int**| Id of the commodityCode to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_commodity_code_by_id**
> CommodityCode get_duplicate_commodity_code_by_id(commodity_code_id)

Get a duplicated a commodityCode by id

Returns a duplicated commodityCode identified by the specified id.

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
api_instance = Infoplus.CommodityCodeApi(Infoplus.ApiClient(configuration))
commodity_code_id = 56 # int | Id of the commodityCode to be duplicated.

try:
    # Get a duplicated a commodityCode by id
    api_response = api_instance.get_duplicate_commodity_code_by_id(commodity_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommodityCodeApi->get_duplicate_commodity_code_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commodity_code_id** | **int**| Id of the commodityCode to be duplicated. | 

### Return type

[**CommodityCode**](CommodityCode.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

