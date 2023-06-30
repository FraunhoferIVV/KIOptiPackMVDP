# mvdp.edc_management_client.DataplaneSelectorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_entry**](DataplaneSelectorApi.md#add_entry) | **POST** /instances | 
[**find**](DataplaneSelectorApi.md#find) | **POST** /instances/select | 
[**get_all**](DataplaneSelectorApi.md#get_all) | **GET** /instances | 


# **add_entry**
> add_entry(data_plane_instance=data_plane_instance)



### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.data_plane_instance import DataPlaneInstance
from mvdp.edc_management_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mvdp.edc_management_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mvdp.edc_management_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mvdp.edc_management_client.DataplaneSelectorApi(api_client)
    data_plane_instance = mvdp.edc_management_client.DataPlaneInstance() # DataPlaneInstance |  (optional)

    try:
        api_instance.add_entry(data_plane_instance=data_plane_instance)
    except Exception as e:
        print("Exception when calling DataplaneSelectorApi->add_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_plane_instance** | [**DataPlaneInstance**](DataPlaneInstance.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find**
> DataPlaneInstance find(selection_request=selection_request)



### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.data_plane_instance import DataPlaneInstance
from mvdp.edc_management_client.models.selection_request import SelectionRequest
from mvdp.edc_management_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mvdp.edc_management_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mvdp.edc_management_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mvdp.edc_management_client.DataplaneSelectorApi(api_client)
    selection_request = mvdp.edc_management_client.SelectionRequest() # SelectionRequest |  (optional)

    try:
        api_response = api_instance.find(selection_request=selection_request)
        print("The response of DataplaneSelectorApi->find:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataplaneSelectorApi->find: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selection_request** | [**SelectionRequest**](SelectionRequest.md)|  | [optional] 

### Return type

[**DataPlaneInstance**](DataPlaneInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> List[DataPlaneInstance] get_all()



### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.data_plane_instance import DataPlaneInstance
from mvdp.edc_management_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mvdp.edc_management_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mvdp.edc_management_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mvdp.edc_management_client.DataplaneSelectorApi(api_client)

    try:
        api_response = api_instance.get_all()
        print("The response of DataplaneSelectorApi->get_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataplaneSelectorApi->get_all: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[DataPlaneInstance]**](DataPlaneInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

