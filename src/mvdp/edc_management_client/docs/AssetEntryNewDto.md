# AssetEntryNewDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**Asset**](Asset.md) |  | 
**data_address** | [**DataAddress**](DataAddress.md) |  | 

## Example

```python
from mvdp.edc_management_client.models.asset_entry_new_dto import AssetEntryNewDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetEntryNewDto from a JSON string
asset_entry_new_dto_instance = AssetEntryNewDto.from_json(json)
# print the JSON string representation of the object
print AssetEntryNewDto.to_json()

# convert the object into a dict
asset_entry_new_dto_dict = asset_entry_new_dto_instance.to_dict()
# create an instance of AssetEntryNewDto from a dict
asset_entry_new_dto_form_dict = asset_entry_new_dto.from_dict(asset_entry_new_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


