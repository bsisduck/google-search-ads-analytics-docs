#!/usr/bin/env python3
"""
Rebuild the google-search-ads-analytics-docs search index (.claude/skills/google-search-ads-analytics-docs/index.json)
from Docs/. Prefers YAML frontmatter (title/source_url/product/section); falls back
to scripts/url_map.json + README titles + first heading. Run after the corpus or
frontmatter changes. Also copies the fresh index to the global skill if present.

Usage: python3 scripts/build_index.py
"""
import glob, json, os, re, shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
os.chdir(REPO)
OUT = ".claude/skills/google-search-ads-analytics-docs/index.json"
URL = {os.path.normpath(k): v for k, v in json.load(open("scripts/url_map.json", encoding="utf-8")).items()} \
      if os.path.exists("scripts/url_map.json") else {}

def parse_fm(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m: return {}
    fm = {}
    for line in m.group(1).splitlines():
        kv = re.match(r'(\w+):\s*"?(.*?)"?\s*$', line)
        if kv: fm[kv.group(1)] = kv.group(2)
    return fm

def product_section(p):
    names = {"essentials": "Search Essentials", "fundamentals": "SEO Fundamentals",
             "crawling-indexing": "Crawling & Indexing", "appearance": "Appearance & Structured Data",
             "monitor-debug": "Monitor & Debug", "specialty": "Specialty Sites", "advanced": "Advanced Guidelines"}
    if p.startswith("Docs/search-central/docs/"):
        return "Google Search Central", f"Docs / {names.get(p.split('/')[3], p.split('/')[3])}"
    if p.startswith("Docs/search-central/help"): return "Google Search Central", "Help & FAQ"
    if p.startswith("Docs/search-central/crawling-docs"): return "Google Search Central", "Crawler Specs"
    if p.startswith("Docs/search-central/case-studies"): return "Google Search Central", "Case Studies"
    if p.startswith("Docs/search-console-help"): return "Google Search Console", "Help Center"
    if p.startswith("Docs/google-ads-help"): return "Google Ads", "Help Center"
    if p.startswith("Docs/google-analytics/collection-ga4"): return "Google Analytics 4", "Collection (gtag)"
    if p.startswith("Docs/google-analytics/measurement-protocol"): return "Google Analytics 4", "Measurement Protocol"
    if p.startswith("Docs/google-analytics/collection-app"): return "Google Analytics 4", "App (Firebase)"
    if p.startswith("Docs/google-analytics/support"): return "Google Analytics 4", "Help Center"
    return "Google", "General"

def first_heading(text):
    lines = text.splitlines()
    for i in range(len(lines) - 1):
        if lines[i].strip() and re.fullmatch(r"=+", (lines[i + 1].strip() or "")):
            return re.sub(r"[*\[\]]", "", lines[i].strip())[:120]
    for ln in lines:
        if ln.startswith("#"): return re.sub(r"^#+\s*", "", ln).strip()[:120]
    return None

idx = []
for f in sorted(glob.glob("Docs/**/*.md", recursive=True)):
    if os.path.basename(f) == "README.md": continue
    norm = os.path.normpath(f)
    text = open(f, encoding="utf-8").read()
    fm = parse_fm(text)
    prod, sec = product_section(norm)
    title = fm.get("title") or first_heading(text) or os.path.splitext(os.path.basename(f))[0].replace("-", " ").capitalize()
    idx.append({
        "doc_id": fm.get("doc_id") or norm[len("Docs/"):],
        "path": norm,
        "title": re.sub(r"\s+", " ", title).strip()[:140],
        "product": fm.get("product") or prod,
        "section": fm.get("section") or sec,
        "source_url": fm.get("source_url") or URL.get(norm, ""),
        "bytes": os.path.getsize(f),
    })
json.dump(idx, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(f"index.json rebuilt: {len(idx)} docs")

g = Path.home() / ".claude/skills/google-search-ads-analytics-docs/index.json"
if g.exists():
    shutil.copy(OUT, g); print(f"copied to global skill: {g}")
