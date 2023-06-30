# mvdp.edc_management_client.ApplicationObservabilityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_health**](ApplicationObservabilityApi.md#check_health) | **GET** /check/health | 
[**get_liveness**](ApplicationObservabilityApi.md#get_liveness) | **GET** /check/liveness | 
[**get_readiness**](ApplicationObservabilityApi.md#get_readiness) | **GET** /check/readiness | 
[**get_startup**](ApplicationObservabilityApi.md#get_startup) | **GET** /check/startup | 


# **check_health**
> HealthStatus check_health()



Performs a liveness probe to determine whether the runtime is working properly.

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.health_status import HealthStatus
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
    api_instance = mvdp.edc_management_client.ApplicationObservabilityApi(api_client)

    try:
        api_response = api_instance.check_health()
        print("The response of ApplicationObservabilityApi->check_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationObservabilityApi->check_health: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthStatus**](HealthStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_liveness**
> List[HealthStatus] get_liveness()



Performs a liveness probe to determine whether the runtime is working properly.

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.health_status import HealthStatus
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
    api_instance = mvdp.edc_management_client.ApplicationObservabilityApi(api_client)

    try:
        api_response = api_instance.get_liveness()
        print("The response of ApplicationObservabilityApi->get_liveness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationObservabilityApi->get_liveness: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[HealthStatus]**](HealthStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_readiness**
> List[HealthStatus] get_readiness()



Performs a readiness probe to determine whether the runtime is able to accept requests.

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.health_status import HealthStatus
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
    api_instance = mvdp.edc_management_client.ApplicationObservabilityApi(api_client)

    try:
        api_response = api_instance.get_readiness()
        print("The response of ApplicationObservabilityApi->get_readiness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationObservabilityApi->get_readiness: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[HealthStatus]**](HealthStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_startup**
> List[HealthStatus] get_startup()



Performs a startup probe to determine whether the runtime has completed startup.

### Example

```python
import time
import os
import mvdp.edc_management_client
from mvdp.edc_management_client.models.health_status import HealthStatus
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
    api_instance = mvdp.edc_management_client.ApplicationObservabilityApi(api_client)

    try:
        api_response = api_instance.get_startup()
        print("The response of ApplicationObservabilityApi->get_startup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationObservabilityApi->get_startup: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[HealthStatus]**](HealthStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

