# madana_sampleclient_python.OrganizationServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nodes3**](OrganizationServiceApi.md#get_nodes3) | **GET** /organizations | 


# **get_nodes3**
> file get_nodes3()



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
    api_instance = madana_sampleclient_python.OrganizationServiceApi(api_client)
    
    try:
        api_response = api_instance.get_nodes3()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganizationServiceApi->get_nodes3: %s\n" % e)
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

