# DataAddressDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**properties** | **Dict[str, str]** |  | 

## Example

```python
from mvdp.edc_management_client.models.data_address_dto import DataAddressDto

# TODO update the JSON string below
json = "{}"
# create an instance of DataAddressDto from a JSON string
data_address_dto_instance = DataAddressDto.from_json(json)
# print the JSON string representation of the object
print DataAddressDto.to_json()

# convert the object into a dict
data_address_dto_dict = data_address_dto_instance.to_dict()
# create an instance of DataAddressDto from a dict
data_address_dto_form_dict = data_address_dto.from_dict(data_address_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


