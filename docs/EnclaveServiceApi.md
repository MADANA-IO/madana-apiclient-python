# madana_sampleclient_python.EnclaveServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_enclave**](EnclaveServiceApi.md#approve_enclave) | **POST** /enclaves/{uuid}/approval | 
[**assign_enclave_agent**](EnclaveServiceApi.md#assign_enclave_agent) | **POST** /enclaves/{uuid}/assign | 
[**attestate_enclave**](EnclaveServiceApi.md#attestate_enclave) | **POST** /enclaves/{uuid}/attestation | 
[**create_enclave_run_request**](EnclaveServiceApi.md#create_enclave_run_request) | **POST** /enclaves | 
[**get_enclave**](EnclaveServiceApi.md#get_enclave) | **GET** /enclaves/{uuid} | 
[**get_enclave_types**](EnclaveServiceApi.md#get_enclave_types) | **GET** /enclaves/types | 
[**get_enclaves**](EnclaveServiceApi.md#get_enclaves) | **GET** /enclaves | Returns UUIDs of existing analyses.
[**kill_enclave**](EnclaveServiceApi.md#kill_enclave) | **POST** /enclaves/{uuid}/kill | 


# **approve_enclave**
> file approve_enclave(uuid, body=body)



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
    api_instance = madana_sampleclient_python.EnclaveServiceApi(api_client)
    uuid = 'uuid_example' # str | 
body = madana_sampleclient_python.JsonEnclaveRunningAttestationApproval() # JsonEnclaveRunningAttestationApproval |  (optional)

    try:
        api_response = api_instance.approve_enclave(uuid, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnclaveServiceApi->approve_enclave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **body** | [**JsonEnclaveRunningAttestationApproval**](JsonEnclaveRunningAttestationApproval.md)|  | [optional] 

### Return type

**file**

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
> file assign_enclave_agent(uuid, body=body)



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
    api_instance = madana_sampleclient_python.EnclaveServiceApi(api_client)
    uuid = 'uuid_example' # str | 
body = madana_sampleclient_python.JsonNodeInfo() # JsonNodeInfo |  (optional)

    try:
        api_response = api_instance.assign_enclave_agent(uuid, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnclaveServiceApi->assign_enclave_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **body** | [**JsonNodeInfo**](JsonNodeInfo.md)|  | [optional] 

### Return type

**file**

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
> file attestate_enclave(uuid, body=body)



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
    api_instance = madana_sampleclient_python.EnclaveServiceApi(api_client)
    uuid = 'uuid_example' # str | 
body = madana_sampleclient_python.JsonEnclaveRunningAttestation() # JsonEnclaveRunningAttestation |  (optional)

    try:
        api_response = api_instance.attestate_enclave(uuid, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnclaveServiceApi->attestate_enclave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **body** | [**JsonEnclaveRunningAttestation**](JsonEnclaveRunningAttestation.md)|  | [optional] 

### Return type

**file**

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
> file create_enclave_run_request(body=body)



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
    api_instance = madana_sampleclient_python.EnclaveServiceApi(api_client)
    body = madana_sampleclient_python.JsonEnclaveRunRequest() # JsonEnclaveRunRequest |  (optional)

    try:
        api_response = api_instance.create_enclave_run_request(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnclaveServiceApi->create_enclave_run_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonEnclaveRunRequest**](JsonEnclaveRunRequest.md)|  | [optional] 

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

# **get_enclave**
> file get_enclave(uuid)



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
    api_instance = madana_sampleclient_python.EnclaveServiceApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_response = api_instance.get_enclave(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnclaveServiceApi->get_enclave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

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

# **get_enclave_types**
> file get_enclave_types()



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
    api_instance = madana_sampleclient_python.EnclaveServiceApi(api_client)
    
    try:
        api_response = api_instance.get_enclave_types()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnclaveServiceApi->get_enclave_types: %s\n" % e)
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

# **get_enclaves**
> file get_enclaves(authorization=authorization, created=created, limit=limit, offset=offset, status=status)

Returns UUIDs of existing analyses.

Returns UUIDs of existing analyses.

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
    api_instance = madana_sampleclient_python.EnclaveServiceApi(api_client)
    authorization = 'authorization_example' # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)
created = 'true' # str | - if Queryparam \"created=true\" only the UUIDs of own Requests are shown (optional) (default to 'true')
limit = '30' # str | Used for offset pagination. Limit/Offset Paging would look like GET /request?limit=20&offset=100. This query would return the 20 rows starting with the 100th row (optional) (default to '30')
offset = '0' # str | Used for offset pagination. Limit/Offset Paging would look like GET /request?limit=20&offset=100. This query would return the 20 rows starting with the 100th row (optional) (default to '0')
status = 'status_example' # str |  (optional)

    try:
        # Returns UUIDs of existing analyses.
        api_response = api_instance.get_enclaves(authorization=authorization, created=created, limit=limit, offset=offset, status=status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnclaveServiceApi->get_enclaves: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional] 
 **created** | **str**| - if Queryparam \&quot;created&#x3D;true\&quot; only the UUIDs of own Requests are shown | [optional] [default to &#39;true&#39;]
 **limit** | **str**| Used for offset pagination. Limit/Offset Paging would look like GET /request?limit&#x3D;20&amp;offset&#x3D;100. This query would return the 20 rows starting with the 100th row | [optional] [default to &#39;30&#39;]
 **offset** | **str**| Used for offset pagination. Limit/Offset Paging would look like GET /request?limit&#x3D;20&amp;offset&#x3D;100. This query would return the 20 rows starting with the 100th row | [optional] [default to &#39;0&#39;]
 **status** | **str**|  | [optional] 

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
**200** | If the actions could be loaded |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kill_enclave**
> file kill_enclave(uuid)



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
    api_instance = madana_sampleclient_python.EnclaveServiceApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_response = api_instance.kill_enclave(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnclaveServiceApi->kill_enclave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

