# madana_apiclient.DataCollectionServiceApi

All URIs are relative to *http://api.madana.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_methods_for_type**](DataCollectionServiceApi.md#get_methods_for_type) | **GET** /datacollection/types/{name}/methods | 
[**get_nodes**](DataCollectionServiceApi.md#get_nodes) | **GET** /datacollection/methods | 
[**get_types**](DataCollectionServiceApi.md#get_types) | **GET** /datacollection/types | 


# **get_methods_for_type**
> file get_methods_for_type(name)



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
    api_instance = madana_apiclient.DataCollectionServiceApi(api_client)
    name = 'name_example' # str | 

    try:
        api_response = api_instance.get_methods_for_type(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCollectionServiceApi->get_methods_for_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

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

# **get_nodes**
> file get_nodes()



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
    api_instance = madana_apiclient.DataCollectionServiceApi(api_client)
    
    try:
        api_response = api_instance.get_nodes()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCollectionServiceApi->get_nodes: %s\n" % e)
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

# **get_types**
> file get_types()



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
    api_instance = madana_apiclient.DataCollectionServiceApi(api_client)
    
    try:
        api_response = api_instance.get_types()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCollectionServiceApi->get_types: %s\n" % e)
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

