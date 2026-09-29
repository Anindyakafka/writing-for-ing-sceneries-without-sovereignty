# PROJECT LOG — Writing for …ing: Sceneries without sovereignty

Chronological log of work sessions on this repository. Oldest entries first.

**Current entry:** Session 013, below. Earlier claims of “real computed” or “publication-ready” imagery record historical work and are qualified by the September evidence review.

---

## Session 001 — 13 April 2026

**Initiated repository.**

- Read the full concept note for *"…ing: Sceneries Without Sovereignty"* (JINN + Nabarun Publication)
- Created repository structure: `drafts/`, `research/`, `data/`, `assets/`
- Wrote `README.md` with publication context, repo structure, themes, and license note
- Added `PROJECT_LOG.md` (this file)
- Added `LICENSE` — CC BY-NC-SA 4.0
- Created `PLAN.md` — initial writing plan outlining potential contributions and data linkage strategy
- Created `data/README.md` — placeholder for linking external data repos
- Created `research/sources.md` — initial bibliography and source tracking file

**Intentions set this session:**
- Write for the publication as both a political and intellectual commitment
- Bring data into the publication's terrain — land acquisition, language, labour, ecology, violence — not as neutral evidence but as contested record
- Plan at least one data-driven long-form article and one poem/short essay
- Link data from separate repositories into `data/` as the work develops

---

## Session 002 — 13 April 2026

**Chose writing direction and visualization stack.**

- Confirmed primary writing direction: Option C (essay) — *Scenery as Weapon*
- Reviewed feasibility of building publication visuals with JavaScript + D3
- Decided to prepare a D3-first visual approach for expressive, publication-grade figures
- Planned next execution step: create a reusable D3 visual scaffold in `assets/visuals/` and connect first chart to curated dataset

**Intentions set this session:**
- Pair essay writing with one strong, publication-ready visual narrative
- Use D3 for design-led storytelling (layout, typography, transitions), not only default charts
- Keep source data traceable and documented in `data/README.md`

---

## Session 003 — 13 April 2026

**Started active writing for Option C.**

- Created first essay draft: `drafts/essays/scenery-as-weapon-v1.md`
- Integrated new political data directions into writing frame:
	- 2002 WB electoral roll (Bengali scanned PDFs)
	- 2026 WB voter deletion records
	- Rare film censorboard decision data
- Updated `PLAN.md` with OCR-to-structured-data workflow and D3-first visual strategy

**Intentions set this session:**
- Expand essay with grounded locality vignette once deletion parsing is validated
- Build first D3 companion visual after censorboard repository review
- Keep analysis auditable with page-level references from scanned sources

---

## Session 004 — 13 April 2026

**Corrected contribution framing.**

- Updated planning language to clearly position writing role as collaborator
- Replaced "Primary Contribution" framing with "Collaborative Contribution" in `PLAN.md`

**Intentions set this session:**
- Keep all future drafts and metadata aligned with collaborator role in the publication

---

## Session 005 — 13 April 2026

**Expanded essay into section folders and prepared censorboard ingestion code.**

- Split `scenery-as-weapon` essay into heading-wise folders with expanded drafts
- Added section workspace at `drafts/essays/scenery-as-weapon-sections/`
- Added local censorboard integration path under `data/censorboard/`
- Added script `scripts/fetch_censorboard_releases.py` to download release assets from `Anindyakafka/CensorBoard_records`
- Updated `data/README.md` to register the censorboard source repo

**Intentions set this session:**
- Use section files for deep edits before reconciling back into one essay draft
- Start dataset profiling immediately after first release fetch

---

## Session 006 — 13 April 2026

**Operationalized censorboard repository integration.**

- Confirmed upstream release structure for `Anindyakafka/CensorBoard_records` (tags: `Data`, `Raw`)
- Documented known release assets in `data/censorboard/README.md`
- Added `scripts/profile_censorboard_csvs.py` to produce quick schema and missingness summaries after download

**Intentions set this session:**
- Download selected CSV assets first (`metadata.csv`, `modifications.csv`, `data.csv`) for rapid theme mapping
- Use profiling output to design first D3 visual narrative around censorship pattern clusters

---

## Session 007 — 13 April 2026

**Built first narrative visualization pipeline for censorboard data.**

- Reviewed upstream censorboard pipeline/schema signals (raw + processed datasets)
- Added `scripts/build_censorboard_story_data.py` to generate D3-ready narrative aggregates
- Added first publication-style D3 view at `assets/visuals/censorboard/story.html`
- Encoded three core panels for political storytelling:
	- Yearly censorship pressure (volume + intensity)
	- Language burden (modified seconds per certificate)
	- Action x content matrix (recurring censorship logic)

**Intentions set this session:**
- Download release CSVs and run story-data builder
- Tune panel annotations after seeing live distributions
- Add a fourth panel on recurring censored terms over time if text quality permits

---

## Session 008 — 13 April 2026

**Extended visual narrative depth with textual pattern panel.**

- Added fourth D3 panel to `assets/visuals/censorboard/story.html` for recurring censored lexicon by year
- Aligned panel with publication narrative: not just volume of cuts, but language of regulation over time

**Intentions set this session:**
- Validate token quality and stopword filters once full CSV assets are loaded
- Annotate key years/spikes directly in visual copy for publication use

---

## Session 009 — 13 April 2026

