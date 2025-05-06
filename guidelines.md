---
layout: default
title: PAN-NZ Draft Data Guidelines
# permalink: /
---


 
These guidelines set out the minimum data requirements for protected areas
datasets to be included in the Protected Areas Network of New Zealand (PAN-NZ). 

<br>

# Why Follow These Guidelines?
---
Aotearoa New Zealand has a rich and diverse network of protected areas,
including national parks, scenic reserves, QEII covenants, and council-managed
green spaces. Representing these areas consistently at a national level depends
on the quality and compatibility of the source data. 

That’s where you come in. 

PAN-NZ is a national initiative that brings together datasets from local and
central government, iwi, and NGOs. By providing your data in a consistent and
accessible format, you help to: 
* Improve national visibility of protected areas in your region 
* Strengthen environmental reporting, both within New Zealand and to
  international frameworks such as the IUCN and the Kunming-Montreal 30x30
  target 
* Support councils, communities, and planners with reliable spatial information 
* Enable more effective land-use planning and biodiversity protection across
  regional boundaries 
* Increase economic efficiency by identifying areas where development may be
  limited, helping focus effort and investment where it is most appropriate 

These guidelines are not intended to create unnecessary work. They aim to reduce
duplication, streamline integration, and simplify updates in future. Often,
small changes to metadata or access settings can make a dataset far more usable
at the national level. 

By aligning your data with these guidelines, you are contributing to a
nationally significant layer that supports conservation, planning, and
transparent decision-making across Aotearoa. 

<br>

# How to Contribute to These Guidelines? 
---

These guidelines are currently in draft form, and we welcome your feedback. 

If you have suggestions, corrections, or would like to propose improvements,
please see the [data catalogues]({{ site.baseurl }}/data_catalogues/index.html)
for information on how to get involved. 

Your input helps ensure the guidelines remain practical, inclusive, and widely
applicable across Aotearoa. 

<br>
# Requirements
---
Below are the minimum requirements that a protected area dataset must meet to be
included in the national PAN-NZ dataset. 

<br>
## Data access
---
To ensure datasets can be easily discovered, evaluated, and integrated into the
national dataset, data holders should meet the following access-related
criteria. 


### 1. Licensing
Open licensing enables datasets to be used nationally without legal uncertainty.
It allows PAN-NZ to be openly published, shared, and integrated with other
public data. 

