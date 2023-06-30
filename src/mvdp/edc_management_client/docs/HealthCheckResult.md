# HealthCheckResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] 
**failure** | [**Failure**](Failure.md) |  | [optional] 
**is_healthy** | **bool** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.health_check_result import HealthCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckResult from a JSON string
health_check_result_instance = HealthCheckResult.from_json(json)
# print the JSON string representation of the object
print HealthCheckResult.to_json()

# convert the object into a dict
health_check_result_dict = health_check_result_instance.to_dict()
# create an instance of HealthCheckResult from a dict
health_check_result_form_dict = health_check_result.from_dict(health_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


