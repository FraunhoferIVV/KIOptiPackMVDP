# TerminateTransferDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 

## Example

```python
from mvdp.edc_management_client.models.terminate_transfer_dto import TerminateTransferDto

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateTransferDto from a JSON string
terminate_transfer_dto_instance = TerminateTransferDto.from_json(json)
# print the JSON string representation of the object
print TerminateTransferDto.to_json()

# convert the object into a dict
terminate_transfer_dto_dict = terminate_transfer_dto_instance.to_dict()
# create an instance of TerminateTransferDto from a dict
terminate_transfer_dto_form_dict = terminate_transfer_dto.from_dict(terminate_transfer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


