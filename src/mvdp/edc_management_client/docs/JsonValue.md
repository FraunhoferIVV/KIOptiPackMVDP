# JsonValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_type** | **str** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.json_value import JsonValue

# TODO update the JSON string below
json = "{}"
# create an instance of JsonValue from a JSON string
json_value_instance = JsonValue.from_json(json)
# print the JSON string representation of the object
print JsonValue.to_json()

# convert the object into a dict
json_value_dict = json_value_instance.to_dict()
# create an instance of JsonValue from a dict
json_value_form_dict = json_value.from_dict(json_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


