# IdResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.id_response_dto import IdResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of IdResponseDto from a JSON string
id_response_dto_instance = IdResponseDto.from_json(json)
# print the JSON string representation of the object
print IdResponseDto.to_json()

# convert the object into a dict
id_response_dto_dict = id_response_dto_instance.to_dict()
# create an instance of IdResponseDto from a dict
id_response_dto_form_dict = id_response_dto.from_dict(id_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


