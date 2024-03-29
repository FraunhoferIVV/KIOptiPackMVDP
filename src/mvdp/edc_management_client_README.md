# mvdp.edc-management-client
EDC REST APIs - merged by OpenApiMerger

The `mvdp.edc_management_client` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0-SNAPSHOT
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.25.3
* python-dateutil
* pydantic
* aenum

## Getting Started

In your own code, to use this library to connect and interact with mvdp.edc-management-client,
you can run the following:

```python

import time
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
    api_instance = mvdp.edc_management_client.ApplicationObservabilityApi(api_client)

    try:
        api_response = api_instance.check_health()
        print("The response of ApplicationObservabilityApi->check_health:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationObservabilityApi->check_health: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApplicationObservabilityApi* | [**check_health**](mvdp/edc_management_client/docs/ApplicationObservabilityApi.md#check_health) | **GET** /check/health | 
*ApplicationObservabilityApi* | [**get_liveness**](mvdp/edc_management_client/docs/ApplicationObservabilityApi.md#get_liveness) | **GET** /check/liveness | 
*ApplicationObservabilityApi* | [**get_readiness**](mvdp/edc_management_client/docs/ApplicationObservabilityApi.md#get_readiness) | **GET** /check/readiness | 
*ApplicationObservabilityApi* | [**get_startup**](mvdp/edc_management_client/docs/ApplicationObservabilityApi.md#get_startup) | **GET** /check/startup | 
*AssetApi* | [**create_asset**](mvdp/edc_management_client/docs/AssetApi.md#create_asset) | **POST** /v2/assets | 
*AssetApi* | [**get_asset**](mvdp/edc_management_client/docs/AssetApi.md#get_asset) | **GET** /v2/assets/{id} | 
*AssetApi* | [**get_asset_data_address**](mvdp/edc_management_client/docs/AssetApi.md#get_asset_data_address) | **GET** /v2/assets/{id}/dataaddress | 
*AssetApi* | [**remove_asset**](mvdp/edc_management_client/docs/AssetApi.md#remove_asset) | **DELETE** /v2/assets/{id} | 
*AssetApi* | [**request_assets**](mvdp/edc_management_client/docs/AssetApi.md#request_assets) | **POST** /v2/assets/request | 
*AssetApi* | [**update_asset**](mvdp/edc_management_client/docs/AssetApi.md#update_asset) | **PUT** /v2/assets | 
*AssetApi* | [**update_data_address**](mvdp/edc_management_client/docs/AssetApi.md#update_data_address) | **PUT** /v2/assets/{assetId}/dataaddress | 
*CatalogApi* | [**request_catalog**](mvdp/edc_management_client/docs/CatalogApi.md#request_catalog) | **POST** /v2/catalog/request | 
*ConsumerPullTokenValidationApi* | [**validate**](mvdp/edc_management_client/docs/ConsumerPullTokenValidationApi.md#validate) | **GET** /token | 
*ContractAgreementApi* | [**get_agreement_by_id**](mvdp/edc_management_client/docs/ContractAgreementApi.md#get_agreement_by_id) | **GET** /v2/contractagreements/{id} | 
*ContractAgreementApi* | [**query_all_agreements**](mvdp/edc_management_client/docs/ContractAgreementApi.md#query_all_agreements) | **POST** /v2/contractagreements/request | 
*ContractDefinitionApi* | [**create_contract_definition**](mvdp/edc_management_client/docs/ContractDefinitionApi.md#create_contract_definition) | **POST** /v2/contractdefinitions | 
*ContractDefinitionApi* | [**delete_contract_definition**](mvdp/edc_management_client/docs/ContractDefinitionApi.md#delete_contract_definition) | **DELETE** /v2/contractdefinitions/{id} | 
*ContractDefinitionApi* | [**get_contract_definition**](mvdp/edc_management_client/docs/ContractDefinitionApi.md#get_contract_definition) | **GET** /v2/contractdefinitions/{id} | 
*ContractDefinitionApi* | [**query_all_contract_definitions**](mvdp/edc_management_client/docs/ContractDefinitionApi.md#query_all_contract_definitions) | **POST** /v2/contractdefinitions/request | 
*ContractDefinitionApi* | [**update_contract_definition**](mvdp/edc_management_client/docs/ContractDefinitionApi.md#update_contract_definition) | **PUT** /v2/contractdefinitions | 
*ContractNegotiationApi* | [**cancel_negotiation**](mvdp/edc_management_client/docs/ContractNegotiationApi.md#cancel_negotiation) | **POST** /v2/contractnegotiations/{id}/cancel | 
*ContractNegotiationApi* | [**decline_negotiation**](mvdp/edc_management_client/docs/ContractNegotiationApi.md#decline_negotiation) | **POST** /v2/contractnegotiations/{id}/decline | 
*ContractNegotiationApi* | [**get_agreement_for_negotiation**](mvdp/edc_management_client/docs/ContractNegotiationApi.md#get_agreement_for_negotiation) | **GET** /v2/contractnegotiations/{id}/agreement | 
*ContractNegotiationApi* | [**get_negotiation**](mvdp/edc_management_client/docs/ContractNegotiationApi.md#get_negotiation) | **GET** /v2/contractnegotiations/{id} | 
*ContractNegotiationApi* | [**get_negotiation_state**](mvdp/edc_management_client/docs/ContractNegotiationApi.md#get_negotiation_state) | **GET** /v2/contractnegotiations/{id}/state | 
*ContractNegotiationApi* | [**initiate_contract_negotiation**](mvdp/edc_management_client/docs/ContractNegotiationApi.md#initiate_contract_negotiation) | **POST** /v2/contractnegotiations | 
*ContractNegotiationApi* | [**query_negotiations**](mvdp/edc_management_client/docs/ContractNegotiationApi.md#query_negotiations) | **POST** /v2/contractnegotiations/request | 
*DataPlaneControlAPIApi* | [**get_transfer_state**](mvdp/edc_management_client/docs/DataPlaneControlAPIApi.md#get_transfer_state) | **GET** /transfer/{processId} | 
*DataPlaneControlAPIApi* | [**initiate_transfer**](mvdp/edc_management_client/docs/DataPlaneControlAPIApi.md#initiate_transfer) | **POST** /transfer | 
*DataPlanePublicAPIApi* | [**delete**](mvdp/edc_management_client/docs/DataPlanePublicAPIApi.md#delete) | **DELETE** /{any} | 
*DataPlanePublicAPIApi* | [**get**](mvdp/edc_management_client/docs/DataPlanePublicAPIApi.md#get) | **GET** /{any} | 
*DataPlanePublicAPIApi* | [**patch**](mvdp/edc_management_client/docs/DataPlanePublicAPIApi.md#patch) | **PATCH** /{any} | 
*DataPlanePublicAPIApi* | [**post**](mvdp/edc_management_client/docs/DataPlanePublicAPIApi.md#post) | **POST** /{any} | 
*DataPlanePublicAPIApi* | [**put**](mvdp/edc_management_client/docs/DataPlanePublicAPIApi.md#put) | **PUT** /{any} | 
*DataplaneSelectorApi* | [**add_entry**](mvdp/edc_management_client/docs/DataplaneSelectorApi.md#add_entry) | **POST** /instances | 
*DataplaneSelectorApi* | [**find**](mvdp/edc_management_client/docs/DataplaneSelectorApi.md#find) | **POST** /instances/select | 
*DataplaneSelectorApi* | [**get_all**](mvdp/edc_management_client/docs/DataplaneSelectorApi.md#get_all) | **GET** /instances | 
*HTTPProvisionerWebhookApi* | [**call_deprovision_webhook**](mvdp/edc_management_client/docs/HTTPProvisionerWebhookApi.md#call_deprovision_webhook) | **POST** /callback/{processId}/deprovision | 
*HTTPProvisionerWebhookApi* | [**call_provision_webhook**](mvdp/edc_management_client/docs/HTTPProvisionerWebhookApi.md#call_provision_webhook) | **POST** /callback/{processId}/provision | 
*PolicyDefinitionApi* | [**create_policy_definition**](mvdp/edc_management_client/docs/PolicyDefinitionApi.md#create_policy_definition) | **POST** /v2/policydefinitions | 
*PolicyDefinitionApi* | [**delete_policy_definition**](mvdp/edc_management_client/docs/PolicyDefinitionApi.md#delete_policy_definition) | **DELETE** /v2/policydefinitions/{id} | 
*PolicyDefinitionApi* | [**get_policy_definition**](mvdp/edc_management_client/docs/PolicyDefinitionApi.md#get_policy_definition) | **GET** /v2/policydefinitions/{id} | 
*PolicyDefinitionApi* | [**query_policy_definitions**](mvdp/edc_management_client/docs/PolicyDefinitionApi.md#query_policy_definitions) | **POST** /v2/policydefinitions/request | 
*PolicyDefinitionApi* | [**update_policy_definition**](mvdp/edc_management_client/docs/PolicyDefinitionApi.md#update_policy_definition) | **PUT** /v2/policydefinitions/{id} | 
*TransferProcessApi* | [**deprovision_transfer_process**](mvdp/edc_management_client/docs/TransferProcessApi.md#deprovision_transfer_process) | **POST** /v2/transferprocesses/{id}/deprovision | 
*TransferProcessApi* | [**get_transfer_process**](mvdp/edc_management_client/docs/TransferProcessApi.md#get_transfer_process) | **GET** /v2/transferprocesses/{id} | 
*TransferProcessApi* | [**get_transfer_process_state**](mvdp/edc_management_client/docs/TransferProcessApi.md#get_transfer_process_state) | **GET** /v2/transferprocesses/{id}/state | 
*TransferProcessApi* | [**initiate_transfer_process**](mvdp/edc_management_client/docs/TransferProcessApi.md#initiate_transfer_process) | **POST** /v2/transferprocesses | 
*TransferProcessApi* | [**query_transfer_processes**](mvdp/edc_management_client/docs/TransferProcessApi.md#query_transfer_processes) | **POST** /v2/transferprocesses/request | 
*TransferProcessApi* | [**terminate_transfer_process**](mvdp/edc_management_client/docs/TransferProcessApi.md#terminate_transfer_process) | **POST** /v2/transferprocesses/{id}/terminate | 
*TransferProcessControlApiApi* | [**complete**](mvdp/edc_management_client/docs/TransferProcessControlApiApi.md#complete) | **POST** /transferprocess/{processId}/complete | 
*TransferProcessControlApiApi* | [**fail**](mvdp/edc_management_client/docs/TransferProcessControlApiApi.md#fail) | **POST** /transferprocess/{processId}/fail | 


## Documentation For Models

 - [Action](mvdp/edc_management_client/docs/Action.md)
 - [ApiErrorDetail](mvdp/edc_management_client/docs/ApiErrorDetail.md)
 - [Asset](mvdp/edc_management_client/docs/Asset.md)
 - [AssetEntryNewDto](mvdp/edc_management_client/docs/AssetEntryNewDto.md)
 - [AssetResponseDto](mvdp/edc_management_client/docs/AssetResponseDto.md)
 - [AssetUpdateRequestDto](mvdp/edc_management_client/docs/AssetUpdateRequestDto.md)
 - [CallbackAddress](mvdp/edc_management_client/docs/CallbackAddress.md)
 - [CallbackAddressDto](mvdp/edc_management_client/docs/CallbackAddressDto.md)
 - [Catalog](mvdp/edc_management_client/docs/Catalog.md)
 - [CatalogRequestDto](mvdp/edc_management_client/docs/CatalogRequestDto.md)
 - [Constraint](mvdp/edc_management_client/docs/Constraint.md)
 - [ContractAgreementDto](mvdp/edc_management_client/docs/ContractAgreementDto.md)
 - [ContractDefinitionRequestDto](mvdp/edc_management_client/docs/ContractDefinitionRequestDto.md)
 - [ContractDefinitionResponseDto](mvdp/edc_management_client/docs/ContractDefinitionResponseDto.md)
 - [ContractNegotiationDto](mvdp/edc_management_client/docs/ContractNegotiationDto.md)
 - [ContractOffer](mvdp/edc_management_client/docs/ContractOffer.md)
 - [ContractOfferDescription](mvdp/edc_management_client/docs/ContractOfferDescription.md)
 - [CriterionDto](mvdp/edc_management_client/docs/CriterionDto.md)
 - [DataAddress](mvdp/edc_management_client/docs/DataAddress.md)
 - [DataAddressDto](mvdp/edc_management_client/docs/DataAddressDto.md)
 - [DataFlowRequest](mvdp/edc_management_client/docs/DataFlowRequest.md)
 - [DataPlaneInstance](mvdp/edc_management_client/docs/DataPlaneInstance.md)
 - [DataRequestDto](mvdp/edc_management_client/docs/DataRequestDto.md)
 - [DataService](mvdp/edc_management_client/docs/DataService.md)
 - [Dataset](mvdp/edc_management_client/docs/Dataset.md)
 - [DeprovisionedResource](mvdp/edc_management_client/docs/DeprovisionedResource.md)
 - [Distribution](mvdp/edc_management_client/docs/Distribution.md)
 - [Duty](mvdp/edc_management_client/docs/Duty.md)
 - [Failure](mvdp/edc_management_client/docs/Failure.md)
 - [HealthCheckResult](mvdp/edc_management_client/docs/HealthCheckResult.md)
 - [HealthStatus](mvdp/edc_management_client/docs/HealthStatus.md)
 - [IdResponseDto](mvdp/edc_management_client/docs/IdResponseDto.md)
 - [JsonObject](mvdp/edc_management_client/docs/JsonObject.md)
 - [JsonValue](mvdp/edc_management_client/docs/JsonValue.md)
 - [NegotiationInitiateRequestDto](mvdp/edc_management_client/docs/NegotiationInitiateRequestDto.md)
 - [NegotiationState](mvdp/edc_management_client/docs/NegotiationState.md)
 - [Permission](mvdp/edc_management_client/docs/Permission.md)
 - [Policy](mvdp/edc_management_client/docs/Policy.md)
 - [PolicyDefinitionRequestDto](mvdp/edc_management_client/docs/PolicyDefinitionRequestDto.md)
 - [PolicyDefinitionResponseDto](mvdp/edc_management_client/docs/PolicyDefinitionResponseDto.md)
 - [PolicyDefinitionUpdateDto](mvdp/edc_management_client/docs/PolicyDefinitionUpdateDto.md)
 - [Prohibition](mvdp/edc_management_client/docs/Prohibition.md)
 - [ProvisionerWebhookRequest](mvdp/edc_management_client/docs/ProvisionerWebhookRequest.md)
 - [QuerySpecDto](mvdp/edc_management_client/docs/QuerySpecDto.md)
 - [SelectionRequest](mvdp/edc_management_client/docs/SelectionRequest.md)
 - [TerminateTransferDto](mvdp/edc_management_client/docs/TerminateTransferDto.md)
 - [TransferProcessDto](mvdp/edc_management_client/docs/TransferProcessDto.md)
 - [TransferProcessFailStateDto](mvdp/edc_management_client/docs/TransferProcessFailStateDto.md)
 - [TransferRequestDto](mvdp/edc_management_client/docs/TransferRequestDto.md)
 - [TransferState](mvdp/edc_management_client/docs/TransferState.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




