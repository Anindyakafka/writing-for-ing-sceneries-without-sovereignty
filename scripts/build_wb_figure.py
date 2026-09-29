#!/usr/bin/env python3
"""Generate an aggregate-only figure from the verified cleaned-file summary."""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]


def main():
    data = json.loads((ROOT / "data/west-bengal/local-verification.json").read_text())
    if not data["passed"]:
        raise ValueError("Verification did not pass")
    keys = ["death", "permanently_shifted", "untraceable_or_absent", "already_enrolled"]
    labels = ["Death", "Permanently shifted", "Untraceable / absent", "Already enrolled"]
    values = [data["counts"]["uncollectable_reason"][k] for k in keys]
    total = data["rows"]
    fig, ax = plt.subplots(figsize=(11, 6.5))
    fig.patch.set_facecolor("#faf7f1")
    ax.set_facecolor("#faf7f1")
    ax.barh(labels, [v / 1e6 for v in values], color=["#713e3c", "#956951", "#b38966", "#717c73"], height=.55)
    ax.invert_yaxis()
    for i, value in enumerate(values):
        ax.text(value / 1e6 + .045, i, f"{value:,}  ({value / total:.2%})", va="center", fontsize=11)
    ax.set_xlim(0, 3.15)
    ax.set_xlabel("Extracted records (millions)", labelpad=12)
    ax.set_xticks([0, .5, 1, 1.5, 2, 2.5, 3])
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0, labelsize=11)
    ax.grid(axis="x", alpha=.15)
    ax.set_axisbelow(True)
    fig.text(.06, .94, "What the enumeration record calls absence", fontsize=20, weight="bold")
    fig.text(.06, .885, "West Bengal 2025 ASD reports for SIR 2026 • 5,819,543 extracted records", fontsize=11)
    fig.text(.06, .10, "Source-recorded reasons, not independently verified circumstances or final deletion outcomes.", fontsize=10)
    fig.text(.06, .065, "Full cleaned-CSV pass: 28 September 2026. Four zero-byte source PDFs yield no records.", fontsize=10)
    fig.text(.06, .03, "Source: Anindyakafka / Electoral-Rolls-West-Bengal-2002. See accompanying provenance and caption.", fontsize=9)
    fig.subplots_adjust(left=.24, right=.98, top=.8, bottom=.25)
    out = ROOT / "assets/visuals/west-bengal"
    out.mkdir(parents=True, exist_ok=True)
    for suffix in ("svg", "pdf", "png"):
        fig.savefig(out / f"asd-recorded-reasons.{suffix}", dpi=180)
    plt.close(fig)


if __name__ == "__main__":
    main()
