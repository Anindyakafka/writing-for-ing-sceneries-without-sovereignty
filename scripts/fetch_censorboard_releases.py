#!/usr/bin/env python3
"""Download release assets from a GitHub repository.

Default target for this project:
owner=Anindyakafka, repo=CensorBoard_records
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import pathlib
import sys
import urllib.error
import urllib.request
from typing import Any


API_BASE = "https://api.github.com"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download GitHub release assets")
    parser.add_argument("--owner", default="Anindyakafka", help="GitHub owner")
    parser.add_argument("--repo", default="CensorBoard_records", help="GitHub repository")
    parser.add_argument("--out", default="data/censorboard/raw", help="Output directory")
    parser.add_argument("--tag", default=None, help="Specific release tag to fetch")
    parser.add_argument("--latest", action="store_true", help="Fetch latest release only")
    parser.add_argument(
        "--include",
        nargs="*",
        default=[],
        help="Optional wildcard patterns for asset names, e.g. '*.csv' '*.json'",
    )
    return parser.parse_args()


def github_get(url: str) -> Any:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "censorboard-release-fetcher",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def matches_include(name: str, patterns: list[str]) -> bool:
    if not patterns:
        return True
    return any(fnmatch.fnmatch(name, pattern) for pattern in patterns)


def ensure_dir(path: pathlib.Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def download(url: str, out_path: pathlib.Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": "censorboard-release-fetcher"})
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    out_path.write_bytes(data)


def get_releases(owner: str, repo: str, tag: str | None, latest: bool) -> list[dict[str, Any]]:
    if tag:
        release = github_get(f"{API_BASE}/repos/{owner}/{repo}/releases/tags/{tag}")
        return [release]
    if latest:
        release = github_get(f"{API_BASE}/repos/{owner}/{repo}/releases/latest")
        return [release]
    return github_get(f"{API_BASE}/repos/{owner}/{repo}/releases")


def main() -> int:
    args = parse_args()
    out_root = pathlib.Path(args.out)
    ensure_dir(out_root)
    manifest_dir = out_root.parent / "metadata"
    ensure_dir(manifest_dir)

    try:
        releases = get_releases(args.owner, args.repo, args.tag, args.latest)
    except urllib.error.HTTPError as exc:
        print(f"GitHub API request failed: {exc}", file=sys.stderr)
        return 1

    manifest: list[dict[str, Any]] = []
    downloaded = 0

    for rel in releases:
        tag_name = rel.get("tag_name", "untagged")
        release_dir = out_root / tag_name
        ensure_dir(release_dir)

        assets = rel.get("assets", [])
        for asset in assets:
            name = asset.get("name", "")
            if not name or not matches_include(name, args.include):
                continue

            url = asset.get("browser_download_url")
            if not url:
                continue

            target = release_dir / name
            try:
                download(url, target)
            except urllib.error.HTTPError as exc:
                print(f"Failed to download {name}: {exc}", file=sys.stderr)
                continue

            downloaded += 1
            manifest.append(
                {
                    "repo": f"{args.owner}/{args.repo}",
                    "release_tag": tag_name,
                    "asset_name": name,
                    "source_url": url,
                    "local_path": str(target).replace("\\", "/"),
                }
            )
            print(f"Downloaded: {tag_name}/{name}")

    manifest_path = manifest_dir / "release-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote manifest: {manifest_path}")
    print(f"Total assets downloaded: {downloaded}")

    if downloaded == 0:
        print("No assets downloaded. Check --include patterns or release availability.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
