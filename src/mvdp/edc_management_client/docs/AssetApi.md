# mvdp.edc_management_client.AssetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset**](AssetApi.md#create_asset) | **POST** /v2/assets | 
[**get_asset**](AssetApi.md#get_asset) | **GET** /v2/assets/{id} | 
[**get_asset_data_address**](AssetApi.md#get_asset_data_address) | **GET** /v2/assets/{id}/dataaddress | 
[**remove_asset**](AssetApi.md#remove_asset) | **DELETE** /v2/assets/{id} | 
[**request_assets**](AssetApi.md#request_assets) | **POST** /v2/assets/request | 
[**update_asset**](AssetApi.md#update_asset) | **PUT** /v2/assets | 
[**update_data_address**](AssetApi.md#update_data_address) | **PUT** /v2/assets/{assetId}/dataaddress | 


# **create_asset**
> IdResponseDto create_asset(asset_entry_new_dto=asset_entry_new_dto)



Creates a new asset together with a data address

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.asset_entry_new_dto import AssetEntryNewDto
from mvdp.edc_management_client.models.id_response_dto import IdResponseDto
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
    api_instance = mvdp.edc_management_client.AssetApi(api_client)
    asset_entry_new_dto = mvdp.edc_management_client.AssetEntryNewDto() # AssetEntryNewDto |  (optional)

    try:
        api_response = api_instance.create_asset(asset_entry_new_dto=asset_entry_new_dto)
        print("The response of AssetApi->create_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->create_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_entry_new_dto** | [**AssetEntryNewDto**](AssetEntryNewDto.md)|  | [optional] 

### Return type

[**IdResponseDto**](IdResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset was created successfully. Returns the asset Id and created timestamp |  -  |
**400** | Request body was malformed |  -  |
**409** | Could not create asset, because an asset with that ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset**
> AssetResponseDto get_asset(id)



Gets an asset with the given ID

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.asset_response_dto import AssetResponseDto
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
    api_instance = mvdp.edc_management_client.AssetApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_asset(id)
        print("The response of AssetApi->get_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AssetResponseDto**](AssetResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The asset |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An asset with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_data_address**
> DataAddressDto get_asset_data_address(id)



Gets a data address of an asset with the given ID

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.data_address_dto import DataAddressDto
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
    api_instance = mvdp.edc_management_client.AssetApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_asset_data_address(id)
        print("The response of AssetApi->get_asset_data_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_asset_data_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DataAddressDto**](DataAddressDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The data address |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An asset with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_asset**
> remove_asset(id)



Removes an asset with the given ID if possible. Deleting an asset is only possible if that asset is not yet referenced by a contract agreement, in which case an error is returned. DANGER ZONE: Note that deleting assets can have unexpected results, especially for contract offers that have been sent out or ongoing or contract negotiations.

### Example

```python
import time
import os
import mvdp.edc_management_client
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
    api_instance = mvdp.edc_management_client.AssetApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.remove_asset(id)
    except Exception as e:
        print("Exception when calling AssetApi->remove_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset was deleted successfully |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An asset with the given ID does not exist |  -  |
**409** | The asset cannot be deleted, because it is referenced by a contract agreement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_assets**
> List[AssetResponseDto] request_assets(query_spec_dto=query_spec_dto)



 all assets according to a particular query

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.asset_response_dto import AssetResponseDto
from mvdp.edc_management_client.models.query_spec_dto import QuerySpecDto
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
    api_instance = mvdp.edc_management_client.AssetApi(api_client)
    query_spec_dto = mvdp.edc_management_client.QuerySpecDto() # QuerySpecDto |  (optional)

    try:
        api_response = api_instance.request_assets(query_spec_dto=query_spec_dto)
        print("The response of AssetApi->request_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->request_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_spec_dto** | [**QuerySpecDto**](QuerySpecDto.md)|  | [optional] 

### Return type

[**List[AssetResponseDto]**](AssetResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Request body was malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset**
> update_asset(asset_update_request_dto=asset_update_request_dto)



Updates an asset with the given ID if it exists. If the asset is not found, no further action is taken. DANGER ZONE: Note that updating assets can have unexpected results, especially for contract offers that have been sent out or are ongoing in contract negotiations.

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.asset_update_request_dto import AssetUpdateRequestDto
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
    api_instance = mvdp.edc_management_client.AssetApi(api_client)
    asset_update_request_dto = mvdp.edc_management_client.AssetUpdateRequestDto() # AssetUpdateRequestDto |  (optional)

    try:
        api_instance.update_asset(asset_update_request_dto=asset_update_request_dto)
    except Exception as e:
        print("Exception when calling AssetApi->update_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_update_request_dto** | [**AssetUpdateRequestDto**](AssetUpdateRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset was updated successfully |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | Asset could not be updated, because it does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_address**
> update_data_address(asset_id, asset_update_request_dto=asset_update_request_dto)



Updates a DataAddress for an asset with the given ID.

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.asset_update_request_dto import AssetUpdateRequestDto
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
    api_instance = mvdp.edc_management_client.AssetApi(api_client)
    asset_id = 'asset_id_example' # str | 
    asset_update_request_dto = mvdp.edc_management_client.AssetUpdateRequestDto() # AssetUpdateRequestDto |  (optional)

    try:
        api_instance.update_data_address(asset_id, asset_update_request_dto=asset_update_request_dto)
    except Exception as e:
        print("Exception when calling AssetApi->update_data_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **asset_update_request_dto** | [**AssetUpdateRequestDto**](AssetUpdateRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset was updated successfully |  -  |
**400** | Request was malformed, e.g. id was null |  -  |
**404** | An asset with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