**Ran first visual preview in browser.**

- Added `data/censorboard/processed/story_data.json` with preview mock values so all D3 panels render
- Opened `assets/visuals/censorboard/story.html` in integrated browser for immediate graph preview

**Intentions set this session:**
- Replace preview mock with real release-derived aggregates once local CSV fetch is executed

---

## Session 010 — 13 April 2026

**Switched from preview to real computed print imagery.**

- Computed aggregates from real release files (`metadata.csv`, `modifications.csv`) via streaming pipeline
- Saved computed dataset snapshot at `data/censorboard/processed/real_computed_story_data.json`
- Generated print-focused static SVG visuals (no HTML dependency):
	- `assets/visuals/censorboard/print/cbfc_yearly_censorship_pressure.svg`
	- `assets/visuals/censorboard/print/cbfc_language_burden.svg`
	- `assets/visuals/censorboard/print/cbfc_action_content_heatmap.svg`
	- `assets/visuals/censorboard/print/cbfc_regulatory_lexicon_lines.svg`

**Intentions set this session:**
- Iterate typography, annotation density, and panel hierarchy for book-layout compatibility
- Export publication variants (CMYK-ready or editor-specified dimensions) if required

---

## Session 011 — 13 April 2026

**Shifted from descriptive plots to inference-led visual argument.**

- Derived observation metrics from computed data and saved at `data/censorboard/processed/inferred_observations.json`
- Added three narrative print plates focused on interpretation:
	- `assets/visuals/censorboard/print/cbfc_narrative_rupture_plate.svg`
	- `assets/visuals/censorboard/print/cbfc_narrative_governance_mode.svg`
	- `assets/visuals/censorboard/print/cbfc_narrative_disparity_lexicon.svg`
- Framed visual claims around rupture (2021 hardening), subtractive governance (deletion dominance), and procedural lexicon persistence

**Intentions set this session:**
- Tighten language-specific caution notes and sample-size caveats for publication ethics
- Prepare alternate minimalist versions for page-constrained print layouts

---

## Session 012 — 28 September 2026

**Reviewed the repository and completed a revised full essay with updated WB evidence.**

- Read the concept note, all essay drafts, project documentation, scripts, saved datasets, and visual sources. Recorded findings in `research/notes/repository-review-2026-09-28.md`.
- Wrote `drafts/essays/scenery-as-weapon-v2.md`: approximately 2,260 words before source notes, retaining the five-part structure and replacing proposed WB extraction with actual findings. Older drafts remain labelled historical.
- Retrieved upstream WB documentation and analysis code at `f1cf680863b332acf91d84c8681848a8d07b6dcd`; retained its license, source URLs, hashes, release metadata, and the official December 16 press note.
- The author supplied `C:\Users\anind\Electoral-Rolls-West-Bengal-2002\data\processed\wb_2025_asd`. Read its 252,175,942-byte cleaned gzip without modification. Independently checked all 5,819,543 rows, record keys, category domains, numeric fields, EPIC completeness, missing-name statuses, and age flags. All checks passed and agree with upstream QA. No PDF re-extraction or final-roll linkage was performed.
- Added a reusable aggregate verification script and saved aggregate-only results. Verified reason counts and the distinction between 6,979 missing name cells and 3,874 affected records. Recorded the unresolved 1,356 difference from official enumeration totals.
- Generated a new WB recorded-reasons figure in SVG, PDF, and PNG with source notes and alt text; visually reviewed the PNG. Kept administrative categories distinct from verified circumstances and final deletion outcomes.
- Replaced active CBFC mock values with an explicitly provisional adapter of the historical saved aggregate. Corrected action-share arithmetic; withdrew causal interpretations; marked all legacy print SVGs unverified and documented invalid proportional encodings. The underlying CBFC source computation remains unreplicated.
- Updated root/data/section READMEs, plan, and sources to identify the current manuscript, verified work, and remaining editorial/evidence tasks.

**Remaining:** author/editor review, Bengali copyedit, publication specifications; WB reconciliation and later outcomes if pursued; CBFC source reproduction and validated figures before quantitative claims. No files in the source data repository were edited. No submission, commit, or publication was performed.

---

## Session 013 ? 29 September 2026

**Incorporated the supplied editorial critique in a new final draft.**

- Added `drafts/final/scenery-as-weapon-v3.md`, approximately 1,830 words before notes; left v1 and v2 unchanged.
- Opened with the damaged name cell; brought residence, land, and ongoing revision into the argument; retained the uncollectable/failed-encounter observation and the final sentence.
- Consolidated evidence limits, addressed the death-category counterargument, and grounded the practical burden of seeking inclusion in the official December instructions, acknowledging official assistance.
- Reduced film to one paragraph and removed the unmatched 2002 comparison from the manuscript. Used an explicitly marked Bengali lexical reading rather than invented testimony.
- Moved technical abbreviations, hashes, local paths, audit counts, and claim boundaries into `research/notes/scenery-as-weapon-v3-methods.md`; retained readable public citations in the essay.
- Updated the main README, active plan, and final/section draft navigation. No datasets or figures were changed and no new empirical results are claimed.
- Checked manuscript figures against the saved verification, footnote references, local navigation, and absence of repository scaffolding in the manuscript.

**Remaining:** author's voice pass, Bengali copyedit, editorial word limit and notes/figure decisions. No submission or publication.
