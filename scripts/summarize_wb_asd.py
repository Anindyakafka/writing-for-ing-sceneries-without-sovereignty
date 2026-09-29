#!/usr/bin/env python3
"""Read the cleaned ASD CSV without modifying it; publish only aggregate checks."""
import argparse
from collections import Counter
import csv
import gzip
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--out", type=Path, default=Path("data/west-bengal/local-verification.json"))
    args = parser.parse_args()
    digest = hashlib.sha256()
    with args.input.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    domains = {
        "gender": {"female", "male", "other"},
        "relation_type": {"father", "mother", "husband", "wife", "other"},
        "uncollectable_reason": {"death", "permanently_shifted", "untraceable_or_absent", "already_enrolled"},
        "elector_name_status": {"observed", "destroyed_cid0_notdef", "source_blank"},
        "relation_name_status": {"observed", "destroyed_cid0_notdef", "source_blank"},
    }
    counts = {field: Counter() for field in domains}
    districts, acs, documents, affected = Counter(), set(), set(), set()
    errors = Counter()
    rows = missing_rows = missing_cells = age_outliers = 0
    current_document = None
    serials = set()
    numeric = ("source_page", "source_table", "source_row", "district_id", "ac_id", "part_id", "serial_number", "old_part_number", "old_serial_number", "age")
    with gzip.open(args.input, "rt", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames
        for row in reader:
            rows += 1
            document = row["document_id"]
            if document != current_document:
                errors["document_reappeared"] += int(document in documents)
                documents.add(document)
                current_document, serials = document, set()
            serial = row["serial_number"]
            errors["duplicate_document_serial"] += int(serial in serials)
            serials.add(serial)
            errors["invalid_record_id"] += int(row["record_id"] != f"{document}:{serial}")
            errors["missing_epic"] += int(not row["epic_number"].strip())
            for field in numeric:
                try:
                    int(row[field])
                except ValueError:
                    errors["invalid_numeric"] += 1
            for field, domain in domains.items():
                counts[field][row[field]] += 1
                errors["invalid_domain"] += int(row[field] not in domain)
            absent = 0
            for field in ("elector_name", "relation_name"):
                empty = not row[field].strip()
                absent += empty
                errors["name_status_mismatch"] += int(empty != (row[field + "_status"] != "observed"))
            missing_cells += absent
            if absent:
                missing_rows += 1
                affected.add(document)
            flag = int(row["age"]) > 120
            age_outliers += flag
            errors["age_flag_mismatch"] += int(row["age_above_120"] != str(int(flag)))
            districts[row["district_name"]] += 1
            acs.add(row["ac_id"])
            if rows % 1000000 == 0:
                print(f"Checked {rows:,} rows", flush=True)
    payload = {
        "verified_on": "2026-09-28", "input_file": args.input.name,
        "input_bytes": args.input.stat().st_size, "sha256": digest.hexdigest(),
        "method": "Full gzip CSV pass; document contiguity plus within-document key checks; no PDF re-extraction or final-roll linkage",
        "rows": rows, "columns": columns, "documents_with_rows": len(documents),
        "district_groups_with_rows": len(districts), "assembly_constituencies_with_rows": len(acs),
        "counts": {k: dict(v) for k, v in counts.items()},
        "district_record_counts": dict(sorted(districts.items())),
        "missing_name_cells": missing_cells, "rows_with_any_missing_name": missing_rows,
        "documents_with_missing_names": len(affected), "age_above_120_rows": age_outliers,
        "errors": dict(errors), "passed": not any(errors.values()) and rows == 5819543,
        "limits": ["No final deletion or targeting inference", "Document keys are not unique-person keys", "District counts have no electorate denominator", "Source damage classification inherited from upstream glyph audit"],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(f"Wrote {args.out}; passed={payload['passed']}")
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
