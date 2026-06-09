#!/usr/bin/env python3
"""
Build the vector sidecar for google-search-ads-analytics-docs: chunk Docs/ by Markdown headings,
embed with a multilingual model (validated on Polish), and save a compact local
index. Run after the corpus changes. Requires sentence-transformers (venv).

Outputs to .claude/skills/google-search-ads-analytics-docs/vec/:
  embeddings.npy  (float16, L2-normalized)   chunks.json   meta.json

Usage: python3 scripts/build_embeddings.py
"""
import glob, json, os, re
from pathlib import Path
import numpy as np

REPO = Path(__file__).resolve().parent.parent
os.chdir(REPO)
OUT = REPO / ".claude/skills/google-search-ads-analytics-docs/vec"
OUT.mkdir(parents=True, exist_ok=True)
MODEL = "intfloat/multilingual-e5-small"   # strong multilingual incl. Polish, 384-dim
MAX_CHARS = 1600

def parse_fm(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m: return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        kv = re.match(r'(\w+):\s*"?(.*?)"?\s*$', line)
        if kv: fm[kv.group(1)] = kv.group(2)
    return fm, m.group(2)

def chunk(body):
    # split on ATX/setext headings; pack into <=MAX_CHARS pieces
    parts, cur = [], []
    for line in body.splitlines():
        if (line.startswith("#") or re.fullmatch(r"[=-]{3,}", line.strip() or "")) and cur:
            parts.append("\n".join(cur)); cur = [line]
        else:
            cur.append(line)
    if cur: parts.append("\n".join(cur))
    out = []
    for p in parts:
        p = p.strip()
        while len(p) > MAX_CHARS:
            cut = p.rfind("\n", 0, MAX_CHARS)
            cut = cut if cut > 400 else MAX_CHARS
            out.append(p[:cut].strip()); p = p[cut:].strip()
        if len(p) > 40:
            out.append(p)
    return out

def main():
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(MODEL)
    chunks = []
    for f in sorted(glob.glob("Docs/**/*.md", recursive=True)):
        if os.path.basename(f) == "README.md": continue
        fm, body = parse_fm(open(f, encoding="utf-8").read())
        for c in chunk(body):
            chunks.append({"doc_id": fm.get("doc_id", f[len("Docs/"):]),
                           "title": fm.get("title", ""), "source_url": fm.get("source_url", ""),
                           "section": fm.get("section", ""), "text": c})
    print(f"chunks: {len(chunks)} from {len(set(c['doc_id'] for c in chunks))} docs; embedding…")
    # Contextual Retrieval (Anthropic): prepend each chunk's title|section so a chunk
    # carries its document context into the embedding. e5 wants a "passage:" prefix.
    def ctx(c):
        head = " | ".join(x for x in (c["title"], c["section"]) if x)
        return f"passage: {head}\n{c['text']}" if head else f"passage: {c['text']}"
    emb = model.encode([ctx(c) for c in chunks],
                       batch_size=64, normalize_embeddings=True, show_progress_bar=True)
    np.save(OUT / "embeddings.npy", emb.astype(np.float16))
    json.dump([{k: c[k] for k in ("doc_id", "title", "source_url", "section", "text")} for c in chunks],
              open(OUT / "chunks.json", "w", encoding="utf-8"), ensure_ascii=False)
    json.dump({"model": MODEL, "dim": int(emb.shape[1]), "count": len(chunks), "query_prefix": "query: "},
              open(OUT / "meta.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"saved {emb.shape} -> {OUT}")

if __name__ == "__main__":
    main()
