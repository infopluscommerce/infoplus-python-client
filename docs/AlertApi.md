# Infoplus.AlertApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_alert**](AlertApi.md#add_alert) | **POST** /beta/alert | Create an alert
[**add_alert_audit**](AlertApi.md#add_alert_audit) | **PUT** /beta/alert/{alertId}/audit/{alertAudit} | Add new audit for an alert
[**add_alert_file**](AlertApi.md#add_alert_file) | **POST** /beta/alert/{alertId}/file/{fileName} | Attach a file to an alert
[**add_alert_file_by_url**](AlertApi.md#add_alert_file_by_url) | **POST** /beta/alert/{alertId}/file | Attach a file to an alert by URL.
[**add_alert_tag**](AlertApi.md#add_alert_tag) | **PUT** /beta/alert/{alertId}/tag/{alertTag} | Add new tags for an alert.
[**delete_alert_file**](AlertApi.md#delete_alert_file) | **DELETE** /beta/alert/{alertId}/file/{fileId} | Delete a file for an alert.
[**delete_alert_tag**](AlertApi.md#delete_alert_tag) | **DELETE** /beta/alert/{alertId}/tag/{alertTag} | Delete a tag for an alert.
[**get_alert_by_filter**](AlertApi.md#get_alert_by_filter) | **GET** /beta/alert/search | Search alerts by filter
[**get_alert_by_id**](AlertApi.md#get_alert_by_id) | **GET** /beta/alert/{alertId} | Get an alert by id
[**get_alert_files**](AlertApi.md#get_alert_files) | **GET** /beta/alert/{alertId}/file | Get the files for an alert.
[**get_alert_tags**](AlertApi.md#get_alert_tags) | **GET** /beta/alert/{alertId}/tag | Get the tags for an alert.
[**get_duplicate_alert_by_id**](AlertApi.md#get_duplicate_alert_by_id) | **GET** /beta/alert/duplicate/{alertId} | Get a duplicated an alert by id
[**update_alert_custom_fields**](AlertApi.md#update_alert_custom_fields) | **PUT** /beta/alert/customFields | Update an alert custom fields


# **add_alert**
> Alert add_alert(body)

Create an alert

Inserts a new alert using the specified data.

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
api_instance = Infoplus.AlertApi(Infoplus.ApiClient(configuration))
body = Infoplus.Alert() # Alert | Alert to be inserted.

try:
    # Create an alert
    api_response = api_instance.add_alert(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->add_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Alert**](Alert.md)| Alert to be inserted. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_alert_audit**
> add_alert_audit(alert_id, alert_audit)

Add new audit for an alert

Adds an audit to an existing alert.

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
api_instance = Infoplus.AlertApi(Infoplus.ApiClient(configuration))
alert_id = 56 # int | Id of the alert to add an audit to
alert_audit = 'alert_audit_example' # str | The audit to add

try:
    # Add new audit for an alert
    api_instance.add_alert_audit(alert_id, alert_audit)
except ApiException as e:
    print("Exception when calling AlertApi->add_alert_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| Id of the alert to add an audit to | 
 **alert_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_alert_file**
> add_alert_file(alert_id, file_name)

Attach a file to an alert

Adds a file to an existing alert.

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
api_instance = Infoplus.AlertApi(Infoplus.ApiClient(configuration))
alert_id = 56 # int | Id of the alert to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an alert
    api_instance.add_alert_file(alert_id, file_name)
except ApiException as e:
    print("Exception when calling AlertApi->add_alert_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| Id of the alert to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_alert_file_by_url**
> add_alert_file_by_url(body, alert_id)

Attach a file to an alert by URL.

Adds a file to an existing alert by URL.

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
api_instance = Infoplus.AlertApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
alert_id = 56 # int | Id of the alert to add an file to

try:
    # Attach a file to an alert by URL.
    api_instance.add_alert_file_by_url(body, alert_id)
except ApiException as e:
    print("Exception when calling AlertApi->add_alert_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **alert_id** | **int**| Id of the alert to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_alert_tag**
> add_alert_tag(alert_id, alert_tag)

Add new tags for an alert.

Adds a tag to an existing alert.

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
api_instance = Infoplus.AlertApi(Infoplus.ApiClient(configuration))
alert_id = 56 # int | Id of the alert to add a tag to
alert_tag = 'alert_tag_example' # str | The tag to add

try:
    # Add new tags for an alert.
    api_instance.add_alert_tag(alert_id, alert_tag)
except ApiException as e:
    print("Exception when calling AlertApi->add_alert_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| Id of the alert to add a tag to | 
 **alert_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_file**
> delete_alert_file(alert_id, file_id)

Delete a file for an alert.

Deletes an existing alert file using the specified data.

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
api_instance = Infoplus.AlertApi(Infoplus.ApiClient(configuration))
alert_id = 56 # int | Id of the alert to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an alert.
    api_instance.delete_alert_file(alert_id, file_id)
except ApiException as e:
    print("Exception when calling AlertApi->delete_alert_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| Id of the alert to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_tag**
> delete_alert_tag(alert_id, alert_tag)

Delete a tag for an alert.

Deletes an existing alert tag using the specified data.

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
api_instance = Infoplus.AlertApi(Infoplus.ApiClient(configuration))
alert_id = 56 # int | Id of the alert to remove tag from
alert_tag = 'alert_tag_example' # str | The tag to delete

try:
    # Delete a tag for an alert.
    api_instance.delete_alert_tag(alert_id, alert_tag)
except ApiException as e:
    print("Exception when calling AlertApi->delete_alert_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| Id of the alert to remove tag from | 
 **alert_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_by_filter**
> list[Alert] get_alert_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search alerts by filter

Returns the list of alerts that match the given filter.

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
api_instance = Infoplus.AlertApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search alerts by filter
    api_response = api_instance.get_alert_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_alert_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[Alert]**](Alert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_by_id**
> Alert get_alert_by_id(alert_id)

Get an alert by id

Returns the alert identified by the specified id.

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
api_instance = Infoplus.AlertApi(Infoplus.ApiClient(configuration))
alert_id = 56 # int | Id of the alert to be returned.

try:
    # Get an alert by id
    api_response = api_instance.get_alert_by_id(alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_alert_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| Id of the alert to be returned. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_files**
> get_alert_files(alert_id)

Get the files for an alert.

Get all existing alert files.

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
api_instance = Infoplus.AlertApi(Infoplus.ApiClient(configuration))
alert_id = 56 # int | Id of the alert to get files for

try:
    # Get the files for an alert.
    api_instance.get_alert_files(alert_id)
except ApiException as e:
    print("Exception when calling AlertApi->get_alert_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| Id of the alert to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_tags**
> get_alert_tags(alert_id)

Get the tags for an alert.

Get all existing alert tags.

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
api_instance = Infoplus.AlertApi(Infoplus.ApiClient(configuration))
alert_id = 56 # int | Id of the alert to get tags for

try:
    # Get the tags for an alert.
    api_instance.get_alert_tags(alert_id)
except ApiException as e:
    print("Exception when calling AlertApi->get_alert_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| Id of the alert to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_alert_by_id**
> Alert get_duplicate_alert_by_id(alert_id)

Get a duplicated an alert by id

Returns a duplicated alert identified by the specified id.

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
api_instance = Infoplus.AlertApi(Infoplus.ApiClient(configuration))
alert_id = 56 # int | Id of the alert to be duplicated.

try:
    # Get a duplicated an alert by id
    api_response = api_instance.get_duplicate_alert_by_id(alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_duplicate_alert_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| Id of the alert to be duplicated. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_custom_fields**
> update_alert_custom_fields(body)

Update an alert custom fields

Updates an existing alert custom fields using the specified data.

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
api_instance = Infoplus.AlertApi(Infoplus.ApiClient(configuration))
body = Infoplus.Alert() # Alert | Alert to be updated.

try:
    # Update an alert custom fields
    api_instance.update_alert_custom_fields(body)
except ApiException as e:
    print("Exception when calling AlertApi->update_alert_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Alert**](Alert.md)| Alert to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

