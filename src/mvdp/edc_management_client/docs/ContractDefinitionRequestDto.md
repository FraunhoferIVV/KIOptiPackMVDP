# ContractDefinitionRequestDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**access_policy_id** | **str** |  | 
**assets_selector** | [**List[CriterionDto]**](CriterionDto.md) |  | 
**contract_policy_id** | **str** |  | 

## Example

```python
from mvdp.edc_management_client.models.contract_definition_request_dto import ContractDefinitionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDefinitionRequestDto from a JSON string
contract_definition_request_dto_instance = ContractDefinitionRequestDto.from_json(json)
# print the JSON string representation of the object
print ContractDefinitionRequestDto.to_json()

# convert the object into a dict
contract_definition_request_dto_dict = contract_definition_request_dto_instance.to_dict()
# create an instance of ContractDefinitionRequestDto from a dict
contract_definition_request_dto_form_dict = contract_definition_request_dto.from_dict(contract_definition_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


