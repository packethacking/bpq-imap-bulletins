# swagger_client.MailApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mail_bulletins_get**](MailApi.md#mail_bulletins_get) | **GET** /mail/bulletins | Get a list of all bulletins
[**mail_get**](MailApi.md#mail_get) | **GET** /mail | Get a list of all mail items of all types
[**mail_id_get**](MailApi.md#mail_id_get) | **GET** /mail/{id} | Retrieve mail item by id
[**mail_inbox_get**](MailApi.md#mail_inbox_get) | **GET** /mail/inbox | Inbox listing, i.e. BPQ \&quot;My Rxed\&quot; mail
[**mail_personal_get**](MailApi.md#mail_personal_get) | **GET** /mail/personal | Get a list of all personal mail, not just mine
[**mail_sent_get**](MailApi.md#mail_sent_get) | **GET** /mail/sent | Sent items, i.e. BPQ \&quot;My Sent\&quot; mail

# **mail_bulletins_get**
> list[MailListEntity] mail_bulletins_get()

Get a list of all bulletins

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
api_instance = swagger_client.MailApi(swagger_client.ApiClient(configuration))

try:
    # Get a list of all bulletins
    api_response = api_instance.mail_bulletins_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailApi->mail_bulletins_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MailListEntity]**](MailListEntity.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_get**
> list[MailListEntity] mail_get()

Get a list of all mail items of all types

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
api_instance = swagger_client.MailApi(swagger_client.ApiClient(configuration))

try:
    # Get a list of all mail items of all types
    api_response = api_instance.mail_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailApi->mail_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MailListEntity]**](MailListEntity.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_id_get**
> list[MailEntity] mail_id_get(id)

Retrieve mail item by id

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
api_instance = swagger_client.MailApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Retrieve mail item by id
    api_response = api_instance.mail_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailApi->mail_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**list[MailEntity]**](MailEntity.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_inbox_get**
> list[MailListEntity] mail_inbox_get()

Inbox listing, i.e. BPQ \"My Rxed\" mail

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
api_instance = swagger_client.MailApi(swagger_client.ApiClient(configuration))

try:
    # Inbox listing, i.e. BPQ \"My Rxed\" mail
    api_response = api_instance.mail_inbox_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailApi->mail_inbox_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MailListEntity]**](MailListEntity.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_personal_get**
> list[MailListEntity] mail_personal_get()

Get a list of all personal mail, not just mine

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
api_instance = swagger_client.MailApi(swagger_client.ApiClient(configuration))

try:
    # Get a list of all personal mail, not just mine
    api_response = api_instance.mail_personal_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailApi->mail_personal_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MailListEntity]**](MailListEntity.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_sent_get**
> list[MailListEntity] mail_sent_get()

Sent items, i.e. BPQ \"My Sent\" mail

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
api_instance = swagger_client.MailApi(swagger_client.ApiClient(configuration))

try:
    # Sent items, i.e. BPQ \"My Sent\" mail
    api_response = api_instance.mail_sent_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailApi->mail_sent_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MailListEntity]**](MailListEntity.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

