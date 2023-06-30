# AssetUpdateRequestDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**private_properties** | **Dict[str, object]** |  | [optional] 
**properties** | **Dict[str, object]** |  | 

## Example

```python
from mvdp.edc_management_client.models.asset_update_request_dto import AssetUpdateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetUpdateRequestDto from a JSON string
asset_update_request_dto_instance = AssetUpdateRequestDto.from_json(json)
# print the JSON string representation of the object
print AssetUpdateRequestDto.to_json()

# convert the object into a dict
asset_update_request_dto_dict = asset_update_request_dto_instance.to_dict()
# create an instance of AssetUpdateRequestDto from a dict
asset_update_request_dto_form_dict = asset_update_request_dto.from_dict(asset_update_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


