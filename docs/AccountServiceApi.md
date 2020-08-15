# madana_sampleclient_python.AccountServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_user**](AccountServiceApi.md#activate_user) | **GET** /account/activation/{token} | 
[**create_object**](AccountServiceApi.md#create_object) | **POST** /account/password | Sends an Password reset mail to the given MailAddress.
[**request_verification_mail**](AccountServiceApi.md#request_verification_mail) | **GET** /account/verifymail | Used to request a new  activation-mail for the user.
[**update_object**](AccountServiceApi.md#update_object) | **PUT** /account/password | Receives the Password reset and tries to set the provided password for the user.


# **activate_user**
> file activate_user(token)



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
    api_instance = madana_sampleclient_python.AccountServiceApi(api_client)
    token = 'token_example' # str | 

    try:
        api_response = api_instance.activate_user(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountServiceApi->activate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_object**
> file create_object(body=body)

Sends an Password reset mail to the given MailAddress.

Sends an Password reset mail to the given MailAddress

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
    api_instance = madana_sampleclient_python.AccountServiceApi(api_client)
    body = madana_sampleclient_python.JsonMDNMailAddress() # JsonMDNMailAddress | - the MaiAddress under which the user has signed up (optional)

    try:
        # Sends an Password reset mail to the given MailAddress.
        api_response = api_instance.create_object(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountServiceApi->create_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonMDNMailAddress**](JsonMDNMailAddress.md)| - the MaiAddress under which the user has signed up | [optional] 

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
**201** | HTTP Status Accepted if the mail has been send, NOT FOUND if the mail address could be found in the system or EXPECTATION FAILED when an error occured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_verification_mail**
> dict(str, object) request_verification_mail()

Used to request a new  activation-mail for the user.

Used to request a new  activation-mail for the user

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
    api_instance = madana_sampleclient_python.AccountServiceApi(api_client)
    
    try:
        # Used to request a new  activation-mail for the user.
        api_response = api_instance.request_verification_mail()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountServiceApi->request_verification_mail: %s\n" % e)
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
**200** | If the mail has been sent |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object**
> file update_object(body=body)

Receives the Password reset and tries to set the provided password for the user.

Receives the Password reset and tries to set the provided password for the user. The Password will only be set if a valid token is provided

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
    api_instance = madana_sampleclient_python.AccountServiceApi(api_client)
    body = madana_sampleclient_python.JsonMDNPasswordReset() # JsonMDNPasswordReset | - the MDN_PasswordReset Object (optional)

    try:
        # Receives the Password reset and tries to set the provided password for the user.
        api_response = api_instance.update_object(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountServiceApi->update_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonMDNPasswordReset**](JsonMDNPasswordReset.md)| - the MDN_PasswordReset Object | [optional] 

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
**204** | HTTP Status ACCEPTED if password has been reset, FORBIDDEN if the token is invalid, NOT FOUND if the email is invalid, EXPECTATION FAILED if an error occured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

