# ApiErrorDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invalid_value** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.api_error_detail import ApiErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorDetail from a JSON string
api_error_detail_instance = ApiErrorDetail.from_json(json)
# print the JSON string representation of the object
print ApiErrorDetail.to_json()

# convert the object into a dict
api_error_detail_dict = api_error_detail_instance.to_dict()
# create an instance of ApiErrorDetail from a dict
api_error_detail_form_dict = api_error_detail.from_dict(api_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


