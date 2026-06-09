#!/usr/bin/env python3
"""
Validate corpus integrity: relative-link resolution, duplicate content (md5),
captured error/404 pages, and tiny/empty files. Exits non-zero on any failure
(usable as a pre-commit / CI check).

Usage: python3 scripts/validate.py
"""
import glob, hashlib, os, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
os.chdir(REPO)
fail = 0

# 1) relative .md link integrity
broken = []
for f in glob.glob("Docs/**/*.md", recursive=True):
    base = os.path.dirname(f)
    for m in re.finditer(r"\]\(([^)]+\.md)\)", open(f, encoding="utf-8").read()):
        link = m.group(1).split("#")[0]
        if link.startswith(("http", "//")): continue
        if not os.path.exists(os.path.normpath(os.path.join(base, link))):
            broken.append((f, link))
print(f"[links]  broken: {len(broken)}")
for f, l in broken[:20]: print(f"         {f} -> {l}")
fail += len(broken)

# 2) duplicate content
seen = {}
for f in glob.glob("Docs/**/*.md", recursive=True):
    if os.path.basename(f) == "README.md": continue
    h = hashlib.md5(open(f, "rb").read()).hexdigest()
    seen.setdefault(h, []).append(f)
dups = [v for v in seen.values() if len(v) > 1]
print(f"[dups]   clusters: {len(dups)}")
for c in dups[:20]: print("         " + " == ".join(c))
fail += len(dups)

# 3) captured error / 404 pages
ERR = re.compile(r"Tej strony nie można znaleźć|Ta strona nie istnieje w|requested url was not found", re.I)
errs = [f for f in glob.glob("Docs/**/*.md", recursive=True)
        if os.path.basename(f) != "README.md" and ERR.search(open(f, encoding="utf-8").read())]
print(f"[errors] captured error pages: {len(errs)}")
for f in errs[:20]: print(f"         {f}")
fail += len(errs)

# 4) tiny files
tiny = [f for f in glob.glob("Docs/**/*.md", recursive=True)
        if os.path.basename(f) != "README.md" and os.path.getsize(f) < 120]
print(f"[size]   files <120B: {len(tiny)}")
for f in tiny: print(f"         {f}")
fail += len(tiny)

print(f"\nVALIDATION {'PASSED' if fail == 0 else 'FAILED'} (issues: {fail})")
sys.exit(1 if fail else 0)
