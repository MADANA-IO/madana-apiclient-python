# madana_sampleclient_python.SocialServiceApi

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
> file get_my_profile()



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
    api_instance = madana_sampleclient_python.SocialServiceApi(api_client)
    
    try:
        api_response = api_instance.get_my_profile()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SocialServiceApi->get_my_profile: %s\n" % e)
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

# **get_platforms2**
> file get_platforms2()

Returns all Platforms / Systems that can be Connected to the MADANA Service.

Returns all Platforms / Systems that can be Connected to the MADANA Service

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
    api_instance = madana_sampleclient_python.SocialServiceApi(api_client)
    
    try:
        # Returns all Platforms / Systems that can be Connected to the MADANA Service.
        api_response = api_instance.get_platforms2()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SocialServiceApi->get_platforms2: %s\n" % e)
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
**200** | List&lt;{MDN_SocialPlatform&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ranking**
> file get_ranking()

Returns the Ranking by PTS within the System.

Returns the Ranking by PTS within the System

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
    api_instance = madana_sampleclient_python.SocialServiceApi(api_client)
    
    try:
        # Returns the Ranking by PTS within the System.
        api_response = api_instance.get_ranking()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SocialServiceApi->get_ranking: %s\n" % e)
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
**200** | Map&lt;String, String&gt; - The key is the username and the value are the points |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_social_platform_feed**
> file get_social_platform_feed(platform)



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
    api_instance = madana_sampleclient_python.SocialServiceApi(api_client)
    platform = 'platform_example' # str | 

    try:
        api_response = api_instance.get_social_platform_feed(platform)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SocialServiceApi->get_social_platform_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  | 

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

# **get_user_profile**
> file get_user_profile(username, simple=simple)



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
    api_instance = madana_sampleclient_python.SocialServiceApi(api_client)
    username = 'username_example' # str | 
simple = 'false' # str |  (optional) (default to 'false')

    try:
        api_response = api_instance.get_user_profile(username, simple=simple)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SocialServiceApi->get_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **simple** | **str**|  | [optional] [default to &#39;false&#39;]

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

# **get_user_profile_0**
> file get_user_profile_0(username)



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
    api_instance = madana_sampleclient_python.SocialServiceApi(api_client)
    username = 'username_example' # str | 

    try:
        api_response = api_instance.get_user_profile_0(username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SocialServiceApi->get_user_profile_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

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

