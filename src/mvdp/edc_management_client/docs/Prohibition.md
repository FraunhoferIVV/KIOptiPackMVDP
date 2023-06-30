# Prohibition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**Action**](Action.md) |  | [optional] 
**assignee** | **str** |  | [optional] 
**assigner** | **str** |  | [optional] 
**constraints** | [**List[Constraint]**](Constraint.md) |  | [optional] 
**target** | **str** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.prohibition import Prohibition

# TODO update the JSON string below
json = "{}"
# create an instance of Prohibition from a JSON string
prohibition_instance = Prohibition.from_json(json)
# print the JSON string representation of the object
print Prohibition.to_json()

# convert the object into a dict
prohibition_dict = prohibition_instance.to_dict()
# create an instance of Prohibition from a dict
prohibition_form_dict = prohibition.from_dict(prohibition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


