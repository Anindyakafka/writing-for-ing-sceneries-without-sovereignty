# Censorboard Dataset Integration

## Review status — 28 September 2026

**Not yet cleared for publication.** Raw CSVs, a checksum manifest, and the exact historical streaming aggregation are absent. `real_computed_story_data.json` is preserved as a historical snapshot attributed to the upstream release, not a freshly reproduced analysis. The browser's former mock data is replaced with a clearly labelled adapter of that snapshot. Run `python scripts/prepare_reviewed_story_snapshot.py` to rebuild the adapter and descriptive observations.

All seven legacy SVGs are marked unverified; the governance pie and disparity bars additionally have invalid proportional encodings. See [the full review](../../research/notes/repository-review-2026-09-28.md) before reuse. Corrected selected-matrix action shares are deletion 94.26%, replacement 3.27%, insertion 2.47%; these do not establish population-wide action rates. Token frequencies describe modification text, not necessarily censored dialogue. Causal claims of hardening and language discrimination are unsupported by these aggregates alone.

The fetching/building instructions below describe the existing pipeline, which requires the schema, merge, denominator, duration, and reproducibility fixes recorded in the review before publication use.

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
