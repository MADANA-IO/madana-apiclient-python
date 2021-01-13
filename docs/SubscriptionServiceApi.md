# madana_apiclient.SubscriptionServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_free_subscription**](SubscriptionServiceApi.md#add_free_subscription) | **POST** /subscriptions/free | 
[**get_application**](SubscriptionServiceApi.md#get_application) | **GET** /subscriptions/active | 


# **add_free_subscription**
> file_type add_free_subscription()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import subscription_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = subscription_service_api.SubscriptionServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.add_free_subscription()
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling SubscriptionServiceApi->add_free_subscription: %s\n" % e)
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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> file_type get_application()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import subscription_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = subscription_service_api.SubscriptionServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_application()
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling SubscriptionServiceApi->get_application: %s\n" % e)
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

