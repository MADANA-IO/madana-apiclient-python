# madana_apiclient.AccountServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_user**](AccountServiceApi.md#activate_user) | **GET** /account/activation/{token} | 
[**create_password_reset**](AccountServiceApi.md#create_password_reset) | **POST** /account/password | Sends an Password reset mail to the given MailAddress.
[**request_verification_mail**](AccountServiceApi.md#request_verification_mail) | **GET** /account/verifymail | Used to request a new  activation-mail for the user.
[**update_password**](AccountServiceApi.md#update_password) | **PUT** /account/password | Receives the Password reset and tries to set the provided password for the user.


# **activate_user**
> file_type activate_user(token)



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import account_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = account_service_api.AccountServiceApi(api_client)
    token = "token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.activate_user(token)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling AccountServiceApi->activate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  |

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_password_reset**
> file_type create_password_reset()

Sends an Password reset mail to the given MailAddress.

Sends an Password reset mail to the given MailAddress

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import account_service_api
from madana_apiclient.model.json_mdn_mail_address import JsonMDNMailAddress
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = account_service_api.AccountServiceApi(api_client)
    body = JsonMDNMailAddress(
        mail="mail_example",
    ) # JsonMDNMailAddress | - the MaiAddress under which the user has signed up (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sends an Password reset mail to the given MailAddress.
        api_response = api_instance.create_password_reset(body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling AccountServiceApi->create_password_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonMDNMailAddress**](JsonMDNMailAddress.md)| - the MaiAddress under which the user has signed up | [optional]

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
**201** | HTTP Status Accepted if the mail has been send, NOT FOUND if the mail address could be found in the system or EXPECTATION FAILED when an error occured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_verification_mail**
> {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)} request_verification_mail()

Used to request a new  activation-mail for the user.

Used to request a new  activation-mail for the user

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import account_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = account_service_api.AccountServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Used to request a new  activation-mail for the user.
        api_response = api_instance.request_verification_mail()
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling AccountServiceApi->request_verification_mail: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the mail has been sent |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password**
> file_type update_password()

Receives the Password reset and tries to set the provided password for the user.

Receives the Password reset and tries to set the provided password for the user. The Password will only be set if a valid token is provided

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import account_service_api
from madana_apiclient.model.json_mdn_password_reset import JsonMDNPasswordReset
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = account_service_api.AccountServiceApi(api_client)
    body = JsonMDNPasswordReset(
        mail="mail_example",
        token="token_example",
        password="password_example",
    ) # JsonMDNPasswordReset | - the MDN_PasswordReset Object (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Receives the Password reset and tries to set the provided password for the user.
        api_response = api_instance.update_password(body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling AccountServiceApi->update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonMDNPasswordReset**](JsonMDNPasswordReset.md)| - the MDN_PasswordReset Object | [optional]

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
**204** | HTTP Status ACCEPTED if password has been reset, FORBIDDEN if the token is invalid, NOT FOUND if the email is invalid, EXPECTATION FAILED if an error occured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

