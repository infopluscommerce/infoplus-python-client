# Infoplus.LineOfBusinessApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_line_of_business**](LineOfBusinessApi.md#add_line_of_business) | **POST** /beta/lineOfBusiness | Create a lineOfBusiness
[**add_line_of_business_audit**](LineOfBusinessApi.md#add_line_of_business_audit) | **PUT** /beta/lineOfBusiness/{lineOfBusinessId}/audit/{lineOfBusinessAudit} | Add new audit for a lineOfBusiness
[**add_line_of_business_file**](LineOfBusinessApi.md#add_line_of_business_file) | **POST** /beta/lineOfBusiness/{lineOfBusinessId}/file/{fileName} | Attach a file to a lineOfBusiness
[**add_line_of_business_file_by_url**](LineOfBusinessApi.md#add_line_of_business_file_by_url) | **POST** /beta/lineOfBusiness/{lineOfBusinessId}/file | Attach a file to a lineOfBusiness by URL.
[**add_line_of_business_tag**](LineOfBusinessApi.md#add_line_of_business_tag) | **PUT** /beta/lineOfBusiness/{lineOfBusinessId}/tag/{lineOfBusinessTag} | Add new tags for a lineOfBusiness.
[**delete_line_of_business_file**](LineOfBusinessApi.md#delete_line_of_business_file) | **DELETE** /beta/lineOfBusiness/{lineOfBusinessId}/file/{fileId} | Delete a file for a lineOfBusiness.
[**delete_line_of_business_tag**](LineOfBusinessApi.md#delete_line_of_business_tag) | **DELETE** /beta/lineOfBusiness/{lineOfBusinessId}/tag/{lineOfBusinessTag} | Delete a tag for a lineOfBusiness.
[**get_duplicate_line_of_business_by_id**](LineOfBusinessApi.md#get_duplicate_line_of_business_by_id) | **GET** /beta/lineOfBusiness/duplicate/{lineOfBusinessId} | Get a duplicated a lineOfBusiness by id
[**get_line_of_business_by_filter**](LineOfBusinessApi.md#get_line_of_business_by_filter) | **GET** /beta/lineOfBusiness/search | Search lineOfBusinesses by filter
[**get_line_of_business_by_id**](LineOfBusinessApi.md#get_line_of_business_by_id) | **GET** /beta/lineOfBusiness/{lineOfBusinessId} | Get a lineOfBusiness by id
[**get_line_of_business_files**](LineOfBusinessApi.md#get_line_of_business_files) | **GET** /beta/lineOfBusiness/{lineOfBusinessId}/file | Get the files for a lineOfBusiness.
[**get_line_of_business_tags**](LineOfBusinessApi.md#get_line_of_business_tags) | **GET** /beta/lineOfBusiness/{lineOfBusinessId}/tag | Get the tags for a lineOfBusiness.
[**update_line_of_business**](LineOfBusinessApi.md#update_line_of_business) | **PUT** /beta/lineOfBusiness | Update a lineOfBusiness
[**update_line_of_business_custom_fields**](LineOfBusinessApi.md#update_line_of_business_custom_fields) | **PUT** /beta/lineOfBusiness/customFields | Update a lineOfBusiness custom fields


# **add_line_of_business**
> LineOfBusiness add_line_of_business(body)

Create a lineOfBusiness

Inserts a new lineOfBusiness using the specified data.

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
api_instance = Infoplus.LineOfBusinessApi(Infoplus.ApiClient(configuration))
body = Infoplus.LineOfBusiness() # LineOfBusiness | LineOfBusiness to be inserted.

try:
    # Create a lineOfBusiness
    api_response = api_instance.add_line_of_business(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LineOfBusinessApi->add_line_of_business: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LineOfBusiness**](LineOfBusiness.md)| LineOfBusiness to be inserted. | 

### Return type

[**LineOfBusiness**](LineOfBusiness.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_line_of_business_audit**
> add_line_of_business_audit(line_of_business_id, line_of_business_audit)

Add new audit for a lineOfBusiness

Adds an audit to an existing lineOfBusiness.

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
api_instance = Infoplus.LineOfBusinessApi(Infoplus.ApiClient(configuration))
line_of_business_id = 56 # int | Id of the lineOfBusiness to add an audit to
line_of_business_audit = 'line_of_business_audit_example' # str | The audit to add

try:
    # Add new audit for a lineOfBusiness
    api_instance.add_line_of_business_audit(line_of_business_id, line_of_business_audit)
except ApiException as e:
    print("Exception when calling LineOfBusinessApi->add_line_of_business_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_of_business_id** | **int**| Id of the lineOfBusiness to add an audit to | 
 **line_of_business_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_line_of_business_file**
> add_line_of_business_file(line_of_business_id, file_name)

Attach a file to a lineOfBusiness

Adds a file to an existing lineOfBusiness.

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
api_instance = Infoplus.LineOfBusinessApi(Infoplus.ApiClient(configuration))
line_of_business_id = 56 # int | Id of the lineOfBusiness to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a lineOfBusiness
    api_instance.add_line_of_business_file(line_of_business_id, file_name)
except ApiException as e:
    print("Exception when calling LineOfBusinessApi->add_line_of_business_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_of_business_id** | **int**| Id of the lineOfBusiness to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_line_of_business_file_by_url**
> add_line_of_business_file_by_url(body, line_of_business_id)

Attach a file to a lineOfBusiness by URL.

Adds a file to an existing lineOfBusiness by URL.

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
api_instance = Infoplus.LineOfBusinessApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
line_of_business_id = 56 # int | Id of the lineOfBusiness to add an file to

try:
    # Attach a file to a lineOfBusiness by URL.
    api_instance.add_line_of_business_file_by_url(body, line_of_business_id)
except ApiException as e:
    print("Exception when calling LineOfBusinessApi->add_line_of_business_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **line_of_business_id** | **int**| Id of the lineOfBusiness to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_line_of_business_tag**
> add_line_of_business_tag(line_of_business_id, line_of_business_tag)

Add new tags for a lineOfBusiness.

Adds a tag to an existing lineOfBusiness.

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
api_instance = Infoplus.LineOfBusinessApi(Infoplus.ApiClient(configuration))
line_of_business_id = 56 # int | Id of the lineOfBusiness to add a tag to
line_of_business_tag = 'line_of_business_tag_example' # str | The tag to add

try:
    # Add new tags for a lineOfBusiness.
    api_instance.add_line_of_business_tag(line_of_business_id, line_of_business_tag)
except ApiException as e:
    print("Exception when calling LineOfBusinessApi->add_line_of_business_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_of_business_id** | **int**| Id of the lineOfBusiness to add a tag to | 
 **line_of_business_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_line_of_business_file**
> delete_line_of_business_file(line_of_business_id, file_id)

Delete a file for a lineOfBusiness.

Deletes an existing lineOfBusiness file using the specified data.

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
api_instance = Infoplus.LineOfBusinessApi(Infoplus.ApiClient(configuration))
line_of_business_id = 56 # int | Id of the lineOfBusiness to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for a lineOfBusiness.
    api_instance.delete_line_of_business_file(line_of_business_id, file_id)
except ApiException as e:
    print("Exception when calling LineOfBusinessApi->delete_line_of_business_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_of_business_id** | **int**| Id of the lineOfBusiness to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_line_of_business_tag**
> delete_line_of_business_tag(line_of_business_id, line_of_business_tag)

Delete a tag for a lineOfBusiness.

Deletes an existing lineOfBusiness tag using the specified data.

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
api_instance = Infoplus.LineOfBusinessApi(Infoplus.ApiClient(configuration))
line_of_business_id = 56 # int | Id of the lineOfBusiness to remove tag from
line_of_business_tag = 'line_of_business_tag_example' # str | The tag to delete

try:
    # Delete a tag for a lineOfBusiness.
    api_instance.delete_line_of_business_tag(line_of_business_id, line_of_business_tag)
except ApiException as e:
    print("Exception when calling LineOfBusinessApi->delete_line_of_business_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_of_business_id** | **int**| Id of the lineOfBusiness to remove tag from | 
 **line_of_business_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_line_of_business_by_id**
> LineOfBusiness get_duplicate_line_of_business_by_id(line_of_business_id)

Get a duplicated a lineOfBusiness by id

Returns a duplicated lineOfBusiness identified by the specified id.

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
api_instance = Infoplus.LineOfBusinessApi(Infoplus.ApiClient(configuration))
line_of_business_id = 56 # int | Id of the lineOfBusiness to be duplicated.

try:
    # Get a duplicated a lineOfBusiness by id
    api_response = api_instance.get_duplicate_line_of_business_by_id(line_of_business_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LineOfBusinessApi->get_duplicate_line_of_business_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_of_business_id** | **int**| Id of the lineOfBusiness to be duplicated. | 

### Return type

[**LineOfBusiness**](LineOfBusiness.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_line_of_business_by_filter**
> list[LineOfBusiness] get_line_of_business_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search lineOfBusinesses by filter

Returns the list of lineOfBusinesses that match the given filter.

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
api_instance = Infoplus.LineOfBusinessApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search lineOfBusinesses by filter
    api_response = api_instance.get_line_of_business_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LineOfBusinessApi->get_line_of_business_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[LineOfBusiness]**](LineOfBusiness.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_line_of_business_by_id**
> LineOfBusiness get_line_of_business_by_id(line_of_business_id)

Get a lineOfBusiness by id

Returns the lineOfBusiness identified by the specified id.

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
api_instance = Infoplus.LineOfBusinessApi(Infoplus.ApiClient(configuration))
line_of_business_id = 56 # int | Id of the lineOfBusiness to be returned.

try:
    # Get a lineOfBusiness by id
    api_response = api_instance.get_line_of_business_by_id(line_of_business_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LineOfBusinessApi->get_line_of_business_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_of_business_id** | **int**| Id of the lineOfBusiness to be returned. | 

### Return type

[**LineOfBusiness**](LineOfBusiness.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_line_of_business_files**
> get_line_of_business_files(line_of_business_id)

Get the files for a lineOfBusiness.

Get all existing lineOfBusiness files.

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
api_instance = Infoplus.LineOfBusinessApi(Infoplus.ApiClient(configuration))
line_of_business_id = 56 # int | Id of the lineOfBusiness to get files for

try:
    # Get the files for a lineOfBusiness.
    api_instance.get_line_of_business_files(line_of_business_id)
except ApiException as e:
    print("Exception when calling LineOfBusinessApi->get_line_of_business_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_of_business_id** | **int**| Id of the lineOfBusiness to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_line_of_business_tags**
> get_line_of_business_tags(line_of_business_id)

Get the tags for a lineOfBusiness.

Get all existing lineOfBusiness tags.

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
api_instance = Infoplus.LineOfBusinessApi(Infoplus.ApiClient(configuration))
line_of_business_id = 56 # int | Id of the lineOfBusiness to get tags for

try:
    # Get the tags for a lineOfBusiness.
    api_instance.get_line_of_business_tags(line_of_business_id)
except ApiException as e:
    print("Exception when calling LineOfBusinessApi->get_line_of_business_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line_of_business_id** | **int**| Id of the lineOfBusiness to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_line_of_business**
> update_line_of_business(body)

Update a lineOfBusiness

Updates an existing lineOfBusiness using the specified data.

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
api_instance = Infoplus.LineOfBusinessApi(Infoplus.ApiClient(configuration))
body = Infoplus.LineOfBusiness() # LineOfBusiness | LineOfBusiness to be updated.

try:
    # Update a lineOfBusiness
    api_instance.update_line_of_business(body)
except ApiException as e:
    print("Exception when calling LineOfBusinessApi->update_line_of_business: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LineOfBusiness**](LineOfBusiness.md)| LineOfBusiness to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_line_of_business_custom_fields**
> update_line_of_business_custom_fields(body)

Update a lineOfBusiness custom fields

Updates an existing lineOfBusiness custom fields using the specified data.

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
api_instance = Infoplus.LineOfBusinessApi(Infoplus.ApiClient(configuration))
body = Infoplus.LineOfBusiness() # LineOfBusiness | LineOfBusiness to be updated.

try:
    # Update a lineOfBusiness custom fields
    api_instance.update_line_of_business_custom_fields(body)
except ApiException as e:
    print("Exception when calling LineOfBusinessApi->update_line_of_business_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LineOfBusiness**](LineOfBusiness.md)| LineOfBusiness to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

