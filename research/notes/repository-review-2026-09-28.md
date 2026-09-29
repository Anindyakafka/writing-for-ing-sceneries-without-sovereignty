# Repository and evidence review — 28 September 2026

## Editorial outcome

The current manuscript is [Scenery as Weapon v2](../../drafts/essays/scenery-as-weapon-v2.md). It develops the existing five-part argument into continuous prose, grounds the West Bengal discussion in the completed upstream extraction, adds source notes, and removes unsupported targeting and causal claims. It is a complete draft for author review, not a declaration that every proposed empirical extension is finished.

The concept-note PDF was read in full. Its emphasis on land, language, shared care, and collective sovereignty informs the opening and conclusion. No co-contributor's argument has been invented from the contributor list. The v1 essay and all five expanded section drafts were read and preserved as historical material; they are superseded, not synchronized editing copies.

## Coverage of this review

Reviewed all original tracked substantive files: root README, plan, log, license, concept note, bibliography, data documentation, main and section drafts, three Python scripts, three processed JSON files, the HTML visual, and all seven SVGs (source, labels, and numerical encodings). Empty `.gitkeep` files only establish intended folders. No local AGENTS.md was found. The initial working tree was clean.

The concept note was extracted with PyMuPDF. JSON was parsed and SVG text/geometry inspected. No browser rendering of the legacy HTML or print proof was performed. No underlying CBFC CSVs were present. After the author supplied the WB local-data path, the entire cleaned gzip was read in place and aggregate checks saved. No PDF extraction was rerun.

## West Bengal: what changed

- Upstream revision inspected: `f1cf680863b332acf91d84c8681848a8d07b6dcd`.
- The August 23 upstream log reports completed extraction, cleaning, and independent validation of **5,819,543 rows**; this supersedes April's proposed extraction workflow.
- Distinguish the **2002 historical roll project**, **2025 ASD source reports for SIR 2026**, and **later final/supplementary/deletion rolls**. The cleaned file's `removed_electors` filename does not determine the legal status of each record.
- The 2025 reports have extractable text and geometric tables; the older blanket OCR proposal is inappropriate for that corpus. Geometry matters for Bengali combining marks.
- Source inventory: 80,655 PDFs; 80,651 readable; four zero-byte sources in Mekliganj, AC 1, parts 129, 130, 132, 133. Missing files are not zero affected electors.
- Missing names: 6,979 **cells**, 3,874 **records**, 3,092 **documents**. Fields: 3,435 elector names plus 3,544 relation names. Conditions: 6,924 CID-0/.notdef cells plus 55 blank cells. The damaged-cell counts must not be presented as missing-person counts or intent.
- The 24 district folders are source administrative groupings, including Kolkata North and South; `district_id` is a directory prefix, not an official geographic join code.
- The official December press note's difference is 5,820,899, leaving **1,356** relative to the extraction. Cause unresolved; do not attribute the difference to the four empty PDFs or call it an error rate.
- No denominator-adjusted district/AC comparison, record linkage to 2002, community targeting estimate, or final-disposition analysis has been completed here.

The public tree and listed release assets did not expose `removed_electors_clean.csv.gz`, `cleaning_qa.json`, or `validation.json` as standalone downloads at review time. Raw ZIP releases are large; their contents were not downloaded or exhaustively searched. The author then supplied the local processed-data path, resolving access for this review.

### Independent full-file check completed

Read all 5,819,543 rows from the 252,175,942-byte cleaned gzip without modifying it. SHA-256: `98e2406644f0d97cae537f6cb656b90e2849294e9cf29415ad89cff240c7894c`. [Output](../../data/west-bengal/local-verification.json) confirms document/serial uniqueness, contiguity, EPIC completeness, numeric conversion, category domains, name-status consistency, and age-flag consistency. All checks passed; aggregate values agree with copied upstream cleaning and validation QA.

Recorded reasons: death 2,416,131; permanently shifted 1,987,636; untraceable/absent 1,277,521; already enrolled 138,255. Missing-cell/record/document counts also reconcile with upstream summaries. A new [figure and caption](../../assets/visuals/west-bengal/README.md) use these verified counts. No individual records were copied into the manuscript or chart. PDF source correctness and administrative reasons were not independently revalidated.

## Censorboard: findings and disposition

