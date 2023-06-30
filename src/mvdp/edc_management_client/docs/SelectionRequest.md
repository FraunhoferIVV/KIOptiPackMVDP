# SelectionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | [**DataAddress**](DataAddress.md) |  | [optional] 
**source** | [**DataAddress**](DataAddress.md) |  | [optional] 
**strategy** | **str** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.selection_request import SelectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SelectionRequest from a JSON string
selection_request_instance = SelectionRequest.from_json(json)
# print the JSON string representation of the object
print SelectionRequest.to_json()

# convert the object into a dict
selection_request_dict = selection_request_instance.to_dict()
# create an instance of SelectionRequest from a dict
selection_request_form_dict = selection_request.from_dict(selection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


