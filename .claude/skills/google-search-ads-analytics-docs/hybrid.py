#!/usr/bin/env python3
"""
Hybrid retrieval for google-search-ads-analytics-docs (best quality path):
  lexical (search.py, stem-aware) + dense (embeddings)  --RRF-->  candidates
  --> cross-encoder rerank (bge-reranker-v2-m3) --> top-k, cited.

Uses the persistent daemon (scripts/serve_models.py) if running (~100-300ms);
otherwise loads models inline (slower cold start). Requires the repo venv with
sentence-transformers + the prebuilt vec/ index.

Usage:
    python3 hybrid.py "jak zrobić żeby produkty pokazywały się z ceną i oceną"
    python3 hybrid.py "<query>" --top 6 --no-rerank
"""
import argparse, json, os, subprocess, sys, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
VEC = HERE / "vec"
RRF_K = 60

def daemon():
    f = VEC / ".daemon.json"
    if not f.exists(): return None
    try:
        port = json.loads(f.read_text())["port"]
        urllib.request.urlopen(f"http://127.0.0.1:{port}/health", timeout=2).read()
        return f"http://127.0.0.1:{port}"
    except Exception:
        return None

def post(base, path, payload):
    req = urllib.request.Request(base + path, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=120).read())

def lexical(query, n):
    """Ranked doc_ids from the stem-aware lexical search."""
    out = subprocess.run([sys.executable, str(HERE / "search.py"), query, "--top", str(n), "--no-content"],
                         capture_output=True, text=True)
    try:
        return [r["doc_id"] for r in json.loads(out.stdout).get("results", [])]
    except Exception:
        return []

def dense(query, n, base, model_cache):
    import numpy as np
    chunks = json.loads((VEC / "chunks.json").read_text(encoding="utf-8"))
    emb = np.load(VEC / "embeddings.npy").astype("float32")
    meta = json.loads((VEC / "meta.json").read_text())
    prefix = meta.get("query_prefix", "query: ")
    if base:
        q = np.array(post(base, "/embed", {"texts": [query], "prefix": prefix})["vectors"][0], dtype="float32")
    else:
        st = model_cache.get("st") or _load_embed(meta["model"], model_cache)
        q = st.encode([prefix + query], normalize_embeddings=True)[0].astype("float32")
    scores = emb @ q
    order = scores.argsort()[::-1]
    docs, seen = [], set()
    best_text = {}
    for i in order:
        d = chunks[i]["doc_id"]
        if d not in best_text:
            best_text[d] = chunks[i]
        if d not in seen:
            seen.add(d); docs.append(d)
        if len(docs) >= n and len(best_text) >= n:
            break
    return docs, best_text, chunks

def _load_embed(name, cache):
    from sentence_transformers import SentenceTransformer
    cache["st"] = SentenceTransformer(name); return cache["st"]

def rrf(*ranklists):
    score = {}
    for rl in ranklists:
        for rank, doc in enumerate(rl):
            score[doc] = score.get(doc, 0.0) + 1.0 / (RRF_K + rank + 1)
    return sorted(score, key=score.get, reverse=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--top", type=int, default=6)
    ap.add_argument("--candidates", type=int, default=30)
    # RRF fusion is the default best path on this corpus (eval: 96% recall@5).
    # The cross-encoder reranker is OPT-IN (--rerank); it regressed this corpus.
    ap.add_argument("--rerank", action="store_true")
    args = ap.parse_args()
    if not (VEC / "embeddings.npy").exists():
        print(json.dumps({"error": "no vector index - run scripts/build_embeddings.py"})); return

    base = daemon()
    cache = {}
    lex = lexical(args.query, args.candidates)
    den, best_text, chunks = dense(args.query, args.candidates, base, cache)
    fused = rrf(lex, den)[: max(args.top, 20)]

    # representative text per candidate doc (best dense chunk, else title)
    idx = {c["doc_id"]: c for c in chunks}
    def rep(doc): return (best_text.get(doc) or idx.get(doc) or {"text": doc})
    cands = [{"doc_id": d, **{k: rep(d).get(k, "") for k in ("title", "source_url", "section", "text")}} for d in fused]

    mode = "hybrid+rrf"
    if args.rerank and cands:
        passages = [f"{c['title']} | {c['section']}\n{c['text']}"[:1200] for c in cands]
        if base:
            scores = post(base, "/rerank", {"query": args.query, "passages": passages})["scores"]
        else:
            from sentence_transformers import CrossEncoder
            scores = [float(s) for s in CrossEncoder("BAAI/bge-reranker-v2-m3").predict([[args.query, p] for p in passages])]
        for c, s in zip(cands, scores): c["rerank"] = round(float(s), 3)
        cands.sort(key=lambda c: c["rerank"], reverse=True)
        mode = "hybrid+rrf+rerank"

    results = [{"title": c["title"], "doc_id": c["doc_id"], "source_url": c["source_url"],
                "section": c["section"], "rerank": c.get("rerank"),
                "snippet": " ".join(c["text"].split())[:200]} for c in cands[: args.top]]
    print(json.dumps({"query": args.query, "mode": mode, "daemon": bool(base), "results": results},
                     ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
