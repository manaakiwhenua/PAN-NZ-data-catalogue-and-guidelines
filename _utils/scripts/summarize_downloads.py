import json
from collections import Counter
from pathlib import Path


def read_status(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {
            "dataset_id": path.parent.name,
            "dataset_name": path.parent.name,
            "scope": path.parent.parent.name if path.parent.parent.name else None,
            "status": "invalid_status_file",
            "download_type": None,
            "records": 0,
            "output": [],
            "error": f"Could not read status file: {exc}",
            "status_file": str(path),
        }


def main():
    status_paths = [Path(p) for p in snakemake.input.statuses]
    output_path = Path(snakemake.output.report)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    items = []
    status_counts = Counter()
    type_counts = Counter()
    total_records = 0

    for status_path in status_paths:
        payload = read_status(status_path)
        payload["status_file"] = str(status_path)

        status = payload.get("status") or "unknown"
        download_type = payload.get("download_type") or "unknown"

        status_counts[status] += 1
        type_counts[download_type] += 1
        total_records += int(payload.get("records") or 0)

        items.append(payload)

    items.sort(
        key=lambda item: (
            (item.get("scope") or ""),
            (item.get("dataset_name") or ""),
        )
    )

    summary = {
        "total_datasets": len(items),
        "total_records_downloaded": total_records,
        "counts_by_status": dict(sorted(status_counts.items())),
        "counts_by_download_type": dict(sorted(type_counts.items())),
        "datasets": items,
    }

    output_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
