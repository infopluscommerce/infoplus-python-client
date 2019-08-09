# Infoplus.VendorComplianceSurveyApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_vendor_compliance_survey**](VendorComplianceSurveyApi.md#add_vendor_compliance_survey) | **POST** /beta/vendorComplianceSurvey | Create a vendorComplianceSurvey
[**add_vendor_compliance_survey_audit**](VendorComplianceSurveyApi.md#add_vendor_compliance_survey_audit) | **PUT** /beta/vendorComplianceSurvey/{vendorComplianceSurveyId}/audit/{vendorComplianceSurveyAudit} | Add new audit for a vendorComplianceSurvey
[**add_vendor_compliance_survey_file**](VendorComplianceSurveyApi.md#add_vendor_compliance_survey_file) | **POST** /beta/vendorComplianceSurvey/{vendorComplianceSurveyId}/file/{fileName} | Attach a file to a vendorComplianceSurvey
[**add_vendor_compliance_survey_tag**](VendorComplianceSurveyApi.md#add_vendor_compliance_survey_tag) | **PUT** /beta/vendorComplianceSurvey/{vendorComplianceSurveyId}/tag/{vendorComplianceSurveyTag} | Add new tags for a vendorComplianceSurvey.
[**delete_vendor_compliance_survey**](VendorComplianceSurveyApi.md#delete_vendor_compliance_survey) | **DELETE** /beta/vendorComplianceSurvey/{vendorComplianceSurveyId} | Delete a vendorComplianceSurvey
[**delete_vendor_compliance_survey_tag**](VendorComplianceSurveyApi.md#delete_vendor_compliance_survey_tag) | **DELETE** /beta/vendorComplianceSurvey/{vendorComplianceSurveyId}/tag/{vendorComplianceSurveyTag} | Delete a tag for a vendorComplianceSurvey.
[**get_duplicate_vendor_compliance_survey_by_id**](VendorComplianceSurveyApi.md#get_duplicate_vendor_compliance_survey_by_id) | **GET** /beta/vendorComplianceSurvey/duplicate/{vendorComplianceSurveyId} | Get a duplicated a vendorComplianceSurvey by id
[**get_vendor_compliance_survey_by_filter**](VendorComplianceSurveyApi.md#get_vendor_compliance_survey_by_filter) | **GET** /beta/vendorComplianceSurvey/search | Search vendorComplianceSurveys by filter
[**get_vendor_compliance_survey_by_id**](VendorComplianceSurveyApi.md#get_vendor_compliance_survey_by_id) | **GET** /beta/vendorComplianceSurvey/{vendorComplianceSurveyId} | Get a vendorComplianceSurvey by id
[**get_vendor_compliance_survey_tags**](VendorComplianceSurveyApi.md#get_vendor_compliance_survey_tags) | **GET** /beta/vendorComplianceSurvey/{vendorComplianceSurveyId}/tag | Get the tags for a vendorComplianceSurvey.
[**update_vendor_compliance_survey**](VendorComplianceSurveyApi.md#update_vendor_compliance_survey) | **PUT** /beta/vendorComplianceSurvey | Update a vendorComplianceSurvey
[**update_vendor_compliance_survey_custom_fields**](VendorComplianceSurveyApi.md#update_vendor_compliance_survey_custom_fields) | **PUT** /beta/vendorComplianceSurvey/customFields | Update a vendorComplianceSurvey custom fields


# **add_vendor_compliance_survey**
> VendorComplianceSurvey add_vendor_compliance_survey(body)

Create a vendorComplianceSurvey

Inserts a new vendorComplianceSurvey using the specified data.

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
api_instance = Infoplus.VendorComplianceSurveyApi(Infoplus.ApiClient(configuration))
body = Infoplus.VendorComplianceSurvey() # VendorComplianceSurvey | VendorComplianceSurvey to be inserted.

try:
    # Create a vendorComplianceSurvey
    api_response = api_instance.add_vendor_compliance_survey(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorComplianceSurveyApi->add_vendor_compliance_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VendorComplianceSurvey**](VendorComplianceSurvey.md)| VendorComplianceSurvey to be inserted. | 

### Return type

[**VendorComplianceSurvey**](VendorComplianceSurvey.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_vendor_compliance_survey_audit**
> add_vendor_compliance_survey_audit(vendor_compliance_survey_id, vendor_compliance_survey_audit)

Add new audit for a vendorComplianceSurvey

Adds an audit to an existing vendorComplianceSurvey.

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
api_instance = Infoplus.VendorComplianceSurveyApi(Infoplus.ApiClient(configuration))
vendor_compliance_survey_id = 56 # int | Id of the vendorComplianceSurvey to add an audit to
vendor_compliance_survey_audit = 'vendor_compliance_survey_audit_example' # str | The audit to add

try:
    # Add new audit for a vendorComplianceSurvey
    api_instance.add_vendor_compliance_survey_audit(vendor_compliance_survey_id, vendor_compliance_survey_audit)
except ApiException as e:
    print("Exception when calling VendorComplianceSurveyApi->add_vendor_compliance_survey_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_compliance_survey_id** | **int**| Id of the vendorComplianceSurvey to add an audit to | 
 **vendor_compliance_survey_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_vendor_compliance_survey_file**
> add_vendor_compliance_survey_file(vendor_compliance_survey_id, file_name)

Attach a file to a vendorComplianceSurvey

Adds a file to an existing vendorComplianceSurvey.

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
api_instance = Infoplus.VendorComplianceSurveyApi(Infoplus.ApiClient(configuration))
vendor_compliance_survey_id = 56 # int | Id of the vendorComplianceSurvey to add a file to
file_name = 'file_name_example' # str | Name of file

try:
    # Attach a file to a vendorComplianceSurvey
    api_instance.add_vendor_compliance_survey_file(vendor_compliance_survey_id, file_name)
except ApiException as e:
    print("Exception when calling VendorComplianceSurveyApi->add_vendor_compliance_survey_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_compliance_survey_id** | **int**| Id of the vendorComplianceSurvey to add a file to | 
 **file_name** | **str**| Name of file | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_vendor_compliance_survey_tag**
> add_vendor_compliance_survey_tag(vendor_compliance_survey_id, vendor_compliance_survey_tag)

Add new tags for a vendorComplianceSurvey.

Adds a tag to an existing vendorComplianceSurvey.

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
api_instance = Infoplus.VendorComplianceSurveyApi(Infoplus.ApiClient(configuration))
vendor_compliance_survey_id = 56 # int | Id of the vendorComplianceSurvey to add a tag to
vendor_compliance_survey_tag = 'vendor_compliance_survey_tag_example' # str | The tag to add

try:
    # Add new tags for a vendorComplianceSurvey.
    api_instance.add_vendor_compliance_survey_tag(vendor_compliance_survey_id, vendor_compliance_survey_tag)
except ApiException as e:
    print("Exception when calling VendorComplianceSurveyApi->add_vendor_compliance_survey_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_compliance_survey_id** | **int**| Id of the vendorComplianceSurvey to add a tag to | 
 **vendor_compliance_survey_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vendor_compliance_survey**
> delete_vendor_compliance_survey(vendor_compliance_survey_id)

Delete a vendorComplianceSurvey

Deletes the vendorComplianceSurvey identified by the specified id.

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
api_instance = Infoplus.VendorComplianceSurveyApi(Infoplus.ApiClient(configuration))
vendor_compliance_survey_id = 56 # int | Id of the vendorComplianceSurvey to be deleted.

try:
    # Delete a vendorComplianceSurvey
    api_instance.delete_vendor_compliance_survey(vendor_compliance_survey_id)
except ApiException as e:
    print("Exception when calling VendorComplianceSurveyApi->delete_vendor_compliance_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_compliance_survey_id** | **int**| Id of the vendorComplianceSurvey to be deleted. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vendor_compliance_survey_tag**
> delete_vendor_compliance_survey_tag(vendor_compliance_survey_id, vendor_compliance_survey_tag)

Delete a tag for a vendorComplianceSurvey.

Deletes an existing vendorComplianceSurvey tag using the specified data.

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
api_instance = Infoplus.VendorComplianceSurveyApi(Infoplus.ApiClient(configuration))
vendor_compliance_survey_id = 56 # int | Id of the vendorComplianceSurvey to remove tag from
vendor_compliance_survey_tag = 'vendor_compliance_survey_tag_example' # str | The tag to delete

try:
    # Delete a tag for a vendorComplianceSurvey.
    api_instance.delete_vendor_compliance_survey_tag(vendor_compliance_survey_id, vendor_compliance_survey_tag)
except ApiException as e:
    print("Exception when calling VendorComplianceSurveyApi->delete_vendor_compliance_survey_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_compliance_survey_id** | **int**| Id of the vendorComplianceSurvey to remove tag from | 
 **vendor_compliance_survey_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_vendor_compliance_survey_by_id**
> VendorComplianceSurvey get_duplicate_vendor_compliance_survey_by_id(vendor_compliance_survey_id)

Get a duplicated a vendorComplianceSurvey by id

Returns a duplicated vendorComplianceSurvey identified by the specified id.

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
api_instance = Infoplus.VendorComplianceSurveyApi(Infoplus.ApiClient(configuration))
vendor_compliance_survey_id = 56 # int | Id of the vendorComplianceSurvey to be duplicated.

try:
    # Get a duplicated a vendorComplianceSurvey by id
    api_response = api_instance.get_duplicate_vendor_compliance_survey_by_id(vendor_compliance_survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorComplianceSurveyApi->get_duplicate_vendor_compliance_survey_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_compliance_survey_id** | **int**| Id of the vendorComplianceSurvey to be duplicated. | 

### Return type

[**VendorComplianceSurvey**](VendorComplianceSurvey.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_compliance_survey_by_filter**
> list[VendorComplianceSurvey] get_vendor_compliance_survey_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search vendorComplianceSurveys by filter

Returns the list of vendorComplianceSurveys that match the given filter.

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
api_instance = Infoplus.VendorComplianceSurveyApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search vendorComplianceSurveys by filter
    api_response = api_instance.get_vendor_compliance_survey_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorComplianceSurveyApi->get_vendor_compliance_survey_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[VendorComplianceSurvey]**](VendorComplianceSurvey.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_compliance_survey_by_id**
> VendorComplianceSurvey get_vendor_compliance_survey_by_id(vendor_compliance_survey_id)

Get a vendorComplianceSurvey by id

Returns the vendorComplianceSurvey identified by the specified id.

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
api_instance = Infoplus.VendorComplianceSurveyApi(Infoplus.ApiClient(configuration))
vendor_compliance_survey_id = 56 # int | Id of the vendorComplianceSurvey to be returned.

try:
    # Get a vendorComplianceSurvey by id
    api_response = api_instance.get_vendor_compliance_survey_by_id(vendor_compliance_survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorComplianceSurveyApi->get_vendor_compliance_survey_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_compliance_survey_id** | **int**| Id of the vendorComplianceSurvey to be returned. | 

### Return type

[**VendorComplianceSurvey**](VendorComplianceSurvey.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_compliance_survey_tags**
> get_vendor_compliance_survey_tags(vendor_compliance_survey_id)

Get the tags for a vendorComplianceSurvey.

Get all existing vendorComplianceSurvey tags.

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
api_instance = Infoplus.VendorComplianceSurveyApi(Infoplus.ApiClient(configuration))
vendor_compliance_survey_id = 56 # int | Id of the vendorComplianceSurvey to get tags for

try:
    # Get the tags for a vendorComplianceSurvey.
    api_instance.get_vendor_compliance_survey_tags(vendor_compliance_survey_id)
except ApiException as e:
    print("Exception when calling VendorComplianceSurveyApi->get_vendor_compliance_survey_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_compliance_survey_id** | **int**| Id of the vendorComplianceSurvey to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vendor_compliance_survey**
> update_vendor_compliance_survey(body)

Update a vendorComplianceSurvey

Updates an existing vendorComplianceSurvey using the specified data.

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
api_instance = Infoplus.VendorComplianceSurveyApi(Infoplus.ApiClient(configuration))
body = Infoplus.VendorComplianceSurvey() # VendorComplianceSurvey | VendorComplianceSurvey to be updated.

try:
    # Update a vendorComplianceSurvey
    api_instance.update_vendor_compliance_survey(body)
except ApiException as e:
    print("Exception when calling VendorComplianceSurveyApi->update_vendor_compliance_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VendorComplianceSurvey**](VendorComplianceSurvey.md)| VendorComplianceSurvey to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vendor_compliance_survey_custom_fields**
> update_vendor_compliance_survey_custom_fields(body)

Update a vendorComplianceSurvey custom fields

Updates an existing vendorComplianceSurvey custom fields using the specified data.

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
api_instance = Infoplus.VendorComplianceSurveyApi(Infoplus.ApiClient(configuration))
body = Infoplus.VendorComplianceSurvey() # VendorComplianceSurvey | VendorComplianceSurvey to be updated.

try:
    # Update a vendorComplianceSurvey custom fields
    api_instance.update_vendor_compliance_survey_custom_fields(body)
except ApiException as e:
    print("Exception when calling VendorComplianceSurveyApi->update_vendor_compliance_survey_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VendorComplianceSurvey**](VendorComplianceSurvey.md)| VendorComplianceSurvey to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

