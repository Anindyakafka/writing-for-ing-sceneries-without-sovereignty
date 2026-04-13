#!/usr/bin/env python3
"""Generate quick profile summaries for downloaded censorboard CSV files."""

from __future__ import annotations

import argparse
import csv
import json
import pathlib
from collections import Counter
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Profile CSV files in a directory tree")
    parser.add_argument("--input", default="data/censorboard/raw", help="Root directory containing CSV files")
    parser.add_argument(
        "--output",
        default="data/censorboard/metadata/csv-profile.json",
        help="Output JSON profile path",
    )
    parser.add_argument("--sample", type=int, default=5000, help="Rows to sample for missing-value stats")
    return parser.parse_args()


def profile_csv(path: pathlib.Path, sample_size: int) -> dict[str, Any]:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []

        row_count = 0
        empty_counts = Counter({name: 0 for name in fieldnames})

        for row in reader:
            row_count += 1
            if row_count <= sample_size:
                for col in fieldnames:
                    val = row.get(col)
                    if val is None or str(val).strip() == "":
                        empty_counts[col] += 1

    missing_ratio = {}
    sampled = min(row_count, sample_size)
    for col in fieldnames:
        if sampled == 0:
            missing_ratio[col] = None
        else:
            missing_ratio[col] = round(empty_counts[col] / sampled, 4)

    return {
        "file": str(path).replace("\\", "/"),
        "rows": row_count,
        "columns": fieldnames,
        "column_count": len(fieldnames),
        "sample_rows_evaluated": sampled,
        "missing_ratio_in_sample": missing_ratio,
    }


def main() -> int:
    args = parse_args()
    input_root = pathlib.Path(args.input)
    output_path = pathlib.Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    csv_files = sorted(input_root.rglob("*.csv"))
    profiles = [profile_csv(file_path, args.sample) for file_path in csv_files]

    payload = {
        "input_root": str(input_root).replace("\\", "/"),
        "files_profiled": len(profiles),
        "profiles": profiles,
    }

    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Profile written: {output_path}")
    print(f"CSV files profiled: {len(profiles)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
