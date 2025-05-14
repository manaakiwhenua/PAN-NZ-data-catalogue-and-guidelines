---
layout: default
title: Regional Data Sources
permalink: /regional_datasets_catalogue/
---

This catalogue documents datasets that represent protected areas managed at the
regional level, typically by local government. By cataloguing these datasets,
PAN-NZ aims to improve the visibility of locally administered protected areas,
support integration into national datasets, and provide a clearer understanding
of the various legal and administrative mechanisms used to protect land at the
local level.

If you are a data holder and your regional protected area dataset is not yet
included, we encourage you to contribute by following the instructions via the
[Contribute / Contact]({{ site.baseurl }}/contributing/index.html) page.  

<br>

## Protection Types
---
In the below data catalogue (see table below), each dataset is categorised as per the below
protection types.

<br>

### 1. Parks and Reserves

These datasets typically represent land set aside for conservation, recreation
and amenity purposes, and may include:
* Reserves gazetted under the Reserves Act 1977
* Regional parks established under section 139 of the Local Government Act 2002
* Local purpose reserves managed by councils
* Other open space identified through district plans or long-term planning instruments

<!-- #### Suitability of Local Government Parks and Reserves Datasets -->


<br>

### 2. SNA Data Sources
This catalogue documents datasets relating to Significant Natural Areas (SNAs)
as identified under Section 6(c) of the Resource Management Act 1991, which
requires all territorial authorities to map and protect areas of significant
indigenous vegetation and significant habitats of indigenous fauna as a matter
of national importance.

While PAN-NZ is gathering protected area data sources more broadly, we are
recording known SNA datasets for visibility and coordination purposes. However,
we are not currently prioritising their inclusion in the national PAN-NZ protected
areas layer. This is due to ongoing ambiguity resulting from recent RMA
legislative changes and the expectation of further updates to New Zealand’s
resource management system.

<br>

### 3. Other Regional Protected Area Types

Previous PAN-NZ reports have noted that local government may hold datasets
relating to local government covenants or other protected areas that do not fall
under typical categories such as parks, reserves, or SNAs.

We are interested in identifying and cataloguing any such datasets. If your
organisation holds spatial data for protected areas created through other
mechanisms, please get in touch. 

<br>
## Known Issues with Local Government Datasets
---

### Dataset Intent
We acknowledge that some local government datasets were not developed with the
intent of representing legally protected areas. For example, the Auckland
Council [Park
Extents](https://data-aucklandcouncil.opendata.arcgis.com/datasets/park-extents/explore)
dataset states that its polygons reflect maintenance areas rather than legal
boundaries, and that it does not indicate whether land is formally gazetted or
protected under legislation such as the Reserves Act 1977 or the Local
Government Act 2002.

Despite these limitations, PAN-NZ may include such datasets where they provide
the only available spatial representation of regionally or nationally
significant areas. For example, this is the case with the Auckland Park Extents dataset,
which currently serves as the only spatial representation of Auckland’s regional
parks we are aware of.

That said, we encourage administering bodies to enhance their existing parks and
reserves datasets by including information about the legal protection status of
each site. Adding relevant legislative and administrative details, such as the
Act and section under which an area is protected. This greatly improves PAN-NZ’s
ability to accurately classify and integrate local data into the national
protected areas layer.

<br>

### Lack of Legal Information 
Many local government parks and reserves datasets lack explicit information
about the legislation under which areas are protected. This lack of legal context
makes it difficult to categorise protections using recognised frameworks such as
the IUCN protected area categories.

Despite this, these datasets are still highly valuable. Most include spatial
boundaries and the names of protected areas, which are essential for mapping and
national completeness. PAN-NZ will include these areas in the national layer, even
if their legal basis is unclear. However, in such cases, we will not assign an
IUCN category.

Where possible, PAN-NZ may attempt to infer legislative context by
cross-referencing central government records and gazette notices. That said,
this approach is less reliable and not preferred, as it relies on secondary
interpretation rather than authoritative information from the administering
body.




<br>

## Regional Data Sources
---
The table below is the regional dataset catalogue. It includes the datasets we
are currently aware of, along with their known status. Some entries are
placeholders where we expect data to exist but have not yet identified it.
These gaps highlight areas where additional data is needed to support the
creation of a complete national protected areas dataset.

<div class="tip-box">
  <strong>Note:</strong> This catalogue is automatically rendered from 
  <a href="https://github.com/manaakiwhenua/PAN-NZ-data-catalogue-and-guidelines/blob/main/_data/regional_protected_areas.csv"> _data/regional_protected_areas.csv</a> .
</div>


<!-- <div class="tip-box">
  <strong>Contributing:</strong> Please see 
  <a href="{{ site.baseurl }}/contributing/index.html">Contribute / Contact</a> 
  for information on contributing and how you can update this table.
</div> -->


<div class="tip-box">
  <strong>Tip:</strong> Use the Fullscreen button to view the below table
</div>


{% include catalogue_table.html datafile="regional_protected_areas" %}


