# madana_sampleclient_python.EnvironmentServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_environment**](EnvironmentServiceApi.md#delete_environment) | **DELETE** /environments/{uuid} | 
[**delete_environment_subscription**](EnvironmentServiceApi.md#delete_environment_subscription) | **DELETE** /environments/{uuid}/subscribe | 
[**get_all_requests**](EnvironmentServiceApi.md#get_all_requests) | **GET** /environments | Returns UUIDs of existing analyses.
[**get_environment**](EnvironmentServiceApi.md#get_environment) | **GET** /environments/{uuid} | 
[**get_published_environments**](EnvironmentServiceApi.md#get_published_environments) | **GET** /environments/published | 
[**get_subscribed_environments**](EnvironmentServiceApi.md#get_subscribed_environments) | **GET** /environments/subscriptions | 
[**publish_environment**](EnvironmentServiceApi.md#publish_environment) | **POST** /environments | 
[**subscribe_environment**](EnvironmentServiceApi.md#subscribe_environment) | **POST** /environments/{uuid}/subscribe | 
[**update_environment**](EnvironmentServiceApi.md#update_environment) | **PUT** /environments/{uuid} | 


# **delete_environment**
> file delete_environment(uuid)



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
    api_instance = madana_sampleclient_python.EnvironmentServiceApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_response = api_instance.delete_environment(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnvironmentServiceApi->delete_environment: %s\n" % e)
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
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_environment_subscription**
> file delete_environment_subscription(uuid)



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
    api_instance = madana_sampleclient_python.EnvironmentServiceApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_response = api_instance.delete_environment_subscription(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnvironmentServiceApi->delete_environment_subscription: %s\n" % e)
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
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_requests**
> file get_all_requests(authorization=authorization, created=created, limit=limit, name=name, offset=offset)

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
    api_instance = madana_sampleclient_python.EnvironmentServiceApi(api_client)
    authorization = 'authorization_example' # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)
created = 'true' # str | - if Queryparam \"created=true\" only the UUIDs of own Requests are shown (optional) (default to 'true')
limit = '30' # str | Used for offset pagination. Limit/Offset Paging would look like GET /request?limit=20&offset=100. This query would return the 20 rows starting with the 100th row (optional) (default to '30')
name = 'name_example' # str |  (optional)
offset = '0' # str | Used for offset pagination. Limit/Offset Paging would look like GET /request?limit=20&offset=100. This query would return the 20 rows starting with the 100th row (optional) (default to '0')

    try:
        # Returns UUIDs of existing analyses.
        api_response = api_instance.get_all_requests(authorization=authorization, created=created, limit=limit, name=name, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnvironmentServiceApi->get_all_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional] 
 **created** | **str**| - if Queryparam \&quot;created&#x3D;true\&quot; only the UUIDs of own Requests are shown | [optional] [default to &#39;true&#39;]
 **limit** | **str**| Used for offset pagination. Limit/Offset Paging would look like GET /request?limit&#x3D;20&amp;offset&#x3D;100. This query would return the 20 rows starting with the 100th row | [optional] [default to &#39;30&#39;]
 **name** | **str**|  | [optional] 
 **offset** | **str**| Used for offset pagination. Limit/Offset Paging would look like GET /request?limit&#x3D;20&amp;offset&#x3D;100. This query would return the 20 rows starting with the 100th row | [optional] [default to &#39;0&#39;]

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

# **get_environment**
> file get_environment(uuid)



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
    api_instance = madana_sampleclient_python.EnvironmentServiceApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_response = api_instance.get_environment(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnvironmentServiceApi->get_environment: %s\n" % e)
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

# **get_published_environments**
> file get_published_environments(limit=limit, name=name, offset=offset)



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
    api_instance = madana_sampleclient_python.EnvironmentServiceApi(api_client)
    limit = '30' # str |  (optional) (default to '30')
name = 'name_example' # str |  (optional)
offset = '0' # str |  (optional) (default to '0')

    try:
        api_response = api_instance.get_published_environments(limit=limit, name=name, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnvironmentServiceApi->get_published_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**|  | [optional] [default to &#39;30&#39;]
 **name** | **str**|  | [optional] 
 **offset** | **str**|  | [optional] [default to &#39;0&#39;]

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

# **get_subscribed_environments**
> file get_subscribed_environments(limit=limit, offset=offset)



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
    api_instance = madana_sampleclient_python.EnvironmentServiceApi(api_client)
    limit = '30' # str |  (optional) (default to '30')
offset = '0' # str |  (optional) (default to '0')

    try:
        api_response = api_instance.get_subscribed_environments(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnvironmentServiceApi->get_subscribed_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**|  | [optional] [default to &#39;30&#39;]
 **offset** | **str**|  | [optional] [default to &#39;0&#39;]

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

# **publish_environment**
> file publish_environment(body=body)



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
    api_instance = madana_sampleclient_python.EnvironmentServiceApi(api_client)
    body = madana_sampleclient_python.JsonEnvironmentPublishingRequest() # JsonEnvironmentPublishingRequest |  (optional)

    try:
        api_response = api_instance.publish_environment(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnvironmentServiceApi->publish_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonEnvironmentPublishingRequest**](JsonEnvironmentPublishingRequest.md)|  | [optional] 

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

# **subscribe_environment**
> file subscribe_environment(uuid)



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
    api_instance = madana_sampleclient_python.EnvironmentServiceApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_response = api_instance.subscribe_environment(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnvironmentServiceApi->subscribe_environment: %s\n" % e)
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

# **update_environment**
> file update_environment(uuid, body=body)



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
    api_instance = madana_sampleclient_python.EnvironmentServiceApi(api_client)
    uuid = 'uuid_example' # str | 
body = madana_sampleclient_python.JsonEnvironment() # JsonEnvironment |  (optional)

    try:
        api_response = api_instance.update_environment(uuid, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnvironmentServiceApi->update_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **body** | [**JsonEnvironment**](JsonEnvironment.md)|  | [optional] 

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
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

