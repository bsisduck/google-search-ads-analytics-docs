#!/usr/bin/env python3
"""
Refresh the corpus: re-scrape all pages from the manifest, re-add frontmatter to
any new files, rebuild the search index, rebuild embeddings (if available), and
validate. Use to pull in Google's documentation updates.

Usage:
    python3 scripts/refresh.py            # full refresh
    python3 scripts/refresh.py --only support

For periodic refresh, schedule this (e.g. Claude Code /schedule, or cron):
    0 7 * * 1  cd <repo> && .venv/bin/python3 scripts/refresh.py >> refresh.log 2>&1
"""
import argparse, subprocess, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PY = str(REPO / ".venv/bin/python3")

def step(name, args):
    print(f"\n=== {name} ===")
    r = subprocess.run([PY, *args], cwd=REPO)
    if r.returncode != 0 and name != "validate":
        sys.exit(f"{name} failed (exit {r.returncode})")
    return r.returncode

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    args = ap.parse_args()
    scrape = ["scripts/scrape.py", "--force"] + (["--only", args.only] if args.only else [])
    step("scrape (force)", scrape)
    step("frontmatter", ["scripts/enhance_frontmatter.py"])      # only new files get it
    step("build index", ["scripts/build_index.py"])
    if (REPO / "scripts/build_embeddings.py").exists():
        step("build embeddings", ["scripts/build_embeddings.py"])
    code = step("validate", ["scripts/validate.py"])
    print(f"\nrefresh complete (validation {'PASSED' if code == 0 else 'FAILED'})")

if __name__ == "__main__":
    main()
