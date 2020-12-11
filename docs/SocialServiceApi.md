# madana_apiclient.SocialServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_my_profile**](SocialServiceApi.md#get_my_profile) | **GET** /social/profiles/me | 
[**get_platforms2**](SocialServiceApi.md#get_platforms2) | **GET** /social | Returns all Platforms / Systems that can be Connected to the MADANA Service.
[**get_ranking**](SocialServiceApi.md#get_ranking) | **GET** /social/ranking | Returns the Ranking by PTS within the System.
[**get_social_platform_feed**](SocialServiceApi.md#get_social_platform_feed) | **GET** /social/feed/{platform} | 
[**get_user_profile**](SocialServiceApi.md#get_user_profile) | **GET** /social/profiles/{username} | 
[**get_user_profile_0**](SocialServiceApi.md#get_user_profile_0) | **GET** /social/profiles/{username}/simple | 


# **get_my_profile**
> file_type get_my_profile()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import social_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = social_service_api.SocialServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_my_profile()
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling SocialServiceApi->get_my_profile: %s\n" % e)
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

# **get_platforms2**
> file_type get_platforms2()

Returns all Platforms / Systems that can be Connected to the MADANA Service.

Returns all Platforms / Systems that can be Connected to the MADANA Service

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import social_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = social_service_api.SocialServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns all Platforms / Systems that can be Connected to the MADANA Service.
        api_response = api_instance.get_platforms2()
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling SocialServiceApi->get_platforms2: %s\n" % e)
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
**200** | List&lt;{MDN_SocialPlatform&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ranking**
> file_type get_ranking()

Returns the Ranking by PTS within the System.

Returns the Ranking by PTS within the System

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import social_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = social_service_api.SocialServiceApi(api_client)
    limit = "99" # str |  (optional) if omitted the server will use the default value of "99"
    offset = "0" # str |  (optional) if omitted the server will use the default value of "0"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the Ranking by PTS within the System.
        api_response = api_instance.get_ranking(limit=limit, offset=offset)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling SocialServiceApi->get_ranking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**|  | [optional] if omitted the server will use the default value of "99"
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
**200** | Map&lt;String, String&gt; - The key is the username and the value are the points |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_social_platform_feed**
> file_type get_social_platform_feed(platform)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import social_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = social_service_api.SocialServiceApi(api_client)
    platform = "platform_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_social_platform_feed(platform)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling SocialServiceApi->get_social_platform_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  |

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

# **get_user_profile**
> file_type get_user_profile(username)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import social_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = social_service_api.SocialServiceApi(api_client)
    username = "username_example" # str | 
    simple = "false" # str |  (optional) if omitted the server will use the default value of "false"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_user_profile(username)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling SocialServiceApi->get_user_profile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_user_profile(username, simple=simple)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling SocialServiceApi->get_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |
 **simple** | **str**|  | [optional] if omitted the server will use the default value of "false"

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

# **get_user_profile_0**
> file_type get_user_profile_0(username)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import social_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = social_service_api.SocialServiceApi(api_client)
    username = "username_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_user_profile_0(username)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling SocialServiceApi->get_user_profile_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |

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

