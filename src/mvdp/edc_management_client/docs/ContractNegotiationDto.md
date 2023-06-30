# ContractNegotiationDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**callback_addresses** | [**List[CallbackAddress]**](CallbackAddress.md) |  | [optional] 
**contract_agreement_id** | **str** |  | [optional] 
**counter_party_address** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**error_detail** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **int** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.contract_negotiation_dto import ContractNegotiationDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContractNegotiationDto from a JSON string
contract_negotiation_dto_instance = ContractNegotiationDto.from_json(json)
# print the JSON string representation of the object
print ContractNegotiationDto.to_json()

# convert the object into a dict
contract_negotiation_dto_dict = contract_negotiation_dto_instance.to_dict()
# create an instance of ContractNegotiationDto from a dict
contract_negotiation_dto_form_dict = contract_negotiation_dto.from_dict(contract_negotiation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


