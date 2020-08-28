# madana_apiclient.UserServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_object**](UserServiceApi.md#create_object) | **POST** /users | Creates a new user object.
[**delete_object**](UserServiceApi.md#delete_object) | **DELETE** /users/{username} | Deletes an User based on the provided id and securitycontext.
[**delete_object_0**](UserServiceApi.md#delete_object_0) | **DELETE** /users/{username}/social/{platform}/{ident} | Deletes linked account from the user and securitycontext.
[**get_avatars**](UserServiceApi.md#get_avatars) | **GET** /users/{username}/avatars | 
[**get_certificates**](UserServiceApi.md#get_certificates) | **GET** /users/{username}/certificates | 
[**get_enclave_history**](UserServiceApi.md#get_enclave_history) | **GET** /users/{username}/enclavehistory | 
[**get_object2**](UserServiceApi.md#get_object2) | **GET** /users/{username} | 
[**set_avatar**](UserServiceApi.md#set_avatar) | **POST** /users/{username}/avatars | 
[**set_settings**](UserServiceApi.md#set_settings) | **POST** /users/{username}/settings | 
[**update_object**](UserServiceApi.md#update_object) | **PUT** /users/{username} | Updates Userproperties based on the provided user object.


# **create_object**
> file create_object(referrer=referrer, body=body)

Creates a new user object.

Creates a new user object

### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.UserServiceApi(api_client)
    referrer = 'referrer_example' # str |  (optional)
body = madana_apiclient.JsonMDNUser() # JsonMDNUser | provided user object inheriting properties and credentials (optional)

    try:
        # Creates a new user object.
        api_response = api_instance.create_object(referrer=referrer, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->create_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **referrer** | **str**|  | [optional] 
 **body** | [**JsonMDNUser**](JsonMDNUser.md)| provided user object inheriting properties and credentials | [optional] 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | HTTP Response OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object**
> file delete_object(username)

Deletes an User based on the provided id and securitycontext.

Deletes an User based on the provided id and securitycontext

### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.UserServiceApi(api_client)
    username = 'username_example' # str | 

    try:
        # Deletes an User based on the provided id and securitycontext.
        api_response = api_instance.delete_object(username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->delete_object: %s\n" % e)
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
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | HTTP Response OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object_0**
> file delete_object_0(ident, platform, username)

Deletes linked account from the user and securitycontext.

Deletes linked account from the user and securitycontext

### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.UserServiceApi(api_client)
    ident = 'ident_example' # str | 
platform = 'platform_example' # str | 
username = 'username_example' # str | 

    try:
        # Deletes linked account from the user and securitycontext.
        api_response = api_instance.delete_object_0(ident, platform, username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->delete_object_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ident** | **str**|  | 
 **platform** | **str**|  | 
 **username** | **str**|  | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | HTTP Response OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_avatars**
> file get_avatars(username)



### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.UserServiceApi(api_client)
    username = 'username_example' # str | 

    try:
        api_response = api_instance.get_avatars(username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->get_avatars: %s\n" % e)
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

# **get_certificates**
> file get_certificates(username)



### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.UserServiceApi(api_client)
    username = 'username_example' # str | 

    try:
        api_response = api_instance.get_certificates(username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->get_certificates: %s\n" % e)
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

# **get_enclave_history**
> file get_enclave_history(username, limit=limit, offset=offset)



### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.UserServiceApi(api_client)
    username = 'username_example' # str | 
limit = '30' # str |  (optional) (default to '30')
offset = '0' # str |  (optional) (default to '0')

    try:
        api_response = api_instance.get_enclave_history(username, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->get_enclave_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
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

# **get_object2**
> file get_object2(username)



### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.UserServiceApi(api_client)
    username = 'username_example' # str | 

    try:
        api_response = api_instance.get_object2(username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->get_object2: %s\n" % e)
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

# **set_avatar**
> file set_avatar(username, body=body)



### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.UserServiceApi(api_client)
    username = 'username_example' # str | 
body = madana_apiclient.JsonMDNUserProfileImage() # JsonMDNUserProfileImage |  (optional)

    try:
        api_response = api_instance.set_avatar(username, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->set_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **body** | [**JsonMDNUserProfileImage**](JsonMDNUserProfileImage.md)|  | [optional] 

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

# **set_settings**
> file set_settings(username, body=body)



### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.UserServiceApi(api_client)
    username = 'username_example' # str | 
body = madana_apiclient.JsonMDNUserSetting() # JsonMDNUserSetting |  (optional)

    try:
        api_response = api_instance.set_settings(username, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->set_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **body** | [**JsonMDNUserSetting**](JsonMDNUserSetting.md)|  | [optional] 

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

# **update_object**
> file update_object(username, body=body)

Updates Userproperties based on the provided user object.

Updates Userproperties based on the provided user object

### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.UserServiceApi(api_client)
    username = 'username_example' # str | 
body = madana_apiclient.JsonMDNUser() # JsonMDNUser | the new user object inherting all properties that should be change (optional)

    try:
        # Updates Userproperties based on the provided user object.
        api_response = api_instance.update_object(username, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->update_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **body** | [**JsonMDNUser**](JsonMDNUser.md)| the new user object inherting all properties that should be change | [optional] 

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
**204** | HTTP Response OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

