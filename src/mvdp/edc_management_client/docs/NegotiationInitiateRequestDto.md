# NegotiationInitiateRequestDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**callback_addresses** | [**List[CallbackAddressDto]**](CallbackAddressDto.md) |  | [optional] 
**connector_address** | **str** |  | 
**connector_id** | **str** |  | 
**consumer_id** | **str** |  | [optional] 
**offer** | [**ContractOfferDescription**](ContractOfferDescription.md) |  | 
**protocol** | **str** |  | 
**provider_id** | **str** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.negotiation_initiate_request_dto import NegotiationInitiateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of NegotiationInitiateRequestDto from a JSON string
negotiation_initiate_request_dto_instance = NegotiationInitiateRequestDto.from_json(json)
# print the JSON string representation of the object
print NegotiationInitiateRequestDto.to_json()

# convert the object into a dict
negotiation_initiate_request_dto_dict = negotiation_initiate_request_dto_instance.to_dict()
# create an instance of NegotiationInitiateRequestDto from a dict
negotiation_initiate_request_dto_form_dict = negotiation_initiate_request_dto.from_dict(negotiation_initiate_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


