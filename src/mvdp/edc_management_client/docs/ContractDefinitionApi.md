# mvdp.edc_management_client.ContractDefinitionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contract_definition**](ContractDefinitionApi.md#create_contract_definition) | **POST** /v2/contractdefinitions | 
[**delete_contract_definition**](ContractDefinitionApi.md#delete_contract_definition) | **DELETE** /v2/contractdefinitions/{id} | 
[**get_contract_definition**](ContractDefinitionApi.md#get_contract_definition) | **GET** /v2/contractdefinitions/{id} | 
[**query_all_contract_definitions**](ContractDefinitionApi.md#query_all_contract_definitions) | **POST** /v2/contractdefinitions/request | 
[**update_contract_definition**](ContractDefinitionApi.md#update_contract_definition) | **PUT** /v2/contractdefinitions | 


# **create_contract_definition**
> IdResponseDto create_contract_definition(contract_definition_request_dto=contract_definition_request_dto)



Creates a new contract definition

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.contract_definition_request_dto import ContractDefinitionRequestDto
from mvdp.edc_management_client.models.id_response_dto import IdResponseDto
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
    api_instance = mvdp.edc_management_client.ContractDefinitionApi(api_client)
    contract_definition_request_dto = mvdp.edc_management_client.ContractDefinitionRequestDto() # ContractDefinitionRequestDto |  (optional)

    try:
        api_response = api_instance.create_contract_definition(contract_definition_request_dto=contract_definition_request_dto)
        print("The response of ContractDefinitionApi->create_contract_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractDefinitionApi->create_contract_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_definition_request_dto** | [**ContractDefinitionRequestDto**](ContractDefinitionRequestDto.md)|  | [optional] 

### Return type

[**IdResponseDto**](IdResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | contract definition was created successfully. Returns the Contract Definition Id and created timestamp |  -  |
**400** | Request body was malformed |  -  |
**409** | Could not create contract definition, because a contract definition with that ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contract_definition**
> delete_contract_definition(id)



Removes a contract definition with the given ID if possible. DANGER ZONE: Note that deleting contract definitions can have unexpected results, especially for contract offers that have been sent out or ongoing or contract negotiations.

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
    api_instance = mvdp.edc_management_client.ContractDefinitionApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_contract_definition(id)
    except Exception as e:
        print("Exception when calling ContractDefinitionApi->delete_contract_definition: %s\n" % e)
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
**200** | Contract definition was deleted successfully |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A contract definition with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_definition**
> ContractDefinitionResponseDto get_contract_definition(id)



Gets an contract definition with the given ID

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.contract_definition_response_dto import ContractDefinitionResponseDto
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
    api_instance = mvdp.edc_management_client.ContractDefinitionApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_contract_definition(id)
        print("The response of ContractDefinitionApi->get_contract_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractDefinitionApi->get_contract_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ContractDefinitionResponseDto**](ContractDefinitionResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contract definition |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An contract agreement with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_all_contract_definitions**
> List[ContractDefinitionResponseDto] query_all_contract_definitions(query_spec_dto=query_spec_dto)



Returns all contract definitions according to a query

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.contract_definition_response_dto import ContractDefinitionResponseDto
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
    api_instance = mvdp.edc_management_client.ContractDefinitionApi(api_client)
    query_spec_dto = mvdp.edc_management_client.QuerySpecDto() # QuerySpecDto |  (optional)

    try:
        api_response = api_instance.query_all_contract_definitions(query_spec_dto=query_spec_dto)
        print("The response of ContractDefinitionApi->query_all_contract_definitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractDefinitionApi->query_all_contract_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec_dto** | [**QuerySpecDto**](QuerySpecDto.md)|  | [optional] 

### Return type

[**List[ContractDefinitionResponseDto]**](ContractDefinitionResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Request was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contract_definition**
> update_contract_definition(contract_definition_request_dto=contract_definition_request_dto)



Updated a contract definition with the given ID. The supplied JSON structure must be a valid JSON-LD object

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.contract_definition_request_dto import ContractDefinitionRequestDto
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
    api_instance = mvdp.edc_management_client.ContractDefinitionApi(api_client)
    contract_definition_request_dto = mvdp.edc_management_client.ContractDefinitionRequestDto() # ContractDefinitionRequestDto |  (optional)

    try:
        api_instance.update_contract_definition(contract_definition_request_dto=contract_definition_request_dto)
    except Exception as e:
        print("Exception when calling ContractDefinitionApi->update_contract_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_definition_request_dto** | [**ContractDefinitionRequestDto**](ContractDefinitionRequestDto.md)|  | [optional] 

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
**204** | Contract definition was updated successfully |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | A contract definition with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

