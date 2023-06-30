# DataRequestDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | [optional] 
**connector_id** | **str** |  | [optional] 
**contract_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.data_request_dto import DataRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DataRequestDto from a JSON string
data_request_dto_instance = DataRequestDto.from_json(json)
# print the JSON string representation of the object
print DataRequestDto.to_json()

# convert the object into a dict
data_request_dto_dict = data_request_dto_instance.to_dict()
# create an instance of DataRequestDto from a dict
data_request_dto_form_dict = data_request_dto.from_dict(data_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


