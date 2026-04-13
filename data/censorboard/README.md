# Censorboard Dataset Integration

This folder tracks integration of data from:
https://github.com/Anindyakafka/CensorBoard_records

The upstream repository stores major data and assets in GitHub Releases.
This repo keeps analysis code and selected local copies for writing workflows.

## Folder Layout

- raw/ : downloaded release assets (large files may be gitignored)
- processed/ : cleaned tables used by analysis and visualizations
- metadata/ : release manifests, checksums, and source notes

## Fetching Release Assets

Use the script in [scripts/fetch_censorboard_releases.py](../../scripts/fetch_censorboard_releases.py):

```bash
python scripts/fetch_censorboard_releases.py --owner Anindyakafka --repo CensorBoard_records --out data/censorboard/raw
```

Optional flags:

- --tag <release-tag> to fetch one release only
- --include "*.csv" "*.json" to download selected files
- --latest to fetch only the newest release

## Notes

- Always preserve source URL and tag for every downloaded file.
- Keep a manifest in metadata/release-manifest.json for reproducibility.
- For publication work, build final analysis tables inside processed/.

## Confirmed Upstream Releases (as of 13 Apr 2026)

- Tag: Data
	- data.csv
- Tag: Raw
	- categories.csv
	- imdb.csv
	- llm.csv
	- metadata.csv
	- modifications.csv
	- recent.csv

## Quick Profiling After Download

Use the profile script to generate schema and missingness summaries:

```bash
python scripts/profile_censorboard_csvs.py --input data/censorboard/raw --output data/censorboard/metadata/csv-profile.json
```
