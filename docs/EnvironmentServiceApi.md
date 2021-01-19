# madana_apiclient.EnvironmentServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_environment**](EnvironmentServiceApi.md#delete_environment) | **DELETE** /environments/{uuid} | 
[**delete_environment_subscription**](EnvironmentServiceApi.md#delete_environment_subscription) | **DELETE** /environments/{uuid}/subscribe | 
[**get_environment**](EnvironmentServiceApi.md#get_environment) | **GET** /environments/{uuid} | 
[**get_environments**](EnvironmentServiceApi.md#get_environments) | **GET** /environments | Returns UUIDs of existing analyses.
[**get_published_environments**](EnvironmentServiceApi.md#get_published_environments) | **GET** /environments/published | 
[**get_subscribed_environments**](EnvironmentServiceApi.md#get_subscribed_environments) | **GET** /environments/subscriptions | 
[**publish_environment**](EnvironmentServiceApi.md#publish_environment) | **POST** /environments | 
[**subscribe_environment**](EnvironmentServiceApi.md#subscribe_environment) | **POST** /environments/{uuid}/subscribe | 
[**update_environment**](EnvironmentServiceApi.md#update_environment) | **PUT** /environments/{uuid} | 


# **delete_environment**
> file_type delete_environment(uuid)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import environment_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = environment_service_api.EnvironmentServiceApi(api_client)
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_environment(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnvironmentServiceApi->delete_environment: %s\n" % e)
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
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_environment_subscription**
> file_type delete_environment_subscription(uuid)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import environment_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = environment_service_api.EnvironmentServiceApi(api_client)
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_environment_subscription(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnvironmentServiceApi->delete_environment_subscription: %s\n" % e)
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
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment**
> file_type get_environment(uuid)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import environment_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = environment_service_api.EnvironmentServiceApi(api_client)
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_environment(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnvironmentServiceApi->get_environment: %s\n" % e)
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

# **get_environments**
> file_type get_environments()

Returns UUIDs of existing analyses.

Returns UUIDs of existing analyses.

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import environment_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = environment_service_api.EnvironmentServiceApi(api_client)
    authorization = "Authorization_example" # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)
    created = "true" # str | - if Queryparam \"created=true\" only the UUIDs of own Requests are shown (optional) if omitted the server will use the default value of "true"
    limit = "30" # str | Used for offset pagination. Limit/Offset Paging would look like GET /request?limit=20&offset=100. This query would return the 20 rows starting with the 100th row (optional) if omitted the server will use the default value of "30"
    name = "name_example" # str |  (optional)
    offset = "0" # str | Used for offset pagination. Limit/Offset Paging would look like GET /request?limit=20&offset=100. This query would return the 20 rows starting with the 100th row (optional) if omitted the server will use the default value of "0"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns UUIDs of existing analyses.
        api_response = api_instance.get_environments(authorization=authorization, created=created, limit=limit, name=name, offset=offset)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnvironmentServiceApi->get_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional]
 **created** | **str**| - if Queryparam \&quot;created&#x3D;true\&quot; only the UUIDs of own Requests are shown | [optional] if omitted the server will use the default value of "true"
 **limit** | **str**| Used for offset pagination. Limit/Offset Paging would look like GET /request?limit&#x3D;20&amp;offset&#x3D;100. This query would return the 20 rows starting with the 100th row | [optional] if omitted the server will use the default value of "30"
 **name** | **str**|  | [optional]
 **offset** | **str**| Used for offset pagination. Limit/Offset Paging would look like GET /request?limit&#x3D;20&amp;offset&#x3D;100. This query would return the 20 rows starting with the 100th row | [optional] if omitted the server will use the default value of "0"

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

# **get_published_environments**
> file_type get_published_environments()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import environment_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = environment_service_api.EnvironmentServiceApi(api_client)
    limit = "30" # str |  (optional) if omitted the server will use the default value of "30"
    name = "name_example" # str |  (optional)
    offset = "0" # str |  (optional) if omitted the server will use the default value of "0"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_published_environments(limit=limit, name=name, offset=offset)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnvironmentServiceApi->get_published_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**|  | [optional] if omitted the server will use the default value of "30"
 **name** | **str**|  | [optional]
 **offset** | **str**|  | [optional] if omitted the server will use the default value of "0"

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

# **get_subscribed_environments**
> file_type get_subscribed_environments()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import environment_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = environment_service_api.EnvironmentServiceApi(api_client)
    limit = "30" # str |  (optional) if omitted the server will use the default value of "30"
    offset = "0" # str |  (optional) if omitted the server will use the default value of "0"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_subscribed_environments(limit=limit, offset=offset)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnvironmentServiceApi->get_subscribed_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**|  | [optional] if omitted the server will use the default value of "30"
 **offset** | **str**|  | [optional] if omitted the server will use the default value of "0"

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

# **publish_environment**
> file_type publish_environment()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import environment_service_api
from madana_apiclient.model.json_environment_publishing_request import JsonEnvironmentPublishingRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = environment_service_api.EnvironmentServiceApi(api_client)
    body = JsonEnvironmentPublishingRequest(
        ipfs_hash="ipfs_hash_example",
        packages="packages_example",
        content="content_example",
        is_public="is_public_example",
        name="name_example",
        ipfs_primary_peer="ipfs_primary_peer_example",
        description="description_example",
        uuid="uuid_example",
        size="size_example",
    ) # JsonEnvironmentPublishingRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.publish_environment(body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnvironmentServiceApi->publish_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonEnvironmentPublishingRequest**](JsonEnvironmentPublishingRequest.md)|  | [optional]

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

# **subscribe_environment**
> file_type subscribe_environment(uuid)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import environment_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = environment_service_api.EnvironmentServiceApi(api_client)
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.subscribe_environment(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnvironmentServiceApi->subscribe_environment: %s\n" % e)
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

# **update_environment**
> file_type update_environment(uuid)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import environment_service_api
from madana_apiclient.model.json_environment import JsonEnvironment
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = environment_service_api.EnvironmentServiceApi(api_client)
    uuid = "uuid_example" # str | 
    body = JsonEnvironment(
        name="name_example",
        packages=[
            "packages_example",
        ],
        size="size_example",
        root_hash_offset="root_hash_offset_example",
        ipfs_hash="ipfs_hash_example",
        description="description_example",
        default_run_configuration=JsonRunConfig(
            args=[
                "args_example",
            ],
            run="run_example",
            environment={
                "key": "key_example",
            },
            disk_config=[
                JsonDiskConfig(
                    roothash_offset=1,
                    disk="disk_example",
                    roothash="roothash_example",
                    readonly=True,
                ),
            ],
        ),
        published=True,
        uuid="uuid_example",
        roothash="roothash_example",
        content=[
            "content_example",
        ],
    ) # JsonEnvironment |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_environment(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnvironmentServiceApi->update_environment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_environment(uuid, body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling EnvironmentServiceApi->update_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **body** | [**JsonEnvironment**](JsonEnvironment.md)|  | [optional]

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
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

