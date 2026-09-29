#!/usr/bin/env python3
"""Record this review's pinned inputs and mark legacy visual artefacts."""
import hashlib
import argparse
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
WB = ROOT / "data/west-bengal"
SHA = "f1cf680863b332acf91d84c8681848a8d07b6dcd"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local-data", type=Path, required=True, help="Folder containing the source cleaning_qa.json and validation.json")
    local = parser.parse_args().local_data
    qa = WB / "local-qa"
    qa.mkdir(exist_ok=True)
    for name in ("cleaning_qa.json", "validation.json"):
        shutil.copyfile(local / name, qa / name)
    manifest = {"retrieved_on": "2026-09-28", "upstream_commit": SHA, "files": []}
    for path in sorted((WB / "upstream").rglob("*")):
        if path.is_file():
            rel = path.relative_to(WB / "upstream").as_posix()
            manifest["files"].append({
                "path": path.relative_to(WB).as_posix(),
                "url": f"https://raw.githubusercontent.com/Anindyakafka/Electoral-Rolls-West-Bengal-2002/{SHA}/{rel}",
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            })
    for path in [WB / "CEO-PN-36-2025.pdf", WB / "releases.json", *qa.glob("*.json")]:
        manifest["files"].append({"path": path.relative_to(WB).as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    (WB / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")
    summary = {
        "reviewed_on": "2026-09-28", "upstream_commit": SHA,
        "source_stage": "2025 uncollectable enumeration forms / SIR 2026 draft omission",
        "upstream_reported": {"pdf_inventory": 80655, "readable_pdfs": 80651, "zero_byte_pdfs": 4, "records": 5819543},
        "independent_csv_verification": "local-verification.json",
        "official_comparison": {"electors": 76637529, "forms_collected": 70816630, "difference": 5820899, "difference_minus_extracted_rows": 1356, "reconciliation_status": "unresolved"},
        "not_estimated": ["final deletions", "community targeting", "district exclusion rates", "2002 linkage"],
    }
    (WB / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8", newline="\n")
    replacements = {
        "Replacement: 3.14%": "Replacement: 3.27%", "Insertion: 2.59%": "Insertion: 2.47%",
        "Rupture: 2021 Is Not Just A Bigger Year": "Recorded Duration: 2020 to 2021",
        "Observation: The archive indicates a regulatory hardening event, not merely more films entering certification.": "Observation: Recorded duration rose; coverage and composition remain unverified. Cause not established.",
        "The censorship apparatus functions predominantly through removal, not substitution or contextualization.": "Deletion is 94.26% of the selected matrix counts; unique-intervention coverage is unknown.",
        "This supports reading the archive as a politics of subtraction.": "Legacy pie geometry is invalid: do not use this plate for publication.",
        "Censorship language remains institutionally procedural over time.": "Three selected description tokens recur; their normalized frequency is not established.",
        "The archive speaks in command verbs and operational tokens, not dialogic justification.": "Legacy ratio bars lack a common scale: regenerate before publication.",
        "These terms dominate the archive language of censorship instructions, indicating procedural standardization of intervention vocabulary.": "Selected description tokens; neither corpus dominance nor institutional change is established.",
    }
    for path in (ROOT / "assets/visuals/censorboard/print").glob("*.svg"):
        text = path.read_text(encoding="utf-8")
        for old, new in replacements.items():
            text = text.replace(old, new)
        if "LEGACY DRAFT" not in text:
            text = text.replace("</svg>", '<rect x="0" y="0" width="1800" height="38" fill="#7a1717"/>\n<text x="24" y="27" font-family="Arial" font-size="22" fill="white">LEGACY DRAFT — UNVERIFIED; NOT CLEARED FOR PUBLICATION (review: 2026-09-28)</text>\n</svg>')
        path.write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
