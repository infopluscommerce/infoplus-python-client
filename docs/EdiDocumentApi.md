# Infoplus.EdiDocumentApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_edi_document**](EdiDocumentApi.md#add_edi_document) | **POST** /beta/ediDocument | Create an ediDocument
[**add_edi_document_audit**](EdiDocumentApi.md#add_edi_document_audit) | **PUT** /beta/ediDocument/{ediDocumentId}/audit/{ediDocumentAudit} | Add new audit for an ediDocument
[**add_edi_document_file**](EdiDocumentApi.md#add_edi_document_file) | **POST** /beta/ediDocument/{ediDocumentId}/file/{fileName} | Attach a file to an ediDocument
[**add_edi_document_tag**](EdiDocumentApi.md#add_edi_document_tag) | **PUT** /beta/ediDocument/{ediDocumentId}/tag/{ediDocumentTag} | Add new tags for an ediDocument.
[**delete_edi_document_tag**](EdiDocumentApi.md#delete_edi_document_tag) | **DELETE** /beta/ediDocument/{ediDocumentId}/tag/{ediDocumentTag} | Delete a tag for an ediDocument.
[**get_duplicate_edi_document_by_id**](EdiDocumentApi.md#get_duplicate_edi_document_by_id) | **GET** /beta/ediDocument/duplicate/{ediDocumentId} | Get a duplicated an ediDocument by id
[**get_edi_document_by_filter**](EdiDocumentApi.md#get_edi_document_by_filter) | **GET** /beta/ediDocument/search | Search ediDocuments by filter
[**get_edi_document_by_id**](EdiDocumentApi.md#get_edi_document_by_id) | **GET** /beta/ediDocument/{ediDocumentId} | Get an ediDocument by id
[**get_edi_document_tags**](EdiDocumentApi.md#get_edi_document_tags) | **GET** /beta/ediDocument/{ediDocumentId}/tag | Get the tags for an ediDocument.


# **add_edi_document**
> EdiDocument add_edi_document(body)

Create an ediDocument

Inserts a new ediDocument using the specified data.

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
api_instance = Infoplus.EdiDocumentApi(Infoplus.ApiClient(configuration))
body = Infoplus.EdiDocument() # EdiDocument | EdiDocument to be inserted.

try:
    # Create an ediDocument
    api_response = api_instance.add_edi_document(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdiDocumentApi->add_edi_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EdiDocument**](EdiDocument.md)| EdiDocument to be inserted. | 

### Return type

[**EdiDocument**](EdiDocument.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_edi_document_audit**
> add_edi_document_audit(edi_document_id, edi_document_audit)

Add new audit for an ediDocument

Adds an audit to an existing ediDocument.

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
api_instance = Infoplus.EdiDocumentApi(Infoplus.ApiClient(configuration))
edi_document_id = 56 # int | Id of the ediDocument to add an audit to
edi_document_audit = 'edi_document_audit_example' # str | The audit to add

try:
    # Add new audit for an ediDocument
    api_instance.add_edi_document_audit(edi_document_id, edi_document_audit)
except ApiException as e:
    print("Exception when calling EdiDocumentApi->add_edi_document_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edi_document_id** | **int**| Id of the ediDocument to add an audit to | 
 **edi_document_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_edi_document_file**
> add_edi_document_file(edi_document_id, file_name)

Attach a file to an ediDocument

Adds a file to an existing ediDocument.

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
api_instance = Infoplus.EdiDocumentApi(Infoplus.ApiClient(configuration))
edi_document_id = 56 # int | Id of the ediDocument to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to an ediDocument
    api_instance.add_edi_document_file(edi_document_id, file_name)
except ApiException as e:
    print("Exception when calling EdiDocumentApi->add_edi_document_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edi_document_id** | **int**| Id of the ediDocument to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_edi_document_tag**
> add_edi_document_tag(edi_document_id, edi_document_tag)

Add new tags for an ediDocument.

Adds a tag to an existing ediDocument.

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
api_instance = Infoplus.EdiDocumentApi(Infoplus.ApiClient(configuration))
edi_document_id = 56 # int | Id of the ediDocument to add a tag to
edi_document_tag = 'edi_document_tag_example' # str | The tag to add

try:
    # Add new tags for an ediDocument.
    api_instance.add_edi_document_tag(edi_document_id, edi_document_tag)
except ApiException as e:
    print("Exception when calling EdiDocumentApi->add_edi_document_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edi_document_id** | **int**| Id of the ediDocument to add a tag to | 
 **edi_document_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_edi_document_tag**
> delete_edi_document_tag(edi_document_id, edi_document_tag)

Delete a tag for an ediDocument.

Deletes an existing ediDocument tag using the specified data.

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
api_instance = Infoplus.EdiDocumentApi(Infoplus.ApiClient(configuration))
edi_document_id = 56 # int | Id of the ediDocument to remove tag from
edi_document_tag = 'edi_document_tag_example' # str | The tag to delete

try:
    # Delete a tag for an ediDocument.
    api_instance.delete_edi_document_tag(edi_document_id, edi_document_tag)
except ApiException as e:
    print("Exception when calling EdiDocumentApi->delete_edi_document_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edi_document_id** | **int**| Id of the ediDocument to remove tag from | 
 **edi_document_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_edi_document_by_id**
> EdiDocument get_duplicate_edi_document_by_id(edi_document_id)

Get a duplicated an ediDocument by id

Returns a duplicated ediDocument identified by the specified id.

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
api_instance = Infoplus.EdiDocumentApi(Infoplus.ApiClient(configuration))
edi_document_id = 56 # int | Id of the ediDocument to be duplicated.

try:
    # Get a duplicated an ediDocument by id
    api_response = api_instance.get_duplicate_edi_document_by_id(edi_document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdiDocumentApi->get_duplicate_edi_document_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edi_document_id** | **int**| Id of the ediDocument to be duplicated. | 

### Return type

[**EdiDocument**](EdiDocument.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edi_document_by_filter**
> list[EdiDocument] get_edi_document_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search ediDocuments by filter

Returns the list of ediDocuments that match the given filter.

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
api_instance = Infoplus.EdiDocumentApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search ediDocuments by filter
    api_response = api_instance.get_edi_document_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdiDocumentApi->get_edi_document_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[EdiDocument]**](EdiDocument.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edi_document_by_id**
> EdiDocument get_edi_document_by_id(edi_document_id)

Get an ediDocument by id

Returns the ediDocument identified by the specified id.

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
api_instance = Infoplus.EdiDocumentApi(Infoplus.ApiClient(configuration))
edi_document_id = 56 # int | Id of the ediDocument to be returned.

try:
    # Get an ediDocument by id
    api_response = api_instance.get_edi_document_by_id(edi_document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EdiDocumentApi->get_edi_document_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edi_document_id** | **int**| Id of the ediDocument to be returned. | 

### Return type

[**EdiDocument**](EdiDocument.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edi_document_tags**
> get_edi_document_tags(edi_document_id)

Get the tags for an ediDocument.

Get all existing ediDocument tags.

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
api_instance = Infoplus.EdiDocumentApi(Infoplus.ApiClient(configuration))
edi_document_id = 56 # int | Id of the ediDocument to get tags for

try:
    # Get the tags for an ediDocument.
    api_instance.get_edi_document_tags(edi_document_id)
except ApiException as e:
    print("Exception when calling EdiDocumentApi->get_edi_document_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edi_document_id** | **int**| Id of the ediDocument to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

