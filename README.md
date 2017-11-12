# pstack-rsearch-api
REST API Specification for ParallelStack RSearch API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://developer.parallelstack.com](https://developer.parallelstack.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import rsearch_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import rsearch_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import rsearch_client
from rsearch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
rsearch_client.configuration.api_key['auth_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# rsearch_client.configuration.api_key_prefix['auth_token'] = 'Bearer'
# Configure API key authorization: writeAppID
rsearch_client.configuration.api_key['X-RSearch-App-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# rsearch_client.configuration.api_key_prefix['X-RSearch-App-ID'] = 'Bearer'
# create an instance of the API class
api_instance = rsearch_client.RsearchApi()
index_name = 'index_name_example' # str | Name of the index
doc_type_name = 'doc_type_name_example' # str | Name of the document_type
doc_id = 'doc_id_example' # str | Document ID
document_details = NULL # object | Details of the document

try:
    api_response = api_instance.add_document(index_name, doc_type_name, doc_id, document_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RsearchApi->add_document: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.parallelstack.com/api/rsearch/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RsearchApi* | [**add_document**](docs/RsearchApi.md#add_document) | **POST** /indexes/{index_name}/document_types/{doc_type_name}/documents/{doc_id} | 
*RsearchApi* | [**add_document_type**](docs/RsearchApi.md#add_document_type) | **POST** /indexes/{index_name}/document_types/{doc_type_name} | 
*RsearchApi* | [**add_index**](docs/RsearchApi.md#add_index) | **POST** /indexes/{index_name} | 
*RsearchApi* | [**delete_document**](docs/RsearchApi.md#delete_document) | **DELETE** /indexes/{index_name}/document_types/{doc_type_name}/documents/{doc_id} | 
*RsearchApi* | [**delete_index**](docs/RsearchApi.md#delete_index) | **DELETE** /indexes/{index_name} | 
*RsearchApi* | [**get_advanced_search_results**](docs/RsearchApi.md#get_advanced_search_results) | **POST** /indexes/{index_name}/document_types/{doc_type_name}/search | 
*RsearchApi* | [**get_all_document_types**](docs/RsearchApi.md#get_all_document_types) | **GET** /indexes/{index_name}/document_types | 
*RsearchApi* | [**get_all_documents**](docs/RsearchApi.md#get_all_documents) | **GET** /indexes/{index_name}/document_types/{doc_type_name}/documents | 
*RsearchApi* | [**get_all_indexes**](docs/RsearchApi.md#get_all_indexes) | **GET** /indexes | 
*RsearchApi* | [**get_basic_search_results**](docs/RsearchApi.md#get_basic_search_results) | **GET** /indexes/{index_name}/search | 
*RsearchApi* | [**get_document**](docs/RsearchApi.md#get_document) | **GET** /indexes/{index_name}/document_types/{doc_type_name}/documents/{doc_id} | 
*RsearchApi* | [**get_document_type**](docs/RsearchApi.md#get_document_type) | **GET** /indexes/{index_name}/document_types/{doc_type_name} | 
*RsearchApi* | [**get_index**](docs/RsearchApi.md#get_index) | **GET** /indexes/{index_name} | 
*RsearchApi* | [**get_suggest_results**](docs/RsearchApi.md#get_suggest_results) | **GET** /indexes/{index_name}/document_types/{doc_type_name}/suggest | 


## Documentation For Models

 - [DoctypesFailure](docs/DoctypesFailure.md)
 - [GetAllDoctypesSuccess](docs/GetAllDoctypesSuccess.md)
 - [GetDoctypeSuccess](docs/GetDoctypeSuccess.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2001Index](docs/InlineResponse2001Index.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2002Indexes](docs/InlineResponse2002Indexes.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2003DocumentType](docs/InlineResponse2003DocumentType.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2004Document](docs/InlineResponse2004Document.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2007SearchResults](docs/InlineResponse2007SearchResults.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2008SuggestResults](docs/InlineResponse2008SuggestResults.md)
 - [InlineResponse200Indexes](docs/InlineResponse200Indexes.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse2011](docs/InlineResponse2011.md)
 - [InlineResponse201Index](docs/InlineResponse201Index.md)
 - [InlineResponse202](docs/InlineResponse202.md)
 - [InlineResponse202Index](docs/InlineResponse202Index.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [InlineResponse4001](docs/InlineResponse4001.md)
 - [InlineResponse4002](docs/InlineResponse4002.md)
 - [InlineResponse4003](docs/InlineResponse4003.md)
 - [InlineResponse4004](docs/InlineResponse4004.md)
 - [InlineResponse4005](docs/InlineResponse4005.md)
 - [InlineResponse4006](docs/InlineResponse4006.md)
 - [InlineResponse4006SearchResults](docs/InlineResponse4006SearchResults.md)
 - [InlineResponse4007](docs/InlineResponse4007.md)
 - [InlineResponse4007SearchResults](docs/InlineResponse4007SearchResults.md)
 - [InlineResponse400Indexes](docs/InlineResponse400Indexes.md)
 - [SearchSuccess](docs/SearchSuccess.md)


## Documentation For Authorization


## authToken

- **Type**: API key
- **API key parameter name**: auth_token
- **Location**: URL query string

## readAppID

- **Type**: API key
- **API key parameter name**: X-RSearch-App-ID
- **Location**: HTTP header

## writeAppID

- **Type**: API key
- **API key parameter name**: X-RSearch-App-ID
- **Location**: HTTP header


## Author

team at parallelstack.com

