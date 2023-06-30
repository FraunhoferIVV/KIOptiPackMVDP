# mvdp.edc_management_client.PolicyDefinitionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_definition**](PolicyDefinitionApi.md#create_policy_definition) | **POST** /v2/policydefinitions | 
[**delete_policy_definition**](PolicyDefinitionApi.md#delete_policy_definition) | **DELETE** /v2/policydefinitions/{id} | 
[**get_policy_definition**](PolicyDefinitionApi.md#get_policy_definition) | **GET** /v2/policydefinitions/{id} | 
[**query_policy_definitions**](PolicyDefinitionApi.md#query_policy_definitions) | **POST** /v2/policydefinitions/request | 
[**update_policy_definition**](PolicyDefinitionApi.md#update_policy_definition) | **PUT** /v2/policydefinitions/{id} | 


# **create_policy_definition**
> IdResponseDto create_policy_definition(policy_definition_request_dto=policy_definition_request_dto)



Creates a new policy definition

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.id_response_dto import IdResponseDto
from mvdp.edc_management_client.models.policy_definition_request_dto import PolicyDefinitionRequestDto
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
    api_instance = mvdp.edc_management_client.PolicyDefinitionApi(api_client)
    policy_definition_request_dto = mvdp.edc_management_client.PolicyDefinitionRequestDto() # PolicyDefinitionRequestDto |  (optional)

    try:
        api_response = api_instance.create_policy_definition(policy_definition_request_dto=policy_definition_request_dto)
        print("The response of PolicyDefinitionApi->create_policy_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionApi->create_policy_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_definition_request_dto** | [**PolicyDefinitionRequestDto**](PolicyDefinitionRequestDto.md)|  | [optional] 

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
**200** | policy definition was created successfully. Returns the Policy Definition Id and created timestamp |  -  |
**400** | Request body was malformed |  -  |
**409** | Could not create policy definition, because a contract definition with that ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_definition**
> delete_policy_definition(id)



Removes a policy definition with the given ID if possible. Deleting a policy definition is only possible if that policy definition is not yet referenced by a contract definition, in which case an error is returned. DANGER ZONE: Note that deleting policy definitions can have unexpected results, do this at your own risk!

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
    api_instance = mvdp.edc_management_client.PolicyDefinitionApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_policy_definition(id)
    except Exception as e:
        print("Exception when calling PolicyDefinitionApi->delete_policy_definition: %s\n" % e)
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
**200** | Policy definition was deleted successfully |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An policy definition with the given ID does not exist |  -  |
**409** | The policy definition cannot be deleted, because it is referenced by a contract definition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_definition**
> PolicyDefinitionResponseDto get_policy_definition(id)



Gets a policy definition with the given ID

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.policy_definition_response_dto import PolicyDefinitionResponseDto
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
    api_instance = mvdp.edc_management_client.PolicyDefinitionApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_policy_definition(id)
        print("The response of PolicyDefinitionApi->get_policy_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionApi->get_policy_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PolicyDefinitionResponseDto**](PolicyDefinitionResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The  policy definition |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An  policy definition with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_policy_definitions**
> List[PolicyDefinitionResponseDto] query_policy_definitions(query_spec_dto=query_spec_dto)



Returns all policy definitions according to a query

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.policy_definition_response_dto import PolicyDefinitionResponseDto
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
    api_instance = mvdp.edc_management_client.PolicyDefinitionApi(api_client)
    query_spec_dto = mvdp.edc_management_client.QuerySpecDto() # QuerySpecDto |  (optional)

    try:
        api_response = api_instance.query_policy_definitions(query_spec_dto=query_spec_dto)
        print("The response of PolicyDefinitionApi->query_policy_definitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyDefinitionApi->query_policy_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec_dto** | [**QuerySpecDto**](QuerySpecDto.md)|  | [optional] 

### Return type

[**List[PolicyDefinitionResponseDto]**](PolicyDefinitionResponseDto.md)

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

# **update_policy_definition**
> update_policy_definition(id, policy_definition_update_dto=policy_definition_update_dto)



Updates an existing Policy, If the Policy is not found, an error is reported

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.policy_definition_update_dto import PolicyDefinitionUpdateDto
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
    api_instance = mvdp.edc_management_client.PolicyDefinitionApi(api_client)
    id = 'id_example' # str | 
    policy_definition_update_dto = mvdp.edc_management_client.PolicyDefinitionUpdateDto() # PolicyDefinitionUpdateDto |  (optional)

    try:
        api_instance.update_policy_definition(id, policy_definition_update_dto=policy_definition_update_dto)
    except Exception as e:
        print("Exception when calling PolicyDefinitionApi->update_policy_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **policy_definition_update_dto** | [**PolicyDefinitionUpdateDto**](PolicyDefinitionUpdateDto.md)|  | [optional] 

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
**200** | policy definition was updated successfully. Returns the Policy Definition Id and updated timestamp |  -  |
**400** | Request body was malformed |  -  |
**404** | policy definition could not be updated, because it does not exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

