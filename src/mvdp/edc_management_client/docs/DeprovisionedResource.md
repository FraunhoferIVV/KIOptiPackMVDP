# DeprovisionedResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **bool** |  | [optional] 
**error_message** | **str** |  | [optional] 
**in_process** | **bool** |  | [optional] 
**provisioned_resource_id** | **str** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.deprovisioned_resource import DeprovisionedResource

# TODO update the JSON string below
json = "{}"
# create an instance of DeprovisionedResource from a JSON string
deprovisioned_resource_instance = DeprovisionedResource.from_json(json)
# print the JSON string representation of the object
print DeprovisionedResource.to_json()

# convert the object into a dict
deprovisioned_resource_dict = deprovisioned_resource_instance.to_dict()
# create an instance of DeprovisionedResource from a dict
deprovisioned_resource_form_dict = deprovisioned_resource.from_dict(deprovisioned_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


