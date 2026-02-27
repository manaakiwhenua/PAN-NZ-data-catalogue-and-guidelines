import json
import logging
import os
from pathlib import Path
import re

import geopandas as gpd
import requests
from dotenv import load_dotenv


def setup_logger(log_path: Path):
    logger = logging.getLogger("download_dataset")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    log_path.parent.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def resolve_url(raw_url: str, logger: logging.Logger):
    if not raw_url:
        return None

    def _replacement(match: re.Match):
        token = match.group(1).strip()
        if not token:
            return match.group(0)

        normalized = re.sub(r"[^A-Za-z0-9_]", "_", token).upper()
        value = os.getenv(token)
        if value is None:
            value = os.getenv(normalized)

        if value is None:
            logger.warning(
                "URL contains <%s> but no matching env var was found (tried '%s' and '%s'); leaving placeholder unchanged.",
                token,
                token,
                normalized,
            )
            return match.group(0)

        return value

    return re.sub(r"<([^>]+)>", _replacement, raw_url)


def has_unresolved_placeholder(url: str | None):
    if not url:
        return False
    return re.search(r"<[^>]+>", url) is not None


def parse_arcgis_crs(payload):
    crs_info = payload.get("crs") or {}
    props = crs_info.get("properties") or {}
    name = props.get("name")
    if name:
        return name
    return None


def ensure_crs(gdf: gpd.GeoDataFrame, fallback_crs: str):
    if gdf.crs is None:
        gdf = gdf.set_crs(fallback_crs, allow_override=True)
    return gdf


def download_arcgis_geojson(url: str, target_crs: str, logger: logging.Logger):
    query_url = url.rstrip("/")
    if not query_url.lower().endswith("/query"):
        query_url = f"{query_url}/query"

    session = requests.Session()
    all_features = []
    offset = 0
    page_size = 2000
    source_crs = None

    while True:
        params = {
            "where": "1=1",
            "outFields": "*",
            "f": "geojson",
            "resultOffset": offset,
            "resultRecordCount": page_size,
        }
        response = session.get(query_url, params=params, timeout=120)
        response.raise_for_status()

        payload = response.json()
        if "error" in payload:
            raise RuntimeError(f"ArcGIS error response: {payload['error']}")

        if source_crs is None:
            source_crs = parse_arcgis_crs(payload)

        features = payload.get("features", [])
        logger.info("ArcGIS page fetched: offset=%s count=%s", offset, len(features))

        if not features:
            break

        all_features.extend(features)

        if len(features) < page_size:
            break

        offset += len(features)

    if not all_features:
        raise RuntimeError("No features returned from ArcGIS REST endpoint.")

    gdf = gpd.GeoDataFrame.from_features(all_features)
    inferred_crs = source_crs or "EPSG:4326"
    gdf = ensure_crs(gdf, inferred_crs)
    return gdf.to_crs(target_crs)


def download_wfs(url: str, target_crs: str):
    gdf = gpd.read_file(url)
    gdf = ensure_crs(gdf, "EPSG:4326")
    return gdf.to_crs(target_crs)


def download_direct(url: str, target_crs: str, raw_file: Path, logger: logging.Logger):
    try:
        gdf = gpd.read_file(url)
        gdf = ensure_crs(gdf, "EPSG:4326")
        return gdf.to_crs(target_crs), None
    except Exception as spatial_error:
        logger.warning("Could not read as vector data (%s). Saving raw download.", spatial_error)
        response = requests.get(url, timeout=120)
        response.raise_for_status()
        raw_file.write_bytes(response.content)
        return None, raw_file


def write_status(path: Path, payload: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main():
    workflow_root = Path(__file__).resolve().parents[1]
    load_dotenv(workflow_root / ".env")

    entry = dict(snakemake.params.entry)
    target_crs = snakemake.params.target_crs

    status_path = Path(snakemake.output.status)
    log_path = Path(snakemake.log[0])
    out_dir = status_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    data_path = out_dir / "data.gpkg"
    raw_path = out_dir / "raw_download"

    logger = setup_logger(log_path)

    status = {
        "dataset_id": entry["id"],
        "dataset_name": entry["dataset_name"],
        "custodian_name": entry.get("custodian_name"),
        "scope": entry["scope"],
        "output_dir": str(out_dir),
        "status_file": str(status_path),
        "log_file": str(log_path),
        "status": "failed",
        "download_type": None,
        "records": 0,
        "output": [],
        "error": None,
    }

    try:
        api_type = (entry.get("api_type") or "").strip().lower()
        api_url = resolve_url(entry.get("api_url"), logger)
        download_url = resolve_url(entry.get("download_url"), logger)

        logger.info("Starting dataset: %s", entry["dataset_name"])
        logger.info("API type: %s", api_type or "(none)")

        gdf = None

        if "arcgis" in api_type:
            candidate_url = api_url or download_url
        elif "wfs" in api_type or "ogc" in api_type:
            candidate_url = api_url or download_url
        else:
            candidate_url = download_url or api_url

        if not candidate_url:
            status["status"] = "skipped"
            status["download_type"] = "arcgis-rest" if "arcgis" in api_type else "ogc-wfs" if ("wfs" in api_type or "ogc" in api_type) else "direct"
            status["error"] = "Skipped: no download URL available for this dataset row."
            logger.info(status["error"])
            write_status(status_path, status)
            return

        if has_unresolved_placeholder(candidate_url):
            status["status"] = "skipped"
            status["download_type"] = "arcgis-rest" if "arcgis" in api_type else "ogc-wfs" if ("wfs" in api_type or "ogc" in api_type) else "direct"
            status["error"] = "Skipped: URL still contains unresolved <TOKEN> placeholder(s)."
            logger.info(status["error"])
            write_status(status_path, status)
            return

        if "arcgis" in api_type:
            status["download_type"] = "arcgis-rest"
            gdf = download_arcgis_geojson(candidate_url, target_crs, logger)
        elif "wfs" in api_type or "ogc" in api_type:
            status["download_type"] = "ogc-wfs"
            gdf = download_wfs(candidate_url, target_crs)
        else:
            status["download_type"] = "direct"
            gdf, raw_file = download_direct(candidate_url, target_crs, raw_path, logger)
            if raw_file is not None:
                status["status"] = "partial"
                status["output"].append(str(raw_file))
                status["error"] = "Downloaded raw file but could not parse spatial vector data."

        if gdf is not None:
            if data_path.exists():
                data_path.unlink()
            gdf.to_file(data_path, layer="dataset", driver="GPKG")
            status["records"] = int(len(gdf))
            status["output"].append(str(data_path))
            if status["status"] != "partial":
                status["status"] = "success"

        if status["status"] == "failed":
            status["error"] = status["error"] or "No spatial data was downloaded."

    except Exception as exc:
        logger.exception("Dataset download failed.")
        status["status"] = "failed"
        status["error"] = str(exc)

    write_status(status_path, status)


if __name__ == "__main__":
    main()
