# mvdp.edc_management_client.DataPlaneControlAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transfer_state**](DataPlaneControlAPIApi.md#get_transfer_state) | **GET** /transfer/{processId} | 
[**initiate_transfer**](DataPlaneControlAPIApi.md#initiate_transfer) | **POST** /transfer | 


# **get_transfer_state**
> get_transfer_state(process_id)



Get the current state of a data transfer.

### Example

```python
import time
import os
import mvdp.edc_management_client
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
    api_instance = mvdp.edc_management_client.DataPlaneControlAPIApi(api_client)
    process_id = 'process_id_example' # str | 

    try:
        api_instance.get_transfer_state(process_id)
    except Exception as e:
        print("Exception when calling DataPlaneControlAPIApi->get_transfer_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Missing access token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_transfer**
> initiate_transfer(data_flow_request=data_flow_request)



Initiates a data transfer for the given request. The transfer will be performed asynchronously.

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.data_flow_request import DataFlowRequest
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
    api_instance = mvdp.edc_management_client.DataPlaneControlAPIApi(api_client)
    data_flow_request = mvdp.edc_management_client.DataFlowRequest() # DataFlowRequest |  (optional)

    try:
        api_instance.initiate_transfer(data_flow_request=data_flow_request)
    except Exception as e:
        print("Exception when calling DataPlaneControlAPIApi->initiate_transfer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_flow_request** | [**DataFlowRequest**](DataFlowRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data transfer initiated |  -  |
**400** | Failed to validate request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

