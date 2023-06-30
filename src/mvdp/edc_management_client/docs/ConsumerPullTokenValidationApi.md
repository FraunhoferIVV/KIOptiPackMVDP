# mvdp.edc_management_client.ConsumerPullTokenValidationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate**](ConsumerPullTokenValidationApi.md#validate) | **GET** /token | 


# **validate**
> validate(authorization)



Checks that the provided token has been signed by the present entity and asserts its validity. If token is valid, then the data address contained in its claims is decrypted and returned back to the caller.

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
    api_instance = mvdp.edc_management_client.ConsumerPullTokenValidationApi(api_client)
    authorization = 'authorization_example' # str | 

    try:
        api_instance.validate(authorization)
    except Exception as e:
        print("Exception when calling ConsumerPullTokenValidationApi->validate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token is valid |  -  |
**400** | Request was malformed |  -  |
**403** | Token is invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

