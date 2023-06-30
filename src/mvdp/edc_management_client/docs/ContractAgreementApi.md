# mvdp.edc_management_client.ContractAgreementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agreement_by_id**](ContractAgreementApi.md#get_agreement_by_id) | **GET** /v2/contractagreements/{id} | 
[**query_all_agreements**](ContractAgreementApi.md#query_all_agreements) | **POST** /v2/contractagreements/request | 


# **get_agreement_by_id**
> ContractAgreementDto get_agreement_by_id(id)



Gets an contract agreement with the given ID

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
    api_instance = mvdp.edc_management_client.ContractAgreementApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_agreement_by_id(id)
        print("The response of ContractAgreementApi->get_agreement_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractAgreementApi->get_agreement_by_id: %s\n" % e)
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
**200** | The contract agreement |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An contract agreement with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_all_agreements**
> List[ContractAgreementDto] query_all_agreements(query_spec_dto=query_spec_dto)



Gets all contract agreements according to a particular query

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.contract_agreement_dto import ContractAgreementDto
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
    api_instance = mvdp.edc_management_client.ContractAgreementApi(api_client)
    query_spec_dto = mvdp.edc_management_client.QuerySpecDto() # QuerySpecDto |  (optional)

    try:
        api_response = api_instance.query_all_agreements(query_spec_dto=query_spec_dto)
        print("The response of ContractAgreementApi->query_all_agreements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractAgreementApi->query_all_agreements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec_dto** | [**QuerySpecDto**](QuerySpecDto.md)|  | [optional] 

### Return type

[**List[ContractAgreementDto]**](ContractAgreementDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Request body was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

