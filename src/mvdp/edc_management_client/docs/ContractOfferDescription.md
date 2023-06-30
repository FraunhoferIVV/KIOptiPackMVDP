# ContractOfferDescription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | 
**offer_id** | **str** |  | 
**policy** | [**Policy**](Policy.md) |  | 
**validity** | **int** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.contract_offer_description import ContractOfferDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ContractOfferDescription from a JSON string
contract_offer_description_instance = ContractOfferDescription.from_json(json)
# print the JSON string representation of the object
print ContractOfferDescription.to_json()

# convert the object into a dict
contract_offer_description_dict = contract_offer_description_instance.to_dict()
# create an instance of ContractOfferDescription from a dict
contract_offer_description_form_dict = contract_offer_description.from_dict(contract_offer_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


