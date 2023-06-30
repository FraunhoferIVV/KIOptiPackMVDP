# CatalogRequestDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**provider_url** | **str** |  | 
**query_spec** | [**QuerySpecDto**](QuerySpecDto.md) |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.catalog_request_dto import CatalogRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogRequestDto from a JSON string
catalog_request_dto_instance = CatalogRequestDto.from_json(json)
# print the JSON string representation of the object
print CatalogRequestDto.to_json()

# convert the object into a dict
catalog_request_dto_dict = catalog_request_dto_instance.to_dict()
# create an instance of CatalogRequestDto from a dict
catalog_request_dto_form_dict = catalog_request_dto.from_dict(catalog_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


