# swagger_client.MailManagementApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mail_management_options_get**](MailManagementApi.md#mail_management_options_get) | **GET** /MailManagement/options | 
[**mail_management_partners_get**](MailManagementApi.md#mail_management_partners_get) | **GET** /MailManagement/partners | 

# **mail_management_options_get**
> ForwardingOptions mail_management_options_get()



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
api_instance = swagger_client.MailManagementApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.mail_management_options_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailManagementApi->mail_management_options_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ForwardingOptions**](ForwardingOptions.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_management_partners_get**
> dict(str, ForwardingStation) mail_management_partners_get()



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
api_instance = swagger_client.MailManagementApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.mail_management_partners_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailManagementApi->mail_management_partners_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, ForwardingStation)**](ForwardingStation.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

