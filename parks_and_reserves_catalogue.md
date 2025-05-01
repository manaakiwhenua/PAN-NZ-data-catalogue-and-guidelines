---
layout: default
title: Local Government Parks and Reserves Data Sources
permalink: /parks_and_reserves_catalogue/
---


This catalogue documents datasets that include protections on local government 
managed land. 

These datasets typically represent land set aside for conservation, 
recreation and amenity purposes, and may include:
* Reserves gazetted under the Reserves Act 1977
* Regional parks established under section 139 of the Local Government Act 2002
* Local purpose reserves managed by councils
* Other open space identified through district plans or long-term planning instruments

By cataloguing these datasets, PAN-NZ aims to improve visibility of locally protected areas, 
support national data aggregation, and enable clearer understanding of the different legal and 
administrative frameworks used to protect land at the local level.

If you are a data holder and your parks or reserves dataset is not yet listed, we encourage
you to contribute by following the instructions via 
the [Contribute / Contact]({{ site.baseurl }}/contributing/index.html) page. 

<br>

## Known Issues with Local Government Datasets
---
Many local government parks and reserves datasets lack explicit information about the legislation under 
which areas are protected. This missing legal context makes it difficult to categorise 
protections using recognised frameworks such as the IUCN protected area categories.

Despite this limitation, these datasets remain highly valuable. Most include spatial extents 
and area names, which are essential for mapping and analysis. These attributes allow the 
areas to be represented in the PAN-NZ national layer, even if their legal basis is unclear.

Where possible, PAN-NZ will attempt to attribute legislation to these areas by cross-referencing 
central government legal records and gazette notices. However, this method is not preferred as it can be error prone, 
and it relies on secondary interpretation rather than the authoritative source of truth (a dataset from the administering body).


<br>

## Suitability of Local Government Parks and Reserves Datasets
--- 
We acknowledge that some local government datasets were not developed with the intent of 
representing legally protected areas. For example, the Auckland Council Park Extents 
dataset states that its polygons reflect maintenance areas rather than legal boundaries,
 and that it does not indicate whether land is formally gazetted or protected under 
 legislation such as the Reserves Act 1977 or the Local Government Act 2002.

Despite these limitations, PAN-NZ may include such datasets where they provide the only 
available spatial representation of regionally or nationally significant areas. For example this is 
the case with the Auckland Parks dataset, which currently serves as the only spatial 
representation of Auckland’s regional parks we are aware of.

That said, we encourage administering bodies to enhance their existing parks and reserves 
datasets by including information about the legal protection status of each site. Adding 
relevant legislative and administrative details, such as the Act and section under which 
an area is protected. This greatly improves PAN-NZ’s ability to accurately classify and 
integrate local data into the national protected areas layer.


<br>

## Parks and Reserves Datasets
---

<div class="tip-box">
  <strong>Note:</strong> This catalogue is automatically rendered from 
  <a href="_data/Parks_and_Reserves.csv">TODO// Update link to csv once merged with master</a> .
</div>


<!-- <div class="tip-box">
  <strong>Contributing:</strong> Please see 
  <a href="{{ site.baseurl }}/contributing/index.html">Contribute / Contact</a> 
  for information on contributing and how you can update this table.
</div> -->


<div class="tip-box">
  <strong>Tip:</strong> Use the Fullscreen button to view the below table
</div>


{% include catalogue_table.html datafile="Parks_and_Reserves" %}

