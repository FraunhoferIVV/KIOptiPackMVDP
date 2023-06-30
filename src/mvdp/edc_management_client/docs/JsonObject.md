# JsonObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**empty** | **bool** |  | [optional] 
**value_type** | **str** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.json_object import JsonObject

# TODO update the JSON string below
json = "{}"
# create an instance of JsonObject from a JSON string
json_object_instance = JsonObject.from_json(json)
# print the JSON string representation of the object
print JsonObject.to_json()

# convert the object into a dict
json_object_dict = json_object_instance.to_dict()
# create an instance of JsonObject from a dict
json_object_form_dict = json_object.from_dict(json_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


