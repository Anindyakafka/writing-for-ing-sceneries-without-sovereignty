#!/usr/bin/env python3
"""Adapt the historical CBFC aggregate; does not reproduce source extraction."""
import json
from collections import Counter
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    folder = root / "data/censorboard/processed"
    source = json.loads((folder / "real_computed_story_data.json").read_text(encoding="utf-8"))
    note = "Historical aggregate, not independently reproduced from CSVs. Selected matrix counts and description tokens; not causal evidence."
    story = {
        "source_mode": "historical_aggregate_unverified",
        "source_files": ["data/censorboard/processed/real_computed_story_data.json"],
        "review_note": note,
        "panels": dict(zip(
            ["yearly_pressure", "language_burden", "action_content_matrix", "censored_words"],
            [source["yearly"], source["languages"], source["matrix"], source["words_2018_2025_top"]],
        )),
    }
    actions = Counter()
    for row in source["matrix"]:
        actions[row["action"]] += row["count"]
    total = sum(actions.values())
    observations = {
        "derived_from": story["source_files"][0], "reviewed_on": "2026-09-28",
        "evidence_status": note, "selected_matrix_total": total,
        "action_counts": dict(actions),
        "action_shares_percent": {k: round(v / total * 100, 2) for k, v in actions.items()},
        "withdrawn_interpretations": ["2021 regulatory hardening established", "language disparity proves unequal treatment", "selected token counts prove institutional persistence", "matrix shares describe all unique interventions"],
    }
    for name, payload in [("story_data.json", story), ("inferred_observations.json", observations)]:
        (folder / name).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
