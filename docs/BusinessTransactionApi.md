# Infoplus.BusinessTransactionApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_business_transaction_audit**](BusinessTransactionApi.md#add_business_transaction_audit) | **PUT** /beta/businessTransaction/{businessTransactionId}/audit/{businessTransactionAudit} | Add new audit for a businessTransaction
[**add_business_transaction_tag**](BusinessTransactionApi.md#add_business_transaction_tag) | **PUT** /beta/businessTransaction/{businessTransactionId}/tag/{businessTransactionTag} | Add new tags for a businessTransaction.
[**delete_business_transaction_tag**](BusinessTransactionApi.md#delete_business_transaction_tag) | **DELETE** /beta/businessTransaction/{businessTransactionId}/tag/{businessTransactionTag} | Delete a tag for a businessTransaction.
[**get_business_transaction_by_filter**](BusinessTransactionApi.md#get_business_transaction_by_filter) | **GET** /beta/businessTransaction/search | Search businessTransactions by filter
[**get_business_transaction_by_id**](BusinessTransactionApi.md#get_business_transaction_by_id) | **GET** /beta/businessTransaction/{businessTransactionId} | Get a businessTransaction by id
[**get_business_transaction_tags**](BusinessTransactionApi.md#get_business_transaction_tags) | **GET** /beta/businessTransaction/{businessTransactionId}/tag | Get the tags for a businessTransaction.
[**get_duplicate_business_transaction_by_id**](BusinessTransactionApi.md#get_duplicate_business_transaction_by_id) | **GET** /beta/businessTransaction/duplicate/{businessTransactionId} | Get a duplicated a businessTransaction by id
[**update_business_transaction_custom_fields**](BusinessTransactionApi.md#update_business_transaction_custom_fields) | **PUT** /beta/businessTransaction/customFields | Update a businessTransaction custom fields


# **add_business_transaction_audit**
> add_business_transaction_audit(business_transaction_id, business_transaction_audit)

Add new audit for a businessTransaction

Adds an audit to an existing businessTransaction.

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
api_instance = Infoplus.BusinessTransactionApi(Infoplus.ApiClient(configuration))
business_transaction_id = 56 # int | Id of the businessTransaction to add an audit to
business_transaction_audit = 'business_transaction_audit_example' # str | The audit to add

try:
    # Add new audit for a businessTransaction
    api_instance.add_business_transaction_audit(business_transaction_id, business_transaction_audit)
except ApiException as e:
    print("Exception when calling BusinessTransactionApi->add_business_transaction_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_transaction_id** | **int**| Id of the businessTransaction to add an audit to | 
 **business_transaction_audit** | **str**| The audit to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_business_transaction_tag**
> add_business_transaction_tag(business_transaction_id, business_transaction_tag)

Add new tags for a businessTransaction.

Adds a tag to an existing businessTransaction.

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
api_instance = Infoplus.BusinessTransactionApi(Infoplus.ApiClient(configuration))
business_transaction_id = 56 # int | Id of the businessTransaction to add a tag to
business_transaction_tag = 'business_transaction_tag_example' # str | The tag to add

try:
    # Add new tags for a businessTransaction.
    api_instance.add_business_transaction_tag(business_transaction_id, business_transaction_tag)
except ApiException as e:
    print("Exception when calling BusinessTransactionApi->add_business_transaction_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_transaction_id** | **int**| Id of the businessTransaction to add a tag to | 
 **business_transaction_tag** | **str**| The tag to add | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_business_transaction_tag**
> delete_business_transaction_tag(business_transaction_id, business_transaction_tag)

Delete a tag for a businessTransaction.

Deletes an existing businessTransaction tag using the specified data.

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
api_instance = Infoplus.BusinessTransactionApi(Infoplus.ApiClient(configuration))
business_transaction_id = 56 # int | Id of the businessTransaction to remove tag from
business_transaction_tag = 'business_transaction_tag_example' # str | The tag to delete

try:
    # Delete a tag for a businessTransaction.
    api_instance.delete_business_transaction_tag(business_transaction_id, business_transaction_tag)
except ApiException as e:
    print("Exception when calling BusinessTransactionApi->delete_business_transaction_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_transaction_id** | **int**| Id of the businessTransaction to remove tag from | 
 **business_transaction_tag** | **str**| The tag to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_transaction_by_filter**
> list[BusinessTransaction] get_business_transaction_by_filter(filter=filter, page=page, limit=limit, sort=sort)

Search businessTransactions by filter

Returns the list of businessTransactions that match the given filter.

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
api_instance = Infoplus.BusinessTransactionApi(Infoplus.ApiClient(configuration))
filter = 'filter_example' # str | Query string, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)
sort = 'sort_example' # str | Sort results by specified field. (optional)

try:
    # Search businessTransactions by filter
    api_response = api_instance.get_business_transaction_by_filter(filter=filter, page=page, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessTransactionApi->get_business_transaction_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Query string, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 
 **sort** | **str**| Sort results by specified field. | [optional] 

### Return type

[**list[BusinessTransaction]**](BusinessTransaction.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_transaction_by_id**
> BusinessTransaction get_business_transaction_by_id(business_transaction_id)

Get a businessTransaction by id

Returns the businessTransaction identified by the specified id.

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
api_instance = Infoplus.BusinessTransactionApi(Infoplus.ApiClient(configuration))
business_transaction_id = 56 # int | Id of the businessTransaction to be returned.

try:
    # Get a businessTransaction by id
    api_response = api_instance.get_business_transaction_by_id(business_transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessTransactionApi->get_business_transaction_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_transaction_id** | **int**| Id of the businessTransaction to be returned. | 

### Return type

[**BusinessTransaction**](BusinessTransaction.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_transaction_tags**
> get_business_transaction_tags(business_transaction_id)

Get the tags for a businessTransaction.

Get all existing businessTransaction tags.

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
api_instance = Infoplus.BusinessTransactionApi(Infoplus.ApiClient(configuration))
business_transaction_id = 56 # int | Id of the businessTransaction to get tags for

try:
    # Get the tags for a businessTransaction.
    api_instance.get_business_transaction_tags(business_transaction_id)
except ApiException as e:
    print("Exception when calling BusinessTransactionApi->get_business_transaction_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_transaction_id** | **int**| Id of the businessTransaction to get tags for | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_duplicate_business_transaction_by_id**
> BusinessTransaction get_duplicate_business_transaction_by_id(business_transaction_id)

Get a duplicated a businessTransaction by id

Returns a duplicated businessTransaction identified by the specified id.

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
api_instance = Infoplus.BusinessTransactionApi(Infoplus.ApiClient(configuration))
business_transaction_id = 56 # int | Id of the businessTransaction to be duplicated.

try:
    # Get a duplicated a businessTransaction by id
    api_response = api_instance.get_duplicate_business_transaction_by_id(business_transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessTransactionApi->get_duplicate_business_transaction_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_transaction_id** | **int**| Id of the businessTransaction to be duplicated. | 

### Return type

[**BusinessTransaction**](BusinessTransaction.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_business_transaction_custom_fields**
> update_business_transaction_custom_fields(body)

Update a businessTransaction custom fields

Updates an existing businessTransaction custom fields using the specified data.

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
api_instance = Infoplus.BusinessTransactionApi(Infoplus.ApiClient(configuration))
body = Infoplus.BusinessTransaction() # BusinessTransaction | BusinessTransaction to be updated.

try:
    # Update a businessTransaction custom fields
    api_instance.update_business_transaction_custom_fields(body)
except ApiException as e:
    print("Exception when calling BusinessTransactionApi->update_business_transaction_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BusinessTransaction**](BusinessTransaction.md)| BusinessTransaction to be updated. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

