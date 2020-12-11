# madana_apiclient.SystemServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_objects**](SystemServiceApi.md#get_all_objects) | **GET** /system/health | 
[**get_application**](SystemServiceApi.md#get_application) | **GET** /system/usage | Return the current application usage.


# **get_all_objects**
> file_type get_all_objects()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import system_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_service_api.SystemServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_all_objects()
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling SystemServiceApi->get_all_objects: %s\n" % e)
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

# **get_application**
> {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)} get_application()

Return the current application usage.

Return the current application usage

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import system_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_service_api.SystemServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Return the current application usage.
        api_response = api_instance.get_application()
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling SystemServiceApi->get_application: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the usage could be generated |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

