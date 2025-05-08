---
layout: default
title: Protected Areas Network New Zealand (PAN-NZ) Data Improvement Project
# permalink: /
---

<br>

## Introduction 
---

The Ministry for the Environment (MfE) and Manaaki Whenua Landcare Research
(MWLR) are jointly developing the Protected Areas Network of New Zealand
(PAN-NZ), a national spatial dataset that provides a comprehensive and
up-to-date overview of protected areas across Aotearoa New Zealand. 

Although the PAN-NZ database has existed for over two decades, it has not been
publicly released since 2007. Past compilations were developed to support
specific projects and were assembled on an ad hoc basis, which limited their
accessibility, consistency, and long-term value. Most notably, previous versions
lacked full coverage, particularly for protections held by local authorities. 

This initiative seeks to address the key issues that have affected previous
releases of PAN-NZ, primarily the significant inefficiencies in combining the
many source datasets required to create a national-level view, and the
persistent data gaps resulting from missing information and limitations on data
sharing. 

This initiative aims to improve PAN-NZ to ensure regular updates, public
availability, and an authoritative dataset by: 
1. Developing data standards for protected areas. 
2. Enabling discovery and interpretation of protected area data through the
   cataloguing of datasets. 

The overarching goal is to enable an up-to-date national view of protections to
inform conservation planning, infrastructure planning, decision-making,
research, and progress tracking toward international commitments. 

<br>

## Use of GitHub
---
This site is hosted using [GitHub Pages](https://pages.github.com/) to support
transparency, collaboration, and rapid publishing. As the PAN-NZ standards and
dataset catalogues are still in draft form, GitHub provides a collaborative
environment where contributors can propose changes, raise issues, and suggest
improvements via GitHub
[issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)
and [pull
requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).
GitHub also acts as a central landing page for PAN-NZ, where updates, draft
guidance, and related materials can be easily published and shared. 

While this is not a full-featured data catalogue, it provides a lightweight and
scalable way to coordinate feedback and track progress. It also allows us to
manage contributions efficiently within current resource constraints. 

For details on how to contribute or provide feedback, please see the [Contribute
/ Contact]({{ site.baseurl }}/contributing/index.html) page. 

<br>

## Guidelines
---

As part of this initiative, we have developed a set of draft guidelines that
define the minimum requirements for protected area datasets to be included in
PAN-NZ. 

These guidelines are intended to reduce duplication and streamline integration.
They focus on making datasets easy to access, interpret, and incorporate into a
national view. We are not requiring rigid schema adoption. Instead, we
prioritise clear licensing, discoverability, and the presence of key attributes
that describe the protection. 

The guidelines outline: 
* The need for a clear and open licence (for example, Creative Commons
  Attribution 4.0) 
* Access methods such as downloadable files or API endpoints 
* A minimal metadata profile 
* Attributes that describe the protected area, including name, protection type,
  and legal basis (such as Act and section) 

The full draft guidelines are available here: [guidelines]({{ site.baseurl
  }}/guidelines/index.html) 
  
By aligning with these standards, dataset holders can ensure their information
  contributes meaningfully to a national understanding of protected areas. 


<br>

## Data Catalogues
---
The PAN-NZ data catalogues aim to identify and document all known protected area
datasets managed by central and local government, as well as by other
organisations such as community groups and NGOs. 

These catalogues are not limited to datasets already included in the national
layer. They also record datasets that are currently incomplete or not yet
eligible for inclusion. By cataloguing these sources, PAN-NZ supports
coordination and helps data holders understand what is already available and
where improvements may be needed. 

The catalogues serve several purposes: 
* Provide a clear picture of all datasets that describe protected areas across
  Aotearoa 
* Support the process of compiling a national protected areas dataset 
* Identify missing or incomplete datasets 
* Help data holders understand the steps required for inclusion 

We encourage all data holders to check the catalogue entries relevant to their
organisation. If your dataset is not yet included, or if updates are needed,
please contact the PAN-NZ team through the [Contribute / Contact]({{
site.baseurl }}/contributing/index.html) page. 

You can view the catalogues on the [data catalogues]({{ site.baseurl
}}/data_catalogues/index.html) page. 

<br>

## The Categorisation of Protections
---
To support a more consistent and useful national dataset, PAN-NZ aims to assign
each protected area an IUCN protection category, where the source information
allows. The IUCN framework is a widely recognised international standard that
describes the level and purpose of protection. Assigning IUCN categories helps
users compare protections across regions and supports applications such as
conservation planning, reporting, and biodiversity assessments. 

Where datasets include the legal act and section under which an area is
protected, PAN-NZ will use this information to determine the most appropriate
IUCN category. If this information is missing or unclear, the protection will
still be included in the national dataset but marked as unranked in the
protection category field. 

Including a protection rank allows users to filter the dataset based on the
strength of protection. For example, a user may choose to focus only on areas
that offer the highest level of legal protection to biodiversity, while others
may wish to see all sites regardless of rank. 

Alongside the main PAN-NZ workstreams, a parallel effort is underway to map New
Zealand's legislation to IUCN categories in a consistent and transparent way.
This work will help ensure that protections are classified accurately and
fairly. Further details about this mapping will be published as the project
progresses. 

 