# `_utils` spatial download workflow

This directory contains a Snakemake workflow that:

1. validates schema for all CSV files in `_data/`
2. downloads each dataset row if possible
3. handles ArcGIS REST (with pagination), OGC WFS, and direct links
4. transforms spatial data to a target CRS
5. writes dataset-level logs and status files next to outputs

## Expected CSV schema

All `_data/*.csv` files must use this exact header schema:

- Custodian code
- Custodian name
- Dataset type
- Dataset name
- License
- WebMap
- Download URL
- API Type
- API URL
- ID
- Name Field
- legislative act
- legislative section
- Protection Type
- Reserve Purpose
- Comment
- Stated Restrictions
- Action Required

Null values may be represented as `-` or empty.

## Setup

From `_utils/`:

1. Create the conda environment:

   ```bash
   conda env create -f envs/workflow.yml
   conda activate pan-nz-download-workflow
   ```

2. Create `_utils/.env` and set required keys, for example:

   ```env
   API_KEY=your_api_key_here
   LINZ_KEY=your_linz_key_here
   ```

   Any URL placeholder in angle brackets is resolved at runtime.
   Example: `<API_KEY>` uses `API_KEY`, `<LINZ_KEY>` uses `LINZ_KEY`.
   If a placeholder token includes non-alphanumeric characters, it is also
   tried as an uppercased, underscore-normalized env var name.

## Run

From `_utils/`:

```bash
snakemake --use-conda --cores 4
```

## Outputs

- Validation report: `_utils/logs/schema_validation.json`
- Download summary report: `_utils/logs/download_summary.json`
- Downloads:
   - `_utils/downloads/National/<custodian_name>/<dataset_slug>/...`
   - `_utils/downloads/Regional/<custodian_name>/<dataset_slug>/...`

Each dataset folder contains:

- `download.log`
- `status.json`
- `data.gpkg` when spatial download/parsing succeeds
- `raw_download` when only raw bytes could be downloaded

## Notes

- ArcGIS REST uses paged requests (`resultOffset` / `resultRecordCount`).
- Target CRS is configured in `_utils/config.yaml` (`target_crs`, default `EPSG:2193`).
- Placeholders are generic (`<TOKEN>`) and are substituted from `_utils/.env`.
