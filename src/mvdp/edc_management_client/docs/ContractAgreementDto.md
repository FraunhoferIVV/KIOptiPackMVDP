# ContractAgreementDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**id** | **str** |  | 
**type** | **str** |  | [optional] 
**asset_id** | **str** |  | 
**consumer_id** | **str** |  | 
**contract_signing_date** | **int** |  | [optional] 
**policy** | [**Policy**](Policy.md) |  | 
**provider_id** | **str** |  | 

## Example

```python
from mvdp.edc_management_client.models.contract_agreement_dto import ContractAgreementDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContractAgreementDto from a JSON string
contract_agreement_dto_instance = ContractAgreementDto.from_json(json)
# print the JSON string representation of the object
print ContractAgreementDto.to_json()

# convert the object into a dict
contract_agreement_dto_dict = contract_agreement_dto_instance.to_dict()
# create an instance of ContractAgreementDto from a dict
contract_agreement_dto_form_dict = contract_agreement_dto.from_dict(contract_agreement_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


