# TransferRequestDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | 
**callback_addresses** | [**List[CallbackAddressDto]**](CallbackAddressDto.md) |  | [optional] 
**connector_address** | **str** |  | 
**connector_id** | **str** |  | 
**contract_id** | **str** |  | 
**data_destination** | [**DataAddress**](DataAddress.md) |  | 
**id** | **str** |  | [optional] 
**managed_resources** | **bool** |  | [optional] 
**private_properties** | **Dict[str, str]** |  | [optional] 
**properties** | **Dict[str, str]** |  | [optional] 
**protocol** | **str** |  | 

## Example

```python
from mvdp.edc_management_client.models.transfer_request_dto import TransferRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransferRequestDto from a JSON string
transfer_request_dto_instance = TransferRequestDto.from_json(json)
# print the JSON string representation of the object
print TransferRequestDto.to_json()

# convert the object into a dict
transfer_request_dto_dict = transfer_request_dto_instance.to_dict()
# create an instance of TransferRequestDto from a dict
transfer_request_dto_form_dict = transfer_request_dto.from_dict(transfer_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


