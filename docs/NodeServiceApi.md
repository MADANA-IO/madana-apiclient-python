# madana_sampleclient_python.NodeServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nodes2**](NodeServiceApi.md#get_nodes2) | **GET** /nodes | 
[**post_node_info**](NodeServiceApi.md#post_node_info) | **POST** /nodes | 


# **get_nodes2**
> file get_nodes2()



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
    api_instance = madana_sampleclient_python.NodeServiceApi(api_client)
    
    try:
        api_response = api_instance.get_nodes2()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NodeServiceApi->get_nodes2: %s\n" % e)
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

# **post_node_info**
> file post_node_info(body=body)



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
    api_instance = madana_sampleclient_python.NodeServiceApi(api_client)
    body = madana_sampleclient_python.JsonNodeInfo() # JsonNodeInfo |  (optional)

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

