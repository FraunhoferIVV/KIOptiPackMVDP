# ProvisionerWebhookRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_jwt** | **str** |  | 
**asset_id** | **str** |  | 
**content_data_address** | [**DataAddress**](DataAddress.md) |  | 
**has_token** | **bool** |  | [optional] 
**resource_definition_id** | **str** |  | 
**resource_name** | **str** |  | 

## Example

```python
from mvdp.edc_management_client.models.provisioner_webhook_request import ProvisionerWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionerWebhookRequest from a JSON string
provisioner_webhook_request_instance = ProvisionerWebhookRequest.from_json(json)
# print the JSON string representation of the object
print ProvisionerWebhookRequest.to_json()

# convert the object into a dict
provisioner_webhook_request_dict = provisioner_webhook_request_instance.to_dict()
# create an instance of ProvisionerWebhookRequest from a dict
provisioner_webhook_request_form_dict = provisioner_webhook_request.from_dict(provisioner_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


