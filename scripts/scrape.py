#!/usr/bin/env python3
"""
Scrape/refresh the Google-docs corpus into Docs/ from scripts/manifest.json.
Escalates get(+selector) -> get -> stealthy-fetch. Idempotent: skips pages that
already have content unless --force.

Usage:
    python3 scripts/scrape.py                 # fetch only missing pages
    python3 scripts/scrape.py --force         # re-fetch everything (refresh)
    python3 scripts/scrape.py --only support  # only paths containing "support"
"""
import argparse, json, os, subprocess, sys, time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRAP = REPO / ".venv/bin/scrapling"
MANIFEST = REPO / "scripts/manifest.json"
MIN_BYTES = 200

def run(cmd, timeout=120):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout).returncode == 0
    except Exception:
        return False

def size(p):
    try: return os.path.getsize(p)
    except OSError: return 0

def fetch(url, path, sel):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if sel and run([str(SCRAP), "extract", "get", url, path, "-s", sel, "--timeout", "60"]) and size(path) >= MIN_BYTES:
        return "get+sel"
    if run([str(SCRAP), "extract", "get", url, path, "--timeout", "60"]) and size(path) >= MIN_BYTES:
        return "get"
    if sel and run([str(SCRAP), "extract", "stealthy-fetch", url, path, "-s", sel, "--timeout", "60000"], 180) and size(path) >= MIN_BYTES:
        return "stealthy+sel"
    if run([str(SCRAP), "extract", "stealthy-fetch", url, path, "--timeout", "60000"], 180) and size(path) >= MIN_BYTES:
        return "stealthy"
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", default="")
    args = ap.parse_args()
    if not SCRAP.exists():
        sys.exit(f"scrapling not found at {SCRAP} - create the venv (see README).")
    man = json.load(open(MANIFEST, encoding="utf-8"))
    ok = fail = skip = 0
    for it in man:
        path = str(REPO / it["path"])
        if args.only and args.only not in it["path"]:
            continue
        if not args.force and size(path) >= MIN_BYTES:
            skip += 1; continue
        m = fetch(it["url"], path, it.get("sel"))
        if m: ok += 1
        else: fail += 1; print(f"  FAIL {it['url']}")
        time.sleep(0.3)
    print(f"scrape done: ok={ok} fail={fail} skipped={skip}")

if __name__ == "__main__":
    main()
