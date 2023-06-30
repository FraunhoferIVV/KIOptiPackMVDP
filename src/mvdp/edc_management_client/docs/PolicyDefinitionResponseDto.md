# PolicyDefinitionResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**policy** | [**Policy**](Policy.md) |  | 

## Example

```python
from mvdp.edc_management_client.models.policy_definition_response_dto import PolicyDefinitionResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyDefinitionResponseDto from a JSON string
policy_definition_response_dto_instance = PolicyDefinitionResponseDto.from_json(json)
# print the JSON string representation of the object
print PolicyDefinitionResponseDto.to_json()

# convert the object into a dict
policy_definition_response_dto_dict = policy_definition_response_dto_instance.to_dict()
# create an instance of PolicyDefinitionResponseDto from a dict
policy_definition_response_dto_form_dict = policy_definition_response_dto.from_dict(policy_definition_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


