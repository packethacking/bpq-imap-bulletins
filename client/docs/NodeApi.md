# swagger_client.NodeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info_get**](NodeApi.md#info_get) | **GET** /info | 
[**links_get**](NodeApi.md#links_get) | **GET** /links | 
[**mheard_port_get**](NodeApi.md#mheard_port_get) | **GET** /mheard/{port} | 
[**nodes_get**](NodeApi.md#nodes_get) | **GET** /nodes | 
[**ports_get**](NodeApi.md#ports_get) | **GET** /ports | 
[**users_get**](NodeApi.md#users_get) | **GET** /users | 

# **info_get**
> GetInfoResponse info_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NodeApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInfoResponse**](GetInfoResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **links_get**
> GetLinksResponse links_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NodeApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.links_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->links_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetLinksResponse**](GetLinksResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mheard_port_get**
> list[BpqApiMheardElement] mheard_port_get(port)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NodeApi(swagger_client.ApiClient(configuration))
port = 56 # int | 

try:
    api_response = api_instance.mheard_port_get(port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->mheard_port_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port** | **int**|  | 

### Return type

[**list[BpqApiMheardElement]**](BpqApiMheardElement.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_get**
> GetNodesResponse nodes_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NodeApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.nodes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->nodes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNodesResponse**](GetNodesResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ports_get**
> GetPortsResponse ports_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NodeApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.ports_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->ports_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPortsResponse**](GetPortsResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> GetUsersResponse users_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NodeApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.users_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->users_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetUsersResponse**](GetUsersResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

