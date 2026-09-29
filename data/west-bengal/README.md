# West Bengal evidence used in the essay

Reviewed 28 September 2026. Source: [Electoral-Rolls-West-Bengal-2002](https://github.com/Anindyakafka/Electoral-Rolls-West-Bengal-2002), pinned revision `f1cf680863b332acf91d84c8681848a8d07b6dcd`.

This folder holds a small upstream documentation/code snapshot and evidence metadata, **not the 5.8-million-row electoral dataset**. See [manifest.json](manifest.json) for source URLs and SHA-256 hashes. Upstream material retains its [MIT license](upstream/LICENSE); official documents retain their issuing authority's terms. The writing repository's CC license does not override these.

## Evidence currently available

| Measure | Upstream reported value | Meaning |
|---|---:|---|
| Inventoried PDFs | 80,655 | Source corpus, not all later SIR documents |
| Readable PDFs | 80,651 | Four zero-byte inputs remain documented |
| Extracted rows | 5,819,543 | Document/serial elector records; not a final deletion count |
| Missing name cells | 6,979 | Across elector and related-person fields |
| Records with a missing name | 3,874 | One or both fields affected |
| Affected documents | 3,092 | Documents containing those cells |
| CID-0 damaged cells | 6,924 | Cannot be recovered from those glyphs by OCR |
| Blank source cells | 55 | No characters in the source cell |

The record, category, document, and missing-name totals were independently confirmed by reading the entire local cleaned CSV on 28 September 2026. [Verification output](local-verification.json) records its SHA-256 hash, aggregate results, and checks; [copied upstream QA](local-qa/validation.json) agrees. The corpus inventory and explanation of glyph damage remain upstream findings: PDFs were not re-extracted. The [summary JSON](summary.json) records units and evidence status. The [category mapping](upstream/data/metadata/wb_2025_asd/category_mappings.csv) retains source-language labels.

| Recorded reason | Independently counted records | Share of extracted records |
|---|---:|---:|
| Death | 2,416,131 | 41.52% |
| Permanently shifted | 1,987,636 | 34.15% |
| Untraceable / absent | 1,277,521 | 21.95% |
| Already enrolled | 138,255 | 2.38% |

These are source classifications, not verified circumstances or final outcomes. [Figure and caption](../../assets/visuals/west-bengal/README.md).

The 2025 uncollectable-form reports concern the SIR 2026 draft stage. They are separate from the 2002 roll archive and from the final roll and later amendments. Sources: [official ASD page](https://ceowestbengal.wb.gov.in/asd_sir), [SIR portal](https://ceowestbengal.wb.gov.in/SIR), and [16 December press note](https://ceowestbengal.wb.gov.in/Downloads/SIR2026/SIR_PressNote/CEO%20PN_36_16.12.2025.pdf).

The press note's two exact totals differ by 5,820,899, **1,356 above the extracted count**. The reason remains unresolved. No zero-byte file or locality has been assigned that difference.

## Local input and next analysis

The public tree omits generated `removed_electors_clean.csv.gz`, `cleaning_qa.json`, and `validation.json`; the release listing saved in `releases.json` exposes raw archives, not standalone cleaned-data assets. The ZIP contents have not been inspected. The author supplied the local directory `C:\Users\anind\Electoral-Rolls-West-Bengal-2002\data\processed\wb_2025_asd`. Its cleaned gzip is 252,175,942 bytes and was read without modification. Reproduce the aggregate check with:

```powershell
python scripts/summarize_wb_asd.py 'C:\Users\anind\Electoral-Rolls-West-Bengal-2002\data\processed\wb_2025_asd\removed_electors_clean.csv.gz'
```

The full pass checked record keys with document contiguity, numeric conversion, category domains, EPIC completeness, name-status consistency, and age flags. It confirmed 24 source district groups, 294 ACs, 80,651 documents with rows, and one age above 120. District counts are saved for audit, not presented as exclusion rates. No PDF-level truth check or later-roll linkage was performed.

Keep personal identifiers out of the publication. No person-level religion/caste inference is needed. A spatial exclusion rate needs a comparable electorate denominator, a validated geographic crosswalk, and a clear procedural stage. A 2002–2025 match needs separate linkage validation. See the [full review](../../research/notes/repository-review-2026-09-28.md).
