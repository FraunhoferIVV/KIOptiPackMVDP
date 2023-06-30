# PolicyDefinitionRequestDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**policy** | [**Policy**](Policy.md) |  | 

## Example

```python
from mvdp.edc_management_client.models.policy_definition_request_dto import PolicyDefinitionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyDefinitionRequestDto from a JSON string
policy_definition_request_dto_instance = PolicyDefinitionRequestDto.from_json(json)
# print the JSON string representation of the object
print PolicyDefinitionRequestDto.to_json()

# convert the object into a dict
policy_definition_request_dto_dict = policy_definition_request_dto_instance.to_dict()
# create an instance of PolicyDefinitionRequestDto from a dict
policy_definition_request_dto_form_dict = policy_definition_request_dto.from_dict(policy_definition_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


