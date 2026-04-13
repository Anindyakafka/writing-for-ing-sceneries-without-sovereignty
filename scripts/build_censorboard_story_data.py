#!/usr/bin/env python3
"""Build narrative datasets for censorboard visual storytelling.

Input priority:
1) data/censorboard/raw/<tag>/data.csv (processed upstream dataset)
2) data/censorboard/raw/<tag>/metadata.csv + modifications.csv

Output:
- data/censorboard/processed/story_data.json
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import Counter, defaultdict

import pandas as pd


TOKEN_RE = re.compile(r"[A-Za-z]{3,}")
STOPWORDS = {
    "the", "and", "for", "with", "that", "this", "from", "have", "has", "were", "been",
    "into", "only", "shall", "film", "scene", "audio", "video", "dialogue", "dialog",
    "remove", "deleted", "delete", "replace", "replaced", "insert", "inserted", "cut",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build processed story data for D3 visuals")
    parser.add_argument("--raw-root", default="data/censorboard/raw", help="Root containing downloaded release folders")
    parser.add_argument("--out", default="data/censorboard/processed/story_data.json", help="Output story JSON")
    return parser.parse_args()


def newest_tag_dir(raw_root: pathlib.Path) -> pathlib.Path | None:
    tag_dirs = [d for d in raw_root.iterdir() if d.is_dir()]
    if not tag_dirs:
        return None
    return sorted(tag_dirs, key=lambda p: p.name.lower())[-1]


def to_year(series: pd.Series) -> pd.Series:
    parsed = pd.to_datetime(series, errors="coerce", dayfirst=True)
    return parsed.dt.year


def safe_col(df: pd.DataFrame, col: str, default):
    if col in df.columns:
        return df[col]
    return pd.Series([default] * len(df))


def split_multivalue(series: pd.Series) -> list[str]:
    items: list[str] = []
    for val in series.dropna().astype(str):
        parts = re.split(r"[,;|]+", val)
        items.extend([p.strip().lower() for p in parts if p.strip()])
    return items


def build_from_processed(data_df: pd.DataFrame) -> dict:
    df = data_df.copy()

    if "cert_date" in df.columns:
        df["year"] = to_year(df["cert_date"])
    else:
        df["year"] = pd.Series([pd.NA] * len(df))

    if "total_modified_time_secs" not in df.columns:
        for col in ["deleted_secs", "replaced_secs", "inserted_secs"]:
            if col not in df.columns:
                df[col] = 0
        df["total_modified_time_secs"] = df[["deleted_secs", "replaced_secs", "inserted_secs"]].fillna(0).sum(axis=1)

    if "certificate_id" not in df.columns:
        df["certificate_id"] = safe_col(df, "id", "unknown")

    # Panel 1: yearly pressure
    yearly = (
        df.dropna(subset=["year"])
        .groupby("year", as_index=False)
        .agg(
            modified_seconds=("total_modified_time_secs", "sum"),
            rows=("certificate_id", "count"),
            certificates=("certificate_id", "nunique"),
            cuts=("cut_no", lambda s: s.notna().sum() if "cut_no" in df.columns else 0),
        )
        .sort_values("year")
    )
    yearly["seconds_per_certificate"] = (yearly["modified_seconds"] / yearly["certificates"].replace(0, pd.NA)).fillna(0)

    # Panel 2: language burden
    if "language" not in df.columns:
        df["language"] = "Unknown"
    lang = (
        df.assign(language=df["language"].fillna("Unknown").astype(str).str.strip())
        .groupby("language", as_index=False)
        .agg(
            modified_seconds=("total_modified_time_secs", "sum"),
            certificates=("certificate_id", "nunique"),
            rows=("certificate_id", "count"),
        )
    )
    lang = lang[lang["language"] != ""]
    lang["seconds_per_certificate"] = (lang["modified_seconds"] / lang["certificates"].replace(0, pd.NA)).fillna(0)
    lang = lang.sort_values("seconds_per_certificate", ascending=False).head(25)

    # Panel 3: content/action matrix
    action_col = None
    content_col = None
    for col in ["ai_action", "type_tags", "mod_tags"]:
        if col in df.columns:
            action_col = col
            break
    for col in ["ai_content_types", "content_tags"]:
        if col in df.columns:
            content_col = col
            break

    matrix_rows: list[dict] = []
    if action_col and content_col:
        counts: defaultdict[tuple[str, str], int] = defaultdict(int)
        for _, row in df[[action_col, content_col]].dropna().iterrows():
            actions = [a for a in re.split(r"[,;|]+", str(row[action_col]).lower()) if a.strip()]
            contents = [c for c in re.split(r"[,;|]+", str(row[content_col]).lower()) if c.strip()]
            for a in actions[:6]:
                a = a.strip()
                if not a:
                    continue
                for c in contents[:8]:
                    c = c.strip()
                    if not c:
                        continue
                    counts[(a, c)] += 1
        for (action, content), n in counts.items():
            matrix_rows.append({"action": action, "content": content, "count": n})
        matrix_rows = sorted(matrix_rows, key=lambda x: x["count"], reverse=True)[:120]

    # Panel 4: most-censored words by year from descriptions
    desc_col = "cleaned_description" if "cleaned_description" in df.columns else "description"
    words_by_year: dict[int, Counter] = defaultdict(Counter)
    if desc_col in df.columns:
        for _, row in df[["year", desc_col]].dropna().iterrows():
            y = int(row["year"])
            tokens = [t.lower() for t in TOKEN_RE.findall(str(row[desc_col])) if t.lower() not in STOPWORDS]
            words_by_year[y].update(tokens)

    word_rows: list[dict] = []
    for y, counter in words_by_year.items():
        for word, n in counter.most_common(10):
            word_rows.append({"year": y, "word": word, "count": n})

    return {
        "yearly_pressure": yearly.to_dict(orient="records"),
        "language_burden": lang.to_dict(orient="records"),
        "action_content_matrix": matrix_rows,
        "censored_words": sorted(word_rows, key=lambda x: (x["year"], -x["count"])),
    }


def build_from_raw(metadata_df: pd.DataFrame, mods_df: pd.DataFrame) -> dict:
    meta = metadata_df.copy()
    mods = mods_df.copy()

    if "id" not in mods.columns and "certificate_id" in mods.columns:
        mods["id"] = mods["certificate_id"]

    for col in ["deleted", "replaced", "inserted"]:
        if col not in mods.columns:
            mods[col] = 0

    def parse_time(v):
        if pd.isna(v):
            return 0.0
        s = str(v).strip()
        if not s:
            return 0.0
        if re.match(r"^\d+\.\d{1,2}$", s):
            m, sec = s.split(".")
            sec = sec + "0" if len(sec) == 1 else sec
            return float(m) * 60 + float(sec)
        if re.match(r"^\d+:\d{2}$", s):
            m, sec = s.split(":")
            return float(m) * 60 + float(sec)
        return 0.0

    for col in ["deleted", "replaced", "inserted"]:
        mods[f"{col}_secs"] = mods[col].apply(parse_time)
    mods["total_modified_time_secs"] = mods[["deleted_secs", "replaced_secs", "inserted_secs"]].sum(axis=1)

    merged = mods.merge(meta, on="id", how="left", suffixes=("", "_meta"))
    if "cert_date" in merged.columns:
        merged["year"] = to_year(merged["cert_date"])
    else:
        merged["year"] = pd.Series([pd.NA] * len(merged))

    if "language" not in merged.columns:
        merged["language"] = "Unknown"

    return build_from_processed(merged)


def main() -> int:
    args = parse_args()
    raw_root = pathlib.Path(args.raw_root)
    out_path = pathlib.Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not raw_root.exists():
        print(f"Raw root not found: {raw_root}")
        return 1

    tag_dir = newest_tag_dir(raw_root)
    if tag_dir is None:
        print("No tag directories found in raw root")
        return 1

    processed_candidate = tag_dir / "data.csv"
    metadata_candidate = tag_dir / "metadata.csv"
    mods_candidate = tag_dir / "modifications.csv"

    if processed_candidate.exists():
        data_df = pd.read_csv(processed_candidate, low_memory=False)
        story = build_from_processed(data_df)
        source_mode = "processed_data_csv"
        source_files = [str(processed_candidate).replace("\\", "/")]
    elif metadata_candidate.exists() and mods_candidate.exists():
        metadata_df = pd.read_csv(metadata_candidate, low_memory=False)
        mods_df = pd.read_csv(mods_candidate, low_memory=False)
        story = build_from_raw(metadata_df, mods_df)
        source_mode = "raw_metadata_mods"
        source_files = [
            str(metadata_candidate).replace("\\", "/"),
            str(mods_candidate).replace("\\", "/"),
        ]
    else:
        print("Could not find suitable input files in latest tag dir")
        return 1

    payload = {
        "source_mode": source_mode,
        "source_files": source_files,
        "panels": story,
    }
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote story data: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
