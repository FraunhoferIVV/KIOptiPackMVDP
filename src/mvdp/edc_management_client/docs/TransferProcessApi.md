# mvdp.edc_management_client.TransferProcessApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deprovision_transfer_process**](TransferProcessApi.md#deprovision_transfer_process) | **POST** /v2/transferprocesses/{id}/deprovision | 
[**get_transfer_process**](TransferProcessApi.md#get_transfer_process) | **GET** /v2/transferprocesses/{id} | 
[**get_transfer_process_state**](TransferProcessApi.md#get_transfer_process_state) | **GET** /v2/transferprocesses/{id}/state | 
[**initiate_transfer_process**](TransferProcessApi.md#initiate_transfer_process) | **POST** /v2/transferprocesses | 
[**query_transfer_processes**](TransferProcessApi.md#query_transfer_processes) | **POST** /v2/transferprocesses/request | 
[**terminate_transfer_process**](TransferProcessApi.md#terminate_transfer_process) | **POST** /v2/transferprocesses/{id}/terminate | 


# **deprovision_transfer_process**
> deprovision_transfer_process(id)



Requests the deprovisioning of resources associated with a transfer process. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received. This may take a long time, so clients must poll the /{id}/state endpoint to track the state.

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
    api_instance = mvdp.edc_management_client.TransferProcessApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.deprovision_transfer_process(id)
    except Exception as e:
        print("Exception when calling TransferProcessApi->deprovision_transfer_process: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**200** | Request to deprovision the transfer process was successfully received |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A contract negotiation with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfer_process**
> TransferProcessDto get_transfer_process(id)



Gets an transfer process with the given ID

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.transfer_process_dto import TransferProcessDto
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
    api_instance = mvdp.edc_management_client.TransferProcessApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_transfer_process(id)
        print("The response of TransferProcessApi->get_transfer_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessApi->get_transfer_process: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TransferProcessDto**](TransferProcessDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transfer process |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A transfer process with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfer_process_state**
> TransferState get_transfer_process_state(id)



Gets the state of a transfer process with the given ID

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.transfer_state import TransferState
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
    api_instance = mvdp.edc_management_client.TransferProcessApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_transfer_process_state(id)
        print("The response of TransferProcessApi->get_transfer_process_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessApi->get_transfer_process_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TransferState**](TransferState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The  transfer process&#39;s state |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An  transfer process with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_transfer_process**
> IdResponseDto initiate_transfer_process(transfer_request_dto=transfer_request_dto)



Initiates a data transfer with the given parameters. Please note that successfully invoking this endpoint only means that the transfer was initiated. Clients must poll the /{id}/state endpoint to track the state

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.id_response_dto import IdResponseDto
from mvdp.edc_management_client.models.transfer_request_dto import TransferRequestDto
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
    api_instance = mvdp.edc_management_client.TransferProcessApi(api_client)
    transfer_request_dto = mvdp.edc_management_client.TransferRequestDto() # TransferRequestDto |  (optional)

    try:
        api_response = api_instance.initiate_transfer_process(transfer_request_dto=transfer_request_dto)
        print("The response of TransferProcessApi->initiate_transfer_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessApi->initiate_transfer_process: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_request_dto** | [**TransferRequestDto**](TransferRequestDto.md)|  | [optional] 

### Return type

[**IdResponseDto**](IdResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transfer was successfully initiated. Returns the transfer process ID and created timestamp |  -  |
**400** | Request body was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_transfer_processes**
> List[TransferProcessDto] query_transfer_processes(query_spec_dto=query_spec_dto)



Returns all transfer process according to a query

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.query_spec_dto import QuerySpecDto
from mvdp.edc_management_client.models.transfer_process_dto import TransferProcessDto
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
    api_instance = mvdp.edc_management_client.TransferProcessApi(api_client)
    query_spec_dto = mvdp.edc_management_client.QuerySpecDto() # QuerySpecDto |  (optional)

    try:
        api_response = api_instance.query_transfer_processes(query_spec_dto=query_spec_dto)
        print("The response of TransferProcessApi->query_transfer_processes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferProcessApi->query_transfer_processes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec_dto** | [**QuerySpecDto**](QuerySpecDto.md)|  | [optional] 

### Return type

[**List[TransferProcessDto]**](TransferProcessDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Request was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_transfer_process**
> terminate_transfer_process(id, terminate_transfer_dto=terminate_transfer_dto)



Requests the termination of a transfer process. Due to the asynchronous nature of transfers, a successful response only indicates that the request was successfully received. Clients must poll the /{id}/state endpoint to track the state.

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.terminate_transfer_dto import TerminateTransferDto
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
    api_instance = mvdp.edc_management_client.TransferProcessApi(api_client)
    id = 'id_example' # str | 
    terminate_transfer_dto = mvdp.edc_management_client.TerminateTransferDto() # TerminateTransferDto |  (optional)

    try:
        api_instance.terminate_transfer_process(id, terminate_transfer_dto=terminate_transfer_dto)
    except Exception as e:
        print("Exception when calling TransferProcessApi->terminate_transfer_process: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **terminate_transfer_dto** | [**TerminateTransferDto**](TerminateTransferDto.md)|  | [optional] 

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
**200** | Request to cancel the transfer process was successfully received |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A contract negotiation with the given ID does not exist |  -  |
**409** | Could not terminate transfer process, because it is already completed or terminated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

