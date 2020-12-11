# madana_apiclient.SocialPlatformServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_platforms**](SocialPlatformServiceApi.md#get_platforms) | **GET** /platforms | Used to Handle Incoming Webhooks from Facebook.
[**listen_twitter_webhook**](SocialPlatformServiceApi.md#listen_twitter_webhook) | **POST** /platforms/twitter | Used to Handle Incoming Webhooks from Facebook.
[**register_twitter_webhook**](SocialPlatformServiceApi.md#register_twitter_webhook) | **GET** /platforms/twitter | Used to Handle Incoming Webhooks from Twitter.


# **get_platforms**
> file_type get_platforms()

Used to Handle Incoming Webhooks from Facebook.

Used to Handle Incoming Webhooks from Facebook

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import social_platform_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = social_platform_service_api.SocialPlatformServiceApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Used to Handle Incoming Webhooks from Facebook.
        api_response = api_instance.get_platforms(body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling SocialPlatformServiceApi->get_platforms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_twitter_webhook**
> file_type listen_twitter_webhook()

Used to Handle Incoming Webhooks from Facebook.

Used to Handle Incoming Webhooks from Facebook

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import social_platform_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = social_platform_service_api.SocialPlatformServiceApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Used to Handle Incoming Webhooks from Facebook.
        api_response = api_instance.listen_twitter_webhook(body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling SocialPlatformServiceApi->listen_twitter_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

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

# **register_twitter_webhook**
> file_type register_twitter_webhook()

Used to Handle Incoming Webhooks from Twitter.

Used to Handle Incoming Webhooks from Twitter

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import social_platform_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = social_platform_service_api.SocialPlatformServiceApi(api_client)
    crc_token = "crc_token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Used to Handle Incoming Webhooks from Twitter.
        api_response = api_instance.register_twitter_webhook(crc_token=crc_token)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling SocialPlatformServiceApi->register_twitter_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crc_token** | **str**|  | [optional]

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

