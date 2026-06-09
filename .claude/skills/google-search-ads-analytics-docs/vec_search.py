#!/usr/bin/env python3
"""
Semantic (vector) fallback for google-search-ads-analytics-docs - for conceptual / paraphrased
queries where Polish stem-grep underperforms. Requires sentence-transformers
(repo venv) and the prebuilt index in vec/ (scripts/build_embeddings.py).

Usage:
    python3 vec_search.py "jak sprawić żeby produkty pojawiały się w wynikach"
    python3 vec_search.py "<query>" --top 6

Returns JSON: doc-level results (best chunk per doc) with title/source_url/snippet.
"""
import argparse, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VEC = HERE / "vec"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--top", type=int, default=6)
    args = ap.parse_args()
    if not (VEC / "embeddings.npy").exists():
        print(json.dumps({"error": "no vector index - run scripts/build_embeddings.py"})); return
    import numpy as np, urllib.request
    meta = json.loads((VEC / "meta.json").read_text(encoding="utf-8"))
    chunks = json.loads((VEC / "chunks.json").read_text(encoding="utf-8"))
    emb = np.load(VEC / "embeddings.npy").astype("float32")
    prefix = meta.get("query_prefix", "query: ")
    # Use the persistent daemon if running (fast); else load the model inline.
    q = None
    df = VEC / ".daemon.json"
    if df.exists():
        try:
            base = f"http://127.0.0.1:{json.loads(df.read_text())['port']}"
            req = urllib.request.Request(base + "/embed",
                  data=json.dumps({"texts": [args.query], "prefix": prefix}).encode(),
                  headers={"Content-Type": "application/json"})
            q = np.array(json.loads(urllib.request.urlopen(req, timeout=60).read())["vectors"][0], dtype="float32")
        except Exception:
            q = None
    if q is None:
        try:
            from sentence_transformers import SentenceTransformer
        except Exception as e:
            print(json.dumps({"error": f"sentence-transformers missing: {e}"})); return
        q = SentenceTransformer(meta["model"]).encode([prefix + args.query], normalize_embeddings=True)[0].astype("float32")
    scores = emb @ q  # cosine (both normalized)
    order = scores.argsort()[::-1]
    best, seen = [], set()
    for i in order:
        c = chunks[i]
        if c["doc_id"] in seen:
            continue
        seen.add(c["doc_id"])
        best.append({"title": c["title"], "doc_id": c["doc_id"], "source_url": c["source_url"],
                     "section": c["section"], "score": round(float(scores[i]), 3),
                     "snippet": " ".join(c["text"].split())[:200]})
        if len(best) >= args.top:
            break
    print(json.dumps({"query": args.query, "mode": "semantic", "model": meta["model"], "results": best},
                     ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
