# Infoplus.RateCardApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_rate_card**](RateCardApi.md#add_rate_card) | **POST** /beta/rateCard | Create a rateCard
[**add_rate_card_audit**](RateCardApi.md#add_rate_card_audit) | **PUT** /beta/rateCard/{rateCardId}/audit/{rateCardAudit} | Add new audit for a rateCard
[**add_rate_card_file**](RateCardApi.md#add_rate_card_file) | **POST** /beta/rateCard/{rateCardId}/file/{fileName} | Attach a file to a rateCard
[**add_rate_card_file_by_url**](RateCardApi.md#add_rate_card_file_by_url) | **POST** /beta/rateCard/{rateCardId}/file | Attach a file to a rateCard by URL.
[**add_rate_card_tag**](RateCardApi.md#add_rate_card_tag) | **PUT** /beta/rateCard/{rateCardId}/tag/{rateCardTag} | Add new tags for a rateCard.
[**delete_rate_card**](RateCardApi.md#delete_rate_card) | **DELETE** /beta/rateCard/{rateCardId} | Delete a rateCard
[**delete_rate_card_file**](RateCardApi.md#delete_rate_card_file) | **DELETE** /beta/rateCard/{rateCardId}/file/{fileId} | Delete a file for a rateCard.
[**delete_rate_card_tag**](RateCardApi.md#delete_rate_card_tag) | **DELETE** /beta/rateCard/{rateCardId}/tag/{rateCardTag} | Delete a tag for a rateCard.
[**get_duplicate_rate_card_by_id**](RateCardApi.md#get_duplicate_rate_card_by_id) | **GET** /beta/rateCard/duplicate/{rateCardId} | Get a duplicated a rateCard by id
[**get_rate_card_by_filter**](RateCardApi.md#get_rate_card_by_filter) | **GET** /beta/rateCard/search | Search rateCards by filter
[**get_rate_card_by_id**](RateCardApi.md#get_rate_card_by_id) | **GET** /beta/rateCard/{rateCardId} | Get a rateCard by id
[**get_rate_card_files**](RateCardApi.md#get_rate_card_files) | **GET** /beta/rateCard/{rateCardId}/file | Get the files for a rateCard.
[**get_rate_card_tags**](RateCardApi.md#get_rate_card_tags) | **GET** /beta/rateCard/{rateCardId}/tag | Get the tags for a rateCard.
[**update_rate_card**](RateCardApi.md#update_rate_card) | **PUT** /beta/rateCard | Update a rateCard


# **add_rate_card**
> RateCard add_rate_card(body)

Create a rateCard

Inserts a new rateCard using the specified data.

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
api_instance = Infoplus.RateCardApi(Infoplus.ApiClient(configuration))
body = Infoplus.RateCard() # RateCard | RateCard to be inserted.

try:
    # Create a rateCard
    api_response = api_instance.add_rate_card(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RateCardApi->add_rate_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RateCard**](RateCard.md)| RateCard to be inserted. | 

### Return type

[**RateCard**](RateCard.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_rate_card_audit**
> add_rate_card_audit(rate_card_id, rate_card_audit)

Add new audit for a rateCard

Adds an audit to an existing rateCard.

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
api_instance = Infoplus.RateCardApi(Infoplus.ApiClient(configuration))
rate_card_id = 56 # int | Id of the rateCard to add an audit to
rate_card_audit = 'rate_card_audit_example' # str | The audit to add

try:
    # Add new audit for a rateCard
    api_instance.add_rate_card_audit(rate_card_id, rate_card_audit)
except ApiException as e:
    print("Exception when calling RateCardApi->add_rate_card_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_card_id** | **int**| Id of the rateCard to add an audit to | 
 **rate_card_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_rate_card_file**
> add_rate_card_file(rate_card_id, file_name)

Attach a file to a rateCard

Adds a file to an existing rateCard.

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
api_instance = Infoplus.RateCardApi(Infoplus.ApiClient(configuration))
rate_card_id = 56 # int | Id of the rateCard to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a rateCard
    api_instance.add_rate_card_file(rate_card_id, file_name)
except ApiException as e:
    print("Exception when calling RateCardApi->add_rate_card_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_card_id** | **int**| Id of the rateCard to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_rate_card_file_by_url**
> add_rate_card_file_by_url(body, rate_card_id)

Attach a file to a rateCard by URL.

Adds a file to an existing rateCard by URL.

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
api_instance = Infoplus.RateCardApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
rate_card_id = 56 # int | Id of the rateCard to add an file to

try:
    # Attach a file to a rateCard by URL.
    api_instance.add_rate_card_file_by_url(body, rate_card_id)
except ApiException as e:
    print("Exception when calling RateCardApi->add_rate_card_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **rate_card_id** | **int**| Id of the rateCard to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_rate_card_tag**
> add_rate_card_tag(rate_card_id, rate_card_tag)

Add new tags for a rateCard.

Adds a tag to an existing rateCard.

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
api_instance = Infoplus.RateCardApi(Infoplus.ApiClient(configuration))
rate_card_id = 56 # int | Id of the rateCard to add a tag to
rate_card_tag = 'rate_card_tag_example' # str | The tag to add

try:
    # Add new tags for a rateCard.
    api_instance.add_rate_card_tag(rate_card_id, rate_card_tag)
except ApiException as e:
    print("Exception when calling RateCardApi->add_rate_card_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_card_id** | **int**| Id of the rateCard to add a tag to | 
 **rate_card_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rate_card**
> delete_rate_card(rate_card_id)

Delete a rateCard

Deletes the rateCard identified by the specified id.

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
api_instance = Infoplus.RateCardApi(Infoplus.ApiClient(configuration))
rate_card_id = 56 # int | Id of the rateCard to be deleted.

try:
    # Delete a rateCard
    api_instance.delete_rate_card(rate_card_id)
except ApiException as e:
    print("Exception when calling RateCardApi->delete_rate_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_card_id** | **int**| Id of the rateCard to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rate_card_file**
> delete_rate_card_file(rate_card_id, file_id)

Delete a file for a rateCard.

Deletes an existing rateCard file using the specified data.

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
api_instance = Infoplus.RateCardApi(Infoplus.ApiClient(configuration))
rate_card_id = 56 # int | Id of the rateCard to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a rateCard.
    api_instance.delete_rate_card_file(rate_card_id, file_id)
except ApiException as e:
    print("Exception when calling RateCardApi->delete_rate_card_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_card_id** | **int**| Id of the rateCard to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rate_card_tag**
> delete_rate_card_tag(rate_card_id, rate_card_tag)

Delete a tag for a rateCard.

Deletes an existing rateCard tag using the specified data.

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
api_instance = Infoplus.RateCardApi(Infoplus.ApiClient(configuration))
rate_card_id = 56 # int | Id of the rateCard to remove tag from
rate_card_tag = 'rate_card_tag_example' # str | The tag to delete

try:
    # Delete a tag for a rateCard.
    api_instance.delete_rate_card_tag(rate_card_id, rate_card_tag)
except ApiException as e:
    print("Exception when calling RateCardApi->delete_rate_card_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_card_id** | **int**| Id of the rateCard to remove tag from | 
 **rate_card_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_rate_card_by_id**
> RateCard get_duplicate_rate_card_by_id(rate_card_id)

Get a duplicated a rateCard by id

Returns a duplicated rateCard identified by the specified id.

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
api_instance = Infoplus.RateCardApi(Infoplus.ApiClient(configuration))
rate_card_id = 56 # int | Id of the rateCard to be duplicated.

try:
    # Get a duplicated a rateCard by id
    api_response = api_instance.get_duplicate_rate_card_by_id(rate_card_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RateCardApi->get_duplicate_rate_card_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_card_id** | **int**| Id of the rateCard to be duplicated. | 

### Return type

[**RateCard**](RateCard.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_card_by_filter**
> list[RateCard] get_rate_card_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search rateCards by filter

Returns the list of rateCards that match the given filter.

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
api_instance = Infoplus.RateCardApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search rateCards by filter
    api_response = api_instance.get_rate_card_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RateCardApi->get_rate_card_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[RateCard]**](RateCard.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_card_by_id**
> RateCard get_rate_card_by_id(rate_card_id)

Get a rateCard by id

Returns the rateCard identified by the specified id.

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
api_instance = Infoplus.RateCardApi(Infoplus.ApiClient(configuration))
rate_card_id = 56 # int | Id of the rateCard to be returned.

try:
    # Get a rateCard by id
    api_response = api_instance.get_rate_card_by_id(rate_card_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RateCardApi->get_rate_card_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_card_id** | **int**| Id of the rateCard to be returned. | 

### Return type

[**RateCard**](RateCard.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_card_files**
> get_rate_card_files(rate_card_id)

Get the files for a rateCard.

Get all existing rateCard files.

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
api_instance = Infoplus.RateCardApi(Infoplus.ApiClient(configuration))
rate_card_id = 56 # int | Id of the rateCard to get files for

try:
    # Get the files for a rateCard.
    api_instance.get_rate_card_files(rate_card_id)
except ApiException as e:
    print("Exception when calling RateCardApi->get_rate_card_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_card_id** | **int**| Id of the rateCard to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_card_tags**
> get_rate_card_tags(rate_card_id)

Get the tags for a rateCard.

Get all existing rateCard tags.

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
api_instance = Infoplus.RateCardApi(Infoplus.ApiClient(configuration))
rate_card_id = 56 # int | Id of the rateCard to get tags for

try:
    # Get the tags for a rateCard.
    api_instance.get_rate_card_tags(rate_card_id)
except ApiException as e:
    print("Exception when calling RateCardApi->get_rate_card_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_card_id** | **int**| Id of the rateCard to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rate_card**
> update_rate_card(body)

Update a rateCard

Updates an existing rateCard using the specified data.

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
api_instance = Infoplus.RateCardApi(Infoplus.ApiClient(configuration))
body = Infoplus.RateCard() # RateCard | RateCard to be updated.

try:
    # Update a rateCard
    api_instance.update_rate_card(body)
except ApiException as e:
    print("Exception when calling RateCardApi->update_rate_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RateCard**](RateCard.md)| RateCard to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

