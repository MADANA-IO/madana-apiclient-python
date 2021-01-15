# madana_apiclient.InvoiceServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_billing_portal_url**](InvoiceServiceApi.md#get_billing_portal_url) | **GET** /invoices/portal | 
[**get_invoices**](InvoiceServiceApi.md#get_invoices) | **GET** /invoices | 


# **get_billing_portal_url**
> file_type get_billing_portal_url()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import invoice_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = invoice_service_api.InvoiceServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_billing_portal_url()
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling InvoiceServiceApi->get_billing_portal_url: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> file_type get_invoices()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import invoice_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = invoice_service_api.InvoiceServiceApi(api_client)
    dayssince = "366" # str |  (optional) if omitted the server will use the default value of "366"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_invoices(dayssince=dayssince)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling InvoiceServiceApi->get_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dayssince** | **str**|  | [optional] if omitted the server will use the default value of "366"

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

