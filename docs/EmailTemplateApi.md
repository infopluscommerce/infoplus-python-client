# Infoplus.EmailTemplateApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_email_template**](EmailTemplateApi.md#add_email_template) | **POST** /v3.0/emailTemplate | Create an emailTemplate
[**add_email_template_audit**](EmailTemplateApi.md#add_email_template_audit) | **PUT** /v3.0/emailTemplate/{emailTemplateId}/audit/{emailTemplateAudit} | Add new audit for an emailTemplate
[**add_email_template_file**](EmailTemplateApi.md#add_email_template_file) | **POST** /v3.0/emailTemplate/{emailTemplateId}/file/{fileName} | Attach a file to an emailTemplate
[**add_email_template_file_by_url**](EmailTemplateApi.md#add_email_template_file_by_url) | **POST** /v3.0/emailTemplate/{emailTemplateId}/file | Attach a file to an emailTemplate by URL.
[**add_email_template_tag**](EmailTemplateApi.md#add_email_template_tag) | **PUT** /v3.0/emailTemplate/{emailTemplateId}/tag/{emailTemplateTag} | Add new tags for an emailTemplate.
[**delete_email_template**](EmailTemplateApi.md#delete_email_template) | **DELETE** /v3.0/emailTemplate/{emailTemplateId} | Delete an emailTemplate
[**delete_email_template_file**](EmailTemplateApi.md#delete_email_template_file) | **DELETE** /v3.0/emailTemplate/{emailTemplateId}/file/{fileId} | Delete a file for an emailTemplate.
[**delete_email_template_tag**](EmailTemplateApi.md#delete_email_template_tag) | **DELETE** /v3.0/emailTemplate/{emailTemplateId}/tag/{emailTemplateTag} | Delete a tag for an emailTemplate.
[**get_duplicate_email_template_by_id**](EmailTemplateApi.md#get_duplicate_email_template_by_id) | **GET** /v3.0/emailTemplate/duplicate/{emailTemplateId} | Get a duplicated an emailTemplate by id
[**get_email_template_by_filter**](EmailTemplateApi.md#get_email_template_by_filter) | **GET** /v3.0/emailTemplate/search | Search emailTemplates by filter
[**get_email_template_by_id**](EmailTemplateApi.md#get_email_template_by_id) | **GET** /v3.0/emailTemplate/{emailTemplateId} | Get an emailTemplate by id
[**get_email_template_files**](EmailTemplateApi.md#get_email_template_files) | **GET** /v3.0/emailTemplate/{emailTemplateId}/file | Get the files for an emailTemplate.
[**get_email_template_tags**](EmailTemplateApi.md#get_email_template_tags) | **GET** /v3.0/emailTemplate/{emailTemplateId}/tag | Get the tags for an emailTemplate.
[**update_email_template**](EmailTemplateApi.md#update_email_template) | **PUT** /v3.0/emailTemplate | Update an emailTemplate
[**update_email_template_custom_fields**](EmailTemplateApi.md#update_email_template_custom_fields) | **PUT** /v3.0/emailTemplate/customFields | Update an emailTemplate custom fields


# **add_email_template**
> EmailTemplate add_email_template(body)

Create an emailTemplate

Inserts a new emailTemplate using the specified data.

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
api_instance = Infoplus.EmailTemplateApi(Infoplus.ApiClient(configuration))
body = Infoplus.EmailTemplate() # EmailTemplate | EmailTemplate to be inserted.

try:
    # Create an emailTemplate
    api_response = api_instance.add_email_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->add_email_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailTemplate**](EmailTemplate.md)| EmailTemplate to be inserted. | 

### Return type

[**EmailTemplate**](EmailTemplate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_email_template_audit**
> add_email_template_audit(email_template_id, email_template_audit)

Add new audit for an emailTemplate

Adds an audit to an existing emailTemplate.

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
api_instance = Infoplus.EmailTemplateApi(Infoplus.ApiClient(configuration))
email_template_id = 56 # int | Id of the emailTemplate to add an audit to
email_template_audit = 'email_template_audit_example' # str | The audit to add

try:
    # Add new audit for an emailTemplate
    api_instance.add_email_template_audit(email_template_id, email_template_audit)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->add_email_template_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_template_id** | **int**| Id of the emailTemplate to add an audit to | 
 **email_template_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_email_template_file**
> add_email_template_file(email_template_id, file_name)

Attach a file to an emailTemplate

Adds a file to an existing emailTemplate.

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
api_instance = Infoplus.EmailTemplateApi(Infoplus.ApiClient(configuration))
email_template_id = 56 # int | Id of the emailTemplate to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an emailTemplate
    api_instance.add_email_template_file(email_template_id, file_name)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->add_email_template_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_template_id** | **int**| Id of the emailTemplate to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_email_template_file_by_url**
> add_email_template_file_by_url(body, email_template_id)

Attach a file to an emailTemplate by URL.

Adds a file to an existing emailTemplate by URL.

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
api_instance = Infoplus.EmailTemplateApi(Infoplus.ApiClient(configuration))
body = Infoplus.RecordFile() # RecordFile | The url and optionly fileName to be used.
email_template_id = 56 # int | Id of the emailTemplate to add an file to

try:
    # Attach a file to an emailTemplate by URL.
    api_instance.add_email_template_file_by_url(body, email_template_id)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->add_email_template_file_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordFile**](RecordFile.md)| The url and optionly fileName to be used. | 
 **email_template_id** | **int**| Id of the emailTemplate to add an file to | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_email_template_tag**
> add_email_template_tag(email_template_id, email_template_tag)

Add new tags for an emailTemplate.

Adds a tag to an existing emailTemplate.

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
api_instance = Infoplus.EmailTemplateApi(Infoplus.ApiClient(configuration))
email_template_id = 56 # int | Id of the emailTemplate to add a tag to
email_template_tag = 'email_template_tag_example' # str | The tag to add

try:
    # Add new tags for an emailTemplate.
    api_instance.add_email_template_tag(email_template_id, email_template_tag)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->add_email_template_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_template_id** | **int**| Id of the emailTemplate to add a tag to | 
 **email_template_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_template**
> delete_email_template(email_template_id)

Delete an emailTemplate

Deletes the emailTemplate identified by the specified id.

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
api_instance = Infoplus.EmailTemplateApi(Infoplus.ApiClient(configuration))
email_template_id = 56 # int | Id of the emailTemplate to be deleted.

try:
    # Delete an emailTemplate
    api_instance.delete_email_template(email_template_id)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->delete_email_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_template_id** | **int**| Id of the emailTemplate to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_template_file**
> delete_email_template_file(email_template_id, file_id)

Delete a file for an emailTemplate.

Deletes an existing emailTemplate file using the specified data.

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
api_instance = Infoplus.EmailTemplateApi(Infoplus.ApiClient(configuration))
email_template_id = 56 # int | Id of the emailTemplate to remove file from
file_id = 56 # int | Id of the file to delete

try:
    # Delete a file for an emailTemplate.
    api_instance.delete_email_template_file(email_template_id, file_id)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->delete_email_template_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_template_id** | **int**| Id of the emailTemplate to remove file from | 
 **file_id** | **int**| Id of the file to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_template_tag**
> delete_email_template_tag(email_template_id, email_template_tag)

Delete a tag for an emailTemplate.

Deletes an existing emailTemplate tag using the specified data.

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
api_instance = Infoplus.EmailTemplateApi(Infoplus.ApiClient(configuration))
email_template_id = 56 # int | Id of the emailTemplate to remove tag from
email_template_tag = 'email_template_tag_example' # str | The tag to delete

try:
    # Delete a tag for an emailTemplate.
    api_instance.delete_email_template_tag(email_template_id, email_template_tag)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->delete_email_template_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_template_id** | **int**| Id of the emailTemplate to remove tag from | 
 **email_template_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_email_template_by_id**
> EmailTemplate get_duplicate_email_template_by_id(email_template_id)

Get a duplicated an emailTemplate by id

Returns a duplicated emailTemplate identified by the specified id.

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
api_instance = Infoplus.EmailTemplateApi(Infoplus.ApiClient(configuration))
email_template_id = 56 # int | Id of the emailTemplate to be duplicated.

try:
    # Get a duplicated an emailTemplate by id
    api_response = api_instance.get_duplicate_email_template_by_id(email_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->get_duplicate_email_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_template_id** | **int**| Id of the emailTemplate to be duplicated. | 

### Return type

[**EmailTemplate**](EmailTemplate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_template_by_filter**
> list[EmailTemplate] get_email_template_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search emailTemplates by filter

Returns the list of emailTemplates that match the given filter.

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
api_instance = Infoplus.EmailTemplateApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search emailTemplates by filter
    api_response = api_instance.get_email_template_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->get_email_template_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[EmailTemplate]**](EmailTemplate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_template_by_id**
> EmailTemplate get_email_template_by_id(email_template_id)

Get an emailTemplate by id

Returns the emailTemplate identified by the specified id.

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
api_instance = Infoplus.EmailTemplateApi(Infoplus.ApiClient(configuration))
email_template_id = 56 # int | Id of the emailTemplate to be returned.

try:
    # Get an emailTemplate by id
    api_response = api_instance.get_email_template_by_id(email_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->get_email_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_template_id** | **int**| Id of the emailTemplate to be returned. | 

### Return type

[**EmailTemplate**](EmailTemplate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_template_files**
> get_email_template_files(email_template_id)

Get the files for an emailTemplate.

Get all existing emailTemplate files.

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
api_instance = Infoplus.EmailTemplateApi(Infoplus.ApiClient(configuration))
email_template_id = 56 # int | Id of the emailTemplate to get files for

try:
    # Get the files for an emailTemplate.
    api_instance.get_email_template_files(email_template_id)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->get_email_template_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_template_id** | **int**| Id of the emailTemplate to get files for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_template_tags**
> get_email_template_tags(email_template_id)

Get the tags for an emailTemplate.

Get all existing emailTemplate tags.

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
api_instance = Infoplus.EmailTemplateApi(Infoplus.ApiClient(configuration))
email_template_id = 56 # int | Id of the emailTemplate to get tags for

try:
    # Get the tags for an emailTemplate.
    api_instance.get_email_template_tags(email_template_id)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->get_email_template_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_template_id** | **int**| Id of the emailTemplate to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_template**
> update_email_template(body)

Update an emailTemplate

Updates an existing emailTemplate using the specified data.

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
api_instance = Infoplus.EmailTemplateApi(Infoplus.ApiClient(configuration))
body = Infoplus.EmailTemplate() # EmailTemplate | EmailTemplate to be updated.

try:
    # Update an emailTemplate
    api_instance.update_email_template(body)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->update_email_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailTemplate**](EmailTemplate.md)| EmailTemplate to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_template_custom_fields**
> update_email_template_custom_fields(body)

Update an emailTemplate custom fields

Updates an existing emailTemplate custom fields using the specified data.

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
api_instance = Infoplus.EmailTemplateApi(Infoplus.ApiClient(configuration))
body = Infoplus.EmailTemplate() # EmailTemplate | EmailTemplate to be updated.

try:
    # Update an emailTemplate custom fields
    api_instance.update_email_template_custom_fields(body)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->update_email_template_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailTemplate**](EmailTemplate.md)| EmailTemplate to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

