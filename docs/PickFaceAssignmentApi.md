# Infoplus.PickFaceAssignmentApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_pick_face_assignment**](PickFaceAssignmentApi.md#add_pick_face_assignment) | **POST** /beta/pickFaceAssignment | Create a pickFaceAssignment
[**add_pick_face_assignment_audit**](PickFaceAssignmentApi.md#add_pick_face_assignment_audit) | **PUT** /beta/pickFaceAssignment/{pickFaceAssignmentId}/audit/{pickFaceAssignmentAudit} | Add new audit for a pickFaceAssignment
[**add_pick_face_assignment_file**](PickFaceAssignmentApi.md#add_pick_face_assignment_file) | **POST** /beta/pickFaceAssignment/{pickFaceAssignmentId}/file/{fileName} | Attach a file to a pickFaceAssignment
[**add_pick_face_assignment_tag**](PickFaceAssignmentApi.md#add_pick_face_assignment_tag) | **PUT** /beta/pickFaceAssignment/{pickFaceAssignmentId}/tag/{pickFaceAssignmentTag} | Add new tags for a pickFaceAssignment.
[**delete_pick_face_assignment**](PickFaceAssignmentApi.md#delete_pick_face_assignment) | **DELETE** /beta/pickFaceAssignment/{pickFaceAssignmentId} | Delete a pickFaceAssignment
[**delete_pick_face_assignment_tag**](PickFaceAssignmentApi.md#delete_pick_face_assignment_tag) | **DELETE** /beta/pickFaceAssignment/{pickFaceAssignmentId}/tag/{pickFaceAssignmentTag} | Delete a tag for a pickFaceAssignment.
[**get_duplicate_pick_face_assignment_by_id**](PickFaceAssignmentApi.md#get_duplicate_pick_face_assignment_by_id) | **GET** /beta/pickFaceAssignment/duplicate/{pickFaceAssignmentId} | Get a duplicated a pickFaceAssignment by id
[**get_pick_face_assignment_by_filter**](PickFaceAssignmentApi.md#get_pick_face_assignment_by_filter) | **GET** /beta/pickFaceAssignment/search | Search pickFaceAssignments by filter
[**get_pick_face_assignment_by_id**](PickFaceAssignmentApi.md#get_pick_face_assignment_by_id) | **GET** /beta/pickFaceAssignment/{pickFaceAssignmentId} | Get a pickFaceAssignment by id
[**get_pick_face_assignment_tags**](PickFaceAssignmentApi.md#get_pick_face_assignment_tags) | **GET** /beta/pickFaceAssignment/{pickFaceAssignmentId}/tag | Get the tags for a pickFaceAssignment.
[**update_pick_face_assignment**](PickFaceAssignmentApi.md#update_pick_face_assignment) | **PUT** /beta/pickFaceAssignment | Update a pickFaceAssignment
[**update_pick_face_assignment_custom_fields**](PickFaceAssignmentApi.md#update_pick_face_assignment_custom_fields) | **PUT** /beta/pickFaceAssignment/customFields | Update a pickFaceAssignment custom fields


# **add_pick_face_assignment**
> PickFaceAssignment add_pick_face_assignment(body)

Create a pickFaceAssignment

Inserts a new pickFaceAssignment using the specified data.

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
api_instance = Infoplus.PickFaceAssignmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.PickFaceAssignment() # PickFaceAssignment | PickFaceAssignment to be inserted.

try:
    # Create a pickFaceAssignment
    api_response = api_instance.add_pick_face_assignment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickFaceAssignmentApi->add_pick_face_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PickFaceAssignment**](PickFaceAssignment.md)| PickFaceAssignment to be inserted. | 

### Return type

[**PickFaceAssignment**](PickFaceAssignment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_pick_face_assignment_audit**
> add_pick_face_assignment_audit(pick_face_assignment_id, pick_face_assignment_audit)

Add new audit for a pickFaceAssignment

Adds an audit to an existing pickFaceAssignment.

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
api_instance = Infoplus.PickFaceAssignmentApi(Infoplus.ApiClient(configuration))
pick_face_assignment_id = 56 # int | Id of the pickFaceAssignment to add an audit to
pick_face_assignment_audit = 'pick_face_assignment_audit_example' # str | The audit to add

try:
    # Add new audit for a pickFaceAssignment
    api_instance.add_pick_face_assignment_audit(pick_face_assignment_id, pick_face_assignment_audit)
except ApiException as e:
    print("Exception when calling PickFaceAssignmentApi->add_pick_face_assignment_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pick_face_assignment_id** | **int**| Id of the pickFaceAssignment to add an audit to | 
 **pick_face_assignment_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_pick_face_assignment_file**
> add_pick_face_assignment_file(pick_face_assignment_id, file_name)

Attach a file to a pickFaceAssignment

Adds a file to an existing pickFaceAssignment.

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
api_instance = Infoplus.PickFaceAssignmentApi(Infoplus.ApiClient(configuration))
pick_face_assignment_id = 56 # int | Id of the pickFaceAssignment to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a pickFaceAssignment
    api_instance.add_pick_face_assignment_file(pick_face_assignment_id, file_name)
except ApiException as e:
    print("Exception when calling PickFaceAssignmentApi->add_pick_face_assignment_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pick_face_assignment_id** | **int**| Id of the pickFaceAssignment to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_pick_face_assignment_tag**
> add_pick_face_assignment_tag(pick_face_assignment_id, pick_face_assignment_tag)

Add new tags for a pickFaceAssignment.

Adds a tag to an existing pickFaceAssignment.

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
api_instance = Infoplus.PickFaceAssignmentApi(Infoplus.ApiClient(configuration))
pick_face_assignment_id = 56 # int | Id of the pickFaceAssignment to add a tag to
pick_face_assignment_tag = 'pick_face_assignment_tag_example' # str | The tag to add

try:
    # Add new tags for a pickFaceAssignment.
    api_instance.add_pick_face_assignment_tag(pick_face_assignment_id, pick_face_assignment_tag)
except ApiException as e:
    print("Exception when calling PickFaceAssignmentApi->add_pick_face_assignment_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pick_face_assignment_id** | **int**| Id of the pickFaceAssignment to add a tag to | 
 **pick_face_assignment_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pick_face_assignment**
> delete_pick_face_assignment(pick_face_assignment_id)

Delete a pickFaceAssignment

Deletes the pickFaceAssignment identified by the specified id.

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
api_instance = Infoplus.PickFaceAssignmentApi(Infoplus.ApiClient(configuration))
pick_face_assignment_id = 56 # int | Id of the pickFaceAssignment to be deleted.

try:
    # Delete a pickFaceAssignment
    api_instance.delete_pick_face_assignment(pick_face_assignment_id)
except ApiException as e:
    print("Exception when calling PickFaceAssignmentApi->delete_pick_face_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pick_face_assignment_id** | **int**| Id of the pickFaceAssignment to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pick_face_assignment_tag**
> delete_pick_face_assignment_tag(pick_face_assignment_id, pick_face_assignment_tag)

Delete a tag for a pickFaceAssignment.

Deletes an existing pickFaceAssignment tag using the specified data.

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
api_instance = Infoplus.PickFaceAssignmentApi(Infoplus.ApiClient(configuration))
pick_face_assignment_id = 56 # int | Id of the pickFaceAssignment to remove tag from
pick_face_assignment_tag = 'pick_face_assignment_tag_example' # str | The tag to delete

try:
    # Delete a tag for a pickFaceAssignment.
    api_instance.delete_pick_face_assignment_tag(pick_face_assignment_id, pick_face_assignment_tag)
except ApiException as e:
    print("Exception when calling PickFaceAssignmentApi->delete_pick_face_assignment_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pick_face_assignment_id** | **int**| Id of the pickFaceAssignment to remove tag from | 
 **pick_face_assignment_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_pick_face_assignment_by_id**
> PickFaceAssignment get_duplicate_pick_face_assignment_by_id(pick_face_assignment_id)

Get a duplicated a pickFaceAssignment by id

Returns a duplicated pickFaceAssignment identified by the specified id.

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
api_instance = Infoplus.PickFaceAssignmentApi(Infoplus.ApiClient(configuration))
pick_face_assignment_id = 56 # int | Id of the pickFaceAssignment to be duplicated.

try:
    # Get a duplicated a pickFaceAssignment by id
    api_response = api_instance.get_duplicate_pick_face_assignment_by_id(pick_face_assignment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickFaceAssignmentApi->get_duplicate_pick_face_assignment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pick_face_assignment_id** | **int**| Id of the pickFaceAssignment to be duplicated. | 

### Return type

[**PickFaceAssignment**](PickFaceAssignment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pick_face_assignment_by_filter**
> list[PickFaceAssignment] get_pick_face_assignment_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search pickFaceAssignments by filter

Returns the list of pickFaceAssignments that match the given filter.

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
api_instance = Infoplus.PickFaceAssignmentApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search pickFaceAssignments by filter
    api_response = api_instance.get_pick_face_assignment_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickFaceAssignmentApi->get_pick_face_assignment_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[PickFaceAssignment]**](PickFaceAssignment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pick_face_assignment_by_id**
> PickFaceAssignment get_pick_face_assignment_by_id(pick_face_assignment_id)

Get a pickFaceAssignment by id

Returns the pickFaceAssignment identified by the specified id.

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
api_instance = Infoplus.PickFaceAssignmentApi(Infoplus.ApiClient(configuration))
pick_face_assignment_id = 56 # int | Id of the pickFaceAssignment to be returned.

try:
    # Get a pickFaceAssignment by id
    api_response = api_instance.get_pick_face_assignment_by_id(pick_face_assignment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickFaceAssignmentApi->get_pick_face_assignment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pick_face_assignment_id** | **int**| Id of the pickFaceAssignment to be returned. | 

### Return type

[**PickFaceAssignment**](PickFaceAssignment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pick_face_assignment_tags**
> get_pick_face_assignment_tags(pick_face_assignment_id)

Get the tags for a pickFaceAssignment.

Get all existing pickFaceAssignment tags.

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
api_instance = Infoplus.PickFaceAssignmentApi(Infoplus.ApiClient(configuration))
pick_face_assignment_id = 56 # int | Id of the pickFaceAssignment to get tags for

try:
    # Get the tags for a pickFaceAssignment.
    api_instance.get_pick_face_assignment_tags(pick_face_assignment_id)
except ApiException as e:
    print("Exception when calling PickFaceAssignmentApi->get_pick_face_assignment_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pick_face_assignment_id** | **int**| Id of the pickFaceAssignment to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pick_face_assignment**
> update_pick_face_assignment(body)

Update a pickFaceAssignment

Updates an existing pickFaceAssignment using the specified data.

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
api_instance = Infoplus.PickFaceAssignmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.PickFaceAssignment() # PickFaceAssignment | PickFaceAssignment to be updated.

try:
    # Update a pickFaceAssignment
    api_instance.update_pick_face_assignment(body)
except ApiException as e:
    print("Exception when calling PickFaceAssignmentApi->update_pick_face_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PickFaceAssignment**](PickFaceAssignment.md)| PickFaceAssignment to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pick_face_assignment_custom_fields**
> update_pick_face_assignment_custom_fields(body)

Update a pickFaceAssignment custom fields

Updates an existing pickFaceAssignment custom fields using the specified data.

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
api_instance = Infoplus.PickFaceAssignmentApi(Infoplus.ApiClient(configuration))
body = Infoplus.PickFaceAssignment() # PickFaceAssignment | PickFaceAssignment to be updated.

try:
    # Update a pickFaceAssignment custom fields
    api_instance.update_pick_face_assignment_custom_fields(body)
except ApiException as e:
    print("Exception when calling PickFaceAssignmentApi->update_pick_face_assignment_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PickFaceAssignment**](PickFaceAssignment.md)| PickFaceAssignment to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

