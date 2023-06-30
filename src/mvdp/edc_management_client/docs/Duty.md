# Duty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**Action**](Action.md) |  | [optional] 
**assignee** | **str** |  | [optional] 
**assigner** | **str** |  | [optional] 
**consequence** | [**Duty**](Duty.md) |  | [optional] 
**constraints** | [**List[Constraint]**](Constraint.md) |  | [optional] 
**parent_permission** | [**Permission**](Permission.md) |  | [optional] 
**target** | **str** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.duty import Duty

# TODO update the JSON string below
json = "{}"
# create an instance of Duty from a JSON string
duty_instance = Duty.from_json(json)
# print the JSON string representation of the object
print Duty.to_json()

# convert the object into a dict
duty_dict = duty_instance.to_dict()
# create an instance of Duty from a dict
duty_form_dict = duty.from_dict(duty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


