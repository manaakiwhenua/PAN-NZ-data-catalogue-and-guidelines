---
layout: default
title: PAN-NZ Draft Data Guidelines
# permalink: /
---


 
These guidelines outline the minimum data requirements for data holders to ensure their 
protected areas data can be incorporated into PAN-NZ. 

<br>

# Why Follow These Guidelines?
---
Aotearoa New Zealand has a rich and diverse network of protected areas, from national parks and 
reserves to QEII covenants and local council-protected sites. However, the ability to
 understand and represent these areas consistently at a national level depends on the
  quality and compatibility of the underlying data.

That’s where you come in.

The Protected Areas Network of New Zealand (PAN-NZ) is a national initiative that brings 
together datasets from local and central government, and NGOs. By contributing your data in a consistent format, you are helping to:
* Improve national visibility of protected areas in your region
* Support stronger environmental reporting, both domestically and to international 
frameworks like the IUCN and the Kunming-Montreal 30x30 target. 
* Empower local communities, councils, and planners with better spatial information
* Enable more effective land-use planning and biodiversity protection across regional boundaries
* Improve economic efficiency by clearly identifying areas where development is restricted, 
helping councils, developers, and infrastructure planners focus effort and investment in appropriate locations


The standards outlined in this document aren’t here to create extra burden, they are designed to 
reduce duplication of effort, streamline integration, and make it easier to update data going forward. 
In many cases, small changes to metadata or access settings can have a big impact.

By aligning your datasets with these guidelines, you're not just supplying data, 
you're contributing to a nationally significant information layer that supports environmental 
stewardship across Aotearoa.

<br>
# Requirements
---
Below are the data requirements that a protected area dataset must meet to be added to the national
PAN-NZ dataset 

<br>
## Data access
---
To ensure datasets can be easily discovered, evaluated, and integrated into 
the national dataset, data holders should meet the access-related requirements
as outlined in the below sections


### 1. Licensing
Open licensing enables datasets to be combined at a national level without legal barriers or ambiguity as to how the data 
can be used. It ensures that PAN-NZ can be openly published, shared, and integrated with other public data.

