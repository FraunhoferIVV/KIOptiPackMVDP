# mvdp.edc_management_client.ContractNegotiationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_negotiation**](ContractNegotiationApi.md#cancel_negotiation) | **POST** /v2/contractnegotiations/{id}/cancel | 
[**decline_negotiation**](ContractNegotiationApi.md#decline_negotiation) | **POST** /v2/contractnegotiations/{id}/decline | 
[**get_agreement_for_negotiation**](ContractNegotiationApi.md#get_agreement_for_negotiation) | **GET** /v2/contractnegotiations/{id}/agreement | 
[**get_negotiation**](ContractNegotiationApi.md#get_negotiation) | **GET** /v2/contractnegotiations/{id} | 
[**get_negotiation_state**](ContractNegotiationApi.md#get_negotiation_state) | **GET** /v2/contractnegotiations/{id}/state | 
[**initiate_contract_negotiation**](ContractNegotiationApi.md#initiate_contract_negotiation) | **POST** /v2/contractnegotiations | 
[**query_negotiations**](ContractNegotiationApi.md#query_negotiations) | **POST** /v2/contractnegotiations/request | 


# **cancel_negotiation**
> cancel_negotiation(id)



Requests aborting the contract negotiation. Due to the asynchronous nature of contract negotiations, a successful response only indicates that the request was successfully received. Clients must poll the /{id}/state endpoint to track the state.

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
    api_instance = mvdp.edc_management_client.ContractNegotiationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.cancel_negotiation(id)
    except Exception as e:
        print("Exception when calling ContractNegotiationApi->cancel_negotiation: %s\n" % e)
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
**200** | Request to cancel the Contract negotiation was successfully received |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A contract negotiation with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decline_negotiation**
> decline_negotiation(id)



Requests cancelling the contract negotiation. Due to the asynchronous nature of contract negotiations, a successful response only indicates that the request was successfully received. Clients must poll the /{id}/state endpoint to track the state.

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
    api_instance = mvdp.edc_management_client.ContractNegotiationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.decline_negotiation(id)
    except Exception as e:
        print("Exception when calling ContractNegotiationApi->decline_negotiation: %s\n" % e)
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
**200** | Request to decline the Contract negotiation was successfully received |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A contract negotiation with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agreement_for_negotiation**
> ContractAgreementDto get_agreement_for_negotiation(id)



Gets a contract agreement for a contract negotiation with the given ID

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.contract_agreement_dto import ContractAgreementDto
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
    api_instance = mvdp.edc_management_client.ContractNegotiationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_agreement_for_negotiation(id)
        print("The response of ContractNegotiationApi->get_agreement_for_negotiation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractNegotiationApi->get_agreement_for_negotiation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ContractAgreementDto**](ContractAgreementDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contract agreement that is attached to the negotiation, or null |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An contract negotiation with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_negotiation**
> ContractNegotiationDto get_negotiation(id)



Gets a contract negotiation with the given ID

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.contract_negotiation_dto import ContractNegotiationDto
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
    api_instance = mvdp.edc_management_client.ContractNegotiationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_negotiation(id)
        print("The response of ContractNegotiationApi->get_negotiation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractNegotiationApi->get_negotiation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ContractNegotiationDto**](ContractNegotiationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contract negotiation |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An contract negotiation with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_negotiation_state**
> NegotiationState get_negotiation_state(id)



Gets the state of a contract negotiation with the given ID

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.negotiation_state import NegotiationState
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
    api_instance = mvdp.edc_management_client.ContractNegotiationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_negotiation_state(id)
        print("The response of ContractNegotiationApi->get_negotiation_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractNegotiationApi->get_negotiation_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**NegotiationState**](NegotiationState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contract negotiation&#39;s state |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An contract negotiation with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_contract_negotiation**
> IdResponseDto initiate_contract_negotiation(negotiation_initiate_request_dto=negotiation_initiate_request_dto)



Initiates a contract negotiation for a given offer and with the given counter part. Please note that successfully invoking this endpoint only means that the negotiation was initiated. Clients must poll the /{id}/state endpoint to track the state

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.id_response_dto import IdResponseDto
from mvdp.edc_management_client.models.negotiation_initiate_request_dto import NegotiationInitiateRequestDto
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
    api_instance = mvdp.edc_management_client.ContractNegotiationApi(api_client)
    negotiation_initiate_request_dto = mvdp.edc_management_client.NegotiationInitiateRequestDto() # NegotiationInitiateRequestDto |  (optional)

    try:
        api_response = api_instance.initiate_contract_negotiation(negotiation_initiate_request_dto=negotiation_initiate_request_dto)
        print("The response of ContractNegotiationApi->initiate_contract_negotiation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractNegotiationApi->initiate_contract_negotiation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **negotiation_initiate_request_dto** | [**NegotiationInitiateRequestDto**](NegotiationInitiateRequestDto.md)|  | [optional] 

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
**200** | The negotiation was successfully initiated. Returns the contract negotiation ID and created timestamp |  -  |
**400** | Request body was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_negotiations**
> List[ContractNegotiationDto] query_negotiations(query_spec_dto=query_spec_dto)



Returns all contract negotiations according to a query

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.contract_negotiation_dto import ContractNegotiationDto
from mvdp.edc_management_client.models.query_spec_dto import QuerySpecDto
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
    api_instance = mvdp.edc_management_client.ContractNegotiationApi(api_client)
    query_spec_dto = mvdp.edc_management_client.QuerySpecDto() # QuerySpecDto |  (optional)

    try:
        api_response = api_instance.query_negotiations(query_spec_dto=query_spec_dto)
        print("The response of ContractNegotiationApi->query_negotiations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractNegotiationApi->query_negotiations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec_dto** | [**QuerySpecDto**](QuerySpecDto.md)|  | [optional] 

### Return type

[**List[ContractNegotiationDto]**](ContractNegotiationDto.md)

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

