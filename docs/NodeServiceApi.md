# madana_apiclient.NodeServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_node**](NodeServiceApi.md#create_node) | **POST** /nodes/v2 | 
[**get_bootstrap**](NodeServiceApi.md#get_bootstrap) | **GET** /nodes/bootstrap | 
[**get_node_licenses**](NodeServiceApi.md#get_node_licenses) | **GET** /nodes/licenses | 
[**get_node_v2**](NodeServiceApi.md#get_node_v2) | **GET** /nodes/v2/{ident} | 
[**get_nodes2**](NodeServiceApi.md#get_nodes2) | **GET** /nodes | 
[**get_nodes_v2**](NodeServiceApi.md#get_nodes_v2) | **GET** /nodes/v2 | Returns UUIDs of existing analyses.
[**kill_node**](NodeServiceApi.md#kill_node) | **POST** /nodes/v2/{ident}/kill | 
[**post_node_info**](NodeServiceApi.md#post_node_info) | **POST** /nodes | 
[**post_node_info_0**](NodeServiceApi.md#post_node_info_0) | **POST** /nodes/create | 


# **create_node**
> file_type create_node()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import node_service_api
from madana_apiclient.model.json_node_run_request import JsonNodeRunRequest
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
    body = JsonNodeRunRequest(
        cpu_count="cpu_count_example",
        subdomain="subdomain_example",
    ) # JsonNodeRunRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_node(body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling NodeServiceApi->create_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonNodeRunRequest**](JsonNodeRunRequest.md)|  | [optional]

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

# **get_node_licenses**
> file_type get_node_licenses()



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
    active = "true" # str |  (optional) if omitted the server will use the default value of "true"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_node_licenses(active=active)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling NodeServiceApi->get_node_licenses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **str**|  | [optional] if omitted the server will use the default value of "true"

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

# **get_node_v2**
> file_type get_node_v2(ident)



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
    ident = "ident_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_node_v2(ident)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling NodeServiceApi->get_node_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ident** | **str**|  |

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

# **get_nodes_v2**
> file_type get_nodes_v2()

Returns UUIDs of existing analyses.

Returns UUIDs of existing analyses.

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
    authorization = "Authorization_example" # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)
    created = "true" # str | - if Queryparam \"created=true\" only the UUIDs of own Requests are shown (optional) if omitted the server will use the default value of "true"
    limit = "30" # str | Used for offset pagination. Limit/Offset Paging would look like GET /request?limit=20&offset=100. This query would return the 20 rows starting with the 100th row (optional) if omitted the server will use the default value of "30"
    offset = "0" # str | Used for offset pagination. Limit/Offset Paging would look like GET /request?limit=20&offset=100. This query would return the 20 rows starting with the 100th row (optional) if omitted the server will use the default value of "0"
    status = "status_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns UUIDs of existing analyses.
        api_response = api_instance.get_nodes_v2(authorization=authorization, created=created, limit=limit, offset=offset, status=status)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling NodeServiceApi->get_nodes_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional]
 **created** | **str**| - if Queryparam \&quot;created&#x3D;true\&quot; only the UUIDs of own Requests are shown | [optional] if omitted the server will use the default value of "true"
 **limit** | **str**| Used for offset pagination. Limit/Offset Paging would look like GET /request?limit&#x3D;20&amp;offset&#x3D;100. This query would return the 20 rows starting with the 100th row | [optional] if omitted the server will use the default value of "30"
 **offset** | **str**| Used for offset pagination. Limit/Offset Paging would look like GET /request?limit&#x3D;20&amp;offset&#x3D;100. This query would return the 20 rows starting with the 100th row | [optional] if omitted the server will use the default value of "0"
 **status** | **str**|  | [optional]

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
**200** | If the actions could be loaded |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kill_node**
> file_type kill_node(ident)



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
    ident = "ident_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.kill_node(ident)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling NodeServiceApi->kill_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ident** | **str**|  |

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
        ipfs_info=JsonIPFSSystemInfo(
            public_key="public_key_example",
            id="id_example",
            protocol_version="protocol_version_example",
            swarm_connection="swarm_connection_example",
            agent_version="agent_version_example",
        ),
        cpu_logical_count=1,
        hardware_firmware="hardware_firmware_example",
        public_key="public_key_example",
        connection_url="connection_url_example",
        hardware_baseboard="hardware_baseboard_example",
        cpu_family="cpu_family_example",
        operating_system_uptime=3.14,
        sgx_info=JsonSGXInfo(
            status="status_example",
            version="version_example",
        ),
        cpu_model="cpu_model_example",
        memory="memory_example",
        operating_system="operating_system_example",
        status="status_example",
        cpu_frequency="cpu_frequency_example",
        processors=[
            "processors_example",
        ],
        owner="owner_example",
        cpu_physical_cores=1,
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

# **post_node_info_0**
> file_type post_node_info_0()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import node_service_api
from madana_apiclient.model.json_node_run_request import JsonNodeRunRequest
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
    body = JsonNodeRunRequest(
        cpu_count="cpu_count_example",
        subdomain="subdomain_example",
    ) # JsonNodeRunRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.post_node_info_0(body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling NodeServiceApi->post_node_info_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonNodeRunRequest**](JsonNodeRunRequest.md)|  | [optional]

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