Each dataset must have a clearly stated data licence that allows for reuse and redistribution. Preferably, 
this should be the [Creative Commons Attribution 4.0 (CC BY 4.0) licence](https://creativecommons.org/licenses/by/4.0/). 
The license should be supplied as part of the datasets metadata (see section [metadata](#3-metadata)) and be clearly 
displayed at the point of access. This approach is consistent with the [New Zealand Government NZGOAL](https://www.data.govt.nz/toolkit/policies/nzgoal) 
policy to release data under open terms to maximise its value and reuse.


<br>

<a href="https://raw.githubusercontent.com/manaakiwhenua/PANNZ-source-data/main/IMG/example_licensing.png" target="_blank">
  <img src="{{ site.baseurl }}/IMG/example_licensing.png"
       alt="PAN-NZ Diagram"
       style="max-width: 100%; height: auto;" />
</a>
**Above:** An example of a protected areas source dataset with its licence clearly displayed at the point of 
access that allows for reuse. Example as per [Hawke's Bay Regional Parks](https://hub.arcgis.com/datasets/658697bb70c345f48d21cc002ecc0bef_1/explore) 


<br>



#### Common Licensing conditions that exclude protected area data being included in PAN-NZ
Below are common licensing issues that prevent datasets from being included in the national PAN-NZ data layer. 
When licensing excludes a dataset, the protected areas it contains may not appear in the national PAN-NZ layer, limiting 
their visibility to policymakers, researchers, and the public.
* **No License:** If no licence is provided, PAN-NZ cannot include the dataset due to the ambiguity around the 
conditions of use.
* **Too restrictive of a License**: Some licenses allow degrees of public reuse but are too restrictive to allow 
  inclusion in PAN-NZ. For example, some protected area datasets are licensed under 
  [CC-BY-4.0-NoNDerivatives](https://creativecommons.org/licenses/by-nd/4.0/) (See the terms of
use in image directly below). This is problematic as PAN-NZ is a derivative, and data under this license therefore can not be 
included. 

<br>

<div style="text-align: center;">
<img src="IMG/cc-by-40-ND.png" alt="PAN-NZ Diagram" width="500" style="border: 1px solid #ccc; padding: 4px;"/>
</div>

**Above:** The [CC-BY-4.0-NoNDerivatives](https://creativecommons.org/licenses/by-nd/4.0/) license which excludes
derivatives as a result of remixing, transforming or building upon the original data. Such license
excludes datasets from PAN-NZ    
<br>


<br>
### 2. Data Access
PAN-NZ requires source datasets to be accessible with minimal effort for both those accessing and supplying the data.

Preferred methods of access (in order of preference):
* **API access:**
    Data supplied via an API can be fetched programmatically and automatically integrated into PAN-NZ. This allows 
    for regular updates, ensuring the national dataset remains current and accurately reflects the latest information.
     API access includes data supplied through OGC (Open Geospatial Consortium) standards such as WFS (Web Feature Service), as well as RESTful APIs.

* **Self-service download:**
    If an API access is not feasible, datasets should be made available through a self-service download link. This 
    allows a PAN-NZ administrator to manually download the dataset. However,
     as it does not support automation, it is considered less efficient than API access.

    Both API and direct download options have the added benefit of discoverability. Services that support these 
    access methods are typically indexed by search engines, making them easier for PAN-NZ administrators to find
    when searching for protected area data sources.

* **Email request:**
    If neither of the above options is available, the PAN-NZ administrator may need to contact the data provider 
    directly to request access. This approach requires significantly more effort for both parties. Additionally,
     because the dataset is not discoverable online, it risks being excluded from the national dataset simply
    because the administrator may not know it exists or whom to contact to obtain it.

<br>

### 3. Metadata

Metadata helps others understand and correctly interpret your dataset. While a full ISO 19115 record is ideal, 
PAN-NZ requires a minimum metadata profile with the following fields:

| Field             | Description                                                     |
| ----------------- | --------------------------------------------------------------- |
| Title             | Name of the dataset                                             |
| Description       | Short explanation of the dataset's purpose and contents         |
| Creator / Owner   | The organisation responsible for maintaining the dataset        |
| Contact Email     | A contact person for questions or updates                       |
| Licence           | The licence applied to the dataset                              |
| Date Updated      | Most recent date of data revision or publication                |
| Geographic Extent | Area covered (e.g. "Tasman District", or bounding box in WGS84) |
| Projection        | Spatial reference system (e.g. NZTM2000 or EPSG:2193)           |
| Format            | File format used (e.g. GeoPackage, Shapefile)                   |


<br>

### 4. Discoverability 
To support discoverability, data providers can take several simple but effective steps to ensure their 
protected area datasets are visible and accessible to national initiatives like PAN-NZ:
* Publish data on open data portals such as their regional open data platforms (e.g. using Koordinates or ArcGIS Online)
These platforms are regularly indexed by search engines.
* Ensure datasets have clear and descriptive metadata, including titles, descriptions, 
  spatial coverage, and keywords such as “protected area,” “conservation land,” or “significant natural area.”
  Well-tagged metadata increases the likelihood that the dataset will surface in search results.
* Use consistent naming and formatting, particularly for datasets that are regularly updated. Avoid generic names
   like “Layer1.shp” in favour of more meaningful titles like “Waikato_Parks_and_Reserves_2024.”
* Ensure download and API links are stable. This makes it easier for PAN-NZ administrators 
  to access and revisit the data as needed.
* Include contact details or data stewards in metadata records. This way if there are issues in accessing the data
  the right person can be easily identified and notified. 
* Ensuring the datasets are recorded in the [data catalogues]({{ site.baseurl }}/data_catalogues/index.html) 
  component of this site.

By taking these steps, councils can help ensure their datasets are not only accessible, but also visible and
usable within national frameworks, contributing to a more complete and accurate picture of protected areas across Aotearoa.

<br>

### 5. Privacy 
PAN-NZ aims to build an open and accessible national dataset of protected areas while upholding privacy obligations under 
the Privacy Act 2020. Public facing protected areas datasets should not contain any personal or identifying 
information about individuals, including:
* Personal names (e.g. landowners)
* Private addresses
* Contact details (e.g. phone numbers or email addresses)

By respecting privacy from the outset, we ensure that PAN-NZ remains a trustworthy, inclusive, and legally sound platform for environmental data.

<br>
## Data Attributes
---
The section below lists the minimum set of attributes needed to describe a protected area in a way that’s
meaningful and usable within PAN-NZ.

<br>

### 1. PAN-NZ Schema 
The PAN-NZ schema defines a minimal set of attributes needed to describe protected areas consistently
across New Zealand. These attributes help ensure integration into the national dataset.


The below table outlines the minimum details required for each protected area entry (feature). 
While these are the minimum, it is expected other information will be provided, however
this will not be included in the national PAN-NZ layer. 

While the schema defines specific field names, it is not required that source datasets use exactly
the same names. However, aligning with the schema is beneficial and appreciated. The key requirement is that
 the necessary fields and their information are present. Field name mappings can be applied 
 during the data aggregation stage to ensure compatibility.
 



| Field Name            | Description                                                                                                                           | Required |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `persistent_id`       | A unique and persistent identifier for the protected area.                                                                            | Yes      |
| `name`                | The commonly used or official name of the protected area.                                                                             | Yes      |
| `legislation_act`     | The name of the legislation under which the area is protected.                                                                        | Yes      |
| `legislation_section` | The specific section or clause of the act relevant to the protection.                                                                 | Yes      |
| `protection_type`     | The type or category of protection (e.g., reserve, covenant, national park).                                                          | No       |
| `local reserve`       | The purpose of reserves under Section 22 (government purpose reserve) and section 23 (local purpose reserve) of the Reserved Act 1977 | No       |

The sections below provide further explanation of each required attribute, outlining its purpose, 
associated requirements, and how it contributes to the PAN-NZ dataset.

<br>



### 2. Persistent Identifier

| PAN-NZ Schema Name | Required |
| ------------------ | -------- |
| id                 | yes      |

Each protected area record should include a persistent, unique identifier. This ensures records 
can be tracked across updates and matched across systems.

<br>

### 3. Protection Name

| PAN-NZ Schema Name | Required             |
| ------------------ | -------------------- |
| name               | yes - where recorded |

If the managing entity assigns names to protected areas, they should be included. Providing a recognisable name helps 
users refer to each area via a common name, rather than relying on IDs alone.

This can also assist in linking protections to other sources of information that 
rely on names as common identifiers, such as management plans that refer to protected areas by name.

<br>

### 4. Legal Act

| PAN-NZ Schema Name | Required                 |
| ------------------ | ------------------------ |
| legislation_act    | yes - where not implicit |

Datasets should specify the legislative act under which each area is protected. This field 
provides the legal context needed to confirm protection status and supports 
classification into IUCN categories. Without this information 
the degree to which the areas is protected can not be communicated. 

However it is noted with some datasets the legislation is implicit and therefore this
field is not required. For example, for a dataset named "Regional Parks"
it may be inferred that the protected areas are under the Local Government Act 2002 
 Section 139 Regional Park. This is the reason that required status is "yes - where not implicit"

Best practices:

* Use the full name of the Act (e.g. Reserves Act 1977), not abbreviations like "RA77".
* Each spatial extent should correspond to a single legislative act. If multiple acts apply, 
separate spatial features should be created for each.

Examples of common protected area related legislation can be found in the below section

<br>

### 5. Legal Section

| PAN-NZ Schema Name  | Required                 |
| ------------------- | ------------------------ |
| legislation_section | yes - where not implicit |

Where applicable, include the specific section in the Act that establishes the legal protection.
This field provides the legal context needed to confirm protection status and supports classification into IUCN categories.


Ideally this is in the format of `S_<Section Number>_<NAME>` e.g. `S19_CONSERVATION_PARK`

The below table provides an example of a subset of the legislative acts and 
sections that are commonly captured by PAN-NZ 

Note, the convention of using capitals. This is due to major central government datasets applying this 
convention to their legislation act and section attributes in their data. Lowercase is also acceptable as
data pipelines can consider this information as the same. 


| Legislation Act                            | Legislation Section           |
| :----------------------------------------- | :---------------------------- |
| CONSERVATION_ACT_1987                      | S19_CONSERVATION_PARK         |
| CONSERVATION_ACT_1987                      | S20_WILDERNESS_AREA           |
| CONSERVATION_ACT_1987                      | S21_ECOLOGICAL_AREA           |
| CONSERVATION_ACT_1987                      | S22_SANCTUARY_AREA            |
| CONSERVATION_ACT_1987                      | S23A_AMENITY_AREA             |
| CONSERVATION_ACT_1987                      | S23B_WILDLIFE_MANAGEMENT_AREA |
| CONSERVATION_ACT_1987                      | S25_STEWARDSHIP_AREA          |
| LOCAL_GOVERNMENT_ACT_2002                  | S139_REGIONAL_PARK            |
| QUEEN_ELIZABETH_II_NATIONAL_TRUST_ACT_1977 | S22_QEII_OPEN_SPACE_COVENANT  |
| RESERVES_ACT_1977                          | S17_RECREATION_RESERVE        |
| RESERVES_ACT_1977                          | S19_1_A_SCENIC_RESERVE        |
| RESERVES_ACT_1977                          | S19_1_B_SCENIC_RESERVE        |
| RESERVES_ACT_1977                          | S23_LOCAL_PURPOSE_RESERVE     |
| RESERVES_ACT_1977                          | S17_RECREATION_RESERVE        |
| WILDLIFE_ACT_1953                          | S14_WILDLIFE_REFUGE           |
| WILDLIFE_ACT_1953                          | S9_WILDLIFE_SANCTUARY         |

**Above Table:** The above table provides an example of a subset of protected area legislation acts and 
sections 

<br>

### 6. Local Purpose Type

| PAN-NZ Schema Name | Required                                                                |
| ------------------ | ----------------------------------------------------------------------- |
| reserve_purpose    | No - only for areas under section 22 and 23 under the Reserves Act 1977 |

Under the Reserves Act 1977, for areas protected under Section 22 (Government Purpose Reserve) and 
Section 23 (Local Purpose Reserve), the specific purpose of the reserve should be recorded in 
the `reserve_purpose` field. These types of reserves are used for a wide range of purposes
 from wetland protection to gravel extraction and capturing this detail helps clarify the 
 intent and degree of protection. This information is essential for understanding 
 how and why an area is protected.

<br>

### 7. Protection Type

| PAN-NZ Schema Name | Required |
| ------------------ | -------- |
| protection_type    | No       |

This field is not required, but some datasets include a type field that describes the
 protection. Where the legal act and section are not available, this field can be 
 used to infer the legislative basis for the protection.

While this is not the preferred approach as it can introduce ambiguity and errors
 when mapping types to legislation, it may be used when no other legal context is 
 available. 

This field should describe the kind of protection conferred by the legal status.
for example as "Scenic Reserve", "Wildlife Sanctuary", "Recreation Reserve", etc.

The PAN-NZ data aggregation process will for example extract "WILDLIFE_ACT_1953
S9_WILDLIFE_SANCTUARY" where the type is "Wildlife Sanctuary" but no legal act or section information
is available. 


<br>


<!-- ## A Note on Data Interoperability Principles
---
Data interoperability means that datasets can be easily discovered, 
accessed, and integrated from the very first point of contact.

In the PAN-NZ schema section above, we outline the minimum required 
fields. While some data interoperability initiatives require strict 
adherence to standardised field names, PAN-NZ instead focuses on 
ensuring that data can be readily used without requiring users to dig deep, negotiating  access, or track down contacts for clarification.

To support this, we encourage the following good practices:
* Use of standard metadata to clearly describe the dataset
* Open and widely supported formats such as GeoJSON, Shapefile, or GeoPackage (GPKG)
* Stable API endpoints, ideally using open standards such as OGC WFS or OGC API
* Clear documentation explaining field meanings and intended use
* Consistent and intuitive attribute naming, where possible

These practices help reduce barriers to integration and make it easier for others to work with your data in national and local contexts. -->


<br>

## Summary of PAN-NZ Minimum Requirements
---
In summary, datasets submitted for inclusion in PAN-NZ must meet the following criteria:

- **Licensing:** Clearly stated open license (CC BY 4.0 preferred)
- **Data Access:** Accessible via API, direct download
- **Metadata:** A minimal metadata profile clearly describing your dataset
- **Discoverability:** Indexed on open data platforms, consistent naming, stable URLs
- **Privacy:** Personal and sensitive information removed
- **Attributes:** Meet the minimum attribute schema including persistent IDs, protection name, protection legislation details

Following these guidelines ensures your protected areas data can be effectively integrated, represented, and used at the national level.


