# Infoplus.JobRecipeApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_job_recipe**](JobRecipeApi.md#add_job_recipe) | **POST** /beta/jobRecipe | Create a jobRecipe
[**add_job_recipe_audit**](JobRecipeApi.md#add_job_recipe_audit) | **PUT** /beta/jobRecipe/{jobRecipeId}/audit/{jobRecipeAudit} | Add new audit for a jobRecipe
[**add_job_recipe_file**](JobRecipeApi.md#add_job_recipe_file) | **POST** /beta/jobRecipe/{jobRecipeId}/file/{fileName} | Attach a file to a jobRecipe
[**add_job_recipe_tag**](JobRecipeApi.md#add_job_recipe_tag) | **PUT** /beta/jobRecipe/{jobRecipeId}/tag/{jobRecipeTag} | Add new tags for a jobRecipe.
[**delete_job_recipe**](JobRecipeApi.md#delete_job_recipe) | **DELETE** /beta/jobRecipe/{jobRecipeId} | Delete a jobRecipe
[**delete_job_recipe_tag**](JobRecipeApi.md#delete_job_recipe_tag) | **DELETE** /beta/jobRecipe/{jobRecipeId}/tag/{jobRecipeTag} | Delete a tag for a jobRecipe.
[**get_duplicate_job_recipe_by_id**](JobRecipeApi.md#get_duplicate_job_recipe_by_id) | **GET** /beta/jobRecipe/duplicate/{jobRecipeId} | Get a duplicated a jobRecipe by id
[**get_job_recipe_by_filter**](JobRecipeApi.md#get_job_recipe_by_filter) | **GET** /beta/jobRecipe/search | Search jobRecipes by filter
[**get_job_recipe_by_id**](JobRecipeApi.md#get_job_recipe_by_id) | **GET** /beta/jobRecipe/{jobRecipeId} | Get a jobRecipe by id
[**get_job_recipe_tags**](JobRecipeApi.md#get_job_recipe_tags) | **GET** /beta/jobRecipe/{jobRecipeId}/tag | Get the tags for a jobRecipe.
[**update_job_recipe**](JobRecipeApi.md#update_job_recipe) | **PUT** /beta/jobRecipe | Update a jobRecipe
[**update_job_recipe_custom_fields**](JobRecipeApi.md#update_job_recipe_custom_fields) | **PUT** /beta/jobRecipe/customFields | Update a jobRecipe custom fields


# **add_job_recipe**
> JobRecipe add_job_recipe(body)

Create a jobRecipe

Inserts a new jobRecipe using the specified data.

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
api_instance = Infoplus.JobRecipeApi(Infoplus.ApiClient(configuration))
body = Infoplus.JobRecipe() # JobRecipe | JobRecipe to be inserted.

try:
    # Create a jobRecipe
    api_response = api_instance.add_job_recipe(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobRecipeApi->add_job_recipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobRecipe**](JobRecipe.md)| JobRecipe to be inserted. | 

### Return type

[**JobRecipe**](JobRecipe.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_recipe_audit**
> add_job_recipe_audit(job_recipe_id, job_recipe_audit)

Add new audit for a jobRecipe

Adds an audit to an existing jobRecipe.

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
api_instance = Infoplus.JobRecipeApi(Infoplus.ApiClient(configuration))
job_recipe_id = 56 # int | Id of the jobRecipe to add an audit to
job_recipe_audit = 'job_recipe_audit_example' # str | The audit to add

try:
    # Add new audit for a jobRecipe
    api_instance.add_job_recipe_audit(job_recipe_id, job_recipe_audit)
except ApiException as e:
    print("Exception when calling JobRecipeApi->add_job_recipe_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_recipe_id** | **int**| Id of the jobRecipe to add an audit to | 
 **job_recipe_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_recipe_file**
> add_job_recipe_file(job_recipe_id, file_name)

Attach a file to a jobRecipe

Adds a file to an existing jobRecipe.

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
api_instance = Infoplus.JobRecipeApi(Infoplus.ApiClient(configuration))
job_recipe_id = 56 # int | Id of the jobRecipe to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a jobRecipe
    api_instance.add_job_recipe_file(job_recipe_id, file_name)
except ApiException as e:
    print("Exception when calling JobRecipeApi->add_job_recipe_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_recipe_id** | **int**| Id of the jobRecipe to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_recipe_tag**
> add_job_recipe_tag(job_recipe_id, job_recipe_tag)

Add new tags for a jobRecipe.

Adds a tag to an existing jobRecipe.

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
api_instance = Infoplus.JobRecipeApi(Infoplus.ApiClient(configuration))
job_recipe_id = 56 # int | Id of the jobRecipe to add a tag to
job_recipe_tag = 'job_recipe_tag_example' # str | The tag to add

try:
    # Add new tags for a jobRecipe.
    api_instance.add_job_recipe_tag(job_recipe_id, job_recipe_tag)
except ApiException as e:
    print("Exception when calling JobRecipeApi->add_job_recipe_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_recipe_id** | **int**| Id of the jobRecipe to add a tag to | 
 **job_recipe_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_recipe**
> delete_job_recipe(job_recipe_id)

Delete a jobRecipe

Deletes the jobRecipe identified by the specified id.

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
api_instance = Infoplus.JobRecipeApi(Infoplus.ApiClient(configuration))
job_recipe_id = 56 # int | Id of the jobRecipe to be deleted.

try:
    # Delete a jobRecipe
    api_instance.delete_job_recipe(job_recipe_id)
except ApiException as e:
    print("Exception when calling JobRecipeApi->delete_job_recipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_recipe_id** | **int**| Id of the jobRecipe to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_recipe_tag**
> delete_job_recipe_tag(job_recipe_id, job_recipe_tag)

Delete a tag for a jobRecipe.

Deletes an existing jobRecipe tag using the specified data.

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
api_instance = Infoplus.JobRecipeApi(Infoplus.ApiClient(configuration))
job_recipe_id = 56 # int | Id of the jobRecipe to remove tag from
job_recipe_tag = 'job_recipe_tag_example' # str | The tag to delete

try:
    # Delete a tag for a jobRecipe.
    api_instance.delete_job_recipe_tag(job_recipe_id, job_recipe_tag)
except ApiException as e:
    print("Exception when calling JobRecipeApi->delete_job_recipe_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_recipe_id** | **int**| Id of the jobRecipe to remove tag from | 
 **job_recipe_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_job_recipe_by_id**
> JobRecipe get_duplicate_job_recipe_by_id(job_recipe_id)

Get a duplicated a jobRecipe by id

Returns a duplicated jobRecipe identified by the specified id.

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
api_instance = Infoplus.JobRecipeApi(Infoplus.ApiClient(configuration))
job_recipe_id = 56 # int | Id of the jobRecipe to be duplicated.

try:
    # Get a duplicated a jobRecipe by id
    api_response = api_instance.get_duplicate_job_recipe_by_id(job_recipe_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobRecipeApi->get_duplicate_job_recipe_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_recipe_id** | **int**| Id of the jobRecipe to be duplicated. | 

### Return type

[**JobRecipe**](JobRecipe.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_recipe_by_filter**
> list[JobRecipe] get_job_recipe_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search jobRecipes by filter

Returns the list of jobRecipes that match the given filter.

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
api_instance = Infoplus.JobRecipeApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search jobRecipes by filter
    api_response = api_instance.get_job_recipe_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobRecipeApi->get_job_recipe_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[JobRecipe]**](JobRecipe.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_recipe_by_id**
> JobRecipe get_job_recipe_by_id(job_recipe_id)

Get a jobRecipe by id

Returns the jobRecipe identified by the specified id.

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
api_instance = Infoplus.JobRecipeApi(Infoplus.ApiClient(configuration))
job_recipe_id = 56 # int | Id of the jobRecipe to be returned.

try:
    # Get a jobRecipe by id
    api_response = api_instance.get_job_recipe_by_id(job_recipe_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobRecipeApi->get_job_recipe_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_recipe_id** | **int**| Id of the jobRecipe to be returned. | 

### Return type

[**JobRecipe**](JobRecipe.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_recipe_tags**
> get_job_recipe_tags(job_recipe_id)

Get the tags for a jobRecipe.

Get all existing jobRecipe tags.

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
api_instance = Infoplus.JobRecipeApi(Infoplus.ApiClient(configuration))
job_recipe_id = 56 # int | Id of the jobRecipe to get tags for

try:
    # Get the tags for a jobRecipe.
    api_instance.get_job_recipe_tags(job_recipe_id)
except ApiException as e:
    print("Exception when calling JobRecipeApi->get_job_recipe_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_recipe_id** | **int**| Id of the jobRecipe to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_recipe**
> update_job_recipe(body)

Update a jobRecipe

Updates an existing jobRecipe using the specified data.

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
api_instance = Infoplus.JobRecipeApi(Infoplus.ApiClient(configuration))
body = Infoplus.JobRecipe() # JobRecipe | JobRecipe to be updated.

try:
    # Update a jobRecipe
    api_instance.update_job_recipe(body)
except ApiException as e:
    print("Exception when calling JobRecipeApi->update_job_recipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobRecipe**](JobRecipe.md)| JobRecipe to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_recipe_custom_fields**
> update_job_recipe_custom_fields(body)

Update a jobRecipe custom fields

Updates an existing jobRecipe custom fields using the specified data.

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
api_instance = Infoplus.JobRecipeApi(Infoplus.ApiClient(configuration))
body = Infoplus.JobRecipe() # JobRecipe | JobRecipe to be updated.

try:
    # Update a jobRecipe custom fields
    api_instance.update_job_recipe_custom_fields(body)
except ApiException as e:
    print("Exception when calling JobRecipeApi->update_job_recipe_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobRecipe**](JobRecipe.md)| JobRecipe to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

