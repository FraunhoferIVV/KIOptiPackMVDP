# DataFlowRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_address** | **str** |  | [optional] 
**destination_data_address** | [**DataAddress**](DataAddress.md) |  | [optional] 
**id** | **str** |  | [optional] 
**process_id** | **str** |  | [optional] 
**properties** | **Dict[str, str]** |  | [optional] 
**source_data_address** | [**DataAddress**](DataAddress.md) |  | [optional] 
**trace_context** | **Dict[str, str]** |  | [optional] 
**trackable** | **bool** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.data_flow_request import DataFlowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataFlowRequest from a JSON string
data_flow_request_instance = DataFlowRequest.from_json(json)
# print the JSON string representation of the object
print DataFlowRequest.to_json()

# convert the object into a dict
data_flow_request_dict = data_flow_request_instance.to_dict()
# create an instance of DataFlowRequest from a dict
data_flow_request_form_dict = data_flow_request.from_dict(data_flow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


