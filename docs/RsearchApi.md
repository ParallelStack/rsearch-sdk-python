# rsearch_client.RsearchApi

All URIs are relative to *https://api.parallelstack.com/api/rsearch/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document**](RsearchApi.md#add_document) | **POST** /indexes/{index_name}/document_types/{doc_type_name}/documents/{doc_id} | 
[**add_document_type**](RsearchApi.md#add_document_type) | **POST** /indexes/{index_name}/document_types/{doc_type_name} | 
[**add_index**](RsearchApi.md#add_index) | **POST** /indexes/{index_name} | 
[**delete_document**](RsearchApi.md#delete_document) | **DELETE** /indexes/{index_name}/document_types/{doc_type_name}/documents/{doc_id} | 
[**delete_index**](RsearchApi.md#delete_index) | **DELETE** /indexes/{index_name} | 
[**get_advanced_doc_type_suggest_results**](RsearchApi.md#get_advanced_doc_type_suggest_results) | **POST** /indexes/{index_name}/document_types/{doc_type_name}/suggest | 
[**get_advanced_index_suggest_results**](RsearchApi.md#get_advanced_index_suggest_results) | **POST** /indexes/{index_name}/suggest | 
[**get_advanced_search_results**](RsearchApi.md#get_advanced_search_results) | **POST** /indexes/{index_name}/document_types/{doc_type_name}/search | 
[**get_all_document_types**](RsearchApi.md#get_all_document_types) | **GET** /indexes/{index_name}/document_types | 
[**get_all_indexes**](RsearchApi.md#get_all_indexes) | **GET** /indexes | 
[**get_basic_search_results**](RsearchApi.md#get_basic_search_results) | **GET** /indexes/{index_name}/search | 
[**get_doc_type_suggest_results**](RsearchApi.md#get_doc_type_suggest_results) | **GET** /indexes/{index_name}/document_types/{doc_type_name}/suggest | 
[**get_document**](RsearchApi.md#get_document) | **GET** /indexes/{index_name}/document_types/{doc_type_name}/documents/{doc_id} | 
[**get_document_type**](RsearchApi.md#get_document_type) | **GET** /indexes/{index_name}/document_types/{doc_type_name} | 
[**get_index**](RsearchApi.md#get_index) | **GET** /indexes/{index_name} | 


# **add_document**
> CreateDocumentSuccess add_document(index_name, doc_type_name, doc_id, document_details)



Creates `doc_id` in `doc_type_name` for `index_name`

### Example
```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = rsearch_client.Configuration()
configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: writeAppID
configuration = rsearch_client.Configuration()
configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'

# create an instance of the API class
api_instance = rsearch_client.RsearchApi(rsearch_client.ApiClient(configuration))
index_name = 'index_name_example' # str | Name of the index
doc_type_name = 'doc_type_name_example' # str | Name of the document_type
doc_id = 'doc_id_example' # str | Document ID
document_details = rsearch_client.Document() # Document | Details of the document

try:
    api_response = api_instance.add_document(index_name, doc_type_name, doc_id, document_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->add_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Name of the index | 
 **doc_type_name** | **str**| Name of the document_type | 
 **doc_id** | **str**| Document ID | 
 **document_details** | [**Document**](Document.md)| Details of the document | 

### Return type

[**CreateDocumentSuccess**](CreateDocumentSuccess.md)

### Authorization

[authToken](../README.md#authToken), [writeAppID](../README.md#writeAppID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_document_type**
> CreateDocTypeSuccess add_document_type(index_name, doc_type_name, doc_type_details)



Creates specific `document_type` in `index_name` with specified parameters. You should define the parameters correctly as per the getting started guide, else getting the right structure might be an issue.

### Example
```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = rsearch_client.Configuration()
configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: writeAppID
configuration = rsearch_client.Configuration()
configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'

# create an instance of the API class
api_instance = rsearch_client.RsearchApi(rsearch_client.ApiClient(configuration))
index_name = 'index_name_example' # str | Name of the index
doc_type_name = 'doc_type_name_example' # str | Name of the document_type
doc_type_details = rsearch_client.DocumentType() # DocumentType | Details of the document_type

try:
    api_response = api_instance.add_document_type(index_name, doc_type_name, doc_type_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->add_document_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Name of the index | 
 **doc_type_name** | **str**| Name of the document_type | 
 **doc_type_details** | [**DocumentType**](DocumentType.md)| Details of the document_type | 

### Return type

[**CreateDocTypeSuccess**](CreateDocTypeSuccess.md)

### Authorization

[authToken](../README.md#authToken), [writeAppID](../README.md#writeAppID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_index**
> CreateIndexSuccess add_index(index_name)



Creates `a new index`.

### Example
```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = rsearch_client.Configuration()
configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: writeAppID
configuration = rsearch_client.Configuration()
configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'

# create an instance of the API class
api_instance = rsearch_client.RsearchApi(rsearch_client.ApiClient(configuration))
index_name = 'index_name_example' # str | Name of the index

try:
    api_response = api_instance.add_index(index_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->add_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Name of the index | 

### Return type

[**CreateIndexSuccess**](CreateIndexSuccess.md)

### Authorization

[authToken](../README.md#authToken), [writeAppID](../README.md#writeAppID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> DeleteDocumentSuccess delete_document(index_name, doc_type_name, doc_id)



Deletes `doc_id` in `doc_type_name` for `index_name`

### Example
```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = rsearch_client.Configuration()
configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: writeAppID
configuration = rsearch_client.Configuration()
configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'

# create an instance of the API class
api_instance = rsearch_client.RsearchApi(rsearch_client.ApiClient(configuration))
index_name = 'index_name_example' # str | Name of the index
doc_type_name = 'doc_type_name_example' # str | Name of the document_type
doc_id = 'doc_id_example' # str | Document ID

try:
    api_response = api_instance.delete_document(index_name, doc_type_name, doc_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->delete_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Name of the index | 
 **doc_type_name** | **str**| Name of the document_type | 
 **doc_id** | **str**| Document ID | 

### Return type

[**DeleteDocumentSuccess**](DeleteDocumentSuccess.md)

### Authorization

[authToken](../README.md#authToken), [writeAppID](../README.md#writeAppID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_index**
> DeleteIndexSuccess delete_index(index_name)



Deletes `an index` {index_name}

### Example
```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = rsearch_client.Configuration()
configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: writeAppID
configuration = rsearch_client.Configuration()
configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'

# create an instance of the API class
api_instance = rsearch_client.RsearchApi(rsearch_client.ApiClient(configuration))
index_name = 'index_name_example' # str | Name of the index

try:
    api_response = api_instance.delete_index(index_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->delete_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Name of the index | 

### Return type

[**DeleteIndexSuccess**](DeleteIndexSuccess.md)

### Authorization

[authToken](../README.md#authToken), [writeAppID](../README.md#writeAppID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advanced_doc_type_suggest_results**
> SuggestSuccess get_advanced_doc_type_suggest_results(index_name, doc_type_name, suggest)



Gets Suggestions from `doc_type_name` in `index_name` limited by the body params. Please ensure you refer the getting started guides, to get the format of the query right.

### Example
```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = rsearch_client.Configuration()
configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: readAppID
configuration = rsearch_client.Configuration()
configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'

# create an instance of the API class
api_instance = rsearch_client.RsearchApi(rsearch_client.ApiClient(configuration))
index_name = 'index_name_example' # str | Name of the index
doc_type_name = 'doc_type_name_example' # str | Name of the Document_type
suggest = rsearch_client.SuggestQuery() # SuggestQuery | Details of the search query

try:
    api_response = api_instance.get_advanced_doc_type_suggest_results(index_name, doc_type_name, suggest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->get_advanced_doc_type_suggest_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Name of the index | 
 **doc_type_name** | **str**| Name of the Document_type | 
 **suggest** | [**SuggestQuery**](SuggestQuery.md)| Details of the search query | 

### Return type

[**SuggestSuccess**](SuggestSuccess.md)

### Authorization

[authToken](../README.md#authToken), [readAppID](../README.md#readAppID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advanced_index_suggest_results**
> SuggestSuccess get_advanced_index_suggest_results(index_name, search)



Gets Suggestions in `index_name` limited by the request body fields

### Example
```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = rsearch_client.Configuration()
configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: readAppID
configuration = rsearch_client.Configuration()
configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'

# create an instance of the API class
api_instance = rsearch_client.RsearchApi(rsearch_client.ApiClient(configuration))
index_name = 'index_name_example' # str | Name of the index
search = rsearch_client.SuggestQuery() # SuggestQuery | Details of the search query

try:
    api_response = api_instance.get_advanced_index_suggest_results(index_name, search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->get_advanced_index_suggest_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Name of the index | 
 **search** | [**SuggestQuery**](SuggestQuery.md)| Details of the search query | 

### Return type

[**SuggestSuccess**](SuggestSuccess.md)

### Authorization

[authToken](../README.md#authToken), [readAppID](../README.md#readAppID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advanced_search_results**
> SearchSuccess get_advanced_search_results(index_name, doc_type_name, search)



Advanced Search which gets all documents in `index_name` for provided search criteria. Please ensure you refer the getting started guides, to get the format of the query right.

### Example
```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = rsearch_client.Configuration()
configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: readAppID
configuration = rsearch_client.Configuration()
configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'

# create an instance of the API class
api_instance = rsearch_client.RsearchApi(rsearch_client.ApiClient(configuration))
index_name = 'index_name_example' # str | Name of the index
doc_type_name = 'doc_type_name_example' # str | Name of the Document_type
search = rsearch_client.SearchQuery() # SearchQuery | Details of the search query

try:
    api_response = api_instance.get_advanced_search_results(index_name, doc_type_name, search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->get_advanced_search_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Name of the index | 
 **doc_type_name** | **str**| Name of the Document_type | 
 **search** | [**SearchQuery**](SearchQuery.md)| Details of the search query | 

### Return type

[**SearchSuccess**](SearchSuccess.md)

### Authorization

[authToken](../README.md#authToken), [readAppID](../README.md#readAppID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_document_types**
> GetDocTypesSuccess get_all_document_types(index_name)



Gets `All document_types` present in `index_name`

### Example
```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = rsearch_client.Configuration()
configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: readAppID
configuration = rsearch_client.Configuration()
configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'

# create an instance of the API class
api_instance = rsearch_client.RsearchApi(rsearch_client.ApiClient(configuration))
index_name = 'index_name_example' # str | Name of the index

try:
    api_response = api_instance.get_all_document_types(index_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->get_all_document_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Name of the index | 

### Return type

[**GetDocTypesSuccess**](GetDocTypesSuccess.md)

### Authorization

[authToken](../README.md#authToken), [readAppID](../README.md#readAppID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_indexes**
> GetIndexesSuccess get_all_indexes()



Fetches `All indexes` that the user has. Not recommended to be used in production code, as there isn't that big a Use case for listing all indexes!

### Example
```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = rsearch_client.Configuration()
configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: readAppID
configuration = rsearch_client.Configuration()
configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'

# create an instance of the API class
api_instance = rsearch_client.RsearchApi(rsearch_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_indexes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->get_all_indexes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetIndexesSuccess**](GetIndexesSuccess.md)

### Authorization

[authToken](../README.md#authToken), [readAppID](../README.md#readAppID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_basic_search_results**
> SearchSuccess get_basic_search_results(index_name, q)



Basic Search which gets all documents in `index_name` for provided search criteria

### Example
```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = rsearch_client.Configuration()
configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: readAppID
configuration = rsearch_client.Configuration()
configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'

# create an instance of the API class
api_instance = rsearch_client.RsearchApi(rsearch_client.ApiClient(configuration))
index_name = 'index_name_example' # str | Name of the index
q = 'q_example' # str | Search Query

try:
    api_response = api_instance.get_basic_search_results(index_name, q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->get_basic_search_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Name of the index | 
 **q** | **str**| Search Query | 

### Return type

[**SearchSuccess**](SearchSuccess.md)

### Authorization

[authToken](../README.md#authToken), [readAppID](../README.md#readAppID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_doc_type_suggest_results**
> SuggestSuccess get_doc_type_suggest_results(index_name, doc_type_name, q)



Gets Suggestions from `doc_type_name` in `index_name`. Please ensure you refer the getting started guides, to get the format of the query right.

### Example
```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = rsearch_client.Configuration()
configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: readAppID
configuration = rsearch_client.Configuration()
configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'

# create an instance of the API class
api_instance = rsearch_client.RsearchApi(rsearch_client.ApiClient(configuration))
index_name = 'index_name_example' # str | Name of the index
doc_type_name = 'doc_type_name_example' # str | Name of the Document_type
q = 'q_example' # str | Details of the suggest query

try:
    api_response = api_instance.get_doc_type_suggest_results(index_name, doc_type_name, q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->get_doc_type_suggest_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Name of the index | 
 **doc_type_name** | **str**| Name of the Document_type | 
 **q** | **str**| Details of the suggest query | 

### Return type

[**SuggestSuccess**](SuggestSuccess.md)

### Authorization

[authToken](../README.md#authToken), [readAppID](../README.md#readAppID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> GetDocumentSuccess get_document(index_name, doc_type_name, doc_id)



Fetches the document referenced by `doc_id` in `doc_type_name` for `index_name`

### Example
```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = rsearch_client.Configuration()
configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: readAppID
configuration = rsearch_client.Configuration()
configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'

# create an instance of the API class
api_instance = rsearch_client.RsearchApi(rsearch_client.ApiClient(configuration))
index_name = 'index_name_example' # str | Name of the index
doc_type_name = 'doc_type_name_example' # str | Name of the document_type
doc_id = 'doc_id_example' # str | Document ID

try:
    api_response = api_instance.get_document(index_name, doc_type_name, doc_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Name of the index | 
 **doc_type_name** | **str**| Name of the document_type | 
 **doc_id** | **str**| Document ID | 

### Return type

[**GetDocumentSuccess**](GetDocumentSuccess.md)

### Authorization

[authToken](../README.md#authToken), [readAppID](../README.md#readAppID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_type**
> GetDocTypeSuccess get_document_type(index_name, doc_type_name)



Checks whether `document_type` in `index_name` exists

### Example
```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = rsearch_client.Configuration()
configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: readAppID
configuration = rsearch_client.Configuration()
configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'

# create an instance of the API class
api_instance = rsearch_client.RsearchApi(rsearch_client.ApiClient(configuration))
index_name = 'index_name_example' # str | Name of the index
doc_type_name = 'doc_type_name_example' # str | Name of the document_type

try:
    api_response = api_instance.get_document_type(index_name, doc_type_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->get_document_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Name of the index | 
 **doc_type_name** | **str**| Name of the document_type | 

### Return type

[**GetDocTypeSuccess**](GetDocTypeSuccess.md)

### Authorization

[authToken](../README.md#authToken), [readAppID](../README.md#readAppID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_index**
> GetIndexSuccess get_index(index_name)



Checks whether `a particular index` {index_name} exists

### Example
```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = rsearch_client.Configuration()
configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: readAppID
configuration = rsearch_client.Configuration()
configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'

# create an instance of the API class
api_instance = rsearch_client.RsearchApi(rsearch_client.ApiClient(configuration))
index_name = 'index_name_example' # str | Name of the index

try:
    api_response = api_instance.get_index(index_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->get_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Name of the index | 

### Return type

[**GetIndexSuccess**](GetIndexSuccess.md)

### Authorization

[authToken](../README.md#authToken), [readAppID](../README.md#readAppID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

