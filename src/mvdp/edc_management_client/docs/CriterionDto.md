# CriterionDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**operand_left** | **object** |  | 
**operand_right** | **object** |  | [optional] 
**operator** | **str** |  | 

## Example

```python
from mvdp.edc_management_client.models.criterion_dto import CriterionDto

# TODO update the JSON string below
json = "{}"
# create an instance of CriterionDto from a JSON string
criterion_dto_instance = CriterionDto.from_json(json)
# print the JSON string representation of the object
print CriterionDto.to_json()

# convert the object into a dict
criterion_dto_dict = criterion_dto_instance.to_dict()
# create an instance of CriterionDto from a dict
criterion_dto_form_dict = criterion_dto.from_dict(criterion_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


