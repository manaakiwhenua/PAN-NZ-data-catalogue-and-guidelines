import csv
import json
from pathlib import Path

REQUIRED_COLUMNS = [
    "Custodian code",
    "Custodian name",
    "Dataset type",
    "Dataset name",
    "License",
    "WebMap",
    "Download URL",
    "API Type",
    "API URL",
    "ID",
    "Name Field",
    "legislative act",
    "legislative section",
    "Protection Type",
    "Reserve Purpose",
    "Comment",
    "Stated Restrictions",
    "Action Required",
]

NULL_MARKERS = {"", "-"}


def normalise(value):
    if value is None:
        return None
    stripped = value.strip()
    if stripped in NULL_MARKERS:
        return None
    return stripped


def normalise_columns(columns):
    normalised = [((column or "").strip()) for column in columns]
    removed_trailing = 0

    while normalised and normalised[-1] == "":
        normalised.pop()
        removed_trailing += 1

    return normalised, removed_trailing


def validate_file(path: Path):
    file_errors = []
    file_warnings = []
    row_count = 0

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        raw_columns = reader.fieldnames or []
        actual_columns, removed_trailing = normalise_columns(raw_columns)

        if removed_trailing > 0:
            file_warnings.append(
                {
                    "type": "trailing_empty_columns_ignored",
                    "count": removed_trailing,
                }
            )

        if actual_columns != REQUIRED_COLUMNS:
            file_errors.append(
                {
                    "type": "schema_mismatch",
                    "expected": REQUIRED_COLUMNS,
                    "actual": raw_columns,
                    "actual_normalised": actual_columns,
                }
            )

        for _row in reader:
            row_count += 1

    return {
        "file": str(path),
        "rows": row_count,
        "errors": file_errors,
        "warnings": file_warnings,
    }


def main():
    csv_paths = [Path(p) for p in snakemake.input.csvs]
    output_path = Path(snakemake.output.report)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    report = {"files": [], "valid": True, "summary": {"errors": 0, "warnings": 0}}

    for csv_path in csv_paths:
        result = validate_file(csv_path)
        report["files"].append(result)
        report["summary"]["errors"] += len(result["errors"])
        report["summary"]["warnings"] += len(result["warnings"])

    report["valid"] = report["summary"]["errors"] == 0

    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    if not report["valid"]:
        print(report)
        raise ValueError(
            f"CSV schema validation failed with {report['summary']['errors']} error(s). See {output_path}."
        )


if __name__ == "__main__":
    main()
