# ContractDefinitionResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**access_policy_id** | **str** |  | [optional] 
**assets_selector** | [**List[CriterionDto]**](CriterionDto.md) |  | [optional] 
**contract_policy_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.contract_definition_response_dto import ContractDefinitionResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDefinitionResponseDto from a JSON string
contract_definition_response_dto_instance = ContractDefinitionResponseDto.from_json(json)
# print the JSON string representation of the object
print ContractDefinitionResponseDto.to_json()

# convert the object into a dict
contract_definition_response_dto_dict = contract_definition_response_dto_instance.to_dict()
# create an instance of ContractDefinitionResponseDto from a dict
contract_definition_response_dto_form_dict = contract_definition_response_dto.from_dict(contract_definition_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


