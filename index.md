## Dataset Catalogue

---
layout: default
title: PAN-NZ Dataset Catalogue
---

## PAN-NZ Protected Area Source Dataset

> This catalogue is automatically rendered from the `DATA/Parks_and_Reserves.csv` file.

| Custodian | Dataset name | License | WebMap | Download URL | API Type | API URL | ID  | Name Field | Legislation Act | Legislation Section | Protection Type | Reserve Purpose | Comment | Stated Restrictions | Action Required |
| --------- | ------------ | ------- | ------ | ------------ | -------- | ------- | --- | ---------- | --------------- | ------------------- | --------------- | --------------- | ------- | ------------------- | --------------- |
{% for item in site.data.catalog %}
| {{ item.Custodian }}
| {{ item["Dataset name"] }}
| {{ item.License }}
| {{ item.WebMap }}
| {{ item["Download URL"] }}
| {{ item["API Type"] }}
| {{ item["API URL"] }}
| {{ item.ID }}
| {{ item["Name Field"] }}
| {{ item["Legislation Act"] }}
| {{ item["Legislation Section"] }}
| {{ item["Protection Type"] }}
| {{ item["Reserve Purpose"] }}
| {{ item.Comment }}
| {{ item["Stated Restrictions"] }}
| {{ item["Action Required"] }} |
{% endfor %}