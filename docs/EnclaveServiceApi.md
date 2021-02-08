# madana_apiclient.EnclaveServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_history**](EnclaveServiceApi.md#add_history) | **POST** /enclaves/{uuid}/history | 
[**approve_enclave**](EnclaveServiceApi.md#approve_enclave) | **POST** /enclaves/{uuid}/approval | 
[**assign_enclave_agent**](EnclaveServiceApi.md#assign_enclave_agent) | **POST** /enclaves/{uuid}/assign | 
[**attestate_enclave**](EnclaveServiceApi.md#attestate_enclave) | **POST** /enclaves/{uuid}/attestation | 
[**create_enclave_run_request**](EnclaveServiceApi.md#create_enclave_run_request) | **POST** /enclaves | 
[**get_enclave**](EnclaveServiceApi.md#get_enclave) | **GET** /enclaves/{uuid} | 
[**get_enclave_types**](EnclaveServiceApi.md#get_enclave_types) | **GET** /enclaves/types | 
[**get_enclaves**](EnclaveServiceApi.md#get_enclaves) | **GET** /enclaves | Returns UUIDs of existing analyses.
[**get_stats**](EnclaveServiceApi.md#get_stats) | **GET** /enclaves/stats | 
[**kill_enclave**](EnclaveServiceApi.md#kill_enclave) | **POST** /enclaves/{uuid}/kill | 


# **add_history**
> file_type add_history(uuid)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import enclave_service_api
from madana_apiclient.model.json_signed_data import JsonSignedData
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enclave_service_api.EnclaveServiceApi(api_client)
    uuid = "uuid_example" # str | 
    body = JsonSignedData(
        fingerpint="fingerpint_example",
        signature="signature_example",
        data="data_example",
    ) # JsonSignedData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_history(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnclaveServiceApi->add_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_history(uuid, body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnclaveServiceApi->add_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **body** | [**JsonSignedData**](JsonSignedData.md)|  | [optional]

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_enclave**
> file_type approve_enclave(uuid)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import enclave_service_api
from madana_apiclient.model.json_enclave_running_attestation_approval import JsonEnclaveRunningAttestationApproval
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enclave_service_api.EnclaveServiceApi(api_client)
    uuid = "uuid_example" # str | 
    body = JsonEnclaveRunningAttestationApproval() # JsonEnclaveRunningAttestationApproval |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.approve_enclave(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnclaveServiceApi->approve_enclave: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.approve_enclave(uuid, body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnclaveServiceApi->approve_enclave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **body** | [**JsonEnclaveRunningAttestationApproval**](JsonEnclaveRunningAttestationApproval.md)|  | [optional]

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_enclave_agent**
> file_type assign_enclave_agent(uuid)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import enclave_service_api
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
    api_instance = enclave_service_api.EnclaveServiceApi(api_client)
    uuid = "uuid_example" # str | 
    body = JsonNodeInfo(
        cpu_model="cpu_model_example",
        operating_system_uptime=3.14,
        cpu_logical_count=1,
        owner="owner_example",
        operating_system="operating_system_example",
        status="status_example",
        memory="memory_example",
        hardware_firmware="hardware_firmware_example",
        cpu_frequency="cpu_frequency_example",
        processors=[
            "processors_example",
        ],
        cpu_family="cpu_family_example",
        sgx_info=JsonSGXInfo(
            version="version_example",
            status="status_example",
        ),
        public_key="public_key_example",
        ipfs_info=JsonIPFSSystemInfo(
            id="id_example",
            protocol_version="protocol_version_example",
            agent_version="agent_version_example",
            swarm_connection="swarm_connection_example",
            public_key="public_key_example",
        ),
        cpu_physical_cores=1,
        connection_url="connection_url_example",
        hardware_baseboard="hardware_baseboard_example",
    ) # JsonNodeInfo |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.assign_enclave_agent(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnclaveServiceApi->assign_enclave_agent: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.assign_enclave_agent(uuid, body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnclaveServiceApi->assign_enclave_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **body** | [**JsonNodeInfo**](JsonNodeInfo.md)|  | [optional]

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attestate_enclave**
> file_type attestate_enclave(uuid)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import enclave_service_api
from madana_apiclient.model.json_enclave_running_attestation import JsonEnclaveRunningAttestation
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enclave_service_api.EnclaveServiceApi(api_client)
    uuid = "uuid_example" # str | 
    body = JsonEnclaveRunningAttestation(
        enclave_process=JsonEnclaveProcess(
            enclave_ident="enclave_ident_example",
            internal_wireguard_server="internal_wireguard_server_example",
            process=JsonProcess(
                error_stream={},
                input_stream={},
                output_stream={},
                alive=True,
            ),
            signer_ident="signer_ident_example",
            ports=[
                JsonEnclavePort(
                    name="name_example",
                    protocol="protocol_example",
                    port="port_example",
                ),
            ],
            enclave_inputstream={},
            remote_control_server="remote_control_server_example",
            ending_time="ending_time_example",
            console_output="console_output_example",
            internal_remote_control_server="internal_remote_control_server_example",
            attestation_server="attestation_server_example",
            port_mapping={
                "key": "key_example",
            },
            internal_ident="internal_ident_example",
            kubernetes_enclave=JsonKubernetesEnclave(),
            status="status_example",
            public_ident="public_ident_example",
            startup_time="startup_time_example",
            environment=JsonEnvironment(
                content=[
                    "content_example",
                ],
                uuid="uuid_example",
                roothash="roothash_example",
                root_hash_offset="root_hash_offset_example",
                default_run_configuration=JsonRunConfig(
                    environment={
                        "key": "key_example",
                    },
                    disk_config=[
                        JsonDiskConfig(
                            readonly=True,
                            disk="disk_example",
                            roothash_offset=1,
                            roothash="roothash_example",
                        ),
                    ],
                    run="run_example",
                    args=[
                        "args_example",
                    ],
                ),
                ipfs_hash="ipfs_hash_example",
                description="description_example",
                published=True,
                name="name_example",
                packages=[
                    "packages_example",
                ],
                size="size_example",
            ),
            wg_interface=JsonWireguardInterface(),
            startup_cmd="startup_cmd_example",
            wireguard_server="wireguard_server_example",
            internal_attesation_server="internal_attesation_server_example",
            wireguard_public_key="wireguard_public_key_example",
        ),
        node_info=JsonNodeInfo(
            cpu_model="cpu_model_example",
            operating_system_uptime=3.14,
            cpu_logical_count=1,
            owner="owner_example",
            operating_system="operating_system_example",
            status="status_example",
            memory="memory_example",
            hardware_firmware="hardware_firmware_example",
            cpu_frequency="cpu_frequency_example",
            processors=[
                "processors_example",
            ],
            cpu_family="cpu_family_example",
            sgx_info=JsonSGXInfo(
                version="version_example",
                status="status_example",
            ),
            public_key="public_key_example",
            ipfs_info=JsonIPFSSystemInfo(
                id="id_example",
                protocol_version="protocol_version_example",
                agent_version="agent_version_example",
                swarm_connection="swarm_connection_example",
                public_key="public_key_example",
            ),
            cpu_physical_cores=1,
            connection_url="connection_url_example",
            hardware_baseboard="hardware_baseboard_example",
        ),
    ) # JsonEnclaveRunningAttestation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.attestate_enclave(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnclaveServiceApi->attestate_enclave: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.attestate_enclave(uuid, body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnclaveServiceApi->attestate_enclave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **body** | [**JsonEnclaveRunningAttestation**](JsonEnclaveRunningAttestation.md)|  | [optional]

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_enclave_run_request**
> file_type create_enclave_run_request()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import enclave_service_api
from madana_apiclient.model.json_enclave_run_request import JsonEnclaveRunRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enclave_service_api.EnclaveServiceApi(api_client)
    body = JsonEnclaveRunRequest(
        wireguard_public_key="wireguard_public_key_example",
        ports=[
            JsonEnclavePort(
                name="name_example",
                protocol="protocol_example",
                port="port_example",
            ),
        ],
        using_default_run_config=True,
        enclave_execution_type="enclave_execution_type_example",
        environment_uuid="environment_uuid_example",
    ) # JsonEnclaveRunRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_enclave_run_request(body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnclaveServiceApi->create_enclave_run_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonEnclaveRunRequest**](JsonEnclaveRunRequest.md)|  | [optional]

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

# **get_enclave**
> file_type get_enclave(uuid)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import enclave_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enclave_service_api.EnclaveServiceApi(api_client)
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_enclave(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnclaveServiceApi->get_enclave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |

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

# **get_enclave_types**
> file_type get_enclave_types()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import enclave_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enclave_service_api.EnclaveServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_enclave_types()
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnclaveServiceApi->get_enclave_types: %s\n" % e)
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

# **get_enclaves**
> file_type get_enclaves()

Returns UUIDs of existing analyses.

Returns UUIDs of existing analyses.

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import enclave_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enclave_service_api.EnclaveServiceApi(api_client)
    authorization = "Authorization_example" # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)
    created = "true" # str | - if Queryparam \"created=true\" only the UUIDs of own Requests are shown (optional) if omitted the server will use the default value of "true"
    limit = "30" # str | Used for offset pagination. Limit/Offset Paging would look like GET /request?limit=20&offset=100. This query would return the 20 rows starting with the 100th row (optional) if omitted the server will use the default value of "30"
    offset = "0" # str | Used for offset pagination. Limit/Offset Paging would look like GET /request?limit=20&offset=100. This query would return the 20 rows starting with the 100th row (optional) if omitted the server will use the default value of "0"
    status = "status_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns UUIDs of existing analyses.
        api_response = api_instance.get_enclaves(authorization=authorization, created=created, limit=limit, offset=offset, status=status)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnclaveServiceApi->get_enclaves: %s\n" % e)
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

# **get_stats**
> file_type get_stats()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import enclave_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enclave_service_api.EnclaveServiceApi(api_client)
    dayssince = "30" # str |  (optional) if omitted the server will use the default value of "30"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stats(dayssince=dayssince)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnclaveServiceApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dayssince** | **str**|  | [optional] if omitted the server will use the default value of "30"

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

# **kill_enclave**
> file_type kill_enclave(uuid)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import enclave_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enclave_service_api.EnclaveServiceApi(api_client)
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.kill_enclave(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnclaveServiceApi->kill_enclave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |

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

