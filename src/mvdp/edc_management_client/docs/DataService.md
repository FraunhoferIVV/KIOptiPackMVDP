# DataService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**terms** | **str** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.data_service import DataService

# TODO update the JSON string below
json = "{}"
# create an instance of DataService from a JSON string
data_service_instance = DataService.from_json(json)
# print the JSON string representation of the object
print DataService.to_json()

# convert the object into a dict
data_service_dict = data_service_instance.to_dict()
# create an instance of DataService from a dict
data_service_form_dict = data_service.from_dict(data_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


