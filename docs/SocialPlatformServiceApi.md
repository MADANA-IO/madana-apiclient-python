# madana_sampleclient_python.SocialPlatformServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_platforms**](SocialPlatformServiceApi.md#get_platforms) | **GET** /platforms | Used to Handle Incoming Webhooks from Facebook.
[**listen_twitter_webhook**](SocialPlatformServiceApi.md#listen_twitter_webhook) | **POST** /platforms/twitter | Used to Handle Incoming Webhooks from Facebook.
[**register_twitter_webhook**](SocialPlatformServiceApi.md#register_twitter_webhook) | **GET** /platforms/twitter | Used to Handle Incoming Webhooks from Twitter.


# **get_platforms**
> file get_platforms(body=body)

Used to Handle Incoming Webhooks from Facebook.

Used to Handle Incoming Webhooks from Facebook

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
    api_instance = madana_sampleclient_python.SocialPlatformServiceApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # Used to Handle Incoming Webhooks from Facebook.
        api_response = api_instance.get_platforms(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SocialPlatformServiceApi->get_platforms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_twitter_webhook**
> file listen_twitter_webhook(body=body)

Used to Handle Incoming Webhooks from Facebook.

Used to Handle Incoming Webhooks from Facebook

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
    api_instance = madana_sampleclient_python.SocialPlatformServiceApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # Used to Handle Incoming Webhooks from Facebook.
        api_response = api_instance.listen_twitter_webhook(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SocialPlatformServiceApi->listen_twitter_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

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

# **register_twitter_webhook**
> file register_twitter_webhook(crc_token=crc_token)

Used to Handle Incoming Webhooks from Twitter.

Used to Handle Incoming Webhooks from Twitter

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
    api_instance = madana_sampleclient_python.SocialPlatformServiceApi(api_client)
    crc_token = 'crc_token_example' # str |  (optional)

    try:
        # Used to Handle Incoming Webhooks from Twitter.
        api_response = api_instance.register_twitter_webhook(crc_token=crc_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SocialPlatformServiceApi->register_twitter_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crc_token** | **str**|  | [optional] 

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

