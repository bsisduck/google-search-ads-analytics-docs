#!/usr/bin/env python3
"""
Persistent model daemon for google-search-ads-analytics-docs: loads the embedding model and the
cross-encoder reranker ONCE and serves them over localhost HTTP, so hybrid.py /
vec_search.py answer in ~100-300ms instead of paying a ~10s cold start per call.

Start it (leave running):
    .venv/bin/python3 scripts/serve_models.py
It writes the chosen port to .claude/skills/google-search-ads-analytics-docs/vec/.daemon.json.

Endpoints:
    GET  /health            -> {"ok": true, ...}
    POST /embed   {"texts":[...], "prefix":"query: "} -> {"vectors":[[...]]}
    POST /rerank  {"query":"...", "passages":[...]}   -> {"scores":[...]}
"""
import json, os, socket
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VEC = REPO / ".claude/skills/google-search-ads-analytics-docs/vec"
EMBED_MODEL = json.loads((VEC / "meta.json").read_text())["model"] if (VEC / "meta.json").exists() else "intfloat/multilingual-e5-small"
RERANKER = "BAAI/bge-reranker-v2-m3"

print(f"loading embed={EMBED_MODEL} + reranker={RERANKER} …", flush=True)
from sentence_transformers import SentenceTransformer, CrossEncoder
_embed = SentenceTransformer(EMBED_MODEL)
_rerank = CrossEncoder(RERANKER)
print("models loaded", flush=True)

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def _send(self, obj, code=200):
        b = json.dumps(obj).encode()
        self.send_response(code); self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        if self.path == "/health":
            self._send({"ok": True, "embed": EMBED_MODEL, "reranker": RERANKER})
        else:
            self._send({"error": "not found"}, 404)
    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        req = json.loads(self.rfile.read(n) or b"{}")
        if self.path == "/embed":
            texts = [req.get("prefix", "") + t for t in req["texts"]]
            v = _embed.encode(texts, normalize_embeddings=True).tolist()
            self._send({"vectors": v})
        elif self.path == "/rerank":
            pairs = [[req["query"], p] for p in req["passages"]]
            scores = [float(s) for s in _rerank.predict(pairs)]
            self._send({"scores": scores})
        else:
            self._send({"error": "not found"}, 404)

def free_port(start=8900, end=8999):
    for p in range(start, end + 1):
        with socket.socket() as s:
            if s.connect_ex(("127.0.0.1", p)) != 0:
                return p
    raise SystemExit("no free port")

def daemon_files():
    # project copy + global skill copy (so both project and global skills find it)
    files = [VEC / ".daemon.json", Path.home() / ".claude/skills/google-search-ads-analytics-docs/vec/.daemon.json"]
    return [f for f in files if f.parent.exists()]

def main():
    port = free_port()
    VEC.mkdir(parents=True, exist_ok=True)
    payload = json.dumps({"port": port, "pid": os.getpid()})
    for f in daemon_files():
        try: f.write_text(payload)
        except OSError: pass
    print(f"serving on http://127.0.0.1:{port}  (Ctrl+C to stop)", flush=True)
    try:
        ThreadingHTTPServer(("127.0.0.1", port), H).serve_forever()
    finally:
        for f in daemon_files():
            try: f.unlink()
            except OSError: pass

if __name__ == "__main__":
    main()
