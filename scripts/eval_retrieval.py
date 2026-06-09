#!/usr/bin/env python3
"""
Retrieval eval: runs the Polish query set (data/eval_queries.json) through each
retrieval method and reports Recall@k and MRR. Use to compare methods and catch
regressions after corpus/model changes.

Usage:
    python3 scripts/eval_retrieval.py            # lexical, dense, hybrid
    python3 scripts/eval_retrieval.py --k 5
    python3 scripts/eval_retrieval.py --methods lexical,hybrid
"""
import argparse, json, subprocess, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
KB = REPO / ".claude/skills/google-search-ads-analytics-docs"
PY = sys.executable
QUERIES = json.loads((REPO / "data/eval_queries.json").read_text(encoding="utf-8"))

METHODS = {
    "lexical": [PY, str(KB / "search.py"), "{q}", "--no-content", "--top", "{k}"],
    "dense":   [PY, str(KB / "vec_search.py"), "{q}", "--top", "{k}"],
    "hybrid":  [PY, str(KB / "hybrid.py"), "{q}", "--top", "{k}"],
}

def run(method, q, k):
    cmd = [a.replace("{q}", q).replace("{k}", str(k)) for a in METHODS[method]]
    out = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return [r["doc_id"] for r in json.loads(out.stdout).get("results", [])]
    except Exception:
        return []

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--methods", default="lexical,dense,hybrid")
    ap.add_argument("--file", default="data/eval_queries.json")
    args = ap.parse_args()
    global QUERIES
    QUERIES = json.loads((REPO / args.file).read_text(encoding="utf-8"))
    methods = [m for m in args.methods.split(",") if m in METHODS]
    agg = {m: {"hit": 0, "rr": 0.0} for m in methods}
    misses = {m: [] for m in methods}
    for item in QUERIES:
        q, exp = item["q"], item["expect"]
        for m in methods:
            docs = run(m, q, args.k)
            rank = next((i for i, d in enumerate(docs) if exp in d), None)
            if rank is not None:
                agg[m]["hit"] += 1; agg[m]["rr"] += 1.0 / (rank + 1)
            else:
                misses[m].append(q)
    n = len(QUERIES)
    print(f"\nRetrieval eval - {n} Polish queries, k={args.k}\n" + "-" * 46)
    print(f"{'method':10} {'Recall@'+str(args.k):>10} {'MRR':>8}")
    for m in methods:
        print(f"{m:10} {agg[m]['hit']/n:>10.2%} {agg[m]['rr']/n:>8.3f}")
    for m in methods:
        if misses[m]:
            print(f"\n{m} missed ({len(misses[m])}):")
            for q in misses[m]: print(f"  - {q}")

if __name__ == "__main__":
    main()
