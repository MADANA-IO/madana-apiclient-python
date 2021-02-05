# madana_apiclient.NodeServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bootstrap**](NodeServiceApi.md#get_bootstrap) | **GET** /nodes/bootstrap | 
[**get_nodes2**](NodeServiceApi.md#get_nodes2) | **GET** /nodes | 
[**post_node_info**](NodeServiceApi.md#post_node_info) | **POST** /nodes | 


# **get_bootstrap**
> file_type get_bootstrap()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import node_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = node_service_api.NodeServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_bootstrap()
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling NodeServiceApi->get_bootstrap: %s\n" % e)
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

# **get_nodes2**
> file_type get_nodes2()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import node_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = node_service_api.NodeServiceApi(api_client)
    owner = "owner_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_nodes2(owner=owner)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling NodeServiceApi->get_nodes2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | [optional]

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

# **post_node_info**
> file_type post_node_info()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import node_service_api
from madana_apiclient.model.json_node_info import JsonNodeInfo
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = node_service_api.NodeServiceApi(api_client)
    body = JsonNodeInfo(
        status="status_example",
        cpu_physical_cores=1,
        processors=[
            "processors_example",
        ],
        owner="owner_example",
        hardware_baseboard="hardware_baseboard_example",
        hardware_firmware="hardware_firmware_example",
        public_key="public_key_example",
        cpu_logical_count=1,
        ipfs_info=JsonIPFSSystemInfo(
            agent_version="agent_version_example",
            swarm_connection="swarm_connection_example",
            public_key="public_key_example",
            id="id_example",
            protocol_version="protocol_version_example",
        ),
        cpu_frequency="cpu_frequency_example",
        memory="memory_example",
        cpu_family="cpu_family_example",
        cpu_model="cpu_model_example",
        sgx_info=JsonSGXInfo(
            version="version_example",
            status="status_example",
        ),
        operating_system="operating_system_example",
        operating_system_uptime=3.14,
        connection_url="connection_url_example",
    ) # JsonNodeInfo |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_node_info(body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling NodeServiceApi->post_node_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonNodeInfo**](JsonNodeInfo.md)|  | [optional]

### Return type

**file_type**

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

