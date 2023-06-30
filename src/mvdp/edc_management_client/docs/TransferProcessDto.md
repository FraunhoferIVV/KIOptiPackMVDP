# TransferProcessDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**callback_addresses** | [**List[CallbackAddressDto]**](CallbackAddressDto.md) |  | [optional] 
**created_at** | **int** |  | [optional] 
**data_destination** | [**DataAddressDto**](DataAddressDto.md) |  | [optional] 
**data_request** | [**DataRequestDto**](DataRequestDto.md) |  | [optional] 
**error_detail** | **str** |  | [optional] 
**properties** | **Dict[str, str]** |  | [optional] 
**state** | **str** |  | [optional] 
**state_timestamp** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **int** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.transfer_process_dto import TransferProcessDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransferProcessDto from a JSON string
transfer_process_dto_instance = TransferProcessDto.from_json(json)
# print the JSON string representation of the object
print TransferProcessDto.to_json()

# convert the object into a dict
transfer_process_dto_dict = transfer_process_dto_instance.to_dict()
# create an instance of TransferProcessDto from a dict
transfer_process_dto_form_dict = transfer_process_dto.from_dict(transfer_process_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


