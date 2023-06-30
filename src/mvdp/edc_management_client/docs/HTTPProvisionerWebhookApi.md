# mvdp.edc_management_client.HTTPProvisionerWebhookApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_deprovision_webhook**](HTTPProvisionerWebhookApi.md#call_deprovision_webhook) | **POST** /callback/{processId}/deprovision | 
[**call_provision_webhook**](HTTPProvisionerWebhookApi.md#call_provision_webhook) | **POST** /callback/{processId}/provision | 


# **call_deprovision_webhook**
> call_deprovision_webhook(process_id, deprovisioned_resource=deprovisioned_resource)



### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.deprovisioned_resource import DeprovisionedResource
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
    api_instance = mvdp.edc_management_client.HTTPProvisionerWebhookApi(api_client)
    process_id = 'process_id_example' # str | 
    deprovisioned_resource = mvdp.edc_management_client.DeprovisionedResource() # DeprovisionedResource |  (optional)

    try:
        api_instance.call_deprovision_webhook(process_id, deprovisioned_resource=deprovisioned_resource)
    except Exception as e:
        print("Exception when calling HTTPProvisionerWebhookApi->call_deprovision_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**|  | 
 **deprovisioned_resource** | [**DeprovisionedResource**](DeprovisionedResource.md)|  | [optional] 

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
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_provision_webhook**
> call_provision_webhook(process_id, provisioner_webhook_request=provisioner_webhook_request)



### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.provisioner_webhook_request import ProvisionerWebhookRequest
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
    api_instance = mvdp.edc_management_client.HTTPProvisionerWebhookApi(api_client)
    process_id = 'process_id_example' # str | 
    provisioner_webhook_request = mvdp.edc_management_client.ProvisionerWebhookRequest() # ProvisionerWebhookRequest |  (optional)

    try:
        api_instance.call_provision_webhook(process_id, provisioner_webhook_request=provisioner_webhook_request)
    except Exception as e:
        print("Exception when calling HTTPProvisionerWebhookApi->call_provision_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**|  | 
 **provisioner_webhook_request** | [**ProvisionerWebhookRequest**](ProvisionerWebhookRequest.md)|  | [optional] 

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
**200** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

