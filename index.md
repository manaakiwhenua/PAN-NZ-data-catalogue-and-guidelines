---
layout: default
title: PAN-NZ Dataset Catalogue
---

## PAN-NZ Protected Area Source Dataset

> This catalogue is automatically rendered from `_data/Parks_and_Reserves.csv`.

<table>
  <thead>
    <tr>
      <th>Custodian</th>
      <th>Dataset name</th>
      <th>License</th>
      <th>WebMap</th>
      <th>Download URL</th>
      <th>API Type</th>
      <th>API URL</th>
      <th>ID</th>
      <th>Name Field</th>
      <th>Legislation Act</th>
      <th>Legislation Section</th>
      <th>Protection Type</th>
      <th>Reserve Purpose</th>
      <th>Comment</th>
      <th>Stated Restrictions</th>
      <th>Action Required</th>
    </tr>
  </thead>
  <tbody>
  {% for item in site.data.Parks_and_Reserves %}
    <tr>
      <td>{{ item.Custodian }}</td>
      <td>{{ item["Dataset name"] }}</td>
      <td>{{ item.License }}</td>
      <td>{{ item.WebMap }}</td>
      <td>{{ item["Download URL"] }}</td>
      <td>{{ item["API Type"] }}</td>
      <td>{{ item["API URL"] }}</td>
      <td>{{ item.ID }}</td>
      <td>{{ item["Name Field"] }}</td>
      <td>{{ item["Legislation Act"] }}</td>
      <td>{{ item["Legislation Section"] }}</td>
      <td>{{ item["Protection Type"] }}</td>
      <td>{{ item["Reserve Purpose"] }}</td>
      <td>{{ item.Comment }}</td>
      <td>{{ item["Stated Restrictions"] }}</td>
      <td>{{ item["Action Required"] }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>