---
layout: default
title: Protected Areas Network New Zealand (PAN-NZ) Data Improvement Project
# permalink: /
---

<br>

## Introduction 
---

The Ministry for the Environment (MfE) and Manaaki Whenua Landcare Research (MWLR)
are jointly developing the Protected Areas Network of New Zealand (PAN-NZ), 
a national spatial dataset that provides a comprehensive and up-to-date 
overview of protected areas across Aotearoa New Zealand.

Although the PAN-NZ database has existed for over two decades, it has not 
been publicly released since 2007. Past compilations were created on an 
ad hoc basis to support specific projects, limiting accessibility and 
long-term utility. More importantly, previous versions consistently 
lacked comprehensive coverage, especially of locally held protections.

This initiative seeks to address the key issues that have affected previous 
releases of PAN-NZ, primarily the significant inefficiencies in combining 
the many source datasets required to create a national-level view, and the 
persistent data gaps resulting from missing information and limitations on data sharing.

This initiative aims to improve PAN-NZ to ensure regular updates, public availability, and an authoritative dataset by:
1. Developing data standards for protected areas.
2. Enabling discovery and interpretation of protected area data through the cataloguing of datasets.

The overarching goal is to enable an up-to-date national picture of protections to inform conservation 
planning, decision-making, research, and progress tracking toward international 
commitments such as the “30 by 30” biodiversity target.

<br>

## Use of GitHub
---
This site is hosted using [GitHub Pages](https://pages.github.com/) to support transparency, 
collaboration, and rapid deployment. As the PAN-NZ standards and dataset catalogues are 
still in draft form, GitHub provides a collaborative environment where contributors can 
propose changes, raise issues, and suggest improvements via GitHub [issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) and
[pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests). As well as this, it creates a landing page for PAN-NZ where 
information about upcoming releases and other details can be easily added.

While this is not a full-featured data catalogue, it represents a practical and 
scalable starting point within current resource constraints. Crucially, GitHub provides the tools
to foster collaboration.

For more details on contributing and providing feedback, please visit 
the [Contribute / Contact]({{ site.baseurl }}/contributing/index.html) page. 


<br>

## Guidelines
---
As part of this initiative, guidelines have been developed to define the minimum requirements 
that protected area datasets must meet to be included in the PAN-NZ national view of legal protections.

These draft guidelines can be found on the [guidelines]({{ site.baseurl }}/guidelines/index.html) page.


<br>

## Data Catalogues
---
The data catalogues aim to capture all protected area datasets held by central and local government, 
as well as other administering bodies such as not-for-profit organisations. The objective of these catalogues 
is to create a comprehensive view of all protected area datasets and their status. 

These catalogues serve several purposes:
* Support the aggregation of a national protected areas dataset by 
  outlining available data and its current status.
* Identify datasets not yet eligible for inclusion in PAN-NZ 
  and detail the steps data holders can take to make them suitable.

For more on these catalogues, please visit the
[data catalogues]({{ site.baseurl }}/data_catalogues/index.html) page.

<br>

## The Categorisation of Protections
---
As part of PAN-NZ, we aim to support more meaningful analysis and 
filtering of protected areas by assigning each record an IUCN protection 
category, where possible. The International Union for Conservation of Nature
(IUCN) framework is widely used to describe the degree and purpose of protection.
This allows for consistency across international datasets and supports a range
of user needs, including conservation planning and policy reporting.

To achieve this, PAN-NZ will attempt to map each protected area to an IUCN category
based on the legal mechanism under which the protection is established. However, 
where source datasets do not include sufficient legislative detail, we will not
be able to confidently assign an IUCN category. These records will still be 
included in the PAN-NZ dataset but will be marked as unranked in the protection category field.

Including a protection rank is important because it allows users to filter protected areas based on 
the degree of protection afforded to biodiversity. This allows us to include protections in 
PAN-NZ that may only afford a low level of protection while allowing users to 
exclude these if they are not relevant to their needs. 

In parallel with this work (guidelines and the cataloguing of source data), 
a separate project is underway to describe how New Zealand’s legislation maps to 
the IUCN protected area categories. More details about this process will be made 
available in future updates.