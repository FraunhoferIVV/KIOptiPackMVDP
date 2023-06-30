# mvdp.edc_management_client.TransferProcessControlApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete**](TransferProcessControlApiApi.md#complete) | **POST** /transferprocess/{processId}/complete | 
[**fail**](TransferProcessControlApiApi.md#fail) | **POST** /transferprocess/{processId}/fail | 


# **complete**
> complete(process_id)



Requests completion of the transfer process. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received

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
    api_instance = mvdp.edc_management_client.TransferProcessControlApiApi(api_client)
    process_id = 'process_id_example' # str | 

    try:
        api_instance.complete(process_id)
    except Exception as e:
        print("Exception when calling TransferProcessControlApiApi->complete: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Request was malformed, e.g. id was null |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fail**
> fail(process_id, transfer_process_fail_state_dto)



Requests completion of the transfer process. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.transfer_process_fail_state_dto import TransferProcessFailStateDto
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
    api_instance = mvdp.edc_management_client.TransferProcessControlApiApi(api_client)
    process_id = 'process_id_example' # str | 
    transfer_process_fail_state_dto = mvdp.edc_management_client.TransferProcessFailStateDto() # TransferProcessFailStateDto | 

    try:
        api_instance.fail(process_id, transfer_process_fail_state_dto)
    except Exception as e:
        print("Exception when calling TransferProcessControlApiApi->fail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**|  | 
 **transfer_process_fail_state_dto** | [**TransferProcessFailStateDto**](TransferProcessFailStateDto.md)|  | 

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
**400** | Request was malformed, e.g. id was null |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

