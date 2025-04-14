---
layout: default
title: PAN-NZ Dataset Catalogue
permalink: /parks_and_reserves_catalogue/
---

## PAN-NZ Protected Area Source Dataset

> This catalogue is automatically rendered from `_data/Parks_and_Reserves.csv`.

<style>
.scroll-sync-container {
  position: relative;
}

.scrollbar-top {
  overflow-x: auto;
  overflow-y: hidden;
  height: 16px;
  width: 100%;
  border-bottom: 1px solid #ccc;
  background: #f5f5f5;
}

.scrollbar-top::before {
  content: '';
  display: block;
  width: 2000px; /* Adjust to match or exceed table min-width */
  height: 1px;
}

.catalogue-table-container {
  overflow-x: auto;
  overflow-y: hidden;
  width: 100%;
}

/* Table styles */
table.catalogue {
  min-width: 2000px;
  border-collapse: collapse;
  font-size: 0.85rem;
  table-layout: fixed;
  width: 100%;
}

table.catalogue th,
table.catalogue td {
  border: 1px solid #ccc;
  padding: 8px;
  vertical-align: top;
  word-break: break-word;
  white-space: pre-wrap;
}

table.catalogue th {
  background-color: #f9f9f9;
  font-weight: bold;
  text-align: left;
  min-width: 100px;
  white-space: normal;
}

table.catalogue tr:nth-child(even) {
  background-color: #f6f6f6;
}

table.catalogue thead th {
  position: sticky;
  top: 0;
  background-color: #f9f9f9;
  z-index: 2;
}

/* Limit width for long-text columns */
table.catalogue td:nth-child(5),
table.catalogue td:nth-child(7),
table.catalogue td:nth-child(14),
table.catalogue td:nth-child(15),
table.catalogue td:nth-child(16) {
  max-width: 300px;
  overflow-wrap: break-word;
}

table.catalogue th:nth-child(4),
table.catalogue th:nth-child(5),
table.catalogue th:nth-child(6),
table.catalogue th:nth-child(7) {
  min-width: 120px;
}

.catalogue-table-container::-webkit-scrollbar {
  height: 12px;
}

.catalogue-table-container::-webkit-scrollbar-thumb {
  background-color: #ccc;
  border-radius: 6px;
}

.catalogue-table-container::-webkit-scrollbar-track {
  background-color: #f5f5f5;
}
</style>

<div class="scroll-sync-container">
  <div class="scrollbar-top"></div>
  <div class="catalogue-table-container">
    <table class="catalogue">
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
          <td>{% if item.WebMap %}<a href="{{ item.WebMap }}" target="_blank">Link</a>{% endif %}</td>
          <td>{% if item["Download URL"] %}<a href="{{ item["Download URL"] }}" target="_blank">Download</a>{% endif %}</td>
          <td>{{ item["API Type"] }}</td>
          <td>{% if item["API URL"] %}<a href="{{ item["API URL"] }}" target="_blank">API</a>{% endif %}</td>
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
  </div>
</div>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const topScroll = document.querySelector(".scrollbar-top");
    const tableScroll = document.querySelector(".catalogue-table-container");

    if (topScroll && tableScroll) {
      topScroll.addEventListener("scroll", () => {
        tableScroll.scrollLeft = topScroll.scrollLeft;
      });

      tableScroll.addEventListener("scroll", () => {
        topScroll.scrollLeft = tableScroll.scrollLeft;
      });
    }
  });
</script>
