#!/usr/bin/env python3
"""
Google Scanner - page signal extractor.
Fetches a URL (Scrapling, browser-impersonating) OR reads a LOCAL .html file and
emits a single JSON snapshot of every SEO / structured-data / page-experience /
tagging signal an audit agent needs. Deterministic; no judgment here.

Usage:
    python3 fetch_page.py "https://example.com/page"
    python3 fetch_page.py app/index.html               # local file in the repo
    python3 fetch_page.py app/index.html --out snap.json
"""
import argparse, json, os, re, sys
from urllib.parse import urlparse

try:
    from scrapling.fetchers import Fetcher
    from scrapling.parser import Selector
except Exception as e:  # pragma: no cover
    print(json.dumps({"error": f"scrapling import failed: {e}"})); sys.exit(1)


class LocalPage:
    """Adapter so a local HTML file exposes the same surface as a Response."""
    def __init__(self, path):
        self.body = open(path, encoding="utf-8", errors="replace").read()
        self._sel = Selector(self.body)
        self.status = "local-file"
        self.url = os.path.abspath(path)
        self.headers = {}
    def css(self, sel):
        return self._sel.css(sel)


def get(url, timeout=45):
    return Fetcher.get(url, timeout=timeout, stealthy_headers=True)


def is_remote(target):
    return target.startswith(("http://", "https://"))


def load(target):
    if is_remote(target):
        return get(target), False
    path = target[7:] if target.startswith("file://") else target
    return LocalPage(path), True


def first(page, sel):
    try:
        v = page.css(sel).get()
        return v.strip() if isinstance(v, str) else v
    except Exception:
        return None


def allc(page, sel):
    try:
        return [x.strip() for x in page.css(sel).getall() if isinstance(x, str) and x.strip()]
    except Exception:
        return []


def detect_tags(html):
    pat = {
        "ga4_gtag": r"gtag/js\?id=G-[A-Z0-9]+|gtag\('config',\s*'G-[A-Z0-9]+'",
        "ga4_id": r"G-[A-Z0-9]{6,}",
        "gtm": r"GTM-[A-Z0-9]+",
        "google_ads_conversion": r"AW-[0-9]+",
        "universal_analytics": r"UA-[0-9]+-[0-9]+",
        "floodlight": r"DC-[0-9]+",
        "google_tag": r"googletagmanager\.com/gtag/js",
    }
    out = {}
    for k, p in pat.items():
        m = re.findall(p, html)
        out[k] = sorted(set(m))[:5] if m else []
    return out


def jsonld(page, html):
    blocks = []
    for raw in allc(page, 'script[type="application/ld+json"]::text') or re.findall(
            r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', html, re.S | re.I):
        raw = raw.strip()
        try:
            data = json.loads(raw)
            items = data if isinstance(data, list) else [data]
            for it in items:
                if isinstance(it, dict):
                    t = it.get("@type")
                    blocks.append({"type": t, "valid": True,
                                   "keys": list(it.keys())[:12]})
        except Exception:
            blocks.append({"type": None, "valid": False,
                           "error": "JSON parse failed", "sample": raw[:120]})
    return blocks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--out")
    args = ap.parse_args()

    snap = {"requested_url": args.url}
    try:
        page, is_local = load(args.url)
    except Exception as e:
        snap["error"] = f"load failed: {e}"
        emit(snap, args.out); return

    html = page.body if isinstance(page.body, str) else (
        page.body.decode("utf-8", "replace") if page.body else "")
    headers = {k.lower(): v for k, v in dict(page.headers or {}).items()}
    final_url = str(page.url)
    pr = urlparse(final_url if not is_local else "file://local")

    # headings
    h1 = allc(page, "h1::text")
    outline = []
    for lvl in range(1, 4):
        for t in allc(page, f"h{lvl}::text"):
            outline.append({"level": lvl, "text": t[:90]})

    # images / alt
    imgs = []
    try:
        imgs = page.css("img")
    except Exception:
        imgs = []
    n_img = len(imgs)
    n_noalt = 0
    for im in imgs:
        try:
            a = im.attrib.get("alt")
        except Exception:
            a = None
        if not a:
            n_noalt += 1

    # hreflang
    hreflang = []
    try:
        for ln in page.css('link[rel="alternate"]'):
            hl = ln.attrib.get("hreflang")
            if hl:
                hreflang.append({"hreflang": hl, "href": ln.attrib.get("href")})
    except Exception:
        pass

    title = first(page, "title::text")
    meta_desc = None
    canonical = None
    meta_robots = None
    viewport = None
    og = {}
    try:
        for m in page.css("meta"):
            name = (m.attrib.get("name") or m.attrib.get("property") or "").lower()
            content = m.attrib.get("content")
            if name == "description":
                meta_desc = content
            elif name == "robots":
                meta_robots = content
            elif name == "viewport":
                viewport = content
            elif name.startswith("og:"):
                og[name] = content
    except Exception:
        pass
    try:
        for ln in page.css('link[rel="canonical"]'):
            canonical = ln.attrib.get("href"); break
    except Exception:
        pass

    body_text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))
    word_count = len(body_text.split())

    # robots.txt
    robots = {"fetched": False}
    if is_local:
        robots = {"fetched": False, "note": "local file - robots.txt is a deployment concern"}
    else:
      try:
        r = get(f"{pr.scheme}://{pr.netloc}/robots.txt", timeout=20)
        rb = r.body if isinstance(r.body, str) else (r.body.decode("utf-8", "replace") if r.body else "")
        robots = {
            "fetched": True, "status": getattr(r, "status", None),
            "has_sitemap": bool(re.search(r"(?im)^\s*sitemap:", rb)),
            "sitemaps": re.findall(r"(?im)^\s*sitemap:\s*(\S+)", rb)[:5],
            "disallows": re.findall(r"(?im)^\s*disallow:\s*(\S+)", rb)[:20],
            "blocks_all": bool(re.search(r"(?is)user-agent:\s*\*\s*disallow:\s*/\s*$", rb)),
        }
      except Exception as e:
        robots = {"fetched": False, "error": str(e)[:120]}

    snap.update({
        "final_url": final_url,
        "status": getattr(page, "status", None),
        "https": (None if is_local else pr.scheme == "https"),
        "is_local": is_local,
        "redirected": (False if is_local else final_url.split("?")[0] != args.url.split("?")[0]),
        "headers": {k: headers.get(k) for k in
                    ["content-type", "x-robots-tag", "cache-control",
                     "strict-transport-security", "content-encoding", "server"]},
        "title": title, "title_len": len(title) if title else 0,
        "meta_description": meta_desc, "meta_description_len": len(meta_desc) if meta_desc else 0,
        "meta_robots": meta_robots,
        "canonical": canonical,
        "viewport": viewport, "mobile_viewport": bool(viewport and "width=device-width" in viewport),
        "lang": (first(page, "html::attr(lang)") or None),
        "h1": h1, "h1_count": len(h1),
        "heading_outline": outline[:40],
        "word_count": word_count,
        "images": {"total": n_img, "missing_alt": n_noalt},
        "hreflang": hreflang,
        "open_graph": og,
        "structured_data": jsonld(page, html),
        "tags": detect_tags(html),
        "robots_txt": robots,
        "html_bytes": len(html),
    })
    emit(snap, args.out)


def emit(snap, out):
    s = json.dumps(snap, ensure_ascii=False, indent=2)
    if out:
        open(out, "w", encoding="utf-8").write(s)
        print(f"wrote {out} ({len(s)} bytes)")
    else:
        print(s)


if __name__ == "__main__":
    main()
