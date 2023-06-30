# mvdp.edc_management_client.CatalogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_catalog**](CatalogApi.md#request_catalog) | **POST** /v2/catalog/request | 


# **request_catalog**
> Catalog request_catalog(catalog_request_dto=catalog_request_dto)



### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.catalog import Catalog
from mvdp.edc_management_client.models.catalog_request_dto import CatalogRequestDto
from mvdp.edc_management_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mvdp.edc_management_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mvdp.edc_management_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mvdp.edc_management_client.CatalogApi(api_client)
    catalog_request_dto = mvdp.edc_management_client.CatalogRequestDto() # CatalogRequestDto |  (optional)

    try:
        api_response = api_instance.request_catalog(catalog_request_dto=catalog_request_dto)
        print("The response of CatalogApi->request_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->request_catalog: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_request_dto** | [**CatalogRequestDto**](CatalogRequestDto.md)|  | [optional] 

### Return type

[**Catalog**](Catalog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets contract offers (&#x3D;catalog) of a single connector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

