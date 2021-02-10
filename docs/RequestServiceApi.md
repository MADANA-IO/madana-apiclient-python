# madana_apiclient.RequestServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_data**](RequestServiceApi.md#add_data) | **POST** /requests/{uuid}/data | Is used to upload and park the data till the AnalysisRequest gets processed.
[**cancel_processing**](RequestServiceApi.md#cancel_processing) | **POST** /requests/{uuid}/cancel | Endpoint is called from the Analysis Processing entity to submit the result.
[**create_new_request**](RequestServiceApi.md#create_new_request) | **POST** /requests | Endpoint used to create a new Analysis Request.
[**get_actions**](RequestServiceApi.md#get_actions) | **GET** /requests/actions | 
[**get_agent**](RequestServiceApi.md#get_agent) | **GET** /requests/{uuid}/agent | Is called from the APE to request all parked datasets.
[**get_all_requests**](RequestServiceApi.md#get_all_requests) | **GET** /requests | Returns UUIDs of existing analyses.
[**get_data**](RequestServiceApi.md#get_data) | **GET** /requests/{uuid}/data | Is called from the APE to request all parked datasets.
[**get_request**](RequestServiceApi.md#get_request) | **GET** /requests/{uuid} | Returns the details for certain Request.
[**get_result**](RequestServiceApi.md#get_result) | **GET** /requests/{uuid}/result | Can be called from creator to request the AnalysisResult.
[**get_status**](RequestServiceApi.md#get_status) | **GET** /requests/stats | 
[**give_consent**](RequestServiceApi.md#give_consent) | **POST** /requests/{uuid}/consent | Used to give consent for request.
[**init_request_parameters**](RequestServiceApi.md#init_request_parameters) | **POST** /requests/{uuid} | Endpoint used initialized addition datacollection parameters for requester.
[**set_agent**](RequestServiceApi.md#set_agent) | **POST** /requests/{uuid}/agent | Is called from the APE to request all parked datasets.
[**set_result**](RequestServiceApi.md#set_result) | **POST** /requests/{uuid}/result | Endpoint is called from the Analysis Processing entity to submit the result.


# **add_data**
> file_type add_data(uuid)

Is used to upload and park the data till the AnalysisRequest gets processed.

Is used to upload and park the data till the AnalysisRequest gets processed

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import request_service_api
from madana_apiclient.model.json_signed_data import JsonSignedData
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_service_api.RequestServiceApi(api_client)
    uuid = "uuid_example" # str | 
    authorization = "Authorization_example" # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)
    body = JsonSignedData(
        signature="signature_example",
        data="data_example",
        fingerpint="fingerpint_example",
    ) # JsonSignedData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Is used to upload and park the data till the AnalysisRequest gets processed.
        api_response = api_instance.add_data(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->add_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Is used to upload and park the data till the AnalysisRequest gets processed.
        api_response = api_instance.add_data(uuid, authorization=authorization, body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->add_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional]
 **body** | [**JsonSignedData**](JsonSignedData.md)|  | [optional]

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the data has been sucessfully received |  -  |
**404** | If the uuid of the request cannot be found |  -  |
**406** | If an unprivileged user tries to send data |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_processing**
> file_type cancel_processing(uuid)

Endpoint is called from the Analysis Processing entity to submit the result.

Endpoint is called from the Analysis Processing entity to submit the result

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import request_service_api
from madana_apiclient.model.json_signed_data import JsonSignedData
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_service_api.RequestServiceApi(api_client)
    uuid = "uuid_example" # str | 
    authorization = "Authorization_example" # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)
    body = JsonSignedData(
        signature="signature_example",
        data="data_example",
        fingerpint="fingerpint_example",
    ) # JsonSignedData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Endpoint is called from the Analysis Processing entity to submit the result.
        api_response = api_instance.cancel_processing(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->cancel_processing: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Endpoint is called from the Analysis Processing entity to submit the result.
        api_response = api_instance.cancel_processing(uuid, authorization=authorization, body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->cancel_processing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional]
 **body** | [**JsonSignedData**](JsonSignedData.md)|  | [optional]

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
**200** | If the result has been received |  -  |
**404** | If the uuid of the request cannot be found |  -  |
**406** | If  the AnalysisRequest has been completed, or the result is malformed |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_request**
> str create_new_request()

Endpoint used to create a new Analysis Request.

Endpoint used to create a new Analysis Request

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import request_service_api
from madana_apiclient.model.json_signed_data import JsonSignedData
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_service_api.RequestServiceApi(api_client)
    authorization = "Authorization_example" # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)
    body = JsonSignedData(
        signature="signature_example",
        data="data_example",
        fingerpint="fingerpint_example",
    ) # JsonSignedData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Endpoint used to create a new Analysis Request.
        api_response = api_instance.create_new_request(authorization=authorization, body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->create_new_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional]
 **body** | [**JsonSignedData**](JsonSignedData.md)|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the request has been created |  -  |
**403** | If the calling entity is not allowed to create the request |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions**
> file_type get_actions()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import request_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_service_api.RequestServiceApi(api_client)
    limit = "30" # str |  (optional) if omitted the server will use the default value of "30"
    offset = "0" # str |  (optional) if omitted the server will use the default value of "0"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_actions(limit=limit, offset=offset)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->get_actions: %s\n" % e)
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

# **get_agent**
> file_type get_agent(uuid)

Is called from the APE to request all parked datasets.

Is called from the APE to request all parked datasets. Returns the transmitted data for certain Request. When requesting the data, the status of the request is automatically set to processing.

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import request_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_service_api.RequestServiceApi(api_client)
    uuid = "uuid_example" # str | 
    authorization = "Authorization_example" # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)

    # example passing only required values which don't have defaults set
    try:
        # Is called from the APE to request all parked datasets.
        api_response = api_instance.get_agent(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->get_agent: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Is called from the APE to request all parked datasets.
        api_response = api_instance.get_agent(uuid, authorization=authorization)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->get_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional]

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
**200** | If the consent has been received could be loaded |  -  |
**403** | If the endpoint is not called from the set agent / APE |  -  |
**404** | If the uuid of the request cannot be found |  -  |
**406** | If the AnalysisRequest has been completed |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_requests**
> file_type get_all_requests()

Returns UUIDs of existing analyses.

Returns UUIDs of existing analyses.

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import request_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_service_api.RequestServiceApi(api_client)
    authorization = "Authorization_example" # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)
    created = "false" # str | - if Queryparam \"created=true\" only the UUIDs of own Requests are shown (optional) if omitted the server will use the default value of "false"
    history = "false" # str | - if queryparam \"history\" is set to true, endpoint returns all user actions. False per default. (optional) if omitted the server will use the default value of "false"
    limit = "30" # str | Used for offset pagination. Limit/Offset Paging would look like GET /request?limit=20&offset=100. This query would return the 20 rows starting with the 100th row (optional) if omitted the server will use the default value of "30"
    new = "true" # str | -  if Queryparam \"new=true\" only the UUIDs of new Requests ( Requests the user has not participated in and still allow participation) are shown (optional) if omitted the server will use the default value of "true"
    offset = "0" # str | Used for offset pagination. Limit/Offset Paging would look like GET /request?limit=20&offset=100. This query would return the 20 rows starting with the 100th row (optional) if omitted the server will use the default value of "0"
    preview = "false" # str |  (optional) if omitted the server will use the default value of "false"
    ready = "false" # str |  (optional) if omitted the server will use the default value of "false"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns UUIDs of existing analyses.
        api_response = api_instance.get_all_requests(authorization=authorization, created=created, history=history, limit=limit, new=new, offset=offset, preview=preview, ready=ready)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->get_all_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional]
 **created** | **str**| - if Queryparam \&quot;created&#x3D;true\&quot; only the UUIDs of own Requests are shown | [optional] if omitted the server will use the default value of "false"
 **history** | **str**| - if queryparam \&quot;history\&quot; is set to true, endpoint returns all user actions. False per default. | [optional] if omitted the server will use the default value of "false"
 **limit** | **str**| Used for offset pagination. Limit/Offset Paging would look like GET /request?limit&#x3D;20&amp;offset&#x3D;100. This query would return the 20 rows starting with the 100th row | [optional] if omitted the server will use the default value of "30"
 **new** | **str**| -  if Queryparam \&quot;new&#x3D;true\&quot; only the UUIDs of new Requests ( Requests the user has not participated in and still allow participation) are shown | [optional] if omitted the server will use the default value of "true"
 **offset** | **str**| Used for offset pagination. Limit/Offset Paging would look like GET /request?limit&#x3D;20&amp;offset&#x3D;100. This query would return the 20 rows starting with the 100th row | [optional] if omitted the server will use the default value of "0"
 **preview** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **ready** | **str**|  | [optional] if omitted the server will use the default value of "false"

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

# **get_data**
> JsonSignedData get_data(uuid)

Is called from the APE to request all parked datasets.

Is called from the APE to request all parked datasets. Returns the transmitted data for certain Request. When requesting the data, the status of the request is automatically set to processing.

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import request_service_api
from madana_apiclient.model.json_signed_data import JsonSignedData
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_service_api.RequestServiceApi(api_client)
    uuid = "uuid_example" # str | 
    authorization = "Authorization_example" # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)

    # example passing only required values which don't have defaults set
    try:
        # Is called from the APE to request all parked datasets.
        api_response = api_instance.get_data(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->get_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Is called from the APE to request all parked datasets.
        api_response = api_instance.get_data(uuid, authorization=authorization)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->get_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional]

### Return type

[**JsonSignedData**](JsonSignedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the consent has been received could be loaded |  -  |
**403** | If the endpoint is not called from the set agent / APE |  -  |
**404** | If the uuid of the request cannot be found |  -  |
**406** | If the AnalysisRequest has been completed |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request**
> file_type get_request(uuid)

Returns the details for certain Request.

Returns the details for certain Request. When requesting an analysis a view of the analysis is stored in the database

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import request_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_service_api.RequestServiceApi(api_client)
    uuid = "uuid_example" # str | 
    authorization = "Authorization_example" # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns the details for certain Request.
        api_response = api_instance.get_request(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->get_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the details for certain Request.
        api_response = api_instance.get_request(uuid, authorization=authorization)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->get_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional]

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
**200** | If the consent has been received could be loaded |  -  |
**404** | If the uuid of the request cannot be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result**
> file_type get_result(uuid)

Can be called from creator to request the AnalysisResult.

Can be called from creator to request the AnalysisResult.

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import request_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_service_api.RequestServiceApi(api_client)
    uuid = "uuid_example" # str | 
    authorization = "Authorization_example" # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)

    # example passing only required values which don't have defaults set
    try:
        # Can be called from creator to request the AnalysisResult.
        api_response = api_instance.get_result(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->get_result: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Can be called from creator to request the AnalysisResult.
        api_response = api_instance.get_result(uuid, authorization=authorization)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->get_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional]

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
**200** | If the consent has been received could be loaded |  -  |
**403** | If the endpoint is not called from the set agent / APE |  -  |
**404** | If the uuid of the request cannot be found |  -  |
**406** | If the AnalysisRequest has been completed |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> file_type get_status()



### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import request_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_service_api.RequestServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_status()
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->get_status: %s\n" % e)
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

# **give_consent**
> file_type give_consent(uuid)

Used to give consent for request.

Used to give consent for request. If the Endpoint is called from the creator of the Analysis, the status of the request is set to completed. If called by another is interpreted as giving consent to participate.

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import request_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_service_api.RequestServiceApi(api_client)
    uuid = "uuid_example" # str | 
    authorization = "Authorization_example" # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)

    # example passing only required values which don't have defaults set
    try:
        # Used to give consent for request.
        api_response = api_instance.give_consent(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->give_consent: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Used to give consent for request.
        api_response = api_instance.give_consent(uuid, authorization=authorization)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->give_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional]

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
**200** | If the consent has been received could be loaded |  -  |
**404** | If the uuid of the request cannot be found |  -  |
**406** | If no consent can be received anymore because the AnalysisRequest is already being processed or completed |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_request_parameters**
> str init_request_parameters(uuid)

Endpoint used initialized addition datacollection parameters for requester.

Endpoint used initialized addition datacollection parameters for requester

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import request_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_service_api.RequestServiceApi(api_client)
    uuid = "uuid_example" # str | 
    authorization = "Authorization_example" # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Endpoint used initialized addition datacollection parameters for requester.
        api_response = api_instance.init_request_parameters(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->init_request_parameters: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Endpoint used initialized addition datacollection parameters for requester.
        api_response = api_instance.init_request_parameters(uuid, authorization=authorization, body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->init_request_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional]
 **body** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If the request has been created |  -  |
**403** | If the calling entity is not allowed to create the request |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_agent**
> file_type set_agent(uuid)

Is called from the APE to request all parked datasets.

Is called from the APE to request all parked datasets. Returns the transmitted data for certain Request. When requesting the data, the status of the request is automatically set to processing.

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import request_service_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_service_api.RequestServiceApi(api_client)
    uuid = "uuid_example" # str | 
    authorization = "Authorization_example" # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)

    # example passing only required values which don't have defaults set
    try:
        # Is called from the APE to request all parked datasets.
        api_response = api_instance.set_agent(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->set_agent: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Is called from the APE to request all parked datasets.
        api_response = api_instance.set_agent(uuid, authorization=authorization)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->set_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional]

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
**200** | If the consent has been received could be loaded |  -  |
**403** | If the endpoint is not called from the set agent / APE |  -  |
**404** | If the uuid of the request cannot be found |  -  |
**406** | If the AnalysisRequest has been completed |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_result**
> file_type set_result(uuid)

Endpoint is called from the Analysis Processing entity to submit the result.

Endpoint is called from the Analysis Processing entity to submit the result

### Example

```python
import time
import madana_apiclient
from madana_apiclient.api import request_service_api
from madana_apiclient.model.json_signed_data import JsonSignedData
from pprint import pprint
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)


# Enter a context with an instance of the API client
with madana_apiclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_service_api.RequestServiceApi(api_client)
    uuid = "uuid_example" # str | 
    authorization = "Authorization_example" # str | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c (optional)
    body = JsonSignedData(
        signature="signature_example",
        data="data_example",
        fingerpint="fingerpint_example",
    ) # JsonSignedData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Endpoint is called from the Analysis Processing entity to submit the result.
        api_response = api_instance.set_result(uuid)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->set_result: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Endpoint is called from the Analysis Processing entity to submit the result.
        api_response = api_instance.set_result(uuid, authorization=authorization, body=body)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling RequestServiceApi->set_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  |
 **authorization** | **str**| Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c | [optional]
 **body** | [**JsonSignedData**](JsonSignedData.md)|  | [optional]

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
**200** | If the result has been received |  -  |
**404** | If the uuid of the request cannot be found |  -  |
**406** | If  the AnalysisRequest has been completed, or the result is malformed |  -  |
**500** | If an servsided error occurs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

