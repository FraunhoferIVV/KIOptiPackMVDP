# QuerySpecDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**filter_expression** | [**List[CriterionDto]**](CriterionDto.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**sort_field** | **str** |  | [optional] 
**sort_order** | **str** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.query_spec_dto import QuerySpecDto

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySpecDto from a JSON string
query_spec_dto_instance = QuerySpecDto.from_json(json)
# print the JSON string representation of the object
print QuerySpecDto.to_json()

# convert the object into a dict
query_spec_dto_dict = query_spec_dto_instance.to_dict()
# create an instance of QuerySpecDto from a dict
query_spec_dto_form_dict = query_spec_dto.from_dict(query_spec_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


