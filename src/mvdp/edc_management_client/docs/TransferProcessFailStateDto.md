# TransferProcessFailStateDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** |  | 

## Example

```python
from mvdp.edc_management_client.models.transfer_process_fail_state_dto import TransferProcessFailStateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransferProcessFailStateDto from a JSON string
transfer_process_fail_state_dto_instance = TransferProcessFailStateDto.from_json(json)
# print the JSON string representation of the object
print TransferProcessFailStateDto.to_json()

# convert the object into a dict
transfer_process_fail_state_dto_dict = transfer_process_fail_state_dto_instance.to_dict()
# create an instance of TransferProcessFailStateDto from a dict
transfer_process_fail_state_dto_form_dict = transfer_process_fail_state_dto.from_dict(transfer_process_fail_state_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


