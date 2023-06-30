# Catalog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_offers** | [**List[ContractOffer]**](ContractOffer.md) |  | [optional] 
**data_services** | [**List[DataService]**](DataService.md) |  | [optional] 
**datasets** | [**List[Dataset]**](Dataset.md) |  | [optional] 
**id** | **str** |  | [optional] 
**properties** | **Dict[str, object]** |  | [optional] 

## Example

```python
from mvdp.edc_management_client.models.catalog import Catalog

# TODO update the JSON string below
json = "{}"
# create an instance of Catalog from a JSON string
catalog_instance = Catalog.from_json(json)
# print the JSON string representation of the object
print Catalog.to_json()

# convert the object into a dict
catalog_dict = catalog_instance.to_dict()
# create an instance of Catalog from a dict
catalog_form_dict = catalog.from_dict(catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


