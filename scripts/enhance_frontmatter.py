#!/usr/bin/env python3
"""
Add YAML frontmatter (title, source_url, product, section, language, scraped_date,
doc_id) to every Docs/*.md content file. Idempotent: skips files that already
start with '---'. Titles come from the curated section README tables, then the
file's first heading, then a humanized slug.

Usage: python3 scripts/enhance_frontmatter.py [--scraped-date YYYY-MM-DD]
"""
import argparse, glob, json, os, re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
os.chdir(REPO)
URL = {os.path.normpath(k): v for k, v in json.load(open("scripts/url_map.json", encoding="utf-8")).items()}

def product_section(p):
    p = p.replace("\\", "/")
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

def looks_like_path(s):
    return ("/" in s) or s.lower().endswith(".md") or bool(re.fullmatch(r"answer-\d+\.md", s.strip()))

def title_map():
    tm = {}
    for r in glob.glob("Docs/**/README.md", recursive=True):
        if os.path.normpath(r) == "Docs/README.md":
            continue
        base = os.path.dirname(r)
        for line in open(r, encoding="utf-8"):
            m = (re.match(r"\s*\|\s*\[([^\]]+)\]\(([^)]+\.md)\)\s*\|\s*([^|]+?)\s*\|", line)
                 or re.match(r"\s*[-*]\s*\[([^\]]+)\]\(([^)]+\.md)\)\s*[---]?\s*(.*)", line))
            if not m: continue
            text, link, desc = m.group(1).strip(), m.group(2).split("#")[0], m.group(3).strip()
            if link.startswith(("http", "//")): continue
            tgt = os.path.normpath(os.path.join(base, link))
            title = desc if looks_like_path(text) else text
            title = re.sub(r"\s+", " ", title).strip().rstrip(".")
            if title and not looks_like_path(title):
                tm.setdefault(tgt, title[:140])
    return tm

TITLES = title_map()

def _clean_h(s):
    return re.sub(r"[*\[\]]", "", re.sub(r"^#+\s*", "", s.strip())).strip()[:120]

def first_heading(f):
    lines = open(f, encoding="utf-8").read().splitlines()
    # setext H1 (==== underline)
    for i in range(len(lines) - 1):
        if lines[i].strip() and re.fullmatch(r"=+", (lines[i + 1].strip() or "")):
            return _clean_h(lines[i])
    # ATX heading
    for ln in lines:
        if ln.startswith("#"): return _clean_h(ln)
    # setext H2 (---- underline) - support.google.com answer pages have no H1 in the
    # extracted content; their first real heading is a dash-underlined H2.
    for i in range(len(lines) - 1):
        cur, nxt = lines[i].strip(), (lines[i + 1].strip() or "")
        if cur and "|" not in cur and len(cur) < 100 and re.fullmatch(r"-{3,}", nxt):
            return _clean_h(cur)
    return None

CHROME = {"Search", "Clear search", "Close search", "Main menu", "Cancel", "Submit",
          "true", "false", "On this page", "outlined_flag", "outlined\\_flag", "Page Summary"}

def strip_summary_widget(text):
    """Remove Google's injected 'Page Summary' AI widget (Spark icon -> AI bullets);
    it is not part of the source documentation."""
    lines = text.split("\n"); out = []; i = 0; n = len(lines); in_sum = False
    while i < n:
        s = lines[i].strip()
        if "spark.svg" in s and s.startswith("!["): i += 1; continue
        if s == "Page Summary" and i + 1 < n and re.fullmatch(r"-{3,}", lines[i + 1].strip()):
            i += 2; continue
        if s in ("outlined_flag", "outlined\\_flag"): in_sum = True; i += 1; continue
        if in_sum:
            if s == "": i += 1; continue
            if s.startswith(("* ", "- ", "+ ")): i += 1; continue
            in_sum = False
        out.append(lines[i]); i += 1
    return "\n".join(out)

def clean_body(text):
    """Strip residual scrape chrome (AI summary widget, feedback buttons, license, nav)."""
    text = strip_summary_widget(text)
    out = []
    DROP = ("Prześlij opinię", "Wyślij opinię", "Send feedback", "Prześlij prośbę o pomoc",
            "Was this helpful?", "Yes No", "Need more help?", "Give feedback about this article",
            "Help Center", "Sign in", "Google apps") + tuple(CHROME)
    for ln in text.split("\n"):
        s = ln.strip()
        if "thumb-up" in s or s.startswith("[[["): continue
        if s.startswith("[Skip to main content]") or s.startswith("[Skip to "): continue
        if s in DROP: continue
        if s.startswith("O ile nie stwierdzono inaczej"): continue          # PL CC license footer
        if s.startswith("Except as otherwise noted"): continue              # EN CC license footer
        if re.match(r"#*\s*Widzisz coś dziwnego", s) or s.startswith("Zdarzyło Ci się trafić na uszkodzony link"): continue
        out.append(ln)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).replace("&nbsp;", " ").strip() + "\n"

def yq(s): return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scraped-date", default="2026-06-05")
    args = ap.parse_args()
    done = skip = 0
    for f in glob.glob("Docs/**/*.md", recursive=True):
        if os.path.basename(f) == "README.md": continue
        raw = open(f, encoding="utf-8").read()
        if raw.lstrip().startswith("---"):
            skip += 1; continue
        norm = os.path.normpath(f)
        title = TITLES.get(norm) or first_heading(f) or os.path.splitext(os.path.basename(f))[0].replace("-", " ").capitalize()
        title = re.sub(r"\s+", " ", title).strip()[:140]
        url = URL.get(norm, "")
        lang = "pl" if "hl=pl" in url else "en"
        product, section = product_section(norm)
        fm = ["---", f"title: {yq(title)}", f"source_url: {yq(url)}", f"product: {yq(product)}",
              f"section: {yq(section)}", f"language: {lang}", f"scraped_date: {args.scraped_date}",
              f"doc_id: {yq(norm[len('Docs/'):])}", "---", ""]
        open(f, "w", encoding="utf-8").write("\n".join(fm) + clean_body(raw))
        done += 1
    print(f"frontmatter: added={done} skipped(existing)={skip}")

if __name__ == "__main__":
    main()
