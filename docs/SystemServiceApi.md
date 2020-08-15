# madana_sampleclient_python.SystemServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_objects**](SystemServiceApi.md#get_all_objects) | **GET** /system/health | 
[**get_application**](SystemServiceApi.md#get_application) | **GET** /system/usage | Return the current application usage.


# **get_all_objects**
> file get_all_objects()



### Example

```python
from __future__ import print_function
import time
import madana_sampleclient_python
from madana_sampleclient_python.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with madana_sampleclient_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_sampleclient_python.SystemServiceApi(api_client)
    
    try:
        api_response = api_instance.get_all_objects()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemServiceApi->get_all_objects: %s\n" % e)
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

# **get_application**
> dict(str, object) get_application()

Return the current application usage.

Return the current application usage

### Example

```python
from __future__ import print_function
import time
import madana_sampleclient_python
from madana_sampleclient_python.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with madana_sampleclient_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_sampleclient_python.SystemServiceApi(api_client)
    
    try:
        # Return the current application usage.
        api_response = api_instance.get_application()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemServiceApi->get_application: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, object)**

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

