# HealthStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_results** | [**List[HealthCheckResult]**](HealthCheckResult.md) |  | [optional] 
**is_system_healthy** | **bool** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.health_status import HealthStatus

# TODO update the JSON string below
json = "{}"
# create an instance of HealthStatus from a JSON string
health_status_instance = HealthStatus.from_json(json)
# print the JSON string representation of the object
print HealthStatus.to_json()

# convert the object into a dict
health_status_dict = health_status_instance.to_dict()
# create an instance of HealthStatus from a dict
health_status_form_dict = health_status.from_dict(health_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


