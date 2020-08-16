# madana_apiclient.CertificateServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_certificate**](CertificateServiceApi.md#authenticate_certificate) | **POST** /certificates | Issues certificates for logged-in users.
[**get_certificate**](CertificateServiceApi.md#get_certificate) | **GET** /certificates/root | 
[**get_certificate_0**](CertificateServiceApi.md#get_certificate_0) | **GET** /certificates/{fingerprint} | 


# **authenticate_certificate**
> JsonMDNCertificate authenticate_certificate(body=body)

Issues certificates for logged-in users.

Issues certificates for logged-in users

### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.CertificateServiceApi(api_client)
    body = madana_apiclient.JsonMDNData() # JsonMDNData |  (optional)

    try:
        # Issues certificates for logged-in users.
        api_response = api_instance.authenticate_certificate(body=body)
        pprint(api_response)
    except ApiException as e:
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

# **get_certificate**
> file get_certificate()



### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.CertificateServiceApi(api_client)
    
    try:
        api_response = api_instance.get_certificate()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CertificateServiceApi->get_certificate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**file**

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

# **get_certificate_0**
> file get_certificate_0(fingerprint)



### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.CertificateServiceApi(api_client)
    fingerprint = 'fingerprint_example' # str | 

    try:
        api_response = api_instance.get_certificate_0(fingerprint)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CertificateServiceApi->get_certificate_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fingerprint** | **str**|  | 

### Return type

**file**

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