Each dataset must have a clearly stated data licence that permits reuse and
redistribution. The preferred licence is [Creative Commons Attribution 4.0 (CC
BY 4.0)](https://creativecommons.org/licenses/by/4.0/). The licence should be
included in the dataset’s metadata and clearly visible at the point of access.
This aligns with the [New Zealand Government's NZGOAL framework](New Zealand
Government NZGOAL), which encourages open release of public data to maximise
value and reuse. 


<br>

<a href="https://raw.githubusercontent.com/manaakiwhenua/PANNZ-source-data/main/IMG/example_licensing.png" target="_blank">
  <img src="{{ site.baseurl }}/IMG/example_licensing.png"
       alt="PAN-NZ Diagram"
       style="max-width: 100%; height: auto;" />
</a>
**Above:** An example of a protected areas source dataset with its licence
clearly displayed at the point of access that allows for reuse. Example as per
[Hawke's Bay Regional
Parks](https://hub.arcgis.com/datasets/658697bb70c345f48d21cc002ecc0bef_1/explore) 


<br>



#### Common Licensing Issues That Exclude Datasets 
Below are common licensing issues that prevent datasets from being included in
the national PAN-NZ data layer. When licensing excludes a dataset, the protected
areas it contains may not appear in the national PAN-NZ layer, limiting their
visibility to policymakers, researchers, and the public. 
* **No License:** Without a licence, the reuse conditions are unclear and the
  dataset cannot be included. 
* **Restrictive licence:** Licences such as [CC BY-ND (No
  Derivatives)](https://creativecommons.org/licenses/by-nd/4.0/) (see the terms
  of use in image directly below) prohibit modifications or integration with
  other datasets. Since PAN-NZ requires remixing and aggregation, such datasets
  are excluded. 

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
PAN-NZ prioritises datasets that are easy to access and update. Preferred
methods are listed below in order of suitability: 
* **API access:** Data provided via API (such as OGC WFS or REST services)
  allows for automated integration and regular updates. 
* **Self-service download:** If API access is not feasible, datasets should be
  made available through a direct download link. This enables a PAN-NZ
  administrator to manually retrieve the data, though it does not support
  automation and is therefore considered less efficient. 

  Both API and download options support discoverability, as these services are
  typically indexed by search engines. This makes them easier for PAN-NZ
  administrators to locate when searching for protected area data sources. 

* **Email request:** If neither of the above options is available, data may
* still be provided upon request by email. However, this approach increases the
* workload for both parties and limits discoverability. Datasets that are not
* publicly visible or accessible may be missed simply because administrators do
* not know they exist or cannot identify a contact person. 
  
<br>

### 3. Metadata

Metadata provides essential context to help users understand and correctly
interpret your dataset. While a full ISO 19115 metadata record is ideal, PAN-NZ
requires only a minimal metadata profile containing the following fields: 

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
To ensure your protected area datasets are visible and accessible to PAN-NZ and
other users, we encourage the following good practices: 

* **Publish data on open data portals:** Hosting datasets on platforms such as
  Koordinates, ArcGIS Online, council open data sites, or
  [data.govt.nz](https://data.govt.nz/catalogue-guide/releasing-data-on-data-govt-nz)
  significantly improves visibility. These platforms are routinely indexed by
  search engines, making your data easier to discover.Use clear and descriptive
  metadata: Include titles, summaries, spatial coverage, and keywords such as
  “protected area,” “conservation land,” or “significant natural area.”
  Well-tagged metadata increases the chances your dataset will appear in search
  results. 
* **Apply consistent naming conventions:** Avoid generic names like Layer1.shp.
  Instead, use clear, versioned titles such as Waikato_Parks_and_Reserves to
  improve clarity and version tracking. 
* **Ensure stable access URLs:** Maintain consistent download and API URLs so
  that PAN-NZ administrators can access your dataset reliably over time. 
* **Provide contact details in metadata:** Include the name and email of a
  responsible person or team. This helps PAN-NZ reach out with questions or
  update requests. 
* **Register your dataset in the PAN-NZ data catalogues:** Ensure your dataset
  is recorded in the [cataloguing
  component](https://manaakiwhenua.github.io/PANNZ-source-data/data_catalogues/index.html)
  of this site. This helps track coverage and supports national coordination. 

By following these steps, your dataset becomes easier to discover, interpret,
and integrate into national frameworks, contributing to a clearer and more
complete picture of protected areas across Aotearoa. 

<br>

### 5. Privacy 
PAN-NZ aims to develop an open and accessible national dataset of protected
areas while fully complying with the Privacy Act 2020. Public-facing datasets
should not include any personal or identifying information about individuals.
This includes, but is not limited to: 
* Personal names (e.g. landowners) 
* Private addresses 
* Contact details (e.g. phone numbers or email addresses) 

Maintaining privacy from the outset helps ensure that PAN-NZ remains a trusted,
inclusive, and legally compliant platform for sharing environmental information. 

<br>

## Data Attributes
---
The section below lists the minimum set of attributes needed to describe a
protected area in a way that’s meaningful and usable within PAN-NZ. 

<br>

### 1. PAN-NZ Schema 
To support consistent integration across New Zealand, PAN-NZ defines a minimal
schema for describing protected areas. This schema outlines the essential
attributes each dataset should contain to be eligible for inclusion in the
national dataset. 

The table below specifies the minimum attributes required for each protected
area record. While we expect many datasets to contain additional information,
only the fields listed here are considered necessary for national aggregation.
Additional attributes may still be valuable locally but will not be carried into
the PAN-NZ core dataset. 

Note: While we define preferred field names, your dataset does not need to use
these exact names. The key requirement is that the information is present. Field
mappings can be applied during aggregation to align your dataset with the PAN-NZ
schema. 



| Field Name          | Description                                                                                                                           | Required |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| persistent_id       | A unique and persistent identifier for the protected area.                                                                            | Yes      |
| name                | The commonly used or official name of the protected area.                                                                             | Yes      |
| legislation_act     | The name of the legislation under which the area is protected.                                                                        | Yes      |
| legislation_section | The specific section or clause of the act relevant to the protection.                                                                 | Yes      |
| protection_type     | The type or category of protection (e.g., reserve, covenant, national park).                                                          | No       |
| local_reserve       | The purpose of reserves under Section 22 (government purpose reserve) and section 23 (local purpose reserve) of the Reserved Act 1977 | No       |

Further detail on each field is provided in the following sections, including
how they support national integration and classification (e.g. IUCN category
mapping). 

<br>



### 2. Persistent Identifier

| PAN-NZ Schema Name | Required |
| ------------------ | -------- |
| id                 | yes      |

Each protected area record should include a persistent, unique identifier. This
ensures records can be tracked across updates and matched across systems. 

<br>

### 3. Protection Name

| PAN-NZ Schema Name | Required             |
| ------------------ | -------------------- |
| name               | yes - where recorded |

name 
	

yes - where recorded 

If the managing entity assigns names to protected areas, they should be
included. Providing a recognisable name helps users refer to each area via a
common name, rather than relying on IDs alone. 

This can also assist in linking protections to other sources of information that
rely on names as common identifiers, such as management plans that refer to
protected areas by name. 

<br>

### 4. Legal Act

| PAN-NZ Schema Name | Required                 |
| ------------------ | ------------------------ |
| legislation_act    | yes - where not implicit |


Datasets should specify the legislative act under which each area is protected.
This field provides the legal context needed to confirm protection status and
supports classification into IUCN categories. Without this information the
degree to which the areas is protected can not be communicated. 

In some cases, however, the applicable legislation may be implied from the
dataset context. For example, a dataset titled “Regional Parks” may be
understood to refer to areas protected under Section 139 of the Local Government
Act 2002. For this reason, this field is marked as required where not implicit. 

Best practices: 
* Use the full name of the Act (e.g. Reserves Act 1977), not abbreviations like
  “RA77”. 
* Each spatial extent should correspond to a single legislative act. If multiple
  acts apply, separate spatial features should be created for each. 

Examples of common protected area related legislation can be found in the below
section 

<br>

### 5. Legal Section

| PAN-NZ Schema Name  | Required                 |
| ------------------- | ------------------------ |
| legislation_section | yes - where not implicit |

Where applicable, include the specific section in the Act that establishes the
legal protection. This field provides the legal context needed to confirm
protection status and supports classification into IUCN categories. 

The preferred format is: `S_<Section Number>_<NAME>`, for example:
S19_CONSERVATION_PARK. 

The below table provides an example of a subset of the legislative acts and
sections that are commonly captured by PAN-NZ 

Note, the convention of using capitals. This is due to major central government
datasets applying this convention to their legislation act and section
attributes in their data. Lowercase is also acceptable as data pipelines can
consider this information as the same. 


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

**Above Table:** The above table provides an example of a subset of protected
area legislation acts and sections 

<br>

### 6. Local Purpose Type

| PAN-NZ Schema Name | Required                                                                |
| ------------------ | ----------------------------------------------------------------------- |
| reserve_purpose    | No - only for areas under section 22 and 23 under the Reserves Act 1977 |

Under the Reserves Act 1977, areas protected under Section 22 (Government
Purpose Reserve) and Section 23 (Local Purpose Reserve) should include the
specific purpose of the reserve in the `reserve_purpose` field. These reserves can
serve a wide variety of functions, ranging from wetland conservation to
infrastructure-related uses such as gravel extraction. Capturing this detail
helps clarify both the intent and the strength of protection provided. Including
this information is important for understanding the role and significance of
each protected area within the national context. 

<br>

### 7. Protection Type

| PAN-NZ Schema Name | Required |
| ------------------ | -------- |
| protection_type    | No       |

This field is not mandatory, but some datasets include a type attribute that
describes the nature of the protection. When legal act and section details are
missing, this field can help infer the legislative basis for protection. 

Using this field alone is not the preferred method, as it can introduce
ambiguity or lead to incorrect classifications. However, it may still be useful
when no formal legal references are available. 

The protection type should describe the form of protection, such as “Scenic
Reserve,” “Wildlife Sanctuary,” or “Recreation Reserve.” During data
aggregation, PAN-NZ may use these values to assign likely legal categories. For
example, if a record is typed as “Wildlife Sanctuary” but lacks legal
references, PAN-NZ may infer it corresponds to Section 9 of the Wildlife Act 1953. 


<br>

## Working with Incomplete or Partial Datasets 
---
We recognise that not all datasets will initially meet every requirement in
these guidelines. Some datasets may be missing legal references or may be
incomplete. These datasets are still valuable. 

Even if your data is not yet fully compliant, we encourage you to share it with
us. Early contribution allows us to: 
* Provide feedback to help align with PAN-NZ requirements 
* Identify opportunities to improve national coverage 
* Work together on small enhancements that improve usability 

You don’t need to wait for a perfect dataset. PAN-NZ is designed to evolve and
improve over time, your early contribution is a key part of that process. 

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

In summary, datasets that contribute to the PAN-NZ national layer should meet
the following criteria: 
* **Licensing:** A clearly stated open licence is required, with Creative Commons
  Attribution 4.0 (CC BY 4.0) preferred. 
* **Data Access:** Datasets must be accessible via API or direct download. 
* **Metadata:** A basic metadata profile should describe the dataset’s content,
  source, and licence. 
* **Discoverability:** Datasets should be hosted on open data platforms, use
  consistent naming, and provide stable URLs. 
* **Privacy:** All personal or sensitive information must be removed in accordance
  with the Privacy Act 2020. 
* **Attributes:** The dataset must include the minimum PAN-NZ schema fields,
  including a persistent ID, protection name, and legislative references. 

By meeting these requirements, data holders help ensure their protected areas
data can be accurately integrated and nationally recognised through PAN-NZ. 

