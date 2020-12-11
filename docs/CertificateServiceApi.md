# madana_apiclient.CertificateServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_certificate**](CertificateServiceApi.md#authenticate_certificate) | **POST** /certificates | Issues certificates for logged-in users.
[**get_certificate_by_fingerprint**](CertificateServiceApi.md#get_certificate_by_fingerprint) | **GET** /certificates/{fingerprint} | 
[**get_root_certificate**](CertificateServiceApi.md#get_root_certificate) | **GET** /certificates/root | 


# **authenticate_certificate**
> JsonMDNCertificate authenticate_certificate()

Issues certificates for logged-in users.

Issues certificates for logged-in users

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import certificate_service_api
from madana_apiclient.model.json_mdn_certificate import JsonMDNCertificate
from madana_apiclient.model.json_mdn_data import JsonMDNData
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_service_api.CertificateServiceApi(api_client)
    body = JsonMDNData(
        data="data_example",
    ) # JsonMDNData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Issues certificates for logged-in users.
        api_response = api_instance.authenticate_certificate(body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling CertificateServiceApi->authenticate_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonMDNData**](JsonMDNData.md)|  | [optional]

### Return type

[**JsonMDNCertificate**](JsonMDNCertificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the Request have been signed could be verified |  -  |
**403** | If an error occurs |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_by_fingerprint**
> file_type get_certificate_by_fingerprint(fingerprint)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import certificate_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_service_api.CertificateServiceApi(api_client)
    fingerprint = "fingerprint_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_certificate_by_fingerprint(fingerprint)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling CertificateServiceApi->get_certificate_by_fingerprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fingerprint** | **str**|  |

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

# **get_root_certificate**
> file_type get_root_certificate()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import certificate_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_service_api.CertificateServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_root_certificate()
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling CertificateServiceApi->get_root_certificate: %s\n" % e)
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

