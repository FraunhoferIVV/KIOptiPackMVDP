# DataAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | **Dict[str, str]** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.data_address import DataAddress

# TODO update the JSON string below
json = "{}"
# create an instance of DataAddress from a JSON string
data_address_instance = DataAddress.from_json(json)
# print the JSON string representation of the object
print DataAddress.to_json()

# convert the object into a dict
data_address_dict = data_address_instance.to_dict()
# create an instance of DataAddress from a dict
data_address_form_dict = data_address.from_dict(data_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


