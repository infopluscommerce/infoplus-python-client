# Infoplus.ManifestPartnerApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_manifest_partner_by_search_text**](ManifestPartnerApi.md#get_manifest_partner_by_search_text) | **GET** /beta/manifestPartner/search | Search manifestPartners
[**get_manifest_solution_provider_by_id**](ManifestPartnerApi.md#get_manifest_solution_provider_by_id) | **GET** /beta/manifestPartner/{manifestPartnerId} | Get a manifestPartner by id


# **get_manifest_partner_by_search_text**
> list[ManifestPartner] get_manifest_partner_by_search_text(search_text=search_text, page=page, limit=limit)

Search manifestPartners

Returns the list of manifestPartners that match the given searchText.

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
api_instance = Infoplus.ManifestPartnerApi(Infoplus.ApiClient(configuration))
search_text = 'search_text_example' # str | Search text, used to filter results. (optional)
page = 56 # int | Result page number.  Defaults to 1. (optional)
limit = 56 # int | Maximum results per page.  Defaults to 20.  Max allowed value is 250. (optional)

try:
    # Search manifestPartners
    api_response = api_instance.get_manifest_partner_by_search_text(search_text=search_text, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManifestPartnerApi->get_manifest_partner_by_search_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | **str**| Search text, used to filter results. | [optional] 
 **page** | **int**| Result page number.  Defaults to 1. | [optional] 
 **limit** | **int**| Maximum results per page.  Defaults to 20.  Max allowed value is 250. | [optional] 

### Return type

[**list[ManifestPartner]**](ManifestPartner.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manifest_solution_provider_by_id**
> ManifestPartner get_manifest_solution_provider_by_id(manifest_partner_id)

Get a manifestPartner by id

Returns the manifestPartner identified by the specified id.

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
api_instance = Infoplus.ManifestPartnerApi(Infoplus.ApiClient(configuration))
manifest_partner_id = 'manifest_partner_id_example' # str | Id of manifestPartner to be returned.

try:
    # Get a manifestPartner by id
    api_response = api_instance.get_manifest_solution_provider_by_id(manifest_partner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManifestPartnerApi->get_manifest_solution_provider_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_partner_id** | **str**| Id of manifestPartner to be returned. | 

### Return type

[**ManifestPartner**](ManifestPartner.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

