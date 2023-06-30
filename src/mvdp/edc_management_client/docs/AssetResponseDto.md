# AssetResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**private_properties** | **Dict[str, object]** |  | [optional] 
**properties** | **Dict[str, object]** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.asset_response_dto import AssetResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetResponseDto from a JSON string
asset_response_dto_instance = AssetResponseDto.from_json(json)
# print the JSON string representation of the object
print AssetResponseDto.to_json()

# convert the object into a dict
asset_response_dto_dict = asset_response_dto_instance.to_dict()
# create an instance of AssetResponseDto from a dict
asset_response_dto_form_dict = asset_response_dto.from_dict(asset_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


