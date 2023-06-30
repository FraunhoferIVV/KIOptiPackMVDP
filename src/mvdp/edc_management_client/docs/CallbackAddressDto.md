# CallbackAddressDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**auth_code_id** | **str** |  | [optional] 
**auth_key** | **str** |  | [optional] 
**events** | **List[str]** |  | 
**transactional** | **bool** |  | [optional] 
**uri** | **str** |  | 

## Example

```python
from mvdp.edc_management_client.models.callback_address_dto import CallbackAddressDto

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackAddressDto from a JSON string
callback_address_dto_instance = CallbackAddressDto.from_json(json)
# print the JSON string representation of the object
print CallbackAddressDto.to_json()

# convert the object into a dict
callback_address_dto_dict = callback_address_dto_instance.to_dict()
# create an instance of CallbackAddressDto from a dict
callback_address_dto_form_dict = callback_address_dto.from_dict(callback_address_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


