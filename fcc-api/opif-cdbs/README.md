# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.9.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

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
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactUpdatesApi(swagger_client.ApiClient(configuration))
body = swagger_client.MainStudioClosedCaptionUpdate() # MainStudioClosedCaptionUpdate | Specify contactType as "MS" for Main Studio Contact and "CC" for Closed Caption Contact. Allowed values for contactSourceServiceCode are "TV", "AM" and "FM" for Main Studio Contact and "TV" for Closed Captions.

try:
    # Specify contactType as \"MS\" for Main Studio Contact and \"CC\" for Closed Caption Contact.
    api_instance.contact_update_json_post(body)
except ApiException as e:
    print("Exception when calling ContactUpdatesApi->contact_update_json_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */api/service*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContactUpdatesApi* | [**contact_update_json_post**](docs/ContactUpdatesApi.md#contact_update_json_post) | **POST** contact/update.json | Specify contactType as \&quot;MS\&quot; for Main Studio Contact and \&quot;CC\&quot; for Closed Caption Contact.
*CableApi* | [**cable_communities_psid_psid_format_get**](docs/CableApi.md#cable_communities_psid_psid_format_get) | **GET** /cable/communities/psid/{psid}.{format} | Cable Communities
*CableApi* | [**cable_eeo_group_by_format_get**](docs/CableApi.md#cable_eeo_group_by_format_get) | **GET** /cable/eeo/{groupBy}.{format} | Cable eeo
*CableApi* | [**cable_empunitid_update_json_post**](docs/CableApi.md#cable_empunitid_update_json_post) | **POST** /cable/empunitid/update.json | Modify Cable service employee units
*CableApi* | [**cable_getall_format_get**](docs/CableApi.md#cable_getall_format_get) | **GET** /cable/getall.{format} | Get All
*CableApi* | [**cable_operator_address_update_json_post**](docs/CableApi.md#cable_operator_address_update_json_post) | **POST** /cable/operatorAddress/update.json | Modify Cable operator address
*CableApi* | [**cable_principal_address_update_json_post**](docs/CableApi.md#cable_principal_address_update_json_post) | **POST** /cable/principalAddress/update.json | Modify Cable principal address
*CableApi* | [**cable_psid_psid_format_get**](docs/CableApi.md#cable_psid_psid_format_get) | **GET** /cable/psid/{psid}.{format} | Cable Details
*CableApi* | [**cable_relationship_username_coalsid_format_get**](docs/CableApi.md#cable_relationship_username_coalsid_format_get) | **GET** /cable/relationship/username/{COALSID}.{format} | Relationship Cable
*CableApi* | [**cable_service_zipcodes_update_json_post**](docs/CableApi.md#cable_service_zipcodes_update_json_post) | **POST** /cable/serviceZipcodes/update.json | Modify Cable service zip codes
*DbsApi* | [**dbs_eeo_facility_facility_id_format_get**](docs/DbsApi.md#dbs_eeo_facility_facility_id_format_get) | **GET** /dbs/eeo/facility/{facilityID}.{format} | DBS EEO
*DbsApi* | [**dbs_frn_frn_format_get**](docs/DbsApi.md#dbs_frn_frn_format_get) | **GET** /dbs/frn/{frn}.{format} | DBS Entity Details
*DbsApi* | [**dbs_getall_format_get**](docs/DbsApi.md#dbs_getall_format_get) | **GET** /dbs/getall.{format} | Get All
*DbsApi* | [**dbs_licensee_address_update_json_post**](docs/DbsApi.md#dbs_licensee_address_update_json_post) | **POST** /dbs/licenseeAddress/update.json | Update licensee address
*FacilityApi* | [**facility_search_keyword_format_get**](docs/FacilityApi.md#facility_search_keyword_format_get) | **GET** /facility/search/{keyword}.{format} | Search
*RelationshipApi* | [**relationship_frn_frn_format_get**](docs/RelationshipApi.md#relationship_frn_frn_format_get) | **GET** /relationship/frn/{frn}.{format} | Relationship FRN
*SdarsApi* | [**sdars_eeo_facility_facility_id_format_get**](docs/SdarsApi.md#sdars_eeo_facility_facility_id_format_get) | **GET** /sdars/eeo/facility/{facilityID}.{format} | SDARS EEO
*SdarsApi* | [**sdars_frn_frn_format_get**](docs/SdarsApi.md#sdars_frn_frn_format_get) | **GET** /sdars/frn/{frn}.{format} | SDARS Entity Details
*SdarsApi* | [**sdars_getall_format_get**](docs/SdarsApi.md#sdars_getall_format_get) | **GET** /sdars/getall.{format} | Get All
*SdarsApi* | [**sdars_licensee_address_update_json_post**](docs/SdarsApi.md#sdars_licensee_address_update_json_post) | **POST** /sdars/licenseeAddress/update.json | Update licensee address
*ServiceApi* | [**service_type_applications_facility_entity_id_format_get**](docs/ServiceApi.md#service_type_applications_facility_entity_id_format_get) | **GET** /{serviceType}/applications/facility/{entityID}.{format} | Entity Applications
*ServiceApi* | [**service_type_eeo_facilityid_entity_id_format_get**](docs/ServiceApi.md#service_type_eeo_facilityid_entity_id_format_get) | **GET** /{serviceType}/eeo/facilityid/{entityID}.{format} | Entity EEO
*ServiceApi* | [**service_type_facility_getall_format_get**](docs/ServiceApi.md#service_type_facility_getall_format_get) | **GET** /{serviceType}/facility/getall.{format} | Get All
*ServiceApi* | [**service_type_facility_id_entity_id_format_get**](docs/ServiceApi.md#service_type_facility_id_entity_id_format_get) | **GET** /{serviceType}/facility/id/{entityID}.{format} | Entity Details
*ServiceApi* | [**service_type_ownership_facilityid_entity_id_format_get**](docs/ServiceApi.md#service_type_ownership_facilityid_entity_id_format_get) | **GET** /{serviceType}/ownership/facilityid/{entityID}.{format} | Entity Ownership
*ServiceApi* | [**service_type_relationship_frn_frn_format_get**](docs/ServiceApi.md#service_type_relationship_frn_frn_format_get) | **GET** /{serviceType}/relationship/frn/{frn}.{format} | Relationship FRN

## Documentation For Models

 - [CableOperatorAddressUpdatePost](docs/CableOperatorAddressUpdatePost.md)
 - [CablePrincipalAddressUpdatePost](docs/CablePrincipalAddressUpdatePost.md)
 - [CableServiceEmpUnitsUpdatePost](docs/CableServiceEmpUnitsUpdatePost.md)
 - [CableServiceZipCodesUpdatePost](docs/CableServiceZipCodesUpdatePost.md)
 - [ClosedCaptionsUpdate](docs/ClosedCaptionsUpdate.md)
 - [Entity](docs/Entity.md)
 - [File](docs/File.md)
 - [FileHistory](docs/FileHistory.md)
 - [FileMovePost](docs/FileMovePost.md)
 - [FileRenamePost](docs/FileRenamePost.md)
 - [FileRestorePost](docs/FileRestorePost.md)
 - [FileUploadStats](docs/FileUploadStats.md)
 - [Folder](docs/Folder.md)
 - [FolderCreate](docs/FolderCreate.md)
 - [FolderHistory](docs/FolderHistory.md)
 - [FolderPost](docs/FolderPost.md)
 - [FolderRenamePost](docs/FolderRenamePost.md)
 - [FolderUpdate](docs/FolderUpdate.md)
 - [LicenseeAddressUpdatePost](docs/LicenseeAddressUpdatePost.md)
 - [MainStudioClosedCaptionUpdate](docs/MainStudioClosedCaptionUpdate.md)
 - [SearchResult](docs/SearchResult.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author


