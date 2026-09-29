# PLAN — Writing for …ing: Sceneries without sovereignty

Working plan for contributions to *"…ing: Sceneries Without Sovereignty"* (JINN + Nabarun Publication).

## Active plan — 29 September 2026

The selected contribution is **Scenery as Weapon**. The [final draft v3](drafts/final/scenery-as-weapon-v3.md), [methods/editorial note](research/notes/scenery-as-weapon-v3-methods.md), and [repository review](research/notes/repository-review-2026-09-28.md) supersede the exploratory plan below. V3 incorporates the supplied critique and makes the electoral archive the essay's centre; CBFC remains a one-paragraph analogy, and the unmatched 2002 comparison is omitted.

1. Author reviews the manuscript's voice and scope; confirm editorial length/deadline and citation requirements.
2. Completed: obtained read access to the author's local WB cleaned CSV and final QA, checked all 5,819,543 rows, and produced aggregate reason counts and a figure. Remaining: reconcile the 1,356 difference from official enumeration totals.
3. Keep 2002 archival linkage, 2025 ASD extraction, and later 2026 dispositions distinct. The 2025 extraction is complete upstream and uses geometric text extraction, not blanket OCR.
4. Only add targeting/outcome analysis with comparable denominators, validated geography/linkage, and substantive evidence. Do not infer individual religion/caste from names.
5. Reproduce CBFC analysis with validated input semantics before using quantitative figures. Legacy print plates are withheld; the active browser preview is explicitly provisional.
6. Complete Bengali copyedit, source check, and production proof before submission.

**Historical brainstorming follows.** Alternative articles, unvalidated hypotheses, the generic 95% OCR target, and the previous proposed “2026 voter-deletion” workflow below are retained for history and are not the active evidence standard or current task list.

---

## What I Understand About This Publication

This is not an exhibition catalogue — it is a **political continuation**. The publication:
- Starts from the position that land is shaped by labour, memory, ecology, and struggle
- Argues that language grows from land — and is severed from it by colonialism, caste, capitalism, nationalism
- Challenges state sovereignty by surfacing **subaltern sovereignties** (commons, customary law, collective labour)
- Uses multilingual form as political commitment, not aesthetic choice
- Is **crowdfunded** to remain independent
- Contributors span South Asia, West Asia, Latin America, Southeast Asia, Africa, Europe, North America

The "-ing" in the title = **ongoing processes**: enclosing, extracting, mapping, demolishing, erasing — not history, but live operations.

---

## What I Can Contribute

### 1. Data-Driven Long-Form Article (Collaborative Contribution)

**Possible angle:** *The Cartography of Eviction — What demolition data tells us about who the city is for*

- Use data on targeted demolitions (Delhi, Mumbai, other cities) to map the political logic of destruction
- Combine with SRA data, bulldozer orders, legal challenges
- Argue that data itself is a battleground — what gets counted, what disappears from the record
- Cross-link with co-contributors: Sucheta De (AICCTU, demolitions in Delhi), Shivangi Mariam Raj (debris and urban absence), Artitra Bhattacharya (SRA, Mumbai)

**Alternative angle:** *Language as Land: What the Census hides*
- Use mother tongue data to map the erasure of minority languages under Hindi/English administrative hegemony
- Link to Moumita Alam (Kamtapuri/Rajbanshi), Mushtaq Ahmad Bhagat (Kashmiri), Bhaskar Hazarika (Assam/translation politics)

**Alternative angle:** *Numbers on the Ground: Mapping farmers' movements through data*
- Deaths in farmers' movements, UAPA charges against activists, land acquisition cases
- Link to Malay Tiwari (Tebhaga to contemporary farmers' movements), KR Shiyas (land struggles, Kerala)

---

### 2. Essay (Collaborative Essay Contribution)

**Possible angle:** *Scenery as Weapon: How aesthetics and conservation erase political life*
- A shorter, reflective piece on how landscape representation (nature photography, heritage tourism, environmental conservation) functions to de-politicise land — producing the "sceneries without sovereignty" the publication names
- Draw from visual analysis and data on forest rights rejection / conservation-driven displacement
- Personal and analytical in tone

---

### 3. Poem (Optional — if it comes)

Not planned — but left open. If a poem emerges from  the research or the writing, it goes in `drafts/poems/`.

---

## Data Linkage Plan

| Writing Piece | Data Needed | Source Repos / Datasets |
|---------------|-------------|------------------------|
| Demolition article | Targeted demolition records, SRA data, bulldozer orders | External repo TBD |
| Language article | Census mother tongue data, PLSI | Census 2011 (language tables), Devy/PLSI |
| Farmers' movement article | UAPA data, land acquisition cases, protest deaths | External repo TBD |
| Scenery essay | Forest rights rejection rate, conservation displacement | MoTA reports, WII data |

### High-Priority Rare Data (New)

- West Bengal 2002 electoral roll PDFs (Bengali, non-searchable) for historical baseline
- West Bengal 2026 voter-deletion lists to trace politically targeted exclusion patterns
- Film censorboard decision data (cuts, certifications, refusals) to track cultural governance

### Extraction Challenges and Proposed Pipeline

- Problem: scanned Bengali PDFs are not reliably machine-readable
- Pipeline: OCR (Tesseract + Bengali language pack) -> text cleanup -> structured parsing -> manual validation sample
- Validation target: at least 95% field-level accuracy on a stratified page sample before full analysis
- Output format: clean CSV with source page references for auditability

Data repos will be created/linked separately and referenced in `data/README.md`.

---

## Visualisation Plan

For data-driven articles, planned outputs:
- Choropleth or dot maps (demolition geography)
- Small multiples / timelines (language decline over census decades)
- Bar/density charts (land acquisition cases by state, UAPA charges)
- Annotation-rich D3 visual essays (interactive timelines, event strips, censorship clusters)

Tools: Python (pandas, geopandas) for processing; D3.js for publication-facing visuals — outputs into `assets/visuals/`

---

## Process Notes

- All drafts live in `drafts/` and are versioned via git
- Research notes and reading accumulate in `research/notes/`
- Data stays in `data/` with source documentation
- `PROJECT_LOG.md` updated every working session
- Pieces will be submitted to the publication editors when ready; submission dates added to the log

---

## Questions to Resolve

- [ ] What format/length does the publication accept for data-driven articles?
- [ ] Is multilingual submission possible / encouraged?
- [ ] Is there a submission deadline beyond what is in the concept note?
- [ ] Which co-contributors' work intersects most directly with mine? Worth reading their pieces.
- [ ] Can data visualisations be embedded in the print publication or only the digital edition?
