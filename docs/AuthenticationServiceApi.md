# madana_apiclient.AuthenticationServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_application**](AuthenticationServiceApi.md#authenticate_application) | **POST** /authentication/application | Authenticates a new application and returns the token.
[**authenticate_ethereum_wallet**](AuthenticationServiceApi.md#authenticate_ethereum_wallet) | **POST** /authentication/ethereum/{wallet} | 
[**authenticate_user**](AuthenticationServiceApi.md#authenticate_user) | **POST** /authentication | Authenticates a new user and returns the token (  forbidden if the credentials cannot be validated ).
[**authenticate_with_ethereum_challenge**](AuthenticationServiceApi.md#authenticate_with_ethereum_challenge) | **POST** /authentication/ethereum/{wallet}/challenge | 
[**get_fractal_authentication_url**](AuthenticationServiceApi.md#get_fractal_authentication_url) | **GET** /authentication/fractal | Returns the AUthorization URL to verify a Twitter Accounts.
[**get_nonce_for_ethereum_wallet**](AuthenticationServiceApi.md#get_nonce_for_ethereum_wallet) | **GET** /authentication/ethereum/{wallet} | Returns a nonce for the client which is used as content for the to be created signature.
[**get_object**](AuthenticationServiceApi.md#get_object) | **GET** /authentication | Used to validate the active connection with the API.
[**get_twitter_authentication_url**](AuthenticationServiceApi.md#get_twitter_authentication_url) | **GET** /authentication/twitter | Returns the AUthorization URL to verify a Twitter Accounts.
[**set_facebook_uid**](AuthenticationServiceApi.md#set_facebook_uid) | **POST** /authentication/facebook | Used as Callback URL when users have successfully authorized their facbeook account.
[**set_fractal_uid**](AuthenticationServiceApi.md#set_fractal_uid) | **POST** /authentication/fractal | 
[**set_twitter_uid**](AuthenticationServiceApi.md#set_twitter_uid) | **POST** /authentication/twitter | 


# **authenticate_application**
> JsonMDNToken authenticate_application(body=body)

Authenticates a new application and returns the token.

Authenticates a new application and returns the token

### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.AuthenticationServiceApi(api_client)
    body = madana_apiclient.JsonMDNCertificate() # JsonMDNCertificate | the credentials used to validate the user (optional)

    try:
        # Authenticates a new application and returns the token.
        api_response = api_instance.authenticate_application(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationServiceApi->authenticate_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonMDNCertificate**](JsonMDNCertificate.md)| the credentials used to validate the user | [optional] 

### Return type

[**JsonMDNToken**](JsonMDNToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the application certificate could be verified |  -  |
**401** | If the application could not be found |  -  |
**403** | If the an error occurs verifying the Application certificate |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate_ethereum_wallet**
> file authenticate_ethereum_wallet(wallet, body=body)



### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.AuthenticationServiceApi(api_client)
    wallet = 'wallet_example' # str | the wallet which should be authenticated
body = madana_apiclient.JsonMDNOAuthToken() # JsonMDNOAuthToken | Token containing nonce and signate (optional)

    try:
        api_response = api_instance.authenticate_ethereum_wallet(wallet, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationServiceApi->authenticate_ethereum_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet** | **str**| the wallet which should be authenticated | 
 **body** | [**JsonMDNOAuthToken**](JsonMDNOAuthToken.md)| Token containing nonce and signate | [optional] 

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
**417** | If the nonce could not be verified |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate_user**
> JsonMDNToken authenticate_user(body=body)

Authenticates a new user and returns the token (  forbidden if the credentials cannot be validated ).

Authenticates a new user and returns the token (  forbidden if the credentials cannot be validated )

### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.AuthenticationServiceApi(api_client)
    body = madana_apiclient.JsonMDNUserCredentials() # JsonMDNUserCredentials | the credentials used to validate the user (optional)

    try:
        # Authenticates a new user and returns the token (  forbidden if the credentials cannot be validated ).
        api_response = api_instance.authenticate_user(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationServiceApi->authenticate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonMDNUserCredentials**](JsonMDNUserCredentials.md)| the credentials used to validate the user | [optional] 

### Return type

[**JsonMDNToken**](JsonMDNToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the credentials could be verified |  -  |
**403** | If the credentials could not be verified |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate_with_ethereum_challenge**
> file authenticate_with_ethereum_challenge(wallet, body=body)



### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.AuthenticationServiceApi(api_client)
    wallet = 'wallet_example' # str | the wallet which should be authenticated
body = madana_apiclient.JsonMDNOAuthToken() # JsonMDNOAuthToken | Token containing nonce and signate (optional)

    try:
        api_response = api_instance.authenticate_with_ethereum_challenge(wallet, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationServiceApi->authenticate_with_ethereum_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet** | **str**| the wallet which should be authenticated | 
 **body** | [**JsonMDNOAuthToken**](JsonMDNOAuthToken.md)| Token containing nonce and signate | [optional] 

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
**417** | If the nonce could not be verified |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fractal_authentication_url**
> file get_fractal_authentication_url()

Returns the AUthorization URL to verify a Twitter Accounts.

Returns the AUthorization URL to verify a Twitter Accounts

### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.AuthenticationServiceApi(api_client)
    
    try:
        # Returns the AUthorization URL to verify a Twitter Accounts.
        api_response = api_instance.get_fractal_authentication_url()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationServiceApi->get_fractal_authentication_url: %s\n" % e)
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

# **get_nonce_for_ethereum_wallet**
> JsonMDNToken get_nonce_for_ethereum_wallet(wallet, authorization=authorization)

Returns a nonce for the client which is used as content for the to be created signature.

Returns a nonce for the client which is used as content for the to be created signature

### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.AuthenticationServiceApi(api_client)
    wallet = 'wallet_example' # str | - wallet address as String * @HTTP 417 If the address is not valid
authorization = 'authorization_example' # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)

    try:
        # Returns a nonce for the client which is used as content for the to be created signature.
        api_response = api_instance.get_nonce_for_ethereum_wallet(wallet, authorization=authorization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationServiceApi->get_nonce_for_ethereum_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet** | **str**| - wallet address as String * @HTTP 417 If the address is not valid | 
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional] 

### Return type

[**JsonMDNToken**](JsonMDNToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object**
> dict(str, object) get_object()

Used to validate the active connection with the API.

Used to validate the active connection with the API

### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.AuthenticationServiceApi(api_client)
    
    try:
        # Used to validate the active connection with the API.
        api_response = api_instance.get_object()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationServiceApi->get_object: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the usage could be generated |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_twitter_authentication_url**
> file get_twitter_authentication_url()

Returns the AUthorization URL to verify a Twitter Accounts.

Returns the AUthorization URL to verify a Twitter Accounts

### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.AuthenticationServiceApi(api_client)
    
    try:
        # Returns the AUthorization URL to verify a Twitter Accounts.
        api_response = api_instance.get_twitter_authentication_url()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationServiceApi->get_twitter_authentication_url: %s\n" % e)
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

# **set_facebook_uid**
> file set_facebook_uid(body=body)

Used as Callback URL when users have successfully authorized their facbeook account.

Used as Callback URL when users have successfully authorized their facbeook account

### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.AuthenticationServiceApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # Used as Callback URL when users have successfully authorized their facbeook account.
        api_response = api_instance.set_facebook_uid(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationServiceApi->set_facebook_uid: %s\n" % e)
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

# **set_fractal_uid**
> file set_fractal_uid(body=body)



### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.AuthenticationServiceApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        api_response = api_instance.set_fractal_uid(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationServiceApi->set_fractal_uid: %s\n" % e)
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

# **set_twitter_uid**
> file set_twitter_uid(body=body)



### Example

```python
from __future__ import print_function
import time
import madana_apiclient
from madana_apiclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = madana_apiclient.AuthenticationServiceApi(api_client)
    body = madana_apiclient.JsonMDNOAuthToken() # JsonMDNOAuthToken |  (optional)

    try:
        api_response = api_instance.set_twitter_uid(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationServiceApi->set_twitter_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonMDNOAuthToken**](JsonMDNOAuthToken.md)|  | [optional] 

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

