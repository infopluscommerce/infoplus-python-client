# Infoplus.ReportApi

All URIs are relative to *https://kingsrook.localhost-testsubdomain1.infopluswms.com:8443/infoplus-wms/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_report**](ReportApi.md#run_report) | **GET** /v3.0/report/{reportId}/runReport | Run a specified report


# **run_report**
> run_report(report_id, format)

Run a specified report

Run a specified report

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
api_instance = Infoplus.ReportApi(Infoplus.ApiClient(configuration))
report_id = 56 # int | Id of the report to run.
format = 'format_example' # str | Format of the report.

try:
    # Run a specified report
    api_instance.run_report(report_id, format)
except ApiException as e:
    print("Exception when calling ReportApi->run_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **int**| Id of the report to run. | 
 **format** | **str**| Format of the report. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

