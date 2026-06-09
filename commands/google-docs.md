---
description: Answer a question from the local Google docs knowledge base (Search/SEO, Search Console, Ads, GA4) with citations to the original source_url.
argument-hint: "[your question]"
---

Answer this from the Google docs knowledge base: **$ARGUMENTS**

Use the `google-search-ads-analytics-docs` skill:

1. Retrieve - `hybrid.py "$ARGUMENTS"` (best), or `search.py "$ARGUMENTS"` (stdlib, no venv).
2. Read the top 1-5 matched files whole.
3. Answer concisely and cite the Google `source_url` for every claim. Quote tables and code (JSON-LD, gtag) verbatim.

For a multi-part or research-style question, run the bundled `docs-research` workflow (decompose -> retrieve -> verify claims -> synthesize). The corpus is Polish; English questions work cross-lingually.