| Finding | Consequence / action |
|---|---|
| `story_data.json` was `preview_mock`, including invented politically charged token counts | Browser preview changed to the existing saved aggregate, explicitly labelled provisional; mock values removed from the active file. |
| Saved aggregate claims a streaming computation, but that exact program, checksums, raw CSVs, and run manifest are absent | Preserve the historical snapshot. Do not promote it to newly verified evidence. Numerical CBFC claims excluded from v2. |
| Matrix sums to 105,544; deletion 99,490; replacement **3,449**; insertion **2,605** | Shares are **94.26%, 3.27%, 2.47%**. Old 3.14% / 2.59% labels were wrong and are corrected. These are selected matrix counts, not proven unique cuts. |
| `other` contributes 85,865 of the 105,544 displayed matrix counts | The smaller named categories do not establish dominant themes across the archive. |
| 2021 comparison is observational; sample composition and coverage unknown | “Regulatory hardening” inference withdrawn. Descriptive change is retained only as a provisional snapshot observation. |
| Language ratios lack case-mix adjustment and denominator validation | No discrimination inference. Certificate counts and archive coverage matter. |
| Tokens come from descriptions, not necessarily censored dialogue | Rename browser panel accordingly; withdraw claims that selected counts prove institutional persistence or absence of justification. |
| Governance pie geometry does not encode the labelled proportions; disparity bars do not share a consistent scale | Both legacy plates are marked withdrawn pending regeneration. All original print SVGs are visibly marked as legacy/unverified. |
| Yearly graphic has an intensity line without a numerical right axis; static scales are approximate | Not cleared for print; require regenerated figures with explicit units and denominators. |
| Heatmap omits `other`; blank cells are ambiguous | Rebuild with explicit selection and missing/zero distinction before publication. |

### Pipeline issues to resolve before recomputation

`build_censorboard_story_data.py` selects a tag directory alphabetically, not chronologically. With `Data` and `Raw`, it may bypass the purported preferred processed input. Missing `cut_no` still causes a pandas named-aggregation failure despite the conditional inside its lambda. Missing IDs are silently set to `unknown`, collapsing denominators. The metadata/modification merge lacks key/cardinality checks; starting with modifications omits certificates with no modification rows. Certificate-level totals could be multiplied if processed rows repeat them. Date parsing and time notation need source-schema validation; unknown durations become zero, and the parser accepts ambiguous decimal minute/second strings. English-only tokenization and top-N truncation constrain interpretation. Multi-label co-occurrence counts are not unique interventions.

`fetch_censorboard_releases.py` reads downloads wholly into memory, has no pagination/checksum verification or retry/timeout policy, and overwrites its manifest per invocation. Failed/empty selections can still end successfully. It assumes trusted release names as filesystem paths. Use explicit assets, validated paths, checksums, and a retained manifest before relying on a new run.

`profile_censorboard_csvs.py` reports missingness for the first N rows, not a random sample or entire dataset, while counting all rows. Its output must retain that distinction. Empty input currently yields an apparently successful empty profile. The original pipeline has no dependency file or automated tests; this revision adds a separate plotting requirements file for the new WB figure.

These scripts were reviewed, not broadly rewritten: their proper correction depends on obtaining the actual upstream schemas and choosing the publication analysis. The visual-data adapter added in this revision does not claim to repair or reproduce the original aggregation.

## What is needed to finish

1. **Author / editor:** review v2's voice, title, length, submission deadline, citation style, and print/digital requirements. The concept note does not settle these.
2. **WB data access — completed for the cleaned output:** author supplied the CSV and final cleaning/validation QA; full-file checks and hashing completed. A separately published cleaned-data asset would improve reader reproducibility. Source PDFs/manifest remain upstream for any future re-extraction.
3. **WB empirical extension, if desired:** reconcile the 1,356 difference; acquire date-matched electorate denominators and a geography crosswalk; follow claims/final outcomes before stating final exclusions. Do not infer religion/caste from names. This extension is not required for the present archive-focused argument, but is required for the earlier proposed targeting claims.
4. **Grounded testimony:** a locality vignette needs real reporting/interviews, consent, source checking, and the opportunity for the person concerned to correct identifying details. No vignette was fabricated.
5. **CBFC:** obtain pinned inputs and reproduce a denominator-aware analysis; validate action coding/duration semantics; close-read selected modification records. Only then introduce quantitative comparisons or a new empirical print plate.
6. **Production:** Bengali copyedit, author pass, source-note format, figure selection/size, accessibility and actual visual proof. No submission or publication has occurred.

Optional article ideas and poetry folders remain available. They are not unfinished sections of the chosen essay.

## Verification completed

- Independent full cleaned-WB-file pass and equality checks against upstream QA; aggregate district and category sums reconcile.
- SHA-256 verification of the saved upstream snapshot and official PDF; source CSV hash retained separately.
- All repository JSON parsed, all SVG XML parsed, and local Python scripts passed syntax parsing.
- Current local Markdown links and v2 footnote references/definitions checked. Upstream snapshot links retain upstream semantics and were excluded from the local link check.
- New WB PNG visually inspected; SVG/PDF exports generated from the same plotted data. Legacy CBFC browser rendering was not tested.
- Git whitespace check passed after normalizing generated files' line endings. No full CBFC extraction, source-level WB re-audit, or publication submission is implied by these checks.
