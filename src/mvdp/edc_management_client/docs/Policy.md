# Policy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**assignee** | **str** |  | [optional] 
**assigner** | **str** |  | [optional] 
**extensible_properties** | **Dict[str, object]** |  | [optional] 
**inherits_from** | **str** |  | [optional] 
**obligations** | [**List[Duty]**](Duty.md) |  | [optional] 
**permissions** | [**List[Permission]**](Permission.md) |  | [optional] 
**prohibitions** | [**List[Prohibition]**](Prohibition.md) |  | [optional] 
**target** | **str** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.policy import Policy

# TODO update the JSON string below
json = "{}"
# create an instance of Policy from a JSON string
policy_instance = Policy.from_json(json)
# print the JSON string representation of the object
print Policy.to_json()

# convert the object into a dict
policy_dict = policy_instance.to_dict()
# create an instance of Policy from a dict
policy_form_dict = policy.from_dict(policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


