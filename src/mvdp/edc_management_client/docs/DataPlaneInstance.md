# DataPlaneInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_dest_types** | **List[str]** |  | [optional] 
**allowed_source_types** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**last_active** | **int** |  | [optional] 
**properties** | **Dict[str, object]** |  | [optional] 
**turn_count** | **int** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.data_plane_instance import DataPlaneInstance

# TODO update the JSON string below
json = "{}"
# create an instance of DataPlaneInstance from a JSON string
data_plane_instance_instance = DataPlaneInstance.from_json(json)
# print the JSON string representation of the object
print DataPlaneInstance.to_json()

# convert the object into a dict
data_plane_instance_dict = data_plane_instance_instance.to_dict()
# create an instance of DataPlaneInstance from a dict
data_plane_instance_form_dict = data_plane_instance.from_dict(data_plane_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


