#!/usr/bin/env python3
"""
Generate English navigation indexes from frontmatter:
  - a README.md in every Docs/ directory that holds content (lists its docs +
    links to subsection READMEs),
  - the master Docs/README.md (product overview + counts).
Run after enhance_frontmatter.py. Idempotent (overwrites the generated READMEs).

Usage: python3 scripts/build_readmes.py
"""
import glob, os, re
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
os.chdir(REPO)

def parse_fm(path):
    txt = open(path, encoding="utf-8").read()
    fm = {}
    if txt.startswith("---"):
        block = txt.split("---", 2)[1]
        for line in block.splitlines():
            m = re.match(r'(\w+):\s*"?(.*?)"?\s*$', line)
            if m: fm[m.group(1)] = m.group(2)
    return fm

PRODUCTS = {
    "search-central": "Google Search Central (SEO)",
    "search-console-help": "Google Search Console",
    "google-ads-help": "Google Ads",
    "google-analytics": "Google Analytics 4",
}
def humanize(name):
    return name.replace("-", " ").replace("_", " ").title()

# collect content files
files = [f for f in glob.glob("Docs/**/*.md", recursive=True)
         if os.path.basename(f) != "README.md" and os.path.normpath(f) != "Docs/KNOWLEDGE-BASE-ARCHITECTURE.md"]
by_dir = defaultdict(list)
for f in files:
    by_dir[os.path.dirname(f)].append(f)

dirs_with_content = set(by_dir)
# every ancestor dir under Docs/ that should carry a README (has content below it)
all_dirs = set()
for d in dirs_with_content:
    p = d
    while p and p.startswith("Docs"):
        all_dirs.add(p); p = os.path.dirname(p)

def subdirs(d):
    return sorted(x for x in all_dirs if os.path.dirname(x) == d and x != d)

def count_under(d):
    return sum(1 for f in files if f.startswith(d + os.sep))

def section_title(d):
    rel = os.path.relpath(d, "Docs")
    if rel == ".": return "Knowledge Base"
    parts = rel.split(os.sep)
    if parts[0] in PRODUCTS and len(parts) == 1:
        return PRODUCTS[parts[0]]
    return humanize(parts[-1])

made = 0
for d in sorted(all_dirs):
    if d == "Docs":
        continue
    lines = [f"# {section_title(d)}", ""]
    n = count_under(d)
    lines.append(f"*{n} page{'s' if n != 1 else ''} in this section.*\n")
    # subsections
    subs = subdirs(d)
    if subs:
        lines.append("## Subsections\n")
        for s in subs:
            lines.append(f"- [{section_title(s)}]({os.path.relpath(s, d)}/README.md) - {count_under(s)} pages")
        lines.append("")
    # direct docs
    here = sorted(by_dir.get(d, []), key=lambda f: f.lower())
    if here:
        lines.append("## Pages\n")
        lines.append("| Page | Source |")
        lines.append("|---|---|")
        for f in here:
            fm = parse_fm(f)
            title = fm.get("title") or humanize(Path(f).stem)
            src = fm.get("source_url", "")
            srccell = f"[google]({src})" if src else "-"
            lines.append(f"| [{title}]({os.path.relpath(f, d)}) | {srccell} |")
        lines.append("")
    open(os.path.join(d, "README.md"), "w", encoding="utf-8").write("\n".join(lines))
    made += 1

# master README
total = len(files)
m = ["# Google Search / Ads / Analytics docs - Knowledge Base", "",
     f"A validated local corpus of **{total} official Google documentation pages** (English), "
     "mirroring Google's URL structure. Each page carries YAML frontmatter with the original "
     "`source_url`. See [KNOWLEDGE-BASE-ARCHITECTURE.md](KNOWLEDGE-BASE-ARCHITECTURE.md) for how "
     "the corpus is mapped for AI-agent retrieval.", "",
     "## Products", "", "| Product | Pages | Index |", "|---|---:|---|"]
for key, label in PRODUCTS.items():
    d = f"Docs/{key}"
    if os.path.isdir(d):
        m.append(f"| {label} | {count_under(d)} | [{key}/README.md]({key}/README.md) |")
m += ["", f"*Total: {total} pages. Content (c) Google, licensed CC BY 4.0; local reference copy.*", ""]
open("Docs/README.md", "w", encoding="utf-8").write("\n".join(m))
made += 1
print(f"READMEs generated: {made} (incl. master). Content pages: {total}")
