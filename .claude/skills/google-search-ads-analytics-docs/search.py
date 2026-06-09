#!/usr/bin/env python3
"""
Ranking search over the Google Docs knowledge base (Docs/).
Stdlib only. Polish-inflection aware (stem/prefix matching) - literal grep
misses inflected forms (e.g. "dane strukturalne" vs files saying "strukturalnych").

Usage:
    python3 search.py "dane strukturalne produktu"          # rank docs
    python3 search.py "robots.txt" --top 5
    python3 search.py "konwersje GA4" --no-content          # metadata-only (faster)
    python3 search.py --doc search-console-help/answer-7440203.md   # show one doc's citation+head

Output: JSON to stdout (the agent reads this; the code never enters context).
"""
import argparse, json, os, re, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent

def _resolve_root():
    # 1) explicit env override; 2) bundled config.json (used by global installs);
    # 3) project layout (.claude/skills/<name>/ -> repo root); 4) cwd.
    env = os.environ.get("GOOGLE_SAA_DOCS_ROOT")
    if env and (Path(env) / "Docs").is_dir():
        return Path(env)
    cfg = HERE / "config.json"
    if cfg.is_file():
        try:
            r = json.loads(cfg.read_text(encoding="utf-8")).get("root")
            if r and (Path(r) / "Docs").is_dir():
                return Path(r)
        except Exception:
            pass
    for p in [HERE.parents[2] if len(HERE.parents) > 2 else HERE, Path.cwd()]:
        if (p / "Docs").is_dir():
            return p
    return HERE.parents[2] if len(HERE.parents) > 2 else HERE

ROOT = _resolve_root()
INDEX = json.loads((HERE / "index.json").read_text(encoding="utf-8"))

# Polish/general suffixes stripped to get a stem for prefix matching.
SUFFIXES = ["owania", "owanie", "owanych", "owany", "ami", "ach", "om", "ego",
            "emu", "ych", "ymi", "nych", "nej", "ość", "ości", "ów", "ie",
            "ę", "ą", "y", "i", "a", "e", "u"]

def fold(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c))

def stem(tok: str) -> str:
    t = fold(tok)
    if len(t) <= 4:
        return t
    for suf in SUFFIXES:
        fs = fold(suf)
        if t.endswith(fs) and len(t) - len(fs) >= 4:
            return t[: len(t) - len(fs)]
    return t[: max(5, len(t) - 2)]  # generic trim

def tokens(q: str):
    raw = re.findall(r"[\wąćęłńóśźż\.\-]+", q, flags=re.UNICODE)
    out = []
    for r in raw:
        if len(r) < 2:
            continue
        out.append((fold(r), stem(r)))
    return out

def read(path):
    try:
        return (ROOT / path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""

def score(doc, toks, use_content):
    title = fold(doc.get("title", ""))
    meta = fold(doc["doc_id"] + " " + doc.get("section", "") + " " + doc.get("product", ""))
    sc = 0.0
    body = fold(read(doc["path"])) if use_content else ""
    for raw, st in toks:
        if raw in title or st in title:
            sc += 5
        if raw in meta or st in meta:
            sc += 3
        if use_content and body:
            hits = body.count(st)
            if hits:
                sc += min(hits, 12) * 0.5
    # phrase bonus
    if len(toks) > 1:
        phrase = fold(" ".join(t[0] for t in toks))
        if phrase in title:
            sc += 10
        elif use_content and body and phrase in body:
            sc += 4
    return sc

def snippet(doc, toks):
    body = read(doc["path"])
    fb = fold(body)
    for _, st in toks:
        i = fb.find(st)
        if i >= 0:
            s = max(0, i - 60)
            return re.sub(r"\s+", " ", body[s:i + 120]).strip()
    return re.sub(r"\s+", " ", body[:160]).strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?", default="")
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--no-content", dest="content", action="store_false")
    ap.add_argument("--doc", help="resolve one doc_id -> citation + head")
    args = ap.parse_args()

    if args.doc:
        d = next((x for x in INDEX if x["doc_id"] == args.doc or x["path"].endswith(args.doc)), None)
        if not d:
            print(json.dumps({"error": "not found", "doc": args.doc})); return
        head = "\n".join(read(d["path"]).splitlines()[:40])
        print(json.dumps({**d, "head": head}, ensure_ascii=False, indent=2)); return

    if not args.query.strip():
        print(json.dumps({"error": "empty query"})); return

    toks = tokens(args.query)
    ranked = sorted(INDEX, key=lambda d: score(d, toks, args.content), reverse=True)
    out = []
    for d in ranked[: args.top]:
        s = score(d, toks, args.content)
        if s <= 0:
            break
        out.append({
            "title": d.get("title", ""),
            "doc_id": d["doc_id"],
            "path": d["path"],
            "section": d.get("section", ""),
            "product": d.get("product", ""),
            "source_url": d.get("source_url", ""),
            "score": round(s, 1),
            "snippet": snippet(d, toks) if args.content else "",
        })
    print(json.dumps({"query": args.query, "stems": [t[1] for t in toks],
                      "results": out, "total_docs": len(INDEX)},
                     ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
