# madana_apiclient.NodeServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bootstrap**](NodeServiceApi.md#get_bootstrap) | **GET** /nodes/bootstrap | 
[**get_nodes2**](NodeServiceApi.md#get_nodes2) | **GET** /nodes | 
[**post_node_info**](NodeServiceApi.md#post_node_info) | **POST** /nodes | 


# **get_bootstrap**
> file get_bootstrap()



### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.NodeServiceApi(api_client)
    
    try:
        api_response = api_instance.get_bootstrap()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NodeServiceApi->get_bootstrap: %s\n" % e)
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

# **get_nodes2**
> file get_nodes2(owner=owner)



### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.NodeServiceApi(api_client)
    owner = 'owner_example' # str |  (optional)

    try:
        api_response = api_instance.get_nodes2(owner=owner)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NodeServiceApi->get_nodes2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | [optional] 

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

# **post_node_info**
> file post_node_info(body=body)



### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.NodeServiceApi(api_client)
    body = madana_apiclient.JsonNodeInfo() # JsonNodeInfo |  (optional)

    try:
        api_response = api_instance.post_node_info(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NodeServiceApi->post_node_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonNodeInfo**](JsonNodeInfo.md)|  | [optional] 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

